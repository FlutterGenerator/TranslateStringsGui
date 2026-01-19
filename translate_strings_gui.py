import os
import xml.etree.ElementTree as ET
import asyncio
from googletrans import Translator
import re

# ---------- Перевод текста ----------
async def translate_text(translator, text, dest_lang):
    result = await translator.translate(text, dest=dest_lang)
    return result.text

# ---------- Исправление строк под Android ----------
def fix_android_string(text):
    if not text:
        return text

    # {something} -> %s
    text = re.sub(r'\{[^}]+\}', '%s', text)

    # Экранируем апострофы
    text = text.replace("\\'", "'")
    text = text.replace("'", "\\'")

    # Если понадобится:
    # text = re.sub(r'%(?!\d*\$?[sd])', '%%', text)

    return text

# ---------- Перевод одного strings.xml ----------
async def translate_strings_xml(input_file, dest_lang='ru'):
    print(f"\n🌍 Начинаю перевод на язык: {dest_lang}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    tree = ET.parse(input_file)
    root = tree.getroot()
    translator = Translator()

    translated_count = 0
    skipped_count = 0

    for string in root.findall('string'):
        if string.attrib.get('translatable', 'true').lower() == 'false':
            skipped_count += 1
            continue

        original_text = string.text
        if not original_text:
            continue

        try:
            translated = await translate_text(translator, original_text, dest_lang)
            fixed_text = fix_android_string(translated)
            string.text = fixed_text
            translated_count += 1
            print(f"  ✅ {original_text} → {fixed_text}")
            print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        except Exception as e:
            print(f"  ❌ Ошибка: {original_text} ({e})")
            print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    output_dir = f'values-{dest_lang}'
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, 'strings.xml')
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

    print(f"💾 Сохранено: {output_file}")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📊 Итог: переведено {translated_count}, пропущено {skipped_count}")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# ---------- Главная функция ----------
async def main():
    input_file = 'strings.xml'

    languages = ['af', 'ak', 'am', 'ar', 'as', 'az', 'be', 'bg', 'bm', 'bn', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy', 'ga', 'gd', 'gl', 'gu', 'ha', 'hi', 'hr', 'hu', 'hy', 'ig', 'id', 'is', 'it', 'he', 'ja', 'yi', 'jv', 'ka', 'kk', 'km', 'kn', 'ko', 'ku', 'ky', 'lb', 'lg', 'ln', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'om', 'or', 'pa', 'pl', 'ps', 'pt', 'qu', 'ro', 'ru', 'rw', 'sd', 'si', 'sk', 'sl', 'sn', 'so', 'sq', 'sr', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'ti', 'tk', 'tr', 'tt', 'ug', 'uk', 'ur', 'uz', 'vi', 'xh', 'yo', 'zh', 'zu'] # Добавь языки, на которые хочешь перевести

    print("🚀 Strings.XML Auto Translator")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📂 Файл: {input_file}")
    print(f"━━━━━━━━━━━━━━━━━━━━")

    tasks = [translate_strings_xml(input_file, lang) for lang in languages]
    await asyncio.gather(*tasks)
    
    print(f"🌐 Языков: {len(languages)}")
    print(f"━━━━━━━━━━━━━━")
    print("\n🎉 ГОТОВО! Все переводы завершены.")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

if __name__ == '__main__':
    asyncio.run(main())