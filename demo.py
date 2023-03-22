#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:TT
# number = input('请输入一个正整数：')
# if number.isdigit() and (number.startswith('-') and number[1:].isdigit()):
# 	if number>0:
# 		if number%3==0 and number % 7==0:
# 			print('可以')
# 		else:
# 			print('不可以')
# 	else:
# 		print('非正整数')
# else:
# 	print('请输入纯数字')

#根据输入的月份来输出，这个月有几天（默认2月28天不考虑闫年）
# mouth = input('请输入月份：')
# print(type(mouth),mouth)
# if mouth in ['1','3','5','7','8','10','12']:
# 	print('%s月有31天'%mouth)
# elif mouth in ['4','6','9','11']:
# 	print('%s月有30天'%mouth)
# elif mouth == '2':
# 	print('%s月有28天' % mouth)
# else:
# 	print('无效的月份')


#3，接收用户输入一年份，判断是否是闰年（判断闰年的方法：能被4整队且不能被100整除，或可以被400整队）
# years = int(input('请入年份：'))
# if years%4==0:
# 	if years%100 != 0:
# 		print('闰年')
# 	else:
# 		print('非闰年')
# elif years % 400 ==0:
# 	print('闰年')
# else:
# 	print('非闰年')

# 3分钟 0.2元 3分钟以后每多1分中增加0.1 计算收费
# sed = input('请输入通话时间：')
# sed = int(sed)
# print(sed)
# total = 0.0
# if sed in range(1,181):
# 	total =0.2
# elif sed >180:
# 	if sed %60 == 0:
# 		total = 0.2 +(sed-180)//60*0.1
# 	else:
# 		print ((sed-180)/60+1)
# 		total = 0.2 + ((sed-180)//60+1)*0.1
# print('应收话费：%.2f'%total)

# a= int(input('请输入：'))
# while a>0:
# 	print(a)
# 	a = int(input('请输入：'))

# x=['s',1,2,3,4]
# for a in range(len(x)):
# 	print(a,x[a])

# x=['a','b','c']
# for i in enumerate(x):
# 	print(i)

# x=[1,2,3,4]
# for i in x:
# 	print(i)
# else:
# 	print('finish')
#给定一个字符串target='hello huice',从中找出第一个不重复的字符，输出它是第几位：
# target = 'hello huice'
# for i in target:
# 	if target.count(i) == 1:
# 		print(i)
# 		print(target.index(i))
# 		break

#输出旋转风车
# while True:
# 	for i in ['|','-','\\','/']:
# 		print(i+'\r',end ='')

#输出n阶乘
# num = int(input('请输入正整数：'))
# a =1
# for i in range(1,num+1):
# 	a=a*i
# print('%d的接乘是：%d'%(num,a))

#分别使用while 和for 循环输出1-100之前的所有偶数
# a=1
# s=1
# while True:
# 	if a<100:
# 		if  a % 2 == 0:
# 			print(a,' ',end='')
# 			a=a+1
# 			s=s+1
# 			if s %10 ==0:
# 				print('')
# 		else:
# 			a=a+1
# 	else:
# 		break

# for i in range(0,101):
# 	if i % 2 == 0:
# 		print (i,' ',end='')
# 		if i % 20 == 0 and i !=0:
# 			print('')

#2，找100以内最大平方数  提示 from math import sqrt sqrt(n)
from math import sqrt
# max=0
# for i in range(1,100):
# 	number = sqrt(i)
# 	if number == int(number):
# 		if max < number:
# 			max = number
# print('100以内最大平方数是:%d'%max)

# for i in range(99,0,-1):
# 	root = sqrt(i)
# 	if root == int(root):
# 		print(root)
# 		break


#3,输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# str1 = input('请输入字符：')
# str_total = 0
# space_total=0
# number_total=0
# other_total=0
# for i in str1:
# 	if (ord(i) >=65 and ord(i) <=106) or (ord(i)>=97 and ord(i)<=122):
# 		str_total +=1
# 	elif ord(i) == 32:
# 		space_total +=1
# 	elif ord(i) >= 48 and ord(i)<=57:
# 		number_total+=1
# 	else:
# 		other_total+=1
# print('中英文字母{0}，空格{1}，数字{2}，其他字符{3}'.format(str_total,space_total,number_total,other_total))

