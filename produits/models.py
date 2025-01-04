from django.db import models

class Bateau(models.Model):
    no_bateau = models.AutoField(primary_key=True)
    nom_bateau = models.CharField(max_length=128)
    capacite_bateau = models.CharField(max_length=128)
    type_bateau = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nom_bateau} ({self.type_bateau})"

    def capacite_max(self):
        return f"Capacité : {self.capacite_bateau}"


class Port(models.Model):
    code_port = models.AutoField(primary_key=True)
    ville = models.CharField(max_length=128)

    def __str__(self):
        return self.ville


class Voyage(models.Model):
    no_transport = models.AutoField(primary_key=True)
    code_port = models.ForeignKey(Port, related_name='voyages_arrivee', on_delete=models.CASCADE)
    code_port_quitte = models.ForeignKey(Port, related_name='voyages_depart', on_delete=models.CASCADE)
    datedepart = models.DateTimeField()
    datearrive = models.DateTimeField()

    def __str__(self):
        return f"Voyage {self.no_transport} de {self.code_port_quitte.ville} à {self.code_port.ville}"

    def duree_voyage(self):
        return (self.datearrive - self.datedepart).total_seconds() / 3600  # Retourne la durée en heures


class Employeur(models.Model):
    id_emp = models.AutoField(primary_key=True)
    nom_emp = models.CharField(max_length=128)
    prenom_emp = models.CharField(max_length=128, null=True, blank=True)
    poste_emp = models.CharField(max_length=128)
    adresse_emp = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nom_emp} {self.prenom_emp} - {self.poste_emp}"


class Client(models.Model):
    no_client = models.AutoField(primary_key=True)
    nom_client = models.CharField(max_length=128)
    prenom_client = models.CharField(max_length=128, null=True, blank=True)
    num_client = models.BigIntegerField()

    def __str__(self):
        return f"{self.nom_client} {self.prenom_client}"


class Reservation(models.Model):
    id_res = models.AutoField(primary_key=True)
    no_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    no_billet = models.ForeignKey('Billet', on_delete=models.CASCADE)
    date_res = models.DateTimeField()
    tarif_res = models.DecimalField(max_digits=13, decimal_places=2)
    quantite_res = models.IntegerField()

    def __str__(self):
        return f"Réservation {self.id_res} par {self.no_client}"

    def total_tarif(self):
        return self.tarif_res * self.quantite_res


class Passager(models.Model):
    no_passager = models.AutoField(primary_key=True)
    id_res = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    nom_passager = models.CharField(max_length=128)
    prenom_passager = models.CharField(max_length=128, null=True, blank=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.nom_passager} {self.prenom_passager}"

    def is_adult(self):
        return self.age >= 18


class Billet(models.Model):
    no_billet = models.AutoField(primary_key=True)
    no_passager = models.ForeignKey(Passager, on_delete=models.CASCADE)
    date_paiement = models.DateTimeField()
    montants = models.DecimalField(max_digits=13, decimal_places=2)
    mode_paiement = models.CharField(max_length=128)

    def __str__(self):
        return f"Billet {self.no_billet} - {self.mode_paiement}"

    def montant_ttc(self, taxe=0.2):
        return self.montants * (1 + taxe)


class Bagage(models.Model):
    id_bagage = models.AutoField(primary_key=True)
    description = models.CharField(max_length=128)
    poids_total = models.IntegerField()
    frais_bagage = models.DecimalField(max_digits=13, decimal_places=2)
    type_bagage = models.CharField(max_length=128)

    def __str__(self):
        return f"Bagage {self.id_bagage} - {self.type_bagage}"

    def frais_par_kg(self):
        return self.frais_bagage / self.poids_total if self.poids_total > 0 else 0


class Responsabilite(models.Model):
    id_emp = models.ForeignKey(Employeur, on_delete=models.CASCADE)
    no_transport = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    type_responsabilite = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.id_emp} responsable pour {self.no_transport}"

    class Meta:
        unique_together = ('id_emp', 'no_transport')


class Enregistre(models.Model):
    no_passager = models.ForeignKey(Passager, on_delete=models.CASCADE)
    id_bagage = models.ForeignKey(Bagage, on_delete=models.CASCADE)
    no_transport = models.ForeignKey(Voyage, on_delete=models.CASCADE)

    def __str__(self):
        return f"Enregistrement {self.no_passager} - {self.id_bagage}"

    class Meta:
        unique_together = ('no_passager', 'id_bagage', 'no_transport')


class Effectue(models.Model):
    no_bateau = models.ForeignKey(Bateau, on_delete=models.CASCADE)
    no_transport = models.ForeignKey(Voyage, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.no_bateau} effectue {self.no_transport}"

    class Meta:
        unique_together = ('no_bateau', 'no_transport')
