def insertion_sort(list) :
    for i in range(0, len(list) - 1) :
        sav = list[i + 1];
        for j in range(0,i + 1) :
            if (sav < list[i - j]) :
                list[i - j + 1] = list[i - j];
                list[i - j] = sav;
            else :
               break;
    for i in range(0, len(list)) :
        print(list[i]);

list = []; #리스트 생성
n = int(input()); #1번째 줄에서 리스트의 길이값을 입력받는다.
for i in range(0, n) :
    list += [int(input())]; #2번째 줄부터 n + 1번째 줄까지 값을 받고 리스트로 만든다.

insertion_sort(list); #정의된 함수 실행
