CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    creator_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    activity VARCHAR(100) NOT NULL,
    max_participants INTEGER NOT NULL,
    is_public BOOLEAN NOT NULL DEFAULT 1,
    description TEXT,
    event_date TIMESTAMP ,
    current_participants INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (creator_id) REFERENCES users(id) ON DELETE CASCADE
);

