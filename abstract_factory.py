from abc import ABCMeta, abstractmethod

#Abstract Factory
class WidgetFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_scrollbar(self):
        pass

    @abstractmethod
    def create_window(self):
        pass

#Concrete Factory
class MotifWidgetFactory(WidgetFactory):

    def create_scrollbar(self):
        return MotifScroll()

    def create_window(self):
        return MotifWindow()


#Concrete Factory
class PMWidgetFactory(WidgetFactory):

    def create_scrollbar(self):
        return PMScroll()

    def create_window(self):
        return PMWindow()


class WindowFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


class MotifWindow(WindowFactory):

    def open(self):
        print "Opens Motif Window"

    def close(self):
        print "Closes Motif Window"

class PMWindow(WindowFactory):

    def open(self):
        print "Opens PM Window"

    def close(self):
        print "Closes PM Window"

class ScrollFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass


class MotifScroll(ScrollFactory):

    def show(self):
        print "Shows Motif Scroll"

    def hide(self):
        print "Hides Motif Scroll"

class PMScroll(ScrollFactory):

    def show(self):
        print "Shows PM Scroll"

    def hide(self):
        print "Hides PM Scroll"


if __name__ == '__main__':

    #factory = MotifWidgetFactory()
    factory = PMWidgetFactory()
    window = factory.create_window()
    window.open()
    scroll = factory.create_scrollbar()
    scroll.show()
