using UnityEngine;
using NativeWebSocket;
using Newtonsoft.Json.Linq;
using System.Collections.Generic;
using System.Text;

public class MesaSync : MonoBehaviour
{
    WebSocket ws;

    [Header("Configuración de Conexión")]
    public string serverUrl = "ws://localhost:8765";

    [Header("Prefabs por Tipo de Agente")]
    public GameObject[] carroPrefabs; // Ahora es un array
    public GameObject semaforo1Prefab;
    public GameObject semaforo2Prefab;
    public GameObject callePrefab;
    public GameObject buildingPrefab;
    public GameObject estacionamientoPrefab;
    public GameObject camionPrefab;

    // Diccionario local para mantener referencia de los objetos instanciados
    private Dictionary<int, GameObject> unityAgents = new Dictionary<int, GameObject>();

    // Diccionario para guardar la posición anterior de cada carro
    private Dictionary<int, Vector3> previousPositions = new Dictionary<int, Vector3>();

    // Posición actual y futura
    private Dictionary<int, Vector3> movementTargets = new Dictionary<int, Vector3>();
    private Dictionary<int, float> movementTimers = new Dictionary<int, float>();

    // Rotación suave insana
    private Dictionary<int, Quaternion> previousRotations = new Dictionary<int, Quaternion>();
    private Dictionary<int, Quaternion> rotationTargets = new Dictionary<int, Quaternion>();
    private Dictionary<int, float> rotationTimers = new Dictionary<int, float>();

    // Diccionario para recordar qué prefab se usó para cada carro
    private Dictionary<int, int> carPrefabIndices = new Dictionary<int, int>();


    async void Start()
    {
        ws = new WebSocket(serverUrl);

        ws.OnOpen += () => Debug.Log("Conexión establecida con Mesa.");
        ws.OnError += (e) => Debug.LogError("Error en WebSocket: " + e);
        ws.OnClose += (e) => Debug.Log("Conexión cerrada: " + e);

        ws.OnMessage += (bytes) =>
        {
            string message = Encoding.UTF8.GetString(bytes);

            try
            {
                JObject json = JObject.Parse(message);

                if ((string)json["type"] == "update")
                {
                    JArray agentsData = (JArray)json["agents"];
                    UpdateUnityScene(agentsData);
                }
            }
            catch (System.Exception ex)
            {
                Debug.LogWarning("Error procesando JSON: " + ex.Message);
            }
        };

        await ws.Connect();
    }

    void UpdateUnityScene(JArray mesaAgents)
    {
        HashSet<int> activeAgents = new HashSet<int>();

        foreach (var agentData in mesaAgents)
        {
            int id = (int)agentData["id"];
            float x = (float)agentData["x"];
            float y = (float)agentData["y"];
            string agentType = (string)agentData["type"];

            activeAgents.Add(id);

            // Si el agente no existe en Unity, lo creamos
            if (!unityAgents.ContainsKey(id))
            {
                GameObject prefab = GetPrefabForType(agentType, agentData, id);

                if (prefab != null)
                {
                    GameObject newAgent = Instantiate(prefab);
                    newAgent.name = $"{agentType}_{id}";
                    unityAgents[id] = newAgent;

                    // Configurar propiedades específicas
                    ConfigureAgent(newAgent, agentType, agentData);
                }
                else
                {
                    Debug.LogWarning($"No hay prefab asignado para tipo: {agentType}");
                    continue;
                }
            }

            // Actualizamos la posición (Mesa usa Y, Unity usa Z para el plano)
            Vector3 targetPosition = new Vector3(x, 0, 23-y);

            // Rotar el carro hacia la dirección del movimiento
            if (agentType == "Carro" || agentType == "Camion")
            {
                if (previousPositions.ContainsKey(id))
                {
                    Vector3 direction = targetPosition - previousPositions[id];

                    if (direction.magnitude > 0.01f)
                    {
                        float angle = 0f;

                        if (Mathf.Abs(direction.x) > Mathf.Abs(direction.z))
                            angle = direction.x > 0 ? 90f : -90f;
                        else
                            angle = direction.z > 0 ? 0f : 180f;

                        rotationTargets[id] = Quaternion.Euler(0, angle, 0);
                        rotationTimers[id] = 0f;
                    }
                }
            }

            movementTargets[id] = targetPosition;
            movementTimers[id] = 0f; // reiniciar el temporizador de animación

            // Actualizar propiedades específicas del agente
            UpdateAgentProperties(unityAgents[id], agentType, agentData);
        }

        // Eliminar agentes que ya no existen en Mesa (carros estacionados)
        List<int> toRemove = new List<int>();
        foreach (var kvp in unityAgents)
        {
            if (!activeAgents.Contains(kvp.Key))
            {
                toRemove.Add(kvp.Key);
            }
        }

        foreach (int id in toRemove)
        {
            Destroy(unityAgents[id]);
            unityAgents.Remove(id);
            carPrefabIndices.Remove(id); // Limpiar también el índice del prefab
            previousPositions.Remove(id);
            movementTargets.Remove(id);
            movementTimers.Remove(id);
            previousRotations.Remove(id);
            rotationTargets.Remove(id);
            rotationTimers.Remove(id);
            Debug.Log($"Agente {id} removido (estacionado)");
        }
    }

