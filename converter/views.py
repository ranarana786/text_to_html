from django.shortcuts import render
from .forms import EditorForms


# Create your views here.
def index(request):
    form = EditorForms()
    if request.method == 'POST':
        form = EditorForms(request.POST)
        if form.is_valid():
            html = form.cleaned_data
    return render(request, 'converter/file.html', {'form': form})

