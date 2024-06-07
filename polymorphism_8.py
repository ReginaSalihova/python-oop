class Person:
    def __init__(self, name, surname, patronymic, phone):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone = phone

    def get_phone(self):
        return self.phone.get('private') if 'private' in self.phone else None

    def get_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def get_work_phone(self):
        return self.phone.get('work') if 'work' in self.phone else None

    def get_sms_text(self):
        return f"Уважаемый {self.name} {self.patronymic}! Примите участие в нашем беспроигрышном конкурсе для фиических лиц"


class Company:
    def __init__(self, name_company, type_company, phone, *employees):
        self.name_company = name_company
        self.type_company = type_company
        self.phone = phone
        self.employees = employees

    def get_phone(self):
        if 'contact' in self.phone:
            return self.phone['contact']
        for employee in self.employees:
            work_phone = employee.get_work_phone()
            if work_phone:
                return work_phone
            return None

    def get_name(self):
        return self.name_company

    def get_sms_text(self):
        return f"Для компании {self.name_company} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.type_company}"


def send_sms(*recipients):
    for recipient in recipients:
        phone = recipient.get_phone()
        if phone:
            print(f"Отправлено СМС на номер {phone} с текстом: {recipient.get_sms_text()}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {recipient.get_name()}")


person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)

send_sms(person1, person2, person3, person4, company1, company2, company3)