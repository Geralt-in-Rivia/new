import time


class model:
    def __init__(self):
        time.sleep(0)
        self.initStatus = True

    def predict(self, text: str) -> int:
        import random
        return random.randint(0, 10)


if __name__ == '__main__':
    modelInstance = model()
    print(modelInstance.predict("test"))
