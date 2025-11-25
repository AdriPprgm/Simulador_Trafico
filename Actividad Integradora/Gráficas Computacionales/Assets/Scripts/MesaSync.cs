using UnityEngine;
using NativeWebSocket;
using Newtonsoft.Json.Linq;
using System.Collections.Generic;
using System.Text;

public class MesaSync : MonoBehaviour
{
    // Dependencias:
    // 1. NativeWebSocket (Instalar desde package manager o git)
    // 2. Newtonsoft.Json (JSON.NET standard en Unity)

    WebSocket ws;

    [Header("Configuraci�n de Conexi�n")]
    public string serverUrl = "ws://localhost:8765";
    public GameObject agentPrefab; // Asigna tu cubo/esfera aqu�

    // Diccionario local para mantener referencia de los objetos instanciados
    private Dictionary<int, GameObject> unityAgents = new Dictionary<int, GameObject>();

    async void Start()
    {
        ws = new WebSocket(serverUrl);

        ws.OnOpen += () => Debug.Log("Conexi�n establecida con Mesa.");
        ws.OnError += (e) => Debug.LogError("Error en WebSocket: " + e);
        ws.OnClose += (e) => Debug.Log("Conexi�n cerrada: " + e);

        ws.OnMessage += (bytes) =>
        {
            // 1. Recibimos mensaje crudo
            string message = Encoding.UTF8.GetString(bytes);

            try
            {
                // 2. Parseamos el JSON
                JObject json = JObject.Parse(message);

                // 3. Verificamos el tipo de mensaje
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

        // Conectar
        await ws.Connect();
    }

    void UpdateUnityScene(JArray mesaAgents)
    {
        // Recorremos la lista de agentes que envi� Mesa
        foreach (var agentData in mesaAgents)
        {
            int id = (int)agentData["id"];
            // Nota: Mesa es Grid (X, Y). Unity es 3D (X, Z) generalmente.
            float x = (float)agentData["x"];
            float y = (float)agentData["y"];

            // Si el agente no existe en Unity, lo creamos
            if (!unityAgents.ContainsKey(id))
            {
                if (agentPrefab != null)
                {
                    GameObject newAgent = Instantiate(agentPrefab);
                    newAgent.name = $"Agent_{id}";
                    unityAgents[id] = newAgent;
                }
                else
                {
                    Debug.LogError("AgentPrefab no asignado en el Inspector.");
                    continue;
                }
            }

            // Actualizamos la posici�n
            // Mapeamos Y de Mesa a Z de Unity para movimiento en el plano suelo
            Vector3 targetPosition = new Vector3(x, 0, y);
            unityAgents[id].transform.position = targetPosition;
        }
    }

    // M�todo para enviar datos A Mesa (si mueves un agente en Unity)
    public async void SendUpdateToMesa(int id, int x, int y)
    {
        if (ws.State == WebSocketState.Open)
        {
            JObject payload = new JObject
            {
                ["type"] = "update",
                ["agents"] = new JArray
                {
                    new JObject { ["id"] = id, ["x"] = x, ["y"] = y }
                }
            };

            await ws.SendText(payload.ToString());
        }
    }

    void Update()
    {
        // Necesario para procesar los mensajes en el hilo principal de Unity
#if !UNITY_WEBGL || UNITY_EDITOR
        ws.DispatchMessageQueue();
#endif
    }

    private async void OnApplicationQuit()
    {
        if (ws != null) await ws.Close();
    }
}
