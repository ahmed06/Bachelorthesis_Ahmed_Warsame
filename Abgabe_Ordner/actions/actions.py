# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Dict, Text, Any, List, Union, Type, Optional

import typing
import logging
import requests
import json
import csv

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher





from datetime import datetime, date, time, timedelta



    


class ActionPDFReader(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return 'action_answer'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        # Load slot value from Tracker Object into the variable theme and transform slot value into low case 
        theme = tracker.get_slot('theme')
        theme_lowercase = theme.lower()

        
        # open the q&aLecturePr1.csv file and search through the row Key  
        with open('q&aLecturePr1.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                text_lowcase = row['key'].lower()
        # if the slot value and the key value is the same, a message will be send back to the User with the method dispatcher.utter_message()  
                if theme_lowercase in text_lowcase:
                    message = row['content'].replace("\\n\\n", "\n").replace("\\n\\n\\n", "\n").replace("\\n", "\n").replace("\\n\\n\\n\\n", "\n").replace("\\n", "\n").replace("\\n\\n\\n\\n\\n", "\n")
                    dispatcher.utter_message(message)


                    


class ActionDate(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return 'action_date'

    def run(self, dispatcher, tracker, domain):
        now = datetime.now() # current date and time
        today = now.strftime("%d/%m/%Y")
        dispatcher.utter_message("Heute ist der {}".format(today)) #send the message back to the user

class ActionTime(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return 'action_time'

    def run(self, dispatcher, tracker, domain):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        dispatcher.utter_message("Es ist gerade {} Uhr".format(current_time)) #send the message back to the user
