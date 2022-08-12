#!/usr/bin/python3
# encoding:utf-8
# https://dormousehole.readthedocs.io/en/latest/quickstart.html# flask快速上手
import flask,json
from markupsafe import escape #变量规则
# 实例化api，把当前这个python文件当作一个服务，__name__代表当前这个python文件
api = flask.Flask(__name__) 
url_for = flask.url_for
request = flask.request
render_template = flask.render_template

@api.route('/')
def index():
    return 'Index Page'

@api.route('/hello',methods = ['POST','GET'])
def hello():
  if(request.method=='POST'):
    return 'Hello, World POST'
  else:
    return 'Hello, World GET'

@api.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@api.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@api.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@api.route('/html/')
@api.route('/html/<name>')
def htmlTest(name=None):
    return render_template('index.html', name=name)
  
 
if __name__ == '__main__':
  api.run(port=8888,debug=True,host='0.0.0.0') # 启动服务
  # debug=True,改了代码后，不用重启，它会自动重启
  # 'host='127.0.0.1'别IP访问地址
  # 'host='0.0.0.0' 局域网可访问
