# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="treffpunkt",
        password="b55tQKAc0z2K0hluWSo7Zxq2cMs9pTgx",
        host="127.0.0.1", # zb. 127.0.0.1 oder 192.168.0.57
        port=3306,
        database="TREFFPUNKT_DB"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute(
    "SELECT CATEGORY_ID, CATEGORY_NAME, CATEGORY_DESCRIPTION FROM CATEGORY")

# Print Result-set
for (CATEGORY_ID, CATEGORY_NAME, CATEGORY_DESCRIPTION) in cur:
    print(f"Id: {CATEGORY_ID}, Name: {CATEGORY_NAME}, Description: {CATEGORY_DESCRIPTION}")

cur.execute(
    "SELECT REGION_NAME, REGION_ZIP FROM REGION WHERE REGION_DISTRICT = 'Passau'")

# Print Result-set
for (REGION_NAME, REGION_ZIP) in cur:
    print(f"Name: {REGION_NAME}, Plz: {REGION_ZIP}")