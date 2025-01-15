CREATE TABLE FriendRequest
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    from_user_id INTEGER NOT NULL,
    to_user_id   INTEGER NOT NULL,
    status       TEXT DEFAULT 'pending',
    FOREIGN KEY (from_user_id) REFERENCES users (id),
    FOREIGN KEY (to_user_id) REFERENCES users (id),
    CONSTRAINT unique_request UNIQUE (from_user_id, to_user_id)
);


INSERT INTO FriendRequest (from_user_id, to_user_id)
VALUES (3, 4);


CREATE TABLE Friends
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    from_user_id INTEGER NOT NULL,
    to_user_id   INTEGER NOT NULL,
    status       TEXT DEFAULT 'friends',
    FOREIGN KEY (from_user_id) REFERENCES users (id),
    FOREIGN KEY (to_user_id) REFERENCES users (id),
    CONSTRAINT unique_friendship UNIQUE (from_user_id, to_user_id)
);

INSERT INTO Friends (from_user_id, to_user_id)
VALUES (1, 4),
       (1, 4);