    GameObject GetPrefabForType(string agentType, JToken agentData, int id)
    {
        switch (agentType)
        {
            case "Carro":
                // Si ya tenemos un prefab asignado para este carro, usarlo
                if (carPrefabIndices.ContainsKey(id))
                {
                    return carroPrefabs[carPrefabIndices[id]];
                }

                // Si es nuevo, asignar un prefab aleatorio
                if (carroPrefabs != null && carroPrefabs.Length > 0)
                {
                    int randomIndex = Random.Range(0, carroPrefabs.Length);
                    carPrefabIndices[id] = randomIndex;
                    return carroPrefabs[randomIndex];
                }

                Debug.LogWarning("No hay prefabs de carro asignados en el array");
                return null;

            case "Semaforo1":
                return semaforo1Prefab;
            case "Semaforo2":
                return semaforo2Prefab;
            case "Camion":
                return camionPrefab;
            case "AgenteCalle":
                // Diferenciar entre calle, building y estacionamiento
                bool isBuilding = agentData["isBuilding"] != null ? (bool)agentData["isBuilding"] : false;
                bool isEstacionamiento = agentData["isEstacionamiento"] != null ? (bool)agentData["isEstacionamiento"] : false;

                if (isBuilding)
                    return buildingPrefab;
                else if (isEstacionamiento)
                    return estacionamientoPrefab;
                else
                    return callePrefab;
            default:
                return null;
        }
    }

    void ConfigureAgent(GameObject agent, string agentType, JToken agentData)
    {
        // Configuración inicial específica por tipo
        switch (agentType)
        {
            case "Carro":
                // Añadir componente de movimiento suave si lo deseas
                agent.tag = "Car";
                break;
            case "Semaforo1":
            case "Semaforo2":
                agent.tag = "TrafficLight";
                break;
            case "AgenteCalle":
                agent.tag = "Road";
                bool isBuilding = agentData["isBuilding"] != null ? (bool)agentData["isBuilding"] : false;
                if (isBuilding)
                    agent.tag = "Building";
                break;
            case "Camion":
                agent.tag = "Camion";
                break;
        }
    }

    void UpdateAgentProperties(GameObject agent, string agentType, JToken agentData)
    {
        // Actualizar propiedades dinámicas
        switch (agentType)
        {
            case "Carro":
                bool estacionado = agentData["estacionado"] != null ? (bool)agentData["estacionado"] : false;
                // Cambiar color o material si está estacionado
                if (estacionado)
                {
                    var renderer = agent.GetComponent<Renderer>();
                    if (renderer != null)
                        renderer.material.color = Color.gray;
                }
                break;

            case "Semaforo1":
            case "Semaforo2":
                bool avanza = agentData["avanza"] != null ? (bool)agentData["avanza"] : false;

                SemaforoSync sem = agent.GetComponent<SemaforoSync>();
                if (sem != null)
                    sem.UpdateSemaforo(avanza);

                break;
            case "Camion":
                bool camionEstacionado = agentData["estacionado"] != null ? (bool)agentData["estacionado"] : false;
                break;
        }
    }

    // Método para enviar comandos a Mesa
    public async void SendCommandToMesa(string command)
    {
        if (ws.State == WebSocketState.Open)
        {
            JObject payload = new JObject
            {
                ["type"] = command
            };

            await ws.SendText(payload.ToString());
        }
    }

void Update()
{
#if !UNITY_WEBGL || UNITY_EDITOR
    ws?.DispatchMessageQueue();
#endif

    // Movimiento suave
    foreach (var kvp in movementTargets)
    {
        int id = kvp.Key;

        if (!unityAgents.ContainsKey(id))
            continue;

        GameObject agent = unityAgents[id];

        Vector3 startPos = previousPositions.ContainsKey(id) ?
                           previousPositions[id] :
                           agent.transform.position;

        Vector3 targetPos = movementTargets[id];

        movementTimers[id] += Time.deltaTime;
        float t = movementTimers[id] / 0.5f;  // duración ahora = 0.5 segundos
        t = Mathf.Clamp01(t);

        agent.transform.position = Vector3.Lerp(startPos, targetPos, t);

        // cuando termina, guardar nueva posición como anterior
        if (t >= 1f)
        {
            previousPositions[id] = targetPos;
        }
    }

    // Rotación suave
    foreach (var kvp in rotationTargets)
    {
        int id = kvp.Key;

        if (!unityAgents.ContainsKey(id))
            continue;

        GameObject agent = unityAgents[id];

        Quaternion startRot = previousRotations.ContainsKey(id) ?
                              previousRotations[id] :
                              agent.transform.rotation;

        Quaternion targetRot = rotationTargets[id];

        rotationTimers[id] += Time.deltaTime;
        float tRot = rotationTimers[id] / 0.5f;   // duración ahora = 0.5 segundos
        tRot = Mathf.Clamp01(tRot);

        agent.transform.rotation = Quaternion.Lerp(startRot, targetRot, tRot);

        if (tRot >= 1f)
            previousRotations[id] = targetRot;
    }
}


    private async void OnApplicationQuit()
    {
        if (ws != null) await ws.Close();
    }
}
