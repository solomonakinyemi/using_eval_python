#!/usr/bin/env python3

"""
This program was written mainly for illustrative purposes 
to compliment the article I wrote on medium. This is not 
a guide as to how you use eval() this was more of an experiment
"""

from shared_lib import SharedLibrary as shared_lib
from random import randint
import time
from pprint import pprint as pp

def call_function(module, function_selector, param={}):
    function_string=''
    function_dict = {"category": "get_chuck_joke_category",
                     "id": "get_chuck_joke_id",
                     "content": "get_url_content"
                    }
    if function_selector == 'id':
        d = next(iter(param.values()))
        function_string = 'module.{0}(random_param="{1}")'.format(function_dict[function_selector], d)
    elif function_selector == 'category':
        function_string = 'module.{0}(category="{1}")'.format(function_dict[function_selector], next(iter(param.values())))
    elif function_selector == 'content':
        function_string = 'module.{0}(random_param="{1}")'.format(function_dict[function_selector], next(iter(param.values())))
    else: 
        print('Unable to recognise the function chosen')

    print('Function called is: {0}'.format(function_string))
    response = eval(function_string)
    print('Successfully called function')
    return response
    

def main():
    response = {}
    function_to_call = ['category', 'id', 'content']
    category_ = ['movie', 'sport', 'music']
    lib_ = shared_lib()
    for function_item in function_to_call:
        rand_int = randint(0,2)
        param = {1:1, 2:2}
        if function_item == 'category':
            selected_category = category_[rand_int]
            param = {'category_chosen': selected_category}
        funct_key = function_item
        store_key = '{0}_{1}'.format('call', function_item)
        response[store_key] = (call_function(module=lib_, function_selector=funct_key, param=param))
        print('------------------------------------------------------')
        time.sleep(0.5)
    print('         ')
    print("                        ### RESULT ####                 ")
    print('         ')
    pp(response)
   
  
if __name__== "__main__":
  main()
