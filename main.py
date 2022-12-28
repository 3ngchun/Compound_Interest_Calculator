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
    :param interest: yearly interest
    :return: the interest gain from the year
    """
    interest_gained = float("{:.2f}".format(float(principal * interest)))
    return interest_gained


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
    present_value = float(principal / pow(1 + inflation, year))
    return float("{:.2f}".format(present_value))


def simple_or_dynamic_interest_calculator_input():
    """
    same user input for simple/dynamic interest calculator
    :return: base, interest, inflation
    """
    base = float("{:.2f}".format(float(input("Yearly Addition: $"))))
    interest = float("{:.4f}".format(float(input("Interest in percentage: ")) / 100))
    inflation = float("{:.4f}".format(float(input("Interest in inflation: ")) / 100))
    return base, interest, inflation


def gains_output(total_contribution, inflation_principal, principal, this_year, year, interest):
    """
    final output result for simple/complex interest calculator
    :param total_contribution: total value inputted
    :param inflation_principal: how total value would become if follow inflation rate
    :param principal: how total value would become if follow interest
    :param this_year: current year of result
    :param year: total years
    :return: print to screen
    """
    global option, final
    print(f"########## Year {this_year}/{year} result! ##########")
    print(f"Total contribution: ${total_contribution}!")
    if not final:
        print(f"Interest of the year: ${interest}!")
    else:
        print(f"Total interest: ${interest}!")
    print(f"Inflated value: ${inflation_principal}!")
    print(f"Future value: ${principal}!")
    if total_contribution != 0:
        if (option % 2) == 1:  # no reinvest
            print(f"Gain vs Base + Interest: "
                  f"{float('{:.2f}'.format(float((((principal + interest) / total_contribution) - 1) * 100)))}%")
        else:  # reinvest
            print(f"Gain vs Base {float('{:.2f}'.format(float(((principal / total_contribution) - 1)) * 100))}%")
    else:
        print("Gain vs Base: not relevant")
    if inflation_principal != 0:
        if (option % 2) == 1:
            print(f"Gain vs Inflation "
                  f"{float('{:.2f}'.format(float((((principal + interest) / inflation_principal) - 1)) * 100))}%")
        else:
            print(f"Gain vs Inflation {float('{:.2f}'.format(float(((principal / inflation_principal) - 1)) * 100))}%")
    else:
        print("Gain vs Inflation: not relevant")
    print(f"############# END OF YEAR #############\n")


def simple_compound_interest_no_reinvest():
    """
    input yearly contribution and no reinvestment with interest rate and inflation rate for a number of years.
    :return: total contribution, inflated value, future value, gain in percentage.
    """
    global final
    principal = inflation_principal = total_interest = 0
    year = int(input("Years of holding: "))
    base, interest, inflation = simple_or_dynamic_interest_calculator_input()
    total_contribution = base * year
    """ calculation """
    for i in range(year):
        """ simple interest dividend """
        principal = this_year_addition(principal, base)
        total_interest += interest_gain(principal, interest)
        """ simple inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        inflation_gain = interest_gain(inflation_principal, inflation)
        inflation_principal = new_principal(inflation_principal, inflation_gain)
    """ final output """
    final = True
    gains_output(total_contribution, inflation_principal, principal, year, year, total_interest)


def simple_compound_gain_reinvest():
    """
    input yearly contribution and reinvestment with interest rate and inflation rate for a number of years.
    :return: total contribution, inflated value, future value, gain in percentage.
    """
    global final
    """ user input parameter """
    principal = inflation_principal = 0
    year = int(input("Years of holding: "))
    base, interest, inflation = simple_or_dynamic_interest_calculator_input()
    total_contribution = base * year
    total_interest = 0
    """ calculation """
    for i in range(year):
        """ simple interest gain """
        principal = this_year_addition(principal, base)
        interest_gained = interest_gain(principal, interest)
        total_interest += interest_gained
        principal = new_principal(principal, interest_gained)
        """ simple inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        inflation_gain = interest_gain(inflation_principal, inflation)
        inflation_principal = new_principal(inflation_principal, inflation_gain)
    """ final output """
    final = True
    gains_output(total_contribution, inflation_principal, principal, year, year, total_interest)


def dynamic_compound_gain_no_reinvest():
    global final
    """ user input parameter part 1/2 """
    principal = inflation_principal = total_interest_gained = 0
    total_contribution = 0
    year = int(input("Years of holding: "))
    this_year = 0
    """ dynamic calculation """
    for i in range(year):
        """ user input parameter part 2/2 """
        base, interest, inflation = simple_or_dynamic_interest_calculator_input()
        total_contribution += base
        """ dynamic interest gain """
        principal = this_year_addition(principal, base)
        interest_gained = interest_gain(principal, interest)
        total_interest_gained += interest_gained
        """ dynamic inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        inflation_gain = interest_gain(inflation_principal, inflation)
        inflation_principal = new_principal(inflation_principal, inflation_gain)
        """ yearly output """
        this_year += 1
        if this_year != year:
            final = False
            gains_output(total_contribution, inflation_principal, principal, this_year, year, interest_gained)
    """ final output """
    final = True
    gains_output(total_contribution, inflation_principal, principal, year, this_year, total_interest_gained)


def dynamic_compound_gain_reinvest():
    """
    input yearly contribution and reinvestment with interest rate and inflation rate for a number of years dynamically.
    :return: total contribution, inflated value, future value, gain in percentage. Yearly and final dynamically.
    """
    global final
    """ user input parameter part 1/2 """
    principal = inflation_principal = total_interest_gained = 0
    total_contribution = 0
    year = int(input("Years of holding: "))
    this_year = 0
    """ dynamic calculation """
    for i in range(year):
        """ user input parameter part 2/2 """
        base, interest, inflation = simple_or_dynamic_interest_calculator_input()
        total_contribution += base
        """ dynamic interest gain """
        principal = this_year_addition(principal, base)
        interest_gained = interest_gain(principal, interest)
        total_interest_gained += interest_gained
        principal = new_principal(principal, interest_gained)
        """ dynamic inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        inflation_gain = interest_gain(inflation_principal, inflation)
        inflation_principal = new_principal(inflation_principal, inflation_gain)
        """ yearly output """
        this_year += 1
        if this_year != year:
            final = False
            gains_output(total_contribution, inflation_principal, principal, this_year, year, interest_gained)
    """ final output """
    final = True
    gains_output(total_contribution, inflation_principal, principal, year, this_year, total_interest_gained)


def main():
    global option
    print("\n##############################################")
    print("| Welcome to Engch interest calculator!      |")
    print("| Only accept numerical numbers input.       |")
    print("| Rounds off to nearest 2 significant value. |")
    print("| Interest kicks in on year 1!               |")
    print("##############################################\n")

    print("Select your option!")
    print("1: Simple compound dividend calculator (no reinvest)")
    print("2: Simple compound gain calculator (reinvest)")
    print("3: Dynamic compound dividend calculator (no reinvest) # NOT DONE")
    print("4: Dynamic compound gain calculator (reinvest)")
    print("5: exit")

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
            sys_exit()
        case _:
            main()


if __name__ == '__main__':
    while True:
        try:
            main()
            print("Thank you for using this CLI service :-)")
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
