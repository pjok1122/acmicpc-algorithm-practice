'''
문제 설명
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
스파이는 하루에 최소 한 개의 의상은 입습니다.
입출력 예
clothes	return
[[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]	5
[[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]	3
입출력 예 설명
예제 #1
headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.

1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses
예제 #2
face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.

1. crow_mask
2. blue_sunglasses
3. smoky_makeup

[문제 풀이]

해시맵을 이용하면 의상의 종류에 따라서 데이터를 정돈할 수 있다는 사실은 이미 알고 있다.

그 사실에 입각해서 바로 해시맵으로 정돈하지 말고, 그 이후의 과정을 생각해보자.

데이터가 해시맵으로 잘 정돈되어있다면, ['headgear' : ['blue', 'red'], 'face': ['mask', 'sunglasses', 'makeup']] 과 같은 상태라고도 볼 수 있다.

이 때, 몇 가지의 경우가 있는지에 대해서 코드로 계산하려 들지 말자.

headgear에서 선택할 수 있는 방법은 [blue, red, 선택안함] 총 3가지 방법이 있다.
face에서 선택할 수 있는 방법은 [mask, sunglass, makeup, 선택안함] 총 4가지 방법이 있다.

이 둘을 곱했을 때, 의상을 선택할 수 있는 모든 종류가 나온다. 여기서 [선택안함, 선택안함]은 외출이 불가능한 복장이므로 제외해줘야 한다. 즉, 정답에서 1을 빼주면 된다.

최종적으로 보면, 우리는 hashMap 전체가 필요하지 않다. 왜냐면 각 key에 대한 value가 몇 개 였는지만 체크하면 되기 때문이다.

따라서 dic['headgear'] = 2 , dic['face'] = 2와 같은 방법으로 정리하는 것이 더 문제에는 적합하다.
'''


def solution(clothes):
    dic = {}
    answer = 1

    for cloth in clothes:
        if cloth[1] in dic.keys():
            dic[cloth[1]] += [cloth[0]]
        else:
            dic[cloth[1]] = [cloth[0]]

    for item in dic.values():
        answer *= len(item)+1

    return answer - 1


print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

print(solution([["crow_mask", "face"], [
      "blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
