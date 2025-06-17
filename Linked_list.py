class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LL:
    def __init__(self):
        self.head=None

    def insert_b(self,data):
        n1=Node(data,self.head)
        self.head=n1

    def print(self):
        if self.head is None:
            print("empty")
            return
        
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data) + '-->'
            itr=itr.next
        print(llstr)

if __name__ =='__main__':
    ll=LL()
    ll.insert_b(1)
    ll.insert_b(7)
    ll.insert_b(6)
    ll.print()
    
