import logging
import argparse


def process_text(text):
    logger.info("Исходный текст: %s", text)
    
    # Очищаем текст
    cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)
    logger.debug("Очищенный текст: %s", cleaned_text)
    
    # Разбиваем текст на слова и считаем их количество
    words = cleaned_text.split()
    word_counts = {}
    
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
            logger.debug("Добавлено слово: '%s' с частотой 1", word)
        else:
            word_counts[word] += 1
            logger.debug("Обновлена частота слова: '%s' до %d", word, word_counts[word])
    
    # Получаем 10 самых часто встречающихся слов
    top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]
    logger.info("Топ 10 слов: %s", top_words)
    
    return top_words

if __name__ == "__main__":
    # Настраиваем аргументы командной строки
    parser = argparse.ArgumentParser(description="Анализ текста и вывод 10 самых часто встречающихся слов.")
    parser.add_argument("text", type=str, help="Текст для анализа.")
    parser.add_argument("--log", type=str, choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], default="INFO", help="Уровень логгирования.")
    
    args = parser.parse_args()
    
    # Настраиваем логирование
    logging.basicConfig(level=getattr(logging, args.log), format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    
    # Обрабатываем текст
    top_words = process_text(args.text)
    
    # Выводим результат
    print(top_words)
