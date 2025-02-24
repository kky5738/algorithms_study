# gpt의 도움을 받았습니다
import sys

def course_registration(max_capacity, student_actions):
    queue = dict()  # 중복을 제거하면서 순서 유지

    for student in student_actions:
        if student in queue:
            queue.pop(student)  # 기존에 있던 경우 삭제
        queue[student] = None  # 다시 삽입 (맨 뒤로 이동)

    # 수강 신청 확정자 결정
    confirmed_students = list(queue.keys())[:max_capacity]

    return confirmed_students

# 입력 처리
max_capacity, n = map(int, sys.stdin.readline().split())  # 첫 번째 줄 입력
student_actions = [sys.stdin.readline().strip() for _ in range(n)]  # 학번 리스트 입력

# 결과 출력
for student in course_registration(max_capacity, student_actions):
    print(student)
