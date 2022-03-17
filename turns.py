"""
    f: front face
    r: right face
    l: left face
    t: top face
    d: down face
    b: back face

    cube = {
        'f': [3][3],
        'r': [3][3],
        'l': [3][3],
        't': [3][3],
        'd': [3][3],
        'b': [3][3]
    }
"""
import numpy as np

def clockwise(cube, f, t, d, l, r):
    turned = cube.copy()

    turned['f'] = np.rot90(f, -1)
    turned['r'][:,0] = np.transpose(t[2,:])
    turned['l'][:,2] = np.transpose(d[0,:])
    turned['t'][2,:] = np.flip(np.transpose(l[:,2]))
    turned['d'][0,:] = np.flip(np.transpose(r[:,0]))

    return turned

def anticlockwise(cube, f, t, d, l, r):
    turned = cube.copy()

    turned['f'] = np.rot90(f, 1)
    turned['r'][:,0] = np.flip(np.transpose(d[0,:]))
    turned['l'][:,2] = np.flip(np.transpose(t[2,:]))
    turned['t'][2,:] = np.transpose(r[:,0])
    turned['d'][0,:] = np.transpose(l[:,2])

    return turned

def f(cube, is_clockwise=True):
    if (is_clockwise):
        return clockwise(
                cube.copy(), 
                cube['f'].copy(), 
                cube['t'].copy(), 
                cube['d'].copy(), 
                cube['l'].copy(), 
                cube['r'].copy()
            )
    return anticlockwise(
        cube.copy(), 
        cube['f'].copy(), 
        cube['t'].copy(), 
        cube['d'].copy(), 
        cube['l'].copy(), 
        cube['r'].copy()
    )

def r(cube, is_clockwise=True):
    turned = {
        'f': cube['r'].copy(),
        'l': cube['f'].copy(),
        'r': cube['b'].copy(),
        'b': cube['l'].copy(),
        't': np.rot90(cube['t'].copy(), -1),
        'd': np.rot90(cube['d'].copy(), 1)
    }
    
    if (is_clockwise):
        returned = clockwise(
                turned.copy(), 
                turned['f'].copy(), 
                turned['t'].copy(), 
                turned['d'].copy(), 
                turned['l'].copy(), 
                turned['r'].copy()
            )
    else: 
        returned = anticlockwise(
            turned.copy(), 
            turned['f'].copy(), 
            turned['t'].copy(), 
            turned['d'].copy(), 
            turned['l'].copy(), 
            turned['r'].copy()
        )
    
    return {
        'f': returned['l'].copy(),
        'b': returned['r'].copy(),
        'r': returned['f'].copy(),
        'l': returned['b'].copy(),
        't': np.rot90(returned['t'].copy(), 1),
        'd': np.rot90(returned['d'].copy(), -1),
    }

def l(cube, is_clockwise=True):
    turned = {
        'f': cube['l'].copy(),
        'l': cube['b'].copy(),
        'r': cube['f'].copy(),
        'b': cube['r'].copy(),
        't': np.rot90(cube['t'].copy(), 1),
        'd': np.rot90(cube['d'].copy(), -1)
    }

    if (is_clockwise):
        returned = clockwise(
            turned.copy(), 
            turned['f'].copy(), 
            turned['t'].copy(), 
            turned['d'].copy(), 
            turned['l'].copy(), 
            turned['r'].copy()
        )
    else:
        returned = anticlockwise(
            turned.copy(), 
            turned['f'].copy(), 
            turned['t'].copy(), 
            turned['d'].copy(), 
            turned['l'].copy(), 
            turned['r'].copy()
        )
    
    return {
        'f': returned['r'].copy(),
        'l': returned['f'].copy(),
        'r': returned['b'].copy(),
        'b': returned['l'].copy(),
        't': np.rot90(returned['t'].copy(), -1),
        'd': np.rot90(returned['d'].copy(), 1)
    }

