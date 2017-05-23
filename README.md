# oscardjango
Django Oscar eCommerce web


#postgressql database setup
sudo su - postgres
psql -U postgres
CREATE DATABASE oscardjango;
CREATE USER oscardjangouser WITH PASSWORD 'oscardjangopassword';
ALTER ROLE oscardjangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE oscardjangouser SET timezone TO 'Asia/Kolkata';
GRANT ALL PRIVILEGES ON DATABASE oscardjango TO oscardjangouser;