# str1 = input('请输入字符串：')
# other = 0
# digit = 0
# space = 0
# alpha = 0
# for i in str1:
# 	if i.isalpha():
# 		alpha += 1
# 	elif i.isspace():
# 		space += 1
# 	elif i.isdigit():
# 		digit += 1
# 	else:
# 		other +=1
# print('中英文字母{0}，空格{1}，数字{2}，其他字符{3}'.format(digit,space,alpha,other))
#4，一个5位数，判断这是不是回文数，即12321是回文数，个位与万位相同，十位与千位相同
# number1 = int(input('请输入5位数：'))
# if number1 >= 10000 and number1 <= 99999:
# 	number = number1
# 	list1=[]
# 	for i in range(5):
# 		n = number % 10
# 		number = number // 10
# 		list1.append(n)
# 	if list1[0] == list1[4] and list1[1]==list1[3]:
# 		print('5位数%d是回文数' % number1)
# 	else:
# 		print('5位数%d不是回文数'%number1)
# else:
# 		print('请重新输入5位数！')

# text=input('请输入一个五位数：')
# for i in range(len(text)):
# 	if text[i] !=  text[-i-1]:
# 		print('%s不是回文数'%text)
# 		break
# else:
# 	print('%s是回文数'%text)
	
# # 打印出100-999中所有的水仙花数，所谓水仙花数是指一个三位数，其各位数字立方和等于该数本身，例如153
# print('100-999之间的水仙花数：')
# for i in range(100, 1000):
# 	ge = i % 10
# 	shi = i % 100//10
# 	bai = i // 100
# 	if i == ge**3+shi**3+bai**3:
# 		print(i, end=' ')
# 输出9*9口
# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print('{0}*{1}={2}'.format(i,j,i*j),end='  ')
# 	print('')
#7，输出100之内的素数总个数，所谓‘素数’是指除了1和它本身以外，不能被任何整数整除的数，例如17
# print('100以内的素数：')
# num=[]
# for i in range(2,101):
# 	j=2
# 	for j in range(2,i):
# 		if i%j == 0 :
# 			break
# 	else: #不能满足所有的for时使用for ...else...
# 		num.append(i)
# print(num,len(num))
#8，算法：python 的冒泡排序  (从大到小)
# list1 = [1,3,2,7,4,9,6]
# swap=0
# for i in range(0,len(list1)):
#    for j in range(i+1,len(list1)):
#       if list1[i]>list1[j]:  #>从小到大，<从大到小
#          swap=list1[i]
#          list1[i]=list1[j]
#          list1[j]=swap
# print(list1)

# alist=[1,3,2,7,4,9,6]
# for i in range(len(alist)-1):
# 	for j in range(0,len(alist)-i-1):
# 		if alist[j]>alist[j+1]:
# 			alist[j],alist[j+1] = alist[j+1],alist[j]
# print(alist)
#9，求输入数之和，输入数小于0时结果
# sum=0
# while True:
# 	a = int(input('请输入：'))
# 	if a < 0:
# 		break
# 	else:
# 		sum += a
# print('输入数据之和：%d'%sum)
'''
*****
*****
*****
*****
'''
# for i in range(0,4):
# 	for j in range(0,5):
# 		print('*',end='')
# 	print()

'''
*****
*   *
*   *
*****
'''
# for i in range(0,4):
# 	if i == 0 or i == 3:
# 		print('*****')
# 		continue
# 	else:
# 		for j in range(0,5):
# 			if j == 0 or j == 4:
# 				print('*',end='')
# 			else:
# 				print(' ',end='')
# 	print()

# for i in range(0,4):
# 	for j in range(0,5):
# 		if i==0 or i == 3 or j == 0 or j ==4:
# 			print('*',end='')
# 		else:
# 			print(' ',end='')
# 	print()
'''
某市的出租车计费标准为：3公里以内为10元，3公里以后每0.5公里加收1元；每等待2.5分钟加收1元；
超过15公里的加收原价的50%为空驶费。要求：对于任意里程数（单位：公里）和等待时间（单位：秒)
计算出应付车费
'''
# s = int(input('请输入里路数：'))
# t = int(input('请输入等待时间：'))
# if s<=3:
# 	c = 10
# elif s > 3 and s <= 15:
# 		c = 10 + int((s - 3) / 0.5 )
# elif s > 15:
# 	c = 10 + ((s - 3) / 0.5 )*1.5
# if t>150:
# 	c += t/150
# print('{0}公里路程，等待时间{1},应付金额{2}'.format(s,t,c))
#一个数如果恰好等于第一因子之和，这个数就是完数，例6=1+2+3 ，编程找出1000以内的所有完数
# print('1000以内的完数如下：')
# for i in range(1,1000):
# 	n=0
# 	for j in range(1,i):
# 		if i % j == 0:
# 			n = n + j
# 	if i == n :
# 		print(i,end=' ')

