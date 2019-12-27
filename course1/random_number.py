import random

highest = 20
lowest = 1

number = random.randrange(lowest, highest)

while True:
    try:
        answer = int(input("숫자를 입력하세요: "))

        if answer > highest or answer < lowest:
            print("{}에서 {}까지의 숫자를 입력해주세요.\n".format(lowest, highest))
        elif number > answer:
            print("너무 낮습니다. 다시 입력하세요!\n")
        elif number < answer:
            print("너무 높습니다. 다시 입력하세요!\n")
        else:
            print("정답입니다!")
            break
    except ValueError:
        print("\n숫자를 입력하세요!\n")
