from flask import Flask,g
from db import RedisClient

__all__ = ['app']
app = Flask(__name__)

def get_conn():
    if not hasattr(g,'redis'):
        g.redis = RedisClient()
    return g.redis

@app.route('/')
def index():
    return "<h2>这里是代理池首页</h2>"

# 随机返回一个代理
@app.route('/random')
def get_proxy():
    conn = get_conn()
    return conn.random()

# 返回代理池代理数量
@app.route('/count')
def get_counts():
    conn = get_conn()
    return str(conn.count())

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5050) #默认端口是5000