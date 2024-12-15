from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark, Category
from .forms import *



def home(request):
    categories = Category.objects.prefetch_related('bookmarks').all()
    return render(request, 'bookmarkmanagerapp/home.html', {'categories': categories})



def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookmarkForm()
        context = {'form':form}
        return render(request,'bookmarkmanagerapp/add_bookmark.html',context)
    
    
    
def edit_bookmark(request,pk):
    bookmark = Bookmark.objects.get(id=pk)
    if request.method == 'POST':
        form = BookmarkForm(request.POST,instance = bookmark)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookmarkForm(instance=bookmark)
        context = {'form': form , 'bookmark':bookmark}
        return render(request, 'bookmarkmanagerapp/edit_bookmark.html',context)
    
    
    
    
def delete_bookmark(request,pk):
    bookmark = Bookmark.objects.get(id=pk)
    bookmark.delete()
    return redirect('home')



def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'bookmarkmanagerapp/add_category.html', {'form': form})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    bookmarks = category.bookmarks.all()  
    return render(request, 'bookmarkmanagerapp/category_detail.html', {'category': category, 'bookmarks': bookmarks})