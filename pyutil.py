#! coding: utf-8
import sys
import json
import os
import datetime


def get_ids():
    '''
    从输入的文件中获得所有的id，文档中的每行是一个json
    usage: python xxx.py file1 file2 file3 ...
    '''
    for filename in sys.argv[1:]:
        f = open(filename, 'r')
        for line in f:
            if line.strip():
                obj = json.loads(line)
                print obj.get('_id')
        f.close()

def generate_dates():
    '''
    根据输入的起始日期，以及每行的限制个数，生成需要的日期行，之前用于hadoop-import生成日期列表，生成到今天为止的日期
    usage: python xxx.py 2016-07-12 num_per_line [sep]
    num_per_line是每行最大放置的日期数量
    sep是日期之间的分隔符, 如果不指定则为逗号
    '''
    from_day_str = sys.argv[1]
    num_per_line = int(sys.argv[2])
    sep = ','
    if len(sys.argv) > 3:
        sep = sys.argv[3]

    from_day = datetime.datetime.strptime(from_day_str, "%Y-%m-%d")
    today = datetime.datetime.now()
    gap_days = (today - from_day).days

    cnt = 0
    days = []
    
    for i in range(gap_days):
        cnt += 1
        days.append( (from_day + datetime.timedelta(days = i)).strftime("%Y%m%d") )
        if cnt % num_per_line == 0:
            print '%s' % sep.join(days)
            days = []

    if len(days) != 0:
        print '%s' % sep.join(days)

if __name__ == "__main__":
    #get_ids()
    generate_dates()
    pass
