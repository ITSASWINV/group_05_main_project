# Generated by Django 3.2.24 on 2024-03-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumini',
            fields=[
                ('alumini_id', models.AutoField(db_column='alumini__id', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('mail', models.CharField(max_length=45)),
                ('phone', models.IntegerField()),
                ('career_path', models.CharField(max_length=45)),
                ('experience', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'alumini',
            },
        ),
    ]
