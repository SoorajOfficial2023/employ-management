import os

employee = []

def clear():
    os.system('clear')

def add_employ():
    clear()
    flag = 0
    while flag == 0:
        try:
            id_no = int(input('enter ID: '))
            name = input('enter the name: ')
            age = int(input('enter age: '))
            job = input('enter the job:')
            flag = 1
        except:
            print('Invalid character, please enter valid character')
        
    
    emp = {
        'id_no':id_no,
        'name':name,
        'age':age,
        'job':job
        
    }
    employee.append(emp)
    print(f"{name} added successfullly")
    
def delete_employ():
    clear()
    flag = 0
    try:
        id_no = int(input('enter the ID number to remove: '))
        for i in employee:
            if i['id_no'] == id_no:
                employee.remove(i)
                print(f"{id_no} deleted")
                flag = 1
                break
        if flag == 0:
            print(f"{id_no} not found")
    except:
        print('Invalid character')

        
   
def search_employ():
    clear()
    flag = 0
   
    try:
        id_no = int(input('enter the ID number to search: '))
        for i in employee:
            if i['id_no'] == id_no:
                print(f"id_no : {i['id_no']}\nname : {i['name']}\nage : {i['age']}\njob : {i['job']}")
                flag = 1
                break
        if flag == 0:
            print(f"{id_no} not found")
    except:
        print('Invalid character')
        
def display_employ():
    clear()
    if not employee:
        print('No data')
    else:
        for i in employee:
            print(f"id_no : {i['id_no']}\nname : {i['name']}\nage : {i['age']}\njob : {i['job']}")       


def main():
    clear()
    while True:
        try:
            print('EMPLOY MANAGEMENT SYSTEM')
            
            print('\nOptions')
            print('1.add employ')
            print('2.delete employ')
            print('3.search employ')
            print('4.display employ')
            print('5.quit')
            
            choice = int(input('choose option: '))
            
            if choice == 1:
                add_employ()
            elif choice == 2:
                delete_employ()
            elif choice == 3:
                search_employ()
            elif choice == 4:
                display_employ()
            elif choice == 5:
                break
            else:
                print('Choose correct option') 
        except ValueError as e:
            print(f"Error: {e}")
            
            

if __name__ == '__main__':
    main()