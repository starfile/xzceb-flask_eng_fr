"""Translate from English to French or from French to English using IBM Watson API."""

import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function translates English to French.
    """

    if not english_text:
        return None

    translation = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()

    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    """
    This function translates French to English.
    """

    if not french_text:
        return None

    translation = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()

    english_text = translation['translations'][0]['translation']

    return english_text
