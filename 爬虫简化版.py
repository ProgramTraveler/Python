#-------------------------------------------------------------------------------
# Name:        模块2
# Purpose:
#
# Author:      王久铭
#
# Created:     30/04/2019
# Copyright:   (c) 王久铭 2019
# Licence:     <your licence>
#-----------------------------------------------------------------------------
import requests
#r=urllib2.urlopen("http://www.baidu.com/")
r=requests.get("http://www.baidu.com")
r.status_code
r.text
print(r.text)
r.encoding
r.encoding='utf-8'
r.text
print(r.text)
