#!/usr/bin/env python

# -*- Coding: UTF-8 -*-
# @Time    : 11/15/18 5:28 PM
# @Author  : Terry LAI
# @Email   : terry.lai@hotmail.com
# @File    : capitalone.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask_cors import CORS
from flask import Flask, abort, request, jsonify
import bb

app = Flask(__name__)

# 测试数据暂时存放
tasks = []
course_dict = {'.NET Framework':['1','2','3'],'REST':['4','5','6'],'React.js':['7','8','9'],
               'Golang':['1','2','3'],'AngularJS':['4','5','6'],'jQuery':['7','8','9'],
               'Frontend Development': ['1', '2', '3'], 'XHTML': ['4', '5', '6'], 'Node.js': ['7', '8', '9']
               }

@app.route('/predict/', methods=['POST'])
def predict():
    print (request.headers)
    print (request.form)
    earningsmonth1 = request.form['earningsmonth1']
    earningsmonth2 = request.form['earningsmonth2']
    earningsmonth3 = request.form['earningsmonth3']
    hoursmonth1 = request.form['hoursmonth1']
    hoursmonth2 = request.form['hoursmonth2']
    hoursmonth3 = request.form['hoursmonth3']
    graphic = request.form['graphic']
    software = request.form['software']
    python = request.form['python']
    r = request.form['html']
    javascript = request.form['javascript']

    print(python)

    earningsmonth1 = int(earningsmonth1)
    earningsmonth2 = int(earningsmonth2)
    earningsmonth3 = int(earningsmonth3)
    hoursmonth1 = int(hoursmonth1)
    hoursmonth2 = int(hoursmonth2)
    hoursmonth3 = int(hoursmonth3)

    hourlyrate = (earningsmonth1+earningsmonth2+earningsmonth3)/(hoursmonth1+hoursmonth1+hoursmonth1)

    ret = None
    if python=='true':
        ret = bb.Happymodel("Python")
    elif r=='true':
        print("hahahah")
        ret = bb.Happymodel("HTML")
    else:
        ret = bb.Happymodel("JavaScript")

    dict = {}
    dict['skills'] = list(ret[0])
    print(ret[1])
    print(hourlyrate)
    dict['rate'] = round(ret[1]/hourlyrate * 10,0)
    course = []
    # for skill in dict['skills']:
    #     course.append(course_dict[skill])
    dict['courses'] = course
    print(dict)
    tasks.append(dict)

    return jsonify({'taskid': len(tasks)-1})

@app.route('/get_result/', methods=['POST'])
def get_result():
    taskid = request.form['taskid']
    taskid = int(taskid)
    ret = tasks[taskid]
    return jsonify({'ret': ret})



@app.route('/add_task/', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=8383, debug=True)


