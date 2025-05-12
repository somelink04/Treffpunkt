# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="treffpunkt",
        password="b55tQKAc0z2K0hluWSo7Zxq2cMs9pTgx",
        host="ip.of.mariadb.server", # zb. 127.0.0.1 oder 192.168.0.57
        port=3306,
        database="TREFFPUNKT_DB"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()