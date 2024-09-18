from database import connect_db
from models.band import Band
from models.venue import Venue
from models.concert import Concert
def setup_database():
    conn = connect_db()
    with open('create_tables.sql') as f:
        conn.executescript(f.read())
    conn.close()
