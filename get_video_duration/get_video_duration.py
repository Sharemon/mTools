import cv2
import os


def calculate_duration(filename):
    cap = cv2.VideoCapture(filename)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fcount = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    duration = fcount / fps
    return duration



if __name__ == '__main__':
    folder = "G:\\学习\\4、自动驾驶环境感知【最新】\\"
    format = ".mp4"

    outf = open("./duration.csv", "w")

    for root,dirs,files in os.walk(folder):
        for file in files:
            if file[-4:] == format:
                raw_path = os.path.join(root, file)
                print(raw_path)
                duration = calculate_duration(raw_path)
                outf.write(raw_path + "," + str(duration))

    outf.close()