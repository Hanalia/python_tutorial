# 리스트(List)는 여러 개의 값을 하나의 변수에 저장할 수 있는 자료형입니다.
# 리스트는 대괄호([])로 감싸고, 각 요소는 쉼표(,)로 구분합니다.

# 빈 리스트 생성
empty_list = []

# 숫자 리스트 생성
numbers = [1, 2, 3, 4, 5]

# 문자열 리스트 생성
fruits = ["apple", "banana", "cherry"]

# 리스트의 요소에 접근하기
# 리스트의 인덱스는 0부터 시작합니다.
first_fruit = fruits[0]  # "apple"
second_fruit = fruits[1]  # "banana"

# 리스트의 요소 변경하기
fruits[0] = "avocado"  # ["avocado", "banana", "cherry"]

# 리스트에 요소 추가하기
fruits.append("date")  # ["avocado", "banana", "cherry", "date"]

# 리스트에서 요소 제거하기
fruits.remove("banana")  # ["avocado", "cherry", "date"]

# 리스트의 길이 구하기
length = len(fruits)  # 3

# 리스트 반복문 사용하기
for fruit in fruits:
    print(fruit)
    # avocado
    # cherry
    # date