2-Link Robot Inverse Kinematics
==========================

![rvizgrab](http://i.imgur.com/OjbZwAK.gif)

Reference for inverse kinematics formula: [A Mathematical Introduction to Robotic Manipulation](http://www.cds.caltech.edu/~murray/mlswiki/index.php/Main_Page "Reference").

This package simulates the inverse kinematics of a planar 2-link robot arm whose end-effector has to trace a circle of desired time period.

The `urdf/2linkrobot.urdf` file defines the model of the 2-link robot as per the following tree:
*  base
    *  arm1
         *  arm2
             *  endEffector

The launch file *display.launch* starts up all the nodes for this simulation and sets up the relevant parameters.  

Nodes:
*   `controller_node`: Publishes joint states theta1 and theta2 for the two continuous joints, as computed from the inverse kinematics formulas
*   `joint_state_publisher`: Use in conjunction with gui when debugging and verifying the robot urdf. Also publishes joint states theta1 and theta2, but from the gui.
*   `robot_state_publisher`: Takes joint states from either of the above two nodes and broadcasts transforms between the frames of the robot.
*   `tf_endEffector_node`: Publishes the transform from base to end-effector, to be used by *rviz* for animating the trajectory.
*   `rviz`: Opens the robot visualizer rviz.

Parameters:
*   `robot_description`: Parses and stores the robot's urdf in the parameter server
*   `use_gui`: "true" if you want to use the slider gui for testing the joint angles, "false" (default) if you want to use the controller_node instead. Associated substitution arg: *gui*
*   `controller_pub_rate`: `controller_node`'s private parameter for specifying the frequency (Hz) at which the desired joint states are to be published. Associated substitution arg: *js_pub_rate*
*   `period`: `controller_node`'s private parameter for specifying the time period for tracing the circle. Associated substitution arg: *circle_period*

Important topics:
*   `/joint_states`: Messages of type *sensor_msgs/JointState* are published to this topic by either the `controller_node` or the `joint_state_publisher`, and is subscribed by the `robot_state_publisher`. Contains the angles of the continuous joints.
*   `/visualization_marker`: Messages of type *visualization_msgs/Marker* are published to this topic by the `tf_endEffector_node`, and is subscribed by `rviz`. Contains the marker data for animation.
*   `/tf`: Messages of type *tf2_msgs/TFMessage* are published to this topic by the `robot_state_publisher`, and is subscribed by `rviz` and `tf_endEffector_node`. Contains tf data of the robot model as it moves.
