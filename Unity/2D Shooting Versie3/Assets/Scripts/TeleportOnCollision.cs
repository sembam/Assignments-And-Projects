using UnityEngine;

public class TeleportOnCollision : MonoBehaviour
{
    public Transform teleportTarget; // Set this in the Inspector to the target position

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Player"))
        {
            collision.gameObject.transform.position = teleportTarget.position;
        }
    }
}
