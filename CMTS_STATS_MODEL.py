
import json
import re
import Helpers

class CMTS_STATS_MODEL:

    def __init__(self):
        self.parse_from_file('test.txt')


    

    def parse_from_file(self, filename):
        
        try:

            file = open(filename, mode = 'r', encoding = 'utf-8-sig')
            ##input = file.readlines()
            ##file.close()

            #CM Index
            cm_id = Helpers.clean(Helpers.find_line_by_keyword_open_file(filename, "CM Index"))
            print(cm_id)

            #Upstream Channels count
            ranging = Helpers.clean(Helpers.find_line_by_keyword_open_file(filename, "Ranging Status"))
            usCount = ranging.count("success")
            print(usCount)

            #Downstream Channels count
            dsChannels = Helpers.find_line_by_keyword_open_file(filename, "Downstream Channel")
            print(dsChannels)
            dsCount = dsChannels.count("DS")
            print(dsCount)

            #Upstream Power
            usTx = Helpers.clean(Helpers.find_line_by_keyword_open_file(filename, "Upstream Transmit Power"))
            print(usTx)

            #Upstream SNR
            usSNR = Helpers.clean(Helpers.find_line_by_keyword_open_file(filename, "Upstream SNR"))
            print(usSNR)

            #Upstream PER
            usPER = Helpers.clean(Helpers.find_line_by_keyword_open_file(filename, "Upstream PER"))
            print(usPER)

            #Min_US_SNR
            usSNR_Min = Helpers.clean(Helpers.find_line_by_keyword_open_file(filename, "Minimum Upstream SNR"))
            print(usSNR_Min)

            #Upstream Channel Name
            us_id = Helpers.clean(Helpers.find_line_by_keyword_open_file(filename, "Upstream Channel"))
            print(us_id)

            #Upstream Frequency Upstream Frequency(MHz)          : 28.40      22.00      25.20      31.60 
            usFrq = Helpers.clean(Helpers.find_line_by_keyword_open_file(filename, "Upstream Frequency"))
            print(usFrq)

            #Upstream Min Power
            usMin = Helpers.clean(Helpers.find_line_by_keyword_open_file(filename, "Minimum Transmit Power"))
            print(usMin)

            #Upstream peak power
            usMax = Helpers.clean(Helpers.find_line_by_keyword_open_file(filename, "Peak Transmit Power"))
            print(usMax)

            #Downstream Power
            dsTx = Helpers.breakup(Helpers, Helpers.find_line_by_keyword_open_file(filename, "Downstream Transmit Power"))
            print(dsTx)

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

            
        except Exception as e:
            print(e)
        finally:
            file.close()


    def parse_from_clipboard(input):
        try:
        #CM Index
            cm_id = Helpers.clean(Helpers.find_line_by_keyword(input, "CM Index"))
            print(cm_id)
            #Upstream Channels count
            ranging = Helpers.clean(Helpers.find_line_by_keyword(input, "Ranging Status"))
            usCount = ranging.count("success")
            print(usCount)

            #Downstream Channels count
            #curr = self.clean(Helpers.find_line_by_keyword_open_file(input, "Downstream Channel"))
            #curr = curr.split(":")

            #curr = Helpers.find_line_by_keyword(file, "Downstream Channel")
            dsChannels = Helpers.find_line_by_keyword(input, "Downstream Channel")
            print(dsChannels)
            dsCount = dsChannels.count("DS")
            print(dsCount)
            #Upstream Power

            usTx = Helpers.clean(Helpers.find_line_by_keyword(input, "Upstream Transmit Power"))
            print(usTx)
            #Upstream SNR

            usSNR = Helpers.clean(Helpers.find_line_by_keyword(input, "Upstream SNR"))
            print(usSNR)
            #Upstream PER

            usPER = Helpers.clean(Helpers.find_line_by_keyword(input, "Upstream PER"))
            print(usPER)

            #Min_US_SNR
            usSNR_Min = Helpers.clean(Helpers.find_line_by_keyword(input, "Minimum Upstream SNR"))
            print(usSNR_Min)

            #Upstream Channel Name


            #Upstream Frequency Upstream Frequency(MHz)          : 28.40      22.00      25.20      31.60 
            usFrq = Helpers.clean(Helpers.find_line_by_keyword(input, "Upstream Frequency"))
            print(usFrq)

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

        except Exception as e:
            print(e)




        
CMTS_STATS_MODEL()



