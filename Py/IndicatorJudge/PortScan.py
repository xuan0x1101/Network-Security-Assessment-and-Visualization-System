import pandas as pd

# # 计算判断指标的阈值
# threshold_fwd_packets = data['Total Fwd Packets'].mean()
# threshold_bwd_packets = data['Total Backward Packets'].mean()
# threshold_fwd_length_min = data['Fwd Packet Length Min'].mean()
# threshold_fwd_length_max = data['Fwd Packet Length Max'].mean()
# threshold_bwd_length_min = data['Bwd Packet Length Min'].mean()
# threshold_bwd_length_max = data['Bwd Packet Length Max'].mean()
# threshold_fwd_header_length = data['Fwd Header Length'].mean()


threshold_fwd_packets = 16.8
threshold_bwd_packets = 20.9
threshold_fwd_length_min = 17.4
threshold_fwd_length_max = 232.8
threshold_bwd_length_min = 34.8
threshold_bwd_length_max = 1220.0
threshold_fwd_header_length = 264.7

def PortScanJudger(data_batch):
    print('PortScanJudging...')
    data_batch_df = pd.DataFrame(data_batch)
    data_batch_df.columns = [
        'Flow ID', 'Source IP', 'Source Port', 'Destination IP', 'Destination Port',
        'Protocol', 'Timestamp', 'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
        'Total Length of Fwd Packets', 'Total Length of Bwd Packets', 'Fwd Packet Length Max',
        'Fwd Packet Length Min', 'Fwd Packet Length Mean', 'Fwd Packet Length Std',
        'Bwd Packet Length Max', 'Bwd Packet Length Min', 'Bwd Packet Length Mean',
        'Bwd Packet Length Std', 'Flow Bytes/s', 'Flow Packets/s', 'Flow IAT Mean',
        'Flow IAT Std', 'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Total', 'Fwd IAT Mean',
        'Fwd IAT Std', 'Fwd IAT Max', 'Fwd IAT Min', 'Bwd IAT Total', 'Bwd IAT Mean',
        'Bwd IAT Std', 'Bwd IAT Max', 'Bwd IAT Min', 'Fwd PSH Flags', 'Bwd PSH Flags',
        'Fwd URG Flags', 'Bwd URG Flags', 'Fwd Header Length', 'Bwd Header Length',
        'Fwd Packets/s', 'Bwd Packets/s', 'Min Packet Length', 'Max Packet Length',
        'Packet Length Mean', 'Packet Length Std', 'Packet Length Variance',
        'FIN Flag Count', 'SYN Flag Count', 'RST Flag Count', 'PSH Flag Count',
        'ACK Flag Count', 'URG Flag Count', 'CWE Flag Count', 'ECE Flag Count',
        'Down/Up Ratio', 'Average Packet Size', 'Avg Fwd Segment Size',
        'Avg Bwd Segment Size', 'Fwd Header Length', 'Fwd Avg Bytes/Bulk',
        'Fwd Avg Packets/Bulk', 'Fwd Avg Bulk Rate', 'Bwd Avg Bytes/Bulk',
        'Bwd Avg Packets/Bulk', 'Bwd Avg Bulk Rate', 'Subflow Fwd Packets',
        'Subflow Fwd Bytes', 'Subflow Bwd Packets', 'Subflow Bwd Bytes',
        'Init_Win_bytes_forward', 'Init_Win_bytes_backward', 'act_data_pkt_fwd',
        'min_seg_size_forward', 'Active Mean', 'Active Std', 'Active Max',
        'Active Min', 'Idle Mean', 'Idle Std', 'Idle Max', 'Idle Min', 'Label'
    ]
    # 根据指标进行判断
    portscan_label = []
    for index, row in data_batch_df.iterrows():
        if (float(row['Total Fwd Packets']) < threshold_fwd_packets) and \
                (float(row['Total Backward Packets']) < threshold_bwd_packets) and \
                (float(row['Fwd Packet Length Max']) >= threshold_fwd_length_min) and \
                (float(row['Fwd Packet Length Max']) <= threshold_fwd_length_max) and \
                (float(row['Fwd Packet Length Min']) >= threshold_fwd_length_min) and \
                (float(row['Fwd Packet Length Min']) <= threshold_fwd_length_max) and \
                (float(row['Bwd Packet Length Max']) >= threshold_bwd_length_min) and \
                (float(row['Bwd Packet Length Max']) <= threshold_bwd_length_max) and \
                (float(row['Bwd Packet Length Min']) >= threshold_bwd_length_min) and \
                (float(row['Bwd Packet Length Min']) <= threshold_bwd_length_max) and \
                (float(row['Fwd Header Length']) < threshold_fwd_header_length):
            portscan_label.append("PortScan")
        else:
            portscan_label.append("BENIGN")

    # 添加标签列
    data_batch_df[' Label'] = portscan_label

    return data_batch
