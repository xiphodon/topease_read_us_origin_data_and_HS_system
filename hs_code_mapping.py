#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/21 10:52
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : hs_code_mapping.py
# @Software: PyCharm

import json


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
    hs_mapping_dict = read_hs_mapping_json()
    print("\n===== HS查询系统 =====\n")
    while True:
        input_str = input("请输入HS编码（4~10位）：")
        if input_str == 'exit':
            print("\n===== 退出HS查询系统 =====\n")
            break
        else:
            check_hs_code(input_str,hs_mapping_dict)