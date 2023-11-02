![1698918792621](C:\Users\ADMINI~1\AppData\Local\Temp\1698918792621.png)

导入库

![1698918816355](C:\Users\ADMINI~1\AppData\Local\Temp\1698918816355.png)

计算两个点的空间距离

![1698918848124](C:\Users\ADMINI~1\AppData\Local\Temp\1698918848124.png)

计算第一维的均值

![1698918864289](C:\Users\ADMINI~1\AppData\Local\Temp\1698918864289.png)

获取点击位置颜色值（最左边）

![1698918895630](C:\Users\ADMINI~1\AppData\Local\Temp\1698918895630.png)

获取点击位置颜色值，最右边

![1698918924228](C:\Users\ADMINI~1\AppData\Local\Temp\1698918924228.png)

将一个点与每一列的点平均值计算距离，导出为数组

![1698918973656](C:\Users\ADMINI~1\AppData\Local\Temp\1698918973656.png)

导入图片

![1698918993777](C:\Users\ADMINI~1\AppData\Local\Temp\1698918993777.png)

弹出窗口让用户点击，获取颜色，计算在校准图中的位置，计算波长，同时获取点击位置

（右侧相同操作）

![1698919099721](C:\Users\ADMINI~1\AppData\Local\Temp\1698919099721.png)

生成350-700的一个数组，长度是校准图片的长度

![1698919146200](C:\Users\ADMINI~1\AppData\Local\Temp\1698919146200.png)

获取左侧和右侧的波长、

![1698919257663](C:\Users\ADMINI~1\AppData\Local\Temp\1698919257663.png)

生成两侧波长的数组，长度是目标图片的点击位置的差值的+1

![1698919337979](C:\Users\ADMINI~1\AppData\Local\Temp\1698919337979.png)

计算波长数组的差值

![1698919380104](C:\Users\ADMINI~1\AppData\Local\Temp\1698919380104.png)

计算两侧需要补充的数量

![1698919399917](C:\Users\ADMINI~1\AppData\Local\Temp\1698919399917.png)

根据差值和数量计算前后需要补全的数组

![1698919428413](C:\Users\ADMINI~1\AppData\Local\Temp\1698919428413.png)

计算出波长的数组

![1698919456004](C:\Users\ADMINI~1\AppData\Local\Temp\1698919456004.png)

将图片转制成灰度图片，导出为数组，计算每一列的均值，形成一维数组，再加一行波长数组



![1698919531069](C:\Users\ADMINI~1\AppData\Local\Temp\1698919531069.png)

截取其中350-700的部分，显示。

