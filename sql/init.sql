CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    message VARCHAR(255) NOT NULL
);

INSERT INTO messages (message)
VALUES ('Data berhasil dibaca dari PostgreSQL');