using UnityEngine;

public class DayNightCycle : MonoBehaviour
{
    [Range(0, 24)]
    public float timeOfDay = 12f; // Hora actual (0 = medianoche, 12 = mediodía)
    public float daySpeed = 1f;    // Qué tan rápido pasa el tiempo

    public Light sun;              // Tu Directional Light del "Sol"
    public Gradient lightColor;    // Colores según la hora
    public AnimationCurve lightIntensity; // Intensidad según la hora

    void Update()
    {
        // Avanza el tiempo
        timeOfDay += Time.deltaTime * daySpeed;
        if (timeOfDay > 24f) timeOfDay -= 24f;

        // Calcula un valor normalizado (0–1) según la hora
        float t = timeOfDay / 24f;

        // Rota el Sol (360° en 24 horas)
        transform.rotation = Quaternion.Euler(t * 360f - 90f, 170f, 0f);

        // Color dinámico
        sun.color = lightColor.Evaluate(t);

        // Intensidad dinámica
        sun.intensity = lightIntensity.Evaluate(t);
    }
}
