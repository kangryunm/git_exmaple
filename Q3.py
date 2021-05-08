'''
시작 시각 : 21:45
종료 시각 : 23:00

Google Drive > 20년 화성대회 > 로깅 영상 > 정지선 인식용 영상에 업로드된 영상을 기반으로,
해당 영상에서 정지선이 인식되면 "Stop"을 출력하는 프로그램을 작성해 주세요.

이미지가 아니라 영상을 로드하셔서 처리해야 하며, 영상은 Repository에 Push하지 말아주세요.

실제 테스트 시에는 해당 Google Drive에 있는 영상 파일을 파일명 변경 없이 사용할 예정입니다.
최상 폴더에 영상을 첨부했을 때 바로 코드를 실행해서 결과물을 볼 수 있도록 작성해 주세요.
'''
import cv2
import numpy as np

def check_stop_line(img):

    front_cam = img  # 정면 Camera raw data를 받는다.
    cv2.imshow("front_cam", front_cam)
    img_front = front_transform(front_cam)  # 받은 이미지를 원근 변환한다.
    cv2.imshow("img_front", img_front)
    img_bin = detect_rgb(img_front)  # 원근 변환한 이미지를 이진화한다.
    cv2.waitKey(1)
    return get_stop_line(img_bin)  # 이진화된 이미지를 get_stop_line를 이용해 정지선을 검출한다.

def get_stop_line(img_bin):
    height, width = img_bin.shape[:2]   # (480, 640)

    # 일정한 사각형 지역을 설정한다.
    left_high = (int(0.2 * width), int(0.88 * height))
    right_low = (int(0.8 * width), int(0.9 * height))
    Area = (right_low[0] - left_high[0]) * (right_low[1] - left_high[1])
    s_img = img_bin[left_high[1]:right_low[1], left_high[0]:right_low[0]]
    cv2.imshow("s_img", s_img)

    nums_flatten = s_img.reshape(-1)
    num = cv2.countNonZero(nums_flatten)

    # 사각형 지역 안에 일정 비율 이상 하얀 픽셀이 존재하면 정지선으로 판단한다.
    if num > int(Area * 0.8):
        print("stop")
        return True
    else:
        return False

def front_transform(img_front):
    height, width = img_front.shape[:2]

    pts1 = np.float32([(150, 360),
                       (0, 465),
                       (640, 465),
                       (500, 360)])

    # 실제 측정한 카메라 시야각을 바탕으로 pts1에서 pts2로 원근변환을 진행합니다.
    pts2 = np.float32([(0 * width, 0 * height),
                       (0 * width, 1 * height),
                       (1 * width, 1 * height),
                       (1 * width, 0 * height)])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    wrapped_img = cv2.warpPerspective(img_front, matrix, (width, height), flags=cv2.INTER_CUBIC + cv2.INTER_LINEAR)
    #cv2.imshow("wrapped_img", wrapped_img)
    return wrapped_img

def detect_rgb(img):
    mask = cv2.inRange(img, np.array([160,160,160]), np.array([255,255,255]))
    #cv2.imshow("mask",mask)
    return mask


if __name__ == '__main__':
    file_path = 'C:/Users/moonk/Desktop/-/HEVEN/stopline.mp4'
    cap = cv2.VideoCapture(file_path)

    while cap.isOpened():
        ret, front = cap.read()
        check_stop_line(front)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

