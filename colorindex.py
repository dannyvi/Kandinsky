#!/usr/local/bin/python3.4
#-*-coding:utf-8-*-
"""
提供了孟塞尔色立体的所有颜色的 jch  rgb 值
"""
import numpy as np
colors =  np.array(
[[342,10,10,44,22,32],
[342,10,20,53,15,35],
[342,10,30,60,3,37],
[351,10,10,45,22,30],
[351,10,20,54,14,31],
[351,10,30,62,0,32],
[0,10,10,45,22,27],
[0,10,20,55,14,27],
[9,10,10,46,22,25],
[9,10,20,56,14,23],
[18,10,10,46,22,23],
[18,10,20,56,14,18],
[27,10,10,45,23,20],
[27,10,20,56,15,10],
[27,10,30,65,3,2],
[36,10,10,44,24,16],
[45,10,10,43,25,13],
[54,10,10,41,26,10],
[63,10,10,38,27,7],
[72,10,10,36,28,7],
[81,10,10,33,29,9],
[90,10,10,30,30,12],
[99,10,10,27,30,15],
[108,10,10,25,31,18],
[117,10,10,22,31,21],
[117,10,20,6,35,2],
[126,10,10,20,31,23],
[135,10,10,19,32,24],
[144,10,10,17,32,25],
[153,10,10,16,32,27],
[162,10,10,15,32,28],
[171,10,10,14,32,30],
[180,10,10,12,32,32],
[189,10,10,11,32,34],
[198,10,10,10,32,36],
[207,10,10,10,32,37],
[216,10,10,10,31,39],
[225,10,10,12,31,40],
[234,10,10,15,30,42],
[243,10,10,18,30,42],
[252,10,10,22,29,43],
[252,10,20,11,29,54],
[261,10,10,27,27,43],
[261,10,20,24,26,54],
[261,10,30,22,23,65],
[261,10,40,23,19,75],
[261,10,50,25,14,84],
[261,10,60,28,5,92],
[270,10,10,31,26,43],
[270,10,20,33,23,53],
[270,10,30,35,20,62],
[270,10,40,37,15,70],
[270,10,50,41,6,79],
[279,10,10,34,25,42],
[279,10,20,38,21,51],
[279,10,30,42,17,58],
[279,10,40,46,9,66],
[288,10,10,36,24,41],
[288,10,20,41,20,49],
[288,10,30,46,14,56],
[288,10,40,51,4,63],
[297,10,10,38,24,40],
[297,10,20,44,19,47],
[297,10,30,49,12,53],
[306,10,10,39,23,39],
[306,10,20,46,18,45],
[306,10,30,51,11,51],
[315,10,10,41,23,38],
[315,10,20,48,17,43],
[315,10,30,54,9,49],
[324,10,10,42,22,36],
[324,10,20,50,16,40],
[324,10,30,56,7,45],
[333,10,10,43,22,34],
[333,10,20,51,15,38],
[333,10,30,59,4,41],
[342,20,10,65,44,50],
[342,20,20,76,37,51],
[342,20,30,85,30,52],
[342,20,40,95,16,54],
[351,20,10,66,44,48],
[351,20,20,77,37,47],
[351,20,30,87,29,46],
[351,20,40,98,14,46],
[0,20,10,66,44,46],
[0,20,20,78,37,43],
[0,20,30,88,29,40],
[0,20,40,99,14,38],
[9,20,10,66,44,44],
[9,20,20,78,37,39],
[9,20,30,88,30,34],
[9,20,40,99,16,29],
[18,20,10,66,44,42],
[18,20,20,78,38,34],
[18,20,30,88,31,26],
[18,20,40,98,19,18],
[27,20,10,65,45,39],
[27,20,20,77,39,29],
[27,20,30,87,33,17],
[36,20,10,64,45,37],
[36,20,20,75,41,23],
[36,20,30,84,36,1],
[45,20,10,63,46,35],
[45,20,20,72,43,18],
[54,20,10,61,47,33],
[54,20,20,69,45,13],
[63,20,10,58,48,32],
[63,20,20,65,46,7],
[72,20,10,56,49,32],
[72,20,20,62,48,2],
[81,20,10,54,50,32],
[81,20,20,58,50,0],
[90,20,10,51,50,34],
[90,20,20,53,51,4],
[99,20,10,48,51,36],
[99,20,20,47,53,12],
[108,20,10,46,52,38],
[108,20,20,41,54,19],
[117,20,10,43,52,40],
[117,20,20,34,55,26],
[117,20,30,21,57,7],
[126,20,10,41,52,42],
[126,20,20,28,56,32],
[126,20,30,3,58,22],
[135,20,10,39,53,44],
[135,20,20,21,56,38],
[144,20,10,38,53,46],
[144,20,20,17,56,41],
[153,20,10,37,53,47],
[153,20,20,13,56,44],
[162,20,10,36,53,48],
[162,20,20,7,57,47],
[171,20,10,35,53,50],
[171,20,20,0,56,51],
[180,20,10,34,53,52],
[189,20,10,34,53,54],
[198,20,10,33,53,56],
[207,20,10,33,52,57],
[216,20,10,34,52,59],
[225,20,10,35,52,60],
[225,20,20,4,54,72],
[234,20,10,37,51,62],
[234,20,20,15,53,74],
[243,20,10,40,50,63],
[243,20,20,25,51,75],
[252,20,10,43,49,63],
[252,20,20,34,50,76],
[252,20,30,17,50,89],
[261,20,10,47,48,64],
[261,20,20,44,47,76],
[261,20,30,41,45,88],
[261,20,40,38,43,100],
[261,20,50,36,40,112],
[261,20,60,37,36,122],
[261,20,70,38,30,132],
[261,20,80,41,22,141],
[261,20,90,44,8,151],
[270,20,10,51,47,63],
[270,20,20,52,45,75],
[270,20,30,54,42,85],
[270,20,40,56,38,96],
[270,20,50,58,33,106],
[270,20,60,61,27,115],
[270,20,70,65,18,124],
[279,20,10,54,46,62],
[279,20,20,57,43,72],
[279,20,30,61,40,81],
[279,20,40,66,34,91],
[279,20,50,71,28,100],
[279,20,60,76,18,108],
[288,20,10,56,46,61],
[288,20,20,62,42,70],
[288,20,30,66,38,77],
[288,20,40,73,31,87],
[288,20,50,78,23,95],
[288,20,60,84,9,103],
[297,20,10,58,45,60],
[297,20,20,65,41,67],
[297,20,30,71,36,74],
[297,20,40,78,28,83],
[297,20,50,84,18,90],
[306,20,10,60,45,58],
[306,20,20,67,40,65],
[306,20,30,74,35,71],
[306,20,40,82,26,78],
[306,20,50,89,13,85],
[315,20,10,62,44,56],
[315,20,20,70,39,61],
[315,20,30,78,33,66],
[315,20,40,87,22,72],
[315,20,50,95,3,77],
[324,20,10,64,44,54],
[324,20,20,73,38,57],
[324,20,30,81,32,61],
[324,20,40,91,20,66],
[333,20,10,64,44,52],
[333,20,20,74,38,54],
[333,20,30,83,31,57],
[333,20,40,93,18,60],
[342,30,10,91,66,70],
[342,30,20,104,59,69],
[342,30,30,116,51,67],
[342,30,40,128,40,67],
[342,30,50,139,23,66],
[351,30,10,91,66,68],
[351,30,20,106,59,64],
[351,30,30,117,51,61],
[351,30,40,130,40,58],
[351,30,50,141,23,55],
[0,30,10,92,66,66],
[0,30,20,106,59,60],
[0,30,30,118,52,54],
[0,30,40,130,41,48],
[0,30,50,141,25,43],
[9,30,10,92,66,64],
[9,30,20,106,60,55],
[9,30,30,118,53,48],
[9,30,40,129,43,39],
[9,30,50,140,29,30],
[18,30,10,91,67,62],
[18,30,20,105,61,52],
[18,30,30,117,54,41],
[18,30,40,128,45,30],
[18,30,50,137,34,17],
[27,30,10,91,67,59],
[27,30,20,103,62,47],
[27,30,30,114,56,32],
[27,30,40,123,50,14],
[36,30,10,89,68,57],
[36,30,20,101,64,42],
[36,30,30,110,59,25],
[45,30,10,88,69,55],
[45,30,20,98,66,38],
[45,30,30,105,63,17],
[54,30,10,85,70,54],
[54,30,20,94,68,35],
[54,30,30,100,65,8],
[63,30,10,82,71,52],
[63,30,20,90,70,31],
[72,30,10,80,72,52],
[72,30,20,85,71,30],
[81,30,10,77,73,52],
[81,30,20,81,73,29],
[90,30,10,74,74,53],
[90,30,20,76,74,29],
[99,30,10,71,74,54],
[99,30,20,70,76,32],
[108,30,10,69,75,56],
[108,30,20,64,77,37],
[108,30,30,59,79,11],
[117,30,10,65,76,60],
[117,30,20,56,79,44],
[117,30,30,45,81,27],
[126,30,10,62,76,63],
[126,30,20,49,80,51],
[126,30,30,32,83,38],
[135,30,10,60,76,65],
[135,30,20,41,80,58],
[135,30,30,6,84,51],
[144,30,10,58,77,67],
[144,30,20,36,81,62],
[153,30,10,57,77,69],
[153,30,20,32,81,66],
[162,30,10,56,77,71],
[162,30,20,27,81,69],
[171,30,10,55,77,73],
[171,30,20,23,81,74],
[180,30,10,54,77,75],
[180,30,20,17,81,79],
[189,30,10,53,77,77],
[189,30,20,13,81,83],
[198,30,10,53,76,80],
[198,30,20,13,80,88],
[207,30,10,53,76,82],
[207,30,20,14,80,92],
[216,30,10,54,76,83],
[216,30,20,20,79,95],
[225,30,10,55,75,85],
[225,30,20,29,78,98],
[234,30,10,58,75,86],
[234,30,20,38,76,100],
[243,30,10,61,74,87],
[243,30,20,47,75,101],
[243,30,30,24,75,114],
[252,30,10,65,73,88],
[252,30,20,56,73,102],
[252,30,30,42,73,115],
[252,30,40,21,73,127],
[261,30,10,70,71,88],
[261,30,20,66,70,102],
[261,30,30,62,69,115],
[261,30,40,58,67,127],
[261,30,50,54,65,139],
[261,30,60,51,62,151],
[261,30,70,50,58,163],
[261,30,80,50,53,175],
[261,30,90,51,47,185],
[261,30,100,53,41,194],
[261,30,110,56,31,205],
[261,30,120,59,14,215],
[270,30,10,74,70,88],
[270,30,20,74,68,101],
[270,30,30,76,65,112],
[270,30,40,77,62,123],
[270,30,50,79,58,135],
[270,30,60,81,54,145],
[270,30,70,84,48,156],
[270,30,80,88,40,166],
[270,30,90,91,31,175],
[270,30,100,95,16,184],
[279,30,10,77,69,87],
[279,30,20,81,66,99],
[279,30,30,85,62,109],
[279,30,40,89,58,119],
[279,30,50,94,52,129],
[279,30,60,98,46,138],
[279,30,70,103,38,147],
[279,30,80,108,26,156],
[279,30,90,113,4,165],
[288,30,10,80,68,86],
[288,30,20,86,64,96],
[288,30,30,91,60,105],
[288,30,40,97,55,114],
[288,30,50,103,48,123],
[288,30,60,109,40,132],
[288,30,70,115,29,140],
[288,30,80,121,8,148],
[297,30,10,83,68,84],
[297,30,20,90,63,92],
[297,30,30,97,58,100],
[297,30,40,105,51,109],
[297,30,50,111,44,117],
[297,30,60,118,33,125],
[297,30,70,125,15,133],
[306,30,10,85,67,81],
[306,30,20,94,62,89],
[306,30,30,102,56,96],
[306,30,40,111,48,103],
[306,30,50,118,39,110],
[306,30,60,127,24,117],
[315,30,10,87,67,78],
[315,30,20,98,61,84],
[315,30,30,107,54,89],
[315,30,40,117,45,94],
[315,30,50,126,34,99],
[315,30,60,135,14,105],
[324,30,10,88,66,75],
[324,30,20,101,60,78],
[324,30,30,112,52,81],
[324,30,40,122,43,85],
[324,30,50,132,29,88],
[333,30,10,90,66,73],
[333,30,20,103,59,74],
[333,30,30,114,52,75],
[333,30,40,126,41,76],
[333,30,50,136,26,78],
[342,40,10,115,91,95],
[342,40,20,129,85,92],
[342,40,30,142,78,90],
[342,40,40,155,69,89],
[342,40,50,166,59,88],
[342,40,60,177,45,87],
[342,40,70,188,23,86],
[351,40,10,115,91,93],
[351,40,20,130,85,88],
[351,40,30,144,78,84],
[351,40,40,156,69,81],
[351,40,50,168,59,77],
[351,40,60,179,45,74],
[351,40,70,190,21,71],
[0,40,10,116,91,90],
[0,40,20,131,85,83],
[0,40,30,145,78,77],
[0,40,40,157,70,70],
[0,40,50,168,60,64],
[0,40,60,179,48,58],
[0,40,70,190,26,52],
[9,40,10,116,91,89],
[9,40,20,132,85,80],
[9,40,30,145,78,71],
[9,40,40,157,70,61],
[9,40,50,168,62,53],
[9,40,60,178,50,43],
[9,40,70,188,34,33],
[18,40,10,116,92,86],
[18,40,20,132,86,74],
[18,40,30,144,80,63],
[18,40,40,156,73,50],
[18,40,50,166,65,36],
[18,40,60,175,56,18],
[27,40,10,116,92,83],
[27,40,20,130,87,69],
[27,40,30,142,82,55],
[27,40,40,152,76,38],
[27,40,50,160,71,15],
[36,40,10,115,93,80],
[36,40,20,128,88,64],
[36,40,30,138,84,47],
[36,40,40,146,80,27],
[45,40,10,114,93,78],
[45,40,20,126,90,59],
[45,40,30,134,87,40],
[45,40,40,140,84,14],
[54,40,10,111,95,76],
[54,40,20,122,92,54],
[54,40,30,129,90,33],
[63,40,10,108,96,74],
[63,40,20,117,94,51],
[63,40,30,123,93,26],
[72,40,10,105,97,73],
[72,40,20,112,96,49],
[72,40,30,116,95,21],
[81,40,10,103,98,73],
[81,40,20,107,98,48],
[81,40,30,110,98,17],
[90,40,10,98,99,75],
[90,40,20,102,100,48],
[90,40,30,103,100,17],
[99,40,10,96,100,76],
[99,40,20,95,101,52],
[99,40,30,94,103,23],
[108,40,10,93,100,78],
[108,40,20,89,103,56],
[108,40,30,84,105,32],
[117,40,10,89,101,82],
[117,40,20,79,104,65],
[117,40,30,69,107,46],
[117,40,40,58,110,19],
[126,40,10,86,101,85],
[126,40,20,73,105,72],
[126,40,30,56,109,57],
[126,40,40,34,112,41],
[135,40,10,83,102,89],
[135,40,20,64,106,80],
[135,40,30,36,110,72],
[144,40,10,81,102,91],
[144,40,20,59,107,85],
[144,40,30,24,111,80],
[153,40,10,80,102,93],
[153,40,20,56,107,89],
[153,40,30,5,111,86],
[162,40,10,79,102,95],
[162,40,20,53,107,93],
[171,40,10,78,102,97],
[171,40,20,49,107,98],
[180,40,10,77,102,100],
[180,40,20,47,107,103],
[189,40,10,76,102,102],
[189,40,20,46,106,107],
[198,40,10,77,102,104],
[198,40,20,46,106,112],
[207,40,10,77,101,106],
[207,40,20,48,105,116],
[216,40,10,79,101,108],
[216,40,20,53,104,119],
[225,40,10,81,100,109],
[225,40,20,60,103,122],
[225,40,30,24,105,134],
[234,40,10,84,99,110],
[234,40,20,66,101,123],
[234,40,30,42,103,136],
[243,40,10,87,98,111],
[243,40,20,74,100,124],
[243,40,30,58,100,137],
[243,40,40,28,101,151],
[252,40,10,91,97,111],
[252,40,20,82,98,125],
[252,40,30,71,98,138],
[252,40,40,55,98,152],
[252,40,50,32,98,165],
[261,40,10,94,96,112],
[261,40,20,91,95,125],
[261,40,30,87,94,138],
[261,40,40,83,93,151],
[261,40,50,77,91,164],
[261,40,60,72,90,177],
[261,40,70,68,87,189],
[261,40,80,64,84,202],
[261,40,90,62,80,215],
[261,40,100,61,74,229],
[261,40,110,62,70,238],
[261,40,120,63,63,250],
[261,40,130,65,55,255],
[270,40,10,98,95,112],
[270,40,20,98,93,124],
[270,40,30,99,91,136],
[270,40,40,100,88,148],
[270,40,50,100,86,160],
[270,40,60,102,82,172],
[270,40,70,103,78,183],
[270,40,80,106,73,193],
[270,40,90,109,67,204],
[270,40,100,113,60,216],
[270,40,110,116,52,224],
[270,40,120,120,42,234],
[270,40,130,124,23,244],
[279,40,10,101,94,111],
[279,40,20,104,91,122],
[279,40,30,108,89,133],
[279,40,40,112,85,143],
[279,40,50,116,81,154],
[279,40,60,120,76,164],
[279,40,70,125,70,174],
[279,40,80,130,63,183],
[279,40,90,135,55,193],
[279,40,100,140,43,203],
[279,40,110,144,30,211],
[288,40,10,104,94,109],
[288,40,20,109,90,120],
[288,40,30,115,86,129],
[288,40,40,120,82,138],
[288,40,50,126,77,148],
[288,40,60,132,71,157],
[288,40,70,138,64,166],
[288,40,80,144,55,175],
[288,40,90,150,44,184],
[288,40,100,156,26,193],
[297,40,10,107,93,107],
[297,40,20,114,89,116],
[297,40,30,122,84,124],
[297,40,40,129,79,132],
[297,40,50,136,73,140],
[297,40,60,143,66,148],
[297,40,70,150,57,156],
[297,40,80,158,44,165],
[297,40,90,165,26,173],
[306,40,10,109,92,105],
[306,40,20,119,87,112],
[306,40,30,128,82,119],
[306,40,40,136,76,125],
[306,40,50,144,69,132],
[306,40,60,152,61,139],
[306,40,70,160,50,145],
[306,40,80,168,35,152],
[315,40,10,111,92,102],
[315,40,20,122,87,107],
[315,40,30,133,80,112],
[315,40,40,143,73,117],
[315,40,50,152,65,122],
[315,40,60,161,55,127],
[315,40,70,170,42,132],
[315,40,80,179,20,137],
[324,40,10,113,92,99],
[324,40,20,125,86,101],
[324,40,30,138,79,104],
[324,40,40,149,71,106],
[324,40,50,158,63,109],
[324,40,60,169,50,112],
[324,40,70,178,34,115],
[333,40,10,114,91,97],
[333,40,20,128,85,97],
[333,40,30,141,78,97],
[333,40,40,153,70,97],
[333,40,50,163,61,98],
[333,40,60,173,48,99],
[333,40,70,184,28,100],
[342,50,10,139,118,120],
[342,50,20,155,112,117],
[342,50,30,169,105,115],
[342,50,40,183,97,112],
[342,50,50,195,88,110],
[342,50,60,208,76,109],
[342,50,70,218,64,108],
[342,50,80,230,45,106],
[351,50,10,139,118,119],
[351,50,20,156,112,114],
[351,50,30,171,105,109],
[351,50,40,184,97,104],
[351,50,50,197,88,100],
[351,50,60,210,76,96],
[351,50,70,220,64,93],
[351,50,80,232,45,90],
[0,50,10,140,118,117],
[0,50,20,157,112,109],
[0,50,30,172,105,102],
[0,50,40,185,97,95],
[0,50,50,198,88,87],
[0,50,60,211,77,81],
[0,50,70,221,65,75],
[0,50,80,232,47,68],
[0,50,90,244,8,61],
[9,50,10,140,118,115],
[9,50,20,157,112,105],
[9,50,30,172,105,95],
[9,50,40,186,98,85],
[9,50,50,198,89,75],
[9,50,60,210,79,64],
[9,50,70,220,68,54],
[9,50,80,231,53,42],
[9,50,90,240,32,30],
[18,50,10,141,118,112],
[18,50,20,157,112,99],
[18,50,30,172,106,86],
[18,50,40,185,100,73],
[18,50,50,196,92,57],
[18,50,60,207,84,40],
[18,50,70,215,77,18],
[27,50,10,141,118,109],
[27,50,20,156,113,95],
[27,50,30,170,108,79],
[27,50,40,182,102,61],
[27,50,50,191,97,42],
[27,50,60,199,92,15],
[36,50,10,140,119,106],
[36,50,20,154,115,89],
[36,50,30,166,110,70],
[36,50,40,176,106,50],
[36,50,50,184,102,25],
[45,50,10,139,119,104],
[45,50,20,152,116,85],
[45,50,30,163,113,63],
[45,50,40,171,109,39],
[54,50,10,137,120,101],
[54,50,20,148,118,79],
[54,50,30,157,115,55],
[54,50,40,164,113,27],
[63,50,10,134,121,100],
[63,50,20,143,120,75],
[63,50,30,151,118,48],
[63,50,40,156,117,13],
[72,50,10,131,123,98],
[72,50,20,138,122,73],
[72,50,30,144,121,43],
[81,50,10,129,124,98],
[81,50,20,133,124,72],
[81,50,30,137,124,41],
[90,50,10,126,124,99],
[90,50,20,128,126,72],
[90,50,30,130,126,42],
[99,50,10,122,125,100],
[99,50,20,121,127,76],
[99,50,30,120,129,48],
[108,50,10,119,126,103],
[108,50,20,115,129,81],
[108,50,30,110,131,56],
[108,50,40,106,133,23],
[117,50,10,114,127,106],
[117,50,20,106,130,89],
[117,50,30,96,134,69],
[117,50,40,86,136,47],
[117,50,50,74,139,10],
[126,50,10,111,128,110],
[126,50,20,98,132,96],
[126,50,30,84,135,81],
[126,50,40,66,139,65],
[126,50,50,41,142,48],
[135,50,10,107,128,113],
[135,50,20,90,133,104],
[135,50,30,69,137,95],
[135,50,40,34,140,86],
[144,50,10,105,128,116],
[144,50,20,85,133,110],
[144,50,30,59,137,104],
[153,50,10,104,128,118],
[153,50,20,82,133,114],
[153,50,30,52,137,110],
[162,50,10,103,128,120],
[162,50,20,79,133,118],
[162,50,30,47,137,116],
[171,50,10,102,128,122],
[171,50,20,77,133,122],
[171,50,30,42,137,122],
[180,50,10,102,128,125],
[180,50,20,75,133,128],
[180,50,30,34,137,130],
[189,50,10,101,128,128],
[189,50,20,75,132,132],
[189,50,30,27,137,137],
[198,50,10,102,128,130],
[198,50,20,75,132,137],
[198,50,30,26,136,145],
[207,50,10,103,127,131],
[207,50,20,77,131,141],
[207,50,30,32,135,150],
[216,50,10,105,127,133],
[216,50,20,81,130,144],
[216,50,30,45,133,156],
[225,50,10,107,126,134],
[225,50,20,87,129,147],
[225,50,30,59,131,159],
[234,50,10,110,125,135],
[234,50,20,93,127,148],
[234,50,30,72,129,161],
[234,50,40,35,131,175],
[243,50,10,113,124,136],
[243,50,20,101,126,149],
[243,50,30,85,127,163],
[243,50,40,65,128,177],
[243,50,50,28,129,191],
[252,50,10,117,123,136],
[252,50,20,108,124,150],
[252,50,30,98,124,164],
[252,50,40,85,124,178],
[252,50,50,67,125,192],
[252,50,60,38,125,206],
[261,50,10,120,122,136],
[261,50,20,116,122,149],
[261,50,30,112,121,164],
[261,50,40,108,119,177],
[261,50,50,103,118,190],
[261,50,60,97,117,204],
[261,50,70,90,115,218],
[261,50,80,83,113,232],
[261,50,90,77,109,247],
[261,50,100,72,106,255],
[270,50,10,123,121,136],
[270,50,20,123,120,148],
[270,50,30,124,117,162],
[270,50,40,124,115,175],
[270,50,50,124,112,186],
[270,50,60,125,109,199],
[270,50,70,126,106,212],
[270,50,80,127,102,224],
[270,50,90,129,98,235],
[270,50,100,131,93,247],
[270,50,110,135,86,255],
[279,50,10,126,121,135],
[279,50,20,129,118,147],
[279,50,30,132,115,159],
[279,50,40,136,111,171],
[279,50,50,140,108,181],
[279,50,60,144,104,192],
[279,50,70,149,99,202],
[279,50,80,153,93,212],
[279,50,90,158,87,222],
[279,50,100,163,80,233],
[279,50,110,168,71,243],
[279,50,120,173,59,254],
[279,50,130,179,44,255],
[288,50,10,128,120,133],
[288,50,20,134,117,144],
[288,50,30,140,113,155],
[288,50,40,146,109,165],
[288,50,50,151,104,175],
[288,50,60,157,99,185],
[288,50,70,163,93,194],
[288,50,80,169,87,203],
[288,50,90,175,79,212],
[288,50,100,181,70,221],
[288,50,110,187,57,231],
[288,50,120,194,40,240],
[288,50,130,200,1,249],
[297,50,10,131,119,131],
[297,50,20,139,115,140],
[297,50,30,148,110,149],
[297,50,40,156,105,158],
[297,50,50,163,100,166],
[297,50,60,170,93,174],
[297,50,70,178,86,182],
[297,50,80,185,78,190],
[297,50,90,192,67,199],
[297,50,100,200,54,207],
[297,50,110,208,32,216],
[306,50,10,133,119,129],
[306,50,20,143,114,136],
[306,50,30,154,109,143],
[306,50,40,164,102,150],
[306,50,50,172,96,157],
[306,50,60,181,89,164],
[306,50,70,189,80,170],
[306,50,80,198,70,177],
[306,50,90,206,57,184],
[306,50,100,215,36,191],
[315,50,10,135,119,127],
[315,50,20,147,113,132],
[315,50,30,159,107,137],
[315,50,40,171,100,142],
[315,50,50,180,93,146],
[315,50,60,190,84,151],
[315,50,70,200,74,156],
[315,50,80,209,62,161],
[315,50,90,218,44,166],
[315,50,100,227,7,171],
[324,50,10,137,118,124],
[324,50,20,151,112,126],
[324,50,30,164,106,128],
[324,50,40,177,98,130],
[324,50,50,188,90,132],
[324,50,60,199,80,135],
[324,50,70,210,68,137],
[324,50,80,220,53,140],
[324,50,90,230,28,142],
[333,50,10,138,118,122],
[333,50,20,153,112,121],
[333,50,30,167,105,121],
[333,50,40,180,97,121],
[333,50,50,192,89,121],
[333,50,60,204,77,122],
[333,50,70,214,66,123],
[333,50,80,225,48,124],
[333,50,90,235,17,125],
[342,60,10,164,144,146],
[342,60,20,180,138,143],
[342,60,30,196,132,140],
[342,60,40,208,125,137],
[342,60,50,222,117,135],
[342,60,60,235,107,132],
[342,60,70,247,97,131],
[342,60,80,255,82,128],
[342,60,90,255,65,127],
[351,60,10,165,144,144],
[351,60,20,182,138,139],
[351,60,30,198,132,134],
[351,60,40,211,125,129],
[351,60,50,225,117,124],
[351,60,60,238,107,119],
[351,60,70,249,97,116],
[351,60,80,255,82,111],
[351,60,90,255,64,108],
[0,60,10,166,144,143],
[0,60,20,183,138,135],
[0,60,30,199,132,127],
[0,60,40,212,125,121],
[0,60,50,226,117,113],
[0,60,60,239,107,106],
[0,60,70,251,97,99],
[0,60,80,255,84,92],
[0,60,90,255,68,85],
[9,60,10,167,144,140],
[9,60,20,184,138,130],
[9,60,30,199,132,121],
[9,60,40,213,125,111],
[9,60,50,227,117,100],
[9,60,60,239,109,89],
[9,60,70,250,100,77],
[9,60,80,255,88,65],
[9,60,90,255,75,51],
[18,60,10,167,144,138],
[18,60,20,184,139,124],
[18,60,30,199,133,112],
[18,60,40,212,127,99],
[18,60,50,225,120,83],
[18,60,60,236,113,67],
[18,60,70,247,105,47],
[18,60,80,255,97,20],
[27,60,10,168,144,134],
[27,60,20,183,140,120],
[27,60,30,197,134,104],
[27,60,40,210,129,88],
[27,60,50,221,124,69],
[27,60,60,230,118,47],
[27,60,70,238,113,10],
[36,60,10,167,145,131],
[36,60,20,181,141,114],
[36,60,30,194,137,95],
[36,60,40,205,132,75],
[36,60,50,214,128,53],
[36,60,60,221,125,21],
[45,60,10,166,146,129],
[45,60,20,179,142,110],
[45,60,30,190,139,88],
[45,60,40,199,136,65],
[45,60,50,207,133,36],
[54,60,10,163,147,126],
[54,60,20,174,144,104],
[54,60,30,184,142,80],
[54,60,40,192,140,54],
[54,60,50,198,138,16],
[63,60,10,160,148,124],
[63,60,20,170,146,100],
[63,60,30,178,145,74],
[63,60,40,184,143,44],
[72,60,10,157,149,122],
[72,60,20,164,149,97],
[72,60,30,170,148,69],
[72,60,40,175,147,35],
[81,60,10,155,150,122],
[81,60,20,159,150,96],
[81,60,30,163,151,67],
[81,60,40,166,151,29],
[90,60,10,152,151,122],
[90,60,20,154,152,97],
[90,60,30,156,153,67],
[90,60,40,158,153,29],
[99,60,10,148,152,124],
[99,60,20,148,154,99],
[99,60,30,147,155,72],
[99,60,40,146,157,36],
[108,60,10,145,152,126],
[108,60,20,141,155,103],
[108,60,30,137,158,80],
[108,60,40,132,160,50],
[117,60,10,140,154,129],
[117,60,20,131,157,112],
[117,60,30,122,160,93],
[117,60,40,112,163,70],
[117,60,50,101,166,43],
[126,60,10,135,154,134],
[126,60,20,123,158,119],
[126,60,30,109,162,104],
[126,60,40,93,166,88],
[126,60,50,74,169,72],
[126,60,60,46,172,52],
[135,60,10,132,155,138],
[135,60,20,114,160,128],
[135,60,30,95,164,118],
[135,60,40,69,168,109],
[135,60,50,20,171,100],
[144,60,10,130,155,141],
[144,60,20,108,160,134],
[144,60,30,85,164,128],
[144,60,40,49,168,123],
[153,60,10,129,155,143],
[153,60,20,105,160,138],
[153,60,30,79,165,135],
[153,60,40,35,168,131],
[162,60,10,128,155,146],
[162,60,20,102,160,143],
[162,60,30,74,165,141],
[162,60,40,11,169,139],
[171,60,10,127,155,148],
[171,60,20,100,160,147],
[171,60,30,70,165,147],
[180,60,10,126,155,151],
[180,60,20,99,160,153],
[180,60,30,63,164,155],
[189,60,10,126,155,153],
[189,60,20,98,160,158],
[189,60,30,61,164,163],
[198,60,10,127,154,155],
[198,60,20,100,159,163],
[198,60,30,60,163,170],
[207,60,10,128,154,157],
[207,60,20,103,158,166],
[207,60,30,64,162,176],
[216,60,10,131,153,159],
[216,60,20,108,157,169],
[216,60,30,75,160,182],
[225,60,10,133,152,160],
[225,60,20,114,155,172],
[225,60,30,87,158,185],
[225,60,40,46,160,198],
[234,60,10,136,151,160],
[234,60,20,120,154,173],
[234,60,30,99,156,188],
[234,60,40,71,158,201],
[243,60,10,139,150,161],
[243,60,20,128,152,174],
[243,60,30,112,153,189],
[243,60,40,95,154,204],
[243,60,50,69,155,218],
[252,60,10,142,149,161],
[252,60,20,134,150,175],
[252,60,30,124,150,190],
[252,60,40,112,151,205],
[252,60,50,96,151,219],
[252,60,60,72,152,235],
[252,60,70,23,152,251],
[261,60,10,146,148,161],
[261,60,20,142,148,175],
[261,60,30,138,147,190],
[261,60,40,133,146,203],
[261,60,50,128,145,217],
[261,60,60,121,143,233],
[261,60,70,114,142,249],
[270,60,10,149,148,161],
[270,60,20,149,146,174],
[270,60,30,148,144,188],
[270,60,40,148,142,200],
[270,60,50,148,140,213],
[270,60,60,148,137,228],
[270,60,70,149,134,242],
[270,60,80,150,129,255],
[279,60,10,151,147,160],
[279,60,20,154,144,172],
[279,60,30,157,142,185],
[279,60,40,161,138,197],
[279,60,50,164,135,209],
[279,60,60,169,131,220],
[279,60,70,173,126,232],
[279,60,80,179,121,244],
[279,60,90,183,115,254],
[288,60,10,154,146,159],
[288,60,20,159,143,170],
[288,60,30,165,139,181],
[288,60,40,170,136,191],
[288,60,50,176,131,202],
[288,60,60,182,127,212],
[288,60,70,188,121,223],
[288,60,80,194,115,233],
[288,60,90,200,108,243],
[288,60,100,207,100,254],
[297,60,10,157,145,157],
[297,60,20,165,142,165],
[297,60,30,174,137,175],
[297,60,40,182,132,183],
[297,60,50,190,127,192],
[297,60,60,198,121,200],
[297,60,70,206,114,209],
[297,60,80,214,107,217],
[297,60,90,221,98,226],
[297,60,100,230,86,236],
[297,60,110,239,71,245],
[297,60,120,247,52,254],
[306,60,10,159,145,155],
[306,60,20,169,141,162],
[306,60,30,180,135,169],
[306,60,40,189,130,175],
[306,60,50,199,124,182],
[306,60,60,208,117,189],
[306,60,70,218,108,196],
[306,60,80,227,100,203],
[306,60,90,235,90,210],
[306,60,100,245,75,218],
[306,60,110,254,57,225],
[306,60,120,255,29,232],
[315,60,10,161,145,153],
[315,60,20,173,140,157],
[315,60,30,185,134,162],
[315,60,40,196,128,166],
[315,60,50,207,121,171],
[315,60,60,218,113,176],
[315,60,70,229,104,181],
[315,60,80,239,93,186],
[315,60,90,249,81,191],
[315,60,100,255,63,196],
[315,60,110,255,41,201],
[324,60,10,163,144,150],
[324,60,20,176,139,151],
[324,60,30,191,132,153],
[324,60,40,203,126,155],
[324,60,50,214,119,156],
[324,60,60,226,110,159],
[324,60,70,238,100,161],
[324,60,80,249,88,164],
[324,60,90,255,73,166],
[324,60,100,255,47,170],
[324,60,110,255,4,172],
[333,60,10,163,144,148],
[333,60,20,178,139,147],
[333,60,30,194,132,146],
[333,60,40,206,126,146],
[333,60,50,219,118,146],
[333,60,60,231,109,146],
[333,60,70,243,98,147],
[333,60,80,255,84,147],
[333,60,90,255,68,148],
[333,60,100,255,40,150],
[342,70,10,190,171,172],
[342,70,20,206,165,169],
[342,70,30,222,159,166],
[342,70,40,238,151,162],
[342,70,50,252,144,159],
[342,70,60,255,133,156],
[342,70,70,255,123,154],
[342,70,80,255,110,151],
[351,70,10,191,171,171],
[351,70,20,208,165,165],
[351,70,30,224,158,160],
[351,70,40,240,151,154],
[351,70,50,254,143,149],
[351,70,60,255,133,143],
[351,70,70,255,123,138],
[351,70,80,255,110,133],
[0,70,10,192,171,169],
[0,70,20,209,165,161],
[0,70,30,226,158,153],
[0,70,40,241,151,146],
[0,70,50,255,143,138],
[0,70,60,255,134,130],
[0,70,70,255,124,122],
[9,70,10,193,171,167],
[9,70,20,211,165,156],
[9,70,30,226,159,146],
[9,70,40,243,152,135],
[9,70,50,255,145,124],
[9,70,60,255,136,112],
[9,70,70,255,127,100],
[9,70,80,255,116,87],
[18,70,10,193,171,164],
[18,70,20,211,165,151],
[18,70,30,227,160,137],
[18,70,40,242,153,123],
[18,70,50,254,147,109],
[18,70,60,255,140,91],
[18,70,70,255,132,73],
[18,70,80,255,124,49],
[27,70,10,193,171,161],
[27,70,20,210,166,145],
[27,70,30,225,161,128],
[27,70,40,239,156,112],
[27,70,50,250,150,95],
[27,70,60,255,145,72],
[27,70,70,255,139,44],
[36,70,10,193,171,158],
[36,70,20,208,167,139],
[36,70,30,222,163,120],
[36,70,40,233,159,101],
[36,70,50,243,155,79],
[36,70,60,253,151,52],
[45,70,10,192,172,155],
[45,70,20,206,169,134],
[45,70,30,218,166,113],
[45,70,40,227,163,91],
[45,70,50,236,160,66],
[45,70,60,243,157,28],
[54,70,10,190,173,151],
[54,70,20,202,171,128],
[54,70,30,212,169,105],
[54,70,40,220,166,80],
[54,70,50,227,164,51],
[63,70,10,187,174,149],
[63,70,20,197,173,125],
[63,70,30,205,171,99],
[63,70,40,212,170,72],
[63,70,50,217,169,35],
[72,70,10,184,175,148],
[72,70,20,190,175,121],
[72,70,30,197,175,94],
[72,70,40,202,174,65],
[72,70,50,206,174,15],
[81,70,10,181,176,147],
[81,70,20,186,177,120],
[81,70,30,190,177,93],
[81,70,40,193,177,61],
[90,70,10,179,177,147],
[90,70,20,181,178,121],
[90,70,30,183,179,93],
[90,70,40,185,180,61],
[99,70,10,175,178,148],
[99,70,20,174,180,123],
[99,70,30,174,182,98],
[99,70,40,173,183,67],
[99,70,50,172,185,11],
[108,70,10,172,179,150],
[108,70,20,168,182,127],
[108,70,30,164,184,104],
[108,70,40,160,186,77],
[108,70,50,156,188,39],
[117,70,10,166,180,155],
[117,70,20,157,184,136],
[117,70,30,149,187,117],
[117,70,40,140,190,96],
[117,70,50,129,193,70],
[117,70,60,118,196,37],
[126,70,10,161,181,159],
[126,70,20,149,185,143],
[126,70,30,136,189,129],
[126,70,40,121,193,113],
[126,70,50,103,196,96],
[126,70,60,81,200,77],
[126,70,70,51,202,55],
[135,70,10,157,182,163],
[135,70,20,140,186,153],
[135,70,30,122,191,143],
[135,70,40,99,195,133],
[135,70,50,67,199,122],
[144,70,10,155,182,167],
[144,70,20,135,187,160],
[144,70,30,113,191,153],
[144,70,40,84,196,148],
[144,70,50,25,200,142],
[153,70,10,154,182,169],
[153,70,20,132,187,164],
[153,70,30,108,191,160],
[153,70,40,74,196,156],
[162,70,10,153,182,172],
[162,70,20,130,187,169],
[162,70,30,103,192,166],
[162,70,40,64,196,164],
[171,70,10,152,182,173],
[171,70,20,128,187,173],
[171,70,30,100,191,172],
[171,70,40,54,196,172],
[180,70,10,151,182,176],
[180,70,20,126,187,178],
[180,70,30,97,191,180],
[180,70,40,41,196,182],
[189,70,10,152,181,179],
[189,70,20,125,186,183],
[189,70,30,95,191,187],
[189,70,40,34,195,192],
[198,70,10,153,181,182],
[198,70,20,126,186,188],
[198,70,30,95,190,195],
[198,70,40,29,194,202],
[207,70,10,154,180,183],
[207,70,20,128,185,192],
[207,70,30,98,189,201],
[207,70,40,40,192,211],
[216,70,10,157,179,185],
[216,70,20,133,183,196],
[216,70,30,104,187,207],
[216,70,40,60,190,219],
[225,70,10,160,179,186],
[225,70,20,138,182,198],
[225,70,30,114,185,211],
[225,70,40,79,188,225],
[234,70,10,163,178,186],
[234,70,20,146,180,200],
[234,70,30,126,183,214],
[234,70,40,99,185,228],
[234,70,50,53,187,244],
[243,70,10,166,177,187],
[243,70,20,153,178,201],
[243,70,30,139,180,216],
[243,70,40,120,181,231],
[243,70,50,94,183,248],
[252,70,10,169,176,187],
[252,70,20,160,177,201],
[252,70,30,149,177,216],
[252,70,40,137,178,232],
[252,70,50,120,178,249],
[261,70,10,172,175,187],
[261,70,20,168,174,201],
[261,70,30,163,174,217],
[261,70,40,158,173,232],
[261,70,50,152,171,249],
[270,70,10,175,174,186],
[270,70,20,174,173,201],
[270,70,30,174,171,215],
[270,70,40,173,169,229],
[270,70,50,173,166,245],
[270,70,60,173,163,255],
[279,70,10,177,174,186],
[279,70,20,180,171,199],
[279,70,30,183,168,211],
[279,70,40,186,165,224],
[279,70,50,190,161,238],
[279,70,60,194,157,251],
[288,70,10,180,173,185],
[288,70,20,185,170,196],
[288,70,30,190,166,207],
[288,70,40,196,163,219],
[288,70,50,202,158,231],
[288,70,60,208,153,242],
[288,70,70,215,148,253],
[297,70,10,183,172,182],
[297,70,20,192,168,191],
[297,70,30,200,164,200],
[297,70,40,209,159,209],
[297,70,50,218,153,219],
[297,70,60,226,147,227],
[297,70,70,235,140,237],
[297,70,80,244,133,246],
[297,70,90,253,124,255],
[306,70,10,185,172,180],
[306,70,20,196,167,187],
[306,70,30,207,162,194],
[306,70,40,218,156,201],
[306,70,50,228,150,209],
[306,70,60,237,144,215],
[306,70,70,248,136,223],
[306,70,80,255,126,231],
[306,70,90,255,116,238],
[306,70,100,255,104,246],
[306,70,110,255,88,255],
[315,70,10,186,172,178],
[315,70,20,199,166,182],
[315,70,30,213,160,187],
[315,70,40,225,154,192],
[315,70,50,236,147,196],
[315,70,60,248,140,202],
[315,70,70,255,131,206],
[315,70,80,255,120,212],
[315,70,90,255,107,218],
[315,70,100,255,91,224],
[324,70,10,188,171,176],
[324,70,20,202,166,177],
[324,70,30,218,159,179],
[324,70,40,232,152,180],
[324,70,50,244,145,182],
[324,70,60,255,136,184],
[324,70,70,255,126,186],
[324,70,80,255,114,189],
[324,70,90,255,100,192],
[333,70,10,189,171,174],
[333,70,20,204,166,173],
[333,70,30,220,159,172],
[333,70,40,235,152,172],
[333,70,50,248,144,171],
[333,70,60,255,135,171],
[333,70,70,255,124,171],
[333,70,80,255,111,172],
[342,80,10,215,198,200],
[342,80,20,234,192,195],
[342,80,30,251,185,192],
[342,80,40,255,177,188],
[342,80,50,255,169,184],
[351,80,10,215,198,198],
[351,80,20,236,192,191],
[351,80,30,253,185,185],
[351,80,40,255,177,179],
[351,80,50,255,169,173],
[0,80,10,216,198,196],
[0,80,20,237,192,187],
[0,80,30,254,185,179],
[0,80,40,255,177,170],
[0,80,50,255,169,161],
[9,80,10,217,198,194],
[9,80,20,239,191,182],
[9,80,30,255,185,171],
[9,80,40,255,178,158],
[9,80,50,255,170,146],
[18,80,10,218,198,192],
[18,80,20,239,192,176],
[18,80,30,255,186,161],
[18,80,40,255,179,146],
[18,80,50,255,173,131],
[27,80,10,219,198,189],
[27,80,20,239,193,170],
[27,80,30,254,188,153],
[27,80,40,255,182,135],
[27,80,50,255,177,116],
[27,80,60,255,171,95],
[36,80,10,219,198,184],
[36,80,20,236,194,164],
[36,80,30,250,190,145],
[36,80,40,255,186,123],
[36,80,50,255,182,102],
[36,80,60,255,178,77],
[36,80,70,255,174,43],
[45,80,10,218,199,181],
[45,80,20,233,196,159],
[45,80,30,246,192,138],
[45,80,40,255,189,114],
[45,80,50,255,186,90],
[45,80,60,255,183,60],
[54,80,10,216,200,177],
[54,80,20,228,198,154],
[54,80,30,239,196,130],
[54,80,40,248,193,104],
[54,80,50,255,191,77],
[54,80,60,255,189,40],
[63,80,10,214,201,174],
[63,80,20,223,200,150],
[63,80,30,232,199,124],
[63,80,40,239,197,97],
[63,80,50,246,196,66],
[63,80,60,251,195,10],
[72,80,10,211,202,172],
[72,80,20,217,202,146],
[72,80,30,223,202,119],
[72,80,40,228,202,90],
[72,80,50,233,201,54],
[81,80,10,208,203,172],
[81,80,20,213,204,145],
[81,80,30,217,204,117],
[81,80,40,220,205,86],
[81,80,50,223,205,48],
[90,80,10,206,204,171],
[90,80,20,208,205,145],
[90,80,30,210,206,117],
[90,80,40,212,207,86],
[90,80,50,214,208,47],
[99,80,10,203,205,172],
[99,80,20,202,207,147],
[99,80,30,201,209,120],
[99,80,40,200,211,92],
[99,80,50,199,212,53],
[108,80,10,199,206,174],
[108,80,20,196,208,151],
[108,80,30,192,211,126],
[108,80,40,188,213,100],
[108,80,50,184,216,68],
[117,80,10,192,207,179],
[117,80,20,183,211,159],
[117,80,30,175,215,139],
[117,80,40,166,218,117],
[117,80,50,156,221,94],
[117,80,60,146,224,63],
[126,80,10,187,208,183],
[126,80,20,174,213,168],
[126,80,30,160,217,151],
[126,80,40,146,221,136],
[126,80,50,129,224,118],
[126,80,60,110,228,99],
[126,80,70,85,231,79],
[126,80,80,47,234,54],
[135,80,10,183,209,189],
[135,80,20,166,214,178],
[135,80,30,145,219,166],
[135,80,40,124,223,156],
[135,80,50,98,227,145],
[135,80,60,53,231,134],
[144,80,10,180,209,192],
[144,80,20,160,214,185],
[144,80,30,135,220,178],
[144,80,40,107,224,171],
[144,80,50,67,228,166],
[153,80,10,179,209,195],
[153,80,20,157,214,190],
[153,80,30,130,220,185],
[153,80,40,100,224,181],
[153,80,50,47,228,177],
[162,80,10,178,209,198],
[162,80,20,155,215,194],
[162,80,30,126,220,192],
[162,80,40,92,224,189],
[162,80,50,20,228,187],
[171,80,10,177,209,200],
[171,80,20,152,215,198],
[171,80,30,124,219,198],
[171,80,40,85,224,197],
[180,80,10,177,209,203],
[180,80,20,151,214,204],
[180,80,30,121,219,205],
[180,80,40,75,224,208],
[189,80,10,178,208,206],
[189,80,20,151,214,209],
[189,80,30,117,219,214],
[189,80,40,69,223,218],
[198,80,10,179,208,208],
[198,80,20,151,213,214],
[198,80,30,118,218,221],
[198,80,40,66,222,228],
[207,80,10,181,207,210],
[207,80,20,153,212,219],
[207,80,30,120,217,228],
[207,80,40,69,221,238],
[216,80,10,184,206,211],
[216,80,20,158,211,223],
[216,80,30,128,215,235],
[216,80,40,80,219,249],
[225,80,10,187,205,212],
[225,80,20,164,209,225],
[225,80,30,137,213,239],
[225,80,40,96,216,255],
[234,80,10,190,204,212],
[234,80,20,171,207,228],
[234,80,30,149,210,243],
[234,80,40,117,213,255],
[243,80,10,193,203,213],
[243,80,20,179,205,229],
[243,80,30,162,207,245],
[252,80,10,196,203,213],
[252,80,20,186,204,229],
[252,80,30,173,204,247],
[261,80,10,199,202,213],
[261,80,20,194,201,229],
[261,80,30,188,201,246],
[270,80,10,202,201,212],
[270,80,20,201,200,227],
[270,80,30,200,197,244],
[270,80,40,199,195,255],
[279,80,10,204,201,211],
[279,80,20,206,198,226],
[279,80,30,209,195,240],
[279,80,40,212,192,255],
[288,80,10,205,200,210],
[288,80,20,211,197,223],
[288,80,30,216,193,236],
[288,80,40,223,189,249],
[288,80,50,229,184,255],
[297,80,10,208,199,208],
[297,80,20,219,195,217],
[297,80,30,227,191,226],
[297,80,40,238,184,237],
[297,80,50,248,179,247],
[297,80,60,255,172,255],
[306,80,10,210,199,206],
[306,80,20,222,194,213],
[306,80,30,234,189,221],
[306,80,40,247,182,229],
[306,80,50,255,176,236],
[306,80,60,255,169,244],
[306,80,70,255,160,253],
[315,80,10,211,199,204],
[315,80,20,226,193,209],
[315,80,30,241,187,213],
[315,80,40,255,180,218],
[315,80,50,255,173,223],
[315,80,60,255,164,228],
[315,80,70,255,155,234],
[324,80,10,213,199,203],
[324,80,20,229,193,203],
[324,80,30,246,186,205],
[324,80,40,255,178,206],
[324,80,50,255,171,208],
[324,80,60,255,160,210],
[333,80,10,214,198,201],
[333,80,20,232,192,199],
[333,80,30,249,185,198],
[333,80,40,255,177,198],
[333,80,50,255,169,197],
[333,80,60,255,159,197],
[342,90,10,242,226,227],
[342,90,20,255,219,222],
[342,90,30,255,211,217],
[351,90,10,242,226,226],
[351,90,20,255,218,218],
[351,90,30,255,211,210],
[0,90,10,244,226,223],
[0,90,20,255,218,213],
[0,90,30,255,211,203],
[9,90,10,245,225,221],
[9,90,20,255,218,207],
[9,90,30,255,211,194],
[18,90,10,245,225,219],
[18,90,20,255,218,201],
[18,90,30,255,212,185],
[27,90,10,247,225,215],
[27,90,20,255,219,194],
[27,90,30,255,214,175],
[36,90,10,247,226,210],
[36,90,20,255,221,187],
[36,90,30,255,217,167],
[45,90,10,246,226,206],
[45,90,20,255,223,182],
[45,90,30,255,220,159],
[45,90,40,255,217,136],
[54,90,10,244,227,202],
[54,90,20,255,225,176],
[54,90,30,255,223,152],
[54,90,40,255,221,126],
[63,90,10,241,229,199],
[63,90,20,251,228,172],
[63,90,30,255,226,146],
[63,90,40,255,225,119],
[63,90,50,255,224,90],
[63,90,60,255,222,52],
[72,90,10,238,230,197],
[72,90,20,245,230,169],
[72,90,30,251,230,141],
[72,90,40,255,230,112],
[72,90,50,255,229,80],
[72,90,60,255,229,29],
[81,90,10,236,231,196],
[81,90,20,240,232,168],
[81,90,30,244,232,140],
[81,90,40,248,232,109],
[81,90,50,251,233,76],
[81,90,60,254,233,12],
[90,90,10,233,231,196],
[90,90,20,236,233,168],
[90,90,30,238,234,140],
[90,90,40,240,235,108],
[90,90,50,242,236,74],
[99,90,10,230,232,197],
[99,90,20,230,235,169],
[99,90,30,229,237,142],
[99,90,40,228,238,111],
[99,90,50,227,240,78],
[99,90,60,226,241,13],
[108,90,10,227,233,198],
[108,90,20,224,236,172],
[108,90,30,220,239,146],
[108,90,40,216,242,118],
[108,90,50,212,244,87],
[108,90,60,208,246,41],
[117,90,10,219,235,203],
[117,90,20,210,239,182],
[117,90,30,201,243,159],
[117,90,40,192,246,136],
[117,90,50,182,250,111],
[117,90,60,172,252,83],
[117,90,70,161,255,44],
[126,90,10,213,236,209],
[126,90,20,200,241,191],
[126,90,30,183,246,172],
[126,90,40,169,250,156],
[126,90,50,152,254,137],
[126,90,60,134,255,120],
[126,90,70,111,255,99],
[126,90,80,80,255,75],
[126,90,90,16,255,41],
[135,90,10,208,237,214],
[135,90,20,190,242,202],
[135,90,30,167,248,188],
[135,90,40,145,252,177],
[135,90,50,118,255,166],
[135,90,60,84,255,155],
[144,90,10,206,237,218],
[144,90,20,184,243,210],
[144,90,30,156,249,202],
[144,90,40,126,254,195],
[144,90,50,89,255,189],
[153,90,10,204,237,222],
[153,90,20,180,243,216],
[153,90,30,150,249,210],
[153,90,40,117,254,205],
[153,90,50,72,255,201],
[162,90,10,203,237,224],
[162,90,20,178,243,221],
[162,90,30,146,249,217],
[162,90,40,108,254,214],
[162,90,50,51,255,212],
[171,90,10,203,237,227],
[171,90,20,176,243,225],
[171,90,30,142,249,224],
[171,90,40,100,254,223],
[171,90,50,15,255,223],
[180,90,10,203,237,229],
[180,90,20,174,243,230],
[180,90,30,139,249,232],
[180,90,40,90,254,233],
[189,90,10,203,236,233],
[189,90,20,174,242,237],
[189,90,30,136,248,241],
[189,90,40,79,253,246],
[198,90,10,205,236,235],
[198,90,20,174,242,242],
[198,90,30,135,247,249],
[207,90,10,207,235,237],
[207,90,20,176,241,248],
[216,90,10,210,234,239],
[216,90,20,180,239,253],
[225,90,10,214,233,239],
[225,90,20,186,238,255],
[234,90,10,216,232,240],
[234,90,20,192,236,255],
[243,90,10,220,231,240],
[252,90,10,223,230,240],
[261,90,10,226,229,240],
[270,90,10,229,228,239],
[270,90,20,227,227,255],
[279,90,10,231,228,239],
[279,90,20,233,225,255],
[288,90,10,232,228,238],
[288,90,20,238,224,253],
[297,90,10,236,227,235],
[297,90,20,248,222,246],
[297,90,30,255,216,255],
[306,90,10,237,227,233],
[306,90,20,252,221,241],
[306,90,30,255,215,249],
[315,90,10,239,226,232],
[315,90,20,255,220,236],
[315,90,30,255,213,241],
[324,90,10,240,226,230],
[324,90,20,255,219,231],
[324,90,30,255,212,232],
[333,90,10,241,226,228],
[333,90,20,255,219,226],
[333,90,30,255,211,225]],dtype='uint16')
