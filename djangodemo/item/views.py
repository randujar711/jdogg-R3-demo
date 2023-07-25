from django.contrib.auth.decorators import login_required
from django.db.models import Q
# import decorator above

from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
from .models import Item, Category

def items(request): 
    # default it so be empty and you set this with empty ''
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query: 
        # if the name conatins the query then the query will be processed 
        # Q allows you to search in multiple fields
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories, 
        'category_id': int(category_id)
    })

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item, 
        'related_items': related_items
    })

@login_required
def new(request): 
    if request.method == 'POST': 
        # request.FILES is so we get the files the user uploads
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            # the created_by field wont be added if we dont do some tinkering with.save()
            item = form.save(commit=False)
            item.created_by = request.user 
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form, 
        'title' : 'New Item', 
    })


# for some reason it is not registering as a post request
@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    print('requested item', item)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            print('The form is valid')
            print('look here', form.cleaned_data)
            form.save()
            return redirect('item:detail', pk=item.id)
        else: 
            print('The form is not valid')
    else:
        print('not validdddddd')
        form = EditItemForm(instance=item)
        print('here are the errors', form.errors)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')



