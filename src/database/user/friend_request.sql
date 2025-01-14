CREATE TABLE friend_request
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    from_user_id INTEGER NOT NULL,
    to_user_id   INTEGER NOT NULL,
    status       TEXT DEFAULT 'pending',
    FOREIGN KEY (from_user_id) REFERENCES users (id),
    FOREIGN KEY (to_user_id) REFERENCES users (id),
    CONSTRAINT unique_request UNIQUE (from_user_id, to_user_id)
);

INSERT INTO friend_request (from_user_id, to_user_id)
VALUES (3, 4);

DROP TABLE friend_request;