


name = ['yanyang','zhangjiaseng','yangyi','guoqian','wanghuizheng']
#添加
#name.append('youheng')  #直接添加到最后面结果：  ['yanyang', 'zhangjiaseng', 'yangyi', 'guoqian', 'wanghuizheng', 'youheng']
#name.insert(0,'youheng')  #先输入插入到什么位置
position = ['director']
name.extend(position)   #extend 扩展列表 要用列表的形式


print(name)