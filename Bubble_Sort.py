def bubble_sort(list) :
    for i in range(0, len(list) - 1) :
        for j in range(0, len(list) - 1 - i) :
            if (list[j] > list[j + 1]) :
                sav = list[j];
                list[j] = list[j + 1];
                list[j + 1] = sav;
    for i in range(0, len(list)) :
        print(list[i]);

list = []; #리스트 생성
n = int(input()); #1번째 줄에서 리스트의 길이값을 입력받는다.
for i in range(0, n) :
    list += [int(input())]; #2번째 줄부터 n + 1번째 줄까지 값을 받고 리스트로 만든다.

bubble_sort(list); #정의된 함수 실행
