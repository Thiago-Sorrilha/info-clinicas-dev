from django.db import models

from info_clinicas.clinicas.models import Clinica


class Medicos(models.Model):

    SEXO_ESCOLHA = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro"),
    ]

    nome_completo = models.CharField(verbose_name="Nome Completo", max_length=194)
    sexo = models.CharField(verbose_name="Sexo", max_length=9, choices=SEXO_ESCOLHA, default=None)
    cpf = models.CharField(verbose_name="CPF", max_length=11)
    email = models.EmailField(verbose_name="E-mail", max_length=194, blank=True, null=True)
    data_nascimento = models.DateField(verbose_name="Data de nascimento", auto_now=False, auto_now_add=False)
    telefone = models.CharField(verbose_name="Telefone", max_length=11)
    endereco = models.CharField(verbose_name="Endereço", max_length=194)
    bairro = models.CharField(verbose_name="Bairro", max_length=30)
    cidade = models.CharField(verbose_name="Cidade", max_length=10)
    pais = models.CharField(verbose_name="País", max_length=12)
    CEP = models.CharField(verbose_name="CEP", max_length=9)
    CRM = models.CharField(verbose_name="CRM", max_length=7)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
        db_table = "medicos"

    def __str__(self):
        return f'{self.id} - {self.nome_completo}'


class Disponibilidade(models.Model):
    
    disponivel = models.BooleanField(default=True)
    medico = models.ForeignKey(Medicos, on_delete=models.PROTECT)
    data = models.DateField(verbose_name="Data disponível", auto_now=False, auto_now_add=False)
    hora = models.TimeField(verbose_name="Horário disponível", auto_now=False, auto_now_add=False)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, blank=True, null=False)

    class Meta:
        verbose_name = "Disponibilidade"
        verbose_name_plural = "Disponibilidades"
        db_table = "disponibilidade"

    def __str__(self):
        return f'{self.id} - {self.data}-{self.hora} - {self.medico.nome_completo}'




