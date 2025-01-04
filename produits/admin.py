from django.contrib import admin
from .models import Bateau, Port, Voyage, Employeur, Client, Reservation, Passager, Billet, Bagage, Responsabilite, Enregistre, Effectue

@admin.register(Bateau)
class BateauAdmin(admin.ModelAdmin):
    list_display = ('no_bateau', 'nom_bateau', 'capacite_bateau', 'type_bateau')
    search_fields = ('nom_bateau', 'type_bateau')

@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    list_display = ('code_port', 'ville')
    search_fields = ('ville',)

@admin.register(Voyage)
class VoyageAdmin(admin.ModelAdmin):
    list_display = ('no_transport', 'code_port_quitte', 'code_port', 'datedepart', 'datearrive', 'duree_voyage')
    list_filter = ('datedepart', 'datearrive')
    search_fields = ('code_port__ville', 'code_port_quitte__ville')

@admin.register(Employeur)
class EmployeurAdmin(admin.ModelAdmin):
    list_display = ('id_emp', 'nom_emp', 'prenom_emp', 'poste_emp', 'adresse_emp')
    search_fields = ('nom_emp', 'prenom_emp', 'poste_emp')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('no_client', 'nom_client', 'prenom_client', 'num_client')
    search_fields = ('nom_client', 'prenom_client')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id_res', 'no_client', 'no_billet', 'date_res', 'tarif_res', 'quantite_res', 'total_tarif')
    list_filter = ('date_res',)
    search_fields = ('no_client__nom_client',)

@admin.register(Passager)
class PassagerAdmin(admin.ModelAdmin):
    list_display = ('no_passager', 'nom_passager', 'prenom_passager', 'age', 'is_adult')
    search_fields = ('nom_passager', 'prenom_passager')

@admin.register(Billet)
class BilletAdmin(admin.ModelAdmin):
    list_display = ('no_billet', 'no_passager', 'date_paiement', 'montants', 'mode_paiement', 'montant_ttc')
    list_filter = ('mode_paiement',)
    search_fields = ('no_passager__nom_passager',)

@admin.register(Bagage)
class BagageAdmin(admin.ModelAdmin):
    list_display = ('id_bagage', 'description', 'poids_total', 'frais_bagage', 'type_bagage', 'frais_par_kg')
    search_fields = ('description', 'type_bagage')

@admin.register(Responsabilite)
class ResponsabiliteAdmin(admin.ModelAdmin):
    list_display = ('id_emp', 'no_transport', 'type_responsabilite')
    search_fields = ('id_emp__nom_emp', 'no_transport__no_transport')

@admin.register(Enregistre)
class EnregistreAdmin(admin.ModelAdmin):
    list_display = ('no_passager', 'id_bagage', 'no_transport')
    search_fields = ('no_passager__nom_passager', 'id_bagage__description')

@admin.register(Effectue)
class EffectueAdmin(admin.ModelAdmin):
    list_display = ('no_bateau', 'no_transport')
    search_fields = ('no_bateau__nom_bateau', 'no_transport__no_transport')