def b(cube, is_clockwise=True):
    turned = {
        'f': cube['b'].copy(),
        'l': cube['r'].copy(),
        'r': cube['l'].copy(),
        'b': cube['f'].copy(),
        't': np.rot90(cube['t'].copy(), -2),
        'd': np.rot90(cube['d'].copy(), 2)
    }

    if (is_clockwise):
        returned = clockwise(
            turned.copy(), 
            turned['f'].copy(), 
            turned['t'].copy(), 
            turned['d'].copy(), 
            turned['l'].copy(), 
            turned['r'].copy()
        )
    else:
        returned = anticlockwise(
            turned.copy(), 
            turned['f'].copy(), 
            turned['t'].copy(), 
            turned['d'].copy(), 
            turned['l'].copy(), 
            turned['r'].copy()
        )

    return {
        'f': returned['b'].copy(),
        'l': returned['r'].copy(),
        'r': returned['l'].copy(),
        'b': returned['f'].copy(),
        't': np.rot90(returned['t'].copy(), -2),
        'd': np.rot90(returned['d'].copy(), 2)
    }

def t(cube, is_clockwise=True):
    turned = {
        'f': cube['t'].copy(),
        'l': np.rot90(cube['l'].copy(), -1),
        'r': np.rot90(cube['r'].copy(), 1),
        'b': np.rot90(cube['d'].copy(), 2),
        't': np.rot90(cube['b'].copy(), -2),
        'd': cube['f'].copy()
    }

    if (is_clockwise):
        returned = clockwise(
            turned.copy(), 
            turned['f'].copy(), 
            turned['t'].copy(), 
            turned['d'].copy(), 
            turned['l'].copy(), 
            turned['r'].copy()
        )
    else:
        returned = anticlockwise(
            turned.copy(), 
            turned['f'].copy(), 
            turned['t'].copy(), 
            turned['d'].copy(), 
            turned['l'].copy(), 
            turned['r'].copy()
        )
    
    return {
        'f': returned['d'].copy(),
        'l': np.rot90(returned['l'].copy(), 1),
        'r': np.rot90(returned['r'].copy(), -1),
        'b': np.rot90(returned['t'].copy(), 2),
        't': returned['f'].copy(),
        'd': np.rot90(returned['b'].copy(), -2),
    }

def d(cube, is_clockwise=True):
    turned = {
        'f': cube['d'].copy(),
        'l': np.rot90(cube['l'].copy(), 1),
        'r': np.rot90(cube['r'].copy(), -1),
        'b': np.rot90(cube['t'].copy(), 2),
        't': cube['f'].copy(),
        'd': np.rot90(cube['b'].copy(), -2)
    }

    if (is_clockwise):
        returned = clockwise(
            turned.copy(), 
            turned['f'].copy(), 
            turned['t'].copy(), 
            turned['d'].copy(), 
            turned['l'].copy(), 
            turned['r'].copy()
        )
    else :
        returned = anticlockwise(
            turned.copy(), 
            turned['f'].copy(), 
            turned['t'].copy(), 
            turned['d'].copy(), 
            turned['l'].copy(), 
            turned['r'].copy()
        )
    
    return {
        'f': returned['t'].copy(),
        'l': np.rot90(returned['l'].copy(), -1),
        'r': np.rot90(returned['r'].copy(), 1),
        'b': np.rot90(returned['d'].copy(), 2),
        't': np.rot90(returned['b'].copy(), -2),
        'd': returned['f'].copy()
    }

# cube = {
#     'f': np.arange(1, 10).reshape(3,3),
#     'd': np.arange(10, 19).reshape(3,3),
#     'l': np.arange(19, 28).reshape(3,3),
#     't': np.arange(28, 37).reshape(3,3),
#     'r': np.arange(37, 46).reshape(3,3),
#     'b': np.arange(46, 55).reshape(3,3),
# }

# clockwise(
#     cube.copy(), 
#     cube['f'].copy(), 
#     cube['t'].copy(), 
#     cube['d'].copy(), 
#     cube['l'].copy(), 
#     cube['r'].copy()
# )