from django.core.paginator import Paginator
from .consts import ITEM_PER_PAGE
from django.shortcuts import render
from .models import Book, Review
from .forms import BookForm, ReviewForm
from django.shortcuts import redirect

# メモ：redirectの引数にはアプリ名：URL名称を設定する
# Create your views here.
def index_view(request):
    template_name = 'book/index.html'
    book_list = Book.objects.all()
    paginator = Paginator(book_list, ITEM_PER_PAGE)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.page(page_num) 

    ctx = {'page_obj': page_obj}
    return render(request, template_name, ctx)

def list_books(request):
    template_name = 'book/book_list.html'
    book_list = Book.objects.all()
    ctx = {'book_list': book_list}
    return render(request, template_name, ctx)

def detail_book(request, pk):
    template_name = 'book/book_detail.html'
    book = Book.objects.get(pk=pk)
    ctx = {'book': book}
    return render(request, template_name, ctx)

def create_book(request):
    template_name = 'book/create_book.html'
    form = BookForm(request.POST or None)

    if form.is_valid():
        title = form.cleaned_data["title"]
        text = form.cleaned_data["text"]
        category = form.cleaned_data["category"]

        obj = Book(title=title, text=text, category=category)
        obj.save()
        response = redirect('book:list_books')

        return response
    else:
       ctx = {'form': form}
       return render(request, template_name, ctx)

def delete_book(request, pk):
    try:
        Book.objects.get(id=pk).delete()
    except Book.DoesNotExist:
        raise Http404("指定したユーザーは存在しませんでした。")

    response = redirect('book:list_books')
    return response

def update_book(request, pk):
    template_name = 'book/update_book.html'
    book = Book.objects.get(pk=pk)
    init_val = {'title': book.title, 'text': book.text, 'category': book.category}
    form = BookForm(request.POST or init_val)
    ctx = {'form': form}
    print(book)
    if form.is_valid() and request.method == 'POST':
        book.title = form.cleaned_data["title"]
        book.text = form.cleaned_data["text"]
        book.category = form.cleaned_data["category"]
        book.save()

        response = redirect('book:list_books')

        return response
    else:
        return render(request, template_name, ctx)

def review_book(request, pk):
    template_name = 'book/review_form.html'
    form = ReviewForm(request.POST or None)
    book = Book.objects.get(pk=pk)
    ctx = {'form': form, 'book': book}

    if request.method == 'POST':
        if not request.user.is_authenticated:
            ctx['error_msg'] = 'ログインした後、投稿してください。'
            return render(request, template_name, ctx)

        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            rate = form.cleaned_data["rate"]

            obj = Review(title=title, text=text, rate=rate, book_id=book.pk, user_id=request.user.id)
            obj.save()
            response = redirect('book:index')

            return response
        else:
            ctx['error_msg'] = '投稿に失敗しました。'
            return render(request, template_name, ctx)
    else:
        return render(request, template_name, ctx)
    