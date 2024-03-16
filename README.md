# Take-Home

#Task 2

Another colleague of yours in lab wants your help. He is working on a target tracking challenge for which he would like
us to find a way to detect the other Voltas using LiDAR. To do this we want to take a look at deep learning based object
detection methods which use 3D LiDAR. As the LiDAR data is unstructured in nature, usage of CNNs is not possible
directly due to not having property of being permutationally invariant. To enable usage of NN on pointcloud, one of the
first pioneering work was PointNet. To learn more about all the challenges and how PointNet solved those one can refer
to this video.

#Task 2A : Converting dataset to .bag files

For inference use any sample Kitti or NuScenes dataset (depending upon the pre-trained PointNet model being used).
You need not to download the whole dataset just sample ones. You can use kitti2bag or nuscenes2bag converters to obtain
the bag file.

#Task 2B: Implement PointNet on ROS

Get the PointNet working on ROS’s point cloud data. You need not train the model and can run pre-trained model
available on the web for this purpose. Remember you need to make the PointNet inferences run over the stream of point
cloud coming off ROS topic.
