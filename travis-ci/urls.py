from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('grade_conversion_calculator.urls')),
]
