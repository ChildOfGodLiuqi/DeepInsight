
# coding: utf-8

# 数据类型
'''
int 
float  
str
'''

a=3
type(a)

a=3.0
type(a)

a='I am ok'
type(a)


#----------------------------------

## 列表list   有序的可变表

list_var=[]      # 定义列表
list_var=list()  # 定义列表

list_var=['a','b','c']
list_var.append('d')   #添加元素
print(list_var)

list_var=['a','b','c']
list_var.insert(0,'d')  #在指定位置添加元素
print(list_var)

list_var=['a','b','c']
list_var.pop()
print(list_var)    #删除末尾元素

list_var=['a','b','c']
list_var.pop(1)    #按索引删除指定位置元素
print(list_var)

list_var=['a','b','c']
list_var.pop(1)    #删除指定位置元素
print(list_var)

list_var=['a','b','c']
list_var.remove('a')
print(list_var)

list_var=['a','b','c']
print(list_var[1])  #索引元素  
print(list_var[-1]) #逆序索引
print(list_var.index('b')) #获取知道元素索引
print(len(list_var)) #计算列表长度


#----------------------------------
#  元组 tuple 有序的列表，一旦初始化就不能修改

tuple_var=()      # 定义空元组
tuple_var=tuple()

tuple_var=(1,)  # 只有一个元素的元组定义

tuple_var=('a','b','c')
print(tuple_var[1])  #索引元素
print(tuple_var[-1]) #逆序索引元素

#tuple_var[0]='d'     #报错， 元组不能变更内容

tuple_var=('a','b',['x','y'])
tuple_var[2][0]='z'   #可修改，更改的是元素内容，而本元素被身
#tuple_var[2]=['a',6]  #不可修改

tuple_var=('a','b',('x','y'))
#tuple_var[2][0]='z'   #不可修改

print(len(tuple_var)) # 计算元素个数


#----------------------------------
# 字典  查询速度快，但耗费空间多，key 要求为不可变对象
dict_var={}     # 定义空字典
dict_var=dict()

dict_var={'key1':1,'key2':2,'key3':3}
dict_var['key4']=4  #在字典中添加key-value对
dict_var['key1']=10 #修改key1键对于的值(value)
print(dict_var)

dict_var={'key1':1,'key2':2,'key3':3}
dict_var.pop('key1')
print(dict_var)  #删除key-value对

dict_var={'key1':1,'key2':2,'key3':3}
print(dict_var['key1'])  #获取key1键的值
#print(dict_var['key4'])  #不存key4在报错

print(dict_var.get('key1'))
print(dict_var.get('key4')) #不存在返回None
print(dict_var.get('key4','null')) #返回指定值

dict_var={'key1':1,'key2':2,'key3':3}
print(dict_var.keys())   #字典键集合
print(dict_var.values()) #字典值集合
print(dict_var.items())  #键值对集合


#----------------------------------
# 集合 类似dict，但没有value，
set_var=set()  #定义空集合

set_var=set(['a','b','c']) #定义集合 ，输入list列表
#set_var=set(6,2)  #报错
print(set_var)

set_var=set(['a','b','c','b']) #结合结果为{'b','c','a'} 不允许有相同的key
print(set_var) 

set_var=set(['a','b','c'])
set_var.add('d')    #添加元素
print(set_var)  

set_var=set(['a','b','c'])
set_var.remove('c')    #删除元素
print(set_var)

#set_var[0]  #保存，不能索引取值

set_var1=set(['a','b','c'])
set_var2=set(['b','c','d'])

print(set_var1 & set_var2) #交集
print(set_var1.intersection(set_var2))

print(set_var1 | set_var2) #并集
print(set_var1 .union(set_var2))

print(set_var1-set_var2)   #差集
print(set_var1.difference(set_var2))

# set_var1=set(['a','b','c',['a','b']])  #报错，不可以放入可变变量
set_var1=set(['a','b','c',('a','b')]) 
print(set_var1)

#----------------------------------
import re
# 验证邮箱正则表达式
def is_valid_email(addr):
    if re.match(r'[A-Za-z0-9\.\_]+@[a-zA-Z]+(\.com)',addr):
        return True
    else:
        return False
    
print(is_valid_email('someone@gmail.com'))
print(is_valid_email('bill.gates@microsoft.com'))
print(is_valid_email('bob#example.com'))
print(is_valid_email('mr-bob@example.com'))

# 提取邮箱名字
def name_of_email(addr):
    
    name=re.match(r'<[a-zA-Z\s]+>',addr)
    if name:
        name=name.group(0)
        return name[1:len(name)-1]
    else:
        name=re.match(r'\S+@',addr).group(0)
        return name[:-1]
    
print(name_of_email('<Tom Paris> tom@voyager.org'))
print(name_of_email('tom@voyager.org'))


