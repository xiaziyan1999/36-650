Drop TABLE rdata;

CREATE TABLE rdata (
id SERIAL PRIMARY KEY, 
a text UNIQUE NOT NULL CHECK (char_length(a) <= 5), 
b text UNIQUE NOT NULL CHECK (char_length(b) <= 5), 
moment date Default ('2020-01-01'),
x DECIMAL(5,2) check(x>0) 
);
