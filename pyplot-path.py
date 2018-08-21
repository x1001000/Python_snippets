import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import requests
database = 'https://raw.githubusercontent.com/x1001000/www.edc.tw/gh-pages/json/'
filename = hex(ord(input('給個中文字：'))).split('x')[1]
strokes = requests.get(database+filename+'.json').json()
#print(len(strokes))            #筆畫數
#print(type(strokes[0]))        #一個筆畫是一個字典
#print(dict.keys(strokes[0]))   #這個字典內全部的key

verts = []
codes = []
movetos = []
track = []

for stroke in strokes:
    for point in stroke['outline']:
        if point['type'] == 'M':
            verts.append((point['x'], point['y']))
            codes.append(Path.MOVETO)
            movetos.append((point['x'], point['y']))
        if point['type'] == 'L':
            verts.append((point['x'], point['y']))
            codes.append(Path.LINETO)
        if point['type'] == 'Q':
            verts.append((point['begin']['x'], point['begin']['y']))
            verts.append((point['end']['x'], point['end']['y']))
            codes.append(Path.CURVE3)
            codes.append(Path.CURVE3)
    for point in stroke['track']:
        track.append((point['x'], point['y']))

永  = [ ]
永 += [ verts[:25] ]
永 += [ verts[80:117]+verts[31:56] ]
永 += [ verts[148:187]+verts[117:124] ]
永 += [ verts[196:252] ]
if __name__ == '__main__':
    ax = plt.figure().add_subplot(111)
    ax.set_xlim(0, 2000)
    ax.set_ylim(2000, 0)

    path = Path(verts, codes)
    patch = PathPatch(path, facecolor='orange', lw=1)
    ax.add_patch(patch)

    xs, ys = zip(*verts)
    ax.plot(xs, ys, 'o-', color='red', ms=5, lw=1)

    plt.show()
