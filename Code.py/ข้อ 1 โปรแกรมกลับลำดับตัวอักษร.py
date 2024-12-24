class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

# ฟังก์ชันสำหรับกลับลำดับข้อความโดยใช้ Stack
def reverse_string(input_string):
    stack = Stack()
    
    # เพิ่มตัวอักษรทั้งหมดในข้อความลงใน Stack
    for char in input_string:
        stack.push(char)

    # นำตัวอักษรออกจาก Stack เพื่อกลับลำดับข้อความ
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# รับข้อความจากผู้ใช้
user_input = input("กรอกข้อความที่ต้องการกลับลำดับ: ")
reversed_output = reverse_string(user_input)
print("ข้อความที่กลับลำดับ:", reversed_output)
