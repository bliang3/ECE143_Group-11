import csv
import math
import os

from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN, ROUND_FLOOR
from tokenize import String

import xlrd as xlrd
from numpy import double


def open_excel (file):
    try:
        data = xlrd.open_workbook(file)
        print('success')
        return data
    except Exception as e:
        print (str(e))

def decRound (num):

    intNum = Decimal(Decimal(num).quantize(Decimal('1.'), rounding=ROUND_FLOOR))
    diff = Decimal(num) - intNum

    if diff <= 0.25:
        return intNum
    elif diff >= 0.75:
        return intNum + 1
    return intNum + Decimal(0.5)

def excel_table (file, colnameindex = 2, by_name = u'ph_2010'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows  # 行数
    #colnames = table.row_values(colnameindex)  # 某一行数据
    colnames2 = ['SampleDate', 'Analyte', 'Result', 'Latitude', 'Longitude']
    list = []  # 装读取结果的序列

    targetNum = [5, 17, 19, 36, 37]

    for rowNum in range(3, nrows):
        d = dict()
        row = table.row_values(rowNum)  # 根据行号获取行
        if row:
            for i in range(len(targetNum)):  # 一列列地读取行的内容
                if i == 0:
                    k = []
                    flag = 1
                    tmp = xlrd.xldate_as_tuple(table.cell(rowNum, targetNum[i]).value, 0)
                    k.append("/".join(str(x) for x in tmp[0:3]))
                    # d[colnames2[i]] = "/".join(str(x) for x in tmp[0:3])
                    #continue
                elif i == 1:
                    k.append(row[targetNum[i]])
                elif i == 2:
                    if isinstance(row[targetNum[i]], float):
                        k.append(row[targetNum[i]])
                    else:
                        k.append(0)
                elif i == 3 or i == 4:

                    if isinstance(row[targetNum[i]], float):
                        k.append(float(decRound(row[targetNum[i]])))
                        #d[colnames2[i]] = float(decRound(row[targetNum[i]]))
                    else:
                        k.append(0)

            if flag == 1:
                for m in range(len(k)):
                    d[colnames2[m]] = k[m]
        list.append(d)  # 装载数据

    print('success')
    return list

def write_csv (list, by_name = u'ph_2010'):

    fileheader = ['SampleDate', 'Analyte', 'Result', 'Latitude', 'Longitude']
    if by_name == u'ph_2010':
        print('page is open now')
        csvFile = open("ph_sheet1.csv", "w", newline='')
        print('success in opening')
        dict_writer = csv.DictWriter(csvFile, fileheader)
        dict_writer.writeheader()
        for i in list:
            if i['Result'] == 0 or i['Latitude'] == 0 or i['Longitude'] == 0:
                continue
            dict_writer.writerow(i)
        return

    csvFile = open("ph_sheet1.csv", "a", newline='')
    dict_writer = csv.DictWriter(csvFile, fileheader)

    for i in list:

        if i['Result'] == 0 or i['Latitude'] == 0 or i['Longitude'] == 0:
            continue

        dict_writer.writerow(i)
    csvFile.close()


p1 = '../../Dropbox/ECE143/project/dataByYear/ph_2010.xls'
p2 = '../../Dropbox/ECE143/project/dataByYear/ph_2011.xls'
p3 = '../../Dropbox/ECE143/project/dataByYear/ph_2012.xls'
p4 = '../../Dropbox/ECE143/project/dataByYear/ph_2013.xls'
p5 = '../../Dropbox/ECE143/project/dataByYear/ph_2014.xls'
p6 = '../../Dropbox/ECE143/project/dataByYear/ph_2015.xls'
p7 = '../../Dropbox/ECE143/project/dataByYear/ph_2016.xls'
p8 = '../../Dropbox/ECE143/project/dataByYear/ph_2017.xls'
p9 = '../../Dropbox/ECE143/project/dataByYear/ph_2018.xls'
p_index = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
#p_test = [p1, p8]
by_name = [u'ph_2010', u'ph_2011', u'ph_2012', u'ph_2013', u'ph_2014', u'ph_2015', u'ph_2016', u'ph_2017', u'ph_2018']
#by_test = [by_name[0], by_name[7]]
for k in range(len(by_name)):
    write_csv(excel_table(p_index[k], 2, by_name[k]), by_name[k])
    #write_csv(excel_table(p_test[k], 2, by_test[k]), by_test[k])
