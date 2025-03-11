# give a list of str:
EN_EXAMPLES=["The weather is quite pleasant today, with clear skies and a mild breeze", 
"Please ensure that all documents are submitted before the deadline.",
"We appreciate your prompt response and look forward to collaborating further.", 
"The system requires a software update to function properly.", 
"Did you watch the new movie that was released last weekend?"]
EN_EXAMPLES_2=[
    'Other UK car manufacturers have raised fears about leaving the EU without agreement on how cross-border trade will function, including Honda, BMW and Jaguar Land Rover.',
    'Meanwhile, the prime minister is falling dangerously under the spell of the charismatic tech billionaire who claims he can solve Britain\'s computer woes: the sinister Jason Volta, played by Jake Lacy.',
    'However, turnout stood at only 16 percent, compared to 34 percent in last parliamentary election in 2016 when 66 percent of the registered voters cast their ballot.'
]
HI_EXAMPLES_2=[
    'अन्य यू.के. कार निर्माताओं ने होंडा, BMW और जगुआर लैंड रोवर सहित सीमा पार से व्यापार कैसे करेगा, इस पर सहमति के बिना EU छोड़ने के बारे में आशंका जताई है।',
    'इस बीच, प्रधानमंत्री उस केरिसमेटिक तकनीकी अरबपति की बात में आकर खतरे में पड़ जाते हैं जो यह दावा करता है कि उसके पास ब्रिटेन के कंप्यूटर संकटों का समाधान है: पापी जेसन वोल्टा ने जेक लेसी की भूमिका निभाई।',
    'हालांकि, 2016 में जब पिछ्ला संसदीय चुनाव हुआ था, तो उसमें 34 प्रतिशत की तुलना में वोटिंग सिर्फ़ 16 प्रतिशत रही, इसमें 66 प्रतिशत पंजीकृत मतदाताओं ने अपना वोट दिया था।'
]

EN_DE_EXAMPLES=[
  {
    "source": "White nationalists, gun fetishists, pro-dictator right wing.. there's the danger. Deport the white supremacists.",
    "target": "Weiße Nationalisten, Waffenfetischisten, Diktator-Freundliche vom rechten Flügel … da liegt die Gefahr. Deportiert die weißen Rassisten."
  },
  {
    "source": "It's 2023 and I still see people with iPhones actively avoid using Apple Maps.",
    "target": "Es ist 2023 und ich sehe immer noch Menschen mit iPhones, die aktiv die Verwendung von Apple Maps vermeiden."
  },
  {
    "source": "#CNN needs to just close down. Yesterday's fiasco with #MangoMoron was an outrageous fiasco. Who at that pathetic, dying network was responsible for vetting the so-called \"independent voters\" in the audience? Which cable news \"executive\" made the call to give the fat, lying criminal this much air-time?",
    "target": "#CNN muss einfach den Laden dichtmachen. Das Fiasko von gestern mit #MangoMoron war einfach ungeheuerlich. Wer war bei diesem jämmerlichen, im Sterben liegenden Sender eigentlich für die Überprüfung der sogenannten „unabhängigen Wähler“ im Publikum verantwortlich? Welcher Kabelnachrichten-„Verantwortliche“ hat denn die Entscheidung getroffen, dem fetten, lügenden Kriminellen so viel Sendezeit zu geben?"
  }
]

EN_CS_EXAMPLES=[
  {
    "source": "The only way to restore service was to do a AC power reset.",
    "target": "Jediný způsob, jak obnovit službu, bylo provést reset napájení."
  },
  {
    "source": "Then we have to come at a quarter past eight already, so that we have the 30 minutes extra to make sure that everything is running and chase people.",
    "target": "Pak musíme přijít už ve čtvrt na devět, abychom měli 30 minut navíc na to ujistit se, že všechno běží, a abychom nahnali lidi."
  },
  {
    "source": "He added that the decision to withdraw the appeal was more \"to prevent the politics of Hindutva [Hindu nationalism] from being ridiculed in the face of severe criticism from all quarters.\"",
    "target": "Dodal, že rozhodnutí stáhnout výzvu bylo spíše proto, „aby se politika hindutvy (hinduistického nacionalismu) nezesměšnila tváří v tvář tvrdé kritice ze všech stran“."
  }
]

