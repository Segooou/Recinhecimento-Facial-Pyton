import sqlite3
from sqlite3 import Error
import os

minhapasta = os.path.dirname(__file__)

def conect():
    con=None
    try:
        con = sqlite3.connect(minhapasta + '\\Database\\Database.db') 
    except Error as ex:
        return ex
    return con


def cria():
    if os.path.isdir(minhapasta + '\\Database'):
        pass
    else:
        os.mkdir(minhapasta + '\\Database')
    vcon = conect()
    c = vcon.cursor()
  
    c.execute('CREATE TABLE IF NOT EXISTS pessoas (nome  TEXT PRIMARY KEY,nivel INTEGER,img BLOB,ultima TEXT)')


def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData



def cadastrapessoa(nome,nivel,img,ultima):
    vcon = conect()
    c = vcon.cursor()
    try:
        c.execute('INSERT INTO pessoas (nome,nivel,img,ultima) VALUES (?,?,?,?)\
            ',(nome,nivel,convertToBinaryData(img),ultima))
        vcon.commit()
    except Error as ex:
        me = str(ex)
        if str(ex) == 'UNIQUE constraint failed: pessoas.nome':
            me = 'Este usuario já está cadastrado'
        return me


def alterapessoaultima(nome,ultima):
    vcon = conect()
    c = vcon.cursor()
    try:
        c.execute('UPDATE pessoas SET ultima = ? WHERE nome = ?',(ultima,nome))
        vcon.commit()
    except Error as ex:
        me = str(ex)
        return me


def deletapessoa(nome):
    vcon = conect()
    c = vcon.cursor()
    try:
        c.execute('DELETE FROM pessoas WHERE nome = '+'"'+nome+'"')
        vcon.commit()
        vcon.close()
    except Error as ex:
        return ex 


def deletatodaspessoas(nome):
    vcon = conect()
    c = vcon.cursor()
    try:
        c.execute('DELETE FROM pessoas WHERE nome !="'+nome+'"')
        vcon.commit()
        vcon.close()
    except Error as ex:
        return ex


def mostrar(query):
    vcon = conect()
    c = vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.close()
    return res