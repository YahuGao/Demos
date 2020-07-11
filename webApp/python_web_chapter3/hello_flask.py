# coding=utf-8
from flask import Flask
# 引入Flask类, 该类实现了一个WSGI应用

''' 
    创建Flask实例, 接收包或者模块的名字作为参数, 一般都是
    传递__name__, 让flask.helpers.get_root_path函数通过传入的名字确定
    程序的根目录
'''
app = Flask(__name__)

'''
    使用app.route装饰器会将URL和执行的视图函数的关系保存早app.url_map
    属性上. 处理URL和视图函数的关系的程序就是路由. 这里的视图函数就是
    hello_world
'''
@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    '''
    app.run 启动服务, flask默认监听127.0.0.1:5000, 0.0.0.0表示监听
    所有地址, port设置端口地址.
    服务启动后会调用wekzeug.serving.run_simple进入轮询, 默认使用
    单进程单线程的wekzeug.serving.BaseWSGIServer处理请求, 实际上
    还是使用标准库BaseHTTPServer.HTTPServer, 通过select.select做
    0.5秒的while True的事件轮询.
    在访问127.0.0.1:9000/时, 通过app.url_map找到了注册的'/'这个URL
    模式, 找到对应的hello_world函数执行, 返回'hello world', 状态码
    为200.
    '''
    app.run(host='0.0.0.0', port=9000)
    '''
    app.run的启动方式只适合调试, 不要在生产环境中使用, 生产环境应该
    使用Gunicorn或者uWSGI.
    '''
    