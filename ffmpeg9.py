import cv2
import numpy
import subprocess as sp

video1="https://esv-cdn-01.yanao.ru:2225/3UUXFRBLXUHYTPKRO7G4MNJ4QUTSA6KWQRXN5NV676PZNGCXQ2IZLC2CW6GTRNOUMSZPZBXCR7YLQSJTUZE5U72TE3MAHPBRW66QHQHCJKKRVXDRWJNX7PEBAIO5KQEBI2ZCCKBCEUV2BI6FOAQTJMRTVP2XDWR7ZO2TQD3VCKW6DXNHPDPNHPBEWS5FTBZ4XJ6RHBPTNYVH7NXKFRQTTVTPGA75HX5BQTFMC4MXNPJXKWUPAPXWLT4UIYJ67YNE/2a3bb5650a8cb122cef82dcdc5f7b697"
video2="https://esv-cdn-02.yanao.ru:2227/27BYRFQRKOJI3OTNNDTKUFCHQIMCEAK75KXSJRTXDQGEOLOW5LQAZK4FRIW4UTX3YEMJKOZTHEOPYXBFBCE5T2SSA2Z775QCCQJLMS7CJKKRVXDRWJNX7PEBAIO5KQEBI2ZCCKBCEUV2BI6FOAQTJMRTVOSXPWRFWQDBJOF5DTB7JHJR6LVG3KSO2SAW4SWUVIDZFY6XEOHBFP5TM4N3EORUUF4CCJHKANUJRBA/1d05440457e26823ab84021044df59f2"
video3="https://esv-cdn-02.yanao.ru:2226/27BYRFQRKOJI3OTNNDTKUFCHQKE5PJVA5JWRIZQIO4GXCGNHGEHCDWIH6LP2BKNKK7HNREHSAHYB6GO3C5KTADVMSSX76Y4H5VXBOYHCJKKRVXDRWJNX7PEBAIO5KQEBG4OWEDZN3HCH7YACTD7U5ER4774SFRQRD72H6SWE34D6BWXVBN7NHPBEWS5FTBZ4XJ6RHBPTNYVH7NXKFRQTTVTPGA75HX5BQTFMC4MXNPJXKWUPAPXWLT4UIYJ67YNE/607dd348a8d6007b075e6c258b6e4d28"

ffmpeg_cmd="ffmpeg \
    -fflags nobuffer -flags low_delay -strict experimental\
   -i {0} \
   -fflags nobuffer -flags low_delay -strict experimental\
   -i {1} \
   -fflags nobuffer -flags low_delay -strict experimental\
   -i {2} \
    -fflags nobuffer -flags low_delay -strict experimental\
   -i {3} \
    -fflags nobuffer -flags low_delay -strict experimental\
   -i {4} \
    -fflags nobuffer -flags low_delay -strict experimental\
   -i {5} \
    -fflags nobuffer -flags low_delay -strict experimental\
   -i {6} \
    -fflags nobuffer -flags low_delay -strict experimental\
   -i {7} \
    -fflags nobuffer -flags low_delay -strict experimental\
   -i {8} \
  -filter_complex ' \
      [0:v] setpts=''(RTCTIME-RTCSTART)/(TB*1000000)'', scale=qvga [a0]; \
      [1:v] setpts=''(RTCTIME-RTCSTART)/(TB*1000000)'', scale=qvga [a1]; \
      [2:v] setpts=''(RTCTIME-RTCSTART)/(TB*1000000)'', scale=qvga [a2]; \
      [3:v] setpts=''(RTCTIME-RTCSTART)/(TB*1000000)'', scale=qvga [a3]; \
      [4:v] setpts=''(RTCTIME-RTCSTART)/(TB*1000000)'', scale=qvga [a4]; \
      [5:v] setpts=''(RTCTIME-RTCSTART)/(TB*1000000)'', scale=qvga [a5]; \
      [6:v] setpts=''(RTCTIME-RTCSTART)/(TB*1000000)'', scale=qvga [a6]; \
      [7:v] setpts=''(RTCTIME-RTCSTART)/(TB*1000000)'', scale=qvga [a7]; \
      [8:v] setpts=''(RTCTIME-RTCSTART)/(TB*1000000)'', scale=qvga [a8]; \
    [a0][a1][a2][a3][a4][a5][a6][a7][a8]xstack=inputs=9:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0|0_h0+h1|w0_h0+h1|w0+w1_h0+h1[out]' -map '[out]' -c:v libx264 -f matroska - | ffplay -".format(video1, video1, video1, video1, video1, video1, video1, video1, video1)                                             #передача потока в ffplay
pipe=sp.Popen(ffmpeg_cmd, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)

stdout, stderr=pipe.communicate()
print (stderr) #Вывод ошибок

