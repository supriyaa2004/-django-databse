# # from django.shortcuts import render 

 

# # # def hello_world(request):
# #     # return HttpResponse("Hello, World!")
# # def about(request):
# #     return render(request,'index.html')
# # def child(request):
# #     return render(request,'child.html')
# # def child1(request):
# #     return render(request,'child1.html')

# from django.shortcuts import render
# from .forms import bookForm

# def create_book(request):
#     if request.method == 'POST':
#         form = bookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect or perform other actions
#     else:
#         form = bookForm()
#     return render(request, 'book.html', {'form': form})
from django.shortcuts import render
from .forms import ProductForm

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            tittle = form.cleaned_data['title']
            publisher = form.cleaned_data['description']
            year=form.cleaned_data['year']
            status=form.cleaned_data['status']
            roll=form.cleaned_data['roll']
            # Save data to the database or perform other actions
    else:
        form = ProductForm()
    return render(request, 'book.html', {'form': form})
