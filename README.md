# TodoList
優先度や締め切りを設定できるTodoリスト
タスク未完了←→完了を切り替えることが出来ます。

◆使用言語
バックエンド：Django  
フロントエンド：Vue/HTML/CSS

仮想環境（venv）を利用して、以下の手順でアプリケーションを起動できます。

###  ローカル環境構築の手順
```bash
■ リポジトリの取得
git clone [https://github.com/KK0705-flower/TodoList.git](https://github.com/KK0705-flower/TodoList.git)
cd TodoList

■ 仮想環境を作成
python -m venv .venv

# 【Windowsの場合】有効化
.\.venv\Scripts\activate

# 【Mac / Linuxの場合】有効化
source .venv/bin/activate
■必要なライブラリのインストール
pip install -r requirements.txt

■データベースの初期化
# マイグレーションファイルの作成
python manage.py makemigrations

# 実際のデータベースへ反映
python manage.py migrate

■サーバーの立ち上げ
python manage.py runserver
