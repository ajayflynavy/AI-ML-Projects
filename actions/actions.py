# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import requests

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

class Action_Default_Fallback_1(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Apologies, I couldn't get that, please try again")

        return []

class action_predict_p_acc_level(Action):

    def name(self) -> Text:
        return "action_utter_prediction"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

	
        desc = tracker.latest_message.get('text')

        parameters = {'description': desc }
	
        value = requests.get(url = 'http://127.0.0.1:5000/get_p_acc_lvl', params = parameters )

        p_acc_lvl = value.json()	

        dispatcher.utter_message(text=p_acc_lvl )

        
        return []