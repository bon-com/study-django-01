from django import forms
from .models import Book
from .models import Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'text', 'category')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'text', 'rate')