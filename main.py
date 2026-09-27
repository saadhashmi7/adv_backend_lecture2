class student:
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course

    def show_info(self):
        print(f"my name is {self.name},and my roll numer is {self.roll_no},and i study {self.course}")


if __name__ == '__main__':

    saad=student("saad","70154663","adv back end")
    sara=student("sara","70137363","adv front end")

    saad.show_info()
    sara.show_info()


