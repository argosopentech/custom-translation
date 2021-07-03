import argostranslate
from argostranslate import translate

text_to_translate = "Hello world. The previous sentence is a custom translation. Hello world."

def translate(s):
    from_lang_code = 'en'
    to_lang_code = 'es'
    from_lang = list(filter(lambda x: x.code == from_lang_code, argostranslate.translate.get_installed_languages()))[0]
    to_lang = list(filter(lambda x: x.code == to_lang_code, argostranslate.translate.get_installed_languages()))[0]
    translation = from_lang.get_translation(to_lang)
    return translation.translate(s)

def translate_custom(s, custom_translations):
    mappings = list(custom_translations.items())
    if len(mappings) == 0:
        return translate(s)
    mapping = mappings[0]
    i = s.find(mapping[0])
    if i < 0:
        return translate_custom(s, dict(mappings[1:]))
    return s[:i] + mapping[1] + translate_custom(s[i + len(mapping[0]):], custom_translations)

custom_translations = {
    'Hello world.': 'Hola Mars.'
}

print(translate_custom(text_to_translate, custom_translations))

