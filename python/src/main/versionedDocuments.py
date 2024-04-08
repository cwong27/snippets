import time

class document():
    def __init__(self, text):
        self.text = text
        self.timestamp = time.time()
        self.next = None

class documents():
    def __init__(self):
        self.documents = {}
    
    def add(self, name, text):
        if name not in self.documents.keys():
            self.documents[name] = document(text)
        else:
            newDocument = document(text)
            newDocument.next = self.documents[name]
            newDocument.timestamp = time.time()
            self.documents[name] = newDocument
    
    def get(self, name):
        if name not in self.documents.keys():
            return None
        else:
            return self.documents[name].text
        
    def getAll(self, name):
        if name not in self.documents.keys():
            return None
        head = self.documents[name]
        while head:
            print(f"{head.timestamp}:{head.text}")
            head = head.next

    def getAtTime(self, name, time):
        if name not in self.documents.keys():
            return None
        head = self.documents[name]
        while head:
            if head.timestamp <= time:
                return head.text
            head = head.next

docs = documents()

docs.add("test1", "foo")
t1 = time.time()

docs.add("test2", "Car")
print(docs.get("test1"))

time.sleep(0.05)
t2 = time.time()
docs.add("test1", "bar")

time.sleep(0.05)
t3 = time.time()
docs.add("test1", "A")

time.sleep(0.05)
t4 = time.time()
docs.add("test1", "This is test!")

print(docs.getAtTime("test1", t1))
print(docs.getAtTime("test1", t2))
print(docs.getAtTime("test1", t3))
print(docs.getAtTime("test1", t4))

docs.getAll("test1")

