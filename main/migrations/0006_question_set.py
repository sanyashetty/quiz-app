# Generated by Django 2.2.27 on 2022-12-05 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Set'),
        ),
    ]
