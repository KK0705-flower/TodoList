# TodoList
優先度や締め切りを設定できるTodoリスト
タスク未完了←→完了を切り替えることが出来ます。

◆使用言語
バックエンド：Django
フロントエンド：Vue/HTML/CSS



#  ◆ローカル環境構築を行う手順
仮想環境内で起動することが出来ます。

■リポジトリの取得
git clone https://github.com/KK0705-flower/TodoList.git
cd TodoList

■仮想環境を作成
python -m venv .venv

【Windowsの場合】有効化
.\.venv\Scripts\activate
【Mac / Linuxの場合】有効化
source .venv/bin/activate

■必要なライブラリのインストール
pip install -r requirements.txt

■データベースの初期化
# マイグレーションファイルを作成
python manage.py makemigrations
# 実際のデータベースへ反映
python manage.py migrate

■サーバーの立ち上げ
python manage.py runserver