# print('1000以内的完数如下：')
# for i in range(2, 1000):
# 	list1 = []
# 	for j in range(1, i):
# 		if i % j == 0:
# 			list1.append(j)
# 	if sum(list1) == i:
# 		print(i)
#用python的选择排序完成 实例list1=[49,38,27,45,13]从小到大排序
# list1 = [49,38,27,11,13]
# for i in range(len(list1)-1):
# 	for j in range(i+1,len(list1)):
# 		if list1[i]>list1[j]:
# 			list1[i],list1[j]=list1[j],list1[i]
# 		#print(list1)
# print(list1)
#方法二：
# list1 = [49,38,27,11,13]
# for i in range(len(list1)-1):
# 	min = i
# 	for j in range(i+1,len(list1)):
# 		if list1[min]>list1[j]:
# 			min = j
# 	list1[min], list1[i] = list1[i], list1[min]
# print(list1)

# a=(1,2,3)
# b=(4,5)
# c=[1,2,1,3]
# print (tuple(c),type(tuple(c)))
# print(c.index(2))
# print(c.count(1))
#员工工资条，查询结果集如下((1,'zhangshan',3000),(2,'lisi',4500),(3,'tiantian',20000))计算平均工资
# tup1=((1,'zhangshan',3000),(2,'lisi',4500),(3,'tiantian',20000))
# s=0
# for i in range(len(tup1)):
# 	print(tup1[i][-1])
# 	s += tup1[i][-1]
# avg=s/len(tup1)
# print(avg)
# #员工工资条，查询结果集如下((1,'zhangshan',3000),(2,'lisi',4500),(3,'tiantian',20000))计算最高工资
# tup1=((1,'zhangshan',3000),(2,'lisi',4500),(3,'tiantian',20000))
# list1 =[]
# for i in range(len(tup1)):
# 	list1.append(tup1[i][-1])
# print(max(list1))
# a=[1,2,3]
# b=[4,5,6]
# a[2:2]=b
# print(a)

# str1 = 'title = 华为&sign=0 &limit=100'
# list1 = []
# for i in str1.split('&'):
# 	print(i)
# 	if i.startswith('sign='):
# 		list1.append('sign= ')
# 	else:
# 		list1.append(i)
# print('&'.join(list1))
#
# target = 'hello huice'
# list1 = []
# for i in target:
# 	print(i)
# 	print(list1)
# 	if i not in list1:
# 		list1.append(i)
# print(''.join(list1))
'''
接收用户输入的数字，输入负数时结束输入，存入一个列表，以字符串形式输出：1&2&3&4&5&0
提示：全部数字存储一个列表，利用课上说的新列表实现去重，再拼接成字符串输出
'''
# list1 = []
# while True:
# 	a = int(input('请输入一个数字，输入负数停止: '))
# 	if a >= 0:
# 		list1.append(a)
# 	else:
# 		break
# new = []
# for i in list1:
# 	if str(i) not in new:
# 		new.append(str(i))
# print('您输入的数字组合是：%s'%'&'.join(new))

# list =[1,2,3]
# list.append('45')
# print(list)
# list.extend('56')
# print(list)
# list.insert(4,'c')
# print(list)
# print(list.index('c'))
# list.pop()
# print(list)
# list.pop(4)
# print(list)
# list1 = [1,2,3,8,7]
# list1.remove(3)
# print(list1)
# list1.reverse()
# print(list1)
# list1.sort() #升序
# print(list1)
# print(sorted(list1)) #升序
# str_list =['c','c#','java','python','ruby','javascript']
# str_list.sort(key=len,reverse=True) #升序
# print(str_list)
# sorted(str_list,key=len,reverse=True)
# print(str_list)
# str_list.reverse()#降序
# print(str_list)


# list = [[1, 'zhangshan', 3000], [2, 'lisi', 2500], [3, 'tiantian', 20000]]
# print(sorted(list,key=lambda x:x[-1],reverse=True)[0][-1])

#输入一个字符串'address=bejing&limit=200&title=huice_test&time=2018-04-30&username=tianlaoshi'转换为user=tianlaoshititle=huice_test&time=2018-04-30&limit=200&address=bejing
# str = 'address=bejing&limit=200&title=huice_test&time=2018-04-30&username=tianlaoshi'
# list =str.split('&')
# for i in list:
# 	if i.startswith('username='):
# 		list.remove(i)
# 		user = i.split('=')[-1]
# 		print(user,'s')
# list.sort(reverse=True)
# print ('user=%s%s'%(user,'&'.join(list)))
# print('user='+user,'&'.join(list))
#传统
# a = [1,2,3,4,5,6]
# new = []
# for x in a:
# 	new.append(x**2)
# print(new)
# #新方法
# a = [1,2,3,4,5,6]
# new = [i**2 for i in a]
# print (new)
#1 a=[1,2,3,4,5,6] 一行代码实现对a中的偶数位置的元素进行加3，组成新的列表
# a=[1,2,3,4,5,6]
# new = [i+3 for i in (0,len(a),2)]
# print(new)

