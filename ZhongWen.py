#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
name = '小明'
print(f'{name}的成绩提升了 {r:.1f}%')
print('%s的成绩提升了 %.1f%%' % ('小明', r))
print('{0}的成绩提升了 {1:.1f}%'.format('小明', r))

collegues = ['Mark','Tara','Jack','Faheem','Cici']
print(len(collegues))
print(collegues[0])
print(collegues[-2])
collegues.append('Mario')
collegues.insert(2, 'Jeffrey')
collegues[0] = 'Yuyi'
print(collegues)