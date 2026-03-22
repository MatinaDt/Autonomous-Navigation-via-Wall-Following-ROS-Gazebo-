# Mobile Robot Wall Following

##  Description

This project implements a wall-following algorithm for a mobile robot using ROS and Gazebo.

The robot uses sonar sensors to detect obstacles and maintains a constant distance from the wall while moving.

---

##  Files

* `follower.py` → main control algorithm
* `plots.py` → plots sensor data and velocities
* `mobile_partA.launch` → ROS launch file

---

##  Run

```bash
roslaunch mymobibot_gazebo mobile_partA.launch
rosrun your_package follower.py
```

---

##  Output

* Sonar distances over time
* Linear and angular velocities

---

##  Goal

Navigate around obstacles while keeping a fixed distance from the wall.

---
