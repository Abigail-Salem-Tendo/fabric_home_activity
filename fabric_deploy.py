import os
from fabric import Connection
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
USER = os.getenv("USER")
SSH_KEY = os.getenv("SSH_KEY")
SSH_PASSPHRASE = os.getenv("SSH_PASSPHRASE")

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

LOCAL_DUMP = "dump.sql"
REMOTE_DUMP = f"/home/{USER}/dump.sql"


connection = Connection(
    host=HOST,
    user=USER,
    connect_kwargs={
        "key_filename": SSH_KEY,
        "passphrase": SSH_PASSPHRASE
    }
)

#install mysql on the server
def install_mysql():
    connection.run("sudo apt update -y", pty=True)
    connection.run("sudo apt install mysql-server -y", pty=True)

#create the database
def create_database():
    connection.run(
        f"sudo mysql -e \"CREATE DATABASE IF NOT EXISTS {DB_NAME};\"",
        pty=True
    )
#Upload the dump
def upload_dump():
    connection.put(LOCAL_DUMP, REMOTE_DUMP)

#import the dump
def import_dump():
    connection.run(
        f"sudo mysql {DB_NAME} < {REMOTE_DUMP}",
        pty=True
    )

#verify the dump
def verify():
    print("\n[5] Verifying dump")
    connection.run(
        f"sudo mysql -e \"USE {DB_NAME}; SHOW TABLES;\"",
        pty=True
    )

install_mysql()
create_database()
upload_dump()
import_dump()
verify()

print("All done!")