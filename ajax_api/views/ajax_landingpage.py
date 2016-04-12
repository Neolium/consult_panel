#encoding: UTF-8

from django.http import JsonResponse
from consult_panel.models import EmailForBeta

"""
    This is the ajax part for the landing page
    @author=mastercraft
"""

def add_email(request):
    if 'email' in request.GET:
        try:
            email = EmailForBeta.objects.get_or_create(email=request.GET.get('email'))
            email.save()
            #send confirmation email
            status = "success"
            message = "Vous avez reçu un email de confirmation !"
        except:
            status = "error"
            message = "Une erreur est survenu, veuillez réessayer plus tard."
            
    return JsonResponse({
        "status"    :   status,
        "message"        :   message
    });
        
            
        
        
    
