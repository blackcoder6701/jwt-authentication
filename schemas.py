from pydantic import BaseModel


class Jwtmain(BaseModel): 
    
    username:str 
    email:str 
    password:str

    class Config:
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str

    class Config:
        orm_mode=True
        

