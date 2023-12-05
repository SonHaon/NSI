from collections import namedtuple
contact={
    1:{
        "name":"noah",
        "surname":"noahhhhh",
        "birth":"2007",
        "address":"ML",
        "city":"ML",
        "zipcode":"78600",
        "tel":"07********",
        "email":"example@gmail.com"
    },
    2:{
        "name":"noah",
        "surname":"noahhhhh",
        "birth":"2007",
        "address":"ML",
        "city":"ML",
        "zipcode":"78600",
        "tel":"07********",
        "email":"example@gmail.com"
    }
}

for a in contact:
    for b in contact[a]:
        print(a,b)