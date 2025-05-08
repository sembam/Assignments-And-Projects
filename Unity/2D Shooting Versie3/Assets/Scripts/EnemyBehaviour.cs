using UnityEngine;

public class EnemyBehaviour : MonoBehaviour
{
    public int health = 3;

    void Update()
    {
        // Implement enemy behavior like movement and attack
    }

    public void TakeDamage(int damage)
    {
        health -= damage;
        if (health <= 0)
        {
            Destroy(gameObject);
        }
    }
}
