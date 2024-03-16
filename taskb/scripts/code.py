#!/usr/bin/python3
#(haschebang thing is used instead of mentioning extension. it's bin/bash)
#import sys
#sys.path.insert(1, '/home/prasad/catkin_noetic/catkin_ws/src/taskb/PointNet-PyTorch/models/')
import rospy
from sensor_msgs.msg import PointCloud2
import torch  
import torch.nn as nn
import pointcloud2 as pcl2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
import models.pointnet_classifier.PointNetClassifier as pnc

class Point_Cloud:
    def __init__(self):
        self.model = pnc(2000,3)
        self.model.load_state_dict(torch.load('/home/prasad/catkin_noetic/catkin_ws/src/taskb/PointNet-PyTorch/classifier_model_state.pth'),map_location='cpu')
    def pointcloud_callback(self,data):
        pts = list(pcl2.read_points(data, field_names=("x", "y", "z"), skip_nans=True))
        pt = pts[:2000]
        points = np.zeros(shape=(1,3,2000),dtype=np.float64)
        for i, element in enumerate(pt):
            points[0, 0, i] = element[0]  # Assign first element of tuple to first element of array
            points[0, 1, i] = element[1]  # Assign second element of tuple to second element of array
            points[0, 2, i] = element[2] 
        points_tensor = torch.from_numpy(points).float()
        with torch.no_grad(): 
            predictions = self.model(points_tensor)
        print(predictions.cpu().numpy())
        #points is a list of tuples:(x,y,z) [i chose that]
        

if __name__ == "__main__":
    ob1 = Point_Cloud()
    rospy.init_node("pointnet_ros_node")
    # Subscribe to the point cloud topic
    rospy.Subscriber("lidar_top", PointCloud2, ob1.pointcloud_callback)
    rospy.spin()  # Keep the node running
