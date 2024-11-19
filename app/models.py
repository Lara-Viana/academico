from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

#antigo leitor
class Aluno(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do aluno")
    nome_da_mae = models.CharField(max_length=100, verbose_name="Mãe do aluno")
    nome_do_pai = models.CharField(max_length=100, verbose_name="Pai do aluno")
    email = models.CharField(max_length=100, verbose_name="Email do aluno")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF do aluno")
    data_nasc = models.DateField(verbose_name="Data de nascimento") #antiga data_publi
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

class Area(models.Model): #antigo genero
    nome = models.CharField(max_length=100, verbose_name="Gênero")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"
