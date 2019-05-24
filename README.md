# kinetinterface
Интерфейс для работы с программой KINET. 
interface.py содержит класс KinInterface, который принимает при инициализации следующие параметры:
1. Список частиц для отрисовки на первой оси.
2. Список частиц для отрисовки на второй оси.
3. Логическую переменную: если True, то перевести первую ось в логарифмический масштаб.
4. То же для второй оси.
5. Путь к программе KINET
6. Путь до файла образца с моделью расширения .kin.
7. Путь до папки, где будет создана модель и промежуточный файл с данными.

Метод интерфейса fullway позволяет рассчитать модель при данном давлении, соотношении реагентов, температуре и интервале расчета по времени.

В состав проекта входит также файл для jupyter-notebook, который содержит подробный пример того, как работать с интерфейсом. Советую его использовать.
