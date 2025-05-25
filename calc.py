import math

# Extend math functions to support degrees as well
def sind(x): return math.sin(math.radians(x))
def cosd(x): return math.cos(math.radians(x))
def tand(x): return math.tan(math.radians(x))

# Add safe functions to environment
allowed_names = {
    k: v for k, v in math.__dict__.items() if not k.startswith('__')
}
# Add degree versions of trig functions
allowed_names.update({
    'sind': sind,
    'cosd': cosd,
    'tand': tand,
})

print('📐 Calculator — type "exit" to quit')
print('Use sin(), cos(), tan() for radians; use sind(), cosd(), tand() for degrees.')

while True:
    expr = input('>> ')
    if expr.lower() in ['exit', 'quit']:
        break
    try:
        result = eval(expr, {'__builtins__': None}, allowed_names)
        print('= ', result)
    except Exception as e:
        print('Error:', e)
