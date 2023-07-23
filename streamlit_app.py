import streamlit as st

from connections import DuckDBConnection

conn = st.experimental_connection("duckdb", type=DuckDBConnection, database=':memory:')


st.title('Books Dataset')
st.write('Books Data')

c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS books (    book_id INT PRIMARY KEY,    title VARCHAR(255) NOT NULL,    author VARCHAR(100),    genre VARCHAR(50),publication_year INT,price DECIMAL(8, 2), in_stock BOOLEAN);")

# # drop any existing data from a prior run ;)
c.execute("DELETE FROM books")
c.execute("INSERT INTO books (book_id, title, author, genre, publication_year, price, in_stock) VALUES (1, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, 12.99, true), (2, '1984', 'George Orwell', 'Dystopian', 1949, 9.99, true), (3, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, 11.49, true), (4, 'Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 8.99, true), (5, 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, 14.99, true), (6, 'Brave New World', 'Aldous Huxley', 'Dystopian', 1932, 10.79, false), (7, 'Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 'Fantasy', 1997, 16.95, true);")

df = conn.query("select * from books")
st.dataframe(df)


st.write('Customer Data')

c.execute("CREATE TABLE IF NOT EXISTS customers (customer_id INT PRIMARY KEY, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, email VARCHAR(100) UNIQUE, phone VARCHAR(15), address VARCHAR(200));")

c.execute("DELETE FROM customers")
c.execute("INSERT INTO customers (customer_id, first_name, last_name, email, phone, address) VALUES (1, 'John', 'Doe', 'john.doe@example.com', '+1234567890', '123 Main St, City'), (2, 'Jane', 'Smith', 'jane.smith@example.com', '+9876543210', '456 Elm St, Town'), (3, 'Michael', 'Johnson', 'michael.j@example.com', '+1122334455', '789 Oak Ave, Village');")

df = conn.query("select * from customers")
st.dataframe(df)



st.text('Currently Unavailable!')
st.dataframe(conn.query('select * from books, where in_stock=false '))
