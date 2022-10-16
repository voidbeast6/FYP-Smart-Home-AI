import PCF8591 as ADC
import RPi.GPIO as GPIO 
import time 
import math
makerobo_DO=17
GPIO.setmode(GPIO.BCM)
def  makerobo_setup():
     ADC.setup(0x48)	
     GPIO.setup(makerobo_DO, GPIO.IN)
def  makerobo_Print(x):
    if x == 1:
        print ('')
        print ('	************************')	
        print ('	* makerobo Not raining *')	
        print ('	************************')	
        print ('')
    if x == 0:	
        print ('')
        print ('	**********************')	
        print ('    * makerobo Raining!! *') 
        print ('    **********************') 
        print ('')
def makerobo_loop():
    makerobo_status=1	# 雨滴探测模块状态	
while True:
      print(ADC.read(0))	#打印出AINO的模拟量数值	
      makerobo_tmp=GPIO.input(makerobo_DO)#读取数字I/O口电平，读取雨滴探测模块的DO端口
      if makerobo_tmp!=makerobostatus:#状态发生改变
         makerobo_Print(makerobo_tmp)	# 打印出雨滴探测模块的检测信息	
         makerobo_status=makerobo_tmp#对状态值重新赋值
      time.sleep(0.2)	#延时200ms	


if __name__  == '__main__':
     try:	
        makerobo_setup()
        makerobo_loop()
     except KeyboardInterrupt:
      pass