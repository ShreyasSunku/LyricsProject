# Generated by Django 3.2.7 on 2021-11-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lyrics', '0008_auto_20211001_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo_Image', models.ImageField(blank=True, null=True, upload_to='images/Logo/')),
            ],
        ),
    ]