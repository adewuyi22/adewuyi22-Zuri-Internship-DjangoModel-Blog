from django.shortcuts import render

# Create your views here.
def home_view(request):
    projtitle = "Django Model"
    return render(
        request,
        "home.html",
        {"projtitle":projtitle}
    )