def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)

        else:
            binary = '0' + bin(num)[2:]
            
            idx = -1
            for i in range(len(binary) - 1, -1, -1):
                if binary[i] == '0':
                    idx = i
                    break
                    
            binary = binary[:idx] + '10' + binary[idx+2:]
            answer.append(int(binary, 2))
            
    return answer