# Generated by Django 3.0 on 2020-01-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.CharField(max_length=50)),
                ('sname', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('desig', models.CharField(max_length=50)),
                ('directno', models.CharField(blank=True, max_length=50, null=True)),
                ('eabxno', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('emailid', models.EmailField(blank=True, max_length=50, null=True)),
                ('office', models.CharField(max_length=50)),
            ],
        ),
    ]
