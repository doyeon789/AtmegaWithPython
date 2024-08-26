import serial
import os

# 콘솔 화면 클리어.
os.system('cls')

# ATmega128 설정에 맞게 시리얼 포트를 구성.
ser = serial.Serial(
    port='COM3',    # 사용 중인 COM 포트로 변경.
    baudrate=9600,  # ATmega128 설정에 맞는 보레이트(baud rate)를 설정.
    timeout=1
)

def read_value():
    try:
        # 한 줄을 읽고 디코딩합니다.
        line = ser.readline().decode('ascii').strip()  # 한 줄을 읽고 ASCII로 디코딩.
        if line:  # 라인이 비어 있지 않은지 확인.
            return int(line)  # 라인을 정수로 변환.
        return None
    except ValueError:
        print("ValueError: 정수로 변환할 수 없습니다.")
        return None
    except UnicodeDecodeError:
        print(f"UnicodeDecodeError: 수신된 원시 데이터: {line}")
        return None

try:
    while True:
        value = read_value()
        if value is not None:
            print(f"수신된 값: {value}")
        else:
            print("오류: 정수가 아닌 데이터 또는 빈 줄이 수신되었습니다.")
finally:
    ser.close()
