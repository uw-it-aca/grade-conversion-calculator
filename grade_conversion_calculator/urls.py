from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^demo/?$', 'grade_conversion_calculator.views.demo'),
)
