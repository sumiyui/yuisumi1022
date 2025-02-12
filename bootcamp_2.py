import serial
import time
import pandas as pd
   
def get_sensor_data(PORT_NAME, BAURATE, FRAME_COUNT, CSV_NAME):
       row_count = 0 #フレーム数をカウントする変数
       ser = serial.Serial(PORT_NAME, BAURATE, parity=serial.PARITY_NONE)
       time.sleep(1)
       ser.reset_input_buffer()    
       all_data_list = [] #シリアル通信で取得した値を全て入れておくリスト
       
       while True:
           if row_count > FRAME_COUNT: #指定したフレーム数分センサ値を取得
               break
           data = int(ser.readline().decode("utf-8").replace("\n", "").replace("\r", "")) #センサ値の読み込み
           print(data)
           all_data_list.append(data)
           row_count += 1
       # シリアルポートを一度閉じる
       ser.close()	
       # CSV形式にして保存
       light_df = pd.DataFrame(all_data_list)
       light_df.to_csv("./" + CSV_NAME,  index=None, header=False)
   
if __name__ == "__main__":
       PORT_NAME = "COM3"
       BAURATE = 115200
       FRAME_COUNT = 100
       CSV_NAME = "sensor_data.csv"
   
       get_sensor_data(PORT_NAME, BAURATE, FRAME_COUNT, CSV_NAME)