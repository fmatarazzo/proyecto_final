# Generated by Django 4.0.4 on 2022-06-02 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquitectura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archviz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('pagina_web', models.URLField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]