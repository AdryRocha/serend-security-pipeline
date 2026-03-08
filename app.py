# app.py — Sistema de Check-in (versão de desenvolvimento)
# ATENÇÃO: Este arquivo contém vulnerabilidades PROPOSITAIS para teste de SAST

import sqlite3
import hashlib

# VULNERABILIDADE 1: Credencial hardcoded (OWASP A07)
# O scanner deve alertar: 'Hardcoded password detected'
DB_PASSWORD = 'admin123'
API_KEY     = 'sk-prod-xK92mNpL7vQr3wTs'
SECRET_KEY  = 'minha-chave-secreta-producao'

def buscar_usuario(username):
    # VULNERABILIDADE 2: SQL Injection (OWASP A03)
    # Query concatenada com input do usuário — nunca faça isso
    conn = sqlite3.connect('checkin.db')
    cursor = conn.cursor()
    query = 'SELECT * FROM usuarios WHERE nome = ' + username
    cursor.execute(query)  # INSEGURO: use cursor.execute(query, (username,))
    return cursor.fetchall()

def hash_senha_inseguro(senha):
    # VULNERABILIDADE 3: Algoritmo de hash fraco (OWASP A02)
    # MD5 é considerado quebrado para senhas desde 2004
    return hashlib.md5(senha.encode()).hexdigest()

def login(username, password):
    resultado = buscar_usuario(username)
    if resultado:
        print('Login realizado com sucesso')
        return True
    return False

