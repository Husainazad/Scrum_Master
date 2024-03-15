from django.shortcuts import render, redirect
from .models import Certificate
from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == 'POST':
        cert_id = request.POST.get('cert_id')
        certificate = Certificate.objects.filter(certificate_id=cert_id).first()
        if certificate is not None:
            # Open the certificate file directly
            return redirect(f"http://127.0.0.1:8000/{certificate.certificate_file}")

        return HttpResponse("Invalid Certificate ID.")

    return render(request, 'scrum_app/index.html')