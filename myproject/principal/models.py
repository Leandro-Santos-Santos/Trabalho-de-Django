from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    mensagem = models.TextField()

class Pedido(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    TIPO_HAMBURGUER_CHOICES = [
        ('classico', 'Clássico'),
        ('cheddar_bacon', 'Cheddar Bacon'),
        ('vegetariano', 'Vegetariano'),
        ('frango', 'Frango'),
        # Adicione mais tipos conforme necessário
    ]
    tipo_hamburguer = models.CharField(max_length=50, choices=TIPO_HAMBURGUER_CHOICES)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {self.tipo_hamburguer} - {self.valor_total}"

# Create your models here.
