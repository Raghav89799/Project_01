from django.http import HttpResponse

def Home_page(request):
    return HttpResponse("This is home Page......")