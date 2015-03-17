#coding: utf-8

import datetime
import sys

today = datetime.date.today()
print "今日の日付↓"
print today

print 'シングルクオート文字列'
print "ダブルクオート文字列"

print """
複数行表示１
複数行表示２
"""
character_valiable = "文字列結合あ"
print character_valiable + '文字列結合い'

chara_test = 100
str(chara_test)
if type(chara_test):
    print "文字です"
else:
    print "数値です"

chara_search = "abcdefghijklmnopqrstuvwxyzあ"
print "f" in chara_search
print "い" in chara_search

num_test = 100
int(num_test)
if type(num_test):
    print "文字列です。"
else:
    print "数値です。"

test_list1 = ['python', '-', 'izm', '.', 'com']
print test_list1
print '-------------------------------------'
for i in test_list1:
    print i

test_list2 = []
print test_list2
print '--------------------------------------'
test_list2.append('p')
test_list2.append('y')
test_list2.append('t')
test_list2.append('h')
test_list2.append('o')
test_list2.append('n')

print test_list2

test_dectionary1 = {'YEAR' : '2010', 'MONTH' : '1', 'DAY' : '1'}
print test_dectionary1
print '==============================================='

for i in test_dectionary1:
    print i
    print test_dectionary1[i]
    print '--------------------------------------'

print test_dectionary1['YEAR']
print test_dectionary1.get('MONTH')

test_dectionary2 = {'math': 90, 'japanese': 30, 'english': 100}
print test_dectionary2
print test_dectionary2.get('japanese')
print test_dectionary2.get('english')
print test_dectionary2.get('math') 

print '↓データ削除後'

del test_dectionary2['japanese']

print test_dectionary2

test_number = 100
print test_number

test_number += 1
print test_number

print '==========================================='
for i in range(21):
    print i
    
    if i == 20:
        print '20回に到達したので終了'

    elif i == 10:
        print 'あと半分'

test_value = 10

if test_value == 100:
    print 'test_valueは100です'
elif test_value == 10:
    print 'test_valueは10です'
else:
    print 'test_valueは10または100以外です'

