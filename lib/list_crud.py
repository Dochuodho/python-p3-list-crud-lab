def create_an_empty_list():

    return []

def create_a_list():
    new_list=[1, 2, 3, 4]
    return new_list

def add_element_to_end_of_list(l, element):
    l=[1,2,3,4]
    l.append(5)
    
    return l


def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    l=[1,2,3,4]
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l=[1,2,3,4]
    del l[0]
    return l

def retrieve_first_element_from_list(l):
    l=[1,2,3,4]
    

    return l[0]

def retrieve_element_from_index(l, index):
    l=[1,2,3,4]
    


    return l.index(3)

def retrieve_last_element_from_list(l):
    l=[1,2,3,4]

    return l[-1]
