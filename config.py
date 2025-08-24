from peewee import SqliteDatabase, Model, IntegerField, CharField, TextField

db = SqliteDatabase("db.sqlite")


class User(Model):
    id = IntegerField(primary_key=True)  # 主キーの設定
    name = CharField(unique=True)  # ユニークキー...nullを許可する, 複数設定可能
    email = CharField(unique=True)
    password = TextField()

    class Meta:
        database = db
        table_name = "users"


db.create_tables([User])
