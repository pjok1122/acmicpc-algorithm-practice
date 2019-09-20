'''
LIS(Longest increasing subsequence)라고 알려진 문제.

[10, 15, 10, 30, 20, 50] 이 있다면, LIS는 [10, 20, 30, 50] 입니다.

이 문제를 DP로 풀기 위해서는 DP의 의미를 명확하게 정의해야 합니다.

DP[n] := n번째 수를 부분수열의 마지막으로 하는 '가장 긴 부분수열의 길이'
예를 들어, DP[4]를 생각해봅시다. 주어진 수열의 4번째 수는 20입니다.

따라서 20으로 끝나는 가장 긴 부분수열의 길이를 생각해보면,

(1) arr[0] --> arr[1] --> arr[4]
(2) arr[1] --> arr[4]
(3) arr[2] --> arr[4]

이 세 가지가 있겠네요.

이 중 가장 긴 수열은 (1)이므로 DP[4] = 3 입니다.

이 논리를 수식으로 정리하면 다음과 같습니다.

DP[i] = max(DP[j]+1) (j<i && arr[j]<arr[i])

결과적으로 LIS는 max(DP[i])가 됩니다. 각각의 DP[i]의 의미가 i번째 수로 끝나는 부분 수열의 최대 길이이기 때문에, 모든 수열이 카운팅 됐다고 볼 수 있죠.

[부가 설명]

arr[4]는 arr[3], arr[2], arr[1], arr[0] 중 어떤 수로부터 부분 증가 수열을 이룰 것입니다.

그 수가 arr[1]이라면, arr[1]을 마지막으로 하는 부분수열의 길이가 DP[1] 이기 때문에 DP[4] = DP[1]+1이 되는 원리입니다.

다소 복잡하게 느껴질 수도 있지만 사실 원리는 간단합니다. 아이디어를 떠올리기가 어려워서 그렇지요..

'''

N = int(input())
arr =[0]+list(map(int, input().split()))
dp = [0]*(N+1)

for i in range(1,N+1):
    dp[i] = 1

    for j in range(1,i):
        if arr[i] > arr[j] and dp[i]<dp[j]+1:
            dp[i] = dp[j]+1

print(max(dp))
    
