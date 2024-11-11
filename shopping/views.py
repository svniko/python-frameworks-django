from django.shortcuts import render, redirect

shop_list = ["bread", "butter", "cheese"]
# Create your views here.

def index(request):
    return render(request, "shopping/index.html",{
        "shop_list":shop_list,
        "title":'Shopping',
    })

def add(request):
    if request.method == "POST":
        item = request.POST.get("item")
        shop_list.append(item)
        return redirect("shopping:index")
    return render(request, "shopping/add.html")