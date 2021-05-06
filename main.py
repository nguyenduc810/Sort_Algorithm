'''class MyClass :
    def __init__(self , name , age):
        self.name = name
        self.age  =age
    def fun(self):
        print('Name: ',self.name)
        print('Age: ', self.age)
a = MyClass('Nguyen Minh Duc', 20)
a.fun()   '''
class Node:
    """Đây là hàm tạo các Node trong List"""
    def __init__(self, data):
        self.data = data
        self.next  = None
class LinkerList :
    """Cài đặt List"""
    def __init__(self):
        self.head = None
        self.size = 0
    def Push(self, data):
        '''cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)  '''
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size +=1
    def isEmpty(self):
        return self.size == 0
    def Pop(self):
        if self.isEmpty():
            print("The stack is empty.")
        tmp = self.data
        self.head = tmp.next
        self.size -= 1
        return tmp.data
    def PrintInfo(self):
        if not self.isEmpty():
            cur = self.head
            while cur is not None:
                print(cur.data, end=' ')
                cur = cur.next

List = LinkerList()
n = int(input("Input n = "))
while n > 0 :
    List.Push((int(n%2)))
    n = int(n/2)
List.PrintInfo()

