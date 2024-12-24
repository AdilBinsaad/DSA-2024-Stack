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

# ฟังก์ชันแปลงเลขฐาน 10 เป็นฐานอื่นโดยใช้ Stack
def convert_base(number, base):
    stack = Stack()
    digits = "0123456789ABCDEF"

    # นำเศษที่ได้จากการหารฐานใส่ใน Stack
    while number > 0:
        remainder = number % base
        stack.push(digits[remainder])
        number //= base

    # นำตัวเลขออกจาก Stack เพื่อสร้างผลลัพธ์
    converted_number = ""
    while not stack.is_empty():
        converted_number += stack.pop()

    return converted_number

# รับเลขฐาน 10 จากผู้ใช้งาน
decimal_number = int(input("กรอกตัวเลขฐาน 10 ที่ต้องการแปลง: "))

# แปลงเป็นฐาน 2 และฐาน 16
binary_result = convert_base(decimal_number, 2)
hexadecimal_result = convert_base(decimal_number, 16)

# แสดงผลลัพธ์
print(f"เลขฐาน 2: {binary_result}")
print(f"เลขฐาน 16: {hexadecimal_result}")
