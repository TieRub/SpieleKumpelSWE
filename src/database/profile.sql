CREATE TABLE profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    display_name VARCHAR(50),
    about_me TEXT,
    profile_picture TEXT DEFAULT 'assets/profile_picture/pp001.png',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

DROP TABLE profiles;