
# pip install ultalytics 

from ultralytics import YOLO

# Load a model
model = YOLO("best_steles.pt") 


# Predict with the model
results = model("/Users/ayoub/Downloads/Final_DL2-main/images/19636-31.JPG", save=True, show_conf=False, show_labels=False, show_boxes=False)  # predict on 1 image