from google.cloud.sql.connector import Connector
import sqlalchemy

def cursor_init():
    connector = Connector()

    def getconn():
        conn = connector.connect(
            "wander-wheelz:us-central1:ww-db",
            "pymysql",
            user="root",
            password="WanderWheelz@1234",
            db='ww-db'
        )
        return conn


    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )

    return pool