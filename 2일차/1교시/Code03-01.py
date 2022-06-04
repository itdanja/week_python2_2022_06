
"""
	선형 리스트[Linear List]
		--> 데이터를 일정한 순서로 나열한 자료구조
		--> 입력 순서대로 저장하는 데이터에 적당
		--> 배열 사용
		--> 선형 리스트는 메모리에서도 차례로 저장된다.
	또한, 요즘 같은 시기에 코로나 검사를 받기 위해 선별 진료소에 줄을 선 경우도 해당된다.
"""

names = []          # 빈 배열

def add_data(friend) :
        
	names.append(None)
	kLen = len(names)
	names[kLen-1] = friend

add_data('유재석')
add_data('강호동')
add_data('신동엽')
add_data('서장훈')
add_data('김희철')

print(names)


