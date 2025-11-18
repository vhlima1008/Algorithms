class Temperature:
    def __init__(self):
        self._celsius = 0;
        self._farenheint = 0;

    @property
    def celsius(self):
        self._celsius = 5*((self._farenheint - 32)/9);
        return self._celsius;

    @celsius.setter
    def celsius(self, value):
        self._celsius = value;

    @property
    def farenheint(self):
        self._farenheint = ((self._celsius*9)/5)+32;
        return self._farenheint;

    @farenheint.setter
    def farenheint(self, value):
        self._farenheint = value;

t = Temperature()
t.celsius = 30;
print(t.farenheint)