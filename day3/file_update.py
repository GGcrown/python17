# @Time    : 2017/11/16 9:01
# @Author  : Crown
# @File    : file_update.py
import sys

find_str=sys.argv[1]
replay_str=sys.argv[2]
print(find_str)
print(replay_str)
f = open("yesterday", "r", encoding="utf-8")
f_new = open("yesterday2.back", "w", encoding="utf-8")

for line in f:
    if find_str in line:
        # f_new.write("有那么多肆意的快乐等冠哥来享受\n")
        # continue
        print("success")
        line = line.replace(find_str, replay_str)
    f_new.write(line)
f_new.flush()
f.close()
f_new.close()
