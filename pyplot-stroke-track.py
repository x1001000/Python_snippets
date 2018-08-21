#coding:utf-8
#python2
import urllib
import json
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

word = raw_input("只要一個中文字：").decode('utf8')[0] # 'big5' for PC
hex4 = hex(ord(word)).split('x')[1]
urllib.urlretrieve('https://raw.githubusercontent.com/x1001000/www.edc.tw/gh-pages/json/'+hex4+'.json',word+'.txt')
with open(word+'.txt', 'r') as f:
    strokes = json.load(f)

#print len(strokes)              #筆畫數
#print type(strokes[0])          #一個筆畫是一個字典
#print dict.keys(strokes[0])     #字典所有的key
#print strokes[0]['track']       #'track'的value是一個字典串

verts = []
codes = []

Xs = []
Ys = []

for stroke in strokes:
    xs = []
    ys = []
    for point in stroke['outline']:
        if point['type'] == 'M':
            verts.append((point['x'], point['y']))
            codes.append(Path.MOVETO)
        if point['type'] == 'L':
            verts.append((point['x'], point['y']))
            codes.append(Path.LINETO)
        if point['type'] == 'Q':
            verts.append((point['begin']['x'], point['begin']['y']))
            verts.append((point['end']['x'], point['end']['y']))
            codes.append(Path.CURVE3)
            codes.append(Path.CURVE3)
    for point in stroke['track']:
        xs.append(point['x'])
        ys.append(point['y'])
    Xs.append(xs)
    Ys.append(ys)

path = Path(verts, codes)
patch = PathPatch(path, facecolor='red', lw=2)
#xs, ys = zip(*path.vertices)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.add_patch(patch)

P=[]
for xs, ys in zip(Xs, Ys):
    ax.plot(xs, ys, 'o-', lw=5, color='green', ms=5)
    P.append(zip(xs, ys))
print P

ax.set_xlim(0, 2000)
ax.set_ylim(2000, 0)

plt.show()
