import requests
from urllib.request import urlopen
from datetime import datetime
from tabula import read_pdf
from tabulate import tabulate
import wget
import os
import zipfile
import pandas as pd
from django.conf import settings
from datetime import datetime
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

year = datetime.today().year
day = datetime.today().day
day_name = datetime.today().strftime('%A')
month = datetime.today().strftime('%B')
month_no = datetime.now().strftime('%m')

folder_name = str(year)+ '-' + str(month_no) + '-' + str(day)

def url(url):
    options = Options()
    options.headless = True 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(30)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    driver.get(url)
    return driver.page_source

def kibor():

    url = 'https://www.sbp.org.pk/ecodata/kibor/'+str(year)+'/'+str(month)+'/'+'Kibor-'+str(day)+'-'+str(month)+'-'+str(year)[2:4]+'.pdf'
    
    #reads table from pdf file
    df = read_pdf(url,pages="all") #address of pdf file
    l = ['Week_1', 'Week_2', 'Month_1', 'Month_3', 'Month_6', 'Month_9', 'Year_1']
    b = pd.DataFrame(df[0])['OFFER'].values.tolist()
    return b

def libor():
    df = pd.read_html('https://www.global-rates.com/en/interest-rates/libor/american-dollar/american-dollar.aspx')
    a = df[9].values.tolist()
    l = []
    for i in range(1,len(a)):
        l1 = []
        for j in range(len(a[0])):
            l1.append(a[j][i])
        l.append(l1)
    return l
    

def currency():
    # For each page the table can be read with the following code
    table_pdf = read_pdf('https://www.sbp.org.pk/ecodata/rates/m2m/' + str(year) + '/' + str(month) + '/' + str(day) + '-' + str(month) + '-' + str(22) + '.pdf', 
                        guess=False, pages = 'all', stream=True, encoding='cp1252')
    b = table_pdf[0][str(day) + '-' + str(month) + '-' + str(22)].values.tolist()
    a = table_pdf[0]['Exchange Rates for Mark to Market Revaluation by Authorized Dealers in Foreign Exchange'].values.tolist()
    e = table_pdf[0]['Unnamed: 1'].values.tolist()

    l = []
    # col = ['CURRENCY', 'READY','1-WEEK','2-WEEK','1-MONTH','2-MONTH','3-MONTH','4-MONTH','5-MONTH','6-MONTH','9-MONTH','1-YEAR']
    col = ['CURRENCY', 'READY']
    for i in range(1,len(b)):
        a[i] = str(a[i]).replace('nan', '')
        c = str(a[i]).split(' ')
        b[i] = str(b[i]).replace('nan', '')
        d = str(b[i]).split(' ')
        g = str(e[i]).replace('nan', '')
        if a[i] == '' or b[i] == '':
            break
        f = [d[0], d[1]]
        for j in range(len(c)):
            f.append(c[j])
        f.append(g)
        l.append(f)
    
    final_list = []
    final_list = []
    for i in range(len(l)):
    #     main_dict = {}
    #     for j in range(2):
    #         main_dict[col[j]] = l[i][j]
    #         print(main_dict)
        final_list.append([l[i][0], l[i][1]])
    return final_list

def closing():
    print(folder_name)
    try: 
        os.mkdir(os.path.join(str(settings.MEDIA_ROOT) + '/closing/', folder_name))
    except OSError as error: 
        pass
    
    url = 'https://dps.psx.com.pk/download/mkt_summary/' + str(year) + '-'+ str(month_no) + '-' + str(day) + '.Z'
    zipresp = urlopen(url)
    path = os.path.join(str(settings.MEDIA_ROOT)+ '/closing/'+ folder_name, folder_name + '.Z')
    tempzip = open(path, "wb")
    #     'https://dps.psx.com.pk/download/mkt_summary/2022-05-26.Z'), "wb")
    # Write the contents of the downloaded file into the new file
    tempzip.write(zipresp.read())
        # Close the newly-created file
    tempzip.close()
    # path = wget.download(os.path.join(str(settings.MEDIA_ROOT)+ '/closing/'+ folder_name, 
    #     'https://dps.psx.com.pk/download/mkt_summary/2022-05-26.Z'))
    zip = zipfile.ZipFile(path)
    zip.extractall(str(settings.MEDIA_ROOT) + '\\closing\\'+ folder_name + '\\')
    df = pd.read_csv(os.path.join(str(settings.MEDIA_ROOT)+ '/closing/'+ folder_name, 'closing11.lis'), sep="|", header=None)
    new_df = df.iloc[:,[0,1,3,4,5,6,7,8,9]]
    new_df.columns = ['Date', 'Ticker','CompanyName', 'Open', 'High', 'Low', 'Close', 'Volume', 'LDCP']
    new_df = new_df.sort_values(by=['Volume'], ascending=False)
    return new_df.values.tolist()

def kse100():
    import pandas as pd
    df = pd.read_html('https://dps.psx.com.pk/indices/KSE100')
    return df[0].values.tolist()

