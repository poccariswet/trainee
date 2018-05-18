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

del keys[0:4],keys[-1]
rdata=[]
b=[]
skucode = "\'0305056900000\'"
dtpcode = "\'030000\'"
records = b""

for key in keys:
    r = s3.select_object_content(
        Bucket="ld-rawdata-2",
        Key = key,
        ExpressionType='SQL',
#Expression="SELECT s._9,s._13 FROM s3Object as s where s._4 like" + skucode,
        Expression="SELECT s._4,s._9,s._13 FROM s3Object as s where s._5 like" + dtpcode,
        InputSerialization = {'CSV': {"FileHeaderInfo": "IGNORE"}},
        OutputSerialization = {'CSV': {}},
        )
    for event in r['Payload']:
        if 'Records' in event:
            records += event['Records']['Payload']
    rdata.append(records.decode('utf-8', 'replace'))
    records=b""


format_csv_3Dlist = [[x.split(',') for x in data] for data in [x.split('\n') for x in rdata]]

uniqe_sku_li = [set([line[0] for line in lines]) for lines in format_csv_3Dlist]

last_times = [last_time[-10:-8] for last_time in keys]

uniqe_data_dics = {last_time: {sku_code: ['',0] for sku_code in sku_codes} for last_time, sku_codes in zip(last_times, uniqe_sku_li)}

for last_time, lines in zip(last_times, format_csv_3Dlist):
    for line in lines:
        if len(line) > 2:
            uniqe_data_dics[last_time][line[0]][0] = line[1]
            uniqe_data_dics[last_time][line[0]][1] += float(line[2])

Items = {sku: {} for sku in [flatten for inner in uniqe_sku_li for flatten in inner]}

for last_time in uniqe_data_dics.keys():
    for sku in uniqe_data_dics[last_time].keys():
        if sku != '' and uniqe_data_dics[last_time][sku][0] != '':
            Items[sku]["skucode"] = sku                             
            Items[sku]["p_name"] = uniqe_data_dics[last_time][sku][0]
            Items[sku][last_time] = uniqe_data_dics[last_time][sku][1]
