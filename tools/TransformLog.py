import sys
import datetime

class TransformLog:
    '''Python Object TransformLog, transforming sysu log and lab log'''
    SYSU = 'SYSU'
    LAB = 'LAB'

    def __init__(self):
        self.__mode = TransformLog.SYSU   # default mode is SYSU mode
        self.__filename_input = './data_input/log_sysu.txt' # default
        self.__filename_middle = './data_middle/transform_log_sysu.txt' # default

    # Set Mode for transform principle
    def __setMode(self, mode):    # 'sysu' mode or 'lab' mode
        self.__mode = mode

    def setModeSysu(self):
        self.__setMode(TransformLog.SYSU)

    def setModeLab(self):
        self.__setMode(TransformLog.LAB)
    # end of Set Mode

    def setFilename(self, filename_input, filename_middle):
        self.__filename_input = filename_input
        self.__filename_middle = filename_middle


    def transformLogSysu(self):
        if self.__mode != TransformLog.SYSU:
            print ('Mode isn\'t correct.')
            return

        fr = open(self.__filename_input, 'r')
        fw = open(self.__filename_middle, 'w')

        fr.readline()  # read lines unvaliable

        begin_date = None
        for line in fr:
            data = line.strip().split()  # split by space defaultly

            if len(data) < 9:
                print('Problem Data Entry.')
                continue

            # only deal with GET request
            request_type = data[5]
            if request_type != '\"GET':
                continue

            # Date String Format : [10/Apr/2013:00:00:09 +0800]
            date_str = '{0} {1}'.format(data[3][1:], data[4][:-1])
            current_date = datetime.datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z')

            if begin_date is None:
                begin_date = current_date

            # transform file format.
            minute_delta = int( (current_date - begin_date).seconds )
            # Format: access-ip time-span uri status response-size
            fw.write('{0} {1} {2} {3} {4}\n'.format(data[0], minute_delta, data[6], data[8], data[9]))

        fw.close()
        fr.close()

    def transformLogLab(self):
        if self.__mode != TransformLog.LAB:
            print ('Mode isn\'t correct.')
            return

        fr = open(self.__filename_input, 'r')
        fw = open(self.__filename_middle, 'w')

        # read lines unvaliable
        for i in range(4):
            fr.readline()


        begin_date = None
        for line in fr:
            data = line.strip().split()

            if len(data) < 20:
                print ('Problem data entry meet.')
                continue

            # only deal with GET request
            request_type = data[5]
            if request_type != 'GET':
                continue

            # get Elements from entry
            time_str = '{0} {1}'.format(data[0], data[1])
            current_date = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            if begin_date is None:
                begin_date = current_date
            time_span = int( (current_date - begin_date).seconds )
            uri = data[6]
            c_ip = data[10]
            status = data[16]
            response_size = data[19]

            fw.write( '{0} {1} {2} {3} {4}\n'.format(c_ip, time_span, uri, status, response_size) )

        fw.close()
        fr.close()


if __name__ == '__main__':
    mode = sys.argv[1]
    filename_input = sys.argv[2]
    filename_middle = sys.argv[3]

    transform_log = TransformLog()

    transform_log.setFilename(filename_input, filename_middle)
    if mode == TransformLog.SYSU:
        transform_log.setModeSysu()
        transform_log.transformLogSysu()
    else:
        transform_log.setModeLab()
        transform_log.transformLogLab()

















