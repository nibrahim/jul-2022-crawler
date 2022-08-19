import psycopg2


def get_connection(dbname):
    return psycopg2.connect(f"dbname={dbname}")

                     
    
