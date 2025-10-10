# Realizar la ejecución simbólica de los siguientes códigos:

# 1. x=5 ; y=7; x = x + y
"""
x=5
y=7
    // Estados a
x = x + y
    // Estado b
    // Vale x == x@a + y@a == 5 + 7 == 12
"""
# 2. x=5 ; y=7 ; z=x+y; y = z * 2
"""
x=5
y=7
    // Estados a
z=x+y
    // Estado b
    // Vale z == x@a + y@a == 5 + 7 == 12
y = z * 2
    // Estado c
    // Vale y == z@b * 2 == 12 * 2 == 24
"""

# 3. x=5 ; y=7 ; x="hora"; y = x * 2
"""
x=5
y=7
    // Estados a
x = "hora"
    // Estado b
y = x * 2
    // Estado c
    // Vale y == x@b * 2 == "hora" * 2 == "horahora"
"""

# 4. x=False ; res=not(x)
"""
x=False
    // Estado a
res=not(x)
    // Estado b
    // Vale res == not(x@a) == not(False) == True
"""

# 5. x=False ; x=not(x)

"""
x=False
    // Estado a
x=not(x)
    // Estado b
    // Vale x == not(x@a) == not(False) == True
"""

# 6. x=True ; y=False ; res=x and y; x = res and x

"""
x=True
y=False
    // Estados a
res=x and y
    // Estado b
    // Vale res == x@a and y@a == True and False == False
x = res and x
    // Estado c
    // Vale x == res@b and x@a == False and True == False
"""
