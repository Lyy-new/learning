import face_recognition
import cv2
from ament_index_python.packages import get_package_share_directory

def main():
    # 获取资源文件路径
    default_image_path = get_package_share_directory('demo_python_service') + '/resource/default.jpg'
    
    # 使用OpenCV加载图片
    image = cv2.imread(default_image_path)
    if image is None:
        print("无法加载图像，请检查路径:", default_image_path)
        return
    
    # 使用face_recognition库找到人脸位置
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=2, model='hog')

    # 在图像中标记每个人脸的位置
    for top, right, bottom, left in face_locations:
        cv2.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 2)

    # 显示结果图像
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Detected face locations:", face_locations)

if __name__ == '__main__':
    main()
