from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine=create_engine("postgresql://postgres:jeel@localhost/jwtdb")


Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)