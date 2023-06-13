# 🤙🏻 Automatic License Plate Detection and Recognition ⚡️

![Using Easy YOLOv7 by Theos AI]

This a clean and easy-to-use implementation of [YOLOv7](https://github.com/WongKinYiu/yolov7) in PyTorch, made with ❤️ by [Theos AI](https://theos.ai).

Refer [Blog](https://blog.theos.ai) and [YouTube Channel](https://www.youtube.com/@theos-ai/)!

### Install all the dependencies
Always install the requirements inside a [virtual environment](https://docs.python.org/3/library/venv.html):
```
pip install -r requirements.txt
```
#### Fix dependencies
If you run into issues installing some dependencies, first make sure you installed them inside a virtual environment.
For cython-bbox, try installing it like this:
```
pip install -e git+https://github.com/samson-wang/cython_bbox.git#egg=cython-bbox
```

### Detect the image

```
python image.py
```

### Detect the webcam

```
python webcam.py
```

### Detect the video

```
python video.py
```

### Detect and OCR the image

```
python ocr_image.py
```

### Detect and OCR the video

```
python ocr_video.py
```

### Detect and OCR the Webcam

```
python ocr_webcam.py
```

Note: Project is a Modified Project from Easy-yolov7 by Theoas AI.
