from abc import ABCMeta, abstractmethod

class Application(object):

    @abstractmethod
    def create_document(self):
        pass

    def add_document(self):
        pass

    def open_document(self):
        pass

class MyApplication(Application):

    def create_document(self):
        return MyDocument()


class Document():
    def open(self):
        pass


class MyDocument():

    def open (self):
        print "Opening My Document"


if __name__ == '__main__':
    app = MyApplication()
    doc = app.create_document()
    doc.open()
