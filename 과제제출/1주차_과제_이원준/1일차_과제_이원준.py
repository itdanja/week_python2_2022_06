# 1일차
    # 1. 엘레베이터 알고리즘
    # 2. 신호등 알고리즘
    # 3. 로또 구매 프로그램
        # 1. 로또 게임 횟수 입력받기
        # 2. 게임수 만큼 한 게임 마다 6개 입력
        # 3. 난수(추첨번호 - 6개) 생성
        # 4. 한 게임 마다 등수 출력


# 1. 엘레베이터 알고리즘 ## 1.
def elevator(press):
    print(" %d층 입니다 " %press)

elevator(3)

# 2. 신호등 알고리즘   ## 2. 코드 작성이 아닌 순서도(알고리즘) 작성 이었습니다.
def RtoG(now1):
    now1 = "green"
def GtoR(now1):
    now1 = "red"
def traffic_light(now1):
    import time
    import threading
    if now1 == "red":
        threading.Timer(60, RtoG).start()
    elif now1 == "green":
        threading.Timer(60, GtoR).start()

# 3. 로또 구매 프로그램
def lottogame(count):
    import random
    put, rand = list(), list()
    for i in range(1, count):
        put.append(input())
    rand.append(random.randrange(1, 46))
    howmany = set(set(put).intersection(set(rand)))
    if len(howmany) == 6:
        print(" 1등 입니다 ")
    elif len(howmany) == 5:
        print(" 3등 입니다 ")
    elif len(howmany) == 4:
        print(" 4등 입니다 ")
    elif len(howmany) == 3:
        print(" 5등 입니다 ")
    else:
        print(" 미당첨 입니다 ")