#2.x=[1,2,3,4] y=[5,6,7,8] 一行代码输出，一个新的列表，两个list中的偶数分别相加，结果 【2+6,4+6,2+8,4+8】
# x=[1,2,3,4]
# y=[5,6,7,8]
# list =[]
# for i in y:
# 	if i%2 ==0:
# 		for j in x:
# 			if j % 2 == 0:
# 				list.append(i+j)
# print(list)
# a=[1,2,3]
# b=[4,5]
# print(a+b)
# print(a*3)
# a +=b
# print (a)
# a = [1,2,3,4]
# b = ['a','b','c']
# c = [100,200,300]
# d = list(zip(a,b,c))
# print(d)

# a = [1,2,3,4]
# b = ['a','b','c']
# c = [100,200,300]
# d = list(zip(,a,b,c))
# print(d)

#用zip函数组合输出 ((1,'zhangshan',3000),(2,'lisi',4500),(3,'tiantian',20000))

# a=set([1,2,3])
# #set集合取值
# print(a,type(a))
# for i in a:
# 	print(i)
# #set 去重
# b=set([1,2,3,4,3])
# print(b)

# list1 = [1,2,3,1,2,3]
# new = []
# for i in list1:
# 	if i not in new:
# 		new.append(i)
# print (new)
# #去重按ascii重新排序升序
# new1=list(set(list1))
# new1.sort(key=list1.index)
# print(new1)
# a=[1, 2, 3, 5, 6]
# b=[0, 2, 5, 7]
# new =[]
# for i in a:
# 	if i not in new:
# 		new.append(i)
# for j in b:
# 	if j not in new:
# 		new.append(j)
# print(new)
#
# a=[1, 2, 3, 5, 6]
# b=[0, 2, 5, 7]
# new =[]
# a.extend(b)
# for i in a:
# 	if i not in new:
# 		new.append(i)
# print(new)

# a = [1, 2, 3, 5, 6]
# b = [0, 2, 5, 7]
# c = list(set(a+b))
# #c.sort( key = a.index)
# print(c)
#大脚超市赊账人中名单如下：['刘能','王老七','谢广坤','赵玉田','杨晓燕','刘大脑袋','王长贵','谢飞机','赵四','王大拿']，大脚想移除里面姓氏重复的人（不考虑复姓），但是对于每种姓氏大脚保留最后出现的那个人。希望你来帮助她
# names=['刘能','王老七','谢广坤','赵玉田','杨晓燕','刘大脑袋','王长贵','谢飞机','赵四','王大拿']
# f_names= []
# result = []
# for name in range(len(names)-1,0,-1):
# 	print(names[name][0])
# 	if names[name][0] not in f_names:
# 		f_names.append(names[name][0])
# 		result.append(names[name])
# print(sorted(result,key=names.index))

# a={'id':1,'name':'zhangsan','salay':1}
# a['id']=2
# print(a['id'])
#把字符串'k1:1|k2:2|k3:3'处理成python字典的形式{‘ke':3,'k2':2,'k1':1}
# c= 'k1:1|k2:2|k3:3'
# d= {}
# list =c.split('|')
# for i in list:
# 	key = i.split(':')[0]
# 	value = i.split(':')[1]
# 	d[key] = value
# print(d)
# del d['k3']
# print(d)

# d={'k1': '1', 'k2': '2', 'k3': '3'}
# print('k1' in d)
# print(d.keys(),d.values(),d.items())
# d.pop('k3')
# for i in d.items():
# 	print(i)
# l =('zhangsan','tianlaoshi')
# m = dict.fromkeys(l,0)
# print(m)

# d0 ={'k3':1,'k2':2}
# d00=d0.get('k6')
# print(d00)

# d1 ={'k3':1,'k2':2}
# d2 = {'k3':0,'k4':5}
# d1.update(d2)
# print(d1)


# d1 ={'k3':1,'k2':2}
# for key in d1.keys():
# 	print(key)
# for value in d1.values():
# 	print(value)
# for items in d1.items():
# 	print(items)
#
# for key,value in d1.items():
# 	print(key,value)
#去除字典value重复的项(‘zhangsan’:100,'lisi':65,'tianlaoshi':65,'liulaoshi':99)
# dic =  {'zhangsan':100,'lisi':65,'tianlaoshi':65,'liulaoshi':99}
# list_value=[]
# del_dic=[]
# for key,value in dic.items():
# 	if value in list_value:
# 		del_dic.append(key)
# 	list_value.append(value)
# for k in del_dic:
# 	dic.pop(k)
# print(dic)

