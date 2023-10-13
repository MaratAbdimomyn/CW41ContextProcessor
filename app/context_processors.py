from .models import *

def my_context(request):
    phones = Phone.objects.all()
    return {'phones': phones}