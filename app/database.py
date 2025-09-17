from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import URL,create_engine
import config

url_object = URL.create(
    drivername='postgresql+psycopg2',
    host=config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

engine = create_engine(url_object)
Base = declarative_base()

Session = sessionmaker(autocommit = False,autoflush=True,bind=engine)