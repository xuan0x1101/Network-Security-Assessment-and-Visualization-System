## 进入虚拟机

### 查看服务状态

使用`sudo systemctl status`查看influx, telegraf, grafana运行状态，确保其为运行状态。

若非运行状态，使用`sudo systemctl start`启动服务。

### 数据库查看

`/usr/bin/influx`进入数据库，以下代码可对数据库进行增删改查：

```
show databases
create database 数据库名
drop database 数据库名 
use 数据库名
```



## 机器学习模块（ML）

`/Py/ML`中为机器学习模块，其中`clearData`为对数据进行清洗的文件夹。

![image-20230705194544586](https://article.biliimg.com/bfs/article/36311677565118751425fc4c238befb25d43c39c.png)

`train`文件夹为数据预处理与模型训练。在`preProcess.py`中，设置`data_path`和`save_path`，分别为数据存放和保存路径。

![image-20230705195122301](https://article.biliimg.com/bfs/article/6e0d033f4446f4042622b942ad39e4d6854e72d2.png)

设置好后可以开始数据预处理，完成后的数据会以csv保存在存储路径。

![image-20230705195444829](https://article.biliimg.com/bfs/article/3e39d3b494740c7e35a8d1f2008d29e6d49f94a2.png)

随后进入`DTlearning.py`，设置`data_path`及`model_path`，分别为预处理数据存放路径及模型输出路径。随后运行文件即可得到模型文件。

![image-20230705195827453](https://article.biliimg.com/bfs/article/5206871713a9aa9f539c4c87a02da851639b9691.png)

最后在`predict`文件夹中的`predict_byRow.py`为数据预测单元，需要设置的参数为`selected_indices`、`model_path`。文件中的函数接收待预测数据作为参数，根据给定的模型及标签进行预测，返回结果。



## 规则匹配模块（IndicatorJudge）

`/Py/IndicatorJudge`中为规则匹配模块，包含`DDoS.py`和`PortScan.py`两个文件夹，分别对应两种攻击的检测。两个文件夹中均仅需将待预测数据传入参数，函数返回预测结果。



## 数据发送模块（InfluxSender）

`/Py/InfluxSender`中为数据发送模块，包含三个文件夹：`filter.py`、`reader.py`、`sender.py`。

![image-20230705200757317](https://article.biliimg.com/bfs/article/4a5c9999a21e5235000160bd50839f5662ea2b2c.png)

在reader中直接给`read_csv`传递数据文件路径，运行即可开始读取数据文件。随后数据将被传送到filter中进行分类预测，得到的预测完成的数据将被送入sender发送至虚拟机中的influx数据库。



## 可视化查看

使用浏览器登陆`http://192.168.10.100:3000`，在面板中可以添加数据源。

![在这里插入图片描述](https://img-blog.csdnimg.cn/cff98475992945f79c7dabe07357cc78.png)

![image-20230705202253112](https://article.biliimg.com/bfs/article/fcd595a0c4f4db66c8c1ffc163ec7395107c4aee.png)

添加好数据源后，在Dashboard中添加可视化面板，可以选择合适的展示样式，利用grafana的配置面板或SQL语言进行查询。

![image-20230705202419144](https://article.biliimg.com/bfs/article/591fd204099c5eaf2ae0e07182aa1cb7068b450b.png)

最终可以得到理想的数据看板。

![image-20230705202443458](https://article.biliimg.com/bfs/article/e45a1863e3e09c52342d8072be2931a611524ace.png)