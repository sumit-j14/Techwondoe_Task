# Generated by Django 4.1.1 on 2022-09-23 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('UUID', models.IntegerField(primary_key=True, serialize=False)),
                ('Team_lead', models.CharField(max_length=20)),
                ('CompanyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_app.company')),
            ],
        ),
    ]
