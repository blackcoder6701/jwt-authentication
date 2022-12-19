from fastapi_jwt_auth import AuthJWT
from database.database import SessionLocal
from app.models.models import LoginUser
from app.schemas.schemas import Login,Jwtmain
from fastapi import FastAPI,APIRouter, Body, Depends,HTTPException
import hashlib

db=SessionLocal()

root = APIRouter()

#definig the Schemas 
@root.get('/')
def homepage():
    
    """home page function

    Returns:
        _type_: _description_
    """    

    return {"data":"you are homepage" }


@root.post('/nextpage')
def nextpage(user:Jwtmain):

    """posting the details about the users like username,password,email

    Args:
        user (Jwtmain): _description_

    Returns:
        _type_: _description_
    """    
    new_user = LoginUser(
        username = user.username,
        email = user.email,
        password = hash(user.password)    
    )
    db.add(new_user)
    db.commit()

    return new_user


#getting all the users
@root.get('/user/all')
def getall():
    """get all the users details 

    Returns:
        _type_: _description_
    """    
    display_users=db.query(LoginUser).all()
    return display_users


@root.post('/login')
def login(user:Login,Authorize:AuthJWT=Depends()):
    """taking the inputs from the user that are the password and username and also validating it

    Args:
        user (Login): _description_
        Authorize (AuthJWT, optional): _description_. Defaults to Depends().

    Returns:
        _type_: _description_
    """    

    user_name=user.username
    pass_user=user.password
       
    if db.query(LoginUser).filter(LoginUser.username == user_name, LoginUser.password == pass_user).count():
        access_token = Authorize.create_access_token(subject=user.username)
    return access_token 


@root.get('/protected')
def protected(Authorize:AuthJWT=Depends()):

    """creating the protected routed that will only show the information 

    Args:
        Authorize (AuthJWT, optional): _description_. Defaults to Depends().

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """  

    try:
        Authorize.jwt_required()    
    
    except Exception as e:
        raise HTTPException(status_code=401,detail="invalid token")

    current_user=Authorize.get_jwt_subject()

    return current_user

@root.get('/newtoken')
def refreshtoken(Authorize:AuthJWT=Depends()):
    try:
        Authorize.fresh_jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401,detail="no token generated")
 
    current_user=Authorize.get_jwt_subject()
    
    access_token=Authorize.create_access_token(subject=current_user)

    return access_token


