import sys

class UriDict:
    '''Python Object UriDict, helping make uri dictionary from experimental data.'''
    def __init__(self):
        self.__filename_inputs = [] # file format: ip span uri status size
        self.__filename_uri_dict = './data_middle/uridict.txt'
        self.__next_id = 0
        self.__uri_dict_in_mem = {}

    def setFilenameUriDict(self, filename_uri_dict):
        self.__filename_uri_dict = filename_uri_dict

    def setFilenameInputs(self, filename_inputs):
        self.__filename_inputs = filename_inputs

    @staticmethod
    def uriAdjust(uri):
        # special case: uri is /
        if len( uri ) > 1 and uri[-1] == '/':
            return uri[:-1]
        else:
            return uri

    # Must be used after setFilenameInputs and setFilenameUriDict method.
    def readUriDict(self):

        fr = open( self.__filename_uri_dict , 'r' )

        for line in fr:
            # get entry: id uri
            data = line.strip().split() # default by space
            if len(data) != 2:
                print ('Entry in uridict is wrong.')
                continue
            id, uri = int(data[0]), data[1]

            if uri not in self.__uri_dict_in_mem.keys():
                self.__uri_dict_in_mem.__setitem__(uri, id)

            self.__next_id = id + 1 if self.__next_id <= id else self.__next_id

        fr.close()


    # Must be used after readUriDict Method.
    def updateUriDict(self):

        fa = open( self.__filename_uri_dict, 'a' )  # update uri dict file

        for filename in self.__filename_inputs:
            fr = open ( filename, 'r' )

            for line in fr:
                data = line.strip().split()
                if len(data) != 5:
                    print ('Entry format is not correct.')
                    continue

                # update uri dict
                uri_adjusted = UriDict.uriAdjust(data[2])

                if uri_adjusted not in self.__uri_dict_in_mem.keys():
                    self.__uri_dict_in_mem.__setitem__(uri_adjusted, self.__next_id)
                    self.__next_id += 1
                    fa.write( '{0} {1}\n'.format(self.__uri_dict_in_mem[uri_adjusted] , uri_adjusted) )

            fr.close()

        fa.close()

if __name__ == '__main__':
    filename_uri_dict = sys.argv[1]
    filename_inputs = sys.argv[2:]

    # debug
    print (filename_inputs)

    # create uri_dict and set preinfo
    uri_dict = UriDict()
    uri_dict.setFilenameUriDict(filename_uri_dict)
    uri_dict.setFilenameInputs(filename_inputs)

    uri_dict.readUriDict()
    uri_dict.updateUriDict()

