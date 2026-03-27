from django.db import models

# Create your models here.
from django.utils import timezone

class TodoItem(models.Model):
    PRIORITY_CHOICES = [(3, '高'), (2, '中'), (1, '低')]
    # タスクのタイトル 
    title = models.CharField(max_length=200)
    # タスクの詳細 (オプション)
    description = models.TextField(blank=True, null=True)
    # 作成日時 (タスクが作られた時間を自動で記録)
    created_at = models.DateTimeField(default=timezone.now)
    #締め切り
    deadline=models.DateField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    # 完了フラグ
    completed = models.BooleanField(default=False)
    
    # モデルの文字列表現を定義
    def __str__(self):
        # 管理画面などで表示されるオブジェクト名
        return self.title

    # データベースのテーブル名やモデルのオプションを定義するインナークラス
    class Meta:
        # created_at の降順（新しいものが上）でリストを並べ替える
        ordering = ['-created_at']