from googletrans import LANGUAGES

languages = ['af', 'ak', 'am', 'ar', 'as', 'az', 'be', 'bg', 'bm', 'bn', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy', 'ga', 'gd', 'gl', 'gu', 'ha', 'hi', 'hr', 'hu', 'hy', 'ig', 'id', 'is', 'it', 'he', 'ja', 'yi', 'jv', 'ka', 'kk', 'km', 'kn', 'ko', 'ku', 'ky', 'lb', 'lg', 'ln', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'om', 'or', 'pa', 'pl', 'ps', 'pt', 'qu', 'ro', 'ru', 'rw', 'sd', 'si', 'sk', 'sl', 'sn', 'so', 'sq', 'sr', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'ti', 'tk', 'tr', 'tt', 'ug', 'uk', 'ur', 'uz', 'vi', 'xh', 'yo', 'zh', 'zu', 'in'] # твой список языков

supported_languages = set(LANGUAGES.keys())

unsupported_languages = [lang for lang in languages if lang not in supported_languages]

print(" ❌ Неподдерживаемые языки:", unsupported_languages)