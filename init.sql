-- Create a users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    pwd TEXT NOT NULL,
    userrole varchar(255),
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert a default admin user
INSERT INTO users (username, email, pwd,userrole) 
VALUES ('umais', 'umais.siddiqui@harriscountytx.gov', '$2b$12$QdaoxCLuDsApxz6wpRoA7OhN2aE6foVQ.oWa31qqDhfIan2u304mO','admin') 
ON CONFLICT (email) DO NOTHING;

CREATE TABLE IF NOT EXISTS Applications (
     id SERIAL PRIMARY KEY,
     ApplicationName VARCHAR(255),
     ApplicationType VARCHAR(255),
     ApplicationSecret VARCHAR(255),
     ApplicationID VARCHAR(255),
     date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP


)

CREATE TABLE IF NOT EXISTS UserApplications (
     id SERIAL PRIMARY KEY,
     UserId int,
     ApplicationId int ,
     ApplicationID VARCHAR(255),
     date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP


)


CREATE TABLE IF NOT EXISTS Organizations (
     id SERIAL PRIMARY KEY,
     UserId int,
     OrganizationName varchar(255) ,
     OrganizationAddress TEXT,
     OrganizationPhoneNumber varchar(50),
     OrganizationLogoURL varchar(255),
     OrganizationHeader varchar(255),
     date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP


)

