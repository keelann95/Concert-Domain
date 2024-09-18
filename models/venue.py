
class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    @staticmethod
    def create_venue(title, city, conn):
        query = "INSERT INTO venues (title, city) VALUES (?, ?)"
        cur = conn.cursor()
        cur.execute(query, (title, city))
        conn.commit()

    @staticmethod
    def get_by_id(venue_id, conn):
        query = "SELECT * FROM venues WHERE id = ?"
        cur = conn.cursor()
        cur.execute(query, (venue_id,))
        return cur.fetchone()

    @staticmethod
    def concerts(venue_id, conn):
        query = "SELECT * FROM concerts WHERE venue_id = ?"
        cur = conn.cursor()
        cur.execute(query, (venue_id,))
        return cur.fetchall()

    @staticmethod
    def bands(venue_id, conn):
        query = """
        SELECT DISTINCT bands.* FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        """
        cur = conn.cursor()
        cur.execute(query, (venue_id,))
        return cur.fetchall()

    @staticmethod
    def concert_on(venue_id, date, conn):
        query = """
        SELECT * FROM concerts
        WHERE venue_id = ? AND date = ?
        LIMIT 1
        """
        cur = conn.cursor()
        cur.execute(query, (venue_id, date))
        return cur.fetchone()

    @staticmethod
    def most_frequent_band(venue_id, conn):
        query = """
        SELECT bands.*, COUNT(concerts.id) as performance_count FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY performance_count DESC
        LIMIT 1
        """
        cur = conn.cursor()
        cur.execute(query, (venue_id,))
        return cur.fetchone()
