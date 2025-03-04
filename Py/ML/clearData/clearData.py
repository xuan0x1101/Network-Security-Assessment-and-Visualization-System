import pandas as pd
import numpy as np
import os

def clearData(file_path, file_name):
    # 读取 CSV 文件并计算总行数
    df = pd.read_csv(file_path)
    total_rows = df.shape[0]

    # 判断第14列和第15列是否存在缺失值和无穷值
    row_mask = df.apply(lambda row: pd.isnull(row[14]) or np.isinf(row[14]) or pd.isnull(row[15]) or np.isinf(row[15]), axis=1)

    # 统计要删除的行数并删除特定行
    rows_to_remove = row_mask.sum()
    df = df[~row_mask]

    # 统计最后一列标签类别及其数量
    label_counts = df.iloc[:, -1].value_counts()

    # 输出结果
    print(f'=======================================')
    print(f'{file_name}')
    print(f'---------------------------------------')
    print(f"Total rows     {total_rows}")
    print(f"Rows removed   {rows_to_remove}")
    print(f"Label counts:\n{label_counts}")
    print(f'=======================================')

    # 将结果写入CSV文件
    target_file_path = os.path.join(target_dir, file_name)
    df.to_csv(target_file_path, index=False)

# 定义原始文件所在目录和目标文件夹目录
source_dir = f'D:\毕设\模拟数据\MachineLearningCVE'
target_dir = f'D:\毕设\模拟数据\MachineLearningCVE\cleared'

# 遍历原始文件夹中的所有文件
for filename in os.listdir(source_dir):
    if filename.endswith('.csv'):
        # 构造原始文件路径和目标文件路径
        source_file = os.path.join(source_dir, filename)

        # 调用清理数据函数
        clearData(source_file, filename)
