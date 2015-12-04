# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:43:59 2015

@author: briciola
"""

import re

def fix_lines(iterable):
        
    temp_list = []
    itr = iter(iterable)
    for line in itr:
        temp_list.append(re.sub(r'recordingId=[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{6}_[0-9]{3}Z_[0-9]*', "", line))

    itr = iter(temp_list)  # get an iterator
    

    while True:
        line = next(itr)
        cur = ""
        #catch the cases with text, and check for the unescaped newlines
        if line[0:5] == "text,":
            #the actual string argument is the 5th column
            text = line.split(",")[4]
            #keep collecting lines til you find the 
            #next one that ends with the single quote
            while text[-2:] != "'\n":
                if cur == "":
                    cur = line
                else:
                    cur = cur.rstrip('\r') + text
                text=next(itr)
            else:
                if cur == "":
                     #this is the case where there was no unintentional linebreak
                    cur = line
                else:
                     #this is the case where we collected the strings above
                    cur = cur.rstrip('\r') + text
            yield cur
            cur = ""
        else:
            #all the strings that don't start with "text," are well behaved, so pass along
            yield line
                
import os
import pandas as pd
import datetime as dt
path = "NEEMO20-Crew"




dfs = []
for filename in os.listdir(path):
    if filename.endswith(".log") and filename.startswith("2015"): 
        with open(path+"/" + filename, "rt") as file:
            print filename
            dl = []
            recordingId = filename[:-4]
            clientAddress = ""
            t_init = dt.datetime(2000,1,1)
            t = dt.datetime(2000,1,1)
            browser= ""
            for line in fix_lines(file):
             
                if line[0:2] == "t=":
                    t_init = dt.datetime.strptime(line[2:-2], "%Y-%m-%dT%H:%M:%S.%f")
                    t = t_init
                elif line[0:2] == "t+":
                    t = t+dt.timedelta(milliseconds = int(line[2:]))

                
                #ignoring these for now
                elif line[0:3] == "DOM":
                    pass
                elif line[0:6] == "window":
                   pass
                

                elif line[0:7] == "browser":
                    browser = line[8:-1]
                elif line[0:13] == "clientAddress":
                    clientAddress = line[14:-1]
                    
                #everything else is something we want to parse as an event
                else:  
                    event = {
                        "recordingId": recordingId,
                        "clientAddress": clientAddress,
                        "browser": browser,
                        "t":t
                    
                    }
                    if line[0:6] == "scroll":
                        event.update({
                            "event":"scroll",
                            "other":line[7:-1]
                        })
                        dl.append(event)
                    elif line[0:5] == "click":
                        event.update({
                            "event":"click",
                            "other":line[6:-1]
                        })
                        dl.append(event)
                    elif line[0:3] == "att":
                        event.update({
                            "event":"att",
                            "other":line[4:-1]
                        })
                        dl.append(event)
                    elif line[0:10] == "mouse,over":
                        event.update({
                            "event":"mouse,over",
                            "other":line[11:-1]
                        })
                        dl.append(event)
                    elif line[0:9] == "mouse,out":
                        event.update({
                            "event":"mouse,out",
                            "other":line[10:-1]
                        })
                        dl.append(event)
                    elif line[0:5] == "state":
                        event.update({
                            "event":"state",
                            "other":line[6:-1]
                        })
                        dl.append(event)
                    elif line[0:3] == "tap":
                        event.update({
                            "event":"tap",
                            "other":line[4:-1]
                        })
                        dl.append(event)
                    elif line[0:3] == "key":
                        event.update({
                            "event":"key",
                            "other":line[4:-1]
                        })
                        dl.append(event)
                    elif line[0:4] == "text":
                        event.update({
                            "event":"text",
                            "other":line[5:-1]
                        })
                        dl.append(event)
                    elif line[0:13] == "drag,dragging":
                        event.update({
                            "event":"drag,dragging",
                            "other":line[14:-1]
                        })
                        dl.append(event)
                    elif line[0:15] == "dragend,endDrag":
                        event.update({
                            "event":"dragend,endDrag",
                            "other":line[16:-1]
                        })
                        dl.append(event)
                    elif line[0:15] == "touch,touchmove":
                        event.update({
                            "event":"touch,touchmove",
                            "other":line[16:-1]
                        })
                        dl.append(event)
                    elif line[0:16] == "touch,touchstart":
                        event.update({
                            "event":"touch,touchstart",
                            "other":line[17:-1]
                        })
                        dl.append(event)
                    elif line[0:14] == "touch,touchend":
                        event.update({
                            "event":"touch,touchend",
                            "other":line[15:-1]
                        })
                        dl.append(event)
                    elif line[0:6] == "txtsel":
                        event.update({
                            "event":"txtsel",
                            "other":line[7:-1]
                        })
                        dl.append(event)
                    elif line[0:4] == "open":
                        event.update({
                            "event":"open",
                            "other":line[5:-1]
                        })
                        dl.append(event)
                    elif line[0:14] == "session-closed":
                        event.update({
                            "event":"session-closed",
                            "other":line[15:-1]
                        })
                        dl.append(event)
                    elif line[0:4] == "hold":
                        event.update({
                            "event":"hold",
                            "other":line[5:-1]
                        })
                        dl.append(event)
                    elif line[0:5] == "paste":
                        event.update({
                            "event":"paste",
                            "other":line[6:-1]
                        })
                        dl.append(event)
                    elif line[0:3] == "cut":
                        event.update({
                            "event":"cut",
                            "other":line[4:-1]
                        })
                        dl.append(event)
                    elif line[0:4] == "prop":
                        event.update({
                            "event":"prop",
                            "other":line[5:-1]
                        })
                        dl.append(event)
                    elif line == "\n" or line == "":
                        #all the files end with a blank line
                        pass
                        
                    else:
                        print line
            
            if len(dl) > 0:
                dfs.append(pd.DataFrame(dl))
                        
df = pd.concat(dfs)
df.to_csv("tidy.csv")
