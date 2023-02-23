import yaml
import mysql.connector
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)['database']
conn=mysql.connector.connect(
    host=config['host'],
    port=config['port'],
    database=config['dbname'],
    user=config['user'],
    password=config['password']
)
cur=conn.cursor()
cur.execute("SELECT * FROM mobile_phones")
rows=cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()