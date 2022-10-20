from collections import Counter
def solution(X, Y):
    answer = ''
    a = Counter(X)
    b = Counter(Y)
    
    for i in range(9,-1,-1) :
        m = min(a[str(i)],b[str(i)])
        answer += (str(i)*m) 
    
    if not answer : return "-1"
    if answer[0] == '0' : return "0"
    return answer