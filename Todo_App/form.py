from django import forms
from .models import TodoItem
import datetime
from django.core.exceptions import ValidationError 
class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        # フォームでユーザーに入力させるフィールドを指定
        fields = ['title', 'description', 'deadline','priority']
        
        # フィールドごとのカスタマイズ
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '新しいタスクを入力'}),
            'description': forms.Textarea(attrs={'placeholder': '詳細', 'rows': 2}),
            
            'deadline': forms.SelectDateWidget(
                years=range(datetime.date.today().year, datetime.date.today().year + 5),
                empty_label=("年", "月", "日"),
                attrs={'class': 'date-select-box'}
            ),
            'priority': forms.Select(attrs={'class': 'priority-select-box'})
            }
        
        # 締め切り日のバリデーションを追加
    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        
        # 1. 過去の日付（昨日以前）をチェック
        if deadline and deadline < datetime.date.today():
            raise ValidationError("過去の日付は設定できません。")
            
        return deadline        


