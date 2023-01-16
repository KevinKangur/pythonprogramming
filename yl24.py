def upc_check_digit(upc):
    check_sum = 0
    for i in range(0, 11, 2):
        check_sum += int(upc[i])

    check_sum *= 3

    for i in range(1, 10, 2):
        check_sum += int(upc[i])

    reminder = check_sum % 10

    if (reminder):
        check_sum = 10 - reminder
    else:
        check_sum = 0

    print(check_sum)


upc_check_digit('042100005264')
upc_check_digit('036000291452')
upc_check_digit('12345678910')