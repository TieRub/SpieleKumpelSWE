CREATE TABLE events
(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    creator_id      INTEGER NOT NULL,
    name            STRING NOT NULL,
    max_mitglieder  INTEGER NOT NULL,
    oefentlich          BOOLEAN,
    description     STRING,
    datum           DATE,
    mitglieder      LIST,
    aktuelle_anzahl Integer NOT NULL,
    FOREIGN KEY (mitglieder) REFERENCES users (username),
    FOREIGN KEY (creator_id) REFERENCES users (id),
    CONSTRAINT unique_events UNIQUE (mitglieder, id)
);

INSERT INTO events (creator_id, name, max_mitglieder, oefentlich, description, datum, aktuelle_anzahl)
VALUES (2, 'SUPER KRASSES Event', 4, 1, 'YOLO', NULL, 1),
       (4, 'S-Tier Event', 4, 1, 'auf Lock', 2055 - 01 - 08, 1);

DROP TABLE events;