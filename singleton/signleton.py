class SingleTon:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingleTon,cls).__new__(cls)
            return cls._instance

    def __init__(self):
        if not hasattr(self,'initialized'):
            self.initialized = True
            self.value = 42

singleton1 = SingleTon()
print(singleton1.value)
singleton2 = SingleTon()
print(singleton2.value)