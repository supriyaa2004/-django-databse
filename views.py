# from django.shortcuts import render 

 

# # def hello_world(request):
#     # return HttpResponse("Hello, World!")
# def about(request):
#     return render(request,'index.html')
# def child(request):
#     return render(request,'child.html')
# def child1(request):
#     return render(request,'child1.html')

from django.shortcuts import render
from .forms import bookForm

def create_book(request):
    if request.method == 'POST':
        form = bookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or perform other actions
    else:
        form = bookForm()
    return render(request, 'book.html', {'form': form})
