from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

#postgresql://<username>:<password>@<ip_addresse/hostname>/<databasename> the format of a connection string
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
        
        
# while True:
    
#     try:
#         conn = psycopg2.connect(host='localhost',
#                                 database='fastapi',
#                                 user='postgres',
#                                 password='madara666',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection was successful")
#         break
#     except Exception as e:
#         print("connecting to database failed")
#         print("Error: ", e)
#         time.sleep(2)