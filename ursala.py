class Pointer(object):
    def __init__(self):
        self._pair = None

    def set_pair(self, pair):
        self._pair = pair

    def get_pair(self):
        return self._pair

    pair = property(get_pair, set_pair)

    def exe(self):
        def f():
            for p in self.expr._agenda:
                print 'p = {0}'.format(p)
                self.pair = getattr(self, p)
            return self.pair
        return f

    @property
    def l(self):
        return self.pair[0]

    @property
    def r(self):
        return self.pair[1]

class PointerBuilder(object):
    def __init__(self):
        self._agenda = []

    @property
    def l(self):
        self._agenda.append("l")
        return self

    @property
    def r(self):
        self._agenda.append("r")
        return self



pair = (('foo', 'bar'), 'baz')

pb = PointerBuilder()
expr = pb.l.r

ptr = Pointer()
ptr.pair = pair
ptr.expr = expr
print "Expr agenda {0}".format(ptr.expr._agenda)
f = ptr.exe()
print f
p = f()
print "resuls = {0}".format(p)
