using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI; // For UI elements

public class Player : MonoBehaviour
{
    public int lives = 3;
    public Transform groundCheck;
    public LayerMask groundLayer;
    public LayerMask enemyLayer;
    public LayerMask waterLayer;
    private bool isGrounded;
    private Rigidbody2D rb;
    public Text livesText; // Reference to the UI text element

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        UpdateLivesUI();
    }

    void Update()
    {
        Move();
        Jump();
        CheckGround();
    }

    void Move()
    {
        float horizontal = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(horizontal * 5f, rb.velocity.y);
    }

    void Jump()
    {
        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            rb.velocity = new Vector2(rb.velocity.x, 10f);
        }
    }

    void CheckGround()
    {
        isGrounded = Physics2D.OverlapCircle(groundCheck.position, 0.2f, groundLayer);
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.gameObject.layer == LayerMask.NameToLayer("Enemy") || other.gameObject.layer == LayerMask.NameToLayer("Water"))
        {
            LoseLife();
        }
    }

    void LoseLife()
    {
        lives--;
        UpdateLivesUI();

        if (lives <= 0)
        {
            GameOver();
        }
        else
        {
            // Respawn logic, e.g., move the player to a safe position
            transform.position = new Vector3(0, 0, 0); // Example respawn position
        }
    }

    void UpdateLivesUI()
    {
        livesText.text = "Lives: " + lives;
    }

    void GameOver()
    {
        // Reload the current scene or go to game over screen
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
}
