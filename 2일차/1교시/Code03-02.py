names = ["유재석", "강호동", "신동엽", "서장훈", "김희철"]

def insert_data(position, friend) :

	if position < 0 or position > len(names) :
		print("데이터를 삽입할 범위를 벗어났습니다.")
		return
    
	names.append(None)   # 빈칸 추가							# 1) 배열 맨 끝 자리를 확보한다.
	kLen = len(names)       # 배열의 현재 크기

	for i in range(kLen-1, position, -1) :
		names[i] = names[i-1]								#2) 삽입할 위치 기준 오른쪽 데이터들을 뒤로 한 칸씩 이동시킨다.
		names[i-1] = None 

	names[position] = friend   # 지정한 위치에 친구 추가		# 3) 빈 자리에 데이터를 삽입한다.

insert_data(2, '하하')
print(names)
insert_data(6, '박명수')
print(names)
