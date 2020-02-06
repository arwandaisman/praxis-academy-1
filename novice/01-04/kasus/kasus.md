Algoritma Program
Class : 
1. Deposit Class : menyetor uang (nabung)

       
       -setDeposit => memberikan value berapa banyak nabung
       -getDeposti => mengambil value berapa banyak nabung
       
       
 2. Withdraw Class : menarik uang
       ```
       -setWithdraw => memberikan value berapa banyak narik
       -getWithdraw => mengambil value berapa banyak narik
       ```
 3. Balance Inquiry Class : info saldo
       ```
       -setBalance => memberikan value berapa banyak saldo
       -getBalance => mengambil value berapa banyak saldo
       ```
 4. ATM Machine Class : main program
       ```
       -checkBalance()
           -getBalance()
           
       -withdrawMoney()
       if Balance == 0
              unable to Withdraw
       elif Balance <=500
              uang ga cukup untuk ditarik 
       elif Withdraw > Balance 
              penarikan melebihi saldo
       else Balance = Balance - Withdraw #saldo dikurangi
              penarikan berhasil sebanyak Withdraw
              
       -depositMoney()
              kamu deposit sebanyak . . .
              
        1. Deposit
        2. Withdraw
        3. Balance Inquiry
        4. Exit
        >4. Try another transaction
              1. yes; 2. no
        
        input selain angka masukkan exception handling untuk menanganinya
       ```
       



