from PIL import Image
from ultralytics import YOLO

model = YOLO('visdrone.pt')
#model = YOLO('dota8-obb.pt')
#model = YOLO('yolov8n.pt')
#model = YOLO('yolov8s.pt')
#model = YOLO('yolov8n-seg.pt')
#model = YOLO('yolov8s-seg.pt')
#model = YOLO('yolov8n-obb.pt')
#model = YOLO('yolov8s-obb.pt')
#model = YOLO('yolov8n-pose.pt')
#model = YOLO('dotav1.5.pt')
results = model("img\\cars-003.jpg")

for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')  # save image
#    print(im_array[0])
#    print(r.boxes)
#    print(r.masks)

