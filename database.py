from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL ="sqlite:///../students.db"
# SQLALCHEMY_DATABASE_URL ="postgres://studentsdb_user:YZ8NwFaud0ia47DQDQegsUEtpf4hvE7z@dpg-cfgkt19a6gdma8h5544g-a/studentsdb"

engine =create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
    )

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
