import sys
import psycopg2

USER = 'postgres'
PASSWORD = 'pramod'
HOST = 'localhost'
PORT = 5432
DBNAME = 'interndemo'

def main():
    try:
        conn = psycopg2.connect(dbname='postgres', user=USER, password=PASSWORD, host=HOST, port=PORT)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (DBNAME,))
        if cur.fetchone():
            print(f"database '{DBNAME}' already exists")
        else:
            cur.execute(f'CREATE DATABASE "{DBNAME}"')
            print(f"database '{DBNAME}' created")
        cur.close()
        conn.close()
    except Exception as e:
        print('error:', e)
        sys.exit(1)

if __name__ == '__main__':
    main()
