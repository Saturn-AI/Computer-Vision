# Welcome to Automatic Number Plate Recognition (ANPR) 🚗💡

Dive into the world of ANPR using the power of YOLOv8 combined with the simplicity of easyOCR. This guide will help you set up your environment, train your model for license plate detection, and perform detection and recognition on your chosen videos. Let's get started!

## Getting Started 🚀

#### Setting Up Your Environment
Use Python 3.7 for better result
First things first, let's install YOLOv8 and easyOCR. Open your terminal or command prompt and run the following commands:

```bash
pip install ultralytics==8.0.0
pip install easyocr
pip install opencv-contrib-python
```

Training Your Model for License Plate Detection
Now, let's train your model to become a license plate detection expert:

## Load a Pretrained Model

We recommend starting with a pretrained model to make your training process faster and more efficient. Here's how you can load the YOLOv8 model:

```python
from ultralytics import YOLO
model = YOLO('yolov8n.pt')  # This loads a pretrained model
```
## Train the Model

With your model loaded, it's time to train it on your license plate data:

```python
Copy code
results = model.train(data='data.yaml', epochs=200, imgsz=640) 
```
Here, we're training the model for 200 epochs with an image size of 640. Feel free to adjust these parameters based on your requirements.

## Testing Your Model
After training, you'll want to see how well your model performs:

Load Your Trained Model

Load the model you've just trained or any other pretrained model you wish to test:

```python
model = YOLO('ultralytics/runs/detect/train_model/weights/best.pt')
```
### Run Inference on a Video

Test your model on a video to see it in action:

```python
model.predict('test_vid.mp4', save=True, imgsz=320, conf=0.2)
```
## Performing Detection and Recognition
Ready to see everything come together? Use the following command to perform both detection and recognition on your video:

```bash
python predict_modified.py model='ultralytics/runs/detect/train_model/weights/best.pt' source='your_video_link.mp4'
```
Replace 'your_video_link.mp4' with the path to your video file, and you're all set!