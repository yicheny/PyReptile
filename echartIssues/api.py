from flask import Flask,jsonify
from flask_cors import CORS
from PyReptile.common.mongoDB import MongoClient
from PyReptile.echartIssues.setting import DB_NAME,TABLE_NAME

app = Flask(__name__)
CORS(app)


db = MongoClient(db_name=DB_NAME,table_name=TABLE_NAME)
@app.route('/local/echartIssues',methods=['GET'])
def login():
    # infos = list(db.find({})) # 直接转换成list响应会报错
    res = []
    for item in db.find({}):
        item.pop('_id')
        res.append(item)
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)