employee = []

def add_employ():
    id_no = int(input('enter employe id: '))
    name = input('enter name: ')
    age = int(input('enter the age: '))
    job = input('enter job: ')
    
    emp = {
        'id_no':id_no,
        'name':name,
        'age':age,
        'job':job
        
    }
    employee.append(emp)
    print(f"{name} added")

def delete_employ():
    id_no = int(input('enter id number to remove: '))
    for i in employee:
        if i['id_no'] == id_no:
            employee.remove(i)
            print("deleted")
        else:
            print(f"{id_no} not found")

def display_info():
    if not employee:
        print('no data')
        
    else:
        for i in employee:
            print(f"id_no :{i['id_no']}\nname :{i['name']}\nage :{i['age']}\njob :{i['job']}")

def search_employ():
    id_no = int(input('enter id number: '))
    for i in employee:
        if i['id_no'] == id_no:
            print(f"id_no :{i['id_no']}\nname :{i['name']}\nage :{i['age']}\njob :{i['job']}")
        else:
            print(f"{id_no} not found")

                        


def main():
    while True:
        print('1.add employ')
        print('2.delete')
        print('3.display')
        print('4.search')
        print('5.quit')
        
        value = int(input('enter the option: '))
        
        if value == 1:
            add_employ()
        elif value == 2:
            delete_employ()
        elif value == 3:
            display_info()
        elif value == 4:
            search_employ()
        elif value == 5:
            break
if __name__ == "__main__":
    main()
        
