# 과제 : 식당 웨이팅 프로그램 구현 [ 버전 : 1.선형리스트 버전  2. 연결리스트 버전 ]
    # 요구사항
        # 식당이 오픈 전
        # 1. 이름 , 전화번호 , 인원수 입력받는다 . [ 현재시간 자동 입력받기 ]
        # 2. 등록된 웨이팅를 리스트에 담는다 .
        # 3. 사용자에게 순서대기 번호 알려준다. [ 인덱스번호 혹은 노드 순서번호 ]
        # 변수 요구 : 이미 시간대 별로 웨이팅 이 존재하는데 중간에 예약이 된다..
        #       어플 예약 : 이름 , 전화번호 , 인원수 , 예약 시간 입력받는다 .
        #       어플 예약 등록 되었을때 예약 시간보다 더 큰 시간은 뒤로 한칸씩 대기번호 증가
        # 4. 관리자가 입장 하면  가장 앞에 있는 순서대기부터 삭제처리 한다. [ 한칸씩 인덱스,노드 당겨짐 ]
        # 예)
        #       강호동 030 3 1:13
        #       신동엽 010 2 2:20
        #                           어플 예약 : 유재석 020 2 1:30
        #       강호동 유재석 신동엽
        # 예)
        #     입장시 강호동부터 입장처리 [ 삭제 ]
        # 5. 1. 웨이팅 등록   2. [관리자]입장

# 선형리스트ver.
def waiting_linear_list() :
    import datetime
    now = datetime.datetime.now()
    AllList, one = list(), list()
    while True :
        select = int( input( ' 1.(손님)대기 등록  2.(손님)어플 대기 등록  3.[관리자]입장 ') )
        if select == 1 :
            print("*(손님) 대기 등록 합니다. *")
            one.append(str(input())) # 이름
            one.append(int(input())) # 전화번호
            one.append(int(input())) # 인원수
            one.append(now.strftime('%H:%M:%S')) # 예약 시간
            AllList.append(one)
            one = []
        elif select == 2:
            print("*(손님) 어플 대기 등록 합니다. *")
            one.append(str(input()))  # 이름
            one.append(int(input()))  # 전화번호
            one.append(int(input()))  # 인원수
            one.append(now.strftime('%H:%M:%S')) # 예약 시간
            AllList.append(one)
            one = []
            for i in range(0, len(AllList), 1):  # i : 비교기준
                for j in range(0, len(AllList), 1):  # j : 비교대상
                    if AllList[i][3] > AllList[j][3]:  # i의 시간과 j의 시간 비교
                        # i 인덱스 데이터 와 j의 인덱스 데이터 교환[ swap ]
                        temp = AllList[i]
                        AllList[i] = AllList[j]
                        AllList[j] = temp
        elif select == 3:
            print("*(관리자) 대기번호 1 입장. *")
            count = len(AllList)
            AllList[0] = None
            for i in range(1, count):
                AllList[i-1] = AllList[i]
                AllList[i] = None
            del (AllList[count-1])
        else :
            print("*알수 없는 번호입니다. 다시 입력해주세요~ ")
waiting_linear_list()


# 연결리스트ver.
def waiting_signly_linked_list():
    import datetime
    now = datetime.datetime.now()
    global head , current , pre
    class Node( ) : # Node 라는 이름으로 클래스 선언
        def __init__(self):     # Node 구조
            self.data = None        # 필드1 = 데이터
            self.link = None        # 필드2 = 링크
    while True:
        select = int(input(' 1.(손님)대기 등록  2.(손님)어플 대기 등록  3.[관리자]입장 '))
        if select == 1:
            print("*(손님) 대기 등록 합니다. *")
            name = str(input())  # 이름
            phone = int(input())  # 전화번호
            howmany = int(input())  # 인원수
            times = now.strftime('%H:%M:%S')  # 예약 시간
            node = Node() # 노드 객체 선언
            node.data = (name, phone, howmany, times) # 노드 데이터 생성
            if head == None:
                head = node # 헤드 생성
            else:
                head.link = node
        elif select == 2:
            print("*(손님) 어플 대기 등록 합니다. *")
            name = str(input())  # 이름
            phone = int(input())  # 전화번호
            howmany = int(input())  # 인원수
            times = now.strftime('%H:%M:%S')  # 예약 시간
            node = Node() # 노드 객체 선언
            node.data = (name, phone, howmany, times) # 노드 데이터 생성
            while current.link != None:  # 마지막 노드까지 반복처리
                pre = current  # 이전노드에 현재노드 대입
                current = current.link  # 현재노드에 다음노드 대입
                if current.data[3] > node.data[3]:  # 만약에 다음노드와 새로입력받음 비교
                    pre.link = node  # 이전노드에 새로운노드
                    node.link = current  # 새로운노드 - > 다음노드
                    return
        elif select == 3:
            print("*(관리자) 대기번호 1 입장. *")
            ### 노드를 이러한 입력값을 계속받는 함수에서는 node1, node2,node3 이렇게 하나하나 지정할수있는게 아니라서 어떻게 2번째, 3번째 노드를 표현해야할지 모르겠습니다"
            node2.link = node3.link
            del(node)
        else:
            print("*알수 없는 번호입니다. 다시 입력해주세요~ ")
waiting_signly_linked_list()