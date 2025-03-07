document.addEventListener("DOMContentLoaded", function() {
  const elements = document.querySelectorAll('.number');
  const stepX = 700; // Шаг между колонками
  const stepY = 700; // Шаг между строками
  const startX = 100; // Начальная X-координата
  const startY = -3300; // Начальная Y-координата

  elements.forEach((element) => {
    const number = parseInt(element.getAttribute('data-number'));
    const group = Math.floor((number - 1) / 3); // Группа (0, 1, 2)
    const positionInGroup = (number - 1) % 3; // Позиция в группе (0, 1, 2)

    // Рассчитываем координаты
    const left = startX + (group * stepX);
    const top = startY + (positionInGroup * stepY);

    // Устанавливаем позицию
    element.style.left = `${left}px`;
    element.style.top = `${top}px`;
  });
});