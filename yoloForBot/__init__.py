from ultralytics import YOLO
import os

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')


def getResult(path):
    """
    从路径path中读取图片 让yolo识别
    :param path: 路径
    :return: 识别后图片根目录
    """
    results = model(path, save=True)
    outpath = r'runs/detect/'
    # print(os.listdir(outpath))
    end = [int(i.replace('predict', '')) for i in os.listdir(outpath) if i != "predict"]
    now = max(end) if len(end) != 0 else ""

    repath = f'runs/detect/predict{now}'
    print(repath)
    return repath



if __name__ == '__main__':
    getResult("d.jpg")
