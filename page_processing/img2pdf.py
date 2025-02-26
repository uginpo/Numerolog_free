import os
from PIL import Image
import fitz  # PyMuPDF
from loguru import logger


def create_pdf_from_images(client_name: str, input_folder: str, output_folder: str):
    """
    Создает PDF-файл из изображений, хранящихся в указанной папке.

    :param client_name: Имя клиента для названия выходного файла.
    :param input_folder: Путь к папке с изображениями.
    :param output_folder: Путь к папке для сохранения PDF-файла.
    """
    # Проверяем существование входной папки
    if not os.path.exists(input_folder):
        raise FileNotFoundError(
            f"Папка с изображениями не найдена: {input_folder}")

    # Проверяем существование выходной папки и создаем её, если она отсутствует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Собираем список файлов PNG в папке
    image_files = [f for f in os.listdir(input_folder) if f.endswith(".png")]
    if not image_files:
        raise ValueError("В папке нет изображений в формате PNG.")

    # Сортируем файлы по имени для правильного порядка страниц
    # Сортировка по номеру страницы
    image_files.sort(key=lambda x: int(x.split("-")[1].split()[0]))

    # Создаем PDF-документ
    pdf_document = fitz.open()

    for image_file in image_files:
        try:
            # Полный путь к изображению
            image_path = os.path.join(input_folder, image_file)

            # Открываем изображение и оптимизируем его размер
            with Image.open(image_path) as img:
                # Конвертируем в RGB для совместимости с PDF
                img = img.convert("RGB")
                # Масштабируем до размера A4 (опционально)
                img.thumbnail((2480, 3508))

                # Сохраняем временное изображение в JPEG для уменьшения размера
                temp_image_path = os.path.join(
                    input_folder, f"{os.path.splitext(image_file)[0]}.jpg")
                img.save(temp_image_path, "JPEG", quality=85, optimize=True)

            # Добавляем изображение как страницу в PDF
            rect = fitz.Rect(0, 0, 595, 842)  # Размер страницы A4
            page = pdf_document.new_page(width=rect.width, height=rect.height)
            page.insert_image(rect, filename=temp_image_path)

            # Удаляем временное изображение
            os.remove(temp_image_path)

        except Exception as e:
            logger.error(f"Ошибка при обработке изображения {image_file}: {e}")

    # Формируем имя выходного файла
    output_file = os.path.join(
        output_folder, f"Профайлинг для {client_name}.pdf")

    try:
        # Сохраняем PDF-документ
        pdf_document.save(output_file, garbage=4,
                          deflate=True)  # Оптимизация PDF
        pdf_document.close()

        logger.info(f"PDF-файл успешно создан: {output_file}")
    except Exception as e:
        logger.error(f"Ошибка при сохранении PDF-файла: {e}")
