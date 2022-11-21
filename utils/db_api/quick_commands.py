from utils.db_api.schemas.user import User
from asyncpg import UniqueViolationError
from utils.db_api.db_gino import db
from sqlalchemy import create_engine
engine = create_engine(
    "postgresql+psycopg2://gino:0321467213z@185.250.205.118/game_db")
async def add_user(user_id: int, username:str,  balance:float, status:str):
    try:
        user = User(user_id = user_id,  username = username, balance = balance, status = status)
        await user.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")
async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user
async def update_user_balance(user_id, change_b):
    user = await select_user(user_id)
    new_balance = user.balance + float(change_b)
    await user.update(balance = new_balance).apply()
async def select_all_users():
    users =  User.query.order_by(User.balance)
    result = engine.execute(users).fetchall()
    mas_b = []
    mas_n = []
    for record in result:
        mas_b.append(record[1])
        mas_n.append(record[2])
    return [mas_b, mas_n]