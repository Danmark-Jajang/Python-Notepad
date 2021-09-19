class Hello:
    def __enter__(self):
        print('Enter...')
        return self
    
    def sayHello(self, name):
        print('Hello' + name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit...')

with Hello() as h:
    h.sayHello('obama')
    h.sayHello('trump')