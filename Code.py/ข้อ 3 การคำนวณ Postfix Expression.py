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

# ทดสอบโปรแกรมโดยรับนิพจน์ Postfix จากผู้ใช้
postfix_expression = input("กรอกนิพจน์ Postfix (คั่นด้วยช่องว่าง): ")
result = evaluate_postfix(postfix_expression)
print("ผลลัพธ์ของนิพจน์ Postfix:", result)
