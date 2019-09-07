""" reverse interators """

class RevInterator():
    def __init__(self, data):
        self.data = data
        self.position = len(self.data)

    def __next__(self):
        if self.position == 0:
            raise StopIteration
        else:
            self.position = self.position -1
            return self.data[self.position]

    def __iter__(self):
        return self


mylist = [1, 2, 3, 4, 5]
print(*RevInterator(mylist))



