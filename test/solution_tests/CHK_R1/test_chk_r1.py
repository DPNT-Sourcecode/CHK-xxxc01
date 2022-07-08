from lib.solutions.CHK.checkout_solution import checkout

class TestChk():
    def test_checkout_has_only_allowed_skus(self):
        assert checkout("ABCDE") == -1
    
    def test_checkout_has_allowed_skus(self):
        assert checkout("ABCD") == True