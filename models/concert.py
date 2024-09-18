
class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @staticmethod
    def create_concert(band_id, venue_id, date, conn):
        query = "INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)"
        cur = conn.cursor()
        cur.execute(query, (band_id, venue_id, date))
        conn.commit()

    @staticmethod
    def get_by_id(concert_id, conn):
        query = "SELECT * FROM concerts WHERE id = ?"
        cur = conn.cursor()
        cur.execute(query, (concert_id,))
        return cur.fetchone()

    @staticmethod
    def band(concert_id, conn):
        query = """
        SELECT bands.* FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.id = ?
        """
        cur = conn.cursor()
        cur.execute(query, (concert_id,))
        return cur.fetchone()

    @staticmethod
    def venue(concert_id, conn):
        query = """
        SELECT venues.* FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        """
        cur = conn.cursor()
        cur.execute(query, (concert_id,))
        return cur.fetchone()

    @staticmethod
    def hometown_show(concert_id, conn):
        query = """
        SELECT bands.hometown = venues.city FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        """
        cur = conn.cursor()
        cur.execute(query, (concert_id,))
        return cur.fetchone()[0]

    @staticmethod
    def introduction(concert_id, conn):
        query = """
        SELECT bands.name, bands.hometown, venues.city FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        """
        cur = conn.cursor()
        cur.execute(query, (concert_id,))
        band, hometown, city = cur.fetchone()
        return f"Hello {city}!!!!! We are {band} and we're from {hometown}"
