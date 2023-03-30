class ConcertTicket(object):
    SECTIONS = {'lower', 'premier', 'mezzanine', 'floor'}
    def __init__(self, price, section):
        self._price = price
        self._section = section
    @property
    def price(self):
        return self._price
    @property
    def section(self):
        return self._section
    @section.setter
    def section(self, section):
        if section not in self.SECTIONS:
            raise ValueError('Invalid section "{}"'.format(section))
        self._section = section


if __name__ == '__main__':
    import doctest
    doctest.testmod()