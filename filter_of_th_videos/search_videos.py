# -*- coding: utf-8 -*-
"""
Created on 2020/2/2 17:36
版权所有（c）<2020> 11598
github:https://github.com/HydrogenDeuterium
反996许可证版本1.0
在符合下列条件的情况下，特此免费向任何得到本授权作品的副本（包括源代码、文件和/或相关内容，以下统称为“授权作品”）的个人和法人实体授权：被授权个人或法人实体有权以任何目的处置授权作品，包括但不限于使用、复制，修改，衍生利用、散布，发布和再许可：
1. 个人或法人实体必须在许可作品的每个再散布或衍生副本上包含以上版权声明和本许可证，不得自行修改。
2.
个人或法人实体必须严格遵守与个人实际所在地或个人出生地或归化地、或法人实体注册地或经营地（以较严格者为准）的司法管辖区所有适用的与劳动和就业相关法律、法规、规则和标准。如果该司法管辖区没有此类法律、法规、规章和标准或其法律、法规、规章和标准不可执行，则个人或法人实体必须遵守国际劳工标准的核心公约。
3.
个人或法人不得以任何方式诱导或强迫其全职或兼职员工或其独立承包人以口头或书面形式同意直接或间接限制、削弱或放弃其所拥有的，受相关与劳动和就业有关的法律、法规、规则和标准保护的权利或补救措施，无论该等书面或口头协议是否被该司法管辖区的法律所承认，该等个人或法人实体也不得以任何方法限制其雇员或独立承包人向版权持有人或监督许可证合规情况的有关当局报告或投诉上述违反许可证的行为的权利。
该授权作品是"按原样"提供，不做任何明示或暗示的保证，包括但不限于对适销性、特定用途适用性和非侵权性的保证。在任何情况下，无论是在合同诉讼、侵权诉讼或其他诉讼中，版权持有人均不承担因本软件或本软件的使用或其他交易而产生、引起或与之相关的任何索赔、损害或其他责任。
"""
import csv

whitelist = {166, 552, 691, 743, 755, 768, 912, 937, 1040, 1317, 1369, 2256, 2300, 3918, 5128, 5796, 7698, 7768, 8144,
        9241, 9377, 9379, 9394, 10619, 13453, 14253, 16700, 19354, 32972, 35391, 39389, 39393, 49854, 61446, 67277,
        68899, 101578, 249735, 702956, 960703, 992170, 1170051, 1288519, 1293428, 1341993, 1769944, 2079052, 2485355,
        2485798, 2493141, 2494413, 2501879, 2564523, 2564525, 2569764, 2581284, 2594104, 2616330, 2667821, 2731075,
        2804891, 2823669, 2903194, 2933130, 2938700, 3119756, 3426337, 3445888, 3468726, 3537174, 3597143, 3697720,
        3703914, 6269440, 6349190, 6660004, 7582884}
blacklist = {34155, 61021, 86902, 141998, 1018507, 1477013, 1694863}


def in_black(tag_list):
    return tag_list & blacklist != set()


def in_white(tag_list):
    return tag_list & whitelist != set()


with open(r"b站tag数据_180719/video_tag_seq.csv", "r") as f, open("th_videos.csv", "w")as g:
    csv_reader = csv.reader(f)
    # num = 0
    # 对每行分别处理
    for row in csv_reader:
        # 获取标签数据
        tag_data = row[1]

        # 处理单个标签情况
        if type(tag_data) == int:
            tag_list = {tag_data}
        # 处理多个或空标签情况
        elif type(tag_data) == str:

            # 处理空标签情况
            if tag_data == "":
                continue
            # 处理多个标签情况
            else:
                tag_list = set(map(int, tag_data.split(",")))
        pass
        # 判断是否满足条件
        # 在白名单内
        if in_white(tag_list):
            # 不在黑名单内
            if not in_black(tag_list):
                # print(row[0])
                g.write(row[0]+"\n")
        # num+=1
        # if num>10000:
        #     break