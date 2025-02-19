"""Test your functions from Week 2 assignment.
"""
import preclass_assignment.functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    #bedlenght = "145"
    #output2 = "the bed is ok"
    # when
    #fxn.goldilocks(inp)
    # then
    #assert output2 == actualoutput  #! Update the contents of this function so it correctly tests goldilocks


def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    inp = [5] # test input to function
    exp_out = [1, 1, 2, 3, 5] # expected output
    # when
    output = fxn.fibonacci(inp)
    # then
    assert exp_out == output #! Update the contents of this function so it correctly tests fibonacci_stop


def test_logical_operator():
    """Check logical_operator works as expected."""
    # given
    pitch_angles = [10, 85, -5, 95, 40, 100, 70]
    status_signals = [0, 0, 1, 0, 0, 2, 1]
    # when
    actual_output = fxn.logical_operator(pitch_angles)
    # then
    assert status_signals == actual_output #Compare expected and actual results
