# Generated by Django 3.2.7 on 2021-10-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0005_auto_20210929_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_round', models.CharField(default=None, max_length=10, null=True)),
            ],
        ),
    ]