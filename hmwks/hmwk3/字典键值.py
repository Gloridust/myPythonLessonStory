class KeyValueDictionary:  
    def __init__(self):  
        self.data = {}  
  
    def set(self, key, value):  
        self.data[key] = value  
  
    def get(self, key):  
        if key in self.data:  
            return self.data[key]  
        else:  
            return "您输入的键不存在！"  
              
# 测试代码  
d = KeyValueDictionary()  
d.set('name', 'Alice')  
d.set('age', 25)  
print(d.get('name'))  # 输出：Alice  
print(d.get('age'))  # 输出：25  
print(d.get('job'))  # 输出：您输入的键不存在！