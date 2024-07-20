-- create_table.sql
CREATE TABLE energy_data (
  id SERIAL PRIMARY KEY,
  timestamp TIMESTAMP NOT NULL,
  energy_usage REAL NOT NULL,
  energy_production REAL NOT NULL
);

-- insert_data.sql
INSERT INTO energy_data (timestamp, energy_usage, energy_production)
VALUES ('2024-07-20 12:00:00', 100, 200);
