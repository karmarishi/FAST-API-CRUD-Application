from fastapi import FastAPI

# app=FastAPI()

# @app.get("/ok")
# async def read_me():
#     return ("Hellow World")



# from user import api as UserRoute
# from configs.connection import  DATABASE_URL

# db_url= DATABASE_URL()
app=FastAPI()

# app.include_router(UserRoute.router,prefix="/user",tags=["Users"]),

@app.get("/")
async def root():
    return {"message": "Hello World"}