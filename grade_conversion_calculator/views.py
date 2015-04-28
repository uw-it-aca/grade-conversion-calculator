from django.template import RequestContext
from django.shortcuts import render_to_response


def demo(request):
    params = {}
    return render_to_response("demo.html", params, RequestContext(request))
