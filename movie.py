# _*_ coding:utf-8 _*_

import tushare as ts
import pandas as pd
from pyecharts import Bar

'''
get monthly movie's data from tushare 
by 'ts.month_boxoffice()'
'''
def get_movie():
	movies = []
	for m in range(1,11):
		df = ts.month_boxoffice('2018-'+str(m))
		movies.append(df)
	
	res = pd.concat(movies)
	return res

'''
show top10 boxoffice movies by the sum of boxoffice
'''
def top10():
	bo = df.groupby(['MovieName'])['boxoffice'].sum().sort_values(ascending=False)
	top10 = bo.head(10)
	data = dict(top10)
	data = sorted(data.items(),key=lambda d:d[1],reverse=True)
	attr = [d[0] for d in data]
	val = [d[1] for d in data]
	# print(attr)
	bar = Bar("票房 top10", "made by rxl")
	bar.add("票房", attr, val, mark_line=["average"],xaxis_rotate=20,is_label_show=True)
	bar.render(path = "票房top10.html")

'''
show top10 hottest movies by the index of average show count
'''
def hot():
	bo = df.groupby(['MovieName'])['avgshowcount'].sum().sort_values(ascending=False)
	top10 = bo.head(10)
	data = dict(top10)
	data = sorted(data.items(),key=lambda d:d[1],reverse=True)
	attr = [d[0] for d in data]
	val = [d[1] for d in data]
	# print(attr)
	bar = Bar('hot', "made by rxl")
	bar.add("hot", attr, val, xaxis_rotate=20,is_label_show=True)
	bar.render(path = "hot.html")

'''
show the number of movies in month
'''
def total():
	bo = df.groupby(['MovieName'])['releaseTime']
	val = [0 for i in range(1,11)]
	attr = [i for i in range(1,11)]
	data = list(bo)
	
	for d in data:
		date = list(d[1])
		ymd = date[0].split('/')
		m = int(ymd[1])
		val[m-1] += 1
	bar = Bar('每月电影上映数量', "made by rxl")
	bar.add("每月电影上映数量", attr, val, is_label_show=True)
	bar.render(path = "每月电影上映数量.html")

if __name__ == "__main__":
	# data = get_movie()
	# data.to_csv('movie.csv')
	df = pd.read_csv('movie.csv')
	# top10()
	# hot()
	# total()