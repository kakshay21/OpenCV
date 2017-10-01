import cv2
import time
import imutils
#from subprocess import call


cap = cv2.VideoCapture('05_05.mp4')

interestingMoments = []

videoStartTime = time.time()
firstFrame = None
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
#fgbg = cv2.createBackgroundSubtractorMOG2()
# threshold = dryRun(cap,fgbg) # need to implement a way to find threshold
# call(["./darknet","detector","test","cfg/combine9k.data","cfg/yolo9000.cfg"," ../yolo9000-weights/yolo9000.weights","data/3.png"])

eventTime = []
startTime = None

while(cap.isOpened()):
	ret,frame = cap.read()
	event = None
	if not ret:
		break

	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#fgmask = fgbg.apply(frame)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	if firstFrame is None:
		firstFrame = gray
		continue

	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]


	thresh = cv2.dilate(thresh, None, iterations=2)
	(_, contours, _) = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		# to ignore small chages
		if cv2.contourArea(c) < 500:
			continue
		event = True
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		eventTime.append(int(time.time()))

	if event is not None:
		interestingMoments.append(int(eventTime[-1] - videoStartTime))

	cv2.imshow("Security Feed", frame)
	
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break


cap.release()
cv2.destroyAllWindows()


interestingMoment = []
timepoint = []

for i in interestingMoments:
		if i in interestingMoment:
			continue
		else:
			interestingMoment.append(i)

timepoint.append(interestingMoment[0])

for j in range(1,len(interestingMoment)):
	#print("interestingMoment:{}".format(interestingMoment[j]))
	if (interestingMoment[j] - interestingMoment[j-1]) > 5:
		timepoint.append(interestingMoment[j-1])
		timepoint.append(interestingMoment[j])
timeToWatch = []
i=0
while i+1 < len(timepoint):
	watch = [timepoint[i],timepoint[i+1]]
	#print(watch)
	timeToWatch.append(watch)
	i=i+2
outputWr = ""
with open("output.txt", "w") as output:
	for i in timeToWatch:
		print("{}:{} - {}:{}".format(int(i[0]/60),i[0]%60,int(i[1]/60),i[1]%60))
		outputWr = outputWr + "{}:{} - {}:{}\n".format(int(i[0]/60),i[0]%60,int(i[1]/60),i[1]%60)
	output.write(outputWr)
	output.close()