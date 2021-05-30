class A:
    def method(self):
        print("We are in class A")


obja = A()
if __name__ == '__main__':
    print("Module Name :", obja.__module__)