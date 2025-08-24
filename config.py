from flask_login import UserMixin
from peewee import SqliteDatabase, Model, IntegerField, CharField, TextField

db = SqliteDatabase("db.sqlite")


class User(UserMixin, Model):
    id = IntegerField(primary_key=True)  # 主キーの設定
    name = CharField(unique=True)  # ユニークキー...nullを許可する, 重複した値が登録されないようにする
    email = CharField(unique=True)
    password = TextField()

    class Meta:
        database = db
        table_name = "users"


db.create_tables([User])
