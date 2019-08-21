# fiducialControl
Controller code to read and process fiducials.
In order to use this, you will have to install the python3 version of ApirlTags:

pip3 install apriltag

This should install opencv in the process.  You will also need to install ZeroMQand pyyaml:

pip3 install pyzmq

pip3 install pyyaml

Or you can comment out the zeromq stuff if you want to do something different. 

While you can run with code with my camera settings, you'll eventually need to calibrate your own camera.  I recommend cloning this package and looking at the README.md

https://github.com/smidm/video2calibration

I've included the checkerboard.png file as well as 4 tags I know work in this repo.  If you want to work with the original C++ code rather than python, you can follow the instructions here:

https://people.csail.mit.edu/kaess/apriltags/

Finally, I found this article really helpful and tied together most of the components.  I had to look at the source code for the apriltags python library in order to figure out how to go from a homography matrix to a pose matrix, but I think the article answered everything else:

https://www.orangenarwhals.com/2018/04/getting-started-with-apriltags-on-ubuntu-16-04/




