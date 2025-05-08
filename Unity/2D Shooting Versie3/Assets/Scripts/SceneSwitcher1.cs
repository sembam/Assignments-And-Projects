using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneSwitcher1 : MonoBehaviour
{
    // Ensure the object has a Collider2D component with "Is Trigger" checked
    void OnTriggerEnter2D(Collider2D other)
    {
        // Check if the collider we are touching is tagged appropriately (e.g., "SwitchTrigger")
        if (other.CompareTag("SwitchTrigger"))
        {
            // Load the target scene
            SceneManager.LoadScene("Scene3"); // Replace "Scene2" with the name of your target scene
        }
    }
}
