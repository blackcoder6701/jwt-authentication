from pydantic import BaseModel


class Jwtmain(BaseModel): 
    """created the schemas for the singnup 

    Args:
        BaseModel (_type_): _description_
    """    
    
    username:str 
    email:str 
    password:str

    class Config:
        orm_mode=True

class Login(BaseModel):
    """created the scehmas for the login module

    Args:
        BaseModel (_type_): _description_
    """    

    username:str
    password:str

    class Config:
        orm_mode=True
        

