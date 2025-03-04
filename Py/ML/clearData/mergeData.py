import pandas as pd

def merge_and_stats():
    # 定义原始文件路径和文件名列表
    file_paths = [
        "Wednesday-workingHours.pcap_ISCX.csv",
        "Tuesday-WorkingHours.pcap_ISCX.csv",
        "Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
        "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
    ]

    # 创建一个空的 DataFrame 用于存储合并后的数据
    merged_df = pd.DataFrame()

    # 遍历文件列表
    for file in file_paths:
        # 读取 CSV 文件并删除表头
        df = pd.read_csv(f'D:\毕设\src\CICIDS2017\LearningData\cleared\{file}', header=None, skiprows=1)

        # 将处理后的数据追加到合并的 DataFrame 中
        merged_df = merged_df.append(df)

    # 统计总行数
    total_rows = merged_df.shape[0]

    # 统计最后一列标签类别及其数量
    label_counts = merged_df.iloc[:, -1].value_counts()

    # 将合并后的数据写入 CSV 文件
    merged_df.to_csv("D:\毕设\src\CICIDS2017\LearningData\\total.csv", index=False)

    # 输出统计结果
    print(f'=======================================')
    print('mergeData:')
    print(f'---------------------------------------')
    print(f"Total rows:   {total_rows}")
    print(f"Label counts:\n{label_counts}")
    print(f'=======================================')


merge_and_stats()
