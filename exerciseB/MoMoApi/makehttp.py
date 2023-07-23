from pay import PayClass

callPay = PayClass.momopay(500, EUR, help101, "phonenumber", askingtopay)
print(callPay["response"])