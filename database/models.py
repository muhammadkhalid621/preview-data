from operator import mod
from pyexpat import model
from django.db import models
from datetime import date


# Create your models here.
today = date.today()
date = today.strftime("%Y-%m-%d")


class Header(models.Model):
    date = models.DateField(default=date)
    Turn_Over = models.CharField(max_length=100, blank=True, null=True)
    Trade_value = models.CharField(max_length=100, blank=True, null=True)
    market_capitalization = models.CharField(
        max_length=100, blank=True, null=True)
    Equal = models.CharField(max_length=100, blank=True, null=True)
    Total = models.CharField(max_length=100, blank=True, null=True)
    Kse_100 = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)\
    
    class Meta:
        db_table = 'Header'

class Header2(models.Model):
    date = models.DateField(default=date)
    Indexes = models.CharField(max_length=100, blank=True, null=True)
    Previos_Index = models.CharField(max_length=100, blank=True, null=True)
    Current_Index = models.CharField(max_length=100, blank=True, null=True)
    High = models.CharField(max_length=100, blank=True, null=True)
    Low = models.CharField(max_length=100, blank=True, null=True)
    NetChange_points = models.CharField(max_length=100, blank=True, null=True)
    NetChange_percent = models.CharField(max_length=100, blank=True, null=True)
    TurnOver = models.CharField(max_length=100, blank=True, null=True)
    # Value = models.CharField(max_length=100, blank=True, null=True)
    # Mkt_Capitalization = models.CharField(
    #     max_length=100, blank=True, null=True)
    # INDX_CGI = models.CharField(max_length=100, blank=True, null=True)
    # CHG_percent = models.CharField(max_length=100, blank=True, null=True)
    # TOCHG = models.CharField(max_length=100, blank=True, null=True)
    # CHG2_percent = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Header2'

class Kibor(models.Model):
    date = models.DateField(default=date)
    Week_1 = models.CharField(max_length=100, blank=True, null=True)
    Week_2 = models.CharField(max_length=100, blank=True, null=True)
    Month_1 = models.CharField(max_length=100, blank=True, null=True)
    Month_3 = models.CharField(max_length=100, blank=True, null=True)
    Month_6 = models.CharField(max_length=100, blank=True, null=True)
    Month_9 = models.CharField(max_length=100, blank=True, null=True)
    Year_1 = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Kibor'


class Libor(models.Model):
    date = models.DateField(default=date)
    overnight = models.CharField(max_length=100, blank=True, null=True)
    Month_1 = models.CharField(max_length=100, blank=True, null=True)
    Month_3 = models.CharField(max_length=100, blank=True, null=True)
    Month_6 = models.CharField(max_length=100, blank=True, null=True)
    Month_12 = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Libor'


class Currency(models.Model):
    date = models.DateField(default=date)
    CURRENCY = models.CharField(max_length=100, blank=True, null=True)
    READY = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Currency'


class Closing(models.Model):
    date = models.DateField(default=date)
    Ticker = models.CharField(max_length=100, blank=True, null=True)
    CompanyName = models.CharField(max_length=100, blank=True, null=True)
    Open = models.CharField(max_length=100, blank=True, null=True)
    High = models.CharField(max_length=100, blank=True, null=True)
    Low = models.CharField(max_length=100, blank=True, null=True)
    Close = models.CharField(max_length=100, blank=True, null=True)
    Volume = models.CharField(max_length=100, blank=True, null=True)
    LDCP = models.CharField(max_length=100, blank=True, null=True)
    Change = models.CharField(max_length=100, blank=True, null=True)
    change_percent = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Closing'


class KSE100Index(models.Model):
    date = models.DateField(default=date)
    Symbol = models.CharField(max_length=100, blank=True, null=True)
    SCRIP = models.CharField(max_length=100, blank=True, null=True)
    LDCP = models.CharField(max_length=100, blank=True, null=True)
    CURRENT = models.CharField(max_length=100, blank=True, null=True)
    CHANGE = models.CharField(max_length=100, blank=True, null=True)
    CHANGE_percent = models.CharField(max_length=100, blank=True, null=True)
    IDX_WTG_percent = models.CharField(max_length=100, blank=True, null=True)
    IDX_POINT = models.CharField(max_length=100, blank=True, null=True)
    VOLUME = models.CharField(max_length=100, blank=True, null=True)
    FREEFLOAT = models.CharField(max_length=100, blank=True, null=True)
    MARKET_CAP = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'KSE100Index'


