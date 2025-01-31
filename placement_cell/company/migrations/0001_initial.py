# Generated by Django 3.2.24 on 2024-03-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('about', models.CharField(max_length=45)),
                ('mail', models.CharField(max_length=45)),
                ('phone', models.IntegerField()),
                ('status', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]