# dic =  {'zhangsan':100,'lisi':65,'tianlaoshi':65,'liulaoshi':99}
#
# for k,v in dic.items():
# 	if dic.values().count(v)>0:
# 		del dic[k]
# print(dic)

#排序
# dic =  {'zhangsan':100,'lisi':65,'tianlaoshi':65,'liulaoshi':99}
# print(sorted(dic.keys()))
# print(sorted(dic.items(),key = lambda item:item[0]))
# print(sorted(dic.values()))
# print(sorted(dic.items(),key = lambda item:item[1]))

# dic =  {'zhangsan':100,'lisi':65,'tianlaoshi':65,'liulaoshi':99}
# def my_sort(x):
# 	return x
# print(sorted(dic.items(),key=my_sort))

#编写一组数据，记录组内每个人的语文成绩，求平均分，找出学霸
# data ={
# 		'JiaNaiLiang': 60,
# 		'LiXiaoLu': 75,
# 		'TianLaoShi': 99,
# 		'MaSu': 88,
# 		'KongLingHui': 35,
# 		'LiuLaoShi': 100}
# avg_sco = float(sum(data.values()))/len(data)
# print('平均分：',avg_sco)
# max_sco = max(data.values())
# print('最高分：',max_sco)
# print('学霸：',sorted(data.items(),key = lambda x:x[-1],reverse=True)[0][0])

#编写一组数据，记录组内每个人的语文、数学、英语成绩a.找出平均分不足60分的人    b.找出各科的最高分 c.算出各科的平均分，再找出各科的学霸
# data = {
# 		'JiaNaiLiang': [60, 68, 45],
# 		'LiXiaoLu': [10, 28, 5],
# 		'TianLaoShi': [44, 86, 73],
# 		'MaSu': [99, 95, 95],
# 		'KongLingHui': [98, 65, 100],
# 		'LiuLaoShi': [77, 97, 65]
# }
#a.找出平均分不足60分的人
# for k, v in data.items():
# 	if sum(v)/len(v) < 60:
# 		print(k)
#b.找出各科的最高分
# shuxue=[]
# yuwen=[]
# yingyu=[]
# for v in data.values():
# 	shuxue.append(v[0])
# 	yuwen.append(v[1])
# 	yingyu.append(v[2])
# print('数学最高分：%s,语文最高分：%s,英文最高分：%s'%(max(shuxue),max(yuwen),max(yingyu)))
#c.算出各科的平均分，再找出各科的学霸
# shuxue=[]
# yuwen=[]
# yingyu=[]
# for k,v in data.items():
# 	shuxue.append(v[0])
# 	yuwen.append(v[1])
# 	yingyu.append(v[2])
# print('数学平均分：%s,语文平均分：%s,英文平均分：%s'% (float(sum(shuxue))/len(shuxue), float(sum(yuwen))/len(yuwen) ,float(sum(yingyu)) /len(yingyu)))
# print('数学学霸：',sorted(data.items(),key = lambda x:x[-1][0],reverse=True)[0][0])
# print('语文学霸：',sorted(data.items(),key = lambda x:x[-1][1],reverse=True)[0][0])
# print('英文学霸：',sorted(data.items(),key = lambda x:x[-1][2],reverse=True)[0][0])

