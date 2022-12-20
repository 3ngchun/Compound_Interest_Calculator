"""
Compound interest calculator with yearly addition option
"""
from os import system
from sys import exit as sys_exit


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


def compound_interest_gain(principal, interest):
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


def simple_or_dynamic_interest_cal_output(total_contribution, inflation_principal, principal, this_year, year):
    """
    final output result for simple/complex interest calculator
    :param total_contribution: total value inputted
    :param inflation_principal: how total value would become if follow inflation rate
    :param principal: how total value would become if follow interest
    :param this_year: current year of result
    :param year: total years
    :return: print to screen
    """
    print(f"########## Year {this_year}/{year} result! ##########")
    print(f"Total contribution: ${total_contribution}!")
    print(f"Inflated value: ${inflation_principal}!")
    print(f"Future value: ${principal}!")
    if total_contribution != 0:
        print(f"Gain vs Base {float('{:.2f}'.format(float(((principal / total_contribution) - 1)) * 100))}%")
    else:
        print("Gain vs Base: not relevant")
    if inflation_principal != 0:
        print(f"Gain vs Inflation {float('{:.2f}'.format(float(((principal / inflation_principal) - 1)) * 100))}%")
    else:
        print("Gain vs Inflation: not relevant")
    print(f"############# END OF YEAR #############\n")


def simple_compound_interest_calculator():
    """
    input yearly contribution with interest rate and inflation rate for a number of years.
    :return: total contribution, inflated value, future value, gain in percentage.
    """
    """ user input parameter """
    principal = inflation_principal = 0
    year = int(input("Years of holding: "))
    base, interest, inflation = simple_or_dynamic_interest_calculator_input()
    total_contribution = base * year
    """ calculation """
    for i in range(year):
        """ simple interest gain """
        principal = this_year_addition(principal, base)
        interest_gain = compound_interest_gain(principal, interest)
        principal = new_principal(principal, interest_gain)
        """ simple inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        inflation_gain = compound_interest_gain(inflation_principal, inflation)
        inflation_principal = new_principal(inflation_principal, inflation_gain)
    """ final output """
    simple_or_dynamic_interest_cal_output(total_contribution, inflation_principal, principal, year, year)


def dynamic_compound_interest_calculator():
    """
    input yearly contribution with interest rate and inflation rate for a number of years dynamically.
    :return: total contribution, inflated value, future value, gain in percentage. Yearly and final dynamically.
    """
    """ user input parameter part 1/2 """
    principal = inflation_principal = 0
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
        interest_gain = compound_interest_gain(principal, interest)
        principal = new_principal(principal, interest_gain)
        """ dynamic inflation gain """
        inflation_principal = this_year_addition(inflation_principal, base)
        inflation_gain = compound_interest_gain(inflation_principal, inflation)
        inflation_principal = new_principal(inflation_principal, inflation_gain)
        """ yearly output """
        this_year += 1
        simple_or_dynamic_interest_cal_output(total_contribution, inflation_principal, principal, this_year, year)
    """ final output """
    simple_or_dynamic_interest_cal_output(total_contribution, inflation_principal, principal, year, this_year)


def main():
    print("\n##############################################")
    print("| Welcome to Engch interest calculator!      |")
    print("| Only accept numerical numbers input.       |")
    print("| Rounds off to nearest 2 significant value. |")
    print("| Interest kicks in on year 1!               |")
    print("##############################################\n")

    print("Select your option!")
    print("1: Simple compound interest calculator")
    print("2: Dynamic compound interest calculator")
    print("3: exit")

    options = int(input("--> "))
    clear()

    """ get type of calculation to execute """
    match options:
        case 1:
            simple_compound_interest_calculator()
        case 2:
            dynamic_compound_interest_calculator()
        case 3:
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
