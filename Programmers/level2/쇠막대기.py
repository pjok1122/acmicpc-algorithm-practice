'''
여러 개의 쇠막대기를 레이저로 절단하려고 합니다. 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자릅니다. 쇠막대기와 레이저의 배치는 다음 조건을 만족합니다.

- 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있습니다.
- 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓습니다.
- 각 쇠막대기를 자르는 레이저는 적어도 하나 존재합니다.
- 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않습니다.
아래 그림은 위 조건을 만족하는 예를 보여줍니다. 수평으로 그려진 굵은 실선은 쇠막대기이고, 점은 레이저의 위치, 수직으로 그려진 점선 화살표는 레이저의 발사 방향입니다.

image0.png

이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있습니다.

(a) 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 '()'으로 표현합니다. 또한 모든 '()'는 반드시 레이저를 표현합니다.
(b) 쇠막대기의 왼쪽 끝은 여는 괄호 '('로, 오른쪽 끝은 닫힌 괄호 ')'로 표현됩니다.
위 예의 괄호 표현은 그림 위에 주어져 있습니다.
쇠막대기는 레이저에 의해 몇 개의 조각으로 잘리는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘리고, 이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘립니다.

쇠막대기와 레이저의 배치를 표현한 문자열 arrangement가 매개변수로 주어질 때, 잘린 쇠막대기 조각의 총 개수를 return 하도록 solution 함수를 작성해주세요.

제한사항
arrangement의 길이는 최대 100,000입니다.
arrangement의 여는 괄호와 닫는 괄호는 항상 쌍을 이룹니다.
입출력 예
arrangement	return
()(((()())(())()))(())	17

[문제 풀이]

여는 괄호'('가 쌓일 수록 막대기가 누적되고, 레이저에 분리되는 개수가 늘어나는 것을 직관적으로 파악하는 것이 최우선이다.

파악하고나면 알고리즘을 명확하게 만드는 것은 그다지 어렵지 않다.

1. '('괄호라면 스택에 넣고, 괄호의 개수를 1 증가시킨다.
2. ')'괄호라면 스택에서 제거하고 괄호의 개수를 1낮춘다.
3. 바로 이전에 만난 괄호가 '('라면 레이저를 의미하기 때문에 스택에 있는 괄호의 개수만큼 쇠막대기가 분리될 것이다. 따라서 answer += open_count 연산을 수행한다.
4. 바로 이전에 만난 괄호가 ')'라면 쇠막대기의 끝을 의미하기 때문에 answer = answer + 1을 수행한다.

[좋은 풀이]

위의 풀이는 바로 이전에 만난 괄호를 기억하고 있어야한다는 번거로움이 있다. 기억해야 하는 이유는 레이저와 쇠막대기의 끝을 구분하기 위함이다.
따라서 레이저 자체를 처음부터 찾아내면 문제를 더욱 쉽게 풀 수도 있다.

ex) arrangement.replace('()', '0')

'''


def solution(arrangement):
    stack = []
    open_count = 0
    open = '('
    close = ')'

    answer = 0
    for i in arrangement:
        if(i == open):
            stack.append(i)
            open_count += 1
            before = open
        elif(i == close):
            stack.pop()
            open_count -= 1
            answer = answer + (open_count if before == open else 1)
            before = close
    return answer


print(solution("()(((()())(())()))(())"))
print(solution("((())()(()))"))
