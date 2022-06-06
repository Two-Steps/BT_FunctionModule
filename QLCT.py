program_run = True

def add_item(myList,item):
    myList.append(item)
    print(f'Add item with name:{item["name"]} success!')

def find_index_item(myList,item_name):
    length = len(myList)
    result = -1
    for i in range(length):
        if myList[i]['name'] == item_name:
            result = i
    return result
def remove_item(myList,item_name):  
    if find_index_item(myList,item_name) > -1:
        myList.pop(find_index_item(myList,item_name))
        print('Your list after remove is:',myList)
    else:
        print('Not have',item_name,'in your list')
        print('Your list:',myList)
myList = []
while program_run:
    #myList = [{'name': 'fruit', 'cost': '31', 'date': '2021'},{'name': 'phone', 'cost': '99', 'date': '2022'}]
    your_option = ''
    print('What do you want to do? \n \
    "1. Add \n \
    "2. Remove \n \
    "3. Quit')
    while not your_option in ['1','2','3']:
        your_option = input('Choice you option: ')
    if your_option == '1':
        input_name = input('Input your item name: ')
        input_cost = input('Input your item cost: ')
        input_date = input('Input your item date: ')
        item = {'name': input_name,'cost': input_cost, 'date': input_date}
        add_item(myList,item)
        print('Your list:',myList)
    elif your_option == '2':
        name_item_remove = input('Input item name you want remove from list: ')
        remove_item(myList,name_item_remove)
    else:
        quit()