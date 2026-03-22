# Mobile Robot Wall Following (ROS/Gazebo)

## Overview

This project implements a wall-following controller for a differential-drive mobile robot using ROS and Gazebo.

The objective is to achieve:

* Stable wall following
* Constant distance from obstacles
* Smooth and continuous motion

The system uses sensor-based feedback control to navigate in an environment with walls.

---

## Problem Description

The robot operates in a bounded environment with obstacles and is required to:

* Move parallel to the walls
* Maintain a constant distance from them
* Complete a full loop around the environment

Key constraints:

* Limited sensing using sonar sensors
* No global map or planning
* Reactive (real-time) control
* Differential-drive kinematics

---

## System
<p align="center">
  <img src="images/Wall Following.png" width="600">
</p>

The robot is equipped with:

* Ultrasonic (sonar) sensors
* IMU

The control inputs are linear and angular velocity.

---
## Control Architecture
<p align="center">
  <img src="images/Control Architecture.png" width="600">
</p>

---

## Methodology

### 1. Wall approaching

The robot starts from the center and moves forward with constant velocity until it detects a nearby wall using front sensors.

---

### 2. Wall following control

A proportional controller regulates the angular velocity based on sonar measurements.

Primary control law:

ω₁ = kₚ₁(d_FR − d_FR_ref)

---

### 3. Corner handling (secondary behavior)

When approaching corners, an additional correction term is activated:

ω₂ = kₚ₂(d_FL − d_FL_ref)

---

### 4. Combined control law

The final angular velocity is:

ω = ω₁ + u · ω₂

where u is a switching variable that activates corner correction.

---

## Technologies Used

* ROS
* Gazebo
* Python
* NumPy


## Project Structure

```id="s7k2m1"
mymobibot_wall_following/
├── launch/
│   └── mobile_partA.launch
├── scripts/
│   ├── follower.py
│   └── plots.py
├── CMakeLists.txt
├── package.xml
└── README.md
```

---

## How to Run

Start ROS:

```bash id="l3q8z2"
roscore
```

Launch simulation:

```bash id="n8x2r5"
roslaunch mymobibot_gazebo mobile_partA.launch
```

Run controller:

```bash id="p4y1k9"
rosrun your_package follower.py
```

The robot will:

* Approach the wall
* Follow it while maintaining a constant distance
* Navigate around corners

---

## Results

The controller achieves stable wall-following with smooth motion and effective cornering.

Typical observations:

* Distance measurements stabilise around reference values
* Angular velocity increases near corners
* Initial transient until the wall is detected
* 
<img src="images/sonar.png" width="45%">
<img src="images/velocity.png" width="45%">

---

## Key Contributions

* Implementation of reactive wall-following control in ROS
* Use of sensor-based feedback for real-time navigation
* Integration of control and simulation in Gazebo

---

## Notes

This project was developed as part of a Robotics course focusing on robot systems and control.
