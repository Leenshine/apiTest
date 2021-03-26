### 项目介绍
基于```python+behave```开发测试用例，```behave```用来管理和执行测试例。使用```allure```工具产生html可读性report.



### 项目目录结构
```
--- cryptoTest
| ---- common
	| ---- utils.py								公用方法
	| ---- websocket_client.py					封装websocket client
| ----config
	| ---- api_name.json						rest接口方法名称
	| ---- general.json							rest_api信息
	| ---- websocket_general.json				websocket_api信息
| ----report									测试报告
| ----restApiTest
	| ---- features
		| ---- steps
			| ---- get_candlestick.py			测试用例步骤实现
		| ---- get_candlestick.feature			testcase用例描述
| ----webSocketTest
	| ---- features
		| ---- steps
			| ---- book_instrument.py			测试用例步骤实现
		| ---- book_instrument.feature			testcase用例描述
		| ---- enviroment.py                    实现每个scenario执行前后的操作
| ----requirements.txt							依赖包信息

```
### 运行

1. 运行restAPI testcases
```
behave -f allure_behave.formatter:AllureFormatter -o report restApiTest/features/
```
2. 运行websocketAPI testcases
```
behave -f allure_behave.formatter:AllureFormatter -o report webSocketTest/features/
```
3. 生成html报告
```
allure serve report
```


