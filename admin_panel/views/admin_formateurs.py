from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import user_passes_test
from admin_panel.forms import *
from admin_panel.user_tests import *


@user_passes_test(is_formateur)
def formateurs_index(request):
    return render(request, 'admin_formateurs_index.html', context={
                  'page_title':   'Gestion des formateurs',
                  'profiles_list': Profile.objects.all()
                  })


@user_passes_test(is_formateur)
def formateurs_add(request):
    return render(request, 'admin_formateurs_add.html', {
                  'page_title': 'Ajouter une formation',
                  'form': ProfileForm()
                  })


@user_passes_test(is_formateur)
def formateurs_edit(request, id):
    return render(request, 'admin_formateurs_edit.html', {
                  'page_title': 'Editer une formation',
                  'form': ProfileForm(instance=Profile.objects.get(pk=id))
                  })
