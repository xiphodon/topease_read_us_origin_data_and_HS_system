#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/19 10:32
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : read_us_origin_data.py
# @Software: PyCharm

import pandas as pd
import re
import json

file_path = r'E:\work_all\topease\美国进口\usa_01_2017\usa_01_2017.txt'

new_three_lines_file_path = r'data/three_lines.csv'

def read_3_lines_from_China_exp():

    three_lines_list = []

    with open(file_path, 'r') as fp:
        line_index = 0
        for line in fp:
            # pprint(line)
            three_lines_list.append(line)
            line_index += 1
            # if line_index > 10:
            #     break

    re1 = re.compile('\t')

    with open(new_three_lines_file_path, 'w') as fp:
        for new_line in three_lines_list:
            write_line = re.sub(re1,"\001",str(new_line))
            fp.write(write_line)


# def read_3_lines_from_three_lines_file():
#     with open(new_three_lines_file_path, 'r') as fp:
#         fp.readlines()


def read_hs_mapping_json():
    with open(r'./data/HS_code_6.json','r',encoding='utf8') as fp:
        hs_mapping_str = fp.read()
        return json.loads(hs_mapping_str)

def check_hs_code(input_str, hs_mapping_dict):
    if input_str == None:
        print("提示：请输入4~10位的HS编码")
    input_str = str(input_str)
    if len(input_str) < 4:
        print("提示：HS编码位数为4~10位")
    else:
        input_str_f4 = input_str[:4]
        if input_str_f4 in hs_mapping_dict:
            hs_f4_dict = hs_mapping_dict[input_str_f4]
            f4_desc = hs_f4_dict['desc']
            if len(input_str) >= 6:
                if 'next' in hs_f4_dict:
                    input_str_f4_6 = input_str[4:6]
                    hs_f4_next_dict = hs_f4_dict['next']
                    if input_str_f4_6 in hs_f4_next_dict:
                        hs_f4_6_dict = hs_f4_next_dict[input_str_f4_6]
                        f4_6_desc = hs_f4_6_dict['desc']
                        print("HS编码描述：", f4_desc + ',' + f4_6_desc)
                    else:
                        print("HS编码描述：", f4_desc)
                else:
                    print("HS编码描述：", f4_desc)
            else:
                print("HS编码描述：", f4_desc)
        else:
            print("提示：未找到该HS编码匹配的类别，请检查输入的HS编码是否正确")



if __name__ == "__main__":
    read_3_lines_from_China_exp()
    data = pd.read_csv(new_three_lines_file_path, sep="\001")
    print(data.info())
