# Generated by Django 4.2.2 on 2023-06-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='skills',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.AddField(
            model_name='project',
            name='frameworks',
            field=models.ManyToManyField(related_name='framework', to='portfolio_app.framework'),
        ),
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(related_name='language', to='portfolio_app.language'),
        ),
    ]
