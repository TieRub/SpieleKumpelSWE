-- Create users
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    profile_picture VARCHAR(255) DEFAULT '{{ url_for(''static'', filename=''assets/profile_picture/pp001.png'') }}',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert example
INSERT INTO users (email, username, password, profile_picture)
VALUES
('Steven@example.com', 'TieRub', 'password123', ''),
('Marcel@example.com', 'Matzel', 'password456', '{{ url_for(''static'', filename=''assets/profile_picture/pp002.png'') }}'),
('Victoria@example.com', 'Marshila', 'password789', '{{ url_for(''static'', filename=''assets/profile_picture/pp003.png'') }}'),
('kenneth@example.com', 'Helistormer', 'password789', '{{ url_for(''static'', filename=''assets/profile_picture/pp004.png'') }}');

DROP TABLE users;