from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql, Float
class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key = True)
    username= Column(String(200), primary_key = True)
    balance = Column(Float)
    status = Column(String(30))
    query:sql.select