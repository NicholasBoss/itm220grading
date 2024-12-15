-- ~
-- SET GLOBAL validate_password.length=5;
-- ~
-- ~
CREATE USER IF NOT EXISTS 'student'@'localhost' IDENTIFIED BY 'student';
-- ~
-- ~
GRANT ALL ON airportdb.* TO 'student'@'localhost';
-- ~
