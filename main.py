from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
from database import SessionLocal
from models import LoginUser
from schemas import Login,Jwtmain
from fastapi import FastAPI, Body, Depends

# from .app.auth import JWTBearer
# from .app.auth_handler import signJWT
#using the authjwt will help us to get the tokens verify the tokensa and all the things will be done by this module or we can say by this class


app=FastAPI()

db=SessionLocal()

class Settings(BaseModel):
    authjwt_secret_key:str='38ad8b3f107abd194954ffa54412b6489f73778dcb96886f4e693f8bea8351c7'

@AuthJWT.load_config
def get_config():
    return Settings()


#definig the Schemas 



@app.get('/')
def homepage():
    """home page function

    Returns:
        _type_: _description_
    """    

    return {"data":"you are homepage" }


@app.post('/nextpage')
def nextpage(user:Jwtmain):
    new_user = LoginUser(
        username = user.username,
        email = user.email,
        password = user.password    
    )
    db.add(new_user)
    db.commit()

    return new_user


#getting all the users
@app.get('/user/all')
def getall():
    display_users=db.query(LoginUser).all()
    return display_users


@app.post('/login')
def login(user:Login,Authorize:AuthJWT=Depends()):
    user_name=user.username
    pass_user=user.password
    # if (db.query(LoginUser.username).username == user_name) and (db.query(LoginUser.password).password == pass_user):
    #     access_token = Authorize.create_access_token(subject=user.username)      
    if db.query(LoginUser).filter(LoginUser.username == user_name, LoginUser.password == pass_user).count():
        access_token = Authorize.create_access_token(subject=user.username)
    return access_token 

    

    # for u in users:
    #     if(u["user"]==user.username) & (u["password"]==user.password):
    #         access_token=Authorize.create_access_token(subject=user.username)

    #         return{"acess token":access_token} 
    #     raise HTTPException(status_code='401',detail="invalid username or password")


@app.get('/protected',dependencies=[Depends(AuthJWT)])
def protected(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()    
    
    except Exception as e:
        raise HTTPException(status_code=401,detail="invalid token")


    current_user=Authorize.get_jwt_subject()

    return current_user

# @app.post("/posts", dependencies=[Depends(JWTBearer())], )
# async def tokendisplay(login: Jwtmain) -> dict:
    