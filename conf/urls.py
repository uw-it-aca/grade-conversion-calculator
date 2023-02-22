from django.conf.urls import include
from django.urls import re_path
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    re_path(r'^', include('grade_conversion_calculator.urls')),
    re_path(
        r'^jsi18n/$',
        JavaScriptCatalog.as_view(packages=['grade_conversion_calculator']),
        name='javascript-catalog')
]
