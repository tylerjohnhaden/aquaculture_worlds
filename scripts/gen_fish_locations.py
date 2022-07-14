import numpy as np

n = 30
center_axis = [0, 0]
max_radius = 22
min_radius = 4
mean_radius = 18
std_radius = mean_radius / 4
max_depth = 25
min_depth = 3
orientiation_noise = 0.08
min_closeness = 5

fish_names = ['goldenfish', 'catfish']
too_close_count = 0

for fish_name in fish_names:

    fish_poses = []
    while len(fish_poses) < n:
        rand_angle = 2 * np.pi * np.random.random()
        rand_radius = min(max_radius, max(min_radius, np.random.normal(mean_radius, std_radius)))
        rand_depth = min_depth + ((max_depth - min_depth) * np.random.random())

        # x, y, z
        position = [
            center_axis[0] + (rand_radius * (np.cos(rand_angle))),
            center_axis[1] + (rand_radius * (np.sin(rand_angle))),
            -rand_depth,
        ]

        # roll, pitch, yaw
        orientation = [
            np.random.normal(0, orientiation_noise) % (2 * np.pi), 
            np.random.normal(0, orientiation_noise) % (2 * np.pi), 
            (np.random.normal(0, orientiation_noise) + (np.pi / 2) + rand_angle) % (2 * np.pi),
        ]

        if fish_name == 'goldenfish':
            orientation[0] += (np.pi / 2)

        for fish_pose in fish_poses:
            closeness = np.sqrt(
                ((position[0] - fish_pose[0]) ** 2) + 
                ((position[1] - fish_pose[1]) ** 2) + 
                ((position[2] - fish_pose[2]) ** 2)
            )

            if closeness <= min_closeness:
                too_close_count += 1
                break
        else:
            fish_poses.append([*position, *orientation])

    
    for i, fish_pose in enumerate(fish_poses):
        x, y, z, r, p, yaw = fish_pose
        print(f'<include><name>{fish_name}{i}</name><uri>model://{fish_name}</uri><pose>{x:0.2f} {y:0.2f} {z:0.2f} {r:0.2f} {p:0.2f} {yaw:0.2f}</pose></include>')
print(f'{too_close_count} were too close')

