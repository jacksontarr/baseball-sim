DROP TABLE IF EXISTS teams;

CREATE TABLE teams(
    id              SERIAL PRIMARY KEY,
    loc             TEXT NOT NULL,
    nickname        TEXT NOT NULL,
    wins            INTEGER DEFAULT 0,
    losses          INTEGER DEFAULT 0,
    games_played    INTEGER DEFAULT 0
);