import csv
import threading
import time
from filter import apply_filters


def read_csv(file_path, batch_size):

    # print('start reading...')


    data_batch = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[20] == 'Infinity' or row[20] == 'NaN' or row[21] == 'Infinity' or row[21] == 'NaN':
                continue
            data_batch.append(row)
            if len(data_batch) >= batch_size:
                thread = threading.Thread(target=apply_filters, args=(data_batch,))
                thread.start()
                thread.join()

                data_batch = []
                time.sleep(0.01)  # 间隔1秒

    # 处理剩余的数据
    if len(data_batch) > 0:
        thread = threading.Thread(target=apply_filters, args=(data_batch,))
        thread.start()
        thread.join()

# 调用 read_csv() 函数并传入 CSV 文件路径和批处理大小
read_csv('D:\毕设\src\Py\\test\\test.csv', batch_size=200)


# for i in range(8,12):
#     print(f'No {i} reading...')
#     read_csv(f'D:\毕设\src\CICIDS2017\FullData\\attackData\others\output_{i}.csv', batch_size=10000)
#     time.sleep(10)
