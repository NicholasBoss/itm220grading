import os
import platform
os_name = platform.system()
try: 
    import mysql.connector
except ImportError or ModuleNotFoundError:
    print("MYSQL module not found. Installing...")
    if os_name == 'Windows':
        os.system("pip install mysql-connector-python")
    elif os_name == 'Linux' or os_name == 'Darwin':
        os.system("pip3 install mysql-connector-python")
    import mysql.connector
    print("MYSQL module installed")
import decimal
import datetime


def format_list(list):
    list = [str(item) for item in list]
    new_list = '\n'.join(list)
    new_list = new_list.replace('[', '')
    new_list = new_list.replace(']', '')
    new_list = new_list.replace("'", "")
    return new_list

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="student",
    password="student",
)

# Create a cursor
mycursor = mydb.cursor()


correct_answer_list = [ # ---------------------------------------------------------------------
                        # Question 1
                        # ---------------------------------------------------------------------
                        [['Aaron'], ['Adams'], ['Adler'], ['Aikman'],
                        ['Akey'], ['Alan'], ['Aldred'], ['Alexander'], 
                        ['Allen'], ['Allman'], ['Alvarado'], ['Alworth'], 
                        ['Anastasio'], ['Anders'], ['Anderson'], ['Arango'], 
                        ['Argento'], ['Arias'], ['Arkhipov'], ['Armstead'], 
                        ['Armstrong'], ['Arnaert'], ['Arnold'], ['Arnott'], 
                        ['Aromashodu'], ['Astley'], ['Atkins'], ['Azubuike'], 
                        ['Babbit'], ['Baker'], ['Bankert'], ['Barbeau'], 
                        ['Barbosa'], ['Bardem'], ['Bare'], ['Barker'], 
                        ['Barlow'], ['Barr'], ['Bartel'], ['Bartos'], 
                        ['Basnight'], ['Bates'], ['Bauman'], ['Bazuin'], 
                        ['Beaubois'], ['Beckham'], ['Beckwith'], ['Bell'], 
                        ['Bellairs'], ['Bellinger'], ['Bender'], ['Bennett'], 
                        ['Benoit'], ['Benson'], ['Berben'], ['Berenger'], 
                        ['Berg'], ['Bergesen'], ['Bergman'], ['Berkoff'], 
                        ['Berlow'], ['Berrian'], ['Berry'], ['Berti'], 
                        ['Bess'], ['Bettany'], ['Bettencourt'], ['Bierbrodt'], 
                        ['Billingsley'], ['Billington'], ['Birkins'], ['Bishop'], 
                        ['Bissonnette'], ['Bjork'], ['Blair'], ['Blazejowski'], 
                        ['Blunstone'], ['Bofshever'], ['Bogans'], ['Bolooki'], 
                        ['Boose'], ['Boswell'], ['Bosworth'], ['Boulanger'], 
                        ['Braaten'], ['Branan'], ['Branson'], ['Braugher'], 
                        ['Brennan'], ['Breslin'], ['Brien'], ['Brisebois'], 
                        ['Bristol'], ['Brock'], ['Brodin'], ['Brody'], 
                        ['Brogna'], ['Brolin'], ['Brosh'], ['Bross'], 
                        ['Brown'], ['Browne'], ['Browning'], ['Brubeck'], 
                        ['Brunette'], ['Bryant'], ['Buchwitz'], ['Budaj'], 
                        ['Budig'], ['Bujold'], ['Bulow'], ['Burke'], ['Burton'], 
                        ['Bush'], ['Butler'], ['Butsayev'], ['Byrne'], ['Caldwell'], 
                        ['Callaway'], ['Cameron'], ['Cammack'], ['Campbell'], ['Cannida'], 
                        ['Capecci'], ['Capelle'], ['Cappelen'], ['Carey'], ['Carr'], 
                        ['Carter'], ['Cash'], ['Casiraghi'], ['Cassidy'], ['Castillo'], 
                        ['Casto'], ['Cavalli'], ['Cello'], ['Chamberlin'], ['Chambers'], 
                        ['Charron'], ['Chastain'], ['Cheek'], ['Cheslin'], ['Childs'], 
                        ['Chodan'], ['Chon'], ['Chouinard'], ['Chung'], ['Cigliuti'], 
                        ['Cimino'], ['Clanton'], ['Clark'], ['Clarke'], ['Clement'], 
                        ['Cobham'], ['Cohen'], ['Colaiacovo'], ['Cole'], ['Coleman'], 
                        ['Collins'], ['Collison'], ['Colston'], ['Condra'], ['Connery'], 
                        ['Conradt'], ['Conway'], ['Cook'], ['Corwin'], ['Coster-Waldau'], 
                        ['Counsell'], ['Coutts'], ['Cox'], ['Coyula'], ['Crandell'], 
                        ['Crawford'], ['Crichton'], ['Cronin'], ['Crosby'], ['Crossman'], 
                        ['Crow'], ['Crowe'], ['Cucca'], ['Cunti'], ['Currie'], ['Curtis'], 
                        ['Cutolo'], ['D'], ['Dale'], ['Dallimore'], ['Dalman'], ['Damond'], 
                        ['Daniels'], ['Daniher'], ['Davis'], ['Day'], ['Dean'], ['DeJesus'], 
                        ['DeLamielleure'], ['Dembia'], ['DePaula'], ['Desiderio'], ['Deyama'], 
                        ['Dharma'], ['Diamond'], ['Diaz'], ['Dillard'], ['Dillon'], ['Discala'], 
                        ['Dollar'], ['Donato'], ['Donnelly'], ['Dory'], ['Douglass'], ['Duda'], 
                        ['Dumas'], ['Dunbar'], ['Dunn'], ['Durand'], ['Dusick'], ['Dutt'], 
                        ['Dyke'], ['Dykes'], ['Eatock'], ['Economos'], ['Eden'], ['Edwards'], 
                        ['Eidsvold'], ['Elali'], ['Elliot'], ['Elliott'], ['Ellis'], ['Ellison'], 
                        ['Elmidoro'], ['Enberg'], ['Epps'], ['Evans'], ['Everitt'], 
                        ['Fairchild'], ['Faires'], ['Famiglietti'], ['Fanene'], ['Farina'], 
                        ['Farmer'], ['Farr'], ['Farrait'], ['Farrow'], ['Fasani'], ['Fata'], 
                        ['Fay'], ['Feagles'], ['Feehily'], ['Fenison'], ['Fenton'], 
                        ['Fernandes'], ['Ferone'], ['Ferry'], ['Fielder'], ['Fields'], 
                        ['Fischer'], ['Floyd'], ['Foley'], ['Foote'], ['Fowler'], ['Fox'],
                        ['Frantz'], ['Frascatore'], ['Freeman'], ['Freia'], ['Frejndlikh'], 
                        ['Frode'], ['Fromm'], ['Fry'], ['Fuller'], ['Gaiman'], ['Galiano'], 
                        ['Gallinari'], ['Garcia'], ['Garfunkel'], ['Garroz'], ['Gary'], 
                        ['Gaye'], ['Gaylor'], ['Geiger'], ['George'], ['Ghadie'], ['Gibson'], 
                        ['Gift'], ['Giles'], ['Gillespie'], ['Gilman'], ['Giordano'], 
                        ['Giovinazzo'], ['Gissell'], ['Gleeson'], ['Goffin'], ['Gogan'],
                        ['Gomes'], ['Gonzalez'], ['Goodman'], ['Gorbe'], ['Gorges'], 
                        ['Gortman'], ['Gould'], ['Grace'], ['Graham'], ['Grant'],
                        ['Graves'], ['Green'], ['Greene'], ['Grey'], ['Grieve'], 
                        ['Griffin'], ['Griffith'], ['Grimes'], ['Grimm'], ['Gross'], 
                        ['Gugino'], ['Guiles'], ['Gulstorff'], ['Gunther'], ['Gustin'], 
                        ['Hale'], ['Haliburton'], ['Hall'], ['Hamill'], ['Hamilton'], 
                        ['Hammond'], ['Hanners'], ['Hanratty'], ['Hargrave'], ['Harper'], 
                        ['Harrell'], ['Harris'], ['Haslinger'], ['Hathaway'], ['Hawkins'], 
                        ['Haworth'], ['Hayden'], ['Hayes'], ['Hayward'], ['Hebert'], ['Heck'], 
                        ['Henderson'], ['Hendricks'], ['Henley'], ['Henner'], ['Hennessy'], 
                        ['Henrik'], ['Hermsen'], ['Hiddink'], ['Higgins'], ['Hill'], 
                        ['Hirondelle'], ['Hodel'], ['Hodgson'], ['Hoffmann'], ['Hogg'], 
                        ['Holdman'], ['Holliday'], ['Honda'], ['Hooks'], ['Hopkins'], 
                        ['Houser'], ['Howell'], ['Hudin'], ['Hulett'], ['Hutch'], ['Hytner'], 
                        ['II'], ['III'], ['Imperioli'], ['Irvine'], ['Isley'], ['IV'], 
                        ['Ivanyi'], ['Izutsu'], ['Izzo'], ['Jackson'], ['James'], 
                        ['Jeffcoat'], ['Jeni'], ['Jeter'], ['Jezina'], ['Joe'], ['John'], 
                        ['Johnson'], ['Jokinen'], ['Jones'], ['Jovanovic'], ['Jovanovski'], 
                        ['Julia'], ['Kacyvenski'], ['Kamien'], ['Kania'], ['Karlstrom'], 
                        ['Kasperavicius'], ['Kawai'], ['Keenan'], ['Kehoe'], ['Keith'], 
                        ['Kelis'], ['Kelly'], ['Kendall'], ['Kennedy'], ['Kerr'], ['Kersey'], 
                        ['Kesler'], ['Kessler'], ['Khan'], ['Kim'], ['Kimbrough'], ['Kimura'], 
                        ['Kinchla'], ['Kind'], ['King'], ['Kirsch'], ['Kishitani'], ['Klein'], 
                        ['Kline'], ['Klinga'], ['Knight'], ['Knowings'], ['Kohinata'], ['Koliwad'], 
                        ['Kolker'], ['Konishi'], ['Korot'], ['Krall'], ['Kranjcar'], 
                        ['Kubina'], ['Kuhn'], ['Kunitz'], ['LaBour'], ['Lachance'], 
                        ['Laing'], ['Lamas'], ['Lamaze'], ['Lane'], ['Laswell'], ['Lavalais'], 
                        ['Lavorato'], ['Lawrence'], ['Leaf'], ['Ledden'], ['Ledger'], ['LeDoux'], 
                        ['Lee'], ['Leigh'], ['Leino'], ['Leskanic'], ['Leslie'], ['Lester'], 
                        ['Lewis'], ['Ligabue'], ['Lightfoot'], ['Lince'], ['Lind'], ['Liriano'], 
                        ['Little'], ['Liu'], ['Livanova'], ['Loera'], ['Loffler'], ['Logan'], 
                        ['LoMenzo'], ['Lopez'], ['Lorini'], ['Love'], ['Lulu'], ['Luna'], 
                        ['Lundmark'], ['Lyman'], ['Lyons'], ['MacLane'], ['MacLean'], ['Madison'], 
                        ['Magloire'], ['Magnuson'], ['Maguire'], ['Maholm'], ['Mahon'], 
                        ['Mahoney'], ['Mahony'], ['Maiga'], ['Malone'], ['Mangum'], 
                        ['Manilow'], ['Manning'], ['Marceline'], ['March'], ['Marciano'], 
                        ['Marcos'], ['Marion'], ['Marleau'], ['Marriott'], ['Marti'], 
                        ['Martin'], ['Martinez'], ['Masaro'], ['Massey'], ['Matenopoulos'], 
                        ['Mathews'], ['Matua'], ['May'], ['McBrain'], ['McBride'], 
                        ['McCarthy'], ['McCourty'], ['McCully'], ['McCune'], ['McCutcheon'], 
                        ['McDaniels'], ['McDonald'], ['McFadden'], ['McGourty'], 
                        ['McGruder'], ['McGuinn'], ['McKenna'], ['McLaughlin'], ['McMillen'], 
                        ['McQuistan'], ['McSwain'], ['McWilliams'], ['Mentana'], ['Menyongar'], 
                        ['Merloni'], ['Michaels'], ['Midorikawa'], ['Mifune'], ['Miles'], 
                        ['Miller'], ['Minor'], ['Mizuno'], ['Moeller'], ['Molinari'], ['Monaghan'], 
                        ['Montador'], ['Montag'], ['Montgomery'], ['Moore'], ['Morasca'], 
                        ['Moreno'], ['Morgan'], ['Morrell'], ['Morris'], ['Moschitto'], 
                        ['Moss'], ['Mota'], ['Mowrey'], ['Moyano'], ['Mrozowska'], ['Muc'], 
                        ['Mulgrew'], ['Muller'], ['Mullins'], ['Mumy'], ['Murphy'], ['Murray'], 
                        ['Myers'], ['Nagamura'], ['Narain'], ['Navratilova'], ['Neal'], 
                        ['Neidig'], ['Neill'], ['Nelson'], ['Nembhard'], ['Neville'], 
                        ['Nevin'], ['Newbury'], ['Newley'], ['Newman'], ['Nguyen'], 
                        ['Nichol'], ['Nicodemou'], ['Nivola'], ['Nixon'], ['Noah'], 
                        ['North'], ['Northern'], ['Norton-Taylor'], ['Norum'], ['Nowak'], 
                        ['Nugent'], ['Oats'], ['Odrick'], ['Orange'], ['Osborn'], 
                        ['Osbourne'], ['Osmond'], ['Overall'], ['Owens'], ['Ozawa'], 
                        ['Palmer'], ['Palushaj'], ['Parcells'], ['Park'], ['Parker'], 
                        ['Paskuda'], ['Patera'], ['Pattinson'], ['Pavelski'], ['Pearson'], 
                        ['Peca'], ['Pedersen'], ['Pennington'], ['Pereira'], ['Perez'], 
                        ['Peroff'], ['Perreault'], ['Peters'], ['Peterson'], ['Petrick'], 
                        ['Petrovich'], ['Pettersen'], ['Phillips'], ['Picard'], ['Piper'], 
                        ['Polanski'], ['Powers'], ['Preki'], ['Presbury'], ['Previn'], 
                        ['Prior'], ['Pujals'], ['Raghavachary'], ['Ramo'], ['Randall'], 
                        ['Randolph'], ['Rarebell'], ['Raven'], ['Ready'], ['Redgrave'], 
                        ['Redman'], ['Rekar'], ['Remick'], ['Renberg'], ['Renna'], 
                        ['Rheinecker'], ['Rhodes'], ['Rhoton'], ['Rice'], ['Richards'], 
                        ['Richey'], ['Richmond'], ['Ridley'], ['Rieffel'], ['Riessner'], 
                        ['Riggan'], ['Rincon'], ['Rioux'], ['Ripa'], ['Rissmiller'], 
                        ['Ritchie'], ['Rix'], ['Robertson'], ['Robinson'], ['Rockett'], 
                        ['Rodin'], ['Rodriguez'], ['Rogowski'], ['Rolen'], ['Romero'], 
                        ['Romo'], ['Rosario'], ['Rose'], ['Rourke'], ['Rowlands'], 
                        ['Rudd'], ['Rudolph'], ['Ruff'], ['Rundgren'], ['Runyon'], 
                        ['Rushing'], ['Rusler'], ['Russell'], ['Ruutu'], ['Ryland'], 
                        ['Ryo'], ['Saartamo'], ['Salas'], ['Sanchez'], ['Sandberg'], 
                        ['Sanders'], ['Sandoval'], ['Sankey'], ['Sartori'], ['Saul'], 
                        ['Save'], ['Scarborough'], ['Schaffel'], ['Schefft'], 
                        ['Schexnayder'], ['Schlesinger'], ['Schmoll'], ['Schutt'],
                        ['Scott'], ['Seabrook'], ['Seagraves'], ['Seda'], 
                        ['Seguignol'], ['Semple'], ['Seru'], ['Shah'], 
                        ['Shanks'], ['Shaud'], ['Shaw'], ['Shenkarow'], 
                        ['Shields'], ['Shimojo'], ['Shirow'], ['Shoals'], ['Shuey'], 
                        ['Shyer'], ['Simmons'], ['Sims'], ['Skoula'], ['Skye'], ['Sloan'], 
                        ['Smalley'], ['Smith'], ['Snider'], ['Snowdon'], ['Soentpiet'], 
                        ['Soroko'], ['Sosa'], ['Spall'], ['Spann'], ['Spencer'], 
                        ['Spielberg'], ['Stahl'], ['Stamps'], ['Staples'], ['Steele'], 
                        ['Stein'], ['Steinauer'], ['Stern'], ['Stevenson'], ['Stewart'], 
                        ['Stick'], ['Stoddard'], ['Storz'], ['Stouffer'], ['Sullivan'], 
                        ['Summerall'], ['Svendsen'], ['Sweeney'], ['Tanaka'], ['Tardy'], 
                        ['Taylor'], ['Tejada'], ['Tendler'], ['Tennant'], ['Tettleton'], 
                        ['Thibodeaux'], ['Thiessen'], ['Thomas'], ['Thompson'], ['Thomson'], 
                        ['Thorpe'], ['Tibbetts'], ['Tiffin'], ['Tipton'], ['Tokiwa'], 
                        ['Tollefsen'], ['Tomei'], ['Tomlin'], ['Tomuri'], ['Tovar'], ['Towne'], 
                        ['Tracie'], ['Tracy'], ['Tretiak'], ['Tritt'], ['Trombley'], ['Tsatsos'], 
                        ['Tubbs'], ['Tucker'], ['Tunick'], ['Turner'], ['Twombly'], ['Tyler'], 
                        ['Tynan'], ['Tyson'], ['Uecker'], ['Valentine'], ['Vance'], ['Vanda'], 
                        ['Vann'], ['Vazquez'], ['VelJohnson'], ['Verlander'], ['Verlinden'], 
                        ['Viharo'], ['VII'], ['Villarreal'], ['Vitale'], ['Volodarsky'], 
                        ['Waddell'], ['Waggoner'], ['Wallace'], ['Walters'], ['Wanting'], 
                        ['Ward'], ['Ware'], ['Wargo'], ['Warne'], ['Waters'], ['Watkins'], 
                        ['Watts'], ['Wayne'], ['Weathers'], ['Weaver'], ['Weiler'], 
                        ['Weinger'], ['Wells'], ['Westman'], ['Whalen'], ['Whannell'], 
                        ['Whibley'], ['White'], ['Whitley'], ['Wiberg'], ['Wiggins'], 
                        ['Wilhelmsen'], ['Wilkins'], ['Willey'], ['Williams'], ['Williamson'], 
                        ['Willis'], ['Wilm'], ['Wilson'], ['Wimbley'], ['Winfield'], 
                        ['Winger'], ['Winwood'], ['Wisniewski'], ['Witasick'], ['Wojda'], 
                        ['Wolfe'], ['Woods'], ['Woodward'], ['Woolf'], ['Wright'], 
                        ['Xavier'], ['Yamaoka'], ['Yates'], ['Zandt'], ['Zarchen'], 
                        ['Zegers'], ['Zelenka'], ['Zellner'], ['Zettler'], ['Zima'], 
                        ['Zomer'], ['Zonca'], ['Zucker'], ['Zwick-Nash']],
                        # ---------------------------------------------------------------------
                        # Question 2
                        # ---------------------------------------------------------------------
                        [['Afghanistan Airlines', 'BAMYAN'], #2
                         ['Albania Airlines', 'RINAS'], 
                         ['American Samoa Airli', 'PAGO PAGO INTL'], 
                         ['Angola Airlines', 'ALBANO MACHADO'], 
                         ['Argentina Airlines', 'ALMIRANTE ZAR'], 
                         ['Australia Airlines', 'ADELAIDE INTL'], 
                         ['Azerbaijan Airlines', 'BINA'], 
                         ['Bahamas Airlines', 'ANDROS TOWN INTL'], 
                         ['Belarus Airlines', 'BREST'], 
                         ['Bhutan Airlines', 'PARO'], 
                         ['Bolivia Airlines', 'APOLO'], 
                         ['Brazil Airlines', 'AEROCLUB'], 
                         ['Bulgaria Airlines', 'BURGAS'], 
                         ['Caicos Is Airlines', 'CONCH BAR'], 
                         ['Central African Rep ', "M'POKO"], 
                         ['Chad Airlines', 'ABECHE'], 
                         ['Colombia Airlines', 'AGUAS CLARAS'], 
                         ['Croatia Airlines', 'CILIPI'], 
                         ['Cuba Airlines', 'ABEL SANTA MARIA'], 
                         ['Cyprus Airlines', 'AKROTIRI AB'], 
                         ['Czech Airlines', 'HOLESOV'], 
                         ['Dakhla And Laayoune ', 'DAKHLA'], 
                         ['Denmark Airlines', 'AALBORG'], 
                         ['Djibouti Airlines', 'AMBOULI'], 
                         ['Dominica Airlines', 'CANEFIELD INTL'], 
                         ['Ecuador Airlines', 'CHACHOAN'], 
                         ['Egypt Airlines', 'ABU SIMBEL'], 
                         ['El Salvador Airlines', 'EL SALVADOR INTL'],
                         ['Equatorial Guinea Ai', 'BATA'], 
                         ['Eritrea Airlines', 'ASMARA INTL'], 
                         ['Estonia Airlines', 'KARDLA'], 
                         ['Ethiopia Airlines', 'A.T.D. YILMA INTL'], 
                         ['Falkland Is Airlines', 'MOUNT PLEASANT'], 
                         ['Fiji Is Airlines', 'LABASA'], 
                         ['France Airlines', 'AIX-LES-BAINS'], 
                         ['Gabon Airlines', 'BITAM'], 
                         ['Georgia Airlines', 'KOPITNARI'], 
                         ['Ghana Airlines', 'KOTOKA INTL'], 
                         ['Gibraltar Airlines', 'GIBRALTAR AB'], 
                         ['Greece Airlines', 'AGRINION AB'], 
                         ['Guadeloupe Airlines', 'BAILLIF'], 
                         ['Haiti Airlines', 'CAP HAITIEN INTL'], 
                         ['Honduras Airlines', 'CATACAMAS'], 
                         ['Hungary Airlines', 'FERIHEGY'], 
                         ['Iceland Airlines', 'AKUREYRI'], 
                         ['India Airlines', 'AGARTALA'], 
                         ['Iran Airlines', 'ABADAN'], 
                         ['Isla De Pascua Airli', 'MATAVERI INTL'], 
                         ['Italy Airlines', 'ALBENGA'], 
                         ['Ivory Coast Airlines', 'ABENGOUROU'], 
                         ['Jamaica Airlines', 'NORMAN MANLEY INTL'], 
                         ['Jerusalem Airlines', 'JERUSALEM'], 
                         ['Johnston Atoll Airli', 'JOHNSTON ATOLL'], 
                         ['Kazakhstan Airlines', 'AKTAU'], 
                         ['Kenya Airlines', 'AMBOSELI'], 
                         ['Kiribati Airlines', 'BONRIKI INTL'], 
                         ['Korea Airlines', 'A-306'], 
                         ['Kuwait Airlines', 'KUWAIT INTL'], 
                         ['Kyrgyzstan Airlines', 'MANAS'],
                         ['Laos Airlines', 'ATTOPEU'], 
                         ['Lebanon Airlines', 'BEIRUT INTL'], 
                         ['Liberia Airlines', 'BUCKANAN'], 
                         ['Luxembourg Airlines', 'LUXEMBOURG'], 
                         ['Macau Airlines', 'MACAU INTL'], 
                         ['Melilla Airlines', 'MELILLA'], 
                         ['Micronesia Airlines', 'BABELTHUAP/ KOROR'], 
                         ['Moldova Airlines', 'CHISINAU'], 
                         ['Myanmar Airlines', 'BAGAN'], 
                         ['Namibia Airlines', 'ARANDIS'], 
                         ['Nepal Airlines', 'BAGLUNG'], 
                         ['Nicaragua Airlines', 'BLUEFIELDS'], 
                         ['Northern Mariana Is ', 'ROTA I INTL'], 
                         ['Oman Airlines', 'KHASAB AB'], 
                         ['Pakistan Airlines', 'ALLAMA IQBAL INTL'], 
                         ['Peru Airlines', 'ALEJANDRO VELAZCO ASTETE'], 
                         ['Philippines Airlines', 'BACOLOD'], 
                         ['Poland Airlines', 'BABIMOST'], 
                         ['Puerto Rico Airlines', 'LUIS MUNOZ MARIN INTL'], 
                         ['Qatar Airlines', 'DOHA INTL'], 
                         ['Reunion Airlines', 'GILLOT'], 
                         ['Romania Airlines', 'ARAD'], 
                         ['Russia Airlines', 'ABAKAN'], 
                         ['Rwanda Airlines', 'BUTARE'], 
                         ['San Andres Airlines', 'GUSTAVO ROJAS PINILLA'], 
                         ['Senegal Airlines', 'BAKEL'], 
                         ['Sierra Leone Airline', 'BO'], 
                         ['Slovakia Airlines', 'KOSICE'], 
                         ['Solomon Is Airlines', 'GIZO'], 
                         ['Spain Airlines', 'A CORUNA'], 
                         ['Sri Lanka Airlines', 'AMPARAI'], 
                         ['St Kitts Airlines', 'NEWCASTLE'], 
                         ['Sudan Airlines', 'ATBARA'], 
                         ['Swaziland Airlines', 'MATSAPHA INTL'], 
                         ['Syria Airlines', 'ALEPPO INTL'], 
                         ['Taiwan Airlines', 'CHIANG KAI SHEK INTL'], 
                         ['Thailand Airlines', 'BANGKOK INTL'], 
                         ['Togo Airlines', 'NIAMTOUGOU'], 
                         ['Trinidad Airlines', 'CROWN POINT'], 
                         ['Tunisia Airlines', 'CARTHAGE'], 
                         ['Uganda Airlines', 'ARUA'], 
                         ['Ukraine Airlines', "BORYSPIL'"], 
                         ['United Arab Emirates', 'ABU DHABI INTL'], 
                         ['Uruguay Airlines', 'ARTIGAS INTL'], 
                         ['Uzbekistan Airlines', 'BUKHARA'], 
                         ['Vanuatu Airlines', 'BAUERFIELD'], 
                         ['Venezuela Airlines', 'ALBERTO CARNEVALLI'], 
                         ['Vietnam Airlines', 'BUONMATHUOT'], 
                         ['Wake I Airlines', 'WAKE I AAF'], 
                         ['Western Samoa Airlin', 'FAGALI'], 
                         ['Yemen Airlines', 'ABBS'], 
                         ['Yugoslavia Airlines', 'BELGRADE'], 
                         ['Zambia Airlines', 'CHIPATA'], 
                         ['Zimbabwe Airlines', 'BUFFALO RANGE']],
                        # ---------------------------------------------------------------------
                        # Question 3
                        # ---------------------------------------------------------------------
                        [['A R S SPORT STRIP', 'UNITED STATES'], #3
                         ['ABERDEEN REGL', 'UNITED STATES'], 
                         ['ABERNATHY', 'UNITED STATES'], 
                         ['ABILENE REGL', 'UNITED STATES'], 
                         ['ACADIANA REGL', 'UNITED STATES'], 
                         ['ACCOMACK CO', 'UNITED STATES'], 
                         ['ADA MUN', 'UNITED STATES'], 
                         ['ADAK', 'UNITED STATES'], 
                         ['ADAMS', 'UNITED STATES'], 
                         ['ADDINGTON', 'UNITED STATES'], 
                         ['ADDISON', 'UNITED STATES'], 
                         ['ADIRONDACK REGL', 'UNITED STATES'], 
                         ['AFTON MUN', 'UNITED STATES'], 
                         ['AIKEN MUN', 'UNITED STATES'], 
                         ['AINSWORTH MUN', 'UNITED STATES'], 
                         ['AIRBORNE', 'UNITED STATES'], 
                         ['AIRLAKE', 'UNITED STATES'], 
                         ['AITKIN MUN - KURTZ', 'UNITED STATES'], 
                         ['AKRON FULTON INTL', 'UNITED STATES'], 
                         ['AKRON-CANTON REGL', 'UNITED STATES']],
                        # ---------------------------------------------------------------------
                        # Question 4
                        # ---------------------------------------------------------------------
                        [['A R S SPORT STRIP', None, '7Y7'], #4
                         ['A-511 AAF', None, 'RKSG'], 
                         ['AARS', None, 'EKVH'], 
                         ['AAVAHELUKKA', None, 'EFAA'], 
                         ['ABA', None, 'FZJF'], 
                         ['ABARE', None, 'SDLI'], 
                         ['ABBEVILLE', None, 'LFOI'], 
                         ['ABBEYSHRULE', None, 'EIAB'], 
                         ['ABERNATHY', None, 'KGZS'], ['ABERPORTH', None, 'EGFA']],
                        # ---------------------------------------------------------------------
                        # Question 5
                        # ---------------------------------------------------------------------
                        [['LU8903', '10:00:00', '0:51:00', 'Luxembourg Airlines', 1], 
                         ['TH1768', '10:00:00', '19:29:00', 'Thailand Airlines', 1], 
                         ['BU3447', '10:01:00', '19:07:00', 'Bulgaria Airlines', 1],
                         ['BU9691', '10:01:00', '23:37:00', 'Bulgaria Airlines', 1], 
                         ['CY2779', '10:01:00', '0:39:00', 'Cyprus Airlines', 1], 
                         ['JO7310', '10:01:00', '15:25:00', 'Johnston Atoll Airli', 1], 
                         ['KI9721', '10:02:00', '20:26:00', 'Kiribati Airlines', 1], 
                         ['DE4644', '10:02:00', '22:26:00', 'Denmark Airlines', 1], 
                         ['ST6158', '10:02:00', '22:44:00', 'St Kitts Airlines', 1], 
                         ['AZ7862', '10:03:00', '6:09:00', 'Azerbaijan Airlines', 1], 
                         ['IC8570', '10:03:00', '15:31:00', 'Iceland Airlines', 1], 
                         ['SY1381', '10:03:00', '15:10:00', 'Syria Airlines', 1], 
                         ['AM9153', '10:04:00', '11:59:00', 'American Samoa Airli', 1], 
                         ['EL9828', '10:04:00', '18:14:00', 'El Salvador Airlines', 1], 
                         ['YU9092', '10:04:00', '14:38:00', 'Yugoslavia Airlines', 1], 
                         ['CE3838', '10:05:00', '18:52:00', 'Central African Rep ', 1], 
                         ['DJ1287', '10:05:00', '17:51:00', 'Djibouti Airlines', 1], 
                         ['GU5693', '10:05:00', '15:16:00', 'Guadeloupe Airlines', 1], 
                         ['RU3079', '10:05:00', '0:41:00', 'Russia Airlines', 1], 
                         ['RU5633', '10:05:00', '20:50:00', 'Russia Airlines', 1], 
                         ['BE9463', '10:06:00', '22:54:00', 'Belarus Airlines', 1], 
                         ['EG9300', '10:06:00', '14:49:00', 'Egypt Airlines', 1], 
                         ['JO2925', '10:06:00', '2:39:00', 'Johnston Atoll Airli', 1], 
                         ['EL1731', '10:06:00', '12:11:00', 'El Salvador Airlines', 1], 
                         ['IR2446', '10:06:00', '22:58:00', 'Iran Airlines', 1], 
                         ['HA8726', '10:06:00', '15:20:00', 'Haiti Airlines', 1], 
                         ['MI3892', '10:06:00', '20:09:00', 'Micronesia Airlines', 1], 
                         ['FR1844', '10:07:00', '21:47:00', 'France Airlines', 1], 
                         ['KI2109', '10:08:00', '2:12:00', 'Kiribati Airlines', 1], 
                         ['SP3612', '10:08:00', '19:03:00', 'Spain Airlines', 1], 
                         ['FI4432', '10:09:00', '11:29:00', 'Fiji Is Airlines', 1], 
                         ['KY3522', '10:09:00', '21:42:00', 'Kyrgyzstan Airlines', 1], 
                         ['FR3107', '10:09:00', '23:30:00', 'France Airlines', 1], 
                         ['HO2781', '10:10:00', '1:06:00', 'Honduras Airlines', 1], 
                         ['IN7951', '10:10:00', '10:57:00', 'India Airlines', 1], 
                         ['UG4340', '10:10:00', '14:45:00', 'Uganda Airlines', 1], 
                         ['VI9496', '10:10:00', '2:45:00', 'Vietnam Airlines', 1], 
                         ['GH4696', '10:11:00', '12:10:00', 'Ghana Airlines', 1], 
                         ['MY8586', '10:11:00', '15:24:00', 'Myanmar Airlines', 1], 
                         ['NE9403', '10:11:00', '14:09:00', 'Nepal Airlines', 1], 
                         ['JE5131', '10:11:00', '4:25:00', 'Jerusalem Airlines', 1], 
                         ['LI7287', '10:11:00', '4:12:00', 'Liberia Airlines', 1], 
                         ['LU7823', '10:11:00', '21:14:00', 'Luxembourg Airlines', 1], 
                         ['TR4045', '10:12:00', '12:50:00', 'Trinidad Airlines', 1], 
                         ['LE1737', '10:12:00', '19:41:00', 'Lebanon Airlines', 1], 
                         ['FA3272', '10:13:00', '20:54:00', 'Falkland Is Airlines', 1],
                         ['AZ1009', '10:13:00', '11:12:00', 'Azerbaijan Airlines', 1], 
                         ['CY1407', '10:13:00', '21:08:00', 'Cyprus Airlines', 1], 
                         ['YU8939', '10:13:00', '23:55:00', 'Yugoslavia Airlines', 1], 
                         ['NO7733', '10:14:00', '4:13:00', 'Northern Mariana Is ', 1], 
                         ['CR5382', '10:14:00', '4:31:00', 'Croatia Airlines', 1], 
                         ['OM2166', '10:14:00', '23:28:00', 'Oman Airlines', 1], 
                         ['SW1352', '10:14:00', '18:34:00', 'Swaziland Airlines', 1], 
                         ['AF1078', '10:15:00', '20:46:00', 'Afghanistan Airlines', 1],
                         ['SL5832', '10:15:00', '14:25:00', 'Slovakia Airlines', 1], 
                         ['CO2518', '10:15:00', '2:05:00', 'Colombia Airlines', 1]],
                        # ---------------------------------------------------------------------
                        # Question 6
                        # ---------------------------------------------------------------------
                        [['FA8332', '0:58:00', '20:08:00', 'Falkland Is Airlines', 0],
                         ['SE2117', '1:03:00', '20:09:00', 'Senegal Airlines', 0], 
                         ['UR2755', '1:21:00', '20:06:00', 'Uruguay Airlines', 0], 
                         ['SR1045', '1:31:00', '20:01:00', 'Sri Lanka Airlines', 0], 
                         ['AR8167', '3:30:00', '20:09:00', 'Argentina Airlines', 0], 
                         ['NO3458', '3:47:00', '20:01:00', 'Northern Mariana Is ', 0], 
                         ['CZ7153', '3:53:00', '20:02:00', 'Czech Airlines', 0], 
                         ['SU1022', '4:12:00', '20:03:00', 'Sudan Airlines', 0], 
                         ['OM2391', '4:27:00', '20:03:00', 'Oman Airlines', 0], 
                         ['CU5194', '4:55:00', '20:10:00', 'Cuba Airlines', 0], 
                         ['PU7766', '5:01:00', '20:03:00', 'Puerto Rico Airlines', 0], 
                         ['ZI4380', '5:28:00', '20:09:00', 'Zimbabwe Airlines', 0], 
                         ['CZ1298', '5:55:00', '20:14:00', 'Czech Airlines', 0], 
                         ['TA1388', '7:03:00', '20:09:00', 'Taiwan Airlines', 0], 
                         ['RE3644', '7:14:00', '20:08:00', 'Reunion Airlines', 0], 
                         ['IN1796', '7:21:00', '20:05:00', 'India Airlines', 0], 
                         ['TH1744', '7:23:00', '20:13:00', 'Thailand Airlines', 0], 
                         ['EQ7736', '7:24:00', '20:14:00', 'Equatorial Guinea Ai', 0], 
                         ['GE9982', '7:27:00', '20:06:00', 'Georgia Airlines', 0], 
                         ['IS8837', '8:17:00', '20:13:00', 'Isla De Pascua Airli', 0], 
                         ['RU1252', '8:22:00', '20:11:00', 'Russia Airlines', 0], 
                         ['SP8138', '9:05:00', '20:08:00', 'Spain Airlines', 0], 
                         ['BH7756', '9:21:00', '20:14:00', 'Bhutan Airlines', 0], 
                         ['LI4160', '10:13:00', '20:02:00', 'Liberia Airlines', 0], 
                         ['HO1609', '10:27:00', '20:09:00', 'Honduras Airlines', 0], 
                         ['VI8019', '10:46:00', '20:08:00', 'Vietnam Airlines', 0], 
                         ['BA4101', '10:54:00', '20:08:00', 'Bahamas Airlines', 0], 
                         ['SI5464', '11:26:00', '20:06:00', 'Sierra Leone Airline', 0], 
                         ['SR9097', '11:39:00', '20:06:00', 'Sri Lanka Airlines', 0], 
                         ['WE9274', '11:39:00', '20:09:00', 'Western Samoa Airlin', 0], 
                         ['DJ8420', '12:19:00', '20:14:00', 'Djibouti Airlines', 0], 
                         ['CU2063', '12:40:00', '20:06:00', 'Cuba Airlines', 0], 
                         ['LI3003', '13:03:00', '20:10:00', 'Liberia Airlines', 0], 
                         ['RU3168', '13:16:00', '20:02:00', 'Russia Airlines', 0], 
                         ['NO1349', '14:03:00', '20:11:00', 'Northern Mariana Is ', 0], 
                         ['ET6479', '14:49:00', '20:13:00', 'Ethiopia Airlines', 0], 
                         ['DJ1651', '15:28:00', '20:02:00', 'Djibouti Airlines', 0], 
                         ['SY2783', '15:57:00', '20:12:00', 'Syria Airlines', 0], 
                         ['TO5049', '16:05:00', '20:14:00', 'Togo Airlines', 0], 
                         ['AZ1856', '17:09:00', '20:11:00', 'Azerbaijan Airlines', 0], 
                         ['WE7788', '17:17:00', '20:12:00', 'Western Samoa Airlin', 0], 
                         ['YU1921', '17:18:00', '20:10:00', 'Yugoslavia Airlines', 0], 
                         ['KO9219', '17:29:00', '20:04:00', 'Korea Airlines', 0], 
                         ['AZ5851', '17:33:00', '20:07:00', 'Azerbaijan Airlines', 0], 
                         ['PE1857', '17:37:00', '20:01:00', 'Peru Airlines', 0], 
                         ['SL9463', '18:21:00', '20:12:00', 'Slovakia Airlines', 0], 
                         ['TO6072', '18:43:00', '20:01:00', 'Togo Airlines', 0], 
                         ['UG5477', '22:36:00', '20:02:00', 'Uganda Airlines', 0], 
                         ['YE8510', '23:39:00', '20:09:00', 'Yemen Airlines', 0]],
                        # ---------------------------------------------------------------------
                        # Question 7
                        # ---------------------------------------------------------------------
                        [['HO7035', '15:02:00', '18:34:00', 'Honduras Airlines', 1, 0], #7
                         ['DO3636', '15:10:00', '18:42:00', 'Dominica Airlines', 1, 1], 
                         ['SE9865', '15:15:00', '18:11:00', 'Senegal Airlines', 0, 1], 
                         ['GE3128', '15:18:00', '18:32:00', 'Georgia Airlines', 0, 1], 
                         ['GI1994', '15:21:00', '18:39:00', 'Gibraltar Airlines', 1, 0], 
                         ['EC5799', '15:22:00', '18:45:00', 'Ecuador Airlines', 1, 0], 
                         ['PU6775', '15:22:00', '18:06:00', 'Puerto Rico Airlines', 1, 1], 
                         ['FI9015', '15:25:00', '18:30:00', 'Fiji Is Airlines', 1, 0], 
                         ['SU7567', '15:29:00', '18:47:00', 'Sudan Airlines', 1, 0], 
                         ['KE7024', '15:42:00', '18:06:00', 'Kenya Airlines', 0, 1], 
                         ['SP3786', '15:50:00', '18:42:00', 'Spain Airlines', 1, 1], 
                         ['TR3884', '15:51:00', '18:06:00', 'Trinidad Airlines', 1, 1]]]

