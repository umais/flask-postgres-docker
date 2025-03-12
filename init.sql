-- Create a users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    pwd TEXT NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert a default admin user
INSERT INTO users (username, email, pwd) 
VALUES ('umais', 'umais.siddiqui@harriscountytx.gov', '$2b$12$QdaoxCLuDsApxz6wpRoA7OhN2aE6foVQ.oWa31qqDhfIan2u304mO') 
ON CONFLICT (email) DO NOTHING;

CREATE TABLE IF NOT EXISTS Applications (
     id SERIAL PRIMARY KEY,
     ApplicationName VARCHAR(255),
     ApplicationType VARCHAR(255),
     date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP


)