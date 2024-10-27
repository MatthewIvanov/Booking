class Car:

    def _start_engine(self):
        return "Engine's sound."

    def run(self):
        return self._start_engine()



car = Car()
assert "Engine's sound." == car.run()
assert "Engine's sound." == car._start_engine()