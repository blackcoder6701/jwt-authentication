from database import Base,engine
from models import LoginUser


Base.metadata.create_all(engine)



print("creating the database")
