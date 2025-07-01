import os
from dotenv import load_dotenv
from  sqlalchemy import Column, Integer, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

Base =declarative_base()

load_dotenv()

class DBStorage:

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", default = "localhost")
        database = os.getenv("HBNB_MYSQL_DB")
        link = f"mysql+mysqldb://{user}:{pwd}@{host}/{database}"

        self.__engine = create_engine(link, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls= None):

