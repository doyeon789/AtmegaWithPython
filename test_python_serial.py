import serial
import os

# 콘솔 화면 클리어.
os.system('cls')

# ATmega128에 맞게 시리얼 포트를 구성.
ser = serial.Serial(
    port='COM3',        # 사용 중인 COM 포트로 변경.
    baudrate=9600,      # ATmega128 설정에 맞는 보레이트를 설정.
    timeout=1
)

def read_value():
    try:
        line = ser.readline().decode('ascii').strip()  # 한 줄을 읽고 ASCII로 디코딩.
        if line:  # line이 비어 있지 않은지 확인.
            return line  # 문자열로 line 리턴
        return None
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        return None

try:
    while True:
        value = read_value()
        if value is not None:
            print(f"Received value: {value}")
        else:
            #별다른 동작이 없으면 아무런 동작도 하지 않
            pass
finally:
    ser.close()
