import pandas as pd
import joblib

# 全局变量
selected_indices = pd.read_csv('D:\毕设\src\CICIDS2017\LearningData\preProcessed\selected_indices.csv', header=None)[0].tolist()
model_path = 'D:\毕设\src\Py\ML\model\DTmodel.pkl'
label_mapping_inverse = {
    0: 'BENIGN',
    1: 'DoS slowloris',
    2: 'DoS Slowhttptest',
    3: 'DoS Hulk',
    4: 'DoS GoldenEye',
    5: 'FTP-Patator',
    6: 'SSH-Patator',
}

def predict_byRow(data_batch):
    print('DTJudging...')

    # 加载模型
    model = joblib.load(model_path)
    predicted_data = []

    data_batch_df = pd.DataFrame(data_batch)
    for index, data_row in data_batch_df.iterrows():

        row = data_row.drop([0, 1, 2, 3, 5, 6]).reset_index(drop=True)  #删除机器学习不需要的列
        features = row[selected_indices]  # 提取选中的特征列

        label_onehot = model.predict([features])[0]  # 进行标签预测（返回的是One-Hot编码）
        label = label_mapping_inverse[label_onehot.argmax()]  # 将One-Hot编码转换为原始标签

        data_row = data_row.tolist() + [label]
        predicted_data.append(data_row)

    data_batch_df = pd.DataFrame(predicted_data)



    return data_batch
    # predicted_df.to_csv('D:\毕设\src\\result.csv', index=False, header=False)
