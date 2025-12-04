using UnityEngine;

public class FreeCamera : MonoBehaviour
{
    public float moveSpeed = 10f;
    public float fastSpeed = 30f;
    public float mouseSensitivity = 3f;

    float rotationX = 0f;
    float rotationY = 0f;

    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked;
    }

    void Update()
    {
        // --- ROTACIÓN CON EL MOUSE ---
        rotationX += Input.GetAxis("Mouse X") * mouseSensitivity;   // <- cambiado (+)
        rotationY -= Input.GetAxis("Mouse Y") * mouseSensitivity;
        rotationY = Mathf.Clamp(rotationY, -85f, 85f);

        transform.localRotation = Quaternion.Euler(rotationY, rotationX, 0);

        // --- MOVIMIENTO ---
        float speed = Input.GetKey(KeyCode.LeftShift) ? fastSpeed : moveSpeed;

        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");

        Vector3 direction = transform.forward * vertical + transform.right * horizontal;

        if (Input.GetKey(KeyCode.E)) direction += transform.up;
        if (Input.GetKey(KeyCode.Q)) direction -= transform.up;

        transform.position += direction * speed * Time.deltaTime;
    }
}
