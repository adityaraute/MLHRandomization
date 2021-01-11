import time

class Randomization:

    def random_generator(self, length):
        lis=[]
        for i in range(length):
            sec = time.time_ns()
            time.sleep(0.02)
            lis.append(int((sec//100)%10))
        return lis

    def randomInt(self,length):
        lista = map(str, self.random_generator(length))
        return (int("".join(lista)))

    def randomList(self,length):
        return self.random_generator(length)
        


if __name__ == "__main__":
    count = int(input("Enter number of random digits required: "))
    choice = input("Enter 0 for a randomized integer and 1 for a list of random integers: ")
    r = Randomization()
    if choice=='1':
        print(r.randomList(count))
    elif choice=='0':
        print(r.randomInt(count))
    else:
        print("Illegal choice")