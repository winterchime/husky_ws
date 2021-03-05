# husky_ws

For obstacle avoidance only 
open husky_ws and launch gazebo, 
$cd husky_ws
$roslaunch husky_gazebo husky_maze.launch

in a new terminal i use the command below for obstacle avoidance algorithm node, 

$rosrun husky_control sensorlistenerlidar.py


For the Navigation portion,

$cd husky_ws

$roslaunch husky_gazebo husky_maze.launch

in a new terminal, launch amcl launch file
$cd husky_ws
$roslaunch husky_navigation amcl_demo.launch

new terminal launch rviz file

$cd husky_ws
$roslaunch husky_rviz rviz.launch


