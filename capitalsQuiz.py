import random, sys   #There are 198 countries.
capitalsdict={'Afghanistan': 'Kabul', 'Albania': 'Tirana', 'Algeria': 'Algiers', 'Andorra': 'Andorra la Vella',
        'Angola': 'Luanda', 'Antigua and Barbuda': "Saint John's", 'Argentina': 'Buenos Aires',
        'Armenia': 'Yerevan', 'Australia': 'Canberra', 'Austria': 'Vienna', 'Azerbaijan': 'Baku',
        'Bahamas': 'Nassau', 'Bahrain': 'Manama', 'Bangladesh': 'Dhaka', 'Barbados': 'Bridgetown',
        'Belarus': 'Minsk', 'Belgium': 'Brussels', 'Belize': 'Belmopan', 'Benin': 'Porto-Novo',
        'Bhutan': 'Thimphu', 'Bolivia': 'Sucre', 'Bosnia and Herzegovina': 'Sarajevo', 'Botswana': 'Gaborone',
        'Brazil': 'Brasilia', 'Brunei': 'Bandar Seri Begawan', 'Bulgaria': 'Sofia', 'Burkina Faso': 'Ouagadougou',
        'Burundi': 'Gitega', 'Cabo Verde': 'Praia', 'Cambodia': 'Phnom Penh', 'Cameroon': 'Yaounde',
        'Canada': 'Ottawa', 'Central African Republic': 'Bangui', 'Chad': "N'Djamena", 'Chile': 'Santiago',
        'China': 'Beijing', 'Colombia': 'Bogotá', 'Comoros': 'Moroni', 'Congo': 'Kinshasa',
        'Congo Brazzaville': 'Brazzaville', 'Costa Rica': 'San Jose', "Cote d'Ivoire": 'Yamoussoukro',
        'Croatia': 'Zagreb', 'Cuba': 'Havana', 'Cyprus': 'Nicosia', 'Czechia': 'Prague', 'Denmark': 'Copenhagen',
        'Djibouti': 'Djibouti', 'Dominica': 'Roseau', 'Dominican Republic': 'Santo Domingo', 'Ecuador': 'Quito',
        'Egypt': 'Cairo', 'El Salvador': 'San Salvador', 'Equatorial Guinea': 'Malabo', 'Eritrea': 'Asmara',
        'Estonia': 'Tallinn', 'Eswatini': 'Mbabane', 'Ethiopia': 'Addis Ababa', 'Fiji': 'Suva',
        'Finland': 'Helsinki', 'France': 'Paris', 'Gabon': 'Libreville', 'Gambia': 'Banjul', 'Georgia': 'Tbilisi',
        'Germany': 'Berlin', 'Ghana': 'Accra', 'Greece': 'Athens', 'Grenada': "Saint George's",
        'Guatemala': 'Guatemala City', 'Guinea': 'Conakry', 'Guinea-Bissau': 'Bissau', 'Guyana': 'Georgetown',
        'Haiti': 'Port-au-Prince', 'Honduras': 'Tegucigalpa', 'Hungary': 'Budapest', 'Iceland': 'Reykjavik',
        'India': 'New Delhi', 'Indonesia': 'Jakarta', 'Iran': 'Tehran', 'Iraq': 'Baghdad', 'Ireland': 'Dublin',
        'Israel': 'West Jerusalem', 'Italy': 'Rome', 'Jamaica': 'Kingston', 'Japan': 'Tokyo', 'Jordan': 'Amman',
        'Kazakhstan': 'Nur-Sultan', 'Kenya': 'Nairobi', 'Kiribati': 'Tarawa', 'Kosovo': 'Pristina',
        'Kuwait': 'Kuwait City', 'Kyrgyzstan': 'Bishkek', 'Laos': 'Vientiane', 'Latvia': 'Riga',
        'Lebanon': 'Beirut', 'Lesotho': 'Maseru', 'Liberia': 'Monrovia', 'Libya': 'Tripoli',
        'Liechtenstein': 'Vaduz', 'Lithuania': 'Vilnius', 'Luxembourg': 'Luxembourg', 'Country': 'Capital city',
        'Madagascar': 'Antananarivo', 'Malawi': 'Lilongwe', 'Malaysia': 'Kuala Lumpur', 'Maldives': 'Male',
        'Mali': 'Bamako', 'Malta': 'Valletta', 'Marshall Islands': 'Majuro', 'Mauritania': 'Nouakchott',
        'Mauritius': 'Port Louis', 'Mexico': 'Mexico City', 'Micronesia': 'Palikir', 'Moldova': 'Chisinau',
        'Monaco': 'Monaco', 'Mongolia': 'Ulaanbaatar', 'Montenegro': 'Podgorica', 'Morocco': 'Rabat',
        'Mozambique': 'Maputo', 'Myanmar': 'Naypyidaw', 'Namibia': 'Windhoek', 'Nauru': 'Yaren District',
        'Nepal': 'Kathmandu', 'Netherlands': 'Amsterdam', 'New Zealand': 'Wellington', 'Nicaragua': 'Managua',
        'Niger': 'Niamey', 'Nigeria': 'Abuja', 'North Korea': 'Pyongyang', 'North Macedonia': 'Skopje',
        'Norway': 'Oslo', 'Oman': 'Muscat', 'Pakistan': 'Islamabad', 'Palau': 'Ngerulmud', 'Palestine': 'East Jerusalem',
        'Panama': 'Panama City', 'Papua New Guinea': 'Port Moresby', 'Paraguay': 'Asunción', 'Peru': 'Lima',
        'Philippines': 'Manila', 'Poland': 'Warsaw', 'Portugal': 'Lisbon', 'Qatar': 'Doha', 'Romania': 'Bucharest',
        'Russia': 'Moscow', 'Rwanda': 'Kigali', 'Saint Kitts and Nevis': 'Basseterre', 'Saint Lucia': 'Castries',
        'Saint Vincent and the Grenadines': 'Kingstown', 'Samoa': 'Apia', 'San Marino': 'San Marino',
        'Sao Tome and Principe': 'São Tomé', 'Saudi Arabia': 'Riyadh', 'Senegal': 'Dakar', 'Serbia': 'Belgrade',
        'Seychelles': 'Victoria', 'Sierra Leone': 'Freetown', 'Singapore': 'Singapore', 'Slovakia': 'Bratislava',
        'Slovenia': 'Ljubljana', 'Solomon Islands': 'Honiara', 'Somalia': 'Mogadishu', 'South Africa': 'Cape Town',
        'South Korea': 'Seoul', 'South Sudan': 'Juba', 'Spain': 'Madrid', 'Sri Lanka': 'Sri Jayawardenepura Kotte',
        'Sudan': 'Khartoum', 'Suriname': 'Paramaribo', 'Sweden': 'Stockholm', 'Switzerland': 'Bern', 'Syria': 'Damascus',
        'Taiwan': 'Taipei', 'Tajikistan': 'Dushanbe', 'Tanzania': 'Dodoma', 'Thailand': 'Bangkok', 'Timor-Leste': 'Dili',
        'Togo': 'Lomé', 'Tonga': 'Nukuʻalofa', 'Trinidad and Tobago': 'Port of Spain', 'Tunisia': 'Tunis',
        'Turkey': 'Ankara', 'Turkmenistan': 'Ashgabat', 'Tuvalu': 'Funafuti', 'Uganda': 'Kampala', 'Ukraine': 'Kyiv',
        'United Arab Emirates': 'Abu Dhabi', 'United Kingdom': 'London', 'United States of America': 'Washington, D.C.',
        'Uruguay': 'Montevideo', 'Uzbekistan': 'Tashkent', 'Vanuatu': 'Port Vila', 'Vatican City': 'Vatican City',
        'Venezuela': 'Caracas', 'Vietnam': 'Hanoi', 'Yemen': "Sana'a", 'Zambia': 'Lusaka', 'Zimbabwe': 'Harare'}
