class phone:
    type = "smartphones"

    def __init__(self,brand,storage_gb):
        self.brand=brand
        self.storage_gb=storage_gb

    def full_specs(self):
        print(f"this is a {self.type},brand:{self.brand},storage:{self.storage_gb},GB")

if __name__ == '__main__':
    phone1=phone("samsung","120")
    phone2=phone("qmobile","280")

    phone1.full_specs()
    phone2.full_specs()