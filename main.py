"""
Compound interest calculator with yearly addition option
"""
from os import system
from sys import exit as sys_exit

global option, final


def clear():
    """
    clear screen
    :return: none
    """
    system("cls||clear")


def this_year_addition(principal, base):
    """
    add yearly contribution to principal
    :param principal: the current principal
    :param base: the additional principal
    :return: the actual current principal
    """
    new_base = principal + base
    return new_base


def interest_gain(principal, interest):
    """
    get yearly interest gain of the new principal
    :param principal: yearly principal
    :param interest: yearly interest/dividend
    :return: the interest gain from the year
    """
    return float("{:.2f}".format(float(principal * interest)))


def new_principal(principal, interest_gained):
    """
    get the new principal of the year
    :param principal: the current principal
    :param interest_gained: this year's interest gain
    :return: the new principal for next year
    """
    return float("{:.2f}".format(float(principal + interest_gained)))


def today_value_of_outcome(principal, year, inflation):
    """
    get the present value of the future value
    :param principal: future value
    :param year: how many years to de-compound
    :param inflation: the inflation rate
    :return: present value of future growth value
    """
    return float("{:.2f}".format(float(principal / pow(1 + inflation, year + 1))))


def inflation_cal(principal, inflation):
    """
    Inflation gain if contribution is cash and not invested
    :param principal: principal before inflation of the year
    :param inflation: inflation of the year
    :return: principal after inflation
    """
    inflation_gain = interest_gain(principal, inflation)
    return new_principal(principal, inflation_gain)


def simple_or_dynamic_interest_calculator_input():
    """
    same user input for simple/dynamic interest calculator
    :return: base, interest, inflation
    """
    print("|################################|")
    print("| User to input                  |")
    print("| --> Yearly Addition            |")
    print("| --> Holding gain in percentage |")
    print("| --> Interest in percentage     |")
    print("| --> Interest in inflation      |")
    print("|################################|\n")
    base = float("{:.2f}".format(float(input("Yearly Addition: $"))))
    gain = float("{:.4f}".format(float(input("Holding gain in percentage: ")) / 100))
    interest = float("{:.4f}".format(float(input("Interest in percentage: ")) / 100))
    inflation = float("{:.4f}".format(float(input("Interest in inflation: ")) / 100))
    return base, gain, interest, inflation


def gains_output(total_contribution, inflation_principal, future_principal, this_year, year, interest, gain,
                 present_principal):
    """
    final output result for simple/complex interest calculator
    :param total_contribution: total value inputted
    :param inflation_principal: how total value would become if follow inflation rate
    :param future_principal: how total value would become if follow interest
    :param this_year: current year of result
    :param year: total years
    :param interest: dividend gain
    :param gain: gain/loss for holding on to dear life
    :param present_principal: today worth of the future principal
    :return: print to screen the following:
    --> Total Contribution
    --> Future Value
    --> Inflated Value
    --> Gain
    --> Interest
    --> Future (w|wo Interest) vs Total Contribution
    --> Future (w|wo Interest) vs Inflation
    --> Present Principal (w|wo Interest) vs Total Contribution
    """
    global option, final
    print(f"########## Year {this_year}/{year} result! ##########")
    # start
    print(f"Total Contribution: ${total_contribution}!")
    #
    print(f"Future Value: ${future_principal}!")
    #
    print(f"Present Value: ${present_principal}!")
    #
    print(f"Inflated Value: ${inflation_principal}!")
    #
    if not final:
        print(f"Gain of the year: ${gain}!")
    else:
        print(f"Total Gain: ${gain}!")
    #
    if not final:
        print(f"Interest of the year: ${interest}!")
    else:
        print(f"Total Interest: ${interest}!")
    #
    if total_contribution != 0:
        if (option % 2) == 1:  # no reinvest
            print(f"Future + Interest vs Total Contribution: "
                  f"{float('{:.2f}'.format(float((((future_principal + interest) / total_contribution) - 1) * 100)))}%")
        else:  # reinvest
            print(
                f"Future vs Total Contribution: "
                f"{float('{:.2f}'.format(float(((future_principal / total_contribution) - 1)) * 100))}%")
    else:
        print("Future vs Total Contribution: not relevant")
    #
    if inflation_principal != 0:
        if (option % 2) == 1:  # no reinvest
            print(f"Future + Interest vs Inflation: "
                  f"{float('{:.2f}'.format(float((((future_principal + interest) / inflation_principal) - 1)) * 100))}%")
        else:  # reinvest
            print(
                f"Future vs Inflation: "
                f"{float('{:.2f}'.format(float(((future_principal / inflation_principal) - 1)) * 100))}%")
    else:
        print("Future vs Inflation: not relevant")
    #
    if present_principal != 0:
        if (option % 2) == 1:  # no reinvest
            print(f"Present + Interest vs Total Contribution: "
                  f"{float('{:.2f}'.format(float((((present_principal + interest) / total_contribution) - 1)) * 100))}%")
        else:  # reinvest
            print(f"Present vs Total Contribution: "
                  f"{float('{:.2f}'.format(float(((present_principal / total_contribution) - 1)) * 100))}%")
    else:
        print("Present vs Total Contribution: not relevant")
    # end
    print(f"############# END OF YEAR #############\n")


