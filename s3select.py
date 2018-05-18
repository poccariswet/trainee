import boto3
from boto3 import Session
import os
import sys



s3 = boto3.client('s3')
argvs = sys.argv
if (len(argvs) != 2):
    print('Usage: # python %s date => ex. python ***.py 20180418' % argvs[0])
    quit()

s3client = Session().client('s3')

response = s3client.list_objects(
    Bucket='ld-rawdata-2',
    Prefix= 'TR_JISSEKI/' + argvs[1] + 'XXXXXX/'
)

if 'Contents' in response:  # 該当する key がないと response に 'Contents' が含まれない
    keys = [content['Key'] for content in response['Contents']]
    del keys[0:4],keys[-1] #上４つと最後の２３時のデータを取り除く


def GenerateRawCsvData(keys):
    raw_csv_data=[]
    dptcode = "\'030000\'"
    records = b""
    for key in keys:
        r = s3.select_object_content(
            Bucket="ld-rawdata-2",
            Key = key,
            ExpressionType='SQL',
            Expression="SELECT s._4,s._9,s._13 FROM s3Object as s where s._5 like" + dptcode,
            InputSerialization = {'CSV': {"FileHeaderInfo": "IGNORE"}},
            OutputSerialization = {'CSV': {}},
            )
        for event in r['Payload']:
            if 'Records' in event:
                records += event['Records']['Payload']
        raw_csv_data.append(records.decode('utf-8', 'replace'))
        records=b""
    
    return raw_csv_data

def GenerateFormatCsv3Dlist(raw_csv_data):
    return [[x.split(',') for x in data] for data in [x.split('\n') for x in raw_csv_data]]

def GenerateUniqeSkuList(format_csv_3dlist):
    uniqe_sku_tmp = []  
    uniqe_sku_li = [] 
    for lines in format_csv_3dlist: 
         for line in lines:                                                                                                  
                 if line[0] not in uniqe_sku_tmp: 
                         uniqe_sku_tmp.append(line[0]) 
         uniqe_sku_li.append(uniqe_sku_tmp)

    return uniqe_sku_li

def GenerateLastTimeList(keys):
    last_times = []
    for key in keys:
        last_times.append(key[-10:-8])
    return last_times

def GenerateUniqeDataDics(last_times, uniqe_sku_li, format_csv_3dlist):
    uniqe_data_dic = {}
    uniqe_data_dics ={}
    for last_time in last_times:
        uniqe_data_dics[last_time] = {}
    
    for last_time, sku_codes in zip(last_times, uniqe_sku_li):
        for sku_code in sku_codes:
            uniqe_data_dic[sku_code] = ['', 0]
        uniqe_data_dics[last_time].update(uniqe_data_dic)
    
    for last_time, lines in zip(last_times, format_csv_3dlist):
        for line in lines:
            if len(line) > 2:
                uniqe_data_dics[last_time][line[0]][0] = line[1]
                uniqe_data_dics[last_time][line[0]][1] += float(line[2])
    return uniqe_data_dics

def GenerateItems(uniqe_sku_list, uniqe_data_dics, last_time):
    Items = {}
    for skus in uniqe_sku_list:
        for sku in skus:
                Items[sku] = {}
    
    for last_time in uniqe_data_dics.keys():
        for sku in uniqe_data_dics[last_time].keys():
            if sku != '':
                Items[sku]["skucode"] = sku                             
                if uniqe_data_dics[last_time][sku][0] != '':
                    Items[sku]["p_name"] = uniqe_data_dics[last_time][sku][0]
                Items[sku][last_time] = uniqe_data_dics[last_time][sku][1]

    return Items

Items = GenerateItems(
    GenerateUniqeSkuList(
        GenerateFormatCsv3Dlist(
            GenerateRawCsvData(keys)
    )
    ), 
    GenerateUniqeDataDics(
        GenerateLastTimeList(keys),
        GenerateUniqeSkuList(
            GenerateFormatCsv3Dlist(
                GenerateRawCsvData(keys)
            )
        ),
        GenerateFormatCsv3Dlist(
            GenerateRawCsvData(keys)
        )
    ),
    GenerateLastTimeList(keys)
)
