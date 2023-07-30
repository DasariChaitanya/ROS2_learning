#!/bin/bash
echo "Entrypoint check"

source /opt/ros/${ROS_DISTRO}/setup.bash
exec "$@"