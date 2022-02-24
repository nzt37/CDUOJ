# Generated by Django 3.2.4 on 2021-12-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassStudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentUserName', models.CharField(default='', max_length=50)),
                ('studentNumber', models.CharField(max_length=50)),
                ('className', models.CharField(max_length=50)),
                ('studentRealName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='theClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(default='None', max_length=50)),
                ('classSize', models.CharField(default='None', max_length=50)),
                ('canjoinclass', models.CharField(default='open', max_length=50)),
            ],
        ),
    ]
