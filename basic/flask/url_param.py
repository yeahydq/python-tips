from flask import Flask
from werkzeug.routing import BaseConverter

app=Flask(__name__)

# 自定义转换器类
class RegexConverter(BaseConverter):

    def __init__(self,map,*args):
        super(RegexConverter, self).__init__(map)
        print(map)
        self.regex = args[0]
        print(args[0])

# 添加自定义的转换器给默认转换器的字典容器
app.url_map.converters['re'] = RegexConverter

@app.route('/regex/<re("[a-z]{6}"):text>')
def hello(text):
    return 'hello %s' % text

@app.route('/regex/<path:text>')
def byPath(text):
    print("Parameters: ", text)
    return 'hello %s' % text

'''
string: 默认的数据类型，需注意不能带有'/'，否则会报404error。
int: 整型数据。
float: 浮点型。
path： 和string类似，但是可以传递斜杠/。
uuid： uuid类型的字符串。
any：可以指定多种路径
'''

@app.route('/regex/<string:text>')
def byString(text):
    print(__name__, "Parameters: ", text)
    return 'hello %s' % text


if __name__ == '__main__':
    # print(app.url_map)
    # app.run(debug=True)
    print("End points: ", app.url_map)
    app.run(debug=True)

# curl http://127.0.0.1:5000/regex/reabca

