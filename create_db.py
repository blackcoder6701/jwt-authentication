from database.database import Base,engine
from app.models.models import LoginUser


Base.metadata.create_all(engine)



print("creating the database")
