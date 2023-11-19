# json_viewer/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import LogEntry
import json

def display_json(request):
    entries = LogEntry.objects.values()
    data = list(entries)
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})

def index(request):
    return render(request, 'index.html')

def save_json_data(request):
    # Specify the path to your JSON file
    json_file_path = 'C:\\Users\\DELL\\PycharmProjects\\pythonProject\\data.json'

    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)

        # Save each entry in the JSON data to the database
        for entry in json_data:
            # Check if an entry with the same ID already exists
            entry_id = entry['timestamp']
            if entry_id is not None and LogEntry.objects.filter(timestamp=entry_id).exists():
                return JsonResponse({"message": "Duplicate entry, skipping"}, status=200)

            # Extract all key-value pairs from the entry

            # Save the entry to the database
            string=''
            for k in entry['metadata']:
                string += entry['metadata'][k]+' '
            LogEntry.objects.create(
                level=entry['level'],
                message=entry['message'],
                resourceId=entry['resourceId'],
                timestamp=entry['timestamp'],
                traceId=entry['traceId'],
                spanId=entry['spanId'],
                commit=entry['commit'],
                parentResourceId=string,
            ).save()

        return JsonResponse({"message": "JSON data saved successfully"}, status=201)

    except FileNotFoundError:
        return JsonResponse({"error": "JSON file not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

from django.db.models import Q

def search(request):
    if request.method == 'GET':
        field = request.GET.get('field', None)
        search_text = request.GET.get('search_text', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        query = Q()  # Create an empty Q object
        print(field,search_text,start_date,end_date)
        cd1,cd2=False,False
        if start_date and end_date:
            # If both start_date and end_date are provided, perform date range search

            results = LogEntry.objects.filter(timestamp__range=[start_date, end_date]).values()

        else:
            if field == 'level':
                query |= Q(level__icontains=search_text)
            elif field == 'message':
                query |= Q(message__icontains=search_text)
            elif field == 'resourceId':
                query |= Q(resourceId__icontains=search_text)
            elif field == 'timestamp':
                query |= Q(timestamp__icontains=search_text)
            elif field == 'traceId':
                query |= Q(traceId__icontains=search_text)
            elif field == 'spanId':
                query |= Q(spanId__icontains=search_text)
            elif field == 'commit':
                query |= Q(commit__icontains=search_text)
            elif field == 'parentResourceId':
                query |= Q(parentResourceId__icontains=search_text)
            else:
                # If no specific field is selected, search across all fields
                query |= (
                    Q(level__icontains=search_text)
                    | Q(message__icontains=search_text)
                    | Q(resourceId__icontains=search_text)
                    | Q(timestamp__icontains=search_text)
                    | Q(traceId__icontains=search_text)
                    | Q(spanId__icontains=search_text)
                    | Q(commit__icontains=search_text)
                    | Q(parentResourceId__icontains=search_text)
                )

            results = LogEntry.objects.filter(query).values()


        data = list(results)
        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})

    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

#
# def search(request):
#     if request.method == 'GET':
#         field = request.GET.get('field', None)
#         search_text = request.GET.get('search_text', None)
#         start_date = request.GET.get('start_date', None)
#         end_date = request.GET.get('end_date', None)
#
#         query = Q()  # Create an empty Q object
#
#         if field == 'level':
#             query |= Q(level__icontains=search_text)
#         elif field == 'message':
#             query |= Q(message__icontains=search_text)
#         elif field == 'resourceId':
#             query |= Q(resourceId__icontains=search_text)
#         elif field == 'timestamp':
#             query |= Q(timestamp__icontains=search_text)
#         elif field == 'traceId':
#             query |= Q(traceId__icontains=search_text)
#         elif field == 'spanId':
#             query |= Q(spanId__icontains=search_text)
#         elif field == 'commit':
#             query |= Q(commit__icontains=search_text)
#         elif field == 'parentResourceId':
#             query |= Q(parentResourceId__icontains=search_text)
#         else:
#             # If no specific field is selected, search across all fields
#             query |= (
#                 Q(level__icontains=search_text)
#                 | Q(message__icontains=search_text)
#                 | Q(resourceId__icontains=search_text)
#                 | Q(traceId__icontains=search_text)
#                 | Q(spanId__icontains=search_text)
#                 | Q(commit__icontains=search_text)
#                 | Q(parentResourceId__icontains=search_text)
#             )
#
#         # Add the date range condition
#         if start_date and end_date:
#             query &= (Q(timestamp__range=[start_date, end_date]))
#
#         results = list(LogEntry.objects.filter(query).values())
#
#         data = results
#         return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})
#
#     else:
#         return JsonResponse({"error": "Invalid request method"}, status=400)

