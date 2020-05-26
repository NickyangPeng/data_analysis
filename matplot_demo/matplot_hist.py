# -*- coding: utf-8 -*-
# @Author      : Nick
# @File        : matplot_hist.py  v1.0
# @Desc        :《matplotlib 直方图绘图步骤》
# @Contact     : PENGYANG19@163.COM
# @CreateTime  : 2020-05-26 10:44:39
# Copyright (C) 2020 Nick Ltd. All rights reserved.
from matplotlib import pyplot as plt

"""
使用场景:
    用于表示分布情况
    通过直方图还可以观察和估计哪些数据比较集中，异常或者孤立的数据分布在何处
"""
# 案例: 展现不同电影的时长分布状态
# 创建一个figure >>> figsize:指定图的长宽, dpi:图像的清晰度, 返回fig对象
plt.figure(figsize=(20, 8), dpi=100)

# 准备时长数据
time = [131, 98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130,
        124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 136, 126, 134, 95, 138, 117, 111, 78, 132, 124, 113, 150, 110,
        117, 86, 95, 144, 105, 126, 130, 126, 130, 126, 116, 123, 106, 112, 138, 123, 86, 101, 99, 136, 123, 117, 119,
        105, 137, 123, 128, 125, 104, 109, 134, 125, 127, 105, 120, 107, 129, 116, 108, 132, 103, 136, 118, 102, 120,
        114, 105, 115, 132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134, 156, 106, 117, 127, 144, 139, 139, 119,
        140, 83, 110, 102, 123, 107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133, 112, 114, 122, 109,
        106, 123, 116, 131, 127, 115, 118, 112, 135, 115, 146, 137, 116, 103, 144, 83, 123, 111, 110, 111, 100, 154,
        136, 100, 118, 119, 133, 134, 106, 129, 126, 110, 111, 109, 141, 120, 117, 106, 149, 122, 122, 110, 118, 127,
        121, 114, 125, 126, 114, 140, 103, 130, 141, 117, 106, 114, 121, 114, 133, 137, 92, 121, 112, 146, 97, 137, 105,
        98, 117, 112, 81, 97, 139, 113, 134, 106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101, 110, 105, 129, 137,
        112, 120, 113, 133, 112, 83, 94, 146, 133, 101, 131, 116, 111, 84, 137, 115, 122, 106, 144, 109, 123, 116, 111,
        111, 133, 150]
"""
设置组距: gap, 每一组两个端点的差
设置组数: 在统计数据时，我们把数据按照不同的范围分成几个组，分成的组的个数称为组数
    一般设置组数会有相应公式：组数 = 极差/组距= (max-min)/gap
"""
# 定义一个间隔大小 - 组距
gap = 2
# 根据指定间隔计算出组数
bins = int((max(time) - min(time)) / gap)

# 画出直方图
plt.hist(time, bins, density=1)

# 指定刻度的范围，以及步长
plt.xticks(list(range(min(time), max(time)))[::2])
plt.title("电影时长分布状态", fontsize=24)
# 增加网格显示
plt.grid(True, linestyle='--', alpha=0.5)

plt.xlabel("电影时长大小")
plt.ylabel("电影的数据量")

# 指定保存图片边缘空白距离，并将绘制的图片保存到images目录
plt.subplots_adjust(top=0.93, bottom=0.08, right=0.97, left=0.05, hspace=0, wspace=0)
plt.margins(0, 0)
plt.savefig("../static/images/matplot_hist.png", dpi=300)

plt.show()