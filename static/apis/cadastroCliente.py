from flask import Flask
from flask import Response
import mysql.connector
import json

def cadastrarUsuario(evt):
    config = {
        'user': 'admin',
        'password': '1234',
        'host': '127.0.0.1',
        'database': 'mydb',
        'raise_on_warnings': True
    }

def verificarLogin(evt):
    
    config = {
        'user': 'admin',
        'password': '1234',
        'host': '127.0.0.1',
        'database': 'mydb',
        'raise_on_warnings': True
    }

    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT nm_jogador, cd_jogador, senha FROM mydb.cad_jogadores where cd_jogador = 1")

        resultado = cursor.fetchall()

        if(len(resultado) >= 1):
            validado = True if evt["id"] == resultado[0][1] and evt["senha"] == resultado[0][2] else False
            if(validado):
                return json.dumps(resultado[0][1])
        else:
            return Response("Id ou senha digitados incorretamente.", status=400)
            
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()

simulaLogin = {
    "id": "1",
    "senha": "12345"
} 



