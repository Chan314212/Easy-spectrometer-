import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image
# 导入库


def dis(a, b):
    return math.sqrt((a[1] - b[1]) * (a[1] - b[1]) + (a[2] - b[2]) * (a[2] - b[2]) + (a[0] - b[0]) * (a[0] - b[0]))
# 计算两个点的空间距离


def mean(ima):
    return np.mean(ima, axis=0)
# 计算第一维的均值

 
# tar_l = [252, 247, 83]
# tar_r = [252, 247, 83]
# 定义一个回调函数，用于获取鼠标点击位置的颜色


def get_color_l(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 获取点击位置的像素值 (B, G, R)
        b, g, r = image_tar[y, x]
        print(f"l颜色值 (BGR): ({r}, {g}, {b})")
        global tar_l
        global left_tar
        tar_l = [r, g, b]
        left_tar = x
        cv2.destroyAllWindows()


def get_color_r(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 获取点击位置的像素值 (B, G, R)
        b, g, r = image_tar[y, x]
        print(f"r颜色值 (BGR): ({r}, {g}, {b})")
        global tar_r
        global right_tar
        tar_r = [r, g, b]
        right_tar = x
        cv2.destroyAllWindows()


def get_loc(len_cal, tar):
    dis_a = np.zeros((len_cal))
    for i in range(0, len_cal):
        dis_a[i] = dis(tar, mean_cal[i])
    print(dis_a[1])
    idx_min = np.argmin(dis_a)
    return idx_min


path = "0.png"
path_tar = "123.jpg"
path_cal = "image_calibration.png"
left_tar, right_tar = 0, 0
left = 0
right = 1

wave_delta = 1

scaling_factor = (right - left) / wave_delta

tar_l = [252, 247, 83]
tar_r = [252, 247, 83]

image_calibration = cv2.imread(path_cal)
image_calibration = cv2.cvtColor(image_calibration, cv2.COLOR_BGR2RGB)
image_tar = cv2.imread(path_tar)
# image_tar = cv2.cvtColor(image_tar, cv2.COLOR_BGR2RGB)
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

ori = np.array(image)
array_calibration = np.array(image_calibration)
array_tar = np.array(image_tar)
print(ori.shape)

# h = ori.shape[0]
# len = ori.shape[1]

# h_cal = array_calibration.shape[0]
len_cal = array_calibration.shape[1]
len_tar = array_tar.shape[1]

# print(h_cal, len_cal)

# dis_a = np.zeros((len_tar))

mean_ori = mean(ori)
mean_cal = mean(array_calibration)

print(mean_ori.shape)
print(mean_cal.shape)

cv2.imshow('Image', image_tar)
# 设置鼠标点击事件的回调函数
cv2.setMouseCallback('Image', get_color_l)
cv2.waitKey(0)
cv2.destroyAllWindows()
left = get_loc(len_cal, tar_l)
print("left", left, left_tar)

cv2.imshow('Image', image_tar)
cv2.setMouseCallback('Image', get_color_r)
cv2.waitKey(0)
cv2.destroyAllWindows()
right = get_loc(len_cal, tar_r)
print("right", right, right_tar)

delta = abs(left - right)
print("delta", delta)
delta_tar = abs(left_tar - right_tar)
print("delta_tar", delta_tar)

scaling_factor = delta / delta_tar
print("len_cal", len_cal)

array_wl_cal = np.linspace(350, 700, len_cal)
print(len(array_wl_cal))

wl_left = array_wl_cal[left]
wl_right = array_wl_cal[right]

array_wl_tar = np.linspace(wl_left, wl_right, delta_tar + 1)

interval = array_wl_tar[1] - array_wl_tar[0]
len_exp_left = left_tar - 1
len_exp_right = len_tar - right_tar
prepend_elements = np.arange(array_wl_tar[0] - len_exp_left * interval, array_wl_tar[0], interval)
append_elements = np.arange(array_wl_tar[-1] + interval, array_wl_tar[-1] + (len_exp_right + 1) * interval, interval)
print(len(prepend_elements))
extended_array = np.concatenate((prepend_elements, array_wl_tar, append_elements))
print("extended_array", len(extended_array))
print(array_tar.shape)

tar_gray = Image.open(path_tar).convert("L")
array_gray = np.array(tar_gray)
column_sums = np.sum(array_gray, axis=0)
print(column_sums.shape)
result = np.vstack((column_sums, extended_array))
print(result.shape)

# plt.plot(result[1], result[0])
# plt.show()

idx_left = np.argmax(result[1] > 350)
idx_right = np.argmin(result[1] < 700)
print("idx",idx_left,idx_right)
result = np.vstack((result[1][idx_left:idx_right], result[0][idx_left:idx_right]))
plt.plot(result[0], result[1])
plt.show()
# ta = [1,2,3]
# tb = [1,2,6]
# print(dis(ta,tb))
# print(dis_a.shape)
# print(0^2)

# for i in range(0,len_tar):
#     dis_a[i] = dis(tar, mean_cal[i])

# print(dis_a[1])
# idx_min = np.argmin(dis_a)
# print(idx_min)

# plt.subplot(311)
# plt.plot(dis_a)

# # print(mean(ori)[1])
# plt.subplot(312)
# plt.imshow(image)

# plt.subplot(313)
# plt.imshow(image_tar)
# plt.show()

# print(scaling_factor)

# ori_pro = ori_mean / scaling_factor

# len_pro = len / scaling_factor

# print(len_pro)


# # 等待用户点击，按任意键退出
# cv2.waitKey(0)
# cv2.destroyAllWindows()
