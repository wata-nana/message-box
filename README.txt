〇設計順序
User テーブルをつくる(情報が分類されてはいっている表みたいなの)
message テーブルをつくる

本来は先にテーブル作成...データベース設計が基本

〇基本
HTMLファイルは必ずtemplatesファイル下で管理する
pythonファイルの@routeではデフォルトだと"GET"しか受け取ってくれない
　...@app.route("/register", methods=["GET", "POST"]) のように明示的に許可する必要がある

主キー：mainの管理キー。1ファイル内に原則1つしか登録できない。idで値を識別管理するキー。
ユニークキー：その値がユニークであること(重複を許さない)を定義する
(ex)
    email = CharField(unique=True) ...誰かがw@gmail.comを登録したら、もうそのメールアドレスは登録できない
    password = TextField()　...違うユーザーが同じパスワードを登録できる

未入力とかでもう一度入力してほしいときはredirect。render_templateだと入力が重複してしまったり、多重にデータが送られてしまったりする。


〇インストールパッケージ
Peeweeは、SQLite,MySQL,Postgresqlのデータベースをサポートしている。

〇データベース
パスワード等の重要な情報を入れるときは、データベース内でhash化(暗号化)をする。

〇flaskモジュール
1. redirect :送信元のアドレスに対して、get.requestでアクセスして送信先に送ってね
2. render_template :テンプレート内の要素を送信先に送ってね
3. request :送信先から得た情報を反映させて送信先に送ってね
