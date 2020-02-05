# -*- coding: utf-8 -*-
"""
Created on 2020/2/5 21:46
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


# with open("th_videos.csv","r")as f:
#     csv_reader=csv.reader(f)
#     p=list(csv_reader)
# with open("b站tag数据_180719/video_tag_seq.csv","r") as g:
#     csv_reader=csv.reader(f)

def sImport(dir):
    with open(dir, "r")as f:
        return list(csv.reader(f))


video_list = sImport("th_videos.csv")
print("video data imported.\n")
video2tag = sImport("b站tag数据_180719/video_tag_seq.csv")
print("tid data imported.\n")
v2t_dict = dict(video2tag)
print("tid data encoded.\n")
tag2name = sImport("b站tag数据_180719/tag_data.csv")
print("tag data imported.\n")
t2n_dict = dict(tag2name)
print("tag data encoded.\n")

with open("th_video_tags.csv", "w+", newline="")as f:
    csv_writer = csv.writer(f)
    for line in video_list:
        vid = line[0]
        tid = v2t_dict[vid]
        if type(tid) == int:
            tid_list = [tid]
        else:
            tid_list = tid.split(",")
        tags = [t2n_dict[tid] for tid in tid_list]
        csv_writer.writerow([vid] + tags)
print("writing finished.")