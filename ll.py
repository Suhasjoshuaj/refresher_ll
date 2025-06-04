class Node:
  def __init__(self, value):
    self.value = value
    self.next  = None


class Linkdlist:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def pp(self):
    if self.length == 0:
      return None
    pre = self.head
    temp = self.head
    while(temp.next):
      pre = temp
      temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
      self.head = None
      self.tail = None
    return temp
  
  def printll(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next
  
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1  
 
  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
  
  def pp_first(self):
    if self.length == 0:
      return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
      self.tail = None
    return True
   
  def geti(self, value):
    temp = self.head
    while temp is not None:
      if temp.value == value:
        return temp
      temp = temp.next
    return None 

  def getv(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp

  def set_value(self, value, index):
    if index < 0 or index >= self.length:  
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next
    temp.value = value

  def insertll(self, value, index):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    temp = self.getv(index - 1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True

  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      return self.pp_first()
    if index == self.length - 1:
      return self.pp()
    pre = self.getv(index - 1)
    temp = pre.next
    pre.next = temp.next
    temp.next = None
    self.length -= 1
    return temp

  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after

    

#ll = Linkdlist(3)
#print("HI")
#ll.prepend(1)
#ll.append(7)
#ll.append(9)
#ll.printll()
#print("jo")
#ll.set_value(11, 3)
#ll.insertll(17, 4)
#ll.remove(4)
#ll.printll()