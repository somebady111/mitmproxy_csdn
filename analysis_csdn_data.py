import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

# 准备数据
title,comments = np.loadtxt('article_list.csv',unpack=True,delimiter=',', usecols=(2,6),dtype='U, U')
print(title,comments,sep='\n')

# 绘制图像