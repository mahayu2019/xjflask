from flask import Flask

'''
创建Flask的应用对象
__name__表示当前的模块名字
    flask以当前这个模块所在目录为根目录,static为静态目录,templates为模板目录
'''
app = Flask(__name__,
            static_url_path='/static',  # 浏览器中访问静态页面的url前缀,默认static
            static_folder="static",  # 静态文件的目录,默认static
            template_folder="templates"  # 模板文件的目录.默认为templates
            )


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