def allshare():
    try: 
        os.mkdir(os.path.join(str(settings.MEDIA_ROOT) + '/allshare/', folder_name))
    except OSError as error: 
        pass

    url = 'https://dps.psx.com.pk/download/text/allshr_new.lis.Z'
    zipresp = urlopen(url)
    path = os.path.join(str(settings.MEDIA_ROOT)+ '/allshare/'+ folder_name, folder_name + '.Z')
    tempzip = open(path, "wb")
    #     'https://dps.psx.com.pk/download/mkt_summary/2022-05-26.Z'), "wb")
    # Write the contents of the downloaded file into the new file
    tempzip.write(zipresp.read())
        # Close the newly-created file
    tempzip.close()
    # path = wget.download(os.path.join(str(settings.MEDIA_ROOT)+ '/closing/'+ folder_name, 
    #     'https://dps.psx.com.pk/download/mkt_summary/2022-05-26.Z'))
    zip = zipfile.ZipFile(path)
    zip.extractall(str(settings.MEDIA_ROOT) + '/allshare/'+ folder_name + '/')
    df = pd.read_csv(os.path.join(str(settings.MEDIA_ROOT)+ '/allshare/'+ folder_name, 'allshr_new.lis'), sep="|", header=None, skipfooter=1)
    new_df = df.iloc[:,[1,2,3,4,5,6,7,8,9]]
    new_df.columns = ['Sector', 'Mkt Cap', 'Turnover', 'Traded Value', 'Pre.Index', 'Cur Index', 'N.Chg', 'M/CAP-%', 'T.Cpt-%']

    return new_df.values.tolist()

def board_meetings():
    options = Options()
    options.headless = True 
    # put the driver in the folder of this code
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  

    driver.get("https://www.ksestocks.com/BoardMeetings/SortByDate")
    time.sleep(3)
    real_soup = BeautifulSoup(driver.page_source, 'html.parser')
    open1 = real_soup.findAll("td",{'class':'bmcell'})
    l = []
    check_list = ['3rd Quarter', 'Half Year', 'Annual', '1st Quarter']
    for i in range(len(open1)):
    #     l.append(open1[i].text)
    #     print(i.text)
        for j in check_list:
            if j == open1[i].text:
                l.append(open1[i-2].text)
                l.append(open1[i-1].text)
                l.append(open1[i].text)
                l.append(open1[i+1].text)

    # for j in check_list:
    #         if j != i.text
    final_list = []
    for i in range(0,len(l),4):
        final_list.append(l[i:i+4])
    return final_list

def pkrv():
    df = pd.read_csv('https://mufap.com.pk/pdf/PKRVs/'+str(year)+'/'+str(month)+'/'+'PKRV'+str(day)+str(month_no)+str(year)+'.csv', encoding='latin-1')
    return df['Mid Rate'].values.tolist()

def local_commodities():
    url = "https://www.pbs.gov.pk/sites/default/files/price_statistics/weekly_spi/SPI_Annex%26USCP_26052022.pdf"
    df = read_pdf(url,pages='all')
    b = df[6].values.tolist()
    sona_urea  = b[0][15]
    dap = b[6][15]
    print('sona urea: ' + str(sona_urea), 'dap: ' + str(dap))
    a = df[5].values.tolist()
    petrol = a[45][13]
    diesel = a[46][13]
    lpg = a[47][13]
    sugar = a[22][13]
    print('petrol: ' + str(petrol), 'diesel: ' + str(diesel), 'lpg: ' + str(lpg), 'sugar' + str(sugar))
    cement = df[7].values.tolist()[0][19]
    print('cement: ' + str(cement))

    url = 'https://www.brecorder.com/markets/karachi-bullion-rates'

    page = requests.get(url)
    # df = pd.read_html(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find('table',{'id':'financial-table'})
    l = []
    for row in results.tbody.find_all('tr'):    
        # Find all data for each column
        columns = row.find_all('td')
    #     print(columns[0].text.strip())
        l.append(columns[0].text.strip())
        break
    l0 = []
    c = ''.join(l).split('\n')
    for i in c:
        l0.append(" ".join(i.split()))
    print('gold: '+ l0[2], 'silver: ' + l0[6])
    final_list = [sona_urea, dap, petrol, diesel, lpg, sugar, cement, l0[2], l0[6]]
    return final_list

def international_commodities(): 
    url = 'https://www.bloomberg.com/energy'
    url_text = url(url)
    df = pd.read_html(url_text)
    a = df[0].values.tolist()
    crude_oil = a[0][2]
    brent = a[1][2]
    print('crude oil: ' + str(crude_oil), 'brent: ' + str(brent))

    url = 'https://www.bloomberg.com/markets/commodities/futures/metals'
    url_text = url(url)
    df = pd.read_html(url_text)
    b = df[0].values.tolist()
    gold = b[2][2]
    c = df[1].values.tolist()
    silver = c[2][2]
    d = df[2].values.tolist()
    platinium = d[0][2]
    e = df[3].values.tolist()
    copper = e[0][2]
    print('gold: ' + str(gold), 'silver: ' + str(silver), 'platinium: ' + str(platinium), 'copper: ' + str(copper))

    url = 'https://www.bloomberg.com/markets/commodities/futures/agriculture'
    url_text = url(url)
    df = pd.read_html(url_text)
    f = df[1].values.tolist()
    cotton = f[2][2]
    sugar = f[4][2]
    print('cotton: ' + str(cotton), 'sugar: ' + str(sugar))

    final_list = [crude_oil, brent, gold, silver, platinium, copper, cotton, sugar]
    return final_list

