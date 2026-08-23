"""Run me: python3 example.py"""


def divide(a: float, b: float) -> float:
    return a / b


# try / except / else / finally
try:
    result = divide(10, 2)
except ZeroDivisionError:
    print("can't divide by zero")
except (TypeError, ValueError) as e:
    print(f"bad input: {e}")
else:
    print(f"result: {result}")  # only runs because no exception was raised
finally:
    print("always runs")

print("---")

# Now trigger the ZeroDivisionError branch
try:
    divide(10, 0)
except ZeroDivisionError:
    print("caught: can't divide by zero")

print("---")


# raise, not throw
class InsufficientFundsError(Exception):
    pass


def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFundsError(f"insufficient funds: {amount} > {balance}")
    return balance - amount


try:
    withdraw(50, 100)
except InsufficientFundsError as e:
    print(f"caught custom exception: {e}")

print("---")

# Exception chaining with `from`
try:
    try:
        int("not a number")
    except ValueError as e:
        raise RuntimeError("config parsing failed") from e
except RuntimeError as e:
    print(f"chained exception: {e}")
    print(f"original cause: {e.__cause__}")

print("---")
print("Now see a real traceback (uncomment the line below and run again):")
# divide(10, 0)  # uncomment this and remove the surrounding try/except above
# to see an actual unhandled traceback printed to the terminal — read it
# bottom-up: last line = the error, then walk the File/line entries upward.
