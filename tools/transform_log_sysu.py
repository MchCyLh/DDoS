import sys
import datetime


if __name__ == '__main__':
    filename = sys.argv[1].strip()  # filename == log_sysu.txt
    middle_filename = 'transform_{0}.txt'.format(filename.split('.')[0])
    fr = open(filename, 'r')
    fw = open(middle_filename, 'w')

    fr.readline()   # read lines unvaliable
    
    begin_time = None

    for line in fr:
        data = line.strip().split() # split by space defaultly
        if begin_time is None:
            time_str = data[3].split('/')[2]
            year,hour,minute,second = time_str.split(':')
            begin_time = datetime.datetime(year, hour, minute, second)
            




    fw.close()
    fr.close()
