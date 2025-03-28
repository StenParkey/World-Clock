# filepath: clockapp/views.py
import datetime
import pytz
from django.shortcuts import render

# List of timezones
timezones = pytz.all_timezones

def world_clock(request):
    local_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    selected_times = []
    num_dropdowns = int(request.POST.get("num_dropdowns", 1))  # Default to 1 dropdown
    form_submitted = False  # Flag to track if the form was submitted

    if request.method == "POST":
        form_submitted = True
        for i in range(num_dropdowns):
            selected_timezone = request.POST.get(f"timezone_{i}")
            if selected_timezone:
                timezone = pytz.timezone(selected_timezone)
                current_time = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
                selected_times.append((selected_timezone, current_time))
            else:
                selected_times.append(("Please select a timezone.", ""))

    return render(request, "clockapp/world_clock.html", {
        "local_time": local_time,
        "timezones": timezones,
        "selected_times": selected_times,
        "num_dropdowns": num_dropdowns,  # Pass the number of dropdowns to the template
        "form_submitted": form_submitted,  # Pass the form submission status
    })