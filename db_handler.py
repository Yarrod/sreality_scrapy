import psycopg2
import os

class DbHandler():
    """
    A class that handles database operations for ads_table.

    Attributes:
        connection: The database connection object.
        cursor: The database cursor object.

    Methods:
        insert_ad: Inserts a new ad into the ads_table.
        get_ads: Retrieves ads from the ads_table.
        close: Closes the database connection.
        db_connect: Establishes a connection to the database.
        create_ads_table: Drops and creates the ads_table
    """
    def __init__(self):
        self.connection = self.db_connect()
        self.cursor = self.connection.cursor()

    def insert_ad(self, item):
        """
        Inserts a new ad into the ads_table.

        Args:
            item (dict): A dictionary containing the ad details.

        Returns:
            None
        """
        insert_query = "INSERT INTO ads_table (title, image_url) VALUES (%s, %s)"
        self.cursor.execute(insert_query, (item['title'], item['image_urls']))
        self.connection.commit()

    def get_ads(self):
        """
        Retrieves ads from the ads_table.

        Returns:
            list: A list of ads retrieved from the ads_table.
        """
        self.cursor.execute("SELECT * FROM ads_table WHERE ID <= 500")
        res = self.cursor.fetchall()
        return res
    
    def close(self):
        """
        Closes the database connection.

        Returns:
            None
        """
        self.connection.close()

    def db_connect(self):
        """
        Establishes a connection to the database.

        Returns:
            psycopg2.extensions.connection: The database connection object.
        """
        # use environment variable if it exists, otherwise use default value
        # because of devcontainer
        host = os.getenv("DB_HOST") or "db"
        dbname = os.getenv("DB_NAME") if os.getenv("DB_NAME") == "" else "sreality_db"
        return psycopg2.connect(
                dbname=dbname,
                user="postgres",
                password="postgres",
                host=host,
                port="5432"
            )

    def create_ads_table(self):
        """
        Drops and creates the ads_table.

        Returns:
            None
        """
        self.cursor.execute(
                """
                DROP TABLE IF EXISTS ads_table 
                """
            )
        self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS ads_table (
                    id SERIAL PRIMARY KEY,
                    title TEXT,
                    image_url TEXT
                )
                """
            )