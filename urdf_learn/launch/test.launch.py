import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, Shutdown
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution                                    
from launch_ros.actions import Node
from launch_ros.substitutions import ExecutableInPackage, FindPackageShare
from launch.conditions import IfCondition, UnlessCondition, LaunchConfigurationEquals, LaunchConfigurationNotEquals
import xacro

def generate_launch_description():
    ld = LaunchDescription()
    
    pkg_path = os.path.join( get_package_share_directory("urdf_learn"))
    xacro_file = os.path.join(pkg_path,"urdf","bot.urdf.xacro")
    # des = xacro.process_file(xacro_file).toxml()
    robot_description_config = Command(['xacro ',xacro_file])
    params = {'robot_description' : robot_description_config }
    node_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output = 'screen',
        parameters=[params]
    )


    # Launch arg to start a joint state publisher gui
    joint_state_gui_arg = DeclareLaunchArgument(name = 'joint_state_gui_arg',
                                                default_value = 'True',
                                                description='Flag to enable joint_sate_publisher_gui')
    node_joint_state_pub  = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name = 'joint_state_pub',
        condition = UnlessCondition(LaunchConfiguration('joint_state_gui_arg'))
    )

    node_joint_state_pub_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name = 'joint_state_pub_gui',
        condition = LaunchConfigurationEquals('joint_state_gui_arg','True')
    )
    
    rviz_file = os.path.join(pkg_path,'config','view_robot.rviz')
    rviz_config =   DeclareLaunchArgument(name='rvizconfig',
                              default_value=rviz_file,
                              description='Path to rviz config file')

    rviz_node = Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', LaunchConfiguration('rvizconfig')],
            on_exit=Shutdown()
        )
   
    ld.add_action(node_state_pub)
    ld.add_action(joint_state_gui_arg)
    ld.add_action(node_joint_state_pub)
    ld.add_action(node_joint_state_pub_gui)
    ld.add_action(rviz_config)
    ld.add_action(rviz_node) 

    return ld