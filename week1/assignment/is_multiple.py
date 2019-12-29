def is_multiple(x, y):
    if x < y:
        return "y가 x보다 큽니다."
    elif x % y == 0:
        return True
    else:
        return False

x = int(input("첫 번째 숫자를 입력하세요: "))
y = int(input("두 번째 숫자를 입력하세요: "))

print(is_multiple(x, y))
