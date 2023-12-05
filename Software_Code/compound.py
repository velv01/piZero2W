def compound_interest(initial, rate, years):
 
    FV = initial * (pow((1 + rate / 100), years))
    interest = FV - initial
    print("Compound interest is: %.5f" % interest)
 
IV = float(input("Enter initial value: "))
i = float(input("Enter interest rate :"))
yr = float(input("Enter number of years: "))

compound_interest(IV, i, yr)


 




   


   
   




 



    

    
    

