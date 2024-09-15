# models/venue.py
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

