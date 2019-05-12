# using_eval_python
I discovered this feature in python when I was trying to optimise a chunk of code I wrote a few months back. I had a conversation with a colleague of mine at work and the response was that the usage of "eval()" was frowned upon so I wanted to understand why. This just shows how I used it.

I used the function "eval()" feature whilst writing a data migration program used to move data between asset management tools I realised I had a bunch of functions doing similar things, i.e. making API calls. 

I was reading a book called programming pearls, which I must confess I still haven't completed yet. And it talked about the advantage of using data structures to reduce the number of lines of code. 

My thought process, I had 5 function calls making API requests, with different parameters. How do I reduce these to a single function whilst using data structures.

This led me to storing all the function names as a string, in a dictionary (my favourite data structure in python besides named tuples). 

Then using the format() function which is excellent for string formatting and substitution. I used this to form the exact API calls. 

And finally, the icing on the cake was eval() which then executed the function call.

My example here just shows a rough idea how I used the "eval()" function to make multiple API calls using a shared library from an external python script.

GOAL: 

1. Use one function to make multiple API calls to a shared library class
2. Store all API function names into a dictionary
3. Use the "format" feature to create a string that represents a function call at run time
4. Use the "eval" feature to evaluate/execute the code at run time to provide the desired effect

To run: 
1. Clone the repository: git@github.com:solomonakinyemi/using_eval_python.git
2. Navigate into the directory where the files are stored
3. Activate the virtual environment: source bin/activate
4. Run the code: python eval_test.py
