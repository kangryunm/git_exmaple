'''
시작 시각 : 17:00
종료 시각 : 18:00


다음 코드에서, 출력되는 결과값이 왜 실제 출력되어야 하는 결과값보다 작은지 설명하시오.

해당 문제점을 해결하기 위해 사용해야 하는 해결책을 서술하고,
해당 개념을 자율차 코드에 적용하였을 때
1) 어느 부분에 적용할 수 있을지,
2) 이를 통해 어떤 이점을 얻을 수 있는지
서술하시오.

(Optional) 아래 코드의 실행 결과값이 실제 출력되어야 하는 결과값과 동일하게 출력되도록 변경하시오.

*** Write Your Answer Below ***
여러 쓰레드를 동시에 사용하는 경우, 두 개 이상의 쓰레드가 동일한 함수를 동시에 호출하게 되면서
실제로 함수가 실행되어야 할 횟수보다 더 적은 횟수가 실행되는 문제가 발생하였다.
이를 해결하기 위해서 쓰레드 동기화가 필요하다.

1) 차선 인식 분야에서 histogram으로 흰 픽셀 값들의 합을 구할 때 쓰레딩을 적용할 수 있다.
2) 파이썬에서 쓰레딩은 I/O연산과 같은 반복문 연산에 있어서 성능이 드러나기에
픽셀들의 값의 합을 구할 때 쓰레딩을 구현하면 연산 속도면에서 이점을 얻을 수 있다고 생각한다.


*** Your Answer Ends Here ***
'''


from threading import Thread


class Count:
    def __init__(self):
        self.count = 0

    def add_offset(self, offset):
        self.count += offset


def worker(idx, limit, count_obj):
    print(idx)
    for _ in range(limit):
        count_obj.add_offset(1)


def run_threads(func, thread_num, limit, count_obj):
    threads = []
    for i in range(thread_num):
        args = (i, limit, count_obj)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


limit = 10 ** 6
thread_num = 3
count = Count()
run_threads(worker, thread_num, limit, count)
print(f"Result should be {thread_num * limit}, but the total count is {count.count}")
