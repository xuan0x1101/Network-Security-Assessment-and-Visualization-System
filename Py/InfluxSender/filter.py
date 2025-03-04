import sys
import os

# 将父文件夹的路径添加到搜索路径中
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from IndicatorJudge import PortScan
from IndicatorJudge import DDoS
from ML.predict import predict_byRow
from sender import send_to_influxdb

def apply_filters(data_batch):

    # print('start filting...')

    
    Benign_batch = []
    DDos_batch = []
    PortScan_batch = []
    DoS_Hulk_batch = []
    DoS_GoldenEye_batch = []
    FTP_Patator_batch = []
    SSH_Patator_batch = []
    DoS_slowloris_batch = []
    DoS_Slowhttptest_batch = []

    PortScan.PortScanJudger(data_batch)
    # DDoS.DDoSJudger(data_batch)
    # predict_byRow.predict_byRow(data_batch)


    # 根据批量数据进行判断，将行数据添加到对应的数据库缓冲区中
    for row in data_batch:
        if row[84] == 'BENIGN':
            Benign_batch.append(row)
        elif row[84] == 'DDoS':
            DDos_batch.append(row)
        elif row[84] == 'PortScan':
            PortScan_batch.append(row)
        elif row[84] == 'DoS Hulk':
            DoS_Hulk_batch.append(row)
        elif row[84] == 'DoS GoldenEye':
            DoS_GoldenEye_batch.append(row)
        elif row[84] == 'FTP-Patator':
            FTP_Patator_batch.append(row)
        elif row[84] == 'SSH-Patator':
            SSH_Patator_batch.append(row)
        elif row[84] == 'DoS slowloris':
            DoS_slowloris_batch.append(row)
        elif row[84] == 'DoS Slowhttptest':
            DoS_Slowhttptest_batch.append(row)
        else:
            continue

    data = []
    if len(Benign_batch) > 0:
        data.append([Benign_batch, 'BENIGN'])
    if len(DDos_batch) > 0:
        data.append([DDos_batch, 'DDos'])
    if len(PortScan_batch) > 0:
        data.append([PortScan_batch, 'PortScan'])
    if len(DoS_Hulk_batch) > 0:
        data.append([DoS_Hulk_batch, 'DoS_Hulk'])
    if len(DoS_GoldenEye_batch) > 0:
        data.append([DoS_GoldenEye_batch, 'DoS_GoldenEye'])
    if len(FTP_Patator_batch) > 0:
        data.append([FTP_Patator_batch, 'FTP_Patator'])
    if len(SSH_Patator_batch) > 0:
        data.append([SSH_Patator_batch, 'SSH_Patator'])
    if len(DoS_slowloris_batch) > 0:
        data.append([DoS_slowloris_batch, 'DoS_slowloris'])
    if len(DoS_Slowhttptest_batch) > 0:
        data.append([DoS_Slowhttptest_batch, 'DoS_Slowhttptest'])

    send_to_influxdb(data)


