import numpy as np
import itertools

cities = ['Grimsby', 'Cherrytown', 'Norwich', 'Hillford', 'Middletown',
 'Tarmsworth', 'Murrayfield', 'Hogsfeet', 'Chester', 'Matlock']

distance = {}
distance['Grimsby'] = {'Cherrytown': 2.6, 'Hillford': 1.7}
distance['Cherrytown'] = {'Norwich': 0.7, 'Hillford': 2.2, 'Grimsby': 2.6}
distance['Norwich'] = {'Hillford': 2.4, 'Middletown': 0.5, 'Cherrytown': 0.7}
distance['Hillford'] = {'Grimsby': 1.7, 'Cherrytown': 2.2, 'Norwich': 2.4, 'Middletown': 2.0, 'Tarmsworth': 1.7}
distance['Middletown'] = {'Norwich': 0.5, 'Hillford': 2.0, 'Tarmsworth': 1.5, 'Murrayfield': 2.0, 'Hogsfeet': 1.5}
distance['Tarmsworth'] = {'Hillford': 1.7, 'Middletown': 1.5, 'Murrayfield': 2.1}
distance['Murrayfield'] = {'Tarmsworth': 2.1, 'Middletown': 2.0, 'Hogsfeet': 1.8, 'Matlock': 0.3}
distance['Hogsfeet'] = {'Middletown': 1.5, 'Murrayfield': 1.8, 'Chester': 2.0}
distance['Matlock'] = {'Murrayfield': 0.3, 'Chester': 1.4}
distance['Chester'] = {'Hogsfeet': 2.0, 'Matlock': 1.4}

def traveltime(path):
    steps = []
    for i in range(len(path) - 1):
        try:
            steps.append(distance[path[i]][path[i+1]])
        except:
            return 100
    return np.sum(steps)

#conditions
#end at chester and be under 9 hours
#stop at norwich under 4 hours
#stop at hogsfeet and matlock
#starts at Grimsby

paths = []
times = []
for i in range(3,10):
    for path in itertools.product(cities, repeat = i):
        if path[0] == 'Grimsby':
            if list(path)[len(path)-1] == 'Chester':
                if 'Hogsfeet' in path:
                    if 'Matlock' in path:
                        if 'Norwich' in path:
                            index = path.index('Norwich')
                            if traveltime(path[:index]) < 4:
                                times.append(traveltime(path))
                                paths.append(path)


