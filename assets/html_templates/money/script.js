document.addEventListener("DOMContentLoaded", function() {
  const elements = document.querySelectorAll('.number');
  const stepX = 700; // Шаг между колонками
  const stepY = 700; // Шаг между строками
  const startX = 100; // Начальная X-координата
  const startY = -3300; // Начальная Y-координата
  const centerX = 1152; // Центральная точка (координата из .main_vtx)

  elements.forEach((element) => {
    const number = parseInt(element.getAttribute('data-number'));
    let left, top;

    switch(number) {
      case 1: // Вершина треугольника
        left = centerX;
        top = startY;
        break;
      case 2: // Левая сторона треугольника
        left = startX;
        top = startY + stepY;
        break;
      case 3: // Правая сторона треугольника
        left = startX + 2 * stepX;
        top = startY + stepY;
        break;
      case 4: // Левый нижний угол
        left = startX;
        top = startY + 2 * stepY;
        break;
      case 5: // Центр нижней строки
        left = centerX;
        top = startY + 2 * stepY;
        break;
      case 6: // Правый нижний угол
        left = startX + 2 * stepX;
        top = startY + 2 * stepY;
        break;
    }

    // Устанавливаем позицию
    element.style.left = `${left}px`;
    element.style.top = `${top}px`;
  });
});