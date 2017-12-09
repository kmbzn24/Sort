#일반적인 Factorial 함수
def fac(n) :
    output = 1;
    for i in range(1, n + 1) :
        output *= i;
    return output;

#재귀함수를 이용한 Factorial 구현
def fac_recursion(n) :
    if (n == 1) :
        return 1;
    else :
        return .n * fac_recursion(n - 1);