def simple_compound_interest_no_reinvest():
    """
    input yearly contribution and no reinvestment with interest rate and inflation rate for a number of years.
    :return: view gains_output function
    """
    global final
    future_principal = inflation_principal = total_interest = total_gain = present_principal = 0
    """ user input parameter """
    year = int(input("Years of holding: "))
    base, gain, interest, inflation = simple_or_dynamic_interest_calculator_input()
    total_contribution = base * year
    """ calculation """
    for i in range(year):
        """ new principal """
        future_principal = this_year_addition(future_principal, base)
        """ simple interest dividend """
        interest_gained = interest_gain(future_principal, interest)
        total_interest += interest_gained
        """ holding increment """
        holding_gain = interest_gain(future_principal, gain)
        total_gain += holding_gain
        future_principal = this_year_addition(future_principal, holding_gain)
        """ simple inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        interest_inflation = interest_gained + holding_gain
        inflation_principal = inflation_cal(inflation_principal + interest_inflation, inflation) - interest_inflation
        """ current value """
        present_principal = today_value_of_outcome(future_principal, i, inflation)
    """ final output """
    final = True
    gains_output(total_contribution, inflation_principal, future_principal, year,
                 year, total_interest, total_gain, present_principal)


def simple_compound_gain_reinvest():
    """
    input yearly contribution and reinvestment with interest rate and inflation rate for a number of years.
    :return: view gains_output function
    """
    global final
    future_principal = inflation_principal = total_interest = total_gain = present_principal = 0
    """ user input parameter """
    year = int(input("Years of holding: "))
    base, gain, interest, inflation = simple_or_dynamic_interest_calculator_input()
    total_contribution = base * year
    """ calculation """
    for i in range(year):
        """ new principal """
        future_principal = this_year_addition(future_principal, base)
        """ simple interest gain """
        interest_gained = interest_gain(future_principal, interest)
        total_interest += interest_gained
        future_principal = new_principal(future_principal, interest_gained)
        """ holding increment """
        holding_gain = interest_gain(future_principal, gain)
        total_gain += holding_gain
        future_principal = new_principal(future_principal, holding_gain)
        """ simple inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        interest_inflation = interest_gained + holding_gain
        inflation_principal = inflation_cal(inflation_principal + interest_inflation, inflation) - interest_inflation
        """ current value """
        present_principal = today_value_of_outcome(future_principal, i, inflation)
    """ final output """
    final = True
    gains_output(total_contribution, inflation_principal, future_principal, year,
                 year, total_interest, total_gain, present_principal)


def dynamic_compound_gain_no_reinvest():
    """
    input yearly contribution and no reinvestment with interest rate and inflation rate for a number of years
    dynamically.
    :return: view gains_output function
    """
    global final
    future_principal = inflation_principal = total_interest_gained = total_contribution = total_gain = this_year = \
        present_principal = 0
    """ user input parameter part 1/2 """
    year = int(input("Years of holding: "))
    """ dynamic calculation """
    for i in range(year):
        """ user input parameter part 2/2 """
        base, gain, interest, inflation = simple_or_dynamic_interest_calculator_input()
        total_contribution += base
        """ new principal """
        future_principal = this_year_addition(future_principal, base)
        """ dynamic interest gain """
        interest_gained = interest_gain(future_principal, interest)
        total_interest_gained += interest_gained
        """ holding increment """
        holding_gain = interest_gain(future_principal, gain)
        total_gain += holding_gain
        future_principal = this_year_addition(future_principal, holding_gain)
        """ dynamic inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        interest_inflation = interest_gained + holding_gain
        inflation_principal = inflation_cal(inflation_principal + interest_inflation, inflation) - interest_inflation
        """ current value """
        present_principal = today_value_of_outcome(future_principal, i, inflation)
        """ yearly output """
        this_year += 1
        if this_year != year:
            final = False
            gains_output(total_contribution, inflation_principal, future_principal, this_year,
                         year, interest_gained, total_gain, present_principal)
    """ final output """
    final = True
    gains_output(total_contribution, inflation_principal, future_principal, year,
                 this_year, total_interest_gained, total_gain, present_principal)


def dynamic_compound_gain_reinvest():
    """
    input yearly contribution and reinvestment with interest rate and inflation rate for a number of years dynamically.
    :return: view gains_output function
    """
    global final
    future_principal = inflation_principal = total_interest_gained = total_contribution = total_gain = this_year \
        = present_principal = 0
    """ user input parameter part 1/2 """
    year = int(input("Years of holding: "))
    """ dynamic calculation """
    for i in range(year):
        """ user input parameter part 2/2 """
        base, gain, interest, inflation = simple_or_dynamic_interest_calculator_input()
        total_contribution += base
        """ new principal """
        future_principal = this_year_addition(future_principal, base)
        """ dynamic interest gain """
        interest_gained = interest_gain(future_principal, interest)
        total_interest_gained += interest_gained
        future_principal = new_principal(future_principal, interest_gained)
        """ holding increment """
        holding_gain = interest_gain(future_principal, gain)
        total_gain += holding_gain
        future_principal = new_principal(future_principal, holding_gain)
        """ dynamic inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        interest_inflation = interest_gained + holding_gain
        inflation_principal = inflation_cal(inflation_principal + interest_inflation, inflation) - interest_inflation
        """ current value """
        present_principal = today_value_of_outcome(future_principal, i, inflation)
        """ yearly output """
        this_year += 1
        if this_year != year:
            final = False
            gains_output(total_contribution, inflation_principal, future_principal, this_year,
                         year, interest_gained, total_gain, present_principal)
    """ final output """
    final = True
    gains_output(total_contribution, inflation_principal, future_principal, this_year,
                 year, total_interest_gained, total_gain, present_principal)


