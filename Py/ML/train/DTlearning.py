import time
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def DTlearning(X_train, X_test, y_train, y_test):
    print("=============================================================")

    start_time = time.time()
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=12, min_samples_leaf=1, splitter="best")
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    end_time = time.time()

    accuracy = accuracy_score(y_test, y_pred)
    joblib.dump(clf, model_path + "\DTmodel.pkl")

    print("训练时间: {:.4f} 秒".format(end_time - start_time))
    print("预测精度: {:.4f}".format(accuracy))
    print("=============================================================")



def loadPreProcessedData(data_path):
    X_train = pd.read_csv(data_path + "/X_train.csv", header=None)
    X_test = pd.read_csv(data_path + "/X_test.csv", header=None)
    y_train = pd.read_csv(data_path + "/y_train.csv", header=None)
    y_test = pd.read_csv(data_path + "/y_test.csv", header=None)
    return X_train, X_test, y_train, y_test


# 调用函数并输出预测精度
data_path = 'D:\毕设\src\CICIDS2017\LearningData\preProcessed'
model_path = 'D:\毕设\src\Py\ML\model'

X_train, X_test, y_train, y_test = loadPreProcessedData(data_path)
DTlearning(X_train, X_test, y_train, y_test)
