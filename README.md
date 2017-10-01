## OpenCV
### *Requirements*
#### openCV 3.0 or greater
#### imutils
#### [this video](https://drive.google.com/file/d/0B2vPCVjlmUOsa2otcnJMbmtKRFE/view?usp=sharing)

### *Approach*
#### Approach 1:
You can use Darknet model to recognize the image but it's computationally heavy task and can't run it on every frame.
Besides, Darknet model is not compiled in openCV, so you can trigger it but the question is How to get the result back? 
I was amazed at its accuracy and wanted to use it so badly in this project but every one frame costs me the 6-second 
loss of the time in computing. 
![alt ](https://github.com/kakshay21/OpenCV/blob/master/predictions.png)
As you can see very good prediction.

#### Approach 2:
Use some predefined algorithm to subtract the background from the video and detect the change in the scene. 
[Here](http://docs.opencv.org/3.3.0/db/d5c/tutorial_py_bg_subtraction.html) is a good tutorial for this.
These actually work well even with the shadow. But the problem with this approach is the video we have to refresh
the scene every 5 sec. So any predefined algorithm like above mentioned takes first 120 frames to set threshold and 
subtract it frame by frame. Only problem, the video we are working with is, it refreshes the scene every 5 sec. 
So even with the no activity in the video, we'll find something like this

#### Approach 3:
Straightforward, just use the approach of the above algorithm and fit it with the current scenario. pretty easy, right?
Let's see in detail.

Just convert the frame into gray one and make a threshold image after blurring it to a bit.
Now subtract it frame by frame with the current frame.

Voila! It's working.

![alt ](https://github.com/kakshay21/OpenCV/blob/master/detect.png)
