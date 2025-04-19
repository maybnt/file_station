import  serial
import  time
import  random
from rich.console import Console
from rich.progress import track

console = Console()
ser = serial.Serial('COM9', 115200)  # 替换为你的端口和波特率
time.sleep(2)  # 等待串口初始化（可选）


def uart_wr(rw,addr,data):
    uart_send_data = rw<<24|addr<<8|data
    bytes_to_send = uart_send_data.to_bytes(4,byteorder='big')
    # print(bytes_to_send)
    ser.write(bytes_to_send)
    time.sleep(0.1)
# for i in range(256):
#     # rdm_data = random.randint(0, 255)
#     rdm_data = i
#     uart_wr(0x00,i,rdm_data)
#     uart_wr(0x01,i,rdm_data)
#     rd_data = int.from_bytes(ser.read(1),byteorder="big")
#     if rd_data == rdm_data:
#         print("PASS",i)
#     else:
#         print("FAILD",rd_data,rdm_data,i)       
# uart_wr(0x01,0x0821,0x70)
# rd_data = int.from_bytes(ser.read(1),byteorder="big")
# print(rd_data)

i=0
c=0
with  open('source/iic_cfg_mem.txt','r',) as read_reg:
    lines = read_reg.readlines()
    for line in track(lines,description="写入中..."):
        i=i+1
        if i%3 == 1:
            addr_h=line.rstrip()
        elif i%3 == 2:
            addr = int(addr_h+line.rstrip()[2:],16)
        elif i%3 == 0:
            data = int(line.rstrip(),16)
            # print(addr,data)
            uart_wr(0x00,addr,data)
ser.close()
