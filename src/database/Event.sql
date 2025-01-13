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

