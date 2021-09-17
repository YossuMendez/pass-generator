from random import randint, random

class passwordGenerator:
    def __init__(self, name, birtday, phoneNumber, email, randomFact) -> None:
        self.__name = name
        self.__birthday = birtday
        self.__phoneNumber = phoneNumber
        self.__email = email
        self.__randomFact = randomFact
    
    def createPasswordName(self) -> str:
        stringName = chr(randint(33, 47))*randint(2,4)
        withoutSpace = self.__name.replace(" ", "")
        halfNum = len(withoutSpace)/2
        stringName = stringName + withoutSpace[randint(0,round(halfNum)):randint(round(halfNum),len(withoutSpace))]
        stringName = stringName.replace("a", "@")
        stringName = stringName.replace("e", "3")
        stringName = stringName.replace("i", "¡")
        stringName = stringName.replace("o", "0")
        stringName = stringName.replace("u", "~")
        #print(f'{stringName}')
        return stringName

    def __createPasswordBirthday(self) -> str:
        stringBirthday = chr(randint(58, 63))*randint(2,4)
        day = self.__birthday[0:2]
        month = self.__birthday[3:5]
        year = self.__birthday[6:10]
        day = int(day) + len(self.__name)
        month = int(month) + len(self.__birthday)
        year = int(year) + len(self.__randomFact)
        stringBirthday = stringBirthday + str (year) + str (day) + str (month)
        #print(f'{day}  {month}  {year}  {stringBirthday}')
        return stringBirthday
    
    def __createPasswordPhoneNumer(self):
        pass



nuevosDatos = passwordGenerator("Josue David Mendez Diaz", "03/02/1999", "502 30438619", "jossugames@gmail.com", "yossu")
