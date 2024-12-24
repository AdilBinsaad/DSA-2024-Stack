class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items

# สร้างอินสแตนซ์ของ Stack
stack = Stack()

# เพิ่มข้อมูล 5 ตัวลงใน Stack
for item in [10, 20, 30, 40, 50]:
    stack.push(item)

# แสดงข้อมูลบนสุดโดยใช้ peek
print("ข้อมูลบนสุด (peek):", stack.peek())

# นำข้อมูลออกจาก Stack 3 ตัว
for _ in range(3):
    print("ข้อมูลที่นำออก (pop):", stack.pop())

# แสดงข้อมูลที่เหลืออยู่ใน Stack
print("ข้อมูลที่เหลืออยู่ใน Stack:", stack.display())
