#coding:utf-8
import urllib  #抓網頁要用的函式庫
import gzip    #解壓縮要用的函式庫
import json    #處理JSON格式資料要用的函式庫
urllib.urlretrieve('http://data.taipei/youbike','data.gz')
with gzip.open('data.gz', 'rb') as f:
    #data_string = f.read()
    data_dict = json.load(f)
#print dict.keys(data_dict)
print '台北市YouBike有',len(data_dict['retVal']),'個租賃站'
#print dict.keys(data_dict['retVal'])
print '每個租賃站有',len(data_dict['retVal']['0001']),'個即時資訊'
#print dict.keys(data_dict['retVal']['0001'])
print '\n'

def print_data(sno):
    print data_dict['retVal'][sno]['sno'].encode('utf-8')
    print data_dict['retVal'][sno]['sna'].encode('utf-8')
    #print data_dict['retVal'][sno]['tot'].encode('utf-8')
    print data_dict['retVal'][sno]['sbi'].encode('utf-8')
    print data_dict['retVal'][sno]['sarea'].encode('utf-8')
    #print data_dict['retVal'][sno]['mday'].encode('utf-8')
    #print data_dict['retVal'][sno]['lat'].encode('utf-8')
    #print data_dict['retVal'][sno]['lng'].encode('utf-8')
    print data_dict['retVal'][sno]['ar'].encode('utf-8')
    #print data_dict['retVal'][sno]['sareaen'].encode('utf-8')
    #print data_dict['retVal'][sno]['snaen'].encode('utf-8')
    #print data_dict['retVal'][sno]['aren'].encode('utf-8')
    #print data_dict['retVal'][sno]['bemp'].encode('utf-8')
    #print data_dict['retVal'][sno]['act'].encode('utf-8')
    print '\n'

for sno in dict.keys(data_dict['retVal']):
    print_data(sno)
