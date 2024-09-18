
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
    def get_by_id(band_id, conn):
        query = "SELECT * FROM bands WHERE id = ?"
        cur = conn.cursor()
        cur.execute(query, (band_id,))
        return cur.fetchone()

    @staticmethod
    def play_in_venue(band_id, venue_id, date, conn):
        query = "INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)"
        cur = conn.cursor()
        cur.execute(query, (band_id, venue_id, date))
        conn.commit()

    @staticmethod
    def concerts(band_id, conn):
        query = "SELECT * FROM concerts WHERE band_id = ?"
        cur = conn.cursor()
        cur.execute(query, (band_id,))
        return cur.fetchall()

    @staticmethod
    def venues(band_id, conn):
        query = """
        SELECT DISTINCT venues.* FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.band_id = ?
        """
        cur = conn.cursor()
        cur.execute(query, (band_id,))
        return cur.fetchall()

    @staticmethod
    def all_introductions(band_id, conn):
        query = """
        SELECT venues.city, bands.name, bands.hometown FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE bands.id = ?
        """
        cur = conn.cursor()
        cur.execute(query, (band_id,))
        concerts = cur.fetchall()
        return [f"Hello {city}!!!!! We are {name} and we're from {hometown}" for city, name, hometown in concerts]

    @staticmethod
    def most_performances(conn):
        query = """
        SELECT bands.*, COUNT(concerts.id) as concert_count FROM bands
        JOIN concerts ON concerts.band_id = bands.id
        GROUP BY bands.id
        ORDER BY concert_count DESC
        LIMIT 1
        """
        cur = conn.cursor()
        cur.execute(query)
        return cur.fetchone()
