# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
LIMIT = 10
text = (
    'норвежская фигуристка, выступавшая в одиночном разряде и в парном катании, а позже американская киноактриса и звезда профессиональных ледовых шоу. '
    'Первая и единственная трёхкратная олимпийская чемпионка (1928, 1932, 1936) в женском одиночном катании. Десятикратная победительница чемпионатов мира (1927—1936) и '
    'шестикратная чемпионка Европы (1931—1936), пятикратная чемпионка Норвегии в женском одиночном разряде и трёхкратная — в парном катании. '
    'Произвела революцию в женском фигурном катании, превратив его произвольную программу из набора разрозненных фигур в балетное представление на льду и внеся в него '
    'атлетические элементы, до этого исполнявшиеся только фигуристами-мужчинами. Оставив в 1936 году в возрасте 24 лет любительский спорт, продолжила карьеру как '
    'основная звезда профессиональных ледовых шоу в США, в течение короткого периода в начале 1950-х годов выступая также в качестве менеджера и продюсера собственного '
    'ледового ревю. В 1936—1948 годах снялась в главных ролях более чем в десятке голливудских фильмов, в основном снятых студией 20th Century-Fox Film, '
    'самым известным из которых стала «Серенада солнечной долины». Как кинолентам с участием Хени, так и её ледовым ревю сопутствовал значительный финансовый успех. '
    'Выйдя замуж в третий раз в 1957 году за норвежского бизнесмена Нильса Унстада, завершила выступления и занялась коллекционированием произведений современного '
    'искусства, собрание которых впоследствии легло в основу экспозиции Центра искусств Хени-Унстад в Осло. Удостоена звезды на Аллее славы в Голливуде, посмертно '
    'включена в списки Зала славы мирового фигурного катания (1976) и Международного зала славы женского спорта (1982).')

sort_text = ''
for item in text:
    if item.isalpha() or item == ' ':
        sort_text += item
lst_word = sort_text.lower().split()

dict_wrd = {}
for item in set(lst_word):
    cnt = lst_word.count(item)
    dict_wrd[item] = cnt

res = []
for i in sorted(dict_wrd.items(), key=lambda para: (-para[1], para[0])):
    res.append(i)
if len(res) > LIMIT:
    res = res[:LIMIT:]
for n, elem in enumerate(res, 1):
    print(f'{n} - {elem}')
