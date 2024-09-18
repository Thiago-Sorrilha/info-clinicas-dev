# Generated by Django 3.2.6 on 2024-09-11 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome Completo')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], default=None, max_length=9, verbose_name='Sexo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('email', models.EmailField(blank=True, max_length=194, null=True, verbose_name='E-mail')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=194, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=10, verbose_name='Cidade')),
                ('pais', models.CharField(max_length=12, verbose_name='País')),
                ('CEP', models.CharField(max_length=9, verbose_name='CEP')),
                ('CRM', models.CharField(max_length=7, verbose_name='CRM')),
                ('clinica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinicas.clinica')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
                'db_table': 'medicos',
            },
        ),
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponivel', models.BooleanField(default=True)),
                ('data', models.DateField(verbose_name='Data disponível')),
                ('hora', models.TimeField(verbose_name='Horário disponível')),
                ('clinica', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clinicas.clinica')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicos.medicos')),
            ],
            options={
                'verbose_name': 'Disponibilidade',
                'verbose_name_plural': 'Disponibilidades',
                'db_table': 'disponibilidade',
            },
        ),
    ]
