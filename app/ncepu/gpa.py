# -*- coding:utf-8 -*-

from NCEPU import NoticeSpider
from lxml import etree
# from ..models import Student, Info

class GPASpider(NoticeSpider):

    def __init__(self,UserName,Password):
        NoticeSpider.__init__(self,UserName,Password)
        self.coure_url = 'http://59.67.225.73/m/Personal/Schedule'
        # 课程信息存储列表
        self.data = list()

        self.credits = 0  # 学分和
        self.sum = 0  # 绩点和
        self.GPA = 0  # 学分绩

    def process_info(self):

        result = self.s.get(self.coure_url).text

        '''处理课程页面,提取所需数据'''      
        selector = etree.HTML(result)
        courses = selector.xpath("//table[@id='table_bx']/tr")

        for course in courses:
            items = course.xpath("td/text()")
            if not items: continue
            # for item in items:
            #     print item,
            # print len(items)
            # print '------------------------'
            # continue  
            for term,course_id,course_name,credit,required,score in [tuple(items)]:
                credit = credit.split('/')[0]
                score = score.split('/')[0]

                dic = {
                        'term':term,
                        'course_id':course_id,
                        'course_name':course_name,
                        'credit':credit,
                        'score':score
                    }
                self.data.append(dic)

        courses2 = selector.xpath("//table[@id='table_xx']/tr")
        for course2 in courses2:
            items = course2.xpath("td/text()")
            if  not items: continue
          
            for term,course_id,course_name,credit,required,score, not_important, not_important2 in [tuple(items)]:
                credit = credit.split('/')[0]
                score = score.split('/')[0]
                dic = {
                        'term':term,
                        'course_id':course_id,
                        'course_name':course_name,
                        'credit':credit,
                        'score':score
                    }
                self.data.append(dic)


        courses3 = selector.xpath("//table[@id='table_sj']/tr")
        for course3 in courses3:
            items = course3.xpath("td/text()")
            if  not items: continue
  
            course_id = items[1]
            course_name = items[2]
            credit = items[3].split('/')[0]
            score = items[-1].split('/')[0]
            dic = {
                    'term':term,
                    'course_id':course_id,
                    'course_name':course_name,
                    'credit':credit,
                    'score':score
                }
            self.data.append(dic)
      

    def calculate_GPA(self):

        '''计算学分和，绩点和，学分绩'''
        map_of_score = {u'通过': 60, u'中': 70, u'良': 80, u'优': 90}  # 把课程的评测结果量化
        other_of_score = ['&nbsp;', u'不及格', u'不通过', ' ']  # 不计入学分绩的条件
        for Course in self.data:
            if Course['score'] in map_of_score:
                self.sum += float(Course['credit']) * map_of_score[Course['score']]
                self.credits += float(Course['credit'])
                continue
            if Course['score'] in other_of_score: continue

            self.sum += float(Course['credit']) * float(Course['score'])
            self.credits += float(Course['credit'])
        self.GPA = float(self.sum/self.credits)

    def spider(self):
        return self.login()



if __name__ == '__main__':

    mySpider = GPASpider('201401400214',11)
    mySpider.spider()
    print 'The total point is: ', mySpider.sum
    print 'The total credits is: ', mySpider.credits
    print 'GPA = ', mySpider.GPA
            #     self.process_info()
        #     self.calculate_GPA()
        #     return self.GPA
        # else:
        #     return -100
