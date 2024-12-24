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

# ฟังก์ชันสำหรับคำนวณผลลัพธ์ของนิพจน์ Postfix
def evaluate_postfix(expression):
    stack = Stack()
    
    for token in expression.split():
        if token.isdigit():  # ถ้าเป็นตัวเลข ให้เพิ่มลงใน Stack
            stack.push(int(token))
        else:  # ถ้าเป็น Operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(int(operand1 / operand2))  # ใช้ int() เพื่อการหารแบบจำนวนเต็ม

    return stack.pop()

# ฟังก์ชันสำหรับตรวจสอบความถูกต้องของ JSON string
import json

def validate_json(json_string):
    stack = Stack()
    
    try:
        # ลองแปลง JSON string ด้วยไลบรารี json เพื่อความถูกต้องเบื้องต้น
        json.loads(json_string)

        for char in json_string:
            if char in '{[':
                stack.push(char)
            elif char in '}]':
                if stack.is_empty():
                    return False
                top = stack.pop()
                if (char == '}' and top != '{') or (char == ']' and top != '['):
                    return False

        return stack.is_empty()
    except json.JSONDecodeError:
        return False

# ทดสอบโปรแกรมโดยรับ JSON string จากผู้ใช้
json_string = input("กรอก JSON string ที่ต้องการตรวจสอบ: ")
if validate_json(json_string):
    print("JSON string ถูกต้อง")
else:
    print("JSON string ไม่ถูกต้อง")
