# husky_ws

Obstacle Avoidance Only 
# open husky_ws and launch gazebo 
```bash
cd husky_ws
```
```bash
roslaunch husky_gazebo husky_maze.launch
```

Obstacle Avoidance Algorithm Node 

```bash
rosrun husky_control sensorlistenerlidar.py
```

Navigation

Shell #1
```bash
cd husky_ws
```
```bash
roslaunch husky_gazebo husky_maze.launch
```

Shell #2
```bash
cd husky_ws
```
```bash
roslaunch husky_navigation amcl_demo.launch
```

Shell #3
```bash
cd husky_ws
```
```bash
roslaunch husky_rviz rviz.launch
```

