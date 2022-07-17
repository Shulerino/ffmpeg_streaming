import ffmpeg
import cv2
import numpy
import subprocess as sp

video1="https://esv-cdn-01.yanao.ru:2225/3UUXFRBLXUHYTPKRO7G4MNJ4QUTSA6KWQRXN5NV676PZNGCXQ2IZLC2CW6GTRNOUMSZPZBXCR7YLQSJTUZE5U72TE3MAHPBRW66QHQHCJKKRVXDRWJNX7PEBAIO5KQEBI2ZCCKBCEUV2BI6FOAQTJMRTVP2XDWR7ZO2TQD3VCKW6DXNHPDPNHPBEWS5FTBZ4XJ6RHBPTNYVH7NXKFRQTTVTPGA75HX5BQTFMC4MXNPJXKWUPAPXWLT4UIYJ67YNE/2a3bb5650a8cb122cef82dcdc5f7b697"
video2="https://esv-cdn-02.yanao.ru:2227/27BYRFQRKOJI3OTNNDTKUFCHQIMCEAK75KXSJRTXDQGEOLOW5LQAZK4FRIW4UTX3YEMJKOZTHEOPYXBFBCE5T2SSA2Z775QCCQJLMS7CJKKRVXDRWJNX7PEBAIO5KQEBI2ZCCKBCEUV2BI6FOAQTJMRTVOSXPWRFWQDBJOF5DTB7JHJR6LVG3KSO2SAW4SWUVIDZFY6XEOHBFP5TM4N3EORUUF4CCJHKANUJRBA/1d05440457e26823ab84021044df59f2"
video3="https://esv-cdn-02.yanao.ru:2226/27BYRFQRKOJI3OTNNDTKUFCHQKE5PJVA5JWRIZQIO4GXCGNHGEHCDWIH6LP2BKNKK7HNREHSAHYB6GO3C5KTADVMSSX76Y4H5VXBOYHCJKKRVXDRWJNX7PEBAIO5KQEBG4OWEDZN3HCH7YACTD7U5ER4774SFRQRD72H6SWE34D6BWXVBN7NHPBEWS5FTBZ4XJ6RHBPTNYVH7NXKFRQTTVTPGA75HX5BQTFMC4MXNPJXKWUPAPXWLT4UIYJ67YNE/607dd348a8d6007b075e6c258b6e4d28"

ffmpeg_cmd="ffmpeg\
   -i {0} \
   -i {1} \
   -i {2} \
   -i {3} \
   -i {4} \
   -i {5} \
   -i {6} \
   -i {7} \
   -i {8} \
  -filter_complex ' \
      [0:v] setpts=PTS-STARTPTS, scale=qvga [a0]; \
      [1:v] setpts=PTS-STARTPTS, scale=qvga [a1]; \
      [2:v] setpts=PTS-STARTPTS, scale=qvga [a2]; \
      [3:v] setpts=PTS-STARTPTS, scale=qvga [a3]; \
      [4:v] setpts=PTS-STARTPTS, scale=qvga [a4]; \
      [5:v] setpts=PTS-STARTPTS, scale=qvga [a5]; \
      [6:v] setpts=PTS-STARTPTS, scale=qvga [a6]; \
      [7:v] setpts=PTS-STARTPTS, scale=qvga [a7]; \
      [8:v] setpts=PTS-STARTPTS, scale=qvga [a8]; \
    [a0][a1][a2][a3][a4][a5][a6][a7][a8]xstack=inputs=9:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0|0_h0+h1|w0_h0+h1|w0+w1_h0+h1[out]' -map '[out]' -c:v libx264 -t '30' -f matroska - | ffplay -".format(video1, video2, video3, video1, video2, video3, video1, video2, video3)                                             #передача потока в ffplay
    #[a0][a1][a2][a3][a4][a5][a6][a7][a8]xstack=inputs=9:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0|0_h0+h1|w0_h0+h1|w0+w1_h0+h1[out]' -map '[out]' -c:v libx264 -hls_time 10 -hls_list_size 10 -start_number 1 ./hls_vlc/video_hls_vlc.m3u8".format(video1, video2, video3, video1, video2, video3, video1, video2, video3) #создание файла формата hls  для трансляции в VLC
    #[a0][a1][a2][a3][a4][a5][a6][a7][a8]xstack=inputs=9:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0|0_h0+h1|w0_h0+h1|w0+w1_h0+h1[out]' -map '[out]' -c:v libx264 -t '30' -f matroska out.mp4".format(video1, video2, video3, video1, video2, video3, video1, video2, video3)                                                 #создание выходного файла mp4
    #[a0][a1][a2][a3][a4][a5][a6][a7][a8]xstack=inputs=9:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0|0_h0+h1|w0_h0+h1|w0+w1_h0+h1[out]' -map '[out]' -f dash -remove_at_exit 1 ./dash/video_dash.mpd".format(video1, video2, video3, video1, video2, video3, video1, video2, video3)                                          #создание файла формата DASH
    #[a0][a1][a2][a3][a4][a5][a6][a7][a8]xstack=inputs=9:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0|0_h0+h1|w0_h0+h1|w0+w1_h0+h1[out]' -map '[out]' -c:v libx264 -hls_time 10 -hls_list_size 10 -start_number 1 ./hls/video_hls.m3u8".format(video1, video2, video3, video1, video2, video3, video1, video2, video3)         #создание файла формата hls
    #[a0][a1][a2][a3][a4][a5][a6][a7][a8]xstack=inputs=9:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0|0_h0+h1|w0_h0+h1|w0+w1_h0+h1[out]' -map '[out]' -c:v libx264 -t '30' -f rawvideo - ".format(video1, video2, video3, video1, video2, video3, video1, video2, video3)                                                      #создание выходного потока
pipe=sp.Popen(ffmpeg_cmd, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)

#Попытка захвата выходного потока в OpenCV (ругается на размер)
# while True:
#     raw_image=pipe.stdout.read()
#     image=numpy.frombuffer(raw_image, dtype='uint8')
#     image = image.reshape((480, 640, 3))
#     cv2.imshow("Video", image)

stdout, stderr=pipe.communicate()
print (stderr) #Вывод ошибок

