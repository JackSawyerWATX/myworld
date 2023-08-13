
from django.http import HttpResponse
from django.template import loader
from .models import Record


def records(request):
    myrecords = Record.objects.all().values()
    template = loader.get_template('all_records.html')
    context = {
        'myrecords': myrecords
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    myrecord = Record.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myrecord': myrecord,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    context = {
        'request': request
    }
    return HttpResponse(template.render(context, request))

def testing(request):
  myrecords = Record.objects.all().values()
  mydata = Record.objects.all().values()
  # mydata = Record.objects.values_list('artist')
  mydata = Record.objects.all().order_by('artist').values()
  template = loader.get_template('template.html')
  context = {
    'firstname': 'Jonathan',
    'drt': ['Django Records & Tapes'],
    'myrecords': myrecords,
    'myrecords': mydata,
  }
  return HttpResponse(template.render(context, request))