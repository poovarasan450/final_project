from base.models import Category
def info(request):
    return {'data':'on saturday we have placement festival at 4pm'}

def extract_categories(request):
    
    return {'categories':Category.objects.all()}

