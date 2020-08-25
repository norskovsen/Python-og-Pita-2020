from sympy import init_session

# Setting up variables
init_session()

# Funktion manipulation
g0 = x**2 +x 
latex(g0)
diff(g0) # Differentier g0

# Integrerer g0
integrate(g0) 
integrate(g0, (x, 0, 2))

factor(g0) # Faktoriserer g0

# Løs for x: x² + x = x + 1
solve(Eq(g0,x+1))

# Løs for x: x² + x = 0
solve(g0)

g1 = (x - 2)*(x - 6)
# Udvid g1
expand(g1)

# Plot g0 og g1
plot(g0,g1)

# Partielle afledede 
g2 = x**2 + 5*y
diff(g2, x)
diff(g2, y)
