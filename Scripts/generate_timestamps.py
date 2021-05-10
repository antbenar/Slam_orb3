import sys
import cv2
import csv

def generate_timestamps(output_path, start, end, frame_rate):
    count = start  #start in this time
    frame_rate = 100000000//int(frame_rate) #represented in nanoseconds


    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp [ns]", "filename"])
        while count<=end:
            writer.writerow([count, "%d.png" % count])
            count += frame_rate

def main():
    if (len(sys.argv) == 1):
        raise Exception("Ingrese directorio de salida")
    
    if (len(sys.argv) == 2):
        raise Exception("Ingrese frame_rate")

    if (len(sys.argv) == 3):
        start = 1403636579763555584
        end   = 1403636590313554529
    else:
        start  = sys.argv[3]
        end    = sys.argv[4]

    output_path =   sys.argv[1]
    frame_rate  =   sys.argv[2]

    print("Directorio de salida",output_path)
    print("Frame_rate",frame_rate)

    #execute
    generate_timestamps(output_path, start, end, frame_rate)

    print("Csv creado")

if __name__ == "__main__":
    main()