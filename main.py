from fastapi import FastAPI
from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table


app = FastAPI()
# # DATABASE_URL = ("sqlite:///database.db")
# # DATABASE = create_engine
# # metadata = MetaData
# # database = DATABASE(DATABASE_URL)
# # app = FastAPI()
#
# # cars = Table(
# #     "cars",
# #     metadata,
# #     Column("id", Integer, primary_key=True),
# #     Column("model", String)
# # )
# @app.on_event('start_up')
# async def startup():
#     await database.connect()
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
#
# @app.get('/cars/{car_id}')
# async def read_car(car_id: int):
#     query = cars.select().where(cars.c.id == car_id)
#     car = await database.fetch_one(query)
#     return {'car': car}

@app.get('/techscils')
def techskils():
    return 'Maksym Sharko'

@app.get('/softscils')
def softskils():
    return 'Anastasya Ivachenko'