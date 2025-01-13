-- Users Table
CREATE TABLE users
(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    email           TEXT    NOT NULL UNIQUE,
    username        TEXT    NOT NULL UNIQUE,
    password        TEXT    NOT NULL,
    profile_picture TEXT DEFAULT '/html/assets/default-profile.png',
    event_join_id   INTEGER NOT NULL,
    FOREIGN KEY (event_join_id) REFERENCES Events (id)
);


INSERT INTO users (email, username, password, profile_picture)
VALUES ('Steven@example.com', 'TieRub', 'password123', '/html/assets/tierub.png'),
       ('Marcel@example.com', 'Matzel', 'password456', '/html/assets/matzel.png'),
       ('Victoria@example.com', 'Marshila', 'password789', '/html/assets/marshila.png'),
       ('kenneth@example.com', 'Helistormer', 'password789', '/html/assets/helistormer.png');


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
VALUES (1, 3),
       (1, 2);

CREATE TABLE Events
(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    creator_id      INTEGER NOT NULL,
    name            STRING  NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES users (id),
    event_picture   TEXT DEFAULT '/html/assets/default-profile.png',
    max_mitglieder  INTEGER NOT NULL,
    privat          BOOLEAN,
    description     STRING,
    datum           DATE,
    mitglieder      LIST,
    FOREIGN KEY (mitglieder) REFERENCES users (username),
    aktuelle_anzahl Integer NOT NULL,
    CONSTRAINT unique_events UNIQUE (mitglieder, id)
);


INSERT INTO Events (creator_id, name, max_mitglieder, privat, description, datum, event_picture)
VALUES (2, 'SUPER KRASSES Event', 4, 1, 'YOLO', NULL, NULL),
       (4, 'S-Tier Event', 4, 1, 'auf Lock', 2055 - 01 - 08, NULL);

