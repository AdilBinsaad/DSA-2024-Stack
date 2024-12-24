# ฟังก์ชันตรวจสอบว่าตัวอักษรเป็นตัวเลขหรือไม่
def is_operand(c):
    return c.isdigit()

# ฟังก์ชันตรวจสอบลำดับความสำคัญของตัวดำเนินการ
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

# ฟังก์ชันการดำเนินการทางคณิตศาสตร์
def apply_operator(op, b, a):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    return 0

# ฟังก์ชันแปลง Infix เป็น Postfix
def infix_to_postfix(expression):
    stack = []
    postfix = []
    for char in expression:
        if char == ' ':
            continue
        elif is_operand(char):
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:  # ตัวดำเนินการ
            while (stack and precedence(stack[-1]) >= precedence(char)):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

# ฟังก์ชันคำนวณผลจาก Postfix
def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if is_operand(char):
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(char, b, a)
            stack.append(result)
    
    return stack[-1]

# ฟังก์ชันหลักสำหรับรับค่า Infix จากผู้ใช้และประเมินผล
def evaluate_infix(expression):
    postfix_expression = infix_to_postfix(expression)
    print(f'Postfix Expression: {postfix_expression}')
    return evaluate_postfix(postfix_expression)

# ทดสอบฟังก์ชัน
if __name__ == '__main__':
    infix_expression = input("กรุณากรอกนิพจน์ในรูป Infix: ")
    result = evaluate_infix(infix_expression)
    print(f'Result: {result}')
