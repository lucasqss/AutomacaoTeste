
class GerenciadorAsserts:

    def __init__(self):
        self.obtained = {}
        self.expected = {}

    def insertAssertion(self, name, obtained, expected):
        self.obtained[name] = obtained
        self.expected[name] = expected

    def performAssertion(self):
        print("\nExpected = ", self.expected)
        print("Obtained = ", self.obtained)
        assert self.obtained == self.expected
