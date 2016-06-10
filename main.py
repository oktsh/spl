import openpyxl
import csv
import xlwt
import datetime

# Открытие книги со списком наших серверов CAS
sl = openpyxl.load_workbook(filename='./CAS_server_list.xlsx')
sheet = sl['Sheet1']
servlist = [v[0].value.upper() for v in sheet.iter_rows('A1:A61')]  # создание list-списка серверов

# Открытие csv со списком серверов для патчинга
psl = open('ServerWindows.csv')
pslist = csv.reader(psl, dialect='excel')

psu = {}
i = 0

# Создание нового excel-файла
rw = xlwt.Workbook()
rws = rw.add_sheet('servers')

# Создание словаря с парами сервер:дата патчинга
for row in pslist:
    psu = dict(server=row[0].upper(), date=row[3].upper())
    if psu['server'] in servlist:
        i += 1
        rws.write(i, 0, psu['server'])
        rws.write(i, 1, psu['date'])

# Сохранение файла с датой
date = str(datetime.date.today())
rw.save('Server patching list ' + date + '.xls')