'''
1、编写一组数据，记录组内每个人的语言成绩、数学成绩、英语成绩
data={
'小明'：{‘语文’:60,'数学':68,'英语':54},
'小璐'：{‘语文’:10,'数学':28,'英语':5},
'小辉'：{‘语文’:44,'数学':86,'英语':73},
'小亮'：{‘语文’:99,'数学':95,'英语':95},
'田老师'：{‘语文’:98,'数学':65,'英语':100},
'刘老师'：{‘语文’:77,'数学':97,'英语':65},
}
a.找出平均分不足60分的人   b.找出各科的最高分，平均分    c，找出各科的学霸
'''
# data={
# 		'小明':{'语文':60,'数学':68,'英语':54},
# 		'小璐':{'语文':10,'数学':28,'英语':5},
# 		'小辉':{'语文':44,'数学':86,'英语':73},
# 		'小亮':{'语文':99,'数学':95,'英语':95},
# 		'田老师':{'语文':98,'数学':65,'英语':100},
# 		'刘老师':{'语文':77,'数学':97,'英语':65},
# }
# def avg(list):
# 	return sum(list)/len(list)
# list=[]
# yuwen={}
# shuxue= {}
# yingyu= {}
# for name,score_dic in data.items():
# 	score_list = score_dic.values()
# 	yuwen[name]=(score_dic.get('语文',0))
# 	shuxue[name]=(score_dic.get('数学',0))
# 	yingyu[name]=(score_dic.get('英语',0))
# 	score_dic.get('英语',0)
# 	if avg(score_list)<60:
# 		list.append(name)
# print('平均分不足60的同学：',' '.join(list))
# print('语文最高分：%s,数学最高分：%s,英文最高分：%s'%(max(yuwen.values()),max(shuxue.values()),max(yingyu.values())))
# print('语文平均分：%s,数学平均分：%s,英文平均分：%s'%(avg(yuwen.values()),avg(shuxue.values()),avg(yingyu.values())))
# print('语文学霸：%s,数学学霸：%s,英文学霸：%s'%(max(yuwen , key =yuwen.get),max(shuxue,key=shuxue.get),max(yingyu,key=yingyu.get)))
# print('语文学霸：%s'%(sorted(yuwen.items(),key=lambda x:x[1],reverse=True))[0][0])
#第二种方法
# data={
# 		'小明':{'语文':60,'数学':68,'英语':54},
# 		'小璐':{'语文':10,'数学':28,'英语':5},
# 		'小辉':{'语文':44,'数学':86,'英语':73},
# 		'小亮':{'语文':99,'数学':95,'英语':95},
# 		'田老师':{'语文':98,'数学':65,'英语':100},
# 		'刘老师':{'语文':77,'数学':97,'英语':65},
# }
# for k,v in data.items():
# 	avg_scor=float(sum(v.values()))/len(v.values())
# 	if avg_scor <60:
# 		print('%s平均分小于60,平均分为%s'%(k,avg_scor))
# yuwen=[]
# shuxue=[]
# yingyu=[]
# for v1 in data.values():
# 	nv=list(v1.values())
# 	yuwen.append(nv[0])
# 	shuxue.append(nv[1])
# 	yingyu.append(nv[2])
# print('语文最高分：%s,数学最高分：%s,英文最高分：%s'%(max(yuwen),max(shuxue),max(yingyu)))
# print('语文平均分：%s,数学平均分：%s,英文平均分：%s'%(sum(yuwen)/len(yuwen),sum(shuxue)/len(shuxue),sum(yingyu)/len(yingyu)))

'''
2统计一篇英文文章每个单词出现频率，并返回出现频率最高的前5个单词及其出现的次数（字典形式）
A small sample of texts from Project Gutenberg appears in the NLTK corpus collection.
However,you maybe interested in analyzing other texts from Project Gutenberg. You Can browse
 the catalog of 25000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to
 an ASCII text file. Although 90% of the texts in Project Guthenberg are in English,it includes
 material in over 50 other languages, including, Chinese, Dutch, Finnish, French, German, Italian
'''
#第一种 方法
# from collections import Counter
# import re
# with open('test.txt','r',encoding='utf-8') as f:
# 	txt = f.read()
# c = re.split(' ',txt)
# Cnt = Counter(c)
# ##1. 获取到的是一个大字典里面统计了单词出现的次数.
# print(Cnt)
# ret = Cnt.most_common(5)
# ##2. 统计了前十个单词出现的次数.
# print(ret)

#第二种 方法
# text ='A small sample of texts from Project Gutenberg appears in the NLTK corpus collection.However,you maybe interested in analyzing other texts from Project Gutenberg. You Can browse the caalog of 25000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. Although 90% of the texts in Project Guthenberg are in English,it includes material in over 50 other languages, including, Chinese, Dutch, Finnish, French, German, Italian'
# list = text.lower().split(' ')
# dic={}
# for i in list:
# 	if i.endswith(',') or i.endswith('.'):
# 		i = i[:-1]
# danci={}.fromkeys(list,0).keys()
# print(danci,type(danci))
# for i in danci:
# 	dic[i]=list.count(i)
# print(sorted(dic.items(),key=lambda  x:x[-1],reverse=True)[:5])
##3. 统计了前十个单词出现的次数放在了一个列表里面.
# lt =[]
# for i in ret:
# 	x=i[0]
# 	lt.append(x)
# print(lt)

#参数
#1.不指定参数名
# def my_function(a,b):
# 	print(a+b)
# my_function(1,2)
#2.指定参数名
# def my_funcation1(name,age):
# 	print('姓名:%s,年龄:%s'%(name,age))
# my_funcation1('zhangsan',10)
# my_funcation1(10,'zhangsan')
# my_funcation1(age=10,name='zhangsan')
#3.指定默认值
# def my_function2(name,age=18):
# 	print('姓名%s,年龄%s'%(name,age))
# my_function2('ztt')
# my_function2('ztt',16)

# def enroll(name,gender,age=7,city='Beijing'):
# 	print('name:',name)
# 	print('gender:',gender)
# 	print('age:',age)
# 	print('city:',city)
# 	print('--------------')
# enroll('itanweifang',0)
# enroll('liuze',0,7,'shanghai')
# enroll(gender=1,age=5,name='zhangsan')

