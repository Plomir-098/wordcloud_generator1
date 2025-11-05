

from wordcloud_utils import read_text_file, load_stopwords, clean_text, create_wordcloud
import os


def main():
  
    print("=== ГЕНЕРАТОР ОБЛАКА СЛОВ ===")
    print("1 - Использовать пример текста")
    print("2 - Указать свой файл")
    
    try:
        choice = input("Выберите опцию (1 или 2): ").strip()
        
        if choice == '1':
            sample_text = """
            Программирование на Python это увлекательный процесс. 
            Python позволяет создавать различные приложения и скрипты.
            Облака слов помогают визуализировать текстовые данные.
            Анализ текста важен для обработки естественного языка.
            Машинное обучение и искусственный интеллект развиваются быстро.
            """
            
            stopwords = load_stopwords()
            word_freq = clean_text(sample_text, stopwords)
            
            print(f"Обработано уникальных слов: {len(word_freq)}")
            print("Топ-5 слов:", list(word_freq.items())[:5])
            
            output_file = "sample_wordcloud.png"
            create_wordcloud(word_freq, output_file)
            
        elif choice == '2':
            file_path = input("Введите путь к текстовому файлу: ").strip()
            
            if not os.path.exists(file_path):
                print("Ошибка: файл не найден!")
                return
                
            text = read_text_file(file_path)
            
            if not text:
                print("Ошибка: не удалось прочитать файл!")
                return
                
            stopwords = load_stopwords()
            word_freq = clean_text(text, stopwords)
            
            print(f"Обработано уникальных слов: {len(word_freq)}")
            print("Топ-5 слов:", list(word_freq.items())[:5])
            
            output_name = input("Введите имя для файла (без .png): ").strip()
            output_file = f"{output_name}.png" if output_name else "wordcloud.png"
            
            create_wordcloud(word_freq, output_file)
            
        else:
            print("Ошибка: неверный выбор!")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()