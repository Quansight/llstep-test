from llstep import step_data
from llstep_test.step_extension import step_extension


simple_value = step_data(int)
simple_result = step_data(int)


@step_extension
def value_is(self, desired_value):
    simple_value = desired_value


@step_extension
def result_is(self, expected_result):
    assert simple_result == expected_result


@step_extension
def value_plus(self, other_value: int):
    simple_result = simple_value + other_value
