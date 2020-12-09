# Neural Poetry Translation
*[Currently under development]*
## Motivation
Translation technologies have been developing rapidly in recent years. Many modern systems have achieved remarkable quality. These technologies allow people from different countries to understand each other and to get into the cultural, social and moral aspects of other nations.<br>
One of the most important elements of culture is poetry. Unfortunately, by now there is no service that provides poetic translation without human involvement. Our goal is to try to create a neural network capable of translating poetry from one language into another.
## Data
We have collected a corpus of texts consisting of pairs of verses in Russian and English.
### Examples
English | Russian | Original | Source
:-: | :-: | :-: | :-:
eyes of gray - the sodden quay ,<br>driving rain and falling tears ,<br>as the steamer heads to sea<br>in a parting storm of cheers .<br>eyes of black - the throbbing keel<br>milky foam to left and right ;<br>little whispers near the wheel<br>in the brilliant tropic night . | серые глаза - рассвет ,<br>пароходная сирена ,<br>дождь , разлука , серый след<br>за винтом бегущей пены .<br>чёрные глаза - жара ,<br>в море сонных звёзд скольженье ,<br>и у борта до утра<br>поцелуев отраженье . | en <br> Joseph Rudyard Kipling | [link](http://www.eng-poetry.ru/Poem.php?PoemId=9614)
sometimes you wake up in turmoil ,<br>prepared to fight and to rout ,<br>and eager to live and to toil<br>by breakfast the urge blows out . | бывает - проснешься , как птица ,<br>крылатой пружиной на взводе ,<br>и хочется жить и трудиться ;<br>но к завтраку это проходит . | ru <br> Igor Guberman | [link](https://eelov.livejournal.com/727.html)
the murmurs ebb ; onto the stage i enter .<br>i am trying , standing in the door ,<br>to discover in the distant echoes<br>what the coming years may hold in store .<br>the nocturnal darkness with a thousand<br>binoculars is focused onto me .<br>take away this cup , o abba father ,<br>everything is possible to thee . | гул затих . я вышел на подмостки .<br>прислонясь к дверному косяку ,<br>я ловлю в далёком отголоске ,<br>что случится на моем веку .<br>на меня наставлен сумрак ночи<br>тысячью биноклей на оси .<br>если только можно , aвва oтче ,<br>чашу эту мимо пронеси . | ru <br> Boris Pasternak | [link](https://ruverses.com/boris-pasternak/hamlet/4701/)
rain on the windows , creaking doors ,<br>with blasts that besom the green<br>and i am here , and you are there ,<br>and a hundred miles between ! | ночь , монотонный гул дождя ,<br>шум листьев за стеной ;<br>и сотни миль , о сотни миль<br>между тобой и мной . | en <br> Thomas Hardy | [link](https://akyla.net/stihi-na-angliyskom/thomas-hardy/404-thomas-hardy/11933-the-division-razluka)
### Scrapers
For collecting data, we used web scrapers on sites with parallel translations. An example of such a program is available in the scrapers folder.
## Approaches
1. The first approach was to create a transformer from scratch and teach it by feeding it the following data: tokenised text, accents, verse meter data, rhyme formation data, X-SAMPA data.
However, this approach has not produced any positive results (perhaps because of too many parameters).
2. The second approach is to train the ruGPT3 neural network issued by Sberbank. As can be seen from the examples below, the model does a good job of translating, but the rhyme and rhythm are only present in some verses.

In both approaches, we combine data from two corpora: ordinary English-Russian translations and poetic translations. This is necessary so that the model can learn jointly translation and generating texts in poetic form. The first token of each source text indicates whether the text is a poem or a plain text.

#### Data Format Example:

*\<s> ***Verse***: i work without turning a hair # by day or at night , as i please . # i keep making money from air # and throwing it to the winds .<br>
***Translation***: не зная покоя и роздыха , # при лунном и солнечном свете # я делаю деньги из воздуха , # чтоб тут же пустить их на ветер .\</s> <br>
\<s> ***Message***: but its initial efforts have already been noticed in an important way .<br>
***Translation***: но первые шаги в этом направлении уже принесли свои немаловажные плоды .\</s>*

#### Translation examples

Verse | Predicted | Gold
:-: | :-: | :-:
another one was called elaine ,<br>then catherine , martha and naomi<br>in wintertime it ' s slow and gloomy -<br>i ' d fall in love and go insane . | другой - елена, мария,<br>а месяц - марфа,<br>и я от любви не умру,<br>и потому не надо мне<br>ничего, что меня уж нет. | еленою звалась зима ,<br>и марфою , и катериной .<br>и я порою зимней , длинной<br>влюблялся и сходил с ума .
i was angry with my friend ;<br>i told my wrath , my wrath did end .<br>i was angry with my foe :<br>i told it not , my wrath did grow .<br>and i waterd it in fears ,<br>nightamp ; morning with my tears :<br>and i sunned it with smiles ,<br>and with soft deceitful wiles .|друг обидел, разозлил -<br>в гневе молвил : гнев мой закон!<br>в гневе я месть отмела,<br>смеясь над своим врагом.<br>в страхе ночей я слезы лью<br>и с улыбкой лью слезы дождем.|друг обидел , разозлил -<br>я в словах свой гнев излил .<br>враг нанес обиду мне -<br>гнев зарыл я в глубине .<br>сон утратил и покой ,<br>окроплял <br>его слезой ,<br>над ростками колдовал ,<br>ковы тайные ковал .
