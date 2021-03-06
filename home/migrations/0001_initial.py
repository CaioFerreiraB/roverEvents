# Generated by Django 2.1.4 on 2019-02-04 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('arquivo', models.FileField(upload_to='')),
                ('capa', models.FileField(upload_to='')),
                ('resumo', models.TextField(default='resumo')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numeral', models.IntegerField()),
                ('estado', models.CharField(max_length=2)),
                ('diretor', models.CharField(max_length=200)),
                ('email_diretor', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('ficha_medica', models.FileField(upload_to='')),
                ('autorizacao', models.FileField(upload_to='')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Grupo')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='grupo',
            unique_together={('nome', 'numeral', 'estado')},
        ),
        migrations.AlterUniqueTogether(
            name='participante',
            unique_together={('nome', 'idade', 'email', 'grupo')},
        ),
    ]
