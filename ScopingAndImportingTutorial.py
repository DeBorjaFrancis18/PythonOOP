#import file
import newSample.Arithmetic as a

#GLOBAL VARIABLE
y = "World" #can be accessed anywhere

#LOCAL VARIABLES
def sayHello():
    global y #change the global variable from function
    y = "Me" #changes "World" to "Me"
    x = "Hello " + y
    print(x) #can only be called in this function

#PARAMETER VARIABLE
def say(word):
    print(word) #just like local variable

sayHello()
say("what's up?")
print(a(5, 6))
