# Generated by Django 4.2.7 on 2023-12-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('sexe', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('ville', models.CharField(max_length=100)),
                ('niveau', models.CharField(max_length=100)),
                ('specialite', models.CharField(max_length=100)),
                ('domaine', models.CharField(max_length=100)),
                ('poste', models.CharField(max_length=100)),
                ('competences', models.CharField(max_length=100)),
            ],
        ),
    ]
