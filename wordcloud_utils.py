"""
Модуль утилит для генерации облака слов
"""

import re
import os
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def read_text_file(file_path):
    """
    Чтение текста из файла
    
    Args:
        file_path (str): путь к файлу
        
    Returns:
        str: содержимое файла или пустая строка при ошибке
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return ""


def load_stopwords():
    """
    Загрузка стоп-слов для русского языка
    
    Returns:
        set: множество стоп-слов
    """
    stopwords = {
        'и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со', 'как', 'а', 
        'то', 'все', 'она', 'так', 'его', 'но', 'да', 'ты', 'к', 'у', 'же', 
        'вы', 'за', 'бы', 'по', 'только', 'ее', 'мне', 'было', 'вот', 'от', 
        'меня', 'еще', 'нет', 'о', 'из', 'ему', 'теперь', 'когда', 'даже', 
        'ну', 'вдруг', 'ли', 'если', 'уже', 'или', 'ни', 'быть', 'был', 
        'него', 'до', 'вас', 'нибудь', 'опять', 'уж', 'вам', 'ведь', 'там', 
        'потом', 'себя', 'ничего', 'ей', 'может', 'они', 'тут', 'где', 'есть', 
        'надо', 'ней', 'для', 'мы', 'тебя', 'их', 'чем', 'была', 'сам', 'чтоб', 
        'без', 'будто', 'чего', 'раз', 'тоже', 'себе', 'под', 'будет', 'ж', 
        'тогда', 'кто', 'этот', 'того', 'потому', 'этого', 'какой', 'совсем', 
        'ним', 'здесь', 'этом'
    }
    return stopwords


def clean_text(text, stopwords):
    """
    Очистка текста и подсчет частотности слов
    
    Args:
        text (str): исходный текст
        stopwords (set): множество стоп-слов
        
    Returns:
        dict: словарь {слово: частота}
    """
    text = text.lower()
    
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    
    words = text.split()
    
    # Фильтрация стоп-слов и коротких слов
    filtered_words = [
        word for word in words 
        if word not in stopwords and len(word) > 2
    ]
    word_freq = Counter(filtered_words)
    
    return dict(word_freq)


def create_wordcloud(word_freq, output_file):
    """
    Создание и сохранение облака слов
    
    Args:
        word_freq (dict): словарь частотности слов
        output_file (str): имя выходного файла
        
    Returns:
        str: путь к сохраненному файлу
    """
    try:
        wordcloud = WordCloud(
            width=1200,
            height=800,
            background_color='white',
            max_words=150,
            colormap='viridis',
            relative_scaling=0.5
        ).generate_from_frequencies(word_freq)
        
        os.makedirs('output', exist_ok=True)
        
        output_path = f'output/{output_file}'
        
        plt.figure(figsize=(12, 8))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Облако слов', fontsize=16, pad=20)
        plt.tight_layout()
        
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Облако слов сохранено как: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Ошибка создания облака слов: {e}")
        return ""


# Демонстрация работы модуля
if __name__ == "__main__":
    # Тестовый пример
    test_text = "Python программирование данные анализ визуализация текст слова"
    stops = load_stopwords()
    frequencies = clean_text(test_text, stops)
    print("Тест модуля:", frequencies)