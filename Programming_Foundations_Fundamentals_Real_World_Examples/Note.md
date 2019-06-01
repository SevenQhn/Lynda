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
- inheritance 
- abstraction 
- encapsulation 
- polymorphism
    - Overwriting
    - Overloading
- import whole module VS import specific of func from specific mdule
    ```python
        import randon
        random.randit(1,20)
        ---
        from randon import randit
        randit(2,20) #easy But may cause confliction
        ---
        random.random()
        from randon import random
        randon()# right
        random.xxx() # wrong multfunction get was right
        import random as ran
        from randon import randit as r
    ```
- import modules VS import Package
    - package has a path attribute which points to the folder path
- Package >> Module
    ```python
        import urllib.request
        urllib.request.xxx()
        ----
        import urllib.request as urlReq
        urllib.__path__ # will retren it path
    ```
- List VS Tuple
    - List
        - List.shift
        - List.append()
        - List[x]
        - List[x] = "xx"
        - List.insert(index,"xxsasx")//insert in any postion u want
        - List.index("xx")// return indedx **first match**
        - List.pop(index)
        - List.remove("xx") /// == List.pop(List.index("")
        - Muliti Dimensional List
            - Floor row
            - how to go through rach elemen in multi-demin List
                ```python
                    for floor in lot_3d:
                        for row in floor:
                            for car in row:
                                print(car)
                ```
    - Tuples
        - Simliar to list but !! **Immutable**
        - for simplicity
            - apply -- for example destination of GPS
        - [] VS () // () for tuple [] for list in python
        - ()[x]
        - ()[x] = xx //!! Report mulfunction
        - froever frozen in their creation state
        - impot tkinter
- Queue vs Stack
    - Queue note how to prevent infinit locking up
        - FIFO first in first out
        - quee() is a block execution
            - can set another interface to add 
                - default infinite wait feed item to exe
            - add to a full queue or get a empty queue will cause shell **stop working**
            - or 
                ```python
                    import queue
                    q = queue.Queue(2)
                    q.empty
                    q.put("asd")
                    q.full()
                    q.put_nowait("asd3")
                ```
    - Stacks
        - FILO first in last out
        - Python no built in fun call stack but could use list to implement it
            - Since list can easy handle move like -- add and remove items from end
            - last in last out .pop/.append
- Set
    - Unorder collection of unique values
    - a = set([x5,x4,x3,x2,x1])
    - c = a.union(b) combine sets // will remove duplicate items and combine them into one single set
    - wildwest --> no order at all
    - len(c)
    - Sort Sets (zhao peng you)
        - a.interset(b) // will find common items
        - a.difference(b) // will find items in a but which is not in b
        - a.symmertwic_difference(b) //will find items which only in a or b
    - Add or remove items from sets
        - "x" in a ? // check if x in set a
        - a.add()
        - a.remove("x")//x has to be exist or throw a error
        - a. pop() //random get one out and deleted 

