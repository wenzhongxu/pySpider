# -*- coding:utf-8 -*- 
'''lambda function'''
def f(i): #用户自定义返回平方数
	return i * i
print (f(3))
	
g = lambda x : x * x
print(g(3))

'''包含多个参数lambda函数'''
def f(x,y):
	return x + y
print(f(3,4))

g = lambda x,y : x + y
print(g(3,4))

'''
filter
对指定序列执行过滤操作，filter(function or None,sequence)
filter函数会对序列参数sequence中的每个元素调用function函数，最后返回的结果包含调用结果为True的元素
'''
def is_Even(i):
	if(i % 2 == 0):
		return True
	else:
		return False

l = [1,2,3,4,5,6,7,8,9,10]
l = filter(is_Even,l)
print(l)    #3.x 返回的是对象 filter object
l = list(l)  #3.x 须做类型转换
print(l)

l = [1,2,3,4,5,6,7,8,9,10]
l = list(filter(lambda x : x % 2 == 0,l))  #结合lambda
print(l)

'''
map函数
对指定序列做映射操作，map(function or None,sequence)
对序列参数sequence中的每个元素调用function函数，返回的结果为每一个元素调用function函数的返回值
'''
def sqr(i):
	return i**2
	
l = [1,2,3]
l = map(sqr,l)
print(l)   #3.x 返回的是对象 map  object
l = list(l)
print(l)

l = [1,2,3]
l = list(map(lambda x : x**2,l))  # 结合lambda
print(l)

'''
reduce 对指定序列做迭代操作
函数中的function参数是一个有两个参数的函数，reduce依次从 sequence 中取一个元素，和上一次调用 function 的结果做参数再次调用function
'''
from functools import reduce  #3.x 版本需要引入
def sum(x,y):
	return x + y

l = [1,2,3,4,5,6]
l = reduce(sum,l)
print(l)

l = [1,2,3,4,5,6]
l = reduce(lambda x,y : x + y,l) #结合lambda
print(l)
help(reduce)    #查看reduce帮助