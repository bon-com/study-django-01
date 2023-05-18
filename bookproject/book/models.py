from django.db import models
from .consts import MAX_RATE

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

# Bookテーブル定義
CATEGORY = (
    ('business', 'ビジネス'),
    ('life', '生活'),
    ('other', 'その他')
)
class Book(models.Model):
    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('説明')
    category = models.CharField(
        'カテゴリ',
        max_length=100,
        choices = CATEGORY
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '書籍'
        verbose_name_plural = "書籍"

# Reviewテーブル定義
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('レビュー内容')
    rate = models.IntegerField('評価', choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'レビュー状況'
        verbose_name_plural = "レビュー状況"
