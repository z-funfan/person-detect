from common import logger
import cv2
import yolo.yolo3_opencv as yo


def yolo_camera(video,
                label_path='./yolo/cfg/yolov3.txt',
                config_path='./yolo/cfg/tiny-yolo.cfg',
                weights_path='./yolo/cfg/tiny-yolo.weights',
                confidence_thre=0.5):
    while True:
        # 抓取每一帧图像
        # ret， 返回值，表示视频是否读完
        # frame， 实际图像帧
        ret, frame = video.read()
        yo.yolo_detect(frame, label_path, config_path, weights_path, confidence_thre=confidence_thre)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        yield frame


if __name__ == "__main__":
    logger.logger().info("启动主程序")
    video_captures = cv2.VideoCapture(0)
    frameGenerator = yolo_camera(video_captures, confidence_thre=0.4)
    for frame in frameGenerator:
        cv2.imshow('Object Detection', frame)

    # When everything is done, release the capture
    logger.logger().info('正在关闭摄像头')
    video_captures.release()
    cv2.destroyAllWindows()
