amount=int(input())
count=0
if(amount>500):
    count=amount//500
    amount=amount%500
if(amount>200):
    count=count+amount//200
    amount=amount%200
if(amount>100):
    count=count+amount//100
    amount=amount%100
if(amount>50):
    count=count+amount//50
    amount=amount%50
if(amount>20):
    count=count+amount//20
    amount=amount%20
if(amount>10):
    count=count+amount//10
    amount=amount%10
print(count)
