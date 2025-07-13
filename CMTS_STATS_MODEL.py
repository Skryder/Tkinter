
import json
import re
import Helpers

class CMTS_STATS_MODEL:

    def __init__(self):
        self.parse()


    def parse(self):
        
        ##file = open('test.txt', mode = 'r', encoding = 'utf-8-sig')
        ##input = file.readlines()
        ##file.close()

        #CM Index
        curr = self.clean(Helpers.find_line_by_keyword('test.txt', "CM Index"))
        print(curr)

        #Upstream Channels count
        curr = self.clean(Helpers.find_line_by_keyword('test.txt', "Ranging Status"))
        print(curr)

        #Downstream Channels count

        #Upstream Power

        #Upstream SNR

        #Upstream PER

        #Min_US_SNR

        #Upstream Channel Name

        #Upstream Frequency

        #Upstream Min Power

        #Upstream peak power

        #Downstream Power

        #Downstream SNR

        #DOwnstream PER

        #DOwnstream Micros

        #Downstream MER

        #DOwnstream Good Codewords

        #Downstream Corrected Codewords

        #DOwnstream Channel name

        #Downstream Frequency

        #Uptime

        #Status

        #CMTS

        #FIrmware

        #IP address

        #Arrival Time

        

    def clean(self, input):
        print(input)
        input = input.split(":")
        input[0] = input[0].strip()
        input[1] = input[1].strip("\r\n")
        input[1] = input[1].strip()
        print(input)
        return input


        
CMTS_STATS_MODEL()



