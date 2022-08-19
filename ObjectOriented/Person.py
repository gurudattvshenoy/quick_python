class Employee:
    company = "Acme"

    def __init__(self,name,age):
        self._age = age
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name,str):
            self._name = name
        else:
            raise AttributeError("Name must be a string")

    @name.setter
    def age(self,age):
        if isinstance(age,int) and age >20:
            self._age = age
        else:
            raise AttributeError("Age must be a string and min: 20,max:60 years")

    def __repr__(self):
        return "Person(name = {},age={}".format(self._name,self._age)

    def __str__(self):
        return "{}".format(self._name)

    @classmethod
    def get_company(cls):
        return cls.company


p1 = Employee("Guru",35)
p2 = Employee("Katrina",40)
p3 = Employee("Neha",32)


print(p1)
print(p2)

#p2.age = "22"
# raise AttributeError("Age must be a string and min: 20,max:60 years")

print(p1.company)
print(p2.company)

