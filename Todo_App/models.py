from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    PRIORITY_CHOICES = [(3, '高'), (2, '中'), (1, '低')] #優先度の選択肢を定義

    title = models.CharField(max_length=200) #タスクのタイトルを保存する
    description = models.TextField(blank=True, null=True)#タスクの詳細を保存
    created_at = models.DateTimeField(default=timezone.now)#作成日時
    deadline=models.DateField()#締切日
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) #優先度
    completed = models.BooleanField(default=False) #タスクが完了したのか判断するためのフィールド
    
    def __str__(self):
        return self.title

    class Meta:
        # created_at の降順でリストを並べ替え
        ordering = ['-created_at']