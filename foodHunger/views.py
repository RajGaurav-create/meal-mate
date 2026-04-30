from django.http import HttpResponse
def hello(request):
   return HttpResponse("Hello welcome to Django")

def thanks(request):
   return HttpResponse("Thank you  for using the django")