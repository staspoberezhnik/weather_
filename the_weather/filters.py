from .models import NewCity
import django_filters


class CityFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    year_created = django_filters.NumberFilter(name='date_created',
                                               label='year created',
                                               lookup_expr='year', )
    month_created = django_filters.NumberFilter(name='date_created',
                                                label='month created',
                                                lookup_expr='month', )
    day_created = django_filters.NumberFilter(name='date_created',
                                              label='day created',
                                              lookup_expr='day', )

    class Meta:
        model = NewCity

        fields = [
            'name',
            'year_created',
            'month_created',
            'day_created',
        ]
