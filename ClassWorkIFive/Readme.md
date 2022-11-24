#  DPCM编码
## 1.运行方式
    将处理图片放在Source文件里面
    在终端输入以下命令：
    $ python .\DPCM.py image_path bit
    iamge_path为图片放置位置，bit为量化比特

##  2.结果
### 2.1PSNR和SSIN
| bit  | PSNR  | SSIM  |
| :--: | :---: | :---: |
|  8   | 51.13 | 0.998 |
|  4   | 23.12 | 0.794 |
|  2   | 9.17  | 0.277 |
|  1   | 8.81  | 0.365 |
### 2.2图像结果
   <div>
     8-bit  &nbsp; &nbsp;
    <img src='./source/Lena.jpg' width='300'/>
    <img src='./target/construct_8_bit.jpg' width='300'/>
    <img src='./target/differ_8_bit.jpg' width='300'/>
</div>

 <div>
     4-bit  &nbsp; &nbsp;
    <img src='./source/Lena.jpg' width='300'/>
    <img src='./target/construct_4_bit.jpg' width='300'/>
    <img src='./target/differ_4_bit.jpg' width='300'/>
</div>

 <div>
     2-bit  &nbsp; &nbsp;
    <img src='./source/Lena.jpg' width='300'/>
    <img src='./target/construct_2_bit.jpg' width='300'/>
    <img src='./target/differ_2_bit.jpg' width='300'/>
</div>

 <div>
     1-bit  &nbsp; &nbsp;
    <img src='./source/Lena.jpg' width='300'/>
    <img src='./target/construct_1_bit.jpg' width='300'/>
    <img src='./target/differ_1_bit.jpg' width='300'/>
</div>


