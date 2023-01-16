# --method_inheritance


# class Jhon:
#     def ing(self):
#         print('singing')

#     def run(self):
#         print('running')

# class Jane:
#     def jog(self):
#         print("jogging")
# parent class

# class Person():
#      def sing(self):
#         print('singing')
# class john(Person):
#      def run(self):
#         print("jogging")
# class Jane(Person):
#     def jog(self):
#         print("jogging")

# runner=john()
# runner.sing()

class person:
    def __init__(self):
        self.employed = True

    def sing(self):
        print("singing")


class Jane(person):
    def jog(self):
        print("jogging")


jogger = Jane()
jogger.employed
