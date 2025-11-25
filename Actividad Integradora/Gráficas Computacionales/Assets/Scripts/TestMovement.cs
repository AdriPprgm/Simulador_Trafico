using UnityEngine;

public class TestMovement : MonoBehaviour
{
    public MesaSync mesaSync;
    public int myAgentID = 1; // Simularemos ser el agente 1

    // Posici�n grid
    int x = 0;
    int y = 0;

    void Update()
    {
        bool moved = false;

        if (Input.GetKeyDown(KeyCode.UpArrow)) { y++; moved = true; }
        if (Input.GetKeyDown(KeyCode.DownArrow)) { y--; moved = true; }
        if (Input.GetKeyDown(KeyCode.RightArrow)) { x++; moved = true; }
        if (Input.GetKeyDown(KeyCode.LeftArrow)) { x--; moved = true; }

        if (moved)
        {
            // Enviamos la nueva intenci�n de posici�n a Mesa
            Debug.Log($"Enviando movimiento a Mesa: {x}, {y}");
            mesaSync.SendUpdateToMesa(myAgentID, x, y);
        }
    }
}
