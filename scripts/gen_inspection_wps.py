import numpy as np

n = 3
center_axis = [0, 0]
radius = 30
max_depth = 25
min_depth = 3
depth_n = 10

slices = np.linspace(0, np.pi / 2, n * 2, endpoint=False)
vertical = np.linspace(min_depth, max_depth, depth_n)

waypoints = []
for i in range(n):
    angle_up = slices[i * 2]

    x = center_axis[0] + (radius * np.cos(angle_up))
    y = center_axis[1] + (radius * np.sin(angle_up))

    for v in vertical:
        waypoints.append([x, y, -v, (angle_up - (np.pi / 2)) % (2 * np.pi)])
        #waypoints.append([x, y, -v, angle_up])
    
    angle_down = slices[(i * 2) + 1]

    x = center_axis[0] + (radius * np.cos(angle_down))
    y = center_axis[1] + (radius * np.sin(angle_down))

    for v in vertical[::-1]:
        waypoints.append([x, y, -v, (angle_down + (np.pi / 2)) % (2 * np.pi)])
        #waypoints.append([x, y, -v, angle_down])

with open('generated_waypoints.yaml', 'w') as f:
    for i in range(len(waypoints)):
        x, y, z, h = waypoints[i]
        f.write(f'''- point: [{x:0.2f}, {y:0.2f}, {z:0.2f}]
  max_forward_speed: {0.5 if i != 0 else 0.7}
  heading: {h if i != 0 else 0:0.3f}
  use_fixed_heading: {'true' if i != 0 else 'false'}
''')


    

