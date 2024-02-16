from pyTdd.Calculator import Operations


def test_adder():
    adder = Operations.Adder()
    assert adder.Add(1, 2, 3) == 6
