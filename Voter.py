voter=('Amit',20,'Sumit',40,'Rajit',12,'Lalit',34,'Dalit',17)
for i in range(len(voter),2):
    if voter[i+1]>=18:
        print((voter[i]),"Valid Voter")
    else:
        print((voter[i]),"Invalid Voter")
