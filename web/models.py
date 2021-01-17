from django.db import models
from core.models import Aluno

# Create your models here.
class Anamnese(models.Model):
    fever = models.BooleanField("Febre")
    fatigue = models.BooleanField("Cançaso")
    dry_cough = models.BooleanField("Tosse seca")
    body_pain = models.BooleanField("Dores no corpo")
    nasal_congestion = models.BooleanField("Congestão nasal")
    headache = models.BooleanField("Dor de cabeça")
    conjuntivite = models.BooleanField("Conjuntivite")
    sore_throat = models.BooleanField("Dor de garganta")
    diarreia = models.BooleanField()
    loss_of_smell_or_taste = models.BooleanField("Perda de olfato ou paladar")
    rash_or_discoloration = models.BooleanField("Erupção cutânea ou descoloração")

    # Não entendi como vamos pegar isso ainda
    # aluno = Aluno()
    datetime = models.DateTimeField("Data e hora da resposta", auto_now_add=True)
    autorizacao = models.BooleanField(default=True)