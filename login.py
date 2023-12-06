import sqlite3
import hashlib
from menu import menu

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def login(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('SELECT * FROM user WHERE username = ? AND password = ?', (username, password_hash))
    user = cursor.fetchone()
    if user:
        print("Login realizado com sucesso!")
        menu()
    else:
        print("Credenciais inválidas.")