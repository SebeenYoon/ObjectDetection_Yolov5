# Train Code

python train.py --img 416 --batch 4 --epochs 10 --data ./datasets/data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name results



# Detect Code

python detect.py --weights ./runs/train/results/weights/best.pt --img 416 --conf 0.05 --source "./datasets/images/train"
