input = __import__('sys').stdin.readline

N, Q = map(int, input().rstrip().split())
a_list = list(map(int, input().rstrip().split()))
q_list = [list(map(int , input().rstrip().split())) for i in range(Q)]
prefix_Q_lsit = [0] * (N + 1)
result = 0

for i in range(1, N + 1) :
    prefix_Q_lsit[i] = prefix_Q_lsit[i - 1] ^ a_list[i - 1]

for i in q_list :
    result ^= prefix_Q_lsit[i[1]] ^ prefix_Q_lsit[i[0] - 1] 

print(result)