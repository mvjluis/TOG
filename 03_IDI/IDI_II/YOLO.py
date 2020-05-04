import turtle
from tkinter import messagebox
from PIL import Image
import imageio
from imageai.Detection import ObjectDetection

boxesList = []

detector = ObjectDetection()

# model_path = "Object detection/models/resnet50_coco_best_v2.0.1.h5"
model_path = "Object detection/models/yolo.h5"
# model_path = "Object detection/models/yolo-tiny.h5"
input_path = "Object detection/input/TestImage1.jpg"
output_path = "Object detection/output/OutputImage.jpg"

# detector.setModelTypeAsRetinaNet()
detector.setModelTypeAsYOLOv3()
# detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()  # detector.loadModel(detection_speed="fast") "normal","fast","faster","fastest","flash"


#######################################################################################################################
# # NORMAL


def normalDetection(boxesList, detector, input_path, output_path):
    detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path,
                                                minimum_percentage_probability=80, display_percentage_probability=False,
                                                display_object_name=True)
    for eachItem in detection:
        # print(eachItem["name"], " : ", eachItem["percentage_probability"], ":", eachItem["box_points"])
        boxesList.append(eachItem["box_points"])


#######################################################################################################################
# # EXTRACT IMAGES DETECTED
def extractDetection(boxesList, detector, input_path, output_path):
    detections, objects_path = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path,
                                                               minimum_percentage_probability=80,
                                                               display_percentage_probability=False,
                                                               display_object_name=True, extract_detected_objects=True)
    for eachItem, eachItemPath in zip(detections, objects_path):
        # print(eachItem["name"], " : ", eachItem["percentage_probability"], " : ", eachItem["box_points"])
        # print("Object's image saved in " + eachItemPath)
        boxesList.append(eachItem["box_points"])


#######################################################################################################################
# # TO DETECT CUSTOM OBJECTS
# customObjects = detector.CustomObjects(car=True, bus=True, truck=True)
# detections = detector.detectCustomObjectsFromImage(custom_objects=customObjects, input_image=input_path,
#                                                    output_image_path=output_path, minimum_percentage_probability=50,
#                                                    display_percentage_probability=False, display_object_name=True)
# for eachItem in detections:
#     print(eachItem["name"], " : ", eachItem["percentage_probability"], " : ", eachItem["box_points"])
#     boxesList.append(eachItem["box_points"])

#######################################################################################################################
## CONVERT TO GIF
#######################################################################################################################
image = [imageio.imread(input_path)]
imageio.mimsave('TEMPGif.gif', image)

#######################################################################################################################
## SET CREATED GIF AS BACKGROUND
#######################################################################################################################
im = Image.open('TEMPGif.gif')
width, height = im.size

screen = turtle.Screen()
screen.setup(width + 50, height + 50)
screen.bgpic("TEMPGif.gif")

# screen.update()

#######################################################################################################################
## TESTING THIS THINGY
#######################################################################################################################
answer = messagebox.askyesno(message="Extraer Imagenes Objetos", title="Testing this Thingy")
if answer:
    extractDetection(boxesList, detector, input_path, output_path)
else:
    normalDetection(boxesList, detector, input_path, output_path)


#######################################################################################################################
## DRAW DETECTED BOXES
#######################################################################################################################

def draw_box(crush, x1, y1, x2, y2, w, h):
    sizeX = x2 - x1
    sizeY = y2 - y1
    start_x = -(w / 2) + x1
    start_y = (h / 2) - y1
    crush.speed("fast")  # "slowest", "slow", "normal", "fast" & "fastest"
    crush.hideturtle()
    crush.penup()
    crush.pensize(5)
    crush.goto(start_x, start_y)
    crush.pendown()
    crush.pencolor("black")

    crush.forward(sizeX)
    crush.right(90)
    crush.forward(sizeY)
    crush.right(90)
    crush.forward(sizeX)
    crush.right(90)
    crush.forward(sizeY)
    crush.right(90)


crush = turtle.Turtle()

for i in boxesList:
    draw_box(crush, i[0], i[1], i[2], i[3], width, height)

turtle.mainloop()
