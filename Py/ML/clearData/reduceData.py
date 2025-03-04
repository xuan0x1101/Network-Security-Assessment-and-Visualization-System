import pandas as pd
import numpy as np

def process_labels(file_path):
    # 读取 CSV 文件
    df = pd.read_csv(file_path)

    # 删除最后一列为 'DDoS'、'PortScan'、'Heartbleed' 的行
    df = df[~df.iloc[:, -1].isin(['DDoS', 'PortScan', 'Heartbleed'])]

    # 删除 'DoS Hulk' 类别中的随机 200000 个样本
    dos_hulk_indices = df[df.iloc[:, -1] == 'DoS Hulk'].index.to_numpy()
    np.random.shuffle(dos_hulk_indices)
    dos_hulk_indices_to_remove = dos_hulk_indices[:200000]
    df = df.drop(dos_hulk_indices_to_remove)

    # 删除 'BENIGN' 类别中的随机 1060000 个样本
    benign_indices = df[df.iloc[:, -1] == 'BENIGN'].index.to_numpy()
    np.random.shuffle(benign_indices)
    benign_indices_to_remove = benign_indices[:1060000]
    df = df.drop(benign_indices_to_remove)

    # 统计最后一列标签类别及其数量
    label_counts = df.iloc[:, -1].value_counts()

    # 将处理后的数据写入 CSV 文件
    df.to_csv("D:\毕设\src\CICIDS2017\LearningData\\total_sub.csv", index=False)

    # 输出统计结果
    print(f'=======================================')
    print('total_sub:')
    print(f'---------------------------------------')
    print(f"Label counts:\n{label_counts}")
    print(f'=======================================')

# 指定文件路径
file_path = "D:\毕设\src\CICIDS2017\LearningData\\total.csv"

# 调用处理函数
process_labels(file_path)
