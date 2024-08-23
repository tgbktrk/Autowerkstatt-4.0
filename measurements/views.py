from django.shortcuts import get_object_or_404, redirect, render
from measurements.forms import MeasurementCreateForm, MeasurementEditForm, FileUploadForm
from .models import Measurement, FileUploadModel
from cars.models import Car
from django.core.paginator import Paginator
import pandas as pd
import plotly.express as px
import plotly.io as pio
from django.contrib.auth.decorators import user_passes_test

def index(request):
    measurements = Measurement.objects.all() 
    cars = Car.objects.all()

    return render(request, 'measurements/list.html', {
        'cars': cars,
        'measurements': measurements,
    })

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_measurement(request):
    if request.method == "POST":
        form = MeasurementCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/measurements')
    else:
        form = MeasurementCreateForm()
    return render(request, "measurements/create-measurement.html", {
        "form": form,
    })

def measurement_list(request):
    measurements = Measurement.objects.all()
    measurements_with_dtc = []
    for measurement in measurements:
        dtc_codes = measurement.read_txt()
        measurements_with_dtc.append((measurement, dtc_codes))
    return render(request, 'measurements/measurement-list.html', {
        'measurements': measurements,
        'measurements_with_dtc': measurements_with_dtc
    })

def measurement_edit(request, slug):
    measurement = get_object_or_404(Measurement, slug=slug)
    
    if request.method == 'POST':
        form = MeasurementEditForm(request.POST, request.FILES, instance=measurement)
        
        if form.is_valid():
            if form.has_changed():
                form.save()
                return redirect('measurement_list')
            else:
                return render(request, 'measurements/measurement-edit.html', {
                    'form': form,
                    'measurement': measurement,
                    'no_changes': True
                })
        else:
            print(form.errors)
    else:
        form = MeasurementEditForm(instance=measurement)
    
    return render(request, 'measurements/measurement-edit.html', {
        'form': form,
        'measurement': measurement,
    })

def measurement_delete(request, slug):
    measurement = get_object_or_404(Measurement, slug=slug)
    if request.method == "POST":
        measurement.delete()
        return redirect("measurement_list")
    
    return render(request, "measurements/measurement-delete.html", {"measurement": measurement})

def upload(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = FileUploadModel(file=request.FILES["file"])
            model.save()
            return render(request, "measurements/success.html")
    else:
        form = FileUploadForm()
    return render(request, "measurements/upload.html", {"form": form})

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        measurements = Measurement.objects.filter(vin_number__contains=q).order_by("date")
        cars = Measurement.objects.all()
    else:
        return redirect("/measurements")
    
    return render(request, 'measurements/search.html',{
        'cars' : cars,
        'measurements' : measurements,
        })

def details(request, slug):
    measurement = Measurement.objects.get(slug=slug)
    dtc_codes = measurement.read_txt()
    df = measurement.read_csv()

    if df is not None:
        # Convert Timestamp to datetime if not already
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
        df = df.dropna(subset=['Timestamp'])  # Drop rows where Timestamp could not be parsed

        # Convert Timestamp to seconds from the start of the recording
        df['TimeSeconds'] = (df['Timestamp'] - df['Timestamp'].min()).dt.total_seconds()

        # Define a function to create a figure
        def create_figure(y_column):
            fig = px.line(df, x='TimeSeconds', y=y_column)
            fig.update_xaxes(
                title_text='Time (seconds)',
                showgrid=True
            )
            return fig

        # Generate figures
        fig1 = create_figure('BatteryVoltage')
        fig2 = create_figure('RPM')
        fig3 = create_figure('B1_S1_O2_Voltage')
        fig4 = create_figure('B1_S2_O2_Voltage')
        fig5 = create_figure('MAF')
        fig6 = create_figure('Intake_Pressure')
        fig7 = create_figure('Intake_Temp')
        fig8 = create_figure('Engine_Load')

        # Convert figures to HTML
        graph_html1 = pio.to_html(fig1, full_html=False)
        graph_html2 = pio.to_html(fig2, full_html=False)
        graph_html3 = pio.to_html(fig3, full_html=False)
        graph_html4 = pio.to_html(fig4, full_html=False)
        graph_html5 = pio.to_html(fig5, full_html=False)
        graph_html6 = pio.to_html(fig6, full_html=False)
        graph_html7 = pio.to_html(fig7, full_html=False)
        graph_html8 = pio.to_html(fig8, full_html=False)

    return render(request, 'measurements/details.html', {
        'graph_html1': graph_html1,
        'graph_html2': graph_html2,
        'graph_html3': graph_html3,
        'graph_html4': graph_html4,
        'graph_html5': graph_html5,
        'graph_html6': graph_html6,
        'graph_html7': graph_html7,
        'graph_html8': graph_html8,
        'dtc_codes' : dtc_codes
    })

def getMeasurementsByCar(request, slug):
    car = get_object_or_404(Car, slug=slug)
    measurements = Measurement.objects.filter(car__slug=slug).order_by("date")
    cars = Car.objects.all()

    paginator = Paginator(measurements, 3)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    print(page_obj.paginator.count)
    print(page_obj.paginator.num_pages)

    return render(request, 'measurements/index.html',{
        'car': car,
        'cars' : cars,
        'measurements' : measurements,
        'page_obj' : page_obj,
        'selectedCar' : slug
    })