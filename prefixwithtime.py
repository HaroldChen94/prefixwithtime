# 一个强迫症的文件重命名工具


import os
import time
import re

filepath = input('请输入文件路径(结尾加上\')：')
# 获取该目录下所有文件，存入列表中
fileList = os.listdir(filepath)
n = 0
for i in fileList:
    if re.match(r'\d{6}_', fileList[n]):
        print('文件名' + fileList[n] + '已符合标准格式。')
        n += 1
        continue
    file_time = re.match(r'\d{6}', fileList[n])
    if file_time:
        new_file_time = file_time.group() + '_'
        new_name = re.sub(r'\d{6}', new_file_time, fileList[n])
    else:
        # 读取文件创建时间
        t = os.stat(filepath).st_ctime
        timeStruct = time.localtime(t)  # 把时间戳转化为时间
        t = time.strftime('%y%m%d', timeStruct)
        new_name = t + '_' + fileList[n]
    # 设置旧文件名（就是路径+文件名）
    oldname = filepath + os.sep + fileList[n]  # os.sep添加系统分隔符
    # 设置新文件名
    newname = filepath + os.sep + new_name
    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(fileList[n], '======>', new_name)
    n += 1
