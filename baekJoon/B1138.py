# 1138번 
"""
문제: N명의 사람이 키 순서대로 줄을 서고 있다. 
각 사람의 앞에 자기보다 키가 큰 사람이 몇 명이 있는지 주어질 때, 줄을 서는 순서를 구하는 프로그램을 작성하시오.
"""

"""
N명의 사람들의 키 순서와 그들이 기억하는 왼쪽에 자신보다 큰 사람의 수를 기반으로 줄을 서는 순서를 구하는 문제
"""

def arrange_people(N, bigger_counts):
    line = [0] * N
    
    for person in range(1, N+1):
        count = bigger_counts[person-1]
        empty_spaces = 0
        for i in range(N):
            if line[i] == 0:  
                if empty_spaces == count:
                    line[i] = person 
                    break
                empty_spaces += 1
    return line

N = int(input())
bigger_counts = list(map(int, input().split()))  

result = arrange_people(N, bigger_counts)
print(*result)
