import sys
import os
from flask import Flask
from aetam import app

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("> 引数が存在しません\n")
        os.system('make help')
        sys.exit()

    if sys.argv[1] == 'runserver':
        app.run(host=app.config['HOST'], port=app.config['PORT'])
    elif sys.argv[1] == 'migrate':
        from aetam.models import util_db
        util_db.init()
    else:
        print('存在しないコマンドです')

