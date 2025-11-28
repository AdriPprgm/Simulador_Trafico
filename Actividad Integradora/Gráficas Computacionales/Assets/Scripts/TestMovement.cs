using UnityEngine;

public class TestMovement : MonoBehaviour
{
    public MesaSync mesaSync;
    
    [Header("Configuración de Simulación")]
    public bool autoStart = true;

    void Start()
    {
        if (autoStart && mesaSync != null)
        {
            Debug.Log("Simulación iniciada automáticamente");
            mesaSync.SendCommandToMesa("resume");
        }
        else if (mesaSync == null)
        {
            Debug.LogError("MesaSync no está asignado en TestMovement");
        }
    }
}
