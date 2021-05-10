import sys
import cv2
import csv

def video2img(pathInput, pathOutput, frame_rate, pathOutput_csv):
    vidcap = cv2.VideoCapture(pathInput)
    success,image = vidcap.read()
    count = 1403636579763555584  #start in this rand time
    frame_rate = 100000000//int(frame_rate) #represented in nanoseconds
    dim = (752, 480)
    csv_rows = [["timestamp [ns]", "filename"]]

    '''
    while success:
        # resize image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        # save image
        cv2.imwrite(pathOutput+"%d.png" % count, image)     # save frame as png file      
        # append to csv
        csv_rows.append([count, "%d.png" % count])

        success,image = vidcap.read()
        count += frame_rate

    with open(pathOutput_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_rows)
    '''

    with open(pathOutput_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp [ns]", "filename"])

        while success:
            # resize image
            image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
            # save image
            cv2.imwrite(pathOutput+"%d.png" % count, image)     # save frame as png file      
            # append to csv
            writer.writerow([count, "%d.png" % count])

            success,image = vidcap.read()
            count += frame_rate
    

def main():
    if (len(sys.argv) == 1):
        print("Ingrese directorio de entrada")
        return
    elif (len(sys.argv) == 2):
        print("Ingrese directorio de salida")
        return
    elif (len(sys.argv) == 3):
        print("Ingrese frame_rate")
        return

    pathInput  = sys.argv[1]
    pathOutput = sys.argv[2]
    frame_rate = int(sys.argv[3])
    pathOutput_csv = sys.argv[4]
    print("Directorio de entrada:", pathInput)
    print("Directorio de salida:" , pathOutput)
    print("Frame rate:" , frame_rate)
    print("Output csv:" , pathOutput_csv)

    #esecute
    video2img(pathInput, pathOutput, frame_rate, pathOutput_csv)

    print("Video Finished")

if __name__ == "__main__":
    main()