CS_UK_EXAMPLES=[{
    "source": "V důvěrném úvodním prohlášení pro účastníky zasedání se přiznává, že nyní \"přinejmenším mezi některými panuje názor, že Spojené království zatím nenašlo cestu vpřed mimo EU\", přičemž brexit \"působí jako brzda našeho růstu a brzdí potenciál Spojeného království\".",
    "target": "У секретній вступній заяві для учасників засідання вона визнає, що зараз \"принаймні між деякими панує думка, що Сполучене Королівство поки що не знайшло шлях вперед поза ЄС\", причому брекзит діє як гальмо нашого зростання і гальмує потенціал Сполученого Королівства\"."
  },
  {
    "source": "Vůbec na tebe nechci tlačit.",
    "target": "Я зовсім не хочу тиснути на тебе."
  },
  {
    "source": "Svého jednání litoval a uvedl, že důvodem páchání trestné činnosti bylo zabezpečení nejen své osoby, ale i jeho rodiny.",
    "target": "Своїх дій шкодував і повідомив, що причиною скоєння злочинів було забезпечення не тільки його особи, але і його сім'ї."
  }
]

JA_ZH_EXAMPLES=[
  {
    "source": "今年のＧＰ決選投票が１１月に同県桑名市で行われるため、地元でのランクアップを狙い、ひやわんの情報発信などを行う「隠（なばり）ひやわん倶楽部」がテーマ曲の制作を企画した。",
    "target": "今年的GP决选投票将于11月在该县桑名市举行，以提高当地的排名为目标，计划为发布hiyawan（三重县名张市的象征性动物形象：出没在狭窄小巷的狗）信息的“隐hiyawan俱乐部”制作主题曲。"
  },
  {
    "source": "「いきもの目線」にホンドタヌキ一家 ２２日公開(2017/9/21) ３６０度動画「いきもの目線」ページに、あす２２日、新しいコンテンツが登場します。",
    "target": "在“生物视线”中貉一家22日公开（2017/9/21）的360度视频“生物视线”页面，明天22日，将有新的内容出现。"
  },
  {
    "source": "弘前大付属中は２４日に記者会見し、２３日に実施した来年度入試の国語の試験で、誤って中学校で習う漢字「眠」を書かせる出題ミスがあったとして陳謝した。",
    "target": "弘前大学附属中学24日召开记者招待会，针对在23日进行的明年入学的国语考试中，错误地让中学才能学习的汉字“眠”出现在题目中而道歉。"
  }
]

EN_ZH_EXAMPLES=[
  {
    "source": "And only the pronunciations that were observed three times or more, or something like that.",
    "target": "只有那些被观察了三次或更多次的发音，或者类似的。"
  },
  {
    "source": "The experiments don't create the facts on this reading, but the choice of which experiments to conduct controls which facts are discovered.",
    "target": "实验并不创造以上所述事实，但选择进行哪些实验控制了哪些事实会被发现。"
  },
  {
    "source": "One arrested amid Tate Britain protest over drag queen children's event",
    "target": "一人在泰特英国抗议变装皇后儿童活动中被捕"
  }
]

ZH_EN_EXAMPLES=[
  {
    "source": "只有那些被观察了三次或更多次的发音，或者类似的。",
    "target": "And only the pronunciations that were observed three times or more, or something like that."
  },
  {
    "source": "实验并不创造以上所述事实，但选择进行哪些实验控制了哪些事实会被发现。",
    "target": "The experiments don't create the facts on this reading, but the choice of which experiments to conduct controls which facts are discovered."
  },
  {
    "source": "一人在泰特英国抗议变装皇后儿童活动中被捕",
    "target": "One arrested amid Tate Britain protest over drag queen children's event"
  }
]

EN_UK_EXAMPLES=[
  {
    "source": "Will a community blossom around the user-generated content piece of the game?",
    "target": "Чи буде привабливим частина гри, де користувачі самі створюють свій контент?"
  },
  {
    "source": "That takes effort.",
    "target": "Це вимагає зусиль."
  },
  {
    "source": "Shortly after, Balenciaga dropped photos for its spring 2023 campaign that featured a page from a 2008 Supreme Court case involving \"virtual child pornography\" in the background.",
    "target": "Невдовзі після цього Balenciaga опублікував фотографії для своєї рекламної кампанії навесні 2023 року, на задньому плані яких була сторінка зі справи у Верховному суді 2008 року про «віртуальну дитячу порнографію»."
  }
]

