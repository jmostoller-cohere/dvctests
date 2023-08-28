class DummyModel:
    def __init__(self, x):
        self.x = x
        
    def __call__(self):
        return self.x + 5