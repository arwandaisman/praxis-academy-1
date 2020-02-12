## Unit Testing

![](https://github.com/dummytarget/praxis-academy/blob/master/img/m-2/h-3/01.png)

Penjelasan
1. rootdir (Root directory) adalah directory tempat unit yang akan di test dan terdapat 10 item yg akan diuji
2. terdapat 5 file kasus yang akan di test
```
    test_kasus01.py ...                                                                                                                                                                    
    test_kasus02.py FF.                                                                                                                                                                       
    test_kasus03.py .                                                                                                                                                                         
    test_kasus04.py ..                                                                                                                                                                        
    test_kasus05.py .    
 ```
3. titik setelah nama folder adalah banyak fungsi yang akan diuji, pada test_kasus02 terjadi 2 Filures test, yang artinya ada 2 fungsi yang bermasalah pada file tersebut
4. error yang terjadi yaitu pada bagian class TestATM.tes_balance, yang dimana unit test mengatakan bahwa 
```
AssertionError: 90 != 80
```
yang artinya input 90 tidak sama hasilnya dengan output 80
5. error yang kedua pada bagian class TestATM.test_deposit `AssertionError: 50 != 90`, input 50 tidak sama outputnya dengan 90
