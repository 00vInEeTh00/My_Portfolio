from django.shortcuts import render
from .forms import PortfolioForm
from django.shortcuts import redirect

# Create your views here.

def home(request):
   return render(request,'home.html')


def portfolio_create(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # replace with your desired redirect
    else:
        form = PortfolioForm()
    return render(request, 'portfolio_form.html', {'form': form})

def index(request):
   return render(request,'home.html')
