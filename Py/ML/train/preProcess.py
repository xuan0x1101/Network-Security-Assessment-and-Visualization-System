import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFECV
from sklearn.model_selection import KFold, train_test_split
import pandas as pd
from sklearn import preprocessing


def preProcess(data_path, frac):
    print("=============================================================")
    start_time = time.time()
    # 加载数据
    data = pd.read_csv(data_path, header=None)
    # 将最后一列转换为数值型
    label_mapping = pd.factorize(data[78])
    data[78] = label_mapping[0]

    # 随机抽样
    data_sample = data.sample(frac=frac, random_state=42)

    # 对原始数据进行切片，分离出特征和标签
    features = data_sample.iloc[:, 0:78]
    labels = data_sample.iloc[:, 78]
    # 对原始特征进行选择
    selected_features, selected_indices = featureSelect(features, labels)

    # 特征数据标准化
    features_normalized = pd.DataFrame(preprocessing.scale(selected_features))
    # 将多维的标签转为一维的数组
    labels_array = labels.values.flatten()
    # onhot 编码
    labels_encoded = pd.get_dummies(labels_array)

    # 将数据分为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(features_normalized, labels_encoded, test_size=0.2, random_state=42)
    end_time = time.time()
    print("训练集 特征维度:", X_train.shape)
    print("测试集 特征维度:", X_test.shape)
    print("训练集 标签维度:", y_train.shape)
    print("测试集 标签维度:", y_test.shape)

    print("预处理时间: {:.4f} 秒".format(end_time - start_time))
    print("=============================================================")
    return X_train, X_test, y_train, y_test, selected_indices


def featureSelect(features, labels):
    # 创建随机森林分类器作为估计函数
    estimator = RandomForestClassifier()
    # 创建RFECV对象，设置最少选择特征数为36
    rfecv = RFECV(estimator=estimator, min_features_to_select=36, cv=KFold(n_splits=2))
    # 进行特征选择和交叉验证
    rfecv.fit(features, labels)
    print("选出的特征数: ", rfecv.n_features_)
    print("特征重要性排序:\n", rfecv.ranking_)
    # 获取选出的特征的列索引
    selected_indices = getSelectedFeatureIndices(rfecv.ranking_)
    # 提取选出的特征
    selected_features = features.iloc[:, selected_indices]
    return selected_features, selected_indices

def getSelectedFeatureIndices(ranking):
    selected_indices = [i for i, rank in enumerate(ranking) if rank == 1]
    print("选出的特征列索引:\n", selected_indices)
    return selected_indices


# 调用函数并传入数据源路径
data_path = "D:\毕设\src\CICIDS2017\LearningData\\total_sub.csv"
x_train, x_test, y_train, y_test, selected_indices = preProcess(data_path, 1)

save_path = 'D:\毕设\src\CICIDS2017\LearningData\preProcessed'
x_train.to_csv(save_path + "/X_train.csv", index=False, header=False)
x_test.to_csv(save_path + "/X_test.csv", index=False, header=False)
y_train.to_csv(save_path + "/y_train.csv", index=False, header=False)
y_test.to_csv(save_path + "/y_test.csv", index=False, header=False)
pd.Series(selected_indices).to_csv(save_path + "/selected_indices.csv", index=False, header=False)
