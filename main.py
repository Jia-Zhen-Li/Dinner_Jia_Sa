# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:31:28 2020

@author: 劉又聖
"""

from adddish import Add_Dish
from pickdish import Pick_Dish
from modifydish import Modify_Dish
from deletedish import Delete_Dish

def main():
    prompt = 'input 1 for Add Dish, 2 for Pick Dish, ' + \
             '3 for Modify Dish, 4 for Delete_Dish, Q for leave.\n>> '
    while True:
        choice = input(prompt)
        
        if   choice == '1':
            Add_Dish()
        elif choice == '2':
            result = Pick_Dish()            
            if result:
                for dish in result:
                    print(dish)
            else:
                print('No result')            
        elif choice == '3':
            Modify_Dish()
        elif choice == '4':
            Delete_Dish()
        elif choice == 'Q':
            break
        else:
            print(f'No {choice} this option')

if __name__ == '__main__':
    main()