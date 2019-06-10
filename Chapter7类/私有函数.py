class Secretive:
    # def _init_(self):

    def __inaccessible(self):
        print("This is inaccessible!")

    def accessible(self):
        print("This is accessible! ")
        self.__inaccessible()


secret = Secretive()
# secret.__inaccessable()
secret.accessible()
secret._Secretive__inaccessible()
