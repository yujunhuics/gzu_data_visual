#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：gzu_data_visual 
@File    ：test.py
@Author  ：Junhui Yu
@Date    ：2021/4/13 19:08 
'''
import pandas as pd

# pure_scv,去除数据库，直接将数据读入内存
# 此文件集成了服务所需要的所有数据的获取

STATIC_PATH = '../static/'

# 对应的文件名称
FILE_NAME = {
    'classes': 'class_.csv',  # 班级信息
    'subjects': 'subject.csv',  # 学科信息
    'controller_type': 'controller.csv',  # 考勤类型
    'controller_infos': 'controller_info.csv',  # 考勤信息
    'exams': 'exam.csv',  # 考试信息
    'exam_results': 'examres.csv',  # 考试成绩
    'total_grade_and_rank': 'total_gc_rank.csv',  # 考试总分
    'dorms': 'sushe.csv',  # 宿舍信息
    'current_student': 'cur_student.csv',  # 在校学生
    'graduated_student': 'grad_student.csv',  # 毕业学生
    'lessons': 'lesson.csv',  # 课程信息
    'study_days': 'study_days.csv',  # 在校天数
    'consumptions': 'consumption.csv',  # 消费信息
    'consumption_predicts': 'consumption_predict.csv',  # 消费预测
    'rank_predicts': 'rank_predict.csv',  # 等地预测
    'subjects_select': 'process_7_3.csv',  # 七选三信息
    'medical_data': 'medical.xlsx'
}


def get_xlsx_data(filename):
    file_path = STATIC_PATH + FILE_NAME[filename]
    data = pd.read_excel(file_path)
    print(data)
    return data


get_xlsx_data('medical_data')


#
# def get_data():
#     data=pd.read_excel('D:\code\python\gzu_data_visual\gzu_data_visual\static\medical.xlsx')
#     # data1=data.head()
#     # print(data1)
#     print(data)
#
# get_data()

