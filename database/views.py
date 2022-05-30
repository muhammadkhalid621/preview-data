from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scrapper import kibor, libor, currency, closing, kse100, allshare, board_meetings, pkrv, local_commodities, international_commodities, header, header2
from .models import Currency, Closing, KSE100Index, AllShare, Libor, Kibor, BoardMeetings, PKRV, LocalCommodities, InternationalCommodities, Header, Header2
from rest_framework import status
from django.http import HttpResponse
from django.template import loader
import datetime
from urllib.error import HTTPError
# Create your views here.


def view(request):
    try:
        currency_data = currency()
        print(currency_data)
        for data in currency_data:
            records_currency = Currency(
                CURRENCY=data[0], READY=data[1])
            records_currency.save()

        closing_data = closing()
        print(closing_data)
        for data in closing_data:
            # date = datetime.datetime.strptime(data[0], '%d%m%Y').strftime('%m-%d-%y')
            try:
                change = round(float(data[6])-float(data[8]), 4)
                change_percent = round((float(data[6])/float(data[8])-1), 4)
            except ZeroDivisionError as error:
                continue
            records_closing = Closing(Ticker=data[1], CompanyName=data[2], Open=data[3], High=data[4],
                                      Low=data[5], Close=data[6], Volume=data[7], LDCP=data[8], Change=change, change_percent=change_percent)
            records_closing.save()

        kse100_data = kse100()
        for data in kse100_data:
            records_kse100 = KSE100Index(Symbol=data[0], SCRIP=data[1], LDCP=data[2], CURRENT=data[3],
                                         CHANGE=data[4], CHANGE_percent=data[5], IDX_WTG_percent=data[6], IDX_POINT=data[7],
                                         VOLUME=data[8], FREEFLOAT=data[9], MARKET_CAP=data[10])
            records_kse100.save()

        allshare_data = allshare()
        for data in allshare_data:
            records_allshare = AllShare(Sector=data[0], Mkt_Cap=data[1], Turnover=data[2], Traded_Value=data[3],
                                        Pre_Index=data[4], Cur_Index=data[5], N_Chg=data[6], M_CAP_percent=data[7], T_Cpt_percent=data[8])
            records_allshare.save()

        libor_data = libor()
        for data in libor_data:
            date = datetime.datetime.strptime(
                data[0], '%m-%d-%Y').strftime('%Y-%m-%d')
            records_libor = Libor(
                date=date, overnight=data[1].replace(u'\xa0', u' '), Month_1=data[2].replace(u'\xa0', u' '),
                Month_3=data[3].replace(u'\xa0', u' '), Month_6=data[4].replace(u'\xa0', u' '), Month_12=data[5].replace(u'\xa0', u' '))
            records_libor.save()

        Kibor_data = kibor()
        print(Kibor_data)
        record_kibor = Kibor(Week_1=Kibor_data[0], Week_2=Kibor_data[1], Month_1=Kibor_data[2],
                             Month_3=Kibor_data[3], Month_6=Kibor_data[4], Month_9=Kibor_data[5], Year_1=Kibor_data[6])
        record_kibor.save()

        board_meeting_data = board_meetings()
        for data in board_meeting_data:
            # date = datetime.datetime.strptime(data[0], '%d%m%Y').strftime('%m-%d-%y')
            records_board_meeting = BoardMeetings(
                Symbol=data[0], CompanyName=data[1], AC_Period=data[2], Date=data[3])
            records_board_meeting.save()

        pkrv_data = pkrv()
        print(pkrv_data)
        record_pkrv = PKRV(W1=pkrv_data[0], W2=pkrv_data[1], M1=pkrv_data[2],
                           M2=pkrv_data[3], M3=pkrv_data[4], M4=pkrv_data[5], M6=pkrv_data[6],
                           M9=pkrv_data[7], Y1=pkrv_data[8], Y2=pkrv_data[9], Y3=pkrv_data[10],
                           Y4=pkrv_data[11], Y5=pkrv_data[12], Y6=pkrv_data[13], Y7=pkrv_data[14],
                           Y8=pkrv_data[15], Y9=pkrv_data[16], Y10=pkrv_data[17], Y15=pkrv_data[18],
                           Y20=pkrv_data[19])
        record_pkrv.save()

        local_comm_data = local_commodities()
        print(local_comm_data)
        record_local_comm = LocalCommodities(urea_sona=local_comm_data[0], DAP=local_comm_data[1], Petrol=local_comm_data[2],
                                             Diesel=local_comm_data[3], LPG=local_comm_data[
                                                 4], Sugar=local_comm_data[5], Cement=local_comm_data[6],
                                             Gold=local_comm_data[7], Silver=local_comm_data[8])
        record_local_comm.save()

        international_comm_data = local_commodities()
        print(international_comm_data)
        record_international_comm = InternationalCommodities(Crude_oil=international_comm_data[0], 
                                                            Brent=international_comm_data[1], Gold=international_comm_data[2],
                                                            Silver=international_comm_data[3], Platinum=international_comm_data[4], 
                                                            Copper=international_comm_data[5], Cotton=international_comm_data[6],
                                                            Sugar=international_comm_data[7])
        record_international_comm.save()

        header_data = header()
        print(header_data)
        header_comm = Header(Turn_Over=header_data[0], Trade_value=header_data[1], market_capitalization=header_data[2],
                             Equal=header_data[3], Total=header_data[4], Kse_100=header_data[5])
        header_comm.save()

        header2_data = header2()
        print(header2_data)
        for data in header2_data:
            header2_comm = Header2(Indexes=data[0] ,Previos_Index=data[1], Current_Index=data[2], High=data[3],
                                    Low=data[4], NetChange_points=data[5], NetChange_percent=data[6], TurnOver=data[7])
            header2_comm.save()

        return HttpResponse('Successful')
    except HTTPError:
        return HttpResponse('Unsuccessful')


def preview_data(request):
    # kse100_data = []
    # for data in KSE100Index.objects.get():
    #     kse100_data.append(data)

    libor_data = list(Libor.objects.all().values())
    kibor_data = list(Kibor.objects.all().values())
    allshare_data = list(AllShare.objects.all().values())
    kse100_data = list(KSE100Index.objects.all().values())
    pkrv_data = list(PKRV.objects.all().values())
    closing_data = list(Closing.objects.all().values())
    boardmeetings_data = list(BoardMeetings.objects.all().values())
    local_comm_data = list(LocalCommodities.objects.all().values())
    international_comm_data = list(InternationalCommodities.objects.all().values())
    currency_data = list(Currency.objects.all().values())
    header_data = list(Header.objects.all().values())
    header2_data = list(Header2.objects.all().values())
    # print(KSE100Index.objects. )
    print(pkrv_data)
    template = loader.get_template('data.html')
    context = {
        'libor_list': libor_data,
        'kibor_list': kibor_data,
        'allshare_list': allshare_data,
        'kse_list': kse100_data,
        'pkrv_list': pkrv_data,
        'closing_list': closing_data,
        'boardmeeting_list': boardmeetings_data,
        'local_comm_list': local_comm_data,
        'international_comm_list': international_comm_data,
        'currency_list': currency_data,
        'header_list': header_data,
        'header2_list': header2_data,
    }
    return HttpResponse(template.render(context, request))
