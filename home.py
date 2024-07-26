import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome()
    try:
        query = input("Введите запрос для поиска на Википедии: ")
        driver.get("https://ru.wikipedia.org/wiki/{}".format(query))

        while True:
            paragraphs = driver.find_elements(By.TAG_NAME, "p")
            for i, paragraph in enumerate(paragraphs):
                print(f"Параграф {i + 1}: {paragraph.text}")
                if i == 2:
                    break

            print("\nВыберите действие:")
            print("1. Листать параграфы статьи.")
            print("2. Перейти на одну из связанных страниц.")
            print("3. Выйти из программы.")
            choice = input("Введите номер действия: ")

            if choice == '1':
                continue
            elif choice == '2':
                links = driver.find_elements(By.XPATH, "//a[@href and not(ancestor::table)]")
                related_links = [link for link in links if '/wiki/' in link.get_attribute('href')]

                if related_links:
                    print("\nВыберите связанную статью:")
                    for i, link in enumerate(related_links[:10]):
                        print(f"{i + 1}. {link.text}")

                    link_choice = input("Введите номер выбранной статьи: ")
                    if link_choice.isdigit() and 1 <= int(link_choice) <= len(related_links):
                        related_article = related_links[int(link_choice) - 1].get_attribute('href')
                        driver.get(related_article)
                    else:
                        print("Неверный выбор!")
                else:
                    print("Нет связанных статей.")
            elif choice == '3':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор!")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()