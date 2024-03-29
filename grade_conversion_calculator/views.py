# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.views.generic import TemplateView


class DemoView(TemplateView):
    template_name = 'demo.html'
