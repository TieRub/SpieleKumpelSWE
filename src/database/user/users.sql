-- Create users
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    profile_picture VARCHAR(255) DEFAULT '',
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