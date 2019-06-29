# To run this code type into the commandline: python3 my_tests.py
# Note: -i can also be used to go into the interpreter after the file runs, like so:
# python3 -i my_tests.py

# Imports #
import operator
# TODO: Put here any other imports needed for the code to run, commonly seen at
# the beginning of an OK test.

all_tests = True

def test_code(b, msg):
  """
  If B is true then the test has passed and nothing happens, if B is false the
  test has failed and therefore a notice should be printed saying the test has
  failed along with MSG.

  Also returns B, to use with all_tests.
  """
  if not b:
    print('Test Fail:', msg)
  return b

# Setup code #
# TODO: Any setup code if needed, usually all that code in the OK
# test seen before it checks a value for the actual test
a = 1 # example code, can be removed
b = 2 # example code, can be removed

# Tests and other code #

# TODO: Write tests like the format below, where the first argument of test_code
# evaluates to a truthy or falsey value and the second argument is a useful
# message.
#
# all_tests is there so if a test ever fails test_code will return a falsey
# value and all_tests becomes False for the rest of the code, which then
# prevents the last if statement from printing that "All test passed!"

# example code, can be removed
all_tests = all_tests and test_code(operator.add(a,b) == (a+b), 'Testing: operator.add')

# Besides just doing the above format, additional code can be used to help with
# readability and to make the MSG argument to be more informative. For example
# see below.

# Uncomment to see a purposefully failing tests
# result = operator.sub(b,a)
# expected = b - a
# all_tests = all_tests and test_code(
#   result == 2,
#   'operator.sub(2,1) returned: ' + str(result) + ' expected: ' + str(expected))

if all_tests:
  print('All tests passed!')
