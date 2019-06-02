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
- Dictionary
    - Rolodex sorted alphabetically
    - dict = {"x":262 ,"asx":sad}
    - dict["sad"] = newValue/(a,b) // add/overwrit a new record to dicct
    - all key are unique
    - Davad / Davad(Amenda)
    - Reverse look ?
        ```python
            def caller_id(look_up_number):
                for name,num in rolodex.items():
                    if num == look_up_number:
                        return name #will onmly give first value match 
                        # the order of the value stored accoding to hash value which mean everytime interperted order changed
        ```
- Conditional Excutions
    - if/ells-if chain
        - Computer can only make binary choice
    - has an judge sequence **So the more restrictive options should go near the top**
    ```python
        if xxx in xxxx:
            print("1")
        elif asd and aasda in asx:
            print("2")
        else :
            print("3")
    ```
    - Switch and case statement
        - for if-else chain if correct answer is on the bottom of the chain efficiency down so we use switch 
        - Python dont have a actually switch structur BUT **could use dictionary to implement it** it will use hash directly find the value rather ran gow through every node following the chain
        - NOt when use switch dont forget break statement
        - **If your program need make decision based on a single variable or expression**
- Loops
    - list.remove("xx")
    - For vs while vs break
    - for
        - when you know how many it you need
    - while 
        - when you know when your loop need finiash
    - Break can be used to jump out of the loop once find the target (not like return it just jump out of the current loop can will continue execute the code next to current loop) 
        - for example : origianl plan is wash all dish but the fact is the container has a capacity celling so add a if/else to prevent outwash happen if full: break
- Error handling
    - Error Catching
        ```python
            try:
                wepaeh = urllib.request.urlopen("xxx")
            except： 
                print("There is a error happen")
            else: #note below block will only execut if try report no error
                for line in webpage
                    print(line)
            -----VS # below will execute whatever above is error or not
            for line in webpage
                    print(line)
        ```
    - try statement
        - contains a block of code if an error occurs durning the excution, the try statement catches the exception,preventing a crash
        ```python
            if xx:
                raise Exception #generic exception
            elif xx:
                raise Exception("Out of the limit")#informative exception//not alwways include the information of the error make it useful
            else:
                xxxx
        ```
    - custom errors
        - Most language has inbuilt error types
        - PYTHON allOW user define custom error class inherit from inbuilt parent generic error class
        - Note if u want specific specific type of except yourself you have to deal with generic err also use excepr:xxxx
- Polling and Event-driven program
    - polling 
        - keep tracking some condition think piza man coming without ring work
        - DONT suse a **free run** while loop to implement a polling routine
        - when use polling routine make sure include some delay mechanism in the loop
        ```python
            import time
            while():
                xxx
                time.sleep(1)
        ```
- Event Driven
    - can only handle a event once a time IMPORTANT
        mean there will be a queue here if something happen when ongoning event not finish
    - tkinter module 
        - For creating graphical user interfaces
        - Easy way to demo event-driven programming
    - Event handler
    - time.sleep(x) //wait x seconds then execue next line