# def my_function3(name,age=10,scores=[0,0,0]):
# 	print('姓名:%s,年龄:%s，成绩：%s'%(name,age,scores))
# my_function3('ztt',scores=[1,2,3])

# def extendList(val,list=None):
# 	if list is None:
# 		list=[]
# 	list.append(val)
# 	return list
#
# list1 = extendList(10)
# list2 = extendList(123 , [])
# list3 = extendList('a')
# print('list1=%s' % list1)
# print('list2=%s' % list2)
# print('list3=%s' % list3 )

# 可变参数
# def checkin(name,id,*other):
# 	print('姓名：%s,工号：%s，其他信息：%s'%(name,id,other))
# checkin('田老师','1234',1380000000,'mm')
# def checkin2(name,id,**other):
# 	print('姓名：%s,工号：%s，其他信息：%s' % (name, id, other))
# checkin2('李老师','332',phone=13100000,address='beijing')

#domain /url=None data=None
#http://127.0.0.1/huice/api?name=tiantian&password=123
# def url_format(domain,url=None,data=None):
# 	result ='http://'+domain
# 	if url:
# 		result = result+'/'+url
# 	if data:
# 		list =[]
# 		for k,v in data.items():
# 			list.append(k+'='+v)
# 		result = result+'?'+'&'.join(list)
# 	return result
#
# print(url_format('127.0.0.1','huice/api',{'name':'tiantian','password':'123'}))
# def fact(n):
# 	if n == 1:
# 		return 1
# 	return n*fact(n-1)
# print(fact(5))

#递归回声
# def fact_voice(context):
# 	if len(context) == 0:
# 		return 0
# 	print(context)
# 	context = context[1:]
# 	return fact_voice(context)
# fact_voice('我爱北京天安门')

#高阶函数
# def add(a,b,f):
# 	return f(a)+f(b)
# def f(x):
# 	return x**2
# print(add(2,3,f))
#
# print(add(2,3,lambda x:x**2))


#map
#方法1
# a=[1,2,3,4,5]
# list=[]
# for i in a :
# 	list.append(i**2)
# print(list)
# #方法2
# print(map(lambda x:x**2,a))
# #方法3
# print([i**2 for i in a])

'''
利用map函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字，输入：['adam','LISA','barT']
'''
# data =['adam','LISA','barT']
# print(list(map(lambda x:x.capitalize(),data)))

#filter
# a=[1,2,3,4,5,6,9,10,15]
# result =list(filter(lambda x:(x% 2==0),a))
# print(result)
#筛选有效输入
# b =['A','B ',None,'c',' ',False,[]]
# print(list(filter( lambda x : x and x.strip(),b)))

#接收用户输入的数字，输入负数时结束输入，存入一个列表，以字符串形式输出：1&2&3&4&5&0
# list1 = []
# def mylist1(*args):
# 	new = []
# 	for i in args:
# 		if str(i) not in new:
# 			new.append(str(i))
# 	return '&'.join(new)
# list2=[2,3,4,2,5]
# res = mylist1(*list2)
# print(res)

#用python的选择排序完成 实例list1=[49,38,27,45,13]从小到大排序
# def mylist2(args):
# 	for i in range(len(args)-1):
# 		for j in range(i+1,len(args)):
# 			if args[i]>args[j]:
# 				args[i],args[j]=args[j],args[i]
# 		print(args)
# 	return args
# list3=[49,38,27,45,13]
# res1 = mylist2(list3)
# print(res1)


# class A:
# 	xuefei=8800
# 	#构造函数、初始化函数
# 	def __init__(self,name):
# 		''' self 代表当前对象'''
# 		self.name=name
# 	def print_name(self): #成员方法
# 		print(self.name)
# 	@classmethod#类方法
# 	def print_xuefei(cls):
# 		print(cls.xuefei)
# 	@staticmethod#静态方法
# 	def my_print():
# 		print(A.xuefei)

# zhangsan = A('张三')
# zhangsan.print_name()
# zhangsan.xuefei=9900
# print(zhangsan.xuefei)
#
# A.xuefei=10000
# lisi = A('李四')
# lisi.print_name()
# print(lisi.xuefei)
#类方法和静态方法不需要对象，可以直接调用
#print(A.print_xuefei()) #类方法
# A.my_print()  #静态方法

