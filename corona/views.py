from django.shortcuts import render
import requests
import country_converter as coco

# Create your views here.
from django.template import RequestContext

api_url_base = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/"
headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "23a2def8fbmshf7ae7a8212cce73p1bbd6ejsn5712b6b8672b"
}


def index(request):
    api_url = '{0}cases_by_country.php'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    corona = response.json()
    country = corona['countries_stat']

    country_names = []
    for country in country:
        country_name = country['country_name']
        country_name = coco.convert(names=country_name, to='ISO2')

        country_names.append(country_name)

    api_url = '{0}worldstat.php'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    world_totals = response.json()

    context = {
        'corona': corona['countries_stat'],
        'world_totals': world_totals,
        'country_names': country_names
    }
    return render(request, 'corona/index.html', context)