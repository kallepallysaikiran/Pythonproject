# Pythonproject
#python programming project

#first detect a face
from deepface import Deepface
import matplotlib.pyplot as plt
import time
#using tensorflow backend
img1_path="deepface/tests/dataset/img1.jpg"
img1_path="deepface/tests/dataset/img1.jpg"

detectors=['opencv','ssd','dlib','mtcnn']
for dectecor in detectors:
  obj=DeepFace.varify(img1_path,img2_path,detector_backend=detector)
  tic=time.time()

img=Deepface.detectFace(img_path=img_path,detector_backend=detector)
toc=time.time()

plt.imshow(img1)
plt.show()
plt.imshow(img2)
plt.show()
print(obj)
print("detector,"backend",toc-tic,"seconds")
print("+++++++++++++++++++++")
