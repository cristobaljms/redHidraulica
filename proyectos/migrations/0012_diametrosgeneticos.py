# Generated by Django 2.1.2 on 2018-11-25 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0011_delete_diametrosgeneticos'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiametrosGeneticos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diametro', models.FloatField(default=0)),
                ('costo', models.FloatField(default=0)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Proyecto')),
            ],
        ),
    ]