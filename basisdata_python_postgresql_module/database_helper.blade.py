# INSTALL MODULE PSYCOPG2 DENGAN CARA
# pip install pyscopg2

import os
import psycopg2
from config import config

# FUNGSI UNTUK KONEK KE DATABASE POSTGRESQL
def connect():
    try:
        conn = None
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
       
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

# FUNGSI UNTUK READ DATABASE
def read_database_one():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = 'SELECT * FROM mahasiswa1'
        cur = conn.cursor()
        cur.execute(sql)
        hasil = cur.fetchall()
        print(f'Database: {hasil}')
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')

# FUNGSI UNTUK CREATE DATABASE
def create_database_one():
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        sql = 'CREATE TABLE mahasiswa1 (id SERIAL PRIMARY KEY, nama VARCHAR(255) NOT NULL, nim VARCHAR(15) NOT NULL,jurusan VARCHAR(100),tanggal_lahir DATE, alamat TEXT)'
        cur = conn.cursor()
        conn.commit()
        cur.execute(sql)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')
            
def main():
    print("Selamat datang di basic CREATE and READ")
    print("Silahkan pilih menu")
    def header():
        print("""
            MENU: 
            1. CREATE MAHASISWA
            2. READ MAHASISWA
            3. EXIT
            """)
    header()
    user_input = input("Masukkan opsi: ")

    while True:
        if user_input == '1':
            create_database_one()
            break
        elif user_input == '2':
            read_database_one()
            break
        elif user_input == '3':
            break
        else:
            print("Pilihan anda tidak valid, silahkan pilih lagi")
            header()
            user_input = input("Masukkan opsi: ")
            
main()