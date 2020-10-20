import mysql.connector

def orderBy(sortlist, orderby=[], desc=[]):
    for i in reversed(orderby):
        sortlist.sort(key=operator.userscore(i), reverse=(i in desc))
    return sortlist
 