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

Метод класса с названием fullway позволяет рассчитать модель при данном давлении, соотношении реагентов, температуре и интервале расчета по времени.

fullway принимает следующие параметры: (давление, [список соотношения реагентов], [названия реагентов], температура, время докуда рисовать, save=False или True)

В состав проекта входит также файл для jupyter-notebook, который содержит подробный пример того, как работать с интерфейсом. Советую его использовать. 

При первом запуске, может потребоваться указать папку прямо в KINETE из пункта 7 самостоятельно. 

Дианой найдены следующие баги:
1. Надо запускать русский KINET, а не англицкий. Найдите русскую версию.
2. Когда вы вызываете fullway, если хотите сохранить файл, поставьте в конце в качестве параметра после запятой save=True. 
3. csv должен сохраняться в формате en. Проверьте, чтобы это было так. Если не так, поставьте вручную в KINETe.

Планы:
Разработать нормальный интерфейс.