EN_ES_EXAMPLES=[
  {
    "source": "In June, the Commission published the results of a public consultation on the proposals which found broad support for calling the assembly a Welsh Parliament.",
    "target": "En junio, la Comisión publicó los resultados de una consulta pública sobre las propuestas, en donde se obtuvo un amplio apoyo para llamar a la asamblea un Parlamento de Gales."
  },
  {
    "source": "Waters' statement quickly drew criticism online, including from former White House press secretary Ari Fleischer.",
    "target": "La declaración de Walters provocó rápidamente críticas en Internet, incluyendo una del anterior secretario de prensa de la Casa Blanca Ari Fleischer."
  },
  {
    "source": "It was a third Elite League defeat of the season for Adam Keefe's men, who had come from behind to beat Dundee 2-1 in Belfast on Friday night.",
    "target": "Fue la tercera derrota de la temporada de la Elite League para el equipo de Adam Keefe, quienes tuvieron que jugar desde una posición en desventaja para vencer a Dundee 2 a 1 en Belfast el viernes en la noche."
  }
]

EN_HI_EXAMPLES=[
  {
    "source": "Other UK car manufacturers have raised fears about leaving the EU without agreement on how cross-border trade will function, including Honda, BMW and Jaguar Land Rover.",
    "target": "अन्य यू.के. कार निर्माताओं ने होंडा, BMW और जगुआर लैंड रोवर सहित सीमा पार से व्यापार कैसे काम करेगा, इस पर सहमति के बिना EU छोड़ने के बारे में आशंका जताई है।"
  },
  {
    "source": "Meanwhile, the prime minister is falling dangerously under the spell of the charismatic tech billionaire who claims he can solve Britain's computer woes: the sinister Jason Volta, played by Jake Lacy.",
    "target": "इस बीच, प्रधानमंत्री उस केरिसमेटिक तकनीकी अरबपति की बात में आकर खतरे में पड़ जाते हैं जो यह दावा करता है कि उसके पास ब्रिटेन के कंप्यूटर संकटों का समाधान है: पापी जेसन वोल्टा ने जेक लेसी की भूमिका निभाई।"
  },
  {
    "source": "However, turnout stood at only 16 percent, compared to 34 percent in last parliamentary election in 2016 when 66 percent of the registered voters cast their ballot.",
    "target": "हालांकि, 2016 में जब पिछ्ला संसदीय चुनाव हुआ था, तो उसमें 34 प्रतिशत की तुलना में वोटिंग सिर्फ़ 16 प्रतिशत रही, इसमें 66 प्रतिशत पंजीकृत मतदाताओं ने अपना वोट दिया था।"
  }
]

EN_IS_EXAMPLES=[
  {
    "source": "PCB Whites' Imam was hit on his left hand while batting against PCB Greens' Naseem Shah on day one of the match.",
    "target": "Imam, sem leikur með PCB Whites, fékk högg á vinstri hönd þegar hann sló högg gegn Naseem Shah í PCB Greens á fyrsta degi viðureignarinnar."
  },
  {
    "source": "Washington - Republican Senator Ted Cruz of Texas accused House Speaker Nancy Pelosi and House Democrats of pushing a coronavirus relief package that focuses on \"shoveling cash at the problem and shutting America down\" as negotiations on the next measure continue.",
    "target": "Washington – Ted Cruz, öldungadeildarþingmaður repúblikana frá Texas, sakaði Nancy Pelosi, forseta þingdeildar og þingflokks demókrata, um að mæla fyrir lögum sem ætlað er að létta á áhrifum kórónuveirunnar með því að „skófla peningum í vandamálið og loka Bandaríkjunum,“ er samningaviðræður um næsta úrræði halda áfram."
  },
  {
    "source": "The rock star wrote next to a snap of him and his wife Anita Dobson: \"Birthday dinner for me - created by Anita - we dressed up to stay home !\"",
    "target": "Rokkstjarnan skrifaði skilaboð við mynd af honum og eiginkonu hans, Anitu Dobson: „Afmæliskvöldverður fyrir mig – sem Anita eldaði – við klæddum okkur upp til að vera heima!“"
  }
]