def present_value():
    """
    what is the current value of a future amount when taking inflation into account
    :return: current value of future inflated amount
    """
    print("|#######################################|")
    print("| Find current value of a future amount |")
    print("| --> Future Amount                     |")
    print("| --> Years of holding                  |")
    print("| --> Inflation                         |")
    print("|#######################################|\n")
    base = float("{:.2f}".format(float(input("Future Amount: $"))))
    year = int(input("Years of holding: "))
    inflation = float("{:.4f}".format(float(input("Interest in inflation: ")) / 100))
    principal = today_value_of_outcome(base, year, inflation)
    print(f"{year} years into the future the value of ${base} is worth today's ${principal}")


def future_value():
    """
    What is the future value of today value when following inflation
    :return: inflated today value into the future
    """
    print("|################################################|")
    print("| How much the amount is after years of interest |")
    print("| --> Amount                                     |")
    print("| --> Years of holding                           |")
    print("| --> Interest                                   |")
    print("|################################################|\n")
    principal = base = float("{:.2f}".format(float(input("Current Amount: $"))))
    year = int(input("Years of holding: "))
    inflation = float("{:.4f}".format(float(input("Interest in inflation: ")) / 100))
    for i in range(year):
        principal = inflation_cal(principal, inflation)
    print(f"{year} years later the amount, ${base}, will become ${principal}")


def main():
    global option
    print("\n|############################################|")
    print("| Welcome to Engch interest calculator!      |")
    print("| Only accept numerical numbers input.       |")
    print("| Rounds off to nearest 2 significant value. |")
    print("| Interest/dividend kicks in on year 1!      |")
    print("| Gains kicks in after interest/dividend!    |")
    print("|############################################|\n")

    print("Select your option!")
    print("1: Simple Compound Dividend Calculator (no reinvest)")
    print("2: Simple Compound Gain Calculator (reinvest)")
    print("3: Dynamic Compound Dividend Calculator (no reinvest)")
    print("4: Dynamic Compound Gain Calculator (reinvest)")
    print("5: Quick Present Value Calculator")
    print("6: Quick Future Value Calculator")
    print("0: Exit")

    option = int(input("--> "))
    clear()

    """ get type of calculation to execute """
    match option:
        case 1:
            simple_compound_interest_no_reinvest()
        case 2:
            simple_compound_gain_reinvest()
        case 3:
            dynamic_compound_gain_no_reinvest()
        case 4:
            dynamic_compound_gain_reinvest()
        case 5:
            present_value()
        case 6:
            future_value()
        case 0:
            sys_exit()
        case _:
            main()


if __name__ == '__main__':
    while True:
        try:
            main()
            print("\n|##########################################|")
            print("| Thank you for using this CLI service :-) |")
            print("|##########################################|\n")
            break
        except ValueError:
            print("Invalid input, please enter numerical numbers only.")
        except OverflowError:
            print("Numerical calculation too huge! Please scale it down and try again.")
        except ZeroDivisionError:
            print("OI funny ah.")
        except FloatingPointError:
            print("Computational error! Please try with lesser floating points.")
        except BufferError:
            print("Buffer error! Please restart and try again.")
        except IndexError:
            print("Index error! Sequence out of range.")
        except KeyError:
            print("Mapping error! Key not found in existing set.")
        except ModuleNotFoundError:
            print(ModuleNotFoundError)
        except ImportError:
            print(ImportError)
        except KeyboardInterrupt:
            print(KeyboardInterrupt)
            sys_exit()
        except MemoryError:
            print(MemoryError)
        except OSError:
            print(OSError)
        except RuntimeError:
            print(RuntimeError)
        except TabError:
            print(TabError)
        except IndentationError:
            print(IndentationError)
        except SyntaxError:
            print(SyntaxError)
        except SystemError:
            print(SystemError)
        except SystemExit:
            print(SystemExit)
            sys_exit()
        except TypeError:
            print(TypeError)
