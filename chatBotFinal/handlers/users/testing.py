#Наши команды и сам тест
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu, direction_menu, direction_menu2, answerButtons, answerButtonsTesting, answerButtonsAfterTest, answerButtonsTestingForStasQuestHard,answerButtonsTestingForStasQuest, answerButtonsTestingForStasQuest2, answerButtonsSoHardQuest, answerButtonsPromDes
from .info import *
from loader import dp
from states.test import Media,Itkvant,Hitech,Airo,Robo,Bio,Math,Des

answerUser =["Да","да","yes","Yes", "Да ", "да "]
answerUserNo =["Нет", "нет","не","НЕТ","Нет ","нет ","no ","NO","No"]
    
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, я твоя помощница. Нужна помощь с определением направления?\nНапишите команду /help", reply_markup=menu)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_007.webp", "rb")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я - Чат бот для помощи в определении направления в кванториуме. Пройдите тест, отвечая Да или Нет, и я помогу вам определиться!\nДля начала или повторного прохождения напишите /test", reply_markup=ReplyKeyboardRemove())
    await message.answer("Мои команды /kvant, /directions, /test", reply_markup=menu)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_025.webp", "rb")

@dp.message_handler(commands=['kvant'])
async def process_kvant_command(message: types.Message):
    await message.answer(
    	text = '''
    	«Кванториум-15» — часть федеральной сети детских технопарков. Мы занимаемся дополнительным образованием в области инженерно-технических и естественных наук.

У нас школьники 5-11 классов учатся
• разрабатывать собственные проекты,
• пользоваться современным оборудованием,
• применять свои разработки на практике.

В «Кванториуме» работают молодые преподаватели, которые прошли обучение в Сколково и продолжают постоянно повышать свою квалификацию. Мы говорим с детьми на одном языке и просто объясняем сложное.
''', 
    	)


@dp.message_handler(commands=['directions'])
async def process_directions_commnad(message: types.Message):
	await message.reply(
			text = '''
			Выберите одно из направлений и я вам дам информацию о нем!
			''' , reply_markup=direction_menu2
		)

@dp.message_handler(Text(equals=["•IT-Квантум","•Хайтек","•Аэроквантум","•Промышленный дизайн","•ПромРобоКвант","•Биоквантум","•Инженерная математика","•Медиа","•Назад"]))
async def get_infoD(message: Message):
    direct = {
     info_itkvant : "•IT-Квантум",
     info_hitech : "•Хайтек",
     info_airkvant : "•Аэроквантум",
     info_promdesign : "•Промышленный дизайн",
     info_promrobokvant : "•ПромРобоКвант",
     info_biokvant : "•Биоквантум",
     info_inmath : "•Инженерная математика",
     info_media : "•Медиа",
     info_back : "•Назад",
    }
    for key , val in direct.items():
        if message.text == val:
            await message.answer(key)

@dp.message_handler(Text(equals=["Сайт Кванториума!"]))
async def get_web(message: Message):
    await message.answer("Всю дополнительную информацию о направления можно посмотреть на сайте https://kvantorium15.ru/")

@dp.message_handler(Command("test"))
async def choice_test(message: types.Message):
    #it-kvant
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_006.webp", "rb", reply_markup=direction_menu)
    await message.answer("Выберите направления по которому хотите пройти тест!")


@dp.message_handler(state =None)
async def enter_test(message: types.Message):
    if message.text == "Медиа":
        await message.answer("Отвечайте на вопросы Да или Нет")
        await message.answer("Вопрос №1.\n───────────────\n"
        "Интересно, как делают интервью на каналах ВДудь и Ещёнепознер?", reply_markup=answerButtons)
        await Media.Q1.set()
    if message.text == "IT-Квант":
        await message.answer("Хочешь попробовать себя разработке игр, приложений и сайтов?",reply_markup=answerButtons)
        await Itkvant.I1.set()
    if message.text == "Хайтек":
        await message.answer("Хотели бы научится работать с 3D принтером, станком лазерной резки?", reply_markup=answerButtons)
        await Hitech.H1.set()
    if message.text == "Аэроквантум":
        await message.answer("3")
        await Airo.A1.set()
    if message.text == "Промышленный дизайн":
        await message.answer("Тебе нравится рисовать ?", reply_markup=answerButtons)
        await Des.D1.set()
    if message.text == "ПромРобоКвант":
        await message.answer("5")
        await Robo.R1.set()
    if message.text == "Биоквантум":
        await message.answer("6")
        await Bio.B1.set()
    if message.text == "Инженерная математика":
        await message.answer("Хотелось бы вам перестать думать шаблонами и научится здравому анализу?", reply_markup=answerButtonsTestingForStasQuest)
        await Math.M1.set()