EN_JA_EXAMPLES=[
  {
    "source": "And some of our submission papers would come later for the PBML proceedings.",
    "target": "そして、提出論文の中には後でPBMLの論文集にのるかもしれません。"
  },
  {
    "source": "(PERSON3) The thing is, as long as we do the analysis more properly, one thing is the possible adversarial evaluation, just to indicate that that the constraints are actually having an impact on the actual output.",
    "target": "(PERSON3)要は、僕らがもっときちんと解析してさえおけば、ひとつは敵対的評価ができるかもしれないし、制約が実際の出力に影響を及ぼしていることを単に表示するためにね。"
  },
  {
    "source": "One per customer rules remain as we try to ensure everyone who queues up can get their hands on a board.",
    "target": "お一人様一点限りのルールは、お並び頂いた皆様に確実に行き渡るようにするためのものです。"
  }
]

EN_RU_EXAMPLES=[
  {
    "source": "The hacked up version of Jedi Knight was crashing because it was calling a function off the end of a vtable.",
    "target": "Взломанная версия Jedi Knight вылетала из-за того, что вызывала функцию с конца виртуальной таблицы."
  },
  {
    "source": "Who at that pathetic, dying network was responsible for vetting the so-called \"independent voters\" in the audience?",
    "target": "Кто на этом жалком умирающем телеканале отвечал за проверку так называемых «независимых избирателей» среди зрителей?"
  },
  {
    "source": "The suspect is charged with two counts of felony first-degree murder and two counts of felony attempted murder, Chicago Police superintendent David Brown announced.",
    "target": "Подозреваемый обвиняется по двум пунктам по делу об убийстве первой степени и двум пунктам по делу о покушении на убийство, сообщил Дэвид Браун, начальник полиции Чикаго."
  }
]
RU_EXAMPLES=["Погода сегодня довольно приятная, с ясной погодой и легким ветром.",
"Убедитесь, что все документы представлены до крайнего срока.",
"Мы ценим ваш оперативный ответ и надеемся на дальнейшее сотрудничество.",
"Система требует обновления программного обеспечения для нормальной работы.",
"Видишь ли ты новый фильм, который вышел на прошлой неделе?"]
ZH_EXAMPLES=["今天的天气相当不错，晴朗无云，微风轻拂。",
"请确保所有文件在截止日期前提交。",
"我们感谢您的及时回复，并期待进一步合作。",
"系统需要软件更新才能正常工作。",
"你上周看过新上映的电影吗？"]
DE_EXAMPLES=["Die Wetter ist heute ziemlich angenehm, mit klaren Himmel und einem leichten Wind.",
"Bitte stellen Sie sicher, dass alle Dokumente bis zum Abgabedatum eingereicht werden.",
"Wir schätzen Ihre schnelle Reaktion und freuen uns auf eine weitere Zusammenarbeit.",
"Das System benötigt ein Softwareupdate, um ordnungsgemäß zu funktionieren.",
"Hast du das neue Film, das letzte Wochenende veröffentlicht wurde, gesehen?"]
HI_EXAMPLES=["आज मौसम काफी सुहावना है, आसमान साफ ​​है और हल्की हवा चल रही है",
"कृपया सुनिश्चित करें कि सभी दस्तावेज समय सीमा से पहले जमा कर दिए जाएं।",
"हम आपकी त्वरित प्रतिक्रिया की सराहना करते हैं तथा आगे भी सहयोग करने की आशा करते हैं।",
"सिस्टम को ठीक से काम करने के लिए सॉफ़्टवेयर अपडेट की आवश्यकता है",
"क्या आपने पिछले सप्ताहांत रिलीज़ हुई नई फिल्म देखी?"]
ES_EXAMPLES=["El clima hoy es bastante agradable, con cielos claros y un ligero viento.",
"Asegúrate de que todos los documentos se presenten antes de la fecha límite.",
"Agradecimos su respuesta rápida y esperamos colaborar en futuras ocasiones.",
"El sistema requiere una actualización de software para funcionar correctamente.",
"¿Has visto la nueva película que se estrenó el fin de semana pasado?"]
CS_EXAMPLES=["Dnes je počasí docela příjemné, s jasným nebem a lehkým větrem.",
"Ujistěte se, že všechny dokumenty jsou předloženy do konce lhůty.",
"Vděčíme vám za rychlou reakci a doufáme, že budeme moci spolupracovat dále.",
"Systém vyžaduje aktualizaci softwaru pro sprábnou funkci.",
"Podíval jsi se na nový film, který byl vydán minulý týden?"]
IS_EXAMPLES=["Í dag er veður næstum umhverfisfrítt, með klart himinn og lítið vindur.",
"Greiðið til þess að öll skjöl séu skilaðar inn að lokum tímabilsins.",
"Við þakka þér fyrir snemma svar og höfum von á að við getum samstarfað áfram.",
"Kerfið þarf tölvubreyting til að vinna rétt.",
"Hefur þú fylgt nýja myndinni sem var látinn út síðasta viku?"]
JA_EXAMPLES=["今日はとても良い天気です。晴れていて、少し風が吹いています。",
"すべてのドキュメントが期限までに提出されることを確認してください。",
"早速の返信に感謝します。さらなるコラボレーションを期待しています。",
"システムは正しく機能するためにソフトウェアの更新が必要です。",
"先週公開された新しい映画を見ましたか？"]
UK_EXAMPLES=["Сьогодні погода досить приємна, з ясним небом і легким вітром.",
"Переконайтеся, що всі документи представлені до кінця терміну.",
"Дякуємо вам за швидку реакцію і сподіваємося на подальшу співпрацю.",
"Система потребує оновлення програмного забезпечення для нормальної роботи.",
"Чи подивились ви нову фільм, який вийшов минулого тижня?"]
FR_EXAMPLES=["Le temps est plutôt agréable aujourd'hui, avec un ciel clair et un léger vent.",
"Assurez-vous que tous les documents sont soumis avant la date limite.",
"Nous vous remercions pour votre réponse rapide et espérons pouvoir collaborer à nouveau.",
"Le système nécessite une mise à jour du logiciel pour fonctionner correctement.",
"Avez-vous vu le nouveau film qui a été sorti la semaine dernière?"]
X_EXAMPLES=["今天的天气相当不错，晴朗无云，微风轻拂。",
"Переконайтеся, що всі документи представлені до кінця терміну.",
"早速の返信に感謝します。さらなるコラボレーションを期待しています。",
"Kerfið þarf tölvubreyting til að vinna rétt.",
"¿Has visto la nueva película que se estrenó el fin de semana pasado?"]
IT_EXAMPLES=["Il tempo è piuttosto accogliente oggi, con cielo sereno e leggero vento.",
"Assicurati che tutti i documenti siano presentati entro la scadenza.",
"Grazie per la tua risposta rapida e speriamo di poter collaborare di nuovo.",
"Il sistema richiede un aggiornamento del software per funzionare correttamente.",
"Hai visto il nuovo film che è stato rilasciato l'ultima settimana?"]
AR_EXAMPLES=["الطقس اليوم يشبه الطقس الصحيح، مع سماء مشرقة وريح خفيفة.",
"تأكد من تقديم جميع الوثائق قبل الموعد المحدد.",
"نشكرك على ردك السريع ونأمل أن نتمكن من التعاون معك مرة أخرى.",
"يتطلب النظام تحديث البرمجيات للعمل بشكل صحيح.",
"هل رأيت الفيلم الجديد الذي تم إصداره في الأسبوع الماضي؟"]
PT_EXAMPLES=["O clima hoje é bastante agradável, com céu claro e vento leve.",
"Certifique-se de que todos os documentos sejam apresentados até a data limite.",
"Agradecemos sua resposta rápida e esperamos poder colaborar novamente.",
"O sistema requer uma atualização do software para funcionar corretamente.",
"Você viu o novo filme que foi lançado na semana passada?"]
SV_EXAMPLES=["Vädret är ganska trevligt idag, med klart väder och lätt vind.",
"Se till att alla dokument lämnas in innan förfallodagen.",
"Tack för din snabba respons och vi hoppas att vi kan samarbeta ytterligare.",
"Systemet kräver en uppdatering av programvaran för att fungera korrekt.",
"Har du sett den nya filmen som släpptes förra veckan?"]