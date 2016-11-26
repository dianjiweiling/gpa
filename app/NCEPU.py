# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from requests import Session
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class NoticeSpider:
    """docstring for NoticeSpider"""
    def __init__(self, UserName, Password):
        self.UserName = UserName
        self.Password = Password
        self.s = Session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                        'Referer': 'http://59.67.225.73/m/Account/Login',
                        'Host': '59.67.225.73',
                        'Origin': 'http://59.67.225.73',
                    }

    def login(self):
        login_url = r'http://59.67.225.73/m/Account/Login'
        print 'here'
        try:
            r = self.s.get(login_url)
            bsObj = BeautifulSoup(r.text, 'html.parser')
            value = bsObj.find('input').get('value')
            payload = {'__RequestVerificationToken': value,
                        'UserName':self.UserName,
                        'Password':self.Password,
                        'RememberMe':'false'
                    }

            r1 = self.s.post(login_url, data=payload, headers=self.headers)
            rr = re.findall(u'输入的学号或密码不正确', r1.text)
            if not rr:
                return True
            else:  
                return False
        except:
            return False


            
        

if __name__ == '__main__':
    print 'hello, i am here'
    spider = NoticeSpider(201401400214,123)
    print spider.login()

    
