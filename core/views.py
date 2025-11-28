from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from core.models import Airport, AirportRoute
from core.forms import AirportForm, AirportRouteForm, NodeSearchForm, LongestNodeForm, ShortestNodeForm
from core.utilities.node_utils import find_nth_route_node, get_longest_node_from_airport, get_shortest_node


# Dashboard
def dashboard(request):
    airports_count = Airport.objects.count()
    routes_count = AirportRoute.objects.count()
    longest_route = AirportRoute.objects.order_by('-duration').first()
    shortest_route = AirportRoute.objects.order_by('duration').first()
    latest_routes = AirportRoute.objects.order_by('-created_at')[:5]
    context = {
        'airports_count': airports_count,
        'routes_count': routes_count,
        'longest_route': longest_route,
        'shortest_route': shortest_route,
        'latest_routes': latest_routes,
    }
    return render(request, 'dashboard.html', context)



# Airport Create
def airport_create(request):
    form = AirportForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Airport created successfully!")
            return redirect('airport_list')
        else:
            messages.error(request, "Please fix the errors below.")
    return render(request, 'airport_form.html', {'form': form})


# Airport List
def airport_list(request):
    airports = Airport.objects.all().order_by('created_at')
    return render(request, 'airport_list.html', {'airports': airports})


# Airport Update
def airport_update(request, pk):
    airport = get_object_or_404(Airport, pk=pk)
    form = AirportForm(request.POST or None, instance=airport)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Airport updated successfully!")
            return redirect('airport_list')
        else:
            messages.error(request, "Please fix the errors below.")

    return render(request, 'airport_form.html', {'form': form})


# Route Create
def route_create(request):
    form = AirportRouteForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Route created successfully!")
            return redirect('route_list')
        else:
            messages.error(request, "Please fix the errors below.")

    return render(request, 'route_form.html', {'form': form})


# Route List
def route_list(request):
    routes = AirportRoute.objects.select_related('from_airport', 'to_airport').all()
    return render(request, 'route_list.html', {'routes': routes})


# Route Update
def route_update(request, pk):
    route = get_object_or_404(AirportRoute, pk=pk)
    form = AirportRouteForm(request.POST or None, instance=route)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Route updated successfully!")
            return redirect('route_list')
        else:
            messages.error(request, "Please fix the errors below.")

    return render(request, 'route_form.html', {'form': form})


# Find Nth Node
def find_nth_node(request):
    form = NodeSearchForm(request.POST or None)
    result = None
    error = None
    path_display = None

    if request.method == "POST" and form.is_valid():
        airport = form.cleaned_data['start_airport']
        position = form.cleaned_data['position']
        n = form.cleaned_data['n_value']

        result, path, error = find_nth_route_node(airport, position, n)

        if path:
            path_display = path

    return render(request, "find_nth_node.html", {
        "form": form,
        "result": result,
        "path": path_display,
        "error": error,
    })


# Longest Route
def longest_route_view(request):
    form = LongestNodeForm(request.POST or None)
    longest_routes = []

    if request.method == 'POST' and form.is_valid():
        start_airport = form.cleaned_data['start_airport']
        longest_routes = get_longest_node_from_airport(start_airport)

    context = {
        'form': form,
        'longest_routes': longest_routes,
    }
    return render(request, 'longest_route.html', context)


# Shortest Route
def shortest_route_view(request):
    form = ShortestNodeForm(request.POST or None)
    shortest_route = None

    if request.method == 'POST' and form.is_valid():
        from_airport = form.cleaned_data['from_airport']
        to_airport = form.cleaned_data['to_airport']
        shortest_route = get_shortest_node(from_airport, to_airport)

    context = {
        'form': form,
        'shortest_route': shortest_route
    }
    return render(request, 'shortest_route.html', context)
