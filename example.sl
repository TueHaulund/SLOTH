# Conditionals:
if (5 < 3) then
    # stmts
elif (3 <5) then
    # stmts
else
    # stmts
end


# Loops:
while (i < 3)
    # stmts
end

for (i := 9; i <87; i += 1)
    # stmts
end

# Var Declarations:
num a := 4
bool x := true

# Var Assignment:
a := 16
a += 14
x := not x

# Function Declarations:
def myFunc (num x, bool y) -> num
    # stmts
    return 2

def myProc (num z) -> void
    # stmts
    return

# Expressions
a := a + 2 - 9 * (4 / 5)
b := -2 * 4
c := (b = a) or (b <= a) and (b >= a) or not b
