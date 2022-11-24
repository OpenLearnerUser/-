#  大津法和迭代法阈值分割
## 1.运行方式
    将处理图片放在source文件里面
    在终端输入以下命令：
    $ python .\Ostu.py image_path oper_type
        iamge_path为图片放置位置，oper_type方法，可选为Ostf(大津法) Iter(迭代阈值分割)

##  2.结果

### 2.1图像处理结果
    下边结果分别为原图，迭代法，大津法
   <div>
     8-bit  &nbsp; &nbsp;
    <img src='./source/Lena.jpg' width='300'/>
    <img src='./target/Iter_Lena.jpg' width='300'/>
    <img src='./target/Ostf_Lena.jpg' width='300'/>
</div>

## 3. 性能比较

下述实验中，迭代法两次灰度差的阈值取值为 1。

| 算法名称 |   图片名   | 分辨率  | 1000 次分割耗时(s) |
| :------: | :--------: | :-----: | :----------------: |
|  大津法  | Lenna.png  | 316×316 |       69.32        |
|  迭代法  | Lenna.png  | 316×316 |       32.33        |


结论：迭代法性能较好