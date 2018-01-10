# Local vs Global

def local():
    # m doesn't belong to the scope definded  by the local function
    # so Python will keep looking into the next enclosing scop.
    # m is finally found in the global scope
    print(m, 'printing from the local scope')

m = 5
print(m, 'printing from the global scope')

local()