@dp.message_handler(state=Media.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Хочешь узнать, как создают крутые медиапроекты и успешные блоги?")
    await Media.next()


@dp.message_handler(state=Media.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Знаешь как отличить фейковую новость от настоящей?")
    await Media.next()

@dp.message_handler(state=Media.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Хочешь узнать, чем сценарий \"Фиксиков\" отличается от сценария \"Вечернего Урганта\"?")
    await Media.next()

@dp.message_handler(state=Media.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("Вопрос №5.\n───────────────\n"
                         "Тебе предложили снять видеообзор на любимую игру. Для тебя это\n\n\n1.Круто! Это может стать началом моего блога об играх.\n\n2.Будет сложновато придумать, о чём рассказывать, но интересно попробовать.\n\n3.Неинтересно. Лучше потрачу это время на то, чтобы научиться делать игры самому!", reply_markup=answerButtonsTesting)
    await Media.next()

@dp.message_handler(state=Media.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer5=2)
    if message.text == "2 вариант":
        await state.update_data(answer5=1)
    if message.text == "3 вариант":
        await state.update_data(answer5=0)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    #inmath
    await message.answer("Вопрос №6.\n─────────────\n"
                         "У вас во дворе собака родила щенят. Нужно найти для них хозяев. Что ты для этого сделаешь?\n\n\n1.Заберут щенков или нет - неизвестно. Лучше пока сделаю для них хорошую будку со встроенным дозатором корма\n\n2.Напишу волонтёрам, которые работают с бездомными животными. Они-то наверняка знают, что делать с щенками!\n\n3.Сделаю такие фотографии этих пёселей, чтобы всем сразу хотелось их взять домой. Выложу фото в соцсетях и попрошу всех, кто может, сделать репосты.")
    await Media.next()

@dp.message_handler(state=Media.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=0)
    if message.text == "2 вариант":
        await state.update_data(answer6=1)
    if message.text == "3 вариант":
        await state.update_data(answer6=2)
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Друзья решили запустить паблик в Вконтакте и пригласили тебя присоединиться. Чем будешь помогать?\n\n\n1.Может быть буду репостить у себя их мемы и комментить интересные посты. Создам активность подписчиков.\n\n2.Кто-то сказал мемы? Я в этом шарю! Буду делать публикации, которые станут собирать тысячи лайков.\n\n3.Сделаю такие фотографии этих пёселей, чтобы всем сразу хотелось их взять домой. Выложу фото в соцсетях и попрошу всех, кто может, сделать репосты.")
    await Media.next()

@dp.message_handler(state=Media.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer7=1)
    if message.text == "2 вариант":
        await state.update_data(answer7=2)
    if message.text == "3 вариант":
        await state.update_data(answer7=0)
    await message.answer("Вопрос №8.\n─────────────────\n"
                         "Классный руководитель предложил написать статью для школьного сайта. Нужно разобраться, как отличать фейковые новости от реальных. Возьмёшься?\n\n\n1.Конечно! Обожаю разоблачать обманщиков и проверять факты! Ещё и рейтинг СМИ составлю по частоте публикации фейков!\n\n2.А как их отличать-то? По-моему, никто наверняка не знает. Ладно, если пятёрку по русскому поставят, то попробую.\n\n3.Вы сайт этот видели? Он даже со смартфона не открывается нормально. Лучше предложу классной сделать новый современный сайт.")
    await Media.next()

@dp.message_handler(state=Media.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer8=2)
    if message.text == "2 вариант":
        await state.update_data(answer8=1)
    if message.text == "3 вариант":
        await state.update_data(answer8=0)
    await message.answer("Вопрос №9.\n─────────────────\n"
                         "Тебе предложили подработку на лето. Можно пойти на ТВ в отдел новостей, в лабораторию института биологии или в мастерскую 3D-печати и лазерной резки. Платить везде будут одинаково. Что выберешь?\n\n\n1.Конечно на ТВ! Посмотрю как делают настоящие новости и сам попробую себя в роли корреспондента\n\n2.Пробирки, реактивы, микроскопы, биоматериалы - кажется я делаю первый шаг к Нобелевке в области физиологии и медицины!\n\n3D-принтеры - это же самые современные технологии. Уже дома и органы для пересадки на них печатают. Однозначно туда!")
    await Media.next()

@dp.message_handler(state=Media.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer9=2)
    if message.text == "2 вариант":
        await state.update_data(answer9=0)
    if message.text == "3 вариант":
        await state.update_data(answer9=0)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?",reply_markup=answerButtonsAfterTest)
    await Media.next()

@dp.message_handler(state=Media.Q0)
async def answer_q0(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    answerM6 = data.get("answer6")
    answerM7 = data.get("answer7")
    answerM8 = data.get("answer8")
    answerM9 = data.get("answer9")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5,answerM6,answerM7,answerM8,answerM9]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
        if item == 3:
            k += 3
    await message.answer("Вам подходит направление Медиа на - {0}% ".format(100*k//12), reply_markup=ReplyKeyboardRemove())
    await message.answer("Удачи вам!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_031.webp","rb")
    await state.finish()

@dp.message_handler(state=Math.M1)
async def answer_a1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=5)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Нравится ли вам решать не стандартные задачи?")
    await Math.next()


@dp.message_handler(state=Math.M2)
async def answer_m2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=5)
    if message.text == "50/50":
        await state.update_data(answer2 =5)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Нравятся ли долгие вычисления и находить решение примеров?")
    await Math.next()

@dp.message_handler(state=Math.M3)
async def answer_m3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUserNo:
        await state.update_data(answer3 =5)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Интересны ли вам доказтельства теорем?", reply_markup=answerButtonsTestingForStasQuest2)
    await Math.next()

@dp.message_handler(state=Math.M4)
async def answer_m4(message: types.Message, state: FSMContext):
    if message.text == "Просто стараюсь из понять.":
        await state.update_data(answer4=10)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("Вопрос №5.\n───────────────\n"
                         "Знаешь ли ты?\n\n1.Я на седьмом этаже. Это как шестой, но на один повыше. Иногда залезаю на крышу.\n\n2.В прямоугольном треугольнике квадрат длины гипотенузы, равен сумме квадратов длин катетов.\n\n3.Вдоль ночных дорог шла, босиком не жалея ног. Сердце его теперь в твоих руках. Не потеряй его и не сломай.\n\n4.В прямоугольном треугольнике квадрат катета, равен сумме квадратов длин гипотенуз.", reply_markup=answerButtonsTestingForStasQuestHard)
    await Math.next()

@dp.message_handler(state=Math.M5)
async def answer_m5(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer5=5)
    if message.text == "3 вариант":
        await state.update_data(answer5=10)
    else:
        await message.answer("Отвечайте правильно, пожалуйста. Надо выбрать вариант ответа!")
    #inmath
    await message.answer("Вопрос №6.\n─────────────\n"
                         "Конкатенация - это болезнь?\n\n1.Да. Это болезнь поджелудочной железы.\n\n2.Да. Это особое восполение слизестой.\n\n3.Нет. Это склеивания объектов\n\n4.Нет. Это термин дифферициального исчесления")
    await Math.next()

@dp.message_handler(state=Math.M6)
async def answer_m6(message: types.Message, state: FSMContext):
    if message.text == "3 вариант":
        await state.update_data(answer6=5)
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Теорема Пифагора это частный случай теоремы косинусов?\n\n1.Теорма Пифагора это частный случай теоремы о синусах.\n\n2.Да.\n\n3.Что такое косинус?\n\n4.Наоброт. Теорема косинусов это частный случай теоремы Пифагора.")
    await Math.next()

@dp.message_handler(state=Math.M7)
async def answer_m7(message: types.Message, state: FSMContext):
    if message.text == "2 вариант":
        await state.update_data(answer7=5)
    await message.answer("Вопрос №8.\n─────────────────\n"
                         "Трисс или Йеннифэр?\n\n1.Трисс\n\n2.Йеннифэр\n\n3.Не выбираю вовсе\n\n4.Обе")
    await Math.next()

@dp.message_handler(state=Math.M8)
async def answer_m8(message: types.Message, state: FSMContext):
    if message.text == "3 вариант":
        await state.update_data(answer8=10)
    if message.text == "2 вариант":
        await state.update_data(answer8 = 5)
    await message.answer("Вопрос №8.\n───────────────\n"
                         "Сколько будет 0,(3) + 0,(3) + 0,(3)?\n\n1.Один\n\n2.0,(9).\n\n3.0,9999999998.\n\n4.Я что калькуляор?.", reply_markup=answerButtonsTestingForStasQuestHard)
    await Math.next()

@dp.message_handler(state=Math.M9)
async def answer_m9(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer9=10)
    if message.text == "2 вариант":
        await state.update_data(answer9=5)
    await message.answer("Вопрос №9.\n───────────────\n"
                         "За столом сидели мужики и...?\n\n1.Ели.\n\n2.Решали задачи.\n\n3.Учили теоремы.\n\n4.Занимались робототехникой.", reply_markup=answerButtonsTestingForStasQuestHard)
    await Math.next()

@dp.message_handler(state=Math.M10)
async def answer_m10(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer10=10)
    if message.text == "2 вариант":
        await state.update_data(answer10=5)
    await message.answer("Вопрос №10.\n───────────────\n"
                         "Смотрите ли вы канал \"Хауди Хо\"?", reply_markup=answerButtonsSoHardQuest)
    await Math.next()

@dp.message_handler(state=Math.M11)
async def answer_m11(message: types.Message, state: FSMContext):
    if message.text == "Не знаю кто это":
        await state.update_data(answer11=5)
    if message.text == "Нет":
        await state.update_data(answer11=5)
    if message.text == "Да":
        await state.update_data(answer11= -20)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?", reply_markup=answerButtonsAfterTest)
    await Math.next()

@dp.message_handler(state=Math.M12)
async def answer_m12(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    answerM6 = data.get("answer6")
    answerM7 = data.get("answer7")
    answerM8 = data.get("answer8")
    answerM9 = data.get("answer9")
    answerM10 = data.get("answer10")
    answerM11 = data.get("answer11")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5,answerM6,answerM7,answerM8, answerM9, answerM10,answerM11]
    for item in ans:
        if item == 5:
            k += 5
        if item == 10:
            k += 10
        if item == 0:
            k += 0
        if item == -20:
            k -= 20
    await message.answer("Вам подходит направление Инженерная математика на - {0}% ".format(100*k//80), reply_markup=ReplyKeyboardRemove())
    await message.answer("Это было тяжело, но ты справился!!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_046.webp","rb")
    await state.finish()

@dp.message_handler(state=Des.D1)
async def answer_d1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "Ты хотел(а) бы создать какое нибудь новое изобретение для пользы людей, животных , растений?")
    await Des.next()


@dp.message_handler(state=Des.D2)
async def answer_d2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "Промышленный дизайн занимается разработкой изделий декоративно прикладного характера")
    await Des.next()

@dp.message_handler(state=Des.D3)
async def answer_d3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text == "Нет":
        await state.update_data(answer3=1)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "Промышленный дизайн занимается разработкой предметов, устройств акцентируя внимание не только на эстетике , но и на функционале")
    await Des.next()

@dp.message_handler(state=Des.D4)
async def answer_d4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("Вопрос №5.\n───────────────\n"
                         "Тебе подарили гаджет нового поколения. Что ты сделаешь в первую очередь", reply_markup=answerButtonsPromDes)
    await Des.next()


@dp.message_handler(state=Des.D5)
async def answer_d5(message: types.Message, state: FSMContext):
    if message.text == "2.В первую очередь обращу внимание на дизайн гаджета , экраны и интерфейс, цветовую гамму меню, удобство, эргономику":
        await state.update_data(answer5=2)
    if message.text == "1.Буду смотреть техническую начинку( емкость батареи, оперативку, функции и до.)":
        await state.update_data(answer5=1)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?", reply_markup=answerButtonsAfterTest)
    await Des.next()

@dp.message_handler(state=Des.D6)
async def answer_d6(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
    await message.answer("Вам подходит направление Промышленный дизайн на - {0}% ".format(100*k//6),reply_markup=ReplyKeyboardRemove())
    await message.answer("А вы быстро!!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_034.webp","rb")
    await state.finish()

@dp.message_handler(state=Itkvant.I1)
async def answer_i1(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer1=1)
    await message.answer("Вопрос №2. \n───────────────\n"
                         "")
    await Itkvant.next()


@dp.message_handler(state=Itkvant.I2)
async def answer_i2(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer2=1)
    await message.answer("Вопрос №3.\n────────────────\n"
                         "")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I3)
async def answer_i3(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer3=1)
    await message.answer("Вопрос №4.\n─────────────────\n"
                         "")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I4)
async def answer_i4(message: types.Message, state: FSMContext):
    global answerUser
    if message.text in answerUser:
        await state.update_data(answer4=1)
    await message.answer("Теперь я задам вопросы посерьезнее. Выбери один вариант ответа!")
    await message.answer("Вопрос №5.\n───────────────\n"
                         "Что такое датчики и для чего они используются?\n\n\n1.детекторы, которые имеют возможность измерять некоторые физические качества, такие как давление или свет.\n\n2.Моторы, которые имеют возможность приводить некоторые детали в движения, такие как колеса или свет.\n\n3.И то и то\n\n4.Я не знаю", reply_markup=answerButtonsTesting)
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I5)
async def answer_i5(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer5=2)
    await message.answer("Вопрос №6.\n─────────────\n"
                         "Что такое переменная, тип переменной и область видимости переменной?\n\n\n1.Да\n\n2.Ну почти\n\n3.Что то слышал\n\n4.Нет")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I6)
async def answer_i6(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer6=2)
    if message.text == "2 вариант":
        await state.update_data(answer6=1)
    await message.answer("Вопрос №7.\n─────────────────\n"
                         "Какие личностые требования должны быть к ученику?\n\n1.Навыки командной работы\n\n2.постоять за себя\n\n3.Генерировать различные идеи\n\n4.Чувство юмора")
    await Itkvant.next()


@dp.message_handler(state=Itkvant.I7)
async def answer_i7(message: types.Message, state: FSMContext):
    if message.text == "1 вариант":
        await state.update_data(answer7=2)
    if message.text == "3 вариант":
        await state.update_data(answer7=2)
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_ENG/LINE_Menhera_chan_ENG_005.webp", "rb")
    await message.answer("Готовы получить ответ?")
    await Itkvant.next()

@dp.message_handler(state=Itkvant.I9)
async def answer_i9(message: types.Message, state: FSMContext):
    k = 0  
    data = await state.get_data()
    answerM1 = data.get("answer1")
    answerM2 = data.get("answer2")
    answerM3 = data.get("answer3")
    answerM4= data.get("answer4")
    answerM5 = data.get("answer5")
    answerM6 = data.get("answer6")
    answerM7 = data.get("answer7")
    ans=[answerM1, answerM2, answerM3, answerM4,answerM5,answerM6,answerM7]
    for item in ans:
        if item == 1:
            k += 1
        if item == 2:
            k += 2
    await message.answer("Вам подходит направление IT-Квантум на - {0}% ".format(100*k//10))
    await message.answer("Многообещающе!")
    await message.answer_sticker("https://chpic.su/_data/stickers/l/LINE_Menhera_chan_3_ENG/LINE_Menhera_chan_3_ENG_016.webp","rb")
    await state.finish()

    

