DROP TABLE IF EXISTS teams;

CREATE TABLE teams(
    id              SERIAL PRIMARY KEY,
    loc             TEXT NOT NULL,
    nickname        TEXT NOT NULL,
    season_wins     INTEGER DEFAULT 0,
    season_losses   INTEGER DEFAULT 0,
    total_wins      INTEGER DEFAULT 0,
    total_losses    INTEGER DEFAULT 0,
);