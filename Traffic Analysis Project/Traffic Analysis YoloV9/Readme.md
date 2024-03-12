## Traffic Detection is more accurate with YOLO V9

1. First Download YOLOV9:

```
!git clone https://github.com/SkalskiP/yolov9.git
```

2. Go to yolov9 folder by:

```
%cd yolov9
```

3. Install The dependencies:

```
!pip install -r requirements.txt -q
```

4. Download The Models:

```
!wget  -P {HOME}/weights -q https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt
!wget -P {HOME}/weights -q https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt
!wget -P {HOME}/weights -q https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c.pt
!wget -P {HOME}/weights -q https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-e.pt
```
