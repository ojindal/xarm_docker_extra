# Use ROS 2 Humble base image
FROM osrf/ros:humble-desktop

# Install necessary tools and dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-pip \dwadad wa
    && rm -rf /var/lib/apt/lists/*

# Install Gazebo via script
RUN curl -sSL http://get.gazebosim.org | sh

# Install additional ROS packages
RUN apt-get update && apt-get install -y \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-moveit \
    && rm -rf /var/lib/apt/lists/*

# Update rosdep and ensure ROS package lists are up-to-date
RUN rosdep update && rosdep fix-permissions

# Create a workspace
RUN mkdir -p /root/dev_ws/src

# Navigate to the workspace's source directory
WORKDIR /root/dev_ws/src

# Clone the xarm_ros2 repository (humble branch)
RUN git clone https://github.com/xArm-Developer/xarm_ros2.git --recursive -b humble

# Clone the additional repository
RUN git clone https://github.com/ojindal/xarm_docker_extra.git

# Navigate to the xarm_ros2 repository directory
WORKDIR /root/dev_ws/src/xarm_ros2

# Update the repository and submodules
RUN git pull && git submodule sync && git submodule update --init --remote

# Install dependencies from rosdep
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && \
    apt-get update && \
    rosdep install --from-paths /root/dev_ws/src --ignore-src --rosdistro humble -y"

# Build the workspace
WORKDIR /root/dev_ws
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build"

# Setup the entrypoint
ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash && source /root/dev_ws/install/setup.bash && exec bash"]