alias_counter = 0
total_aliases = 24
total_queries = 7

# open the test folder and read the files inside
if os_name == 'Windows':
    print("Windows OS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '\\tempgrades'
    answer = open(f"{directory}\\week07answers.txt", "w")

elif os_name == 'Linux':
    print("Linux Detected")
    directory = '/home/student/Desktop/itm220grading'
    grading_directory = '/home/student/Desktop/itm220grading/tempgrades'
    answer = open(f"{directory}/week07answers.txt", "w")

elif os_name == 'Darwin':
    print("MacOS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '/tempgrades'
    answer = open(f"{directory}/week07answers.txt", "w")
# if directory doesn't exist, write no files to grade
if not os.path.exists(grading_directory):
    print("No Directory\n")
    os.makedirs(grading_directory)
    print("Directory Created\n")

# if the directory is empty, write no files to grade
if not os.listdir(grading_directory):
    
    print("No Files to Grade\n")

# loop through the files in the directory
else:

    print("Grading in progress...")
    
    file_count = 0

    for filename in os.listdir(grading_directory):

        file_count += 1 # increment the counter
        edit_file = open(f"{grading_directory}/{filename}", "r+")
        file_contents = edit_file.read()
        # Make changes to file_contents as needed
        if not file_contents.__contains__('-- ~'):
            print("Formatting File...")
            file_contents = file_contents.replace("USE", "-- ~\nUSE")
            file_contents = file_contents.replace("SELECT", "-- ~\nSELECT")
            file_contents = file_contents.replace("(-- ~\nSELECT", "(SELECT")
            file_contents = file_contents.replace(";", ";\n-- ~")
            edit_file.seek(0)
            edit_file.write(file_contents)
            edit_file.truncate()
            edit_file.close()
        else:
            edit_file.close()
            print("File already formatted")

        f = open(f"{grading_directory}/{filename}", "r")
        print(f"Grading {filename}...")
        answer.write("***********************************\n")
        answer.write(f"File: {filename}\n")
        # print("---------------------")

        sqlFile = f.read()
        sqlCommands = sqlFile.split('-- ~')
        # strip the \n from the commands
        sqlCommands = [command.strip() for command in sqlCommands]
                # Filter out SELECT and USE commands
        sqlCommands = [command for command in sqlCommands if (not command.lower().startswith('select *') and command.lower().startswith('select')) or command.lower().startswith('use')]
        use_airportdb_count = 0
        for command in sqlCommands:
            if command.lower().startswith('use airportdb'):
                use_airportdb_count += 1
        if use_airportdb_count > 1:
            answer.write(f"USE airportdb; command used {use_airportdb_count} times. Only use it once\n")
            answer.write("Skipping to the next file...\n")
            answer.write("***********************************\n\n")
            continue
        
        # debug.write(f"COMMAND LIST: {sqlCommands}")
        # filter out SELECT @ and SELECT @@ commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('select @') and not command.lower().startswith('select @@')]

        #filter out SET commands
        sqlCommands = [command for command in sqlCommands if not command.lower().startswith('set')]
    
        correct_answer_count = 0
        number = 0
        a_number = 0
        join_counter = 0
        query1_clause_list = []
        query2_clause_list = []
        query3_clause_list = []
        query4_clause_list = []
        query5_clause_list = []
        query6_clause_list = []
        query7_clause_list = []
        query8_clause_list = []
        
        for command in sqlCommands:
            a_number += 1
            
            # debug.write(f"Query {a_number}. {command}\n")            
            if a_number == 1 and not command.lower().__contains__('use'):
                answer.write(f"USE airportdb; Statement NOT FOUND\n")


            if a_number == 2: # Query 1
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 1 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__('distinct'):
                        query1_clause_list.append(f"DISTINCT Clause NOT used")
                    if not command.lower().__contains__('from'):
                        query1_clause_list.append(f"FROM Clause NOT used")                    
                    if not command.lower().__contains__('order by'):
                        query1_clause_list.append(f"ORDER BY Clause NOT used")

            if a_number == 3: # Query 2
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 2 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__('from'):
                        query2_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('inner join'):
                        query1_clause_list.append(f"INNER JOIN Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query2_clause_list.append(f"ORDER BY Clause NOT used")
                    

            if a_number == 4: # Query 3
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 2 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__('from'):
                        query3_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('inner join'):
                        query3_clause_list.append(f"INNER JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query3_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('limit'):
                        query3_clause_list.append(f"LIMIT Clause NOT used")

            if a_number == 5: # Query 4
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 3 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__('from'):
                        query4_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query4_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('limit'):
                        query4_clause_list.append(f"LIMIT Clause NOT used")
                    
            if a_number == 6: # Query 5
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 5 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__('from'):
                        query5_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('inner join'):
                        query5_clause_list.append(f"INNER JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query5_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('between'):
                        query5_clause_list.append(f"BETWEEN Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query5_clause_list.append(f"ORDER BY Clause NOT used")

            if a_number == 7: # Query 6
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 5 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query6_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query6_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('inner join'):
                        query6_clause_list.append(f"INNER JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query6_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('between'):
                        query6_clause_list.append(f"BETWEEN Clause NOT used")
                    if not command.lower().__contains__('and not'):
                        query6_clause_list.append(f"AND NOT operator NOT used")
                    if not command.lower().__contains__('order by'):
                        query6_clause_list.append(f"ORDER BY Clause NOT used")
                    
            between_counter = 0
            and_counter = 0
            or_counter = 0
            if a_number == 8: # Query 7
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 6 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__(' as '):
                        query7_clause_list.append(f"Alias NOT used")
                    if not command.lower().__contains__('from'):
                        query7_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('inner join'):
                        query7_clause_list.append(f"INNER JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query7_clause_list.append(f"WHERE Clause NOT used")
                    # count the number of BETWEEN clauses used (there should be 2 in this query)
                    # count the number of AND operators used (there should be 5 in this query)
                    # count the number of OR operators used (there should be 1 in this query)
                    if command.lower().__contains__('between'):
                        for word in command.split():
                            if word.lower() == 'between':
                                between_counter += 1
                        if between_counter != 2:
                            query7_clause_list.append(f"More than 2 BETWEEN Clauses used")
                        query7_clause_list.append(f"BETWEEN Clause used {between_counter} times")
                    if command.lower().__contains__('and'):
                        for word in command.split():
                            if word.lower() == 'and':
                                and_counter += 1
                        if and_counter != 5:
                            query7_clause_list.append(f"More than 5 AND operators used")
                        query7_clause_list.append(f"AND operator used {and_counter} times")
                    if command.lower().__contains__('or'):
                        for word in command.split():
                            if word.lower() == 'or':
                                or_counter += 1
                        if or_counter != 1:
                            query7_clause_list.append(f"More than 1 OR operator used")
                        query7_clause_list.append(f"OR operator used {or_counter} times")
                    if not command.lower().__contains__('between'):
                        query7_clause_list.append(f"BETWEEN Clause NOT used")
                    if not command.lower().__contains__('and not'):
                        query7_clause_list.append(f"AND NOT operator NOT used")
                    if not command.lower().__contains__('or'):
                        query7_clause_list.append(f"OR operator NOT used")
                    if not command.lower().__contains__('order by'):
                        query7_clause_list.append(f"ORDER BY Clause NOT used")


            # pass each list to a function
            # the function will do all the replacing and formatting
            # then return the list
            
            new_query1c_list = format_list(query1_clause_list)
            new_query2c_list = format_list(query2_clause_list)
            new_query3c_list = format_list(query3_clause_list)
            new_query4c_list = format_list(query4_clause_list)
            new_query5c_list = format_list(query5_clause_list)
            new_query6c_list = format_list(query6_clause_list)
            new_query7c_list = format_list(query7_clause_list)
            new_query8c_list = format_list(query8_clause_list)

            output = ''

            try:
                mycursor.execute(command)
            except mysql.connector.Error as e:
                # number the queries run and print the error
                answer.write("Error found. Skipping to the next file...\n")
                answer.write("-------ERROR DETAILS-------\n")
                answer.write(f"Query {number + 1}. Error: {e}\n")
                
                answer.write("------QUERY------\n")
                answer.write(f"{command}\n")
                answer.write("---------------------\n")
                
                break
            if a_number != 1:
                output = mycursor.fetchall()
                # print(f"{a_number}. {number + 1} retrieved\n")
            # if the commans was a SELECT statement, and it didn't return
            # any results, print that no results were returned in the output list
            if len(output) == 0 and command.lower().__contains__('select'):
                answer.write(f"Query {number + 1}. No results returned\n")
                number += 1
                continue
            
                        

            
            output_list = [list(row) for row in output if row is not None]
            

            # change all decimal values to strings
            for row in output_list:
                for i in range(len(row)):
                    if type(row[i]) == decimal.Decimal:
                        row[i] = str(row[i])

            # convert all datetime objects to dates
            for row in output_list:
                for i in range(len(row)):
                    if type(row[i]) == datetime.date:
                        row[i] = row[i].strftime('%Y-%m-%d')
                    if type(row[i]) == datetime.datetime:
                        row[i] = row[i].strftime('%Y-%m-%d %H:%M:%S')

            # convert all timedelta objects to dates
            for row in output_list:
                for i in range(len(row)):
                    if type(row[i]) == datetime.timedelta:
                        row[i] = str(row[i])
            
            # filter out empty commands
            # only output the result if information is returned
            if len(output_list) > 0:
                student_answers = [list(row) for row in output_list if row is not None]
                

                # Compare the student answers to the correct answers
                if (student_answers in correct_answer_list or student_answers in correct_answer_list[number]):
                    number += 1
                    correct_answer_count += 1
                
                else:
                    number += 1

                    answer.write("---------------------\n")
                    answer.write(f"{number}. Incorrect!\n")
                    # 1, 5, 8 are the USE statments
                    # check for certain clauses and print that they were used
                    answer.write("------QUERY------\n")
                    answer.write(f"{command}\n")
                    answer.write("-----CLAUSES-----\n")
                    if a_number == 2:
                        # debug.write(new_query1_list)
                        if len(new_query1c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query1c_list}\n")
                    elif a_number == 3:
                        # debug.write(new_query2_list)
                        if len(new_query2c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query2c_list}\n")
                    elif a_number == 4:
                        # debug.write(new_query3_list)
                        if len(new_query3c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query3c_list}\n")
                    elif a_number == 5:
                        # debug.write(new_query4_list)
                        if len(new_query4c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query4c_list}\n")
                    elif a_number == 6:
                        # debug.write(new_query5_list)
                        if len(new_query5c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query5c_list}\n")
                    elif a_number == 7:
                        # debug.write(new_query6_list)
                        if len(new_query6c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query6c_list}\n")
                    elif a_number == 8:
                        # debug.write(new_query7_list)
                        if len(new_query7c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query7c_list}\n")
                    elif a_number == 9:
                        # debug.write(new_query7_list)
                        if len(new_query8c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query8c_list}\n")

                    answer.write("----FUNCTIONS----\n")
                    if a_number == 2:
                        # debug.write(new_query1_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 3:
                        # debug.write(new_query2_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 4:
                        # debug.write(new_query3_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 5:
                        # debug.write(new_query4_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 6:
                        # debug.write(new_query5_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 7:
                        # debug.write(new_query6_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 8:
                        # debug.write(new_query7f_list)
                        answer.write(f"No functions Needed\n")
                    if a_number == 9:
                        # debug.write(new_query7_list)
                        answer.write(f"No functions Needed\n")
                    answer.write("-----ANSWERS-----\n")
                    
                    answer.write(f"Student Answer: {student_answers}\n")
                    answer.write(f"Correct Answer: {correct_answer_list[number-1]}\n")
                    answer.write("---------------------\n")
        answer.write("--------RESULTS-------\n") 
        answer.write(f"{alias_counter}/{total_aliases} Alias Used\n")
        answer.write(f"{number}/{total_queries} Queries Written\n")
        answer.write(f"{correct_answer_count}/{total_queries} Queries Correct\n")
        
        alias_counter = 0
        answer.write("***********************************\n\n")
    answer.write("***********************************\n")
    answer.write(f"Total Files Graded: {file_count}\n")
    answer.write("***********************************\n")

    print("Grading Complete")

    answer.close()
    # ask if user wants to delete files in the tempgrades folder
    # if yes, delete the files

    # if no, keep the files
    f.close()
    mydb.close()
    delete_files = input("Would you like to delete the files in the tempgrades folder? (yes/no): ")
    if delete_files.lower() == "yes":
        f.close()
        for filename in os.listdir(grading_directory):
            os.remove(f"{grading_directory}/{filename}")
        if os_name == 'Windows':
            os.remove(f"{directory}\\week07answers.txt")
        elif os_name == 'Linux' or os_name == 'Darwin':
            os.remove(f"{directory}/week07answers.txt")
        print("Files Deleted")
    else:
        f.close()
        print("Files Kept")

