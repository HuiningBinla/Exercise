# coding=utf-8

tuple = ("abcd", 786, 2.23, "john", 70.2)
tinytuple = (123, "john")

# 输出完整元组
print(tuple)
# 输出元组的第一个元素
print(tuple[0])
# 输出第二个至第三个元素
print(tuple[1:3])
# 输出从第三个开始至列表末尾的所有元素
print(tuple[2:])
# 输出元组两次
print(tuple * 2)
# 打印组合的元组
print(tuple + tinytuple)

