# Fungtional Programming
Adalah pemrograman yang berbasis fungsi

    
    fibonacci = (lambda n, first=0, second=1: "" if n == 0 else str(first) + "\n" + fibonacci(n - 1, second, first + second))
    print(fibonacci(10), end="")

    # Output
    # 0
    # 1
    # 1
    # 2
    # 3
    # 5
    # 8
    # 13
    # 21
    # 34
    

    
    fibonacci = (lambda n, first=0, second=1:[] if n == 0 else [first] + fibonacci(n - 1, second, first + second))
    print(fibonacci(10))

    # Output
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    

