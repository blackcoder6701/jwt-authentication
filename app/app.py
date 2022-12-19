from fastapi import FastAPI,Depends,HTTPException,APIRouter
from pydantic import BaseModel
from app.routes.routes import root
from fastapi_jwt_auth import AuthJWT

app=FastAPI()

app.include_router(root)

class Settings(BaseModel):
    """used the secret modules to get generate the secretkey 

    Args:
        BaseModel (_type_): _description_
    """    
    authjwt_secret_key:str='38ad8b3f107abd194954ffa54412b6489f73778dcb96886f4e693f8bea8351c7'

@AuthJWT.load_config
def get_config():
    """configuring the settings defined 

    Returns:
        _type_: _description_
    """    
    return Settings()


