import sqlite3
import hashlib

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def create_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('INSERT INTO user (username, password) VALUES (?, ?)', (username, password_hash))
    conn.commit()
    print("Usuário cadastrado com sucesso!")
    
def create_book(title, author, genre, isbn):
    cursor.execute('INSERT INTO book (title, author, genre, isbn) VALUES (?, ?, ?, ?)', (title, author, genre, isbn))
    conn.commit()
    print("Livro adicionado com sucesso!")

def select_book(id):
        cursor.execute('SELECT * FROM book WHERE id = ?', (id,))
        book = cursor.fetchone()
        if book:
            print(f"ID: {book[0]} | Título: {book[1]} | Autor: {book[2]} | Gênero: {book[3]} | ISBN: {book[4]}")
        else:
            print("Livro não encontrado.")

def update_book(id, title, author, genre, isbn):
    cursor.execute('SELECT * FROM book WHERE id = ?', (id,))
    existing_book = cursor.fetchone()
    if existing_book:
        cursor.execute('UPDATE book SET title = ?, author = ?, genre = ?, isbn = ? WHERE id = ?', (title, author, genre, isbn, id))
        conn.commit()
        print("Livro atualizado com sucesso!")
    else:
        print("Livro não encontrado. Atualização cancelada.")

def delete_book(id):
    cursor.execute('SELECT * FROM book WHERE id = ?', (id,))
    existing_book = cursor.fetchone()
    if existing_book:
        cursor.execute('DELETE FROM book WHERE id = ?', (id,))
        conn.commit()
        print("Livro excluído com sucesso!")
    else:
        print("Livro não encontrado. Exclusão cancelada.")