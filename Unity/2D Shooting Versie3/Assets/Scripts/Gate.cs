using UnityEngine;

public class Gate : MonoBehaviour
{
    private bool isUnlocked = false;

    public void UnlockGate()
    {
        isUnlocked = true;
        // Here you can add an animation or change the sprite to show the gate is open
        gameObject.SetActive(false); // Example: deactivate the gate object to open it
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (isUnlocked && other.CompareTag("Player"))
        {
            // Allow the player to pass through
            // In this example, we just deactivate the gate, so the player can walk through it
        }
    }
}
