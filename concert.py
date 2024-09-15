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

