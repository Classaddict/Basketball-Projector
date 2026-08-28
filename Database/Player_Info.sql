DROP TABLE IF EXISTS Player_Info;
CREATE TABLE IF NOT EXISTS Player_Info(
    player_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(50),
    team INT NOT NULL,
    position INT NOT NULL,
    FOREIGN KEY (team) REFERENCES Teams(team_id) 
);

