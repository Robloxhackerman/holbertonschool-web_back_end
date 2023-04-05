-- Write a SQL script that creates a table users

CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE ,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name, country) VALUES ('bob@dylan.com', 'Bob', 'US');