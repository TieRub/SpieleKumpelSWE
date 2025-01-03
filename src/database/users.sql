CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    profile_picture TEXT DEFAULT '/html/assets/default-profile.png'
);

INSERT INTO users (email, username, password, profile_picture) VALUES
('Steven@example.com', 'TieRub', 'password123', '/html/assets/tierub.png'),
('Marcel@example.com', 'Matzel', 'password456', '/html/assets/matzel.png'),
('Victoria@example.com', 'Marshila', 'password789', '/html/assets/marshila.png'),
('kenneth@example.com', 'Helistormer', 'password789', '/html/assets/helistormer.png');