from ultralytics import YOLO
import cv2
import numpy as np


def main():
    model = YOLO("./assets/yolov8n.pt")
    img_path = "assets/dunk.jpg"
    frame = cv2.imread(img_path)
    if frame is None:
        print(f"Erro: Não foi possível carregar a imagem {img_path}")
        return

    height = 450
    h, w = frame.shape[:2]
    scale = height / h
    width = int(w * scale)
    original_resized = cv2.resize(
        frame,
        (width, height)
    )

    results = model(frame)
    annotated_frame = results[0].plot()

    h_seg, w_seg = annotated_frame.shape[:2]
    segmentation_scale = height / h_seg
    segmented_width = int(w_seg * segmentation_scale)
    segmentada_resized = cv2.resize(
        annotated_frame,
        (segmented_width, height)
    )

    both_images = np.hstack((original_resized, segmentada_resized))

    cv2.imshow("Original e Segmentada", both_images)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
