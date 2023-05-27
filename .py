# Pythonproject
#python programming project

#first detect a face
from deepface import Deepface
import matplotlib.pyplot as plt
#using tensorflow backend
img_path="deepface/tests/dataset/img1.jpg"
detectors=['opencv','ssd','dlib','mtcnn']
for dectecor in detectors:
  print(detectors)

img=Deepface.detectFace(img_path=img_path,detector_backend=detector)