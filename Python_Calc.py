print "Welcome to the Python Calculus Prototype!"
print "We have three functions: derivatives, antiderivatives, and definite integrals."

function = raw_input("What will you do? ")

if function == "Derivative" or function == "derivative" or function == "derivatives" or function == "Derivatives":
    terms = int(raw_input("how many terms are there in the function?"))
    while terms>0
        coe = float(raw_input("What is the coefficient of the first term?  If no coefficient, type \"1\": "))
        exp = float(raw_input("What is the exponent?  If none, type \"1\", if no variable, type \"0\": "))
        coea = coe * exp
        expa = exp - 1
        print "original equation: " + str(coe) + "X^" + str(exp)
        rand = raw_input("Is this correct? ")
        if rand == "yes" or rand == "Yes":
            if expa == 1:
                print "the derivative is: " + str(coea) + "X"
            else:
                print "the derivative is: " + str(coea) + "X^" + str(expa)
        else:
            print "Sorry.  Please start over."
        
        
    #coex, X^, expx
    #coex + expx, X^, expx - 1
    
elif function == "Antiderivatie" or function == "antiderivative":
    print "Sorry, the antiderivative function is currently unavailable."
elif function == "Definite Integral" or function == "Definite integral" or function == "definite integral":
    print "Sorry, the definite integrals function is currently unavailable."
else:
    print "Sorry, we cannot do that.  Please start over."