countrieslist=list(capitalsdict)
def capitalquiz():
    global win, loss
    quizcountry=random.choice(countrieslist)
    print('What is the capital of '+quizcountry+'?')
    correctanswer=capitalsdict[quizcountry]
    choicepool=[correctanswer]
    for i in range(3):
        while True:
            tempcapital=capitalsdict[random.choice(countrieslist)]
            if tempcapital==correctanswer:
                continue
            choicepool.append(tempcapital)
            break
    random.shuffle(choicepool)
    random.shuffle(choicepool)
    choicepooldict={'a':choicepool[0],'b':choicepool[1],'c':choicepool[2],'d':choicepool[3]}
    for k, v in choicepooldict.items():
        print(k+'. '+v)
    while True:
        response=input()
        if response in 'abcd':
            answer=choicepooldict[response]
            break
        else:
            print('invalid answer: try again')
    if answer==correctanswer:
        print('Correct!\n')
        win+=1
    else:
        print(random.choice(lossoutputs)+correctanswer+'.\n')
        loss+=1

def capitalquiz2():
    global win, loss
    correctanswer=random.choice(countrieslist)
    quizcapital=capitalsdict[correctanswer]
    print(quizcapital+' is the capital of....')
    choicepool=[correctanswer]
    for i in range(3):
        while True:
            tempcountry=random.choice(countrieslist)
            if tempcountry==correctanswer:
                continue
            choicepool.append(tempcountry)
            break
    random.shuffle(choicepool)
    random.shuffle(choicepool)
    choicepooldict={'a':choicepool[0],'b':choicepool[1],'c':choicepool[2],'d':choicepool[3]}
    for k, v in choicepooldict.items():
        print(k+'. '+v)
    while True:
        response=input()
        if response in 'abcd':
            answer=choicepooldict[response]
            break
        else:
            print('invalid answer: try again')
    if answer==correctanswer:
        print('Correct!\n')
        win+=1
    else:
        print(random.choice(lossoutputs)+correctanswer+'.\n')
        loss+=1

lossoutputs=['Sorry, the answer is ','Oops! It\'s ','The correct answer is ','Sorry, it is ']
win=0
loss=0
while True:
    for q in range(10):
        smalldice=random.randint(1,4)
        if smalldice==1:
            capitalquiz2()
        else:
            capitalquiz()
    if win==10:
        print('Congratulations, you answered all questions correctly!')
    elif loss==10:
        print('Sorry, you answer all questions incorrectly.')
    else:
        print('Finished! The results are\nwins: '+str(win)+'\nlosses: '+str(loss))
    while True:
        print('Type "r" to replay or "q" to quit.\n')
        response2=input()
        if response2.lower()=='r':
            break
        elif response2.lower()=='q':
            sys.exit()
        else:
            continue
