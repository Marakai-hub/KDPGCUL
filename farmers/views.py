from django.shortcuts import render, redirect, get_object_or_404
from .models import Farmer, Query, Harvest, PlantingReport
from .forms import FarmerForm, QueryForm, HarvestForm, PlantingReportForm

def home(request):
    return render(request, 'farmers/home.html')

def register_farmer(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            new_farmer = form.save()
            # Redirect to a new page with the farmer's ID
            return redirect('display_farmer_id', farmer_id=new_farmer.farmer_id)
    else:
        form = FarmerForm()
    return render(request, 'farmers/register.html', {'form': form})

def display_farmer_id(request, farmer_id):
    farmer = get_object_or_404(Farmer, farmer_id=farmer_id)
    return render(request, 'farmers/display_farmer_id.html', {'farmer': farmer})

def farmer_dashboard(request, farmer_id):
    # Logic for showing services or access page based on farmer ID
    farmer = get_object_or_404(Farmer, farmer_id=farmer_id)
    return render(request, 'farmers/farmer_dashboard.html', {'farmer': farmer})


def report_issue(request, farmer_id):
    farmer = get_object_or_404(Farmer, farmer_id=farmer_id)
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.farmer = farmer
            query.save()
            return redirect('home')
    else:
        form = QueryForm()
    return render(request, 'farmers/report_issue.html', {'form': form, 'farmer': farmer})

def report_harvest(request, farmer_id):
    farmer = get_object_or_404(Farmer, farmer_id=farmer_id)
    if request.method == 'POST':
        form = HarvestForm(request.POST)
        if form.is_valid():
            harvest = form.save(commit=False)
            harvest.farmer = farmer
            harvest.save()
            return redirect('home')
    else:
        form = HarvestForm()
    return render(request, 'farmers/report_harvest.html', {'form': form, 'farmer': farmer})

def report_planting(request, farmer_id):
    farmer = get_object_or_404(Farmer, farmer_id=farmer_id)
    if request.method == 'POST':
        form = PlantingReportForm(request.POST)
        if form.is_valid():
            planting = form.save(commit=False)
            planting.farmer = farmer
            planting.save()
            return redirect('home')
    else:
        form = PlantingReportForm()
    return render(request, 'farmers/report_planting.html', {'form': form, 'farmer': farmer})

def view_harvests(request, farmer_id):
    farmer = get_object_or_404(Farmer, farmer_id=farmer_id)
    harvests = Harvest.objects.filter(farmer=farmer)
    return render(request, 'farmers/view_harvests.html', {'harvests': harvests, 'farmer': farmer})

def view_planting_reports(request, farmer_id):
    farmer = get_object_or_404(Farmer, farmer_id=farmer_id)
    plantings = PlantingReport.objects.filter(farmer=farmer)
    return render(request, 'farmers/view_planting_reports.html', {'plantings': plantings, 'farmer': farmer})

def upcoming_events(request):
    # Stub for upcoming events; later add a model to manage events if needed
    events = [
        {"title": "Annual Potato Festival", "date": "2024-11-25"},
        {"title": "Harvest Season Meeting", "date": "2025-02-10"},
    ]
    return render(request, 'farmers/upcoming_events.html', {'events': events})