def header():
    print(folder_name)
    try: 
        os.mkdir(os.path.join(str(settings.MEDIA_ROOT) + '/header/', folder_name))
    except OSError as error: 
        pass
    
    url = 'https://dps.psx.com.pk/download/text/header.zip'
    zipresp = urlopen(url)
    path = os.path.join(str(settings.MEDIA_ROOT)+ '/header/'+ folder_name, folder_name + '.Z')
    tempzip = open(path, "wb")
    #     'https://dps.psx.com.pk/download/mkt_summary/2022-05-26.Z'), "wb")
    # Write the contents of the downloaded file into the new file
    tempzip.write(zipresp.read())
        # Close the newly-created file
    tempzip.close()
    # path = wget.download(os.path.join(str(settings.MEDIA_ROOT)+ '/closing/'+ folder_name, 
    #     'https://dps.psx.com.pk/download/mkt_summary/2022-05-26.Z'))
    zip = zipfile.ZipFile(path)
    zip.extractall(str(settings.MEDIA_ROOT) + '\\header\\'+ folder_name + '\\')
    datafile = open(os.path.join(str(settings.MEDIA_ROOT)+ '/header/'+ folder_name, 'header.txt'))
    final_list = []
    for line in datafile:
        if 'P.Turn.' in line:
            print('Mkt Turn Over:',line[45:])
            final_list.append(line[45:])
        if 'P.Trd.Val'in line:
            print('Trade Value:', line[43:])
            final_list.append(line[43:])
        if 'P.Mkt.Cap'in line:
            print('Market Capitalization:',line[39:])
            final_list.append(line[39:])
        if 'Equal'in line:
            print('Equal:',line[54:])
            final_list.append(line[54:])
        if 'Total'in line:
            print('Total:',line[53:])
            final_list.append(line[53:])
        if 'P.Kse100 Index'in line:
            print('Total:',line[48:])
            final_list.append(line[48:57])
    final_list.append(round((float(final_list[5])/10**6),3))
    return final_list

def header2():
    print(folder_name)
    try: 
        os.mkdir(os.path.join(str(settings.MEDIA_ROOT) + '/header2/', folder_name))
    except OSError as error: 
        pass
    
    url = 'https://dps.psx.com.pk/download/text/header2.zip'
    zipresp = urlopen(url)
    path = os.path.join(str(settings.MEDIA_ROOT)+ '/header2/'+ folder_name, folder_name + '.Z')
    tempzip = open(path, "wb")
    #     'https://dps.psx.com.pk/download/mkt_summary/2022-05-26.Z'), "wb")
    # Write the contents of the downloaded file into the new file
    tempzip.write(zipresp.read())
        # Close the newly-created file
    tempzip.close()
    # path = wget.download(os.path.join(str(settings.MEDIA_ROOT)+ '/closing/'+ folder_name, 
    #     'https://dps.psx.com.pk/download/mkt_summary/2022-05-26.Z'))
    zip = zipfile.ZipFile(path)
    zip.extractall(str(settings.MEDIA_ROOT) + '\\header2\\'+ folder_name + '\\')
    datafile = open(os.path.join(str(settings.MEDIA_ROOT)+ '\\header2\\'+ folder_name, 'header_with_tradable_indices.txt'))
    final_list = []
    for line in datafile:
        if 'KSE100' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
        if 'KSE30' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
            
        if 'KMI30' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
        
        if 'KSEALL' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
            
        if 'BATi' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
            
        if 'OGTi' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
            
        if 'PSX_KMI' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
            
        if 'UPP9' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
            
        if 'NITPGI' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
        
        if 'NBPPGI' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
            
        if 'MZNPI' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
            
        if 'JSMFI' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
        
        if 'ACI' in line:
            print(line)
            print(line[0:7])
            print(line[11:20])
            print(line[23:32])
            print(line[34:43])
            print(line[45:54])
            print(line[58:65])
            print(line[71:76])
            final_list.append([line[0:7], line[11:20], line[23:32], line[34:43], line[45:54], line[58:65], line[71:76]])
        # final_list.append(l)
            
    
    url = "https://dps.psx.com.pk/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.findAll('div',{'class':'stats_value'})
    l = []
    for i in range(2, len(results),8):
        print('turnover',results[i].text)
        l.append(results[i].text)
 
    for i in range(len(final_list)):
        final_list[i].append(l[i])
    
    return final_list