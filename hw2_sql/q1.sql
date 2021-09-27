CREATE TABLE rdata (
id SERIAL PRIMARY KEY, 
a text CHECK (char_length(a) <= 5), 
b text CHECK (char_length(b) <= 5), 
moment date,
x DECIMAL(5,2)
);