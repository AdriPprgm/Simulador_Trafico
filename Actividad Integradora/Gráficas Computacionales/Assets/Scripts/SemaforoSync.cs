using UnityEngine;

public class SemaforoSync : MonoBehaviour
{
    public Light luz;  // Apunta al Point Light del semáforo

    // Lo llamará MesaSync cada vez que llegue un update
    public void UpdateSemaforo(bool avanza)
    {
        if (luz == null) return;

        if (avanza)
        {
            luz.color = Color.green;
            luz.intensity = 5f;
        }
        else
        {
            luz.color = Color.red;
            luz.intensity = 5f;
        }
    }
}
