from ipware import get_client_ip
from .models import IpDeClientes
from django.http import HttpResponse

class IpIsValid:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        print("ip:", ip)
        IpDeClientes.objects.create(ip_client = str(ip))
        response = self.get_response(request)

        return response
        