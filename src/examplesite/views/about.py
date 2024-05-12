from django.http import HttpResponse
from django.views import View


class AboutView(View):
    def get(self, request):
        return HttpResponse("This is the about page.")
