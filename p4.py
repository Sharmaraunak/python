try:
    xr= float(input("enter the rate: "))
    xh = float(input("Enter hours:"))
    extra=0
    pay1=pay2=0
    if xh>40:
        extra=xh-40
        pay1=extra*1.5*xr

    pay2=40*xr
    pay=pay1+pay2
    print('pay:',pay)
except:
    print("error,enter numeric input")
