from ultralytics import YOLO

model = YOLO('yolov8s.pt')

model.train(
    data='data.yaml',
    epochs=100,
    imgsz=640,
    batch=16,
    name='my_model'
)

model.export(format='pt',path='my_model.pt')
