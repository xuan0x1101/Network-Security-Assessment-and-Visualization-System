from datetime import datetime
import time
from influxdb import InfluxDBClient
import pytz

utc_tz = pytz.timezone('Etc/GMT-8')
current_time_utc = datetime.now().astimezone(utc_tz)

def send_to_influxdb(data):
    
    start_time = time.time()

    # 创建 InfluxDBClient 对象，连接到 InfluxDB
    client = InfluxDBClient(host='192.168.10.100', port=8086, username='influxUser01', password='123456', database='Test', timeout=10)

    for info,type in data:
        data_points = []

        for row in info:
            time.sleep(0.01)
            # 构造数据点
            # dt = datetime.datetime.strptime(row[6], "%d/%m/%Y %H:%M")
            current_time_utc = datetime.now().astimezone(utc_tz)

            data_point = {
                "measurement": type,
                "tags": {
                    "Flow_ID": row[0]
                },
                "fields": {
                    "Source_IP": row[1],
                    "Source_Port": row[2],
                    "Destination_IP": row[3],
                    "Destination_Port": row[4],
                    "Protocol": row[5],
                    "Flow_Duration": float(row[7]),
                    "Total_Fwd_Packets": float(row[8]),
                    "Total_Backward_Packets": float(row[9]),
                    "Total_Length_of_Fwd_Packets": float(row[10]),
                    "Total_Length_of_Bwd_Packets": float(row[11]),
                    "Fwd_Packet_Length_Max": row[12],
                    "Fwd_Packet_Length_Min": row[13],
                    "Fwd_Packet_Length_Mean": float(row[14]),
                    "Fwd_Packet_Length_Std": row[15],
                    "Bwd_Packet_Length_Max": row[16],
                    "Bwd_Packet_Length_Min": row[17],
                    "Bwd_Packet_Length_Mean": row[18],
                    "Bwd_Packet_Length_Std": row[19],
                    "Flow_Bytes/s": float(row[20]),
                    "Flow_Packets/s": (row[21]),
                    "Flow_IAT_Mean": float(row[22]),
                    "Flow_IAT_Std": row[23],
                    "Flow_IAT_Max": row[24],
                    "Flow_IAT_Min": row[25],
                    "Fwd_IAT_Total": row[26],
                    "Fwd_IAT_Mean": float(row[27]),
                    "Fwd_IAT_Std": row[28],
                    "Fwd_IAT_Max": row[29],
                    "Fwd_IAT_Min": row[30],
                    "Bwd_IAT_Total": row[31],
                    "Bwd_IAT_Mean": row[32],
                    "Bwd_IAT_Std": row[33],
                    "Bwd_IAT_Max": row[34],
                    "Bwd_IAT_Min": row[35],
                    "Fwd_PSH_Flags": row[36],
                    "Bwd_PSH_Flags": row[37],
                    "Fwd_URG_Flags": row[38],
                    "Bwd_URG_Flags": row[39],
                    "Fwd_Header_Length": row[40],
                    "Bwd_Header_Length": row[41],
                    "Fwd_Packets/s": float(row[42]),
                    "Bwd_Packets/s": row[43],
                    "Min_Packet_Length": row[44],
                    "Max_Packet_Length": row[45],
                    "Packet_Length_Mean": float(row[46]),
                    "Packet_Length_Std": row[47],
                    "Packet_Length_Variance": row[48],
                    "FIN_Flag_Count": row[49],
                    "SYN_Flag_Count": row[50],
                    "RST_Flag_Count": row[51],
                    "PSH_Flag_Count": row[52],
                    "ACK_Flag_Count": row[53],
                    "URG_Flag_Count": row[54],
                    "CWE_Flag_Count": row[55],
                    "ECE_Flag_Count": row[56],
                    "Down/Up_Ratio": row[57],
                    "Average_Packet_Size": row[58],
                    "Avg_Fwd_Segment_Size": row[59],
                    "Avg_Bwd_Segment_Size": row[60],
                    "Fwd_Header_Length": row[61],
                    "Fwd_Avg_Bytes/Bulk": row[62],
                    "Fwd_Avg_Packets_Bulk": row[63],
                    "Fwd_Avg_Bulk_Rate": row[64],
                    "Bwd_Avg_Bytes_Bulk": row[65],
                    "Bwd_Avg_Packets_Bulk": row[66],
                    "Bwd_Avg_Bulk_Rate": row[67],
                    "Subflow_Fwd_Packets": row[68],
                    "Subflow_Fwd_Bytes": row[69],
                    "Subflow_Bwd_Packets": row[70],
                    "Subflow_Bwd_Bytes": row[71],
                    "Init_Win_bytes_forward": row[72],
                    "Init_Win_bytes_backward": row[73],
                    "act_data_pkt_fwd": row[74],
                    "min_seg_size_forward": row[75],
                    "Active_Mean": float(row[76]),
                    "Active_Std": row[77],
                    "Active_Max": row[78],
                    "Active_Min": row[79],
                    "Idle_Mean": float(row[80]),
                    "Idle_Std": row[81],
                    "Idle_Max": row[82],
                    "Idle_Min": row[83],
                    "Label": row[84],
                },
                # "time": dt.astimezone(utc_tz).isoformat()  # 时间戳
                "time": current_time_utc.isoformat()  # 时间戳

            }
            
            data_points.append(data_point)

        # 写入 InfluxDB
        client.write_points(data_points, protocol='json', batch_size=5000)

    # 关闭连接
    client.close()

    end_time = time.time()
    print("代码执行时间：", end_time - start_time, "秒")
