using UnityEngine;

public class Crystal : MonoBehaviour
{
    // Reference to the gate that will be unlocked
    public Gate gate;

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            // Unlock the gate
            if (gate != null)
            {
                gate.UnlockGate();
            }

            // Destroy the crystal
            Destroy(gameObject);
        }
    }
}
