from django.shortcuts import render, redirect
from .models import ArtWorx
from ..users.models import User

# Create your views here.
def index(request):
	if "id" not in request.session:
		return redirect("login_page")

	user = User.objects.get(id=request.session["id"])

	context = {
		"artworxs" : ArtWorx.objects.all(), "users" : User.objects.all(),
		"name": user.name, "curpts_user": user.points+150,
	}
	return render(request, "artworx/index.html", context)

def show(request, id):
	if "id" not in request.session:
		return redirect("login_page")

	context = {
		"artworx": ArtWorx.objects.get(id=id)
	}
	return render(request, "artworx/show.html", context)

def new(request):
	if "id" not in request.session:
		return redirect("login_page")

	return render(request, "artworx/new.html")

def join(request, id):
	if "id" not in request.session:
		return redirect("login_page")
	
	trip = ArtWorx.objects.get(id=id)
	user = User.objects.get(id=request.session["id"])

	# trip.travellers.add(user)

	return redirect("travels")

def create(request):
	if request.method != "POST":
		return redirect("travels")
	elif "id" not in request.session:
		return redirect("login_page")


	ArtWorx.objects.create(artname=request.POST["artname"], description=request.POST["description"], creator=User.objects.get(id=request.session["id"]))





	return redirect("travels")