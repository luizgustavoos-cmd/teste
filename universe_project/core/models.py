from django.db import models

class Cliente(models.Model): 

    nome = models.CharField(max_length=50)
    conta = models.CharField(max_length=10, unique=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) 
    email = models.EmailField(max_length=50, unique=True) 
    telefone = models.CharField(max_length=15)
    
    def save(self, *args, **kwargs):
        # Se ainda não tiver número de conta, gera um automaticamente
        if not self.conta:
            ultimo = Cliente.objects.all().order_by('-id').first()
            proximo_id = (ultimo.id + 1) if ultimo else 1
            self.conta = f"{proximo_id:06d}"  # Ex: 000001, 000002...
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Conta {self.conta} - {self.nome}"