# class Student:
# 	school ='sipai'
# 	__expenses ='8800'
# 	def __init__(self,name,age):
# 		self.name=name
# 		self.age=age
# 		self.score=0
# 		self.i=0
# 	def set_score(self,score):
# 		self.score=score
# 	def get_socre(self):
# 		return self.score
# 	def __len__(self):
# 		return(self.name)
# 	def __iter__(self):
# 		return self
# 	#def __next__(self):
# std1=Student('zhangsan',20)
# std1.set_score(85)
# print(std1.name)

# class Auto:
# 	speed = 0

# 	def __init__(self,name):
# 		self.name=name
# 		self.speed=0
# 	def start(self):
# 		print('%s车开始运行'%self.name)
# 	def speedup(self):
# 		self.speed += 10
# 		return self.speed
# 	def stop(self):
# 		if self.speed>= 30:
# 			self.speed -=30
# 			return self.speed
# 		else:
# 			return 0
# if __name__=='__main__':
# 	auto1= Auto('BMW')
# 	auto1.start()
# 	auto1.speedup()

#
# class Stack:
# 	def __init__(self,size):
# 		self.__size=size
# 		self.__data=[]
# 	def get_size(self):
# 		return self.__size
# 	def __isfull__(self):
# 		if len(self.__data)<self.__size:
# 			return False
# 		else:
# 			return True
# 	def __isspace__(self):
# 		if len(self.__data) > 0:
# 			return True
# 		else:
# 			return False
# 	def push(self,a):
# 		if len(self.__data)<self.__size:
# 			self.__data.append(a)
# 	def pop(self):
# 		if len(self.__data) > 0:
# 			self.__data.pop()
# 		return self.__data
# 	def __str__(self):
# 		return ''.join(self.__data)
# if __name__=='__main__':
# 	demo1=Stack(5)
# 	demo1.push('a')
# 	demo1.push('b')
# 	demo1.push('c')
# 	print(demo1.pop())
# 	print (demo1)
#
# import traceback
# try:
# 	#print(5/0)
# 	print(1)
# except (TypeError,ZeroDivisionError) as e:
# 	print(e)
# 	print(traceback.print_exc())
# finally:
# 	print('finally')
# print(2)

# data={'login.py':'a 8 d 2 u 3 ','order.py':'a 15 d 0 u 34','info.py':'a 1 d 20 u 5 '}
# newlist=[]
# for k,v in data.items():
# 	list =v.split(' ')
# 	sum=0
# 	for i in list:
# 		if i.isdigit():
# 			sum+=int(i)
# 	print(k,'文件变更：',sum)

# data={'login.py':'a 8 d 2 u 3 ','order.py':'a 15 d 0 u 34','info.py':'a 1 d 20 u 5 '}
# for k,v in data.items():
# 	line =[]
# 	list =v.split(' ')
# 	for i in list:
# 		try:
# 			line.append(int(i))
# 		except:
# 			pass
# 	print('文件%s变更%d行'%(k,sum(line)))

#接受用户输入的一个字符串，如果是正整数就判断是否能同时被3和7整除
# number =input('请输入一个数：')
# if number.isdigit() or (number.startswith('-') and number[1:].isdigit()):
# 	number = int(number)
# 	if number>0:
# 			if number%3==0 and number % 7 ==0:
# 				print(number,'能够被3和7同时整除')
# 			else:
# 				print(number,'不能够被3和7同时整除')
# 	else:
# 		print(number,'不是正整数')
# else:
# 	print('输入的包含非数字')

#优化后
# number =input('请输入一个数：')
# try:
# 	number = int(number)
# 	if number>0:
# 			if number%3==0 and number % 7 ==0:
# 				print(number,'能够被3和7同时整除')
# 			else:
# 				print(number,'不能够被3和7同时整除')
# 	else:
# 		print(number,'不是正整数')
# except:
# 	print('输入的包含非数字')
# def sum(a,b):
# 	if a==0 or b==0:
# 		raise  BaseException('不能为0')
# 	else:
# 		return a+b

# def sum(a,b):
# 	if a==0 or b==0:
# 		try:
# 			raise  BaseException('不能为0')
# 		except BaseException as e :
# 			print(e)
# 			return None
# 	else:
# 		return a+b
# if sum(1,0):
# 	print(sum(1,0))
# else:
# 	print('有错误')

# def sub(a,b):
# 	if a<b:
# 		raise BaseException('被减数不能小于减数')
# 	else:
# 		return a-b
# print(sub(3,5))

# def sub(a,b):
# 	try:
# 		return a/b
# 	except ZeroDivisionError as e:
# 		print (e)
# 		return 0

# print(sub(2,0))

# def sum():
# 	a = input('请输入第一个数字')
# 	b = input('请输入第二个数字')
# 	result = 0
# 	try:
# 		result = input(a) + int(b)
# 	except:
# 		pass
# 	return result
# print(sum())

import sys
print(sys.path)