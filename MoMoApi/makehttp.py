from pay import PayClass

callPay = PayClass.momopay("500", "EUR", "help101", "#", "rqst2pay")
print(callPay["response"])