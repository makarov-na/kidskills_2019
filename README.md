# Реализация задания kidskills 2019

## Задание

Робот, двигаясь по линии, должен преодолеть дистанцию за наименьшее время, переместить 2 цилиндра (диаметр 66 мм, высота 123 мм) стоящий на пути в позиции 3 и 1. Направление движения по контрольным зонам выбирает команда. При равных результатах в зачет идут команды с наилучшим временем, так же необходимо произвести видео- презентацию робота.

Необходимо снять видео одной попытки в непрерывной съемке со штатива, а также видео-презентацию одним роликом вместе с заездом, выложить видео через предлагаемый сервис при регистрации. Для соблюдений пропорций поля во время съемки необходимо в зоне старта, по одному из краев поля положить линейка 30см.

1. Продолжительность одной попытки составляет не более 2-х минут (120 секунд).
1. Робот стартует из зоны старта-финиша. До старта никакая часть робота не может выступать из зоны старта-финиша.
1. Стартовав из зоны старта-финиша, робот проходит по порядку контрольные зоны 1-2 и 3-4, следуя по черной линии, и финиширует, вступив в зону старта-финиша, так же возможно прохождения контрольных зон в обратном порядке 3-4 и 1-2. Необходимо привести в зону старта-финиша цилиндр из позиции 3 и из позиции 1. Доставлять можно только по 1 цилиндру. Порядок доставки на усмотрение команды.
1. Если во время попытки робот съезжает с черной линии, т.е. оказывается всеми колесами с одной стороны линии, то попытка не зачитывается.
1. Робот считается вступившим в зону старта-финиша, когда он полностью вступил в эту зону, всеми проекциями робота.
1. Цилиндр считается доставленным, если он присутствует в зоне старт-финиш и ни одна проекция не выходит за пределы этой зоны.
1. После заезда необходимо рассказать о достоинствах своего робота в видео-презентации. Например, сколько используется датчиков, о сверх маневренности и т.д. Продолжительность не более 2-х минут (120 секунд). В видео-презентации должны рассказывать о роботе оба участника команды. Качество видео-презентации, а также опрятность рабочего места так же оценивается.

## Верхнеуровневый алгоритм

* Старт из зоны старта-финиша вверх к зоне 3-4
* Следоваение по лини до поворта налево. Контроль линии правый датчик, контроль поворота 90 градусов левый датчик
* Захват объекта
* Разворот на 180 градусов
* Следование по линни до поворота 90 градусов (зона старта финиша)
* Разгрузка
* Старт из зоны старта-финиша налево по линии
* Следование по линии до первого 90 поворота направо (зона 1-2). Контроль линии левый датчик, контроль поворота 90 градусов правый датчик
* Поворот на 90 градусов налево
* Захват объекта
* Разворот на 180 градусов
* Следование по линни до поворота 90 градусов направо
* Поворот 90 градусов направо
* Следование по линии до поворота 90 направо (зона старта-финиша)
* Разгрузка

## Базовые элементы алгоритма

* Следование по прямой линии
* Следование по плавно изгибающейся линии
* Определение поворота на 90 градусов влево
* Определение поворота на 90 градусов вправо
* Поворот на 90 градусов влево
* Поворот на 90 градусов вправо
* Разворот на 180 градусов

### Определение поворота 90 градусов

Если оба датчика находятся на черном, то робот находится на повороте 90 градусов
Для определения наличия поворта нужен дополнительный датчик. С двумя датчиками можно определять только левые или только праве повороты.