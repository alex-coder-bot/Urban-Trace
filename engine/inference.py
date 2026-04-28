from ultralytics import YOLO
import cv2

def run_detection(image_path):
    # Load your trained model weights
    model = YOLO("models/urban_yolo_v8.pt")
    
    # Run inference
    results = model(image_path)
    
    # Process the first result
    res = results[0]
    plot_img = res.plot() # Image with bounding boxes
    
    # Get highest confidence for the sidebar
    max_conf = 0
    if len(res.boxes.conf) > 0:
        max_conf = float(res.boxes.conf.max()) * 100
        
    return plot_img, round(max_conf, 2)
