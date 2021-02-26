from bankaccount import MinimumBalanceAccount

accountMin = MinimumBalanceAccount(1500, 1000)

result = accountMin.try_withdraw(150000)

if(result.is_ok()):
    print(result.message)
else:
    print(result.message, "tralalala poszło źle")