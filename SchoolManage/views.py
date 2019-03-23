from django.shortcuts import render

# Create your views here.

def school_manage_index(request):

    return render(request, "school_manage_index.html")