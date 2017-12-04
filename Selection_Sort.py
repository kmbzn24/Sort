def selection_sort(array) :
    for i in range(0, len(array)) :
        min = float("inf");
        for j in range(i, len(array)) :
            if (array[j] < min) :
                min = array[j];
                loc = j;
        sav = array[i];
        array[i] = min;
        array[loc] = sav;
    for i in range(0, len(array)) :
        print(array[i]);

list = []; #리스트 생성
n = int(input()); #1번째 줄에서 리스트의 길이값을 입력받는다.
for i in range(0, n) :
    list += [int(input())]; #2번째 줄부터 n + 1번째 줄까지 값을 받고 리스트로 만든다.

selection_sort(list); #정의된 함수 실행
