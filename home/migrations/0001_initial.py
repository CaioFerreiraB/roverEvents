# Generated by Django 2.1.4 on 2018-12-21 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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