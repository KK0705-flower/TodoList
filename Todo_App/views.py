from django.shortcuts import render, redirect, get_object_or_404
#get_object_or_404は、Modelとpkを指定し、存在すればuserのオブジェクトを返し、存在しなければ404を返す。
from django.views.decorators.http import require_POST
from .models import TodoItem #モデルからtodoItemをインポート
from .form import TodoItemForm #formからTodeItemFormをインポート

#viewについて：https://docs.djangoproject.com/ja/5.2/topics/http/view/

def list_todos(request):
    all_items = TodoItem.objects.all().order_by('created_at')
    
    incomplete_todos = all_items.filter(completed=False)
    complete_todos = all_items.filter(completed=True)
    
    form = TodoItemForm()
    
    context = {
        'incomplete_todos': incomplete_todos,#未完了タスク
        'complete_todos': complete_todos,#完了
        'form': form,
    }
    
    return render(request, 'Todo_App/list.html', context)
#renderメソッド
#return render(request, template_name, context=None, content_type=None, status=None, using=None)
#データベースのデータを反映したHTMLページを作成し、HTMLレスポンスとしてブラウザに返す。
#HttpResponseはcontextのようなデータをテンプレートに渡すことができないため、関数ベースのviewではrenderメソッドを使う。
#ファイルの表示やダウンロードをブラウザ側で表示させる場合はHttpResponseを使う。
#request引数にはPOSTの情報や、セッション情報が格納されている。
#template_name引数には、表示させるテンプレートを指定する。templateフォルダ起点の相対パスで指定しなければならない。
#context引数には、辞書型のデータを指定する。
#参考サイト：https://office54.net/python/django/views-render-how-to


@require_POST
@require_POST
def add_todo(request):
    form = TodoItemForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('Todo_App:list_todos')
    
    # バリデーションエラー時の処理 
    all_items = TodoItem.objects.all().order_by('created_at')
    incomplete_todos = all_items.filter(completed=False)
    complete_todos = all_items.filter(completed=True)
    
    context = {
        'incomplete_todos': incomplete_todos,
        'complete_todos': complete_todos,
        'form': form, 
    }

    return render(request, 'Todo_App/list.html', context)

@require_POST
def update_completed(request, pk):#
    item = get_object_or_404(TodoItem, pk=pk)
    
    item.completed = not item.completed
    
    item.save()
    
    return redirect('Todo_App:list_todos')

@require_POST
def delete_todo(request, pk):#削除するときに使う関数。
    item = get_object_or_404(TodoItem, pk=pk)
    item.delete()
    
    return redirect('Todo_App:list_todos')