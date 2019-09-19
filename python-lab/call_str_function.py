#this program deals with strings and then calls the functions which remembles those string literals


def A():
    print('A')
    
def B():
    print('B')
    

caller = lambda x : globals()[x]()

calling_str = input(' A\n B\nEnter Function Name\n')
caller(calling_str)