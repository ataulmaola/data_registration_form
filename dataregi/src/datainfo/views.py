from django.shortcuts import render
from .forms import SignUpData
# Create your views here.
def home(request):
    title="My Title"
    form=SignUpData(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    context={"title":title,
             "form":form
    }
    return render(request,"home.html",context)