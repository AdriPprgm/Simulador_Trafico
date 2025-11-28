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
    public GameObject carroPrefab;
    public GameObject semaforo1Prefab;
    public GameObject semaforo2Prefab;
    public GameObject callePrefab;
    public GameObject buildingPrefab;
    public GameObject estacionamientoPrefab;

    // Diccionario local para mantener referencia de los objetos instanciados
    private Dictionary<int, GameObject> unityAgents = new Dictionary<int, GameObject>();

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
                GameObject prefab = GetPrefabForType(agentType, agentData);
                
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
            Vector3 targetPosition = new Vector3(x, 0, y);
            unityAgents[id].transform.position = targetPosition;

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
            Debug.Log($"Agente {id} removido (estacionado)");
        }
    }

    GameObject GetPrefabForType(string agentType, JToken agentData)
    {
        switch (agentType)
        {
            case "Carro":
                return carroPrefab;
            case "Semaforo1":
                return semaforo1Prefab;
            case "Semaforo2":
                return semaforo2Prefab;
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
                // Cambiar color del semáforo
                var lightRenderer = agent.GetComponent<Renderer>();
                if (lightRenderer != null)
                {
                    lightRenderer.material.color = avanza ? Color.green : Color.red;
                }
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
    }

    private async void OnApplicationQuit()
    {
        if (ws != null) await ws.Close();
    }
}
