from django.urls import path
from . import views

# アプリケーションの名前空間を定義 (テンプレートでURLを呼び出す際に利用)
app_name = 'Todo_App' 

urlpatterns = [
#path(route, view, kwargs=None, name=None)   
#route/view/name#オプションで構成されるリスト。path関数あるいはre_path関数で生成されたURLパターン。
#routeでパターンを文字列で指定し、viewの引数でビューを指定し、任意でnameでパターンに名前をつけることができる（templateやview内でURLパターンを参照することができるようになる）
#re_pathはrouteの引数が正規表現をとれる。指定した文字列そのものが正規表現として扱われる。
#Path()関数：https://docs.djangoproject.com/ja/5.2/ref/urls/
#正規表現操作：https://docs.python.org/ja/3/library/re.html

    # Todoリスト表示 (GET /todos/)
    path('', views.list_todos, name='list_todos'),
    
    # Todo新規作成 (POST /todos/add/)
    path('add/', views.add_todo, name='add_todo'), 

    # 完了ステータスの切り替え (POST /todos/<id>/complete/)
    path('<int:pk>/complete/', views.update_completed, name='update_completed'),
    
    # Todo削除 (POST /todos/<id>/delete/)
    path('<int:pk>/delete/', views.delete_todo, name='delete_todo'),
]