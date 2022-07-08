from lib.solutions.CHK.checkout_solution import checkout

class TestChk():
    def test_checkout(self):
        assert checkout("ABCD") == 115