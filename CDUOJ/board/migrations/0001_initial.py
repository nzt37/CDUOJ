# Generated by Django 3.2.4 on 2021-12-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('classes', models.CharField(default='', max_length=50)),
                ('number', models.CharField(default='', max_length=50)),
                ('OJCount', models.IntegerField(default=4)),
                ('OJ', models.CharField(default='Codeforces|HDU|Vjudge|LPOJ|Others', max_length=50)),
                ('account', models.CharField(default='###|###|###|###|###', max_length=50)),
                ('acnum', models.CharField(default='0|0|0|0|0', max_length=50)),
                ('submitnum', models.CharField(default='0|0|0|0|0', max_length=50)),
                ('blogaddress', models.CharField(default='', max_length=500)),
                ('cfrate', models.CharField(default='0|0|0', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DailyBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('account', models.IntegerField(default=0)),
                ('collecttime', models.DateField(auto_now=True)),
                ('cfrate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DailyContestBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contestdate', models.DateField(auto_now=True)),
                ('teammember', models.CharField(max_length=100)),
                ('problemcount', models.IntegerField(default=0)),
                ('wronglist', models.CharField(max_length=1000)),
                ('wrongtime', models.CharField(max_length=1000)),
                ('aclist', models.CharField(max_length=1000)),
                ('actime', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SettingBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(default='University', max_length=100)),
                ('ojname', models.CharField(default='LPOJ', max_length=100)),
                ('openwiki', models.BooleanField(default=True)),
                ('openlanguage', models.CharField(default='C++|C|Python3|Python2|Swift5.1|Java', max_length=500)),
                ('openoi', models.BooleanField(default=True)),
                ('openstatus', models.BooleanField(default=True)),
                ('openvisitor', models.BooleanField(default=True)),
                ('openregister', models.BooleanField(default=True)),
                ('openselfstatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teammember', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=1500)),
                ('collecttime', models.DateField(auto_now=True)),
            ],
        ),
    ]
