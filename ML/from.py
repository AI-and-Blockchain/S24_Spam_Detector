import requests
import time

# 设置API的URL
url = 'http://129.161.154.79:5000/api/start_transact'
url1='http://129.161.154.79:5000/api/output'

# 如果API需要传递数据，可以在这里定义。假设这个API需要用户名和密码，你可以这样做：
data = {
    'message': 'your_utestingggggggggggggggggggggggggggggggggggggggggggggsername',
}
response = requests.post(url, json=data)
# 发送POST请求
while (1):


    response1 = requests.get(url1)
    print(response1.text)
    # 打印响应内容
    print(response.text)
    time.sleep(5)
