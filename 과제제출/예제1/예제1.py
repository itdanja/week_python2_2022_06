
# 잘하셨습니다!!! 첨삭!!
    # 1. 28번줄 : 자동으로 현재시간이 들어가도록 합니다.
    # 2. 62번줄

import datetime

def start(number):
    while True:
        select = int(input('1.(손님)대기 등록 2.(손님)어플에서 대기 등록 3.[관리자]입장'))
        if select == 1:
            print("(손님) 대기 등록 합니다.")

            waiting_data0 = [['유재석,01012345678,2,datetime.time(10, 23, 10)']]

            waiting_data1 = []

            for i in range(number):
                name = str(input('이름을 입력하세요: '))
                waiting_data1.append(name)

                phone_number = int(input('전화번호를 입력하세요: '))
                waiting_data1.append(phone_number)

                people_number = int(input('인원수를 입력하세요: '))
                waiting_data1.append(people_number)



                time =
                waiting_data1.append(time)

            waiting_data2 = []
            waiting_data2.append(waiting_data1)

            waiting_data0.append(waiting_data2)

            index = waiting_data0.index(waiting_data2)

            print('웨이팅 대기 순서: ', index)

            print(waiting_data0)




        elif select == 2:
            print("(손님) 어플 대기 등록 합니다.")

            waiting_data3 = []

            for k in range(number):
                name2 = str(input('이름을 입력하세요: '))
                waiting_data3.append(name2)

                phone_number2 = int(input('전화번호를 입력하세요: '))
                waiting_data3.append(phone_number2)

                people_number2 = int(input('인원수를 입력하세요: '))
                waiting_data3.append(people_number2)

                import datetime

                time2 = datetime.time(11, 10, 30)
                waiting_data3.append(time2)

            waiting_data4 = []
            waiting_data4.append(waiting_data3)

            if time2 != time:
                waiting_data0.insert(1, list(waiting_data4))

            index2 = waiting_data0.index(waiting_data4)

            print('웨이팅 대기 순서: ', index2)

            print(waiting_data0)



        elif select == 3:
            print("(관리자) 대기번호 1 입장.")

            for f in range(number):
                del waiting_data0[0]

                print(waiting_data0)



        else:
            print("알수 없는 번호 입니다.")

            break


start(1)


