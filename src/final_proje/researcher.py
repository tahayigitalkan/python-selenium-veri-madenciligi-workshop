class Researcher:
    def __init__(self, id, name, title):
        self.__id = id
        self.__name = name
        self.__title = title
        self.__deparments = []

    def add_department(self, department):
        if(department not in self.__deparments and department != ""):
            self.__deparments.append(department)

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def get_departments(self):
        return ",".join(self.__deparments)