from lib.solutions.HLO.hello_solution import hello


class TestSum():
    def test_hlo(self):
        assert hello("world") == "world"