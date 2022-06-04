names = ["유재석", "강호동", "신동엽", "서장훈", "김희철"]

def delete_data(position) :
        
	if position < 0 or position > len(names) :
		print("데이터를 삭제할 범위를 벗어났습니다.")
		return

	kLen = len(names)
	names[position] = None	# 데이터 삭제				# 1) 해당 데이터를 삭제한다.
    
	for i in range(position+1, kLen) :					# 2) 삭제한 데이터 기준 오른쪽 데이터들을 앞으로 한 칸씩 이동시킨다.
		names[i-1] = names[i]
		names[i] = None	# 배열의 맨 마지막 위치 삭제		# 3) 배열 맨 끝 자리를 제거한다.

	del(names[kLen-1])


delete_data(1)
print(names)
delete_data(3)
print(names)

