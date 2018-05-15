from django.shortcuts import render
import requests
from .forms import SelectCityForm, InputCityForm
from .models import ExistCity, NewCity
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from.filters import CityFilter
# Create your views here.


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c570c535821c0558cceee4b7a9649e95'
    print(request.POST)
    if request.POST:
        form = InputCityForm(request.POST)
        city = form.data['name']
        req = requests.get(url.format(city)).json()
        if req['cod'] == 200:
            city_data = form.save(commit=False)
            city_data.name = city
            city_data.temperature = req['main']['temp']
            city_data.icon = req['weather'][0]['icon']
            city_data.description = req['weather'][0]['description']
            form.save()

            weather = {
                'city': city,
                'temperature': req['main']['temp'],
                'description': req['weather'][0]['description'],
                'icon': req['weather'][0]['icon'],
            }
            inputform = InputCityForm()
            selectform = SelectCityForm()
            context = {'weather': weather,
                       'inputform': inputform,
                       'selectform': selectform,
                       }

            return render(request, 'home_page.html', context)
        else:
            inputform = InputCityForm()
            selectform = SelectCityForm()
            context = {'inputform': inputform,
                       'selectform': selectform,
                       'error': 'true'}
            return render(request, 'home_page.html', context)

    else:
        inputform = InputCityForm()
        selectform = SelectCityForm()
        context = {'inputform': inputform,
                   'selectform': selectform}
        return render(request, 'home_page.html', context)


def filtered_history(request):
    city_filtered = CityFilter(
            request.GET,
            queryset=NewCity.objects.all().order_by("-date_created")
        )

    paginator = Paginator(city_filtered.qs, 10)  # Show 10  per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'filter': city_filtered,
        'weather': queryset,
        'page_request_var': page_request_var,
        }
    return render(request, 'filtered_history.html', context)


