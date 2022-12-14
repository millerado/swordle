# Generated by Django 4.1.2 on 2022-10-14 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hidden_word', models.CharField(max_length=6)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=6)),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.puzzle')),
            ],
        ),
    ]
