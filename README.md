# using_eval_python
I discovered a feature in python when I was trying to optimise a chunk of code I wrote a few months back. I had a conversation with a colleague of mine at work and the response was that the usage of "eval()" was frowned upon so I wanted to understand why. This jusr shows how I used it

I used the function "eval()" feature whilst writing a data migration program used to move data between asset management tools I realised I had a bunch of functions doing similar things, i.e. making API calls. 

My example here just shows a rough idea how I used the "eval()" function to make multiple API calls using a shared library from an external python script.
GOAL: 

1. Use one function to make multiple API calls to a shared library class
2. Store all API function names into a dictionary
3. Use the "format" feature to create a string that represents a function call at run time
4. Use the "eval" feature to evaluate/execute the code at run time to provide the desired effect
