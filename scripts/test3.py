

class A(object):
    def __init__(self):
        self.a = 123
class B(A):
    def __init__(self):
        A.__init__(self)
        print self.a
        self.b = 345
a = B()
print a.a