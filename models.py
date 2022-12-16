from database import Base
from sqlalchemy import Column,String
import uuid
from sqlalchemy.dialects.postgresql import UUID

class LoginUser(Base):
    __tablename__='login'
    id =Column(UUID(as_uuid=True),default=uuid.uuid4(),primary_key=True)   
    username=Column(String)
    email=Column(String)
    password= Column(String)
    hash_pass=Column(String,nullable=True)