class AllShare(models.Model):
    date = models.DateField(default=date)
    Sector = models.CharField(max_length=100, blank=True, null=True)
    Mkt_Cap = models.CharField(max_length=100, blank=True, null=True)
    Turnover = models.CharField(max_length=100, blank=True, null=True)
    Traded_Value = models.CharField(max_length=100, blank=True, null=True)
    Pre_Index = models.CharField(max_length=100, blank=True, null=True)
    Cur_Index = models.CharField(max_length=100, blank=True, null=True)
    N_Chg = models.CharField(max_length=100, blank=True, null=True)
    M_CAP_percent = models.CharField(max_length=100, blank=True, null=True)
    T_Cpt_percent = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'AllShare'


class BoardMeetings(models.Model):
    Symbol = models.CharField(max_length=100, blank=True, null=True)
    CompanyName = models.CharField(max_length=100, blank=True, null=True)
    AC_Period = models.CharField(max_length=100, blank=True, null=True)
    Date = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'BoardMeetings'

class PKRV(models.Model):
    date = models.DateField(default=date)
    W1 = models.CharField(max_length=100, blank=True, null=True)
    W2 = models.CharField(max_length=100, blank=True, null=True)
    M1 = models.CharField(max_length=100, blank=True, null=True)
    M2 = models.CharField(max_length=100, blank=True, null=True)
    M3 = models.CharField(max_length=100, blank=True, null=True)
    M4 = models.CharField(max_length=100, blank=True, null=True)
    M6 = models.CharField(max_length=100, blank=True, null=True)
    M9 = models.CharField(max_length=100, blank=True, null=True)
    Y1 = models.CharField(max_length=100, blank=True, null=True)
    Y2 = models.CharField(max_length=100, blank=True, null=True)
    Y3 = models.CharField(max_length=100, blank=True, null=True)
    Y4 = models.CharField(max_length=100, blank=True, null=True)
    Y5 = models.CharField(max_length=100, blank=True, null=True)
    Y6 = models.CharField(max_length=100, blank=True, null=True)
    Y7 = models.CharField(max_length=100, blank=True, null=True)
    Y8 = models.CharField(max_length=100, blank=True, null=True)
    Y9 = models.CharField(max_length=100, blank=True, null=True)
    Y10 = models.CharField(max_length=100, blank=True, null=True)
    Y15 = models.CharField(max_length=100, blank=True, null=True)
    Y20 = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'PKRV'

class LocalCommodities(models.Model):
    date = models.DateField(default=date)
    urea_sona = models.CharField(max_length=100, blank=True, null=True)
    DAP = models.CharField(max_length=100, blank=True, null=True)
    Petrol = models.CharField(max_length=100, blank=True, null=True)
    Diesel = models.CharField(max_length=100, blank=True, null=True)
    LPG = models.CharField(max_length=100, blank=True, null=True)
    Sugar = models.CharField(max_length=100, blank=True, null=True)
    Cement = models.CharField(max_length=100, blank=True, null=True)
    Gold = models.CharField(max_length=100, blank=True, null=True)
    Silver = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'LocalCommodities'

class InternationalCommodities(models.Model):
    date = models.DateField(default=date)
    Crude_oil = models.CharField(max_length=100, blank=True, null=True)
    Brent = models.CharField(max_length=100, blank=True, null=True)
    Gold = models.CharField(max_length=100, blank=True, null=True)
    Silver = models.CharField(max_length=100, blank=True, null=True)
    Platinum = models.CharField(max_length=100, blank=True, null=True)
    Copper = models.CharField(max_length=100, blank=True, null=True)
    Cotton = models.CharField(max_length=100, blank=True, null=True)
    Sugar = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'InternationalCommodities'
