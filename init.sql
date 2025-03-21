-- Create a users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    pwd TEXT NOT NULL,
    userrole VARCHAR(255),
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert a default admin user
INSERT INTO users (username, email, pwd, userrole) 
VALUES ('umais', 'umaisabdullah@gmail.com', '$2b$12$QdaoxCLuDsApxz6wpRoA7OhN2aE6foVQ.oWa31qqDhfIan2u304mO', 'admin') 
ON CONFLICT (email) DO NOTHING;

-- Create Applications table
CREATE TABLE IF NOT EXISTS Applications (
    id SERIAL PRIMARY KEY,
    ApplicationName VARCHAR(255),
    ApplicationType VARCHAR(255),
    ApplicationSecret VARCHAR(255),
    ApplicationID VARCHAR(255),
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create UserApplications table with foreign key relationships
CREATE TABLE IF NOT EXISTS UserApplications (
    id SERIAL PRIMARY KEY,
    UserID INT,
    ApplicationId INT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (ApplicationId) REFERENCES Applications(id) ON DELETE CASCADE
);

-- Create Organizations table with foreign key relationship
CREATE TABLE IF NOT EXISTS Organizations (
    id SERIAL PRIMARY KEY,
    UserId INT,
    OrganizationName VARCHAR(255),
    OrganizationAddress TEXT,
    OrganizationPhoneNumber VARCHAR(50),
    OrganizationLogoURL VARCHAR(255),
    OrganizationHeader VARCHAR(255),
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserId) REFERENCES users(id) ON DELETE CASCADE
);
