-- init.sql
CREATE USER 'admin'@'%' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';

