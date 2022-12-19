"""
Compound interest calculator for monthly addition
standard formula: Amount = Principal ( 1 + interest rate ) ^ years
formula: standard formula but add same Principal after every year
"""


def this_year_addition(principal, base):
    """
    add yearly contribution to principal
    :param principal: the current principal
    :param base: the additional principal
    :return: the actual current principal
    """
    new_base = principal + base
    return new_base


def compounded_interest(principal, interest):
    """
    get yearly interest gain of the new principal
    :param principal: yearly principal
    :param interest: yearly interest
    :return: the interest gain from the year
    """
    interest_gain = float("{:.2f}".format(float(principal * interest)))
    return interest_gain


def new_principal(principal, interest_gain):
    """
    get the new principal of the year
    :param principal: the current principal
    :param interest_gain: this year's interest gain
    :return: the new principal for next year
    """
    return float("{:.2f}".format(float(principal + interest_gain)))


def today_value_of_outcome(principal, year, inflation):
    """
    get the present value of the future value
    :param principal: future value
    :param year: how many years to de-compound
    :param inflation: the inflation rate
    :return:
    """
    present_value = float(principal / pow(1 + inflation, year))
    return float("{:.2f}".format(present_value))


def simple_cal():
    """
    input yearly contribution with interest rate and inflation rate for a number of years.
    :return: total contribution, inflated value, future value, gain in percentage.
    """
    principal = inflation_principal = 0
    base = float("{:.2f}".format(float(input("Yearly Addition: $"))))
    interest = float("{:.2f}".format(float(input("Interest in percentage: ")) / 100))
    inflation = float("{:.2f}".format(float(input("Interest in inflation: ")) / 100))
    year = int(input("Years of holding: "))
    total_contribution = base * year

    for i in range(year):
        """ interest gain """
        principal = this_year_addition(principal, base)
        interest_gain = compounded_interest(principal, interest)
        principal = new_principal(principal, interest_gain)
        """ inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        inflation_gain = compounded_interest(inflation_principal, inflation)
        inflation_principal = new_principal(inflation_principal, inflation_gain)

    print(f"This is your total contribution: ${total_contribution}!")
    print(f"This is the inflated value: ${inflation_principal}!")
    print(f"This is the future value: ${principal}!")
    print(f"Gain vs base {float('{:.2f}'.format((principal / total_contribution) - 1)) * 100}%")
    print(f"Gain vs inflation {float('{:.2f}'.format((principal / inflation_principal) - 1)) * 100}%")
    print("Thank you for using this CLI service :-)")


def complex_cal():
    principal = inflation_principal = 0
    total_contribution = 0
    year = int(input("Years of holding: "))
    for i in range(year):
        """ user input parameter """
        base = float("{:.2f}".format(float(input("Addition of the year: $"))))
        interest = float("{:.2f}".format(float(input("Interest in percentage: ")) / 100))
        inflation = float("{:.2f}".format(float(input("Interest in inflation: ")) / 100))
        total_contribution += base

        """ interest gain """


def main():
    options = int(input("select\n1 for simple calculator\n2 for complex calculator\n--> "))
    if options == 1:
        simple_cal()
    if options == 2:
        pass
    else:
        main()


if __name__ == '__main__':
    while True:
        try:
            main()
            break
        except ValueError:
            print("Invalid input, please enter numbers only")
