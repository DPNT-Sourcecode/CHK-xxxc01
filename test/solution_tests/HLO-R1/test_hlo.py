from lib.solutions.HLO.hello_solution import hello


class TestHlo():
    def test_hlo(self):
        assert hello("John") == "Hello, John!"