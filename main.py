import cv2
import os

def generate_coloring_contours(input_image_path, output_image_path):
    """
    Генерує контури розмальовки з вхідного зображення.

    :param input_image_path: шлях до вхідного зображення
    :param output_image_path: шлях до збереження контуру
    """
    # Завантаження зображення
    image = cv2.imread(input_image_path, cv2.IMREAD_COLOR)

    # Перетворення в градації сірого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Розмиття для зменшення шуму
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Виявлення країв за допомогою алгоритму Canny
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

    # Інвертування кольорів для кращого вигляду
    inverted_edges = cv2.bitwise_not(edges)

    # Збереження результату
    cv2.imwrite(output_image_path, inverted_edges)
    print(f"Контури розмальовки збережено у файл: {output_image_path}")

def process_directory(input_directory, output_directory):
    """
    Обробляє всі зображення в каталозі, генеруючи контури розмальовки для кожного файлу.

    :param input_directory: каталог з вхідними зображеннями
    :param output_directory: каталог для збереження контурів
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f"contour_{filename}")
            generate_coloring_contours(input_path, output_path)

# Використання функції
process_directory("img", "output_img")
