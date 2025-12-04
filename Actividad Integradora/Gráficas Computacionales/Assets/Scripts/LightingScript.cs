using UnityEngine;

[System.Serializable]
[CreateAssetMenu(fileName = "LightingScript", menuName = "Scriptables/Lighting Preset", order = 1)]
public class LightingScript : ScriptableObject
{
    public Gradient AmbientColor;    // Colores según la hora
    public Gradient DirectionalColor; // Intensidad según la hora
    public Gradient FogColor;
}