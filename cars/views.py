from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from cars.forms import CarCreateForm, CarEditForm, ImageUploadForm
from cars.models import Car, ImageUploadModel

@login_required()
def car_list(request):
    cars = Car.objects.all()
    return render(request, "cars/car-list.html", {
        'cars': cars
    })

@login_required()
def create_car(request):
    if request.method == "POST":
        form = CarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("car_list")
    else:
        form = CarCreateForm()
    return render(request, "cars/create-car.html", {"form": form})
    
@login_required()
def edit_car(request, slug):
    car = get_object_or_404(Car, slug=slug)
    if request.method == "POST":
        form = CarEditForm(request.POST, request.FILES, instance=car)
        form.save()
        return redirect("car_list")
    else:
        form = CarEditForm(instance=car)

    return render(request, "cars/edit-car.html", {"form": form})

@login_required()
def delete_car(request, slug):
    car = get_object_or_404(Car, slug=slug)
    if request.method == "POST":
        car.delete()
        return redirect("car_list")
    
    return render(request, "cars/delete-car.html", {"car": car})

@login_required()
def upload(request):
    if(request.method == "POST"):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = ImageUploadModel(image=request.FILES["image"])
            model.save()
            return render(request, "cars/success.html")
    else:
        form = ImageUploadForm()
    return render(request, "cars/upload.html", {"form": form})

def search_by_owner(request):
    query = request.GET.get('q', '')
    if query:
        cars = Car.objects.filter(owner__icontains=query)
    else:
        cars = Car.objects.all()

    return render(request, 'cars/car-list.html', {'cars': cars})