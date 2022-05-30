# Generated by Django 4.0.4 on 2022-05-30 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('Sector', models.CharField(blank=True, max_length=100, null=True)),
                ('Mkt_Cap', models.CharField(blank=True, max_length=100, null=True)),
                ('Turnover', models.CharField(blank=True, max_length=100, null=True)),
                ('Traded_Value', models.CharField(blank=True, max_length=100, null=True)),
                ('Pre_Index', models.CharField(blank=True, max_length=100, null=True)),
                ('Cur_Index', models.CharField(blank=True, max_length=100, null=True)),
                ('N_Chg', models.CharField(blank=True, max_length=100, null=True)),
                ('M_CAP_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('T_Cpt_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'AllShare',
            },
        ),
        migrations.CreateModel(
            name='BoardMeetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(blank=True, max_length=100, null=True)),
                ('CompanyName', models.CharField(blank=True, max_length=100, null=True)),
                ('AC_Period', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'BoardMeetings',
            },
        ),
        migrations.CreateModel(
            name='Closing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('Ticker', models.CharField(blank=True, max_length=100, null=True)),
                ('CompanyName', models.CharField(blank=True, max_length=100, null=True)),
                ('Open', models.CharField(blank=True, max_length=100, null=True)),
                ('High', models.CharField(blank=True, max_length=100, null=True)),
                ('Low', models.CharField(blank=True, max_length=100, null=True)),
                ('Close', models.CharField(blank=True, max_length=100, null=True)),
                ('Volume', models.CharField(blank=True, max_length=100, null=True)),
                ('LDCP', models.CharField(blank=True, max_length=100, null=True)),
                ('Change', models.CharField(blank=True, max_length=100, null=True)),
                ('change_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Closing',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('CURRENCY', models.CharField(blank=True, max_length=100, null=True)),
                ('READY', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Currency',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('Turn_Over', models.CharField(blank=True, max_length=100, null=True)),
                ('Trade_value', models.CharField(blank=True, max_length=100, null=True)),
                ('market_capitalization', models.CharField(blank=True, max_length=100, null=True)),
                ('Equal', models.CharField(blank=True, max_length=100, null=True)),
                ('Total', models.CharField(blank=True, max_length=100, null=True)),
                ('Kse_100', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Header',
            },
        ),
        migrations.CreateModel(
            name='Header2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('Indexes', models.CharField(blank=True, max_length=100, null=True)),
                ('Previos_Index', models.CharField(blank=True, max_length=100, null=True)),
                ('Current_Index', models.CharField(blank=True, max_length=100, null=True)),
                ('High', models.CharField(blank=True, max_length=100, null=True)),
                ('Low', models.CharField(blank=True, max_length=100, null=True)),
                ('NetChange_points', models.CharField(blank=True, max_length=100, null=True)),
                ('NetChange_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('TurnOver', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Header2',
            },
        ),
        migrations.CreateModel(
            name='InternationalCommodities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('Crude_oil', models.CharField(blank=True, max_length=100, null=True)),
                ('Brent', models.CharField(blank=True, max_length=100, null=True)),
                ('Gold', models.CharField(blank=True, max_length=100, null=True)),
                ('Silver', models.CharField(blank=True, max_length=100, null=True)),
                ('Platinum', models.CharField(blank=True, max_length=100, null=True)),
                ('Copper', models.CharField(blank=True, max_length=100, null=True)),
                ('Cotton', models.CharField(blank=True, max_length=100, null=True)),
                ('Sugar', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'InternationalCommodities',
            },
        ),
        migrations.CreateModel(
            name='Kibor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('Week_1', models.CharField(blank=True, max_length=100, null=True)),
                ('Week_2', models.CharField(blank=True, max_length=100, null=True)),
                ('Month_1', models.CharField(blank=True, max_length=100, null=True)),
                ('Month_3', models.CharField(blank=True, max_length=100, null=True)),
                ('Month_6', models.CharField(blank=True, max_length=100, null=True)),
                ('Month_9', models.CharField(blank=True, max_length=100, null=True)),
                ('Year_1', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Kibor',
            },
        ),
        migrations.CreateModel(
            name='KSE100Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('Symbol', models.CharField(blank=True, max_length=100, null=True)),
                ('SCRIP', models.CharField(blank=True, max_length=100, null=True)),
                ('LDCP', models.CharField(blank=True, max_length=100, null=True)),
                ('CURRENT', models.CharField(blank=True, max_length=100, null=True)),
                ('CHANGE', models.CharField(blank=True, max_length=100, null=True)),
                ('CHANGE_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('IDX_WTG_percent', models.CharField(blank=True, max_length=100, null=True)),
                ('IDX_POINT', models.CharField(blank=True, max_length=100, null=True)),
                ('VOLUME', models.CharField(blank=True, max_length=100, null=True)),
                ('FREEFLOAT', models.CharField(blank=True, max_length=100, null=True)),
                ('MARKET_CAP', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'KSE100Index',
            },
        ),
        migrations.CreateModel(
            name='Libor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('overnight', models.CharField(blank=True, max_length=100, null=True)),
                ('Month_1', models.CharField(blank=True, max_length=100, null=True)),
                ('Month_3', models.CharField(blank=True, max_length=100, null=True)),
                ('Month_6', models.CharField(blank=True, max_length=100, null=True)),
                ('Month_12', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Libor',
            },
        ),
        migrations.CreateModel(
            name='LocalCommodities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('urea_sona', models.CharField(blank=True, max_length=100, null=True)),
                ('DAP', models.CharField(blank=True, max_length=100, null=True)),
                ('Petrol', models.CharField(blank=True, max_length=100, null=True)),
                ('Diesel', models.CharField(blank=True, max_length=100, null=True)),
                ('LPG', models.CharField(blank=True, max_length=100, null=True)),
                ('Sugar', models.CharField(blank=True, max_length=100, null=True)),
                ('Cement', models.CharField(blank=True, max_length=100, null=True)),
                ('Gold', models.CharField(blank=True, max_length=100, null=True)),
                ('Silver', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'LocalCommodities',
            },
        ),
        migrations.CreateModel(
            name='PKRV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-05-30')),
                ('W1', models.CharField(blank=True, max_length=100, null=True)),
                ('W2', models.CharField(blank=True, max_length=100, null=True)),
                ('M1', models.CharField(blank=True, max_length=100, null=True)),
                ('M2', models.CharField(blank=True, max_length=100, null=True)),
                ('M3', models.CharField(blank=True, max_length=100, null=True)),
                ('M4', models.CharField(blank=True, max_length=100, null=True)),
                ('M6', models.CharField(blank=True, max_length=100, null=True)),
                ('M9', models.CharField(blank=True, max_length=100, null=True)),
                ('Y1', models.CharField(blank=True, max_length=100, null=True)),
                ('Y2', models.CharField(blank=True, max_length=100, null=True)),
                ('Y3', models.CharField(blank=True, max_length=100, null=True)),
                ('Y4', models.CharField(blank=True, max_length=100, null=True)),
                ('Y5', models.CharField(blank=True, max_length=100, null=True)),
                ('Y6', models.CharField(blank=True, max_length=100, null=True)),
                ('Y7', models.CharField(blank=True, max_length=100, null=True)),
                ('Y8', models.CharField(blank=True, max_length=100, null=True)),
                ('Y9', models.CharField(blank=True, max_length=100, null=True)),
                ('Y10', models.CharField(blank=True, max_length=100, null=True)),
                ('Y15', models.CharField(blank=True, max_length=100, null=True)),
                ('Y20', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'PKRV',
            },
        ),
    ]
