# Generated by Django 3.2.7 on 2021-09-25 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lyrics', '0003_auto_20210921_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyrics',
            name='Actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lyrics.actor'),
        ),
    ]
