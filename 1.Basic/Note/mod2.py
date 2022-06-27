def sum(a, b):
    if type(a) != type(b):
        print("더하기를 할수 없습니다.")
        return
    else:
        return a + b
# __로 시작하는거는 다 시스템 변수임, 파이썬은 __를 엄청 좋아함.
# 개발엔 꼭 써줘야함.
# #main method
#python을 터미널로 실행 누르면 30 이 나옴.
if __name__ == "__main__":
    print(sum(10,20))