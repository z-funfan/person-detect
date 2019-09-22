# 简单的行人检测

该项目已暂定为基于opencv与yolo的行人检测程序，用于学习Python基本语法以及YOLO库的使用。

## 概述

### 什么是YOLO
    目标检测算法主要分为两类：

一类是基于Region Proposal（候选区域）的算法，如R-CNN系算法（R-CNN，Fast R-CNN, Faster R-CNN），它们是two-stage（两步法）的，需要先使用Selective search或者CNN网络（RPN）产生Region Proposal，然后再在Region Proposal上做分类与回归。

而另一类是Yolo，SSD这类one-stage算法（一步法），其仅仅使用一个CNN网络直接预测不同目标的类别与位置。第一类方法是准确度高一些，但是速度慢，而第二类算法是速度快，但是准确性要低一些。

YOLO是一种比SSD还要快的目标检测网络模型，OpenCV在3.3.1的版本中开始正式支持Darknet网络框架并且支持YOLO1与YOLO2以及YOLO Tiny网络模型的导入与使用。后面测试，OpenCV3.4.2也支持YOLO3 。

YOLO特色：
1. 检测范围广：YOLO9000 覆盖了9000种常用分类，YOLOv2 覆盖了PASCAL VOC和COCO数据集分类。
2. 检测准确率高
3. 检测速度快：普通CPU就能运行低配版（Tiny YOLO），可使用GPU运行高配版 (YOLOv2)。

### 安装YOLO库
当前YOLOv3有两个主流版本的脚本辅助集合：（
[AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)
 & 
 [pjreddie/darknet](https://github.com/pjreddie/darknet)）, 本例中将使用到的是pj版。

下载安装与训练权重，该权重是微软的COCO数据集（common objects in context），能够识别80钟常见物体。

## 主要代码逻辑

## 运行测试

## 参考：
1. https://github.com/arunponnusamy/object-detection-opencv
2. https://github.com/pascal1129/yolo_person_detect
3. https://zhuanlan.zhihu.com/p/32097670