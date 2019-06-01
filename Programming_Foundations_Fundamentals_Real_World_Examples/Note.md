# Programming Fundations Real World Examples

- making omelet
    - function() VS a = funcion()
- making omelet VS makeing pancake
    - same process can be extract to a new function for example mix_and_flip()
        - make code reuseable
        - optimize code update only need change onc place
- handle string input & output
    ```python
        def inputString(xx):
            a = 'a {} omelette'.format(xx)
            print(a)
    ```
- Pramaeter VS Argument
    - P is the variable name when define the fun
    - A is the specific input values
- handle multiple input
    ```python
        def inputMultiple(*tupleStructre):
            a = 'a {} b'.format(len(tupleStructre))
    ```
    - use * to make this happen and will transfer multiple input as a tuple which can be access iterate (with local scope)
- Only you can have is a the value be returned other local scope value will **gone** after that !!Note this
- Note the scope of your variable
    - when two var with same name but not scope level? then the small local level ar in specific fun win in that fun
    - Because when func was called it will search local scope first if exist then stop search if not will search global level then
- Make a new varable in **pyhtn**
    ```python
        thisIsANewVarable = sometValue
    ```
    - then how to chang a global varibale into a fun scop? add global var
    ```python
        def aa():
            global a
            a = newValue
    ```
    - how to prevent a global var be changed by mistake
- In Python, everything is an object, with a unique ID and attributes
- Python is a ***Strong type language***
- Python is OOPw language
- In OOP language 
    - Func string num are all objects
- Object has unique ID
    - Same Object can be refer by multiple different name 
        ```python
            a = b()
            c = a
            id(a) == id (c)
            a is c // will return true
            //but can change c bind to other object
        ```
- Mutable VS Immutble data/Object
    - List Vs String
    - add delete will note change the **id** of the list
    - id(a) !== id(a + "asda")
        - in behind sysytem create a new string for new value
