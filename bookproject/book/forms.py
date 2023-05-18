from django import forms
from .models import Book
from .models import Review

# フォームの作成方法
# 1. モデル.テーブル名をインポートする
# 2. django.forms.ModelFormを継承する
# 3. Metaクラス内に連動する情報を記載する
#   - model：テーブル名
#   - fields：フォームで入力可能なフィールド名（fields = '__all__'と記載すればすべてになる）
#   - labels：フォーム画面で表示するフィールド名称

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'text', 'category')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'text', 'rate')