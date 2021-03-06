# coding: utf8

import time
import json
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from admin_panel.views import admin_forms
from admin_panel.user_tests import is_formateur
from consult_panel.models import Session, Inscription, Formation, Client
from consult_panel.models import Cours, Catalogue, Profile


@user_passes_test(is_formateur)
def pages_index(request):
    cours_list = []
    cours = Cours.objects.filter(
        session__formation__catalogue__profile__user=request.user
    ).select_related().distinct()
    for c in cours:
        cours_list.append({
            'title': c.session.formation.nom,
            'start': c.date_cours_debut.isoformat(),
            'end': c.date_cours_fin.isoformat(),
            'sessionId': c.session.id,
            'className': 'event-orange',
        })
    head = {
        'sessions': Session.objects.filter(
            formation__catalogue__profile__user=request.user
        ).distinct().count(),
        'inscrits': Inscription.objects.filter(
            session__formation__catalogue__profile__user=request.user
        ).distinct().count(),
        'formations': Formation.objects.filter(
            catalogue__profile__user=request.user
        ).distinct().count(),
        'clients': (Client.objects
                    .filter(catalogue__profile__user=request.user)
                    .distinct().count()),
        'catalogues': (Catalogue.objects.filter(profile__user=request.user)
                       .distinct().count()),
        'entreprises': (Profile.objects.get(user=request.user)
                        .liste_entreprises.count()),
    }

    for key, value in head.items():
        if key != 'inscrits' and value == 0:
            messages.info(
                request,
                (
                    'Pensez à rentrer toutes les données du menu sur la '
                    'gauche afin de pouvoir générer vos conventions'
                )
            )
            break

    return render(request, 'admin_pages_index.html', context={
        'page_title':   'Tableau de bord',
        'header':   False,
        'datas':   {
            'calendar_date': time.strftime('%Y-%m-%d'),
            'calendar_content': json.dumps(cours_list),
            'head': head
        },
    })


@user_passes_test(is_formateur)
def form(request, name):
    if request.method == 'POST':
        response = getattr(admin_forms, name)(request)
        return response if response is not None else redirect('consult/')
    else:
        messages.warning(request, 'Oops, vous vous êtes perdu...')
        return redirect('admin_index')
