print "Welcome to the Python Calculus Prototype!"
print "We have three functions: derivatives, antiderivatives, and definite integrals."

function = raw_input("What will you do? ")

if function == "Derivative" or function == "derivative" or function == "derivatives" or function == "Derivatives":
    terms = int(raw_input("how many terms are there in the function?  Limit 3: "))
    if terms == 1:
        coe = float(raw_input("What is the coefficient?  If no coefficient, type \"1\": "))
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
    if terms == 2:
        coe1 = float(raw_input("What is the first coefficient?  If no coefficient, type \"1\": "))
        exp1 = float(raw_input("what is the first exponent?  If no exponent, type \"1\": "))
        coe2 = float(raw_input("What is the second coefficient?  If no coefficient, type \"1\": "))
        exp2 = float(raw_input("What is the second exponent?  If no exponent, type \"1\": "))
        coe1a = coe1 * exp1
        exp1a = exp1 - 1
        coe2a = coe2 * exp1
        exp2a = exp2 - 1
        print "original equation: " + str(coe1) + "X^" + str(exp1) + "+" + str(coe2) + "X^" + str(exp2)
        
    #coex, X^, expx
    #coex + expx, X^, expx - 1
    
elif function == "Antiderivatie" or function == "antiderivative":
    print "Sorry, the antiderivative function is currently unavailable."
elif function == "Definite Integral" or function == "Definite integral" or function == "definite integral":
    print "Sorry, the definite integrals function is currently unavailable."
else:
    print "Sorry, we cannot do that.  Please start over."
