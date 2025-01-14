-- Create users
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert example
INSERT INTO users (username, password, email)
VALUES
('john_doe', 'password123', 'john.doe@example.com'),
('jane_smith', 'mysecurepassword', 'jane.smith@example.com'),
('alice_williams', 'alicepassword', 'alice.williams@example.com');

DROP TABLE users