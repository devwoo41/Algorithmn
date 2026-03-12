# 1부터 n까지 정수의 합 구하기 3(가우스 공식)
def gaus_add(n):
    return n * (n + 1) // 2

# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a : Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum
'''
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')
'''
# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)

    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
'''
if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬한다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    reverse_array(x)

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
'''

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while문)"""
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i 
        i += 1
'''
if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int((input(f'x[{i}]: ')))

    ky = int(input('검색할 값을 입력하세요.: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
'''