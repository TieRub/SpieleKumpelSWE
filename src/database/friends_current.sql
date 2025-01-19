CREATE TABLE friends_current (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id_1 INTEGER NOT NULL,
    user_id_2 INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id_1) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id_2) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT unique_friendship UNIQUE(user_id_1, user_id_2)
);

DROP TABLE friends_current;