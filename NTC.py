import PCF8591 as ADC 
import RPi.GPIO as GPIO
import time 
import math
makerobo_DO=17	
GPIO.setmode( GPIO.BCM)		

def makerobo_setup():
    ADC.setup(0x48)	
    GPIO.setup(makerobo_DO, GPIO.IN)	
def makerobo_Print(x):
    if x== 1:	#温度合适	
        print (' ')
        print ('***********') 
        print ('* Better~ *') 
        print ('***********') 
        print ('')
if x==0: #温度过高
        print (' ' )
        print ('************') 
        print ('* Too Hot! *') 
        print ('************') 
        print ('')
# 循环函数
def makerob0_loop():
    makerobo_status=1	# 状态值	
    makerobo_tmp=1	#当前值	
    while True:
          makerobo_analogVal= ADC.read(0)	             #读取AINO上的模拟值	
          makerobo_Vr=5*float(makerobo_analogVal) / 255   #转换到0~5v
          makerobo_Rt = 10000 * makerobo_Vr / (5 - makerobo_Vr)
          makerobo_temp = 1/(((math.log(makerobo_Rt / 10000)) / 3950) +
(1 / (273.15+25)))
          makerobo_temp= makerobo_temp-273.15
          print ('temperature = ', makerobo_temp, 'c')
          makerobo_tmp = GPIO.input(makerobo_DO) #读取温度传感器数字端口
          if makerobo_tmp != makerobo_status:	     # 判断状态值是否发生改变	
              makerobo_Print(makerobo_tmp)	         #打印出温度传感器提示信息	
              makerobo_status = makerobo_tmp  #将当前状态值设置为比较状态值，避免重复打印
          time.sleep(0.2)	# 延时 200ms	
# 程序入口
          if __name__  == '__main__':
            try:
               makerobo_setup()	#初始化程序	
               makerobo_loop()	  #循环函数	
            except KeyboardInterrupt:
                pass
