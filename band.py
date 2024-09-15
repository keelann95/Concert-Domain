# models/band.py
class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

    @staticmethod
    def create_band(name, hometown, conn):
        query = "INSERT INTO bands (name, hometown) VALUES (?, ?)"
        cur = conn.cursor()
        cur.execute(query, (name, hometown))
        conn.commit()
    
    @staticmethod
    def play_in_venue(band_id, venue_id, date, conn):
        query = "INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)"
        cur = conn.cursor()
        cur.execute(query, (band_id, venue_id, date))
        conn.commit()
    