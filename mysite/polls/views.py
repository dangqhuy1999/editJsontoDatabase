from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# view1 return  hello in web browser
def index(request):
	myname = "HuyDang"
	myasset = ["dienthoai","may tinh", 5,"Nha ngheo"]
	context = {"name":myname, "asset": myasset}
	return render(request, "polls/index.html", context)


# view2 return  hello in web browser
def haft(request):
	return HttpResponse("<h1>huydang ne</h1><p>huydang2</p>")

	
