CREATE DATABASE IF NOT EXISTS hostel_food;

USE hostel_food;

-- Create user only if it does not exist
CREATE USER IF NOT EXISTS 'hostel_user'@'localhost' IDENTIFIED BY 'password123';

GRANT ALL PRIVILEGES ON hostel_food.* TO 'hostel_user'@'localhost';
FLUSH PRIVILEGES;
