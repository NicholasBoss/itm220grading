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
try:
    from sshtunnel import SSHTunnelForwarder
except ImportError or ModuleNotFoundError:
    print("SSHTunnel module not found. Installing...")
    if os_name == 'Windows':
        os.system("pip install sshtunnel")
    elif os_name == 'Linux' or os_name == 'Darwin':
        os.system("pip3 install sshtunnel")
    from sshtunnel import SSHTunnelForwarder
    print("SSHTunnel module installed")
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
# SSH Connection Details
SSH_HOST = "157.201.16.128"
SSH_PORT = 22
SSH_USER = "student"
SSH_PASSWORD = "ITM220stud3nt!"  # Or use ssh_pkey="path/to/private/key.pem"

# MySQL Connection Details
MYSQL_USER = "student"
MYSQL_PASSWORD = "ITM220stud3nt!"
MYSQL_DB = "airportdb"
with SSHTunnelForwarder(
        (SSH_HOST, SSH_PORT),
        ssh_username=SSH_USER,
        ssh_password=SSH_PASSWORD,  # Use ssh_pkey if you're using an SSH key
        remote_bind_address=("127.0.0.1", 3306),  # Forward remote MySQL
        local_bind_address=('127.0.0.1', 3307),  # Ensure the port is available on localhost
    ) as tunnel:
        print(f"✅ SSH Tunnel established! Local port: {tunnel.local_bind_port}")

        print("Attempting to connect to MySQL...")
        # Connect to MySQL via SSH Tunnel
        
        mydb = mysql.connector.connect(
            host="127.0.0.1",  # Localhost because of SSH tunnel
            port=tunnel.local_bind_port,  # Dynamically assigned local port
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        #For local testing
        # mydb = mysql.connector.connect(
        #     host="localhost",
        #     user="student",
        #     password="student",
        # )
        print("✅ Successfully connected to MySQL!")

        # Create a cursor
        mycursor = mydb.cursor()


        correct_answer_list = [ # ---------------------------------------------------------------------
                                # Question 1
                                # ---------------------------------------------------------------------
                                [['AL9073', 'LAUPHEIM, GERMANY', 'PENEDO, BRAZIL', 'Jun 01, 2015 07:56 AM', 'Jun 01, 2015 06:40 PM']],
                                # ---------------------------------------------------------------------
                                # Question 2
                                # ---------------------------------------------------------------------
                                [['AL9073', 'LAUPHEIM, GERMANY', 'PENEDO, BRAZIL', 50, 25, '25 seats left', 50, 'Flight Full']],
                                # ---------------------------------------------------------------------
                                # Question 3
                                # ---------------------------------------------------------------------
                                [['295', '288', '296', '278', '295', '291', '265', '2008']],
                                # ---------------------------------------------------------------------
                                # Question 4
                                # ---------------------------------------------------------------------
                                [['KI2173', 'DETROIT, UNITED STATES', 'SANTA MONICA, UNITED STATES', 'High Activity', 13787],
                                ['SE9793', 'WILLOWS, UNITED STATES', 'TRENTON, UNITED STATES', 'High Activity', 13681],
                                ['HU1379', 'MILLEDGEVILLE, UNITED STATES', 'NORTH EAST, UNITED STATES', 'High Activity', 12812],
                                ['HA4967', 'JACKSON, UNITED STATES', 'PHILADELPHIA, UNITED STATES', 'High Activity', 12742],
                                ['PO1627', 'MUSKOGEE, UNITED STATES', 'BURLINGTON, UNITED STATES', 'High Activity', 12585],
                                ['SE2863', 'TRAVERSE CITY, UNITED STATES', 'STAUNTON-WAYNESBORO-HARRISONB*, UNITED STATES', 'High Activity', 12486],
                                ['MA1915', 'BLACKSTONE, UNITED STATES', 'ORANGE CITY, UNITED STATES', 'High Activity', 12294],
                                ['YU9000', 'MERRILL, UNITED STATES', 'WESTERLY, UNITED STATES', 'High Activity', 12016],
                                ['YU7366', 'FLORA, UNITED STATES', 'MOLINE, UNITED STATES', 'High Activity', 11879],
                                ['FA2773', 'CHOTEAU, UNITED STATES', 'ROUNDUP, UNITED STATES', 'High Activity', 11850],
                                ['YU6410', 'MENOMINEE, UNITED STATES', 'INDIANOLA, UNITED STATES', 'High Activity', 11702],
                                ['VA8541', 'MARYSVILLE, UNITED STATES', 'TAMPA, UNITED STATES', 'High Activity', 11395],
                                ['ER8710', 'WARREN, UNITED STATES', 'WARROAD, UNITED STATES', 'High Activity', 11039],
                                ['FA2056', 'VINCENNES, UNITED STATES', 'JACKSON, UNITED STATES', 'High Activity', 10773],
                                ['PO1509', 'UTICA, UNITED STATES', 'IDAHO FALLS, UNITED STATES', 'High Activity', 10740],
                                ['YU5775', 'CHARLOTTE, UNITED STATES', 'ANIAK, UNITED STATES', 'High Activity', 10691],
                                ['CZ8966', 'CORONA, UNITED STATES', 'MANNING, UNITED STATES', 'High Activity', 10582],
                                ['ET5618', 'FALLON, UNITED STATES', 'DAYTONA BEACH, UNITED STATES', 'High Activity', 10563],
                                ['HU4662', 'EASTMAN, UNITED STATES', 'CAMP RIPLEY, UNITED STATES', 'High Activity', 10549],
                                ['LU5617', 'CHAPPELL, UNITED STATES', 'WEST PLAINS, UNITED STATES', 'High Activity', 10537],
                                ['MI2776', 'MOBILE, UNITED STATES', 'RED WING, UNITED STATES', 'High Activity', 10423],
                                ['YU4735', "ST MARY'S, UNITED STATES", 'HARRISBURG, UNITED STATES', 'High Activity', 10038],
                                ['NI3099', 'CAMP RIPLEY, UNITED STATES', 'SALT LAKE CITY, UNITED STATES', 'Medium Activity', 9907],
                                ['ME9662', 'DE QUEEN, UNITED STATES', 'JASPER, UNITED STATES', 'Medium Activity', 9880],
                                ['OM9293', 'MONROEVILLE, UNITED STATES', 'CAMBRIDGE, UNITED STATES', 'Medium Activity', 9828],
                                ['YU5941', 'CELINA, UNITED STATES', 'CHARLEVOIX, UNITED STATES', 'Medium Activity', 9819],
                                ['DE7084', 'GREENVILLE, UNITED STATES', 'DEMING, UNITED STATES', 'Medium Activity', 9735],
                                ['MI9290', 'DAYTON, UNITED STATES', 'FRIDAY HARBOR, UNITED STATES', 'Medium Activity', 9708],
                                ['JA2267', 'MESA, UNITED STATES', 'MANISTIQUE, UNITED STATES', 'Medium Activity', 9666],
                                ['OM2569', 'BELUGA, UNITED STATES', 'FESTUS, UNITED STATES', 'Medium Activity', 9636],
                                ['PE1747', 'REED CITY, UNITED STATES', 'CAMBRIDGE, UNITED STATES', 'Medium Activity', 9608],
                                ['UK2667', 'CRESCO, UNITED STATES', 'LA JUNTA, UNITED STATES', 'Medium Activity', 9498],
                                ['AN2405', 'CELINA, UNITED STATES', 'TUCSON, UNITED STATES', 'Medium Activity', 9489],
                                ['LA9078', 'NAPA, UNITED STATES', 'CHARITON, UNITED STATES', 'Medium Activity', 9487],
                                ['TO2549', 'GLENWOOD, UNITED STATES', 'DUGWAY PROVING GROUND, UNITED STATES', 'Medium Activity', 9459],
                                ['GI1545', 'MERIDIAN, UNITED STATES', 'ANGOLA, UNITED STATES', 'Medium Activity', 9415],
                                ['FI4432', 'MARYSVILLE, UNITED STATES', 'MOSES LAKE, UNITED STATES', 'Medium Activity', 9376],
                                ['CH1176', 'CAPE GIRARDEAU, UNITED STATES', 'DELAWARE, UNITED STATES', 'Medium Activity', 9348],
                                ['MI8878', 'CAMPBELLSVILLE, UNITED STATES', 'ESCANABA, UNITED STATES', 'Medium Activity', 9343],
                                ['YE1968', 'PROVINCETOWN, UNITED STATES', 'PASO ROBLES, UNITED STATES', 'Medium Activity', 9258],
                                ['PE7892', 'ERWIN, UNITED STATES', 'GREAT BARRINGTON, UNITED STATES', 'Medium Activity', 9182],
                                ['BA3076', 'ROXBORO, UNITED STATES', 'LAMAR, UNITED STATES', 'Medium Activity', 9169],
                                ['MI3896', 'OWATONNA, UNITED STATES', 'LAKEHURST, UNITED STATES', 'Medium Activity', 9151],
                                ['ET1300', 'LEMMON, UNITED STATES', 'POMPANO BEACH, UNITED STATES', 'Medium Activity', 9009],
                                ['BA4118', 'NEW YORK, UNITED STATES', 'HAMMOND, UNITED STATES', 'Medium Activity', 9005],
                                ['BE6699', 'BATESVILLE, UNITED STATES', 'OCALA, UNITED STATES', 'Medium Activity', 8994],
                                ['CZ1716', 'THOMASTON, UNITED STATES', 'ROCKDALE, UNITED STATES', 'Medium Activity', 8945],
                                ['SE2030', 'SIOUX CENTER, UNITED STATES', 'MINNEAPOLIS, UNITED STATES', 'Medium Activity', 8914],
                                ['KO9219', 'PITTSBURGH, UNITED STATES', 'KEY WEST, UNITED STATES', 'Medium Activity', 8907],
                                ['LA7059', 'GARY, UNITED STATES', 'MINDEN, UNITED STATES', 'Medium Activity', 8889],
                                ['JE5614', 'PONTIAC, UNITED STATES', 'DAVENPORT, UNITED STATES', 'Medium Activity', 8878],
                                ['OM5436', 'WASHINGTON, UNITED STATES', 'PHILADELPHIA, UNITED STATES', 'Medium Activity', 8850],
                                ['LI8159', 'NECEDAH, UNITED STATES', 'SPOKANE, UNITED STATES', 'Medium Activity', 8849],
                                ['MI8337', 'ELKIN, UNITED STATES', 'CHEHALIS, UNITED STATES', 'Medium Activity', 8834],
                                ['WA4076', 'KENOSHA, UNITED STATES', 'WICHITA, UNITED STATES', 'Medium Activity', 8783],
                                ['IR7835', 'DECORAH, UNITED STATES', 'MT POCONO, UNITED STATES', 'Medium Activity', 8768],
                                ['GR4548', 'VENICE, UNITED STATES', 'GREAT BEND, UNITED STATES', 'Medium Activity', 8764],
                                ['DE4317', 'WINTER HAVEN, UNITED STATES', 'HERMISTON, UNITED STATES', 'Medium Activity', 8745],
                                ['CZ7237', 'REDWOOD FALLS, UNITED STATES', 'CHEFORNAK, UNITED STATES', 'Medium Activity', 8739],
                                ['AZ1358', 'PARIS, UNITED STATES', 'ALAMOGORDO, UNITED STATES', 'Medium Activity', 8710],
                                ['PU2662', 'BISHOP, UNITED STATES', 'ANDREWS, UNITED STATES', 'Medium Activity', 8587],
                                ['RO8923', 'ALGONA, UNITED STATES', 'RUGBY, UNITED STATES', 'Medium Activity', 8572],
                                ['WA6519', 'BIRMINGHAM, UNITED STATES', 'WADENA, UNITED STATES', 'Medium Activity', 8545],
                                ['IC9093', 'FT WORTH, UNITED STATES', 'TUSCALOOSA, UNITED STATES', 'Medium Activity', 8509],
                                ['FA6442', 'MONTICELLO, UNITED STATES', 'OLYMPIA, UNITED STATES', 'Medium Activity', 8481],
                                ['WE8883', 'SAN DIEGO, UNITED STATES', 'ATHENS, UNITED STATES', 'Medium Activity', 8467],
                                ['PE9943', 'EMPORIA, UNITED STATES', 'SYLVANIA, UNITED STATES', 'Medium Activity', 8448],
                                ['IR1736', 'ANDREWS, UNITED STATES', 'AKRON, UNITED STATES', 'Medium Activity', 8443],
                                ['TU7887', 'ROCHESTER, UNITED STATES', 'NANTUCKET, UNITED STATES', 'Medium Activity', 8421],
                                ['BU1446', 'MARSHFIELD, UNITED STATES', 'SIKESTON, UNITED STATES', 'Medium Activity', 8420],
                                ['PU1065', 'COLUMBUS, UNITED STATES', 'OCONTO, UNITED STATES', 'Medium Activity', 8399],
                                ['MO6027', 'WICHITA, UNITED STATES', 'WALLA WALLA, UNITED STATES', 'Medium Activity', 8383],
                                ['KE2605', 'EASTLAND, UNITED STATES', 'DUBUQUE, UNITED STATES', 'Medium Activity', 8380],
                                ['IS3636', 'PENSACOLA, UNITED STATES', 'DE KALB, UNITED STATES', 'Medium Activity', 8314],
                                ['JE1595', 'AIKEN, UNITED STATES', 'GUYMON, UNITED STATES', 'Medium Activity', 8307],
                                ['AU4085', 'CUMMING, UNITED STATES', 'HOQUIAM, UNITED STATES', 'Medium Activity', 8304],
                                ['EG8566', 'EL DORADO, UNITED STATES', 'OTTUMWA, UNITED STATES', 'Medium Activity', 8266],
                                ['CA6407', 'FT STEWART, UNITED STATES', 'EMPORIA, UNITED STATES', 'Medium Activity', 8238],
                                ['YU3645', 'CLEARFIELD, UNITED STATES', 'POTEAU, UNITED STATES', 'Medium Activity', 8232],
                                ['YU5789', 'FT BRIDGER, UNITED STATES', 'COCOA BEACH, UNITED STATES', 'Medium Activity', 8219],
                                ['LU2246', 'SHELBYVILLE, UNITED STATES', 'CHATTANOOGA, UNITED STATES', 'Medium Activity', 8207],
                                ['SU1676', 'DAVENPORT, UNITED STATES', 'COLORADO CITY, UNITED STATES', 'Medium Activity', 8194],
                                ['AU6385', 'APPLE VALLEY, UNITED STATES', 'WACO, UNITED STATES', 'Medium Activity', 8131],
                                ['SA1082', 'DECATUR, UNITED STATES', 'STANTON, UNITED STATES', 'Medium Activity', 8131],
                                ['CH1136', 'DILLON, UNITED STATES', 'WAVERLY, UNITED STATES', 'Medium Activity', 8089],
                                ['SA1559', 'WALLA WALLA, UNITED STATES', 'PHOENIX, UNITED STATES', 'Medium Activity', 8077],
                                ['CO8648', 'PITTSBURG, UNITED STATES', 'BANNING, UNITED STATES', 'Medium Activity', 8074],
                                ['TA6155', 'FLORA, UNITED STATES', 'SANTA ANA, UNITED STATES', 'Medium Activity', 8055],
                                ['ET6479', 'MARYSVILLE, UNITED STATES', 'KAKE, UNITED STATES', 'Medium Activity', 8036],
                                ['GR7164', 'HAWTHORNE, UNITED STATES', 'HUTCHINSON, UNITED STATES', 'Medium Activity', 8016],
                                ['AR1842', 'SIREN, UNITED STATES', 'SALEM, UNITED STATES', 'Medium Activity', 8009],
                                ['CH2955', 'MIDDLETON I, UNITED STATES', 'OAKLAND, UNITED STATES', 'Medium Activity', 7977],
                                ['TA8728', 'OXFORD, UNITED STATES', 'CINCINNATI, UNITED STATES', 'Medium Activity', 7932],
                                ['CZ2670', 'MAPLE LAKE, UNITED STATES', 'CHICAGO, UNITED STATES', 'Medium Activity', 7895],
                                ['AN2706', 'CLEVELAND, UNITED STATES', 'HEBBRONVILLE, UNITED STATES', 'Medium Activity', 7864],
                                ['VE9785', 'PULLMAN/ MOSCOW, UNITED STATES', 'OKLAHOMA CITY, UNITED STATES', 'Medium Activity', 7863],
                                ['OM3770', 'PETERSBURG, UNITED STATES', 'WHITEVILLE, UNITED STATES', 'Medium Activity', 7856],
                                ['ST1861', 'CORNELIA, UNITED STATES', 'ROSEAU, UNITED STATES', 'Medium Activity', 7853],
                                ['EL2581', 'CHARLESTON, UNITED STATES', 'ERIE, UNITED STATES', 'Medium Activity', 7829],
                                ['KA5277', 'SIOUX FALLS, UNITED STATES', 'OCONTO, UNITED STATES', 'Medium Activity', 7821],
                                ['BA4153', 'ENDICOTT, UNITED STATES', 'WILLIMANTIC, UNITED STATES', 'Medium Activity', 7793],
                                ['NO7935', 'NAPA, UNITED STATES', 'ST LOUIS, UNITED STATES', 'Medium Activity', 7762],
                                ['LA7187', 'ROCHESTER, UNITED STATES', 'CINCINNATI, UNITED STATES', 'Medium Activity', 7754],
                                ['SW6072', 'KOTZEBUE, UNITED STATES', 'PARSONS, UNITED STATES', 'Medium Activity', 7737],
                                ['EG7409', 'SAGINAW, UNITED STATES', 'WAYNE, UNITED STATES', 'Medium Activity', 7697],
                                ['UZ1338', 'MORRILTON, UNITED STATES', 'RANTOUL, UNITED STATES', 'Medium Activity', 7657],
                                ['MY8586', 'SHEEP MOUNTAIN, UNITED STATES', 'BEATRICE, UNITED STATES', 'Medium Activity', 7622],
                                ['IC1681', 'PENSACOLA, UNITED STATES', 'LOMPOC, UNITED STATES', 'Medium Activity', 7619],
                                ['MY1066', 'NENANA, UNITED STATES', 'DANVILLE, UNITED STATES', 'Medium Activity', 7616],
                                ['SP5709', 'ALAMOGORDO, UNITED STATES', 'NOVATO, UNITED STATES', 'Medium Activity', 7602],
                                ['CY2880', 'ALABASTER, UNITED STATES', 'MARSHALLTOWN, UNITED STATES', 'Medium Activity', 7570],
                                ['BH8009', 'TOLEDO, UNITED STATES', 'MOLOKAI, HAWAII, UNITED STATES', 'Medium Activity', 7569],
                                ['UK4877', 'HUNTSVILLE, UNITED STATES', 'MACON, UNITED STATES', 'Medium Activity', 7564],
                                ['SU1328', 'BATTLE MOUNTAIN, UNITED STATES', 'ALEXANDER CITY, UNITED STATES', 'Medium Activity', 7529],
                                ['CZ2050', 'LAS VEGAS, UNITED STATES', 'FRANKLIN, UNITED STATES', 'Medium Activity', 7519],
                                ['EG7584', 'BROKEN BOW, UNITED STATES', 'HOPKINSVILLE, UNITED STATES', 'Medium Activity', 7510],
                                ['RW1474', 'FARMINGDALE, UNITED STATES', 'DOUGLAS BISBEE, UNITED STATES', 'Medium Activity', 7496],
                                ['AU4409', 'LYONS, UNITED STATES', 'READING, UNITED STATES', 'Medium Activity', 7490],
                                ['HO7035', 'RUSSELL, UNITED STATES', 'NORWOOD, UNITED STATES', 'Medium Activity', 7488],
                                ['SU8712', 'WASKISH, UNITED STATES', 'RIVERTON, UNITED STATES', 'Medium Activity', 7456],
                                ['EL6868', 'ROCHESTER, UNITED STATES', 'LEXINGTON, UNITED STATES', 'Medium Activity', 7454],
                                ['AF5675', 'RALEIGH/ DURHAM, UNITED STATES', 'ROCKPORT, UNITED STATES', 'Medium Activity', 7445],
                                ['KI8766', 'FT RUCKER, UNITED STATES', 'CRYSTAL RIVER, UNITED STATES', 'Medium Activity', 7445],
                                ['CZ9540', 'SANDERSVILLE, UNITED STATES', 'UPLAND, UNITED STATES', 'Medium Activity', 7421],
                                ['DA9563', 'LE MARS, UNITED STATES', 'BATAVIA, UNITED STATES', 'Medium Activity', 7418],
                                ['OM1698', 'FERGUS FALLS, UNITED STATES', 'SHERIDAN, UNITED STATES', 'Medium Activity', 7409],
                                ['TH4435', 'SUSSEX, UNITED STATES', 'OLIVIA, UNITED STATES', 'Medium Activity', 7389],
                                ['UN1107', 'FITCHBURG, UNITED STATES', 'ATLANTA, UNITED STATES', 'Medium Activity', 7382],
                                ['AM9379', 'LEMMON, UNITED STATES', 'GRUNDY, UNITED STATES', 'Medium Activity', 7364],
                                ['SW4247', 'EASTPORT, UNITED STATES', 'NEW PHILADELPHIA, UNITED STATES', 'Medium Activity', 7360],
                                ['KE8199', 'PORT HEIDEN, UNITED STATES', 'MELBOURNE, UNITED STATES', 'Medium Activity', 7351],
                                ['RU4766', 'FRANKLIN, UNITED STATES', 'DELTA, UNITED STATES', 'Medium Activity', 7350],
                                ['DJ8160', 'ALTUS, UNITED STATES', 'WEST BEND, UNITED STATES', 'Medium Activity', 7344],
                                ['CE1110', 'FAIRFIELD, UNITED STATES', 'OLNEY, UNITED STATES', 'Medium Activity', 7315],
                                ['GR8934', 'RIDGELY, UNITED STATES', 'SIERRA ARMY DEPOT, UNITED STATES', 'Medium Activity', 7302],
                                ['WE4320', 'MARTINSBURG, UNITED STATES', 'SARASOTA/ BRADENTON, UNITED STATES', 'Medium Activity', 7293],
                                ['CR6390', 'BRIGHAM CITY, UNITED STATES', 'HETTINGER, UNITED STATES', 'Medium Activity', 7290],
                                ['AR8197', 'APPLETON, UNITED STATES', 'FT LAUDERDALE, UNITED STATES', 'Medium Activity', 7268],
                                ['ER4338', 'KAMUELA, UNITED STATES', 'GLENS FALLS, UNITED STATES', 'Medium Activity', 7259],
                                ['ZI8976', 'GAINESVILLE, UNITED STATES', 'MISSOULA, UNITED STATES', 'Medium Activity', 7248],
                                ['AM6317', 'REEDSVILLE, UNITED STATES', 'BRIDGEWATER, UNITED STATES', 'Medium Activity', 7229],
                                ['AL6672', 'FT BRAGG, UNITED STATES', 'FRONT ROYAL, UNITED STATES', 'Medium Activity', 7214],
                                ['ZI6264', 'EAST HAMPTON, UNITED STATES', 'HAYWARD, UNITED STATES', 'Medium Activity', 7198],
                                ['DJ1059', 'FRANKFORT, UNITED STATES', 'HARRISBURG, UNITED STATES', 'Medium Activity', 7190],
                                ['ES6187', 'CRETE, UNITED STATES', 'ORLANDO, UNITED STATES', 'Medium Activity', 7178],
                                ['DO7105', 'AFTON, UNITED STATES', 'NEW BERN, UNITED STATES', 'Medium Activity', 7159],
                                ['CZ5688', 'SAN MARCOS, UNITED STATES', 'BROOKSVILLE, UNITED STATES', 'Medium Activity', 7158],
                                ['BU5810', 'COMPTON, UNITED STATES', 'LONGVILLE, UNITED STATES', 'Medium Activity', 7130],
                                ['CU2020', 'RANTOUL, UNITED STATES', 'GREENVILLE, UNITED STATES', 'Medium Activity', 7125],
                                ['IS5932', 'BARTOW, UNITED STATES', 'RUSH CITY, UNITED STATES', 'Medium Activity', 7118],
                                ['TH1991', 'BROOKINGS, UNITED STATES', 'ROUNDUP, UNITED STATES', 'Medium Activity', 7109],
                                ['TR3103', 'ORLANDO, UNITED STATES', 'DETROIT LAKES, UNITED STATES', 'Medium Activity', 7094],
                                ['CY1488', 'BRUNSWICK, UNITED STATES', 'ORD, UNITED STATES', 'Medium Activity', 7092],
                                ['BR1926', 'LOGAN, UNITED STATES', 'KEARNEY, UNITED STATES', 'Medium Activity', 7084],
                                ['AU9197', 'RUTHERFORDTON, UNITED STATES', 'FAIRFIELD, UNITED STATES', 'Medium Activity', 7061],
                                ['ER1039', 'UNALAKLEET, UNITED STATES', 'ROBINSON, UNITED STATES', 'Medium Activity', 7060],
                                ['DJ2862', 'MYRTLE BEACH, UNITED STATES', 'INDIANAPOLIS, UNITED STATES', 'Medium Activity', 7043],
                                ['RU9151', 'GAITHERSBURG, UNITED STATES', 'OGDENSBURG, UNITED STATES', 'Medium Activity', 7029],
                                ['SO8920', 'ST INIGOES, UNITED STATES', 'VAN NUYS, UNITED STATES', 'Medium Activity', 6999],
                                ['EL2769', 'HARTFORD, UNITED STATES', 'STUTTGART, UNITED STATES', 'Medium Activity', 6984],
                                ['JE9502', 'NAPA, UNITED STATES', 'HARRISON, UNITED STATES', 'Medium Activity', 6983],
                                ['CO3502', 'CHARLEVOIX, UNITED STATES', 'SAN ANDREAS, UNITED STATES', 'Medium Activity', 6953],
                                ['NA8198', 'WILKES-BARRE, UNITED STATES', 'MINNEAPOLIS, UNITED STATES', 'Medium Activity', 6949],
                                ['YU1039', 'GRIFFIN, UNITED STATES', 'FT COLLINS-LOVELAND, UNITED STATES', 'Medium Activity', 6929],
                                ['YE1695', 'WAGNER, UNITED STATES', 'FREEPORT, UNITED STATES', 'Medium Activity', 6926],
                                ['SW5037', 'PORTERVILLE, UNITED STATES', 'LAKELAND, UNITED STATES', 'Medium Activity', 6880],
                                ['SW2230', 'BILOXI, UNITED STATES', 'WISCASSET, UNITED STATES', 'Medium Activity', 6872],
                                ['SE9624', 'GOSHEN, UNITED STATES', 'PONTIAC, UNITED STATES', 'Medium Activity', 6855],
                                ['UN6147', 'KNOB NOSTER, UNITED STATES', 'DAHLGREN, UNITED STATES', 'Medium Activity', 6824],
                                ['WA9878', 'SCAPPOOSE, UNITED STATES', 'BURNS, UNITED STATES', 'Medium Activity', 6820],
                                ['PE6721', 'ALBANY, UNITED STATES', 'BEAUFORT, UNITED STATES', 'Medium Activity', 6813],
                                ['ER3915', 'CAPE NEWENHAM, UNITED STATES', 'GRAND RAPIDS, UNITED STATES', 'Medium Activity', 6804],
                                ['BA5867', 'MINOT, UNITED STATES', 'WASHINGTON, UNITED STATES', 'Medium Activity', 6801],
                                ['VI4917', 'OAK ISLAND, UNITED STATES', 'YAKIMA, UNITED STATES', 'Medium Activity', 6790],
                                ['IR8147', 'BATTLE CREEK, UNITED STATES', 'DELAWARE, UNITED STATES', 'Medium Activity', 6787],
                                ['MA1427', 'FREMONT, UNITED STATES', 'HERMISTON, UNITED STATES', 'Medium Activity', 6730],
                                ['SU2268', 'LAKE CHARLES, UNITED STATES', 'MIDDLETON I, UNITED STATES', 'Medium Activity', 6689],
                                ['UR5878', 'GAINESVILLE, UNITED STATES', 'ADA, UNITED STATES', 'Medium Activity', 6674],
                                ['TR3884', 'SAN MARCOS, UNITED STATES', 'MITCHELL, UNITED STATES', 'Medium Activity', 6667],
                                ['TR7790', 'MOUNTAIN VIEW, UNITED STATES', 'DULUTH, UNITED STATES', 'Medium Activity', 6642],
                                ['CR1931', 'HEMET, UNITED STATES', 'THERMOPOLIS, UNITED STATES', 'Medium Activity', 6641],
                                ['NA7435', 'SEDONA, UNITED STATES', 'BATTLE CREEK, UNITED STATES', 'Medium Activity', 6635],
                                ['ES1054', 'FREDERICK, UNITED STATES', 'FARMINGTON, UNITED STATES', 'Medium Activity', 6617],
                                ['UN1633', 'KNOB NOSTER, UNITED STATES', 'PONCA CITY, UNITED STATES', 'Medium Activity', 6613],
                                ['DE4536', 'GUTHRIE, UNITED STATES', 'SAULT STE MARIE, UNITED STATES', 'Medium Activity', 6598],
                                ['MY6003', 'HOLYOKE, UNITED STATES', 'LYONS, UNITED STATES', 'Medium Activity', 6586],
                                ['AR9453', 'LITTLE FALLS, UNITED STATES', 'HOUSTON, UNITED STATES', 'Medium Activity', 6578],
                                ['HA7134', 'OTTAWA, UNITED STATES', 'NEW YORK, UNITED STATES', 'Medium Activity', 6552],
                                ['KO4843', 'CALEDONIA, UNITED STATES', 'NASHVILLE, UNITED STATES', 'Medium Activity', 6520],
                                ['FA1933', 'MILWAUKEE, UNITED STATES', 'SPRINGFIELD, UNITED STATES', 'Medium Activity', 6515],
                                ['GA4322', 'JACKSONVILLE, UNITED STATES', 'NORFOLK, UNITED STATES', 'Medium Activity', 6511],
                                ['UK2951', 'DRUMMOND, UNITED STATES', 'ALLIANCE, UNITED STATES', 'Medium Activity', 6480],
                                ['RE8542', 'MULLEN, UNITED STATES', 'CRAIG, UNITED STATES', 'Medium Activity', 6478],
                                ['AU7110', 'MARATHON, UNITED STATES', 'SHISHMAREF, UNITED STATES', 'Medium Activity', 6464],
                                ['IN4127', 'SULLIVAN, UNITED STATES', 'JACKSONVILLE, UNITED STATES', 'Medium Activity', 6455],
                                ['IN6795', 'OAHU, UNITED STATES', 'VANDALIA, UNITED STATES', 'Medium Activity', 6425],
                                ['SI6262', 'DECORAH, UNITED STATES', 'KAPOLEI, UNITED STATES', 'Medium Activity', 6406],
                                ['AN8979', 'CHANDLER, UNITED STATES', 'WARROAD, UNITED STATES', 'Medium Activity', 6393],
                                ['AZ8820', 'SEVIERVILLE, UNITED STATES', 'HAINES, UNITED STATES', 'Medium Activity', 6377],
                                ['UR4131', 'BALTIMORE, UNITED STATES', 'MONTROSE, UNITED STATES', 'Medium Activity', 6373],
                                ['LA1237', 'ALBUQUERQUE, UNITED STATES', 'CHARLES CITY, UNITED STATES', 'Medium Activity', 6334],
                                ['NO9525', 'WATERTOWN, UNITED STATES', 'WALNUT RIDGE, UNITED STATES', 'Medium Activity', 6287],
                                ['JO9003', 'ROSEBURG, UNITED STATES', 'MILLEDGEVILLE, UNITED STATES', 'Medium Activity', 6285],
                                ['IT1776', 'HENDERSON, UNITED STATES', 'HOOPER BAY, UNITED STATES', 'Medium Activity', 6268],
                                ['ZI3151', 'BRUNSWICK, UNITED STATES', 'CAMP ROBINSON, UNITED STATES', 'Medium Activity', 6267],
                                ['GH8991', 'KAUNAKAKAI, UNITED STATES', 'GAITHERSBURG, UNITED STATES', 'Medium Activity', 6265],
                                ['RO4754', 'COLUMBUS-W POINT-STARKVILLE, UNITED STATES', 'SALLISAW, UNITED STATES', 'Medium Activity', 6253],
                                ['CU2063', 'WICHITA, UNITED STATES', 'PAXSON, UNITED STATES', 'Medium Activity', 6249],
                                ['VE3232', 'MALDEN, UNITED STATES', 'TAMPA, UNITED STATES', 'Medium Activity', 6247],
                                ['JO1759', 'GREELEY, UNITED STATES', 'PONTIAC, UNITED STATES', 'Medium Activity', 6230],
                                ['UN5290', 'ATOKA, UNITED STATES', 'HAVRE, UNITED STATES', 'Medium Activity', 6224],
                                ['IV5446', 'SUMMERSVILLE, UNITED STATES', 'ALTUS, UNITED STATES', 'Medium Activity', 6222],
                                ['OM5991', 'LEMOORE, UNITED STATES', 'CHARLEVOIX, UNITED STATES', 'Medium Activity', 6221],
                                ['SO7743', 'COLUMBUS, UNITED STATES', 'CHEROKEE, UNITED STATES', 'Medium Activity', 6204],
                                ['KY4949', 'FALLON, UNITED STATES', 'BROOKSVILLE, UNITED STATES', 'Medium Activity', 6189],
                                ['TO5208', 'TEKAMAH, UNITED STATES', 'GRAND PRAIRIE, UNITED STATES', 'Medium Activity', 6160],
                                ['UG7248', 'CHICAGO/ PROSPECT HGTS/ WHEELI, UNITED STATES', 'ANGOLA, UNITED STATES', 'Medium Activity', 6159],
                                ['MO7962', 'LAKE CITY, UNITED STATES', 'HARRISBURG, UNITED STATES', 'Medium Activity', 6155],
                                ['UG3109', 'SAN FRANCISCO, UNITED STATES', 'BENTON HARBOR, UNITED STATES', 'Medium Activity', 6140],
                                ['QA1273', 'PAXSON, UNITED STATES', 'SOUTH LAKE TAHOE, UNITED STATES', 'Medium Activity', 6111],
                                ['SA8177', "O'NEILL, UNITED STATES", 'PASCAGOULA, UNITED STATES', 'Medium Activity', 6110],
                                ['WA4222', 'LOST RIVER, UNITED STATES', 'MORRISVILLE, UNITED STATES', 'Medium Activity', 6093],
                                ['GH1728', 'EAGLE, UNITED STATES', 'ARDMORE, UNITED STATES', 'Medium Activity', 6076],
                                ['WA1665', 'SAGINAW, UNITED STATES', 'PARKERSBURG, UNITED STATES', 'Medium Activity', 6069],
                                ['AM5320', 'AUSTIN, UNITED STATES', 'ODESSA, UNITED STATES', 'Medium Activity', 6065],
                                ['MO5174', 'WABASH, UNITED STATES', 'SEWARD, UNITED STATES', 'Medium Activity', 6050],
                                ['IT7474', 'NORFOLK, UNITED STATES', 'BINGHAMTON, UNITED STATES', 'Medium Activity', 6043],
                                ['MY1319', 'MINOT, UNITED STATES', 'MOULTRIE, UNITED STATES', 'Medium Activity', 6039],
                                ['RU7114', 'BAD AXE, UNITED STATES', 'OAK ISLAND, UNITED STATES', 'Medium Activity', 6019],
                                ['NA8789', 'PORTLAND, UNITED STATES', 'PETERSBURG, UNITED STATES', 'Medium Activity', 6012],
                                ['DJ4637', 'TAMPA, UNITED STATES', 'JESUP, UNITED STATES', 'Medium Activity', 5974],
                                ['ES8845', 'OROVILLE, UNITED STATES', 'ST FRANCIS, UNITED STATES', 'Medium Activity', 5974],
                                ['TA7838', 'ST GEORGE, UNITED STATES', 'LIVERMORE, UNITED STATES', 'Medium Activity', 5964],
                                ['SE1211', 'DODGE CITY, UNITED STATES', 'PROVIDENCE, UNITED STATES', 'Medium Activity', 5950],
                                ['BR8974', 'DELANO, UNITED STATES', 'PEORIA, UNITED STATES', 'Medium Activity', 5948],
                                ['CR2424', 'DANVILLE, UNITED STATES', 'BLYTHE, UNITED STATES', 'Medium Activity', 5943],
                                ['GA8856', 'KOKOMO, UNITED STATES', 'SAND POINT, UNITED STATES', 'Medium Activity', 5933],
                                ['SP5726', 'LYNCHBURG, UNITED STATES', 'PLATINUM, UNITED STATES', 'Medium Activity', 5925],
                                ['VE1320', 'NORTH MYRTLE BEACH, UNITED STATES', 'DAHLGREN, UNITED STATES', 'Medium Activity', 5896],
                                ['CE1850', 'SHELL LAKE, UNITED STATES', 'ST PAUL I, UNITED STATES', 'Medium Activity', 5884],
                                ['SR1923', 'HANKSVILLE, UNITED STATES', 'MOKAPU, UNITED STATES', 'Medium Activity', 5873],
                                ['AF5169', 'INDIANAPOLIS, UNITED STATES', 'MOSINEE, UNITED STATES', 'Medium Activity', 5867],
                                ['JA1317', 'FT HOOD, UNITED STATES', 'CORVALLIS, UNITED STATES', 'Medium Activity', 5836],
                                ['CO4638', 'DETROIT-GROSSE ILE, UNITED STATES', 'SAND POINT, UNITED STATES', 'Medium Activity', 5813],
                                ['TA1877', 'MITCHELL, UNITED STATES', 'LIVINGSTON, UNITED STATES', 'Medium Activity', 5809],
                                ['AL8474', 'ANCHORAGE, UNITED STATES', 'IOWA CITY, UNITED STATES', 'Medium Activity', 5798],
                                ['MI3429', 'ALBION, UNITED STATES', 'MARION-WYTHEVILLE, UNITED STATES', 'Medium Activity', 5796],
                                ['CY4389', 'ALMA, UNITED STATES', 'COOK, UNITED STATES', 'Medium Activity', 5780],
                                ['EG6927', 'PORTLAND, UNITED STATES', 'GREENVILLE, UNITED STATES', 'Medium Activity', 5780],
                                ['FA7732', 'GLADWIN, UNITED STATES', 'SPOKANE, UNITED STATES', 'Medium Activity', 5747],
                                ['KO1764', 'SEVIERVILLE, UNITED STATES', 'BRIGHAM CITY, UNITED STATES', 'Medium Activity', 5730],
                                ['DA2455', 'KIDRON, UNITED STATES', 'MONTROSE, UNITED STATES', 'Medium Activity', 5719],
                                ['DE1609', 'MANASSAS, UNITED STATES', 'OROVILLE, UNITED STATES', 'Medium Activity', 5717],
                                ['TR6023', 'IDA GROVE, UNITED STATES', 'IMPERIAL, UNITED STATES', 'Medium Activity', 5716],
                                ['TH8111', 'ALEXANDRIA, UNITED STATES', 'EAU CLAIRE, UNITED STATES', 'Medium Activity', 5705],
                                ['UR1624', 'AMERY, UNITED STATES', 'MISSOULA, UNITED STATES', 'Medium Activity', 5692],
                                ['KY7837', 'SALT LAKE CITY, UNITED STATES', 'POTTSTOWN, UNITED STATES', 'Medium Activity', 5682],
                                ['SA8852', 'MARSHALL, UNITED STATES', 'PONTIAC, UNITED STATES', 'Medium Activity', 5646],
                                ['CY1964', 'KOKOMO, UNITED STATES', 'BALTIMORE, UNITED STATES', 'Medium Activity', 5643],
                                ['NA3144', 'CODY, UNITED STATES', 'CHEFORNAK, UNITED STATES', 'Medium Activity', 5627],
                                ['TO1460', 'ALBION, UNITED STATES', 'SHELBY, UNITED STATES', 'Medium Activity', 5627],
                                ['RO4820', 'ORLANDO, UNITED STATES', 'BURBANK, UNITED STATES', 'Medium Activity', 5624],
                                ['LE1327', 'COFFEYVILLE, UNITED STATES', 'DUBUQUE, UNITED STATES', 'Medium Activity', 5621],
                                ['AL1547', 'ROCKY MOUNT, UNITED STATES', 'MINNEAPOLIS, UNITED STATES', 'Medium Activity', 5612],
                                ['VE1350', 'ROCKPORT, UNITED STATES', 'MIAMI, UNITED STATES', 'Medium Activity', 5610],
                                ['NA3702', 'TWENTYNINE PALMS, UNITED STATES', 'PARK FALLS, UNITED STATES', 'Medium Activity', 5606],
                                ['RU7901', 'ROME, UNITED STATES', 'CARTERSVILLE, UNITED STATES', 'Medium Activity', 5601],
                                ['NA1312', 'LANCASTER, UNITED STATES', 'SANTA FE, UNITED STATES', 'Medium Activity', 5597],
                                ['GE2570', 'DWIGHT, UNITED STATES', 'WICHITA, UNITED STATES', 'Medium Activity', 5579],
                                ['FA5517', 'MC RAE, UNITED STATES', 'DILLINGHAM, UNITED STATES', 'Medium Activity', 5568],
                                ['WA1176', 'WILLOUGHBY, UNITED STATES', 'SPARTANBURG, UNITED STATES', 'Medium Activity', 5565],
                                ['MI1413', 'BAKER CITY, UNITED STATES', 'WATONGA, UNITED STATES', 'Medium Activity', 5547],
                                ['ST8898', 'LAS CRUCES, UNITED STATES', 'ARCO, UNITED STATES', 'Medium Activity', 5535],
                                ['FI7683', 'HAMMOND, UNITED STATES', 'HAZLETON, UNITED STATES', 'Medium Activity', 5500],
                                ['WE7788', 'SHENANDOAH, UNITED STATES', 'FITCHBURG, UNITED STATES', 'Medium Activity', 5499],
                                ['UG5815', 'OTTAWA, UNITED STATES', 'MONTICELLO, UNITED STATES', 'Medium Activity', 5493],
                                ['HU1082', 'LANCASTER, UNITED STATES', 'FOREST CITY, UNITED STATES', 'Medium Activity', 5487],
                                ['AR8607', 'MARION, UNITED STATES', 'CLAY CENTER, UNITED STATES', 'Medium Activity', 5453],
                                ['ET1007', 'FT WORTH, UNITED STATES', 'BIRCHWOOD, UNITED STATES', 'Medium Activity', 5451],
                                ['SO8504', 'ASH FLAT, UNITED STATES', 'LANCASTER, UNITED STATES', 'Medium Activity', 5444],
                                ['YE8116', 'WISCASSET, UNITED STATES', 'KEENE, UNITED STATES', 'Medium Activity', 5421],
                                ['SP5715', 'YANKTON, UNITED STATES', 'SAN ANTONIO, UNITED STATES', 'Medium Activity', 5416],
                                ['UK4314', 'JACKSON, UNITED STATES', 'HANCOCK, UNITED STATES', 'Medium Activity', 5416],
                                ['LU2432', 'MANISTIQUE, UNITED STATES', 'AHOSKIE, UNITED STATES', 'Medium Activity', 5402],
                                ['RE6294', 'PITTSBURG, UNITED STATES', 'WESTMINSTER, UNITED STATES', 'Medium Activity', 5388],
                                ['MA6003', 'HARLAN, UNITED STATES', 'TWIN FALLS, UNITED STATES', 'Medium Activity', 5384],
                                ['LU5657', 'WAUCHULA, UNITED STATES', 'NORFOLK, UNITED STATES', 'Medium Activity', 5358],
                                ['BU4491', 'TANANA, UNITED STATES', 'FESTUS, UNITED STATES', 'Medium Activity', 5345],
                                ['KI9835', 'JACKSON, UNITED STATES', 'FARIBAULT, UNITED STATES', 'Medium Activity', 5336],
                                ['TA8715', 'KEY WEST, UNITED STATES', 'SPENCER, UNITED STATES', 'Medium Activity', 5324],
                                ['QA4904', 'NASHVILLE, UNITED STATES', 'BOUNTIFUL, UNITED STATES', 'Medium Activity', 5309],
                                ['AZ1323', 'WORTHINGTON, UNITED STATES', 'PENSACOLA, UNITED STATES', 'Medium Activity', 5306],
                                ['HA9884', 'PENN YAN, UNITED STATES', 'TOMS RIVER, UNITED STATES', 'Medium Activity', 5305],
                                ['MO3131', 'COLUMBUS, UNITED STATES', 'KNOXVILLE, UNITED STATES', 'Medium Activity', 5301],
                                ['YE3740', 'SELINSGROVE, UNITED STATES', 'SAN DIEGO, UNITED STATES', 'Medium Activity', 5281],
                                ['CU2802', 'KEMMERER, UNITED STATES', 'TIN CITY, UNITED STATES', 'Medium Activity', 5216],
                                ['SE7649', 'WINCHESTER, UNITED STATES', 'DECATUR, UNITED STATES', 'Medium Activity', 5214],
                                ['CZ1539', 'JASPER, UNITED STATES', 'TOLEDO, UNITED STATES', 'Medium Activity', 5188],
                                ['IN2177', 'WELLINGTON, UNITED STATES', 'SALISBURY, UNITED STATES', 'Medium Activity', 5184],
                                ['UZ1553', 'TUSCALOOSA, UNITED STATES', 'LOUISBURG, UNITED STATES', 'Medium Activity', 5142],
                                ['EL1896', 'HOBART, UNITED STATES', 'FT BELVOIR, UNITED STATES', 'Medium Activity', 5137],
                                ['UR7539', 'TETERBORO, UNITED STATES', 'CARIBOU, UNITED STATES', 'Medium Activity', 5120],
                                ['GE9943', 'PALM SPRINGS, UNITED STATES', 'FRIENDLY, UNITED STATES', 'Medium Activity', 5111],
                                ['UN1252', 'SIOUX CENTER, UNITED STATES', 'BRUNSWICK, UNITED STATES', 'Medium Activity', 5103],
                                ['AF5511', 'MOAB, UNITED STATES', 'DUNCAN, UNITED STATES', 'Medium Activity', 5101],
                                ['TR5561', 'YAKIMA, UNITED STATES', 'LEMMON, UNITED STATES', 'Medium Activity', 5096],
                                ['RE2124', 'PASCAGOULA, UNITED STATES', 'COLUMBIA, UNITED STATES', 'Medium Activity', 5091],
                                ['RU8104', 'LADYSMITH, UNITED STATES', 'ALAMOGORDO, UNITED STATES', 'Medium Activity', 5081],
                                ['IN5659', 'WESTFIELD/ SPRINGFIELD, UNITED STATES', 'NEW ORLEANS, UNITED STATES', 'Medium Activity', 5076],
                                ['ZA4906', 'RAPID CITY, UNITED STATES', 'VACAVILLE, UNITED STATES', 'Medium Activity', 5051],
                                ['CR1704', 'SANDERSVILLE, UNITED STATES', 'DWIGHT, UNITED STATES', 'Medium Activity', 5041],
                                ['MA1579', 'FAREWELL LAKE, UNITED STATES', 'MORGANTON, UNITED STATES', 'Medium Activity', 5036],
                                ['BR4248', 'SAFFORD, UNITED STATES', 'LITTLE ROCK, UNITED STATES', 'Medium Activity', 5034],
                                ['IT8955', 'INYOKERN, UNITED STATES', 'KERRVILLE, UNITED STATES', 'Low Activity', 4999],
                                ['RW1840', 'AMES, UNITED STATES', 'BILOXI, UNITED STATES', 'Low Activity', 4992],
                                ['ME3758', 'POINT MC INTYRE, UNITED STATES', 'PORT HEIDEN, UNITED STATES', 'Low Activity', 4978],
                                ['AL4631', 'REXBURG, UNITED STATES', 'HENDERSON, UNITED STATES', 'Low Activity', 4969],
                                ['SA6469', 'TELLURIDE, UNITED STATES', 'GAITHERSBURG, UNITED STATES', 'Low Activity', 4965],
                                ['SU1241', 'LINCOLNTON, UNITED STATES', 'JACKSONVILLE, UNITED STATES', 'Low Activity', 4955],
                                ['IN6123', 'SALLISAW, UNITED STATES', 'OMAHA, UNITED STATES', 'Low Activity', 4928],
                                ['GU1200', 'WAPAKONETA, UNITED STATES', 'CUMBERLAND, UNITED STATES', 'Low Activity', 4914],
                                ['QA1677', 'SANTA PAULA, UNITED STATES', 'HARLAN, UNITED STATES', 'Low Activity', 4911],
                                ['BR4921', 'TOMPKINSVILLE, UNITED STATES', 'HAWTHORNE, UNITED STATES', 'Low Activity', 4909],
                                ['BA6328', 'SLEETMUTE, UNITED STATES', 'OGDEN, UNITED STATES', 'Low Activity', 4900],
                                ['UR9705', 'VALPARAISO, UNITED STATES', 'NORTH ADAMS, UNITED STATES', 'Low Activity', 4889],
                                ['GH9790', 'GREENFIELD, UNITED STATES', 'MONTGOMERY, UNITED STATES', 'Low Activity', 4886],
                                ['VE5573', 'DEVILS LAKE, UNITED STATES', 'MOUNT PLEASANT, UNITED STATES', 'Low Activity', 4885],
                                ['IV7414', 'HATTERAS, UNITED STATES', 'SARASOTA/ BRADENTON, UNITED STATES', 'Low Activity', 4877],
                                ['AR6955', 'GULKANA, UNITED STATES', 'MERIDIAN, UNITED STATES', 'Low Activity', 4858],
                                ['KO2721', 'NORFOLK, UNITED STATES', 'BIRMINGHAM, UNITED STATES', 'Low Activity', 4832],
                                ['YE5186', 'MINOCQUA-WOODRUFF, UNITED STATES', 'OMAHA, UNITED STATES', 'Low Activity', 4823],
                                ['CH3914', 'ATWOOD, UNITED STATES', 'BENTONVILLE, UNITED STATES', 'Low Activity', 4808],
                                ['RE5456', 'FT HUACHUCA, UNITED STATES', 'ROGERSVILLE, UNITED STATES', 'Low Activity', 4789],
                                ['ST8550', 'MOUNTAIN HOME, UNITED STATES', 'HAZEN, UNITED STATES', 'Low Activity', 4788],
                                ['AU3342', 'CHEROKEE, UNITED STATES', 'FENTRESS, UNITED STATES', 'Low Activity', 4786],
                                ['CU6108', 'GRAND FORKS, UNITED STATES', 'NEWCASTLE, UNITED STATES', 'Low Activity', 4765],
                                ['NI9531', 'CHEROKEE, UNITED STATES', "COEUR D'ALENE, UNITED STATES", 'Low Activity', 4764],
                                ['ZA5582', 'SAVOONGA, UNITED STATES', 'ANDREWS, UNITED STATES', 'Low Activity', 4753],
                                ['UK7348', 'TWIN FALLS, UNITED STATES', 'HAZLEHURST, UNITED STATES', 'Low Activity', 4715],
                                ['BO9148', 'RICHMOND, UNITED STATES', 'PALM SPRINGS, UNITED STATES', 'Low Activity', 4706],
                                ['TH1462', 'COLD BAY, UNITED STATES', 'LEWISTON, UNITED STATES', 'Low Activity', 4681],
                                ['WE5545', 'MADISON, UNITED STATES', 'JAMESTOWN, UNITED STATES', 'Low Activity', 4680],
                                ['JO8839', 'DANVILLE, UNITED STATES', 'DENVER, UNITED STATES', 'Low Activity', 4667],
                                ['CU8668', 'HARLINGEN, UNITED STATES', 'LADYSMITH, UNITED STATES', 'Low Activity', 4661],
                                ['CH7513', 'WILLMAR, UNITED STATES', 'WHEATLAND, UNITED STATES', 'Low Activity', 4639],
                                ['GA7657', 'CEDAR RAPIDS, UNITED STATES', 'MC MINNVILLE, UNITED STATES', 'Low Activity', 4639],
                                ['SU1915', 'HARLINGEN, UNITED STATES', 'MONROE, UNITED STATES', 'Low Activity', 4627],
                                ['SP3497', 'RICE LAKE, UNITED STATES', 'HILLSBORO, UNITED STATES', 'Low Activity', 4601],
                                ['IC2874', 'PALACIOS, UNITED STATES', 'HAILEY, UNITED STATES', 'Low Activity', 4597],
                                ['RU5293', 'GREYBULL, UNITED STATES', 'PRICE, UNITED STATES', 'Low Activity', 4589],
                                ['AZ2625', 'PHILADELPHIA, UNITED STATES', 'GREENFIELD, UNITED STATES', 'Low Activity', 4584],
                                ['BA2869', 'BATESVILLE, UNITED STATES', 'TIN CITY, UNITED STATES', 'Low Activity', 4582],
                                ['SO7968', 'MARATHON, UNITED STATES', 'WEST BEND, UNITED STATES', 'Low Activity', 4577],
                                ['KA3789', 'MANHATTAN, UNITED STATES', 'DANBURY, UNITED STATES', 'Low Activity', 4575],
                                ['ZI6188', 'ELIZABETH CITY, UNITED STATES', 'WISCASSET, UNITED STATES', 'Low Activity', 4572],
                                ['KU2457', 'HASTINGS, UNITED STATES', 'WASHINGTON, UNITED STATES', 'Low Activity', 4564],
                                ['EL3960', 'RALEIGH/ DURHAM, UNITED STATES', 'WRIGHTSTOWN, UNITED STATES', 'Low Activity', 4552],
                                ['KU1452', 'ADRIAN, UNITED STATES', 'QUINHAGAK, UNITED STATES', 'Low Activity', 4552],
                                ['JO1064', 'POINT HOPE, UNITED STATES', 'WARROAD, UNITED STATES', 'Low Activity', 4549],
                                ['HA7026', 'ELKHART, UNITED STATES', 'FALLON, UNITED STATES', 'Low Activity', 4545],
                                ['KI7489', 'TEHACHAPI, UNITED STATES', 'CINCINNATI, UNITED STATES', 'Low Activity', 4540],
                                ['NI2913', 'BLYTHEVILLE, UNITED STATES', 'STARKVILLE, UNITED STATES', 'Low Activity', 4534],
                                ['UG1501', 'MICHIGAN CITY, UNITED STATES', 'BUCKLAND, UNITED STATES', 'Low Activity', 4529],
                                ['RO1090', 'LORAIN/ ELYRIA, UNITED STATES', 'SHREVEPORT, UNITED STATES', 'Low Activity', 4522],
                                ['KO3866', 'UTICA, UNITED STATES', 'MASON, UNITED STATES', 'Low Activity', 4488],
                                ['BH4662', 'DUBLIN, UNITED STATES', 'SPARREVOHN, UNITED STATES', 'Low Activity', 4464],
                                ['SI6378', 'MONTE VISTA, UNITED STATES', 'NAPLES, UNITED STATES', 'Low Activity', 4462],
                                ['DA3014', 'ARTESIA, UNITED STATES', 'ATLANTA, UNITED STATES', 'Low Activity', 4453],
                                ['KA1073', 'WAGNER, UNITED STATES', 'DE LAND, UNITED STATES', 'Low Activity', 4446],
                                ['ZA9495', 'MUSCATINE, UNITED STATES', 'FT SCOTT, UNITED STATES', 'Low Activity', 4441],
                                ['ES3957', 'TAMPA, UNITED STATES', 'SEARCY, UNITED STATES', 'Low Activity', 4434],
                                ['JA1786', 'RALEIGH/ DURHAM, UNITED STATES', 'FOSTORIA, UNITED STATES', 'Low Activity', 4434],
                                ['DE8785', 'WILMINGTON, UNITED STATES', 'OMAHA, UNITED STATES', 'Low Activity', 4432],
                                ['VA2178', 'WILLOW, UNITED STATES', 'BREMERTON, UNITED STATES', 'Low Activity', 4417],
                                ['HA3425', 'GRAND PRAIRIE, UNITED STATES', 'MONTEVIDEO, UNITED STATES', 'Low Activity', 4382],
                                ['GH4246', 'GLENS FALLS, UNITED STATES', 'DENISON, UNITED STATES', 'Low Activity', 4373],
                                ['NE7662', 'WACO, UNITED STATES', 'NASHUA, UNITED STATES', 'Low Activity', 4373],
                                ['RE9932', 'ELIZABETHTOWN, UNITED STATES', 'AKRON, UNITED STATES', 'Low Activity', 4372],
                                ['SR7387', 'EL DORADO, UNITED STATES', 'UGNU KUPARUK, UNITED STATES', 'Low Activity', 4366],
                                ['IC4901', 'WILLIAMSBURG, UNITED STATES', 'EUGENE, UNITED STATES', 'Low Activity', 4356],
                                ['SP1410', 'KLAMATH FALLS, UNITED STATES', 'MT PLEASANT, UNITED STATES', 'Low Activity', 4311],
                                ['BU1169', 'SOUTH HILL, UNITED STATES', 'SEDALIA, UNITED STATES', 'Low Activity', 4302],
                                ['NE4498', 'OPELOUSAS, UNITED STATES', 'OAK ISLAND, UNITED STATES', 'Low Activity', 4288],
                                ['AZ1409', 'GRIFFIN, UNITED STATES', 'WICHITA, UNITED STATES', 'Low Activity', 4287],
                                ['CR5783', 'MONTROSE, UNITED STATES', 'MT HOLLY, UNITED STATES', 'Low Activity', 4285],
                                ['EG1255', 'LYNCHBURG, UNITED STATES', 'IMMOKALEE, UNITED STATES', 'Low Activity', 4263],
                                ['EQ4385', 'BURLINGTON, UNITED STATES', 'WINDOW ROCK, UNITED STATES', 'Low Activity', 4263],
                                ['AF1363', 'CANADIAN, UNITED STATES', 'INDIANAPOLIS, UNITED STATES', 'Low Activity', 4249],
                                ['SO7110', 'CHICAGO/ PROSPECT HGTS/ WHEELI, UNITED STATES', 'SAC CITY, UNITED STATES', 'Low Activity', 4245],
                                ['KY1862', 'WASKISH, UNITED STATES', 'BENTONVILLE, UNITED STATES', 'Low Activity', 4212],
                                ['SP3786', 'ALAMOGORDO, UNITED STATES', 'PINE MOUNTAIN, UNITED STATES', 'Low Activity', 4206],
                                ['UG3979', 'DE KALB, UNITED STATES', 'PITTSBURGH, UNITED STATES', 'Low Activity', 4201],
                                ['JA8621', 'PORTLAND, UNITED STATES', 'DUMAS, UNITED STATES', 'Low Activity', 4199],
                                ['IT3475', 'VAN NUYS, UNITED STATES', 'RALEIGH/ DURHAM, UNITED STATES', 'Low Activity', 4179],
                                ['DJ1033', 'DETROIT LAKES, UNITED STATES', 'BEAUFORT, UNITED STATES', 'Low Activity', 4173],
                                ['BR7165', 'QUILLAYUTE, UNITED STATES', 'FREEPORT, UNITED STATES', 'Low Activity', 4153],
                                ['BO1531', 'GABBS, UNITED STATES', 'FAIRBURY, UNITED STATES', 'Low Activity', 4148],
                                ['AM6843', 'COLUMBUS, UNITED STATES', 'ELIZABETH CITY, UNITED STATES', 'Low Activity', 4126],
                                ['AN5831', 'PALMDALE, UNITED STATES', 'ELIZABETH CITY, UNITED STATES', 'Low Activity', 4126],
                                ['NI6895', 'WILLOWS, UNITED STATES', 'BOONVILLE, UNITED STATES', 'Low Activity', 4122],
                                ['IC8086', 'KNOXVILLE, UNITED STATES', 'WESTMINSTER, UNITED STATES', 'Low Activity', 4121],
                                ['GI4807', 'BARTER I LRRS, UNITED STATES', 'RAPID CITY, UNITED STATES', 'Low Activity', 4107],
                                ['KY1985', 'KONGIGANAK, UNITED STATES', 'FAREWELL, UNITED STATES', 'Low Activity', 4104],
                                ['UK9814', 'NORTH VERNON, UNITED STATES', 'ALBANY, UNITED STATES', 'Low Activity', 4096],
                                ['GR5936', 'FT HOOD, UNITED STATES', 'OSCODA, UNITED STATES', 'Low Activity', 4095],
                                ['KU8767', 'SALMON, UNITED STATES', 'LAWRENCE, UNITED STATES', 'Low Activity', 4090],
                                ['DA7841', 'WINDER, UNITED STATES', 'CHAPEL HILL, UNITED STATES', 'Low Activity', 4089],
                                ['BR1764', 'CONNERSVILLE, UNITED STATES', 'SUPERIOR, UNITED STATES', 'Low Activity', 4078],
                                ['EG8772', 'ALBION, UNITED STATES', 'YAKIMA, UNITED STATES', 'Low Activity', 4066],
                                ['FA6242', 'FAIRFIELD, UNITED STATES', 'KANAB, UNITED STATES', 'Low Activity', 4060],
                                ['QA9393', 'LOUISA, UNITED STATES', 'HAZEN, UNITED STATES', 'Low Activity', 4058],
                                ['UR1926', 'KENOSHA, UNITED STATES', 'NORWOOD, UNITED STATES', 'Low Activity', 4044],
                                ['HA6897', 'UNALAKLEET, UNITED STATES', 'MC MINNVILLE, UNITED STATES', 'Low Activity', 4038],
                                ['CE8523', 'MARFA, UNITED STATES', 'JOLIET, UNITED STATES', 'Low Activity', 4017],
                                ['GI3520', 'GOSHEN, UNITED STATES', 'NEW BERN, UNITED STATES', 'Low Activity', 4014],
                                ['SW1316', 'SAN JOSE, UNITED STATES', 'WICHITA, UNITED STATES', 'Low Activity', 3982],
                                ['KU1005', 'BOULDER JUNCTION, UNITED STATES', 'RENSSELAER, UNITED STATES', 'Low Activity', 3972],
                                ['NE6793', 'HANA, UNITED STATES', 'HUTCHINSON, UNITED STATES', 'Low Activity', 3966],
                                ['TO9094', 'NEW YORK, UNITED STATES', 'MINNEAPOLIS, UNITED STATES', 'Low Activity', 3963],
                                ['ZA2310', 'FRANKFORT, UNITED STATES', 'MC CALL, UNITED STATES', 'Low Activity', 3955],
                                ['DO7839', 'THOMSON, UNITED STATES', 'MT PLEASANT, UNITED STATES', 'Low Activity', 3952],
                                ['SI7973', 'PAHOKEE, UNITED STATES', 'KEARNEY, UNITED STATES', 'Low Activity', 3940],
                                ['JA4117', 'LINCOLN, UNITED STATES', 'CLEVELAND, UNITED STATES', 'Low Activity', 3926],
                                ['BO6504', 'BUFFALO, UNITED STATES', 'NEWTON, UNITED STATES', 'Low Activity', 3920],
                                ['LE7234', 'MOUNT PLEASANT, UNITED STATES', 'LAKE HAVASU CITY, UNITED STATES', 'Low Activity', 3920],
                                ['PE2895', 'SHELDON, UNITED STATES', 'OAK ISLAND, UNITED STATES', 'Low Activity', 3919],
                                ['TH7797', 'QUAKERTOWN, UNITED STATES', 'LEXINGTON, UNITED STATES', 'Low Activity', 3916],
                                ['NE6274', 'WINSLOW, UNITED STATES', 'HAYWARD, UNITED STATES', 'Low Activity', 3869],
                                ['FR1028', 'JANESVILLE, UNITED STATES', 'LOS ANGELES, UNITED STATES', 'Low Activity', 3813],
                                ['TH3514', 'MANHATTAN, UNITED STATES', 'FRYEBURG, UNITED STATES', 'Low Activity', 3804],
                                ['WA5338', 'GRINNELL, UNITED STATES', 'STAUNTON-WAYNESBORO-HARRISONB*, UNITED STATES', 'Low Activity', 3776],
                                ['SR4214', 'CONNERSVILLE, UNITED STATES', 'MINERAL WELLS, UNITED STATES', 'Low Activity', 3723],
                                ['BR8503', 'FT SUMNER, UNITED STATES', 'SARATOGA, UNITED STATES', 'Low Activity', 3715],
                                ['HA5622', 'ONTONAGON, UNITED STATES', 'CADILLAC, UNITED STATES', 'Low Activity', 3703],
                                ['AL8273', 'PAXSON, UNITED STATES', 'JASPER, UNITED STATES', 'Low Activity', 3667],
                                ['UG8873', 'MADISON, UNITED STATES', 'MONROE, UNITED STATES', 'Low Activity', 3653],
                                ['GI3143', 'PLATTSMOUTH, UNITED STATES', 'REED CITY, UNITED STATES', 'Low Activity', 3651],
                                ['EG3901', 'COMPTON, UNITED STATES', 'FAIRBURY, UNITED STATES', 'Low Activity', 3638],
                                ['BH1799', 'COLUMBUS, UNITED STATES', 'ATLANTA, UNITED STATES', 'Low Activity', 3628],
                                ['EQ9427', 'RED OAK, UNITED STATES', 'DE KALB, UNITED STATES', 'Low Activity', 3614],
                                ['EC9462', 'WEIRWOOD, UNITED STATES', 'GREENWOOD, UNITED STATES', 'Low Activity', 3594],
                                ['MI9412', 'CHARLESTON, UNITED STATES', 'ASPEN, UNITED STATES', 'Low Activity', 3579],
                                ['LU9907', 'DURANGO, UNITED STATES', 'SAVANNAH, UNITED STATES', 'Low Activity', 3553],
                                ['MY6984', 'BELUGA, UNITED STATES', 'CAMP DOUGLAS, UNITED STATES', 'Low Activity', 3544],
                                ['FI5995', 'MT PLEASANT, UNITED STATES', 'IRONWOOD, UNITED STATES', 'Low Activity', 3530],
                                ['ME3104', 'LAWTON, UNITED STATES', 'MOBERLY, UNITED STATES', 'Low Activity', 3504],
                                ['BE6763', 'WABASH, UNITED STATES', 'SANFORD, UNITED STATES', 'Low Activity', 3491],
                                ['GR9521', 'MANISTIQUE, UNITED STATES', 'TORRINGTON, UNITED STATES', 'Low Activity', 3485],
                                ['KE3030', 'HOBBS, UNITED STATES', 'MOBRIDGE, UNITED STATES', 'Low Activity', 3480],
                                ['PU8380', 'REXBURG, UNITED STATES', 'VACAVILLE, UNITED STATES', 'Low Activity', 3467],
                                ['UK8861', 'TEXARKANA, UNITED STATES', 'BENNETTSVILLE, UNITED STATES', 'Low Activity', 3449],
                                ['JA6456', 'NEW MADRID, UNITED STATES', 'QUINHAGAK, UNITED STATES', 'Low Activity', 3410],
                                ['MY2827', 'MIDLAND, UNITED STATES', 'PASCO, UNITED STATES', 'Low Activity', 3394],
                                ['WA4177', 'WAYNESBORO, UNITED STATES', 'CLIFTON-MORENCI, UNITED STATES', 'Low Activity', 3352],
                                ['IT1363', 'MANKATO, UNITED STATES', 'MADISON, UNITED STATES', 'Low Activity', 3343],
                                ['DO3710', 'GARDNER, UNITED STATES', 'MOBILE, UNITED STATES', 'Low Activity', 3327],
                                ['EQ1356', 'WEIRWOOD, UNITED STATES', 'CAPE GIRARDEAU, UNITED STATES', 'Low Activity', 3321],
                                ['HO4948', 'PRESTON, UNITED STATES', 'BLYTHEVILLE, UNITED STATES', 'Low Activity', 3287],
                                ['AR4872', 'GREENVILLE, UNITED STATES', 'THOMSON, UNITED STATES', 'Low Activity', 3280],
                                ['UR1647', 'DOUGLAS, UNITED STATES', 'PERRY, UNITED STATES', 'Low Activity', 3221],
                                ['GU5728', 'MORRISTOWN, UNITED STATES', 'TOCCOA, UNITED STATES', 'Low Activity', 3205],
                                ['KE7574', 'FAYETTEVILLE/ SPRINGDALE/ ROGE, UNITED STATES', 'CHIGNIK, UNITED STATES', 'Low Activity', 3200],
                                ['TU2789', 'AMES, UNITED STATES', 'GARY, UNITED STATES', 'Low Activity', 3197],
                                ['SU9286', 'MILLINOCKET, UNITED STATES', 'LEESBURG, UNITED STATES', 'Low Activity', 3178],
                                ['IN7951', 'APALACHICOLA, UNITED STATES', 'STUART, UNITED STATES', 'Low Activity', 3175],
                                ['KE4962', 'MANKATO, UNITED STATES', 'FT POLK, UNITED STATES', 'Low Activity', 3173],
                                ['PH3107', 'MERRILL, UNITED STATES', 'HEBER SPRINGS, UNITED STATES', 'Low Activity', 3137],
                                ['OM2143', 'YANKTON, UNITED STATES', 'ST CLOUD, UNITED STATES', 'Low Activity', 3130],
                                ['IC4688', 'PINE MOUNTAIN, UNITED STATES', 'SAVANNA, UNITED STATES', 'Low Activity', 3125],
                                ['IT1944', 'PETERSBURG, UNITED STATES', 'MEXIA, UNITED STATES', 'Low Activity', 3117],
                                ['SW6446', 'HUSLIA, UNITED STATES', 'ALICEVILLE, UNITED STATES', 'Low Activity', 3112],
                                ['PA1482', 'WILLOW, UNITED STATES', 'CLEVELAND, UNITED STATES', 'Low Activity', 3069],
                                ['SI3566', 'SPARREVOHN, UNITED STATES', 'KENANSVILLE, UNITED STATES', 'Low Activity', 3056],
                                ['EG1536', 'GREEN BAY, UNITED STATES', 'AKRON, UNITED STATES', 'Low Activity', 3035],
                                ['PA4921', 'RUIDOSO, UNITED STATES', 'SELMER, UNITED STATES', 'Low Activity', 3028],
                                ['DE6893', 'CONNERSVILLE, UNITED STATES', 'WAHPETON, UNITED STATES', 'Low Activity', 3019],
                                ['AF4041', 'MARKSVILLE, UNITED STATES', 'WOODWARD, UNITED STATES', 'Low Activity', 3016],
                                ['BO1663', 'ASTORIA, UNITED STATES', 'MOORELAND, UNITED STATES', 'Low Activity', 2987],
                                ['UG4187', 'UGNU KUPARUK, UNITED STATES', 'CLARKSDALE, UNITED STATES', 'Low Activity', 2987],
                                ['PA2514', 'CHATTANOOGA, UNITED STATES', 'WISCASSET, UNITED STATES', 'Low Activity', 2977],
                                ['FR9337', 'FARMINGTON, UNITED STATES', 'AUBURN, UNITED STATES', 'Low Activity', 2968],
                                ['ST2257', 'RED OAK, UNITED STATES', 'LIVINGSTON, UNITED STATES', 'Low Activity', 2964],
                                ['CE4126', 'CASA GRANDE, UNITED STATES', 'CRESCENT CITY, UNITED STATES', 'Low Activity', 2941],
                                ['MI4717', 'VERSAILLES, UNITED STATES', 'DECATUR, UNITED STATES', 'Low Activity', 2918],
                                ['NO9017', 'STURGEON BAY, UNITED STATES', 'NEOSHO, UNITED STATES', 'Low Activity', 2911],
                                ['SL3645', 'JACKSONVILLE, UNITED STATES', 'MEXIA, UNITED STATES', 'Low Activity', 2898],
                                ['SU3807', 'FRANKFORT, UNITED STATES', 'CLARION, UNITED STATES', 'Low Activity', 2874],
                                ['CY1974', 'HATTIESBURG-LAUREL, UNITED STATES', 'PASO ROBLES, UNITED STATES', 'Low Activity', 2863],
                                ['MI1352', 'ERROL, UNITED STATES', 'INDIANAPOLIS, UNITED STATES', 'Low Activity', 2845],
                                ['IT1277', 'HOQUIAM, UNITED STATES', 'LUSK, UNITED STATES', 'Low Activity', 2818],
                                ['EG4371', 'BEAVER FALLS, UNITED STATES', 'PLATTSBURGH, UNITED STATES', 'Low Activity', 2781],
                                ['OM4727', 'PLATTSMOUTH, UNITED STATES', 'CORPUS CHRISTI, UNITED STATES', 'Low Activity', 2775],
                                ['KO2336', 'PATTERSON, UNITED STATES', 'IOWA CITY, UNITED STATES', 'Low Activity', 2748],
                                ['KO1317', 'ROUNDUP, UNITED STATES', 'MENOMINEE, UNITED STATES', 'Low Activity', 2727],
                                ['DJ3110', 'TOLEDO, UNITED STATES', 'CHICAGO, UNITED STATES', 'Low Activity', 2723],
                                ['BU1379', 'JOPLIN, UNITED STATES', 'HATTIESBURG, UNITED STATES', 'Low Activity', 2719],
                                ['KY2342', 'MT STERLING, UNITED STATES', 'BLOCK ISLAND, UNITED STATES', 'Low Activity', 2671],
                                ['HO2613', 'LEWISBURG, UNITED STATES', 'SAN ANTONIO, UNITED STATES', 'Low Activity', 2634],
                                ['CA3610', 'ORMOND BEACH, UNITED STATES', 'RENSSELAER, UNITED STATES', 'Low Activity', 2623],
                                ['LU3137', 'THREE RIVERS, UNITED STATES', 'FT RILEY, UNITED STATES', 'Low Activity', 2622],
                                ['TU9140', 'NAPA, UNITED STATES', 'WILLIMANTIC, UNITED STATES', 'Low Activity', 2607],
                                ['AU7928', 'MATTOON-CHARLESTON, UNITED STATES', 'OKLAHOMA CITY, UNITED STATES', 'Low Activity', 2606],
                                ['DJ5687', 'BOCA RATON, UNITED STATES', 'CALEDONIA, UNITED STATES', 'Low Activity', 2583],
                                ['ES1102', 'READING, UNITED STATES', 'ST PETERSBURG, UNITED STATES', 'Low Activity', 2564],
                                ['CU3699', 'HAYDEN, UNITED STATES', 'FRANKLIN, UNITED STATES', 'Low Activity', 2562],
                                ['UZ1192', 'KLAMATH FALLS, UNITED STATES', 'FLEMINGSBURG, UNITED STATES', 'Low Activity', 2559],
                                ['PH2954', 'JACKSONVILLE, UNITED STATES', 'COLUMBUS, UNITED STATES', 'Low Activity', 2546],
                                ['DJ9528', 'COLORADO CITY, UNITED STATES', 'SALMON, UNITED STATES', 'Low Activity', 2498],
                                ['JA4415', 'MARANA, UNITED STATES', 'MINDEN, UNITED STATES', 'Low Activity', 2387],
                                ['EG6129', 'THOMASTON, UNITED STATES', 'NEW YORK, UNITED STATES', 'Low Activity', 2346],
                                ['ER9027', 'INDEPENDENCE, UNITED STATES', 'GREENWOOD, UNITED STATES', 'Low Activity', 2339],
                                ['KU1172', 'MEADE, UNITED STATES', 'WARSAW, UNITED STATES', 'Low Activity', 2319],
                                ['SL9463', 'ST PAUL, UNITED STATES', 'AMARILLO, UNITED STATES', 'Low Activity', 2297],
                                ['BO3305', 'EGEGIK, UNITED STATES', 'GRAND FORKS, UNITED STATES', 'Low Activity', 2240],
                                ['SL7796', 'OLATHE, UNITED STATES', 'REXBURG, UNITED STATES', 'Low Activity', 2225],
                                ['SL8636', 'KENAI, UNITED STATES', 'MANISTIQUE, UNITED STATES', 'Low Activity', 2192],
                                ['EL8065', 'STATESBORO, UNITED STATES', 'SYLACAUGA, UNITED STATES', 'Low Activity', 2172],
                                ['GU9630', 'CHEFORNAK, UNITED STATES', 'MEXIA, UNITED STATES', 'Low Activity', 2120],
                                ['UN1806', 'CHAPPELL, UNITED STATES', 'CHILLICOTHE, UNITED STATES', 'Low Activity', 2112],
                                ['PH1229', 'RIVERTON, UNITED STATES', 'ROCKFORD, UNITED STATES', 'Low Activity', 2096],
                                ['MA3384', 'NOGALES, UNITED STATES', 'TOPEKA, UNITED STATES', 'Low Activity', 2063],
                                ['MA7716', 'TACOMA, UNITED STATES', 'HETTINGER, UNITED STATES', 'Low Activity', 2058],
                                ['UG4477', 'MULLEN, UNITED STATES', 'MARION-WYTHEVILLE, UNITED STATES', 'Low Activity', 2032],
                                ['RU6111', 'MT POCONO, UNITED STATES', 'GREENVILLE, UNITED STATES', 'Low Activity', 1946],
                                ['PH4565', 'KETCHIKAN, UNITED STATES', 'WASHINGTON, UNITED STATES', 'Low Activity', 1921],
                                ['GU8557', 'TELLURIDE, UNITED STATES', 'WARSAW, UNITED STATES', 'Low Activity', 1870],
                                ['BR5762', 'LOMPOC, UNITED STATES', 'ALBUQUERQUE, UNITED STATES', 'Low Activity', 1760],
                                ['YE8931', 'MONROE, UNITED STATES', 'ELK CITY, UNITED STATES', 'Low Activity', 1734],
                                ['OM1745', 'WATERTOWN, UNITED STATES', 'CLINTON, UNITED STATES', 'Low Activity', 1724],
                                ['PO2519', 'BIRMINGHAM, UNITED STATES', 'TETERBORO, UNITED STATES', 'Low Activity', 1707],
                                ['BA9434', 'LINCOLN, UNITED STATES', 'CARIBOU, UNITED STATES', 'Low Activity', 1693],
                                ['LE6208', 'PLANT CITY, UNITED STATES', 'FT YUKON, UNITED STATES', 'Low Activity', 1669],
                                ['SL7953', 'LATROBE, UNITED STATES', 'MC ALESTER, UNITED STATES', 'Low Activity', 1668],
                                ['JO1796', 'PULLMAN/ MOSCOW, UNITED STATES', 'SPRINGHILL, UNITED STATES', 'Low Activity', 1657],
                                ['SL5666', 'ROGERS, UNITED STATES', 'BATESVILLE, UNITED STATES', 'Low Activity', 1639],
                                ['SE5025', 'MARYSVILLE, UNITED STATES', 'MERRILL, UNITED STATES', 'Low Activity', 1634],
                                ['UK2852', 'RAMONA, UNITED STATES', 'HOLLYWOOD, UNITED STATES', 'Low Activity', 1590],
                                ['PH3740', 'ROCKDALE, UNITED STATES', 'LANSING, UNITED STATES', 'Low Activity', 1546],
                                ['PH6652', 'ELIZABETHTOWN, UNITED STATES', 'OMAHA, UNITED STATES', 'Low Activity', 1518],
                                ['ME2896', 'OLNEY-NOBLE, UNITED STATES', 'ROME, UNITED STATES', 'Low Activity', 1517],
                                ['KA7447', 'ARTESIA, UNITED STATES', 'SPRINGFIELD, UNITED STATES', 'Low Activity', 1463],
                                ['UZ4793', 'SELMER, UNITED STATES', 'NUIQSUT, UNITED STATES', 'Low Activity', 1355],
                                ['LI6241', 'MONTROSE, UNITED STATES', 'WACO, UNITED STATES', 'Low Activity', 1260],
                                ['TO8949', 'SPRINGFIELD/ CHICOPEE, UNITED STATES', 'BURLINGTON, UNITED STATES', 'Low Activity', 1194],
                                ['KU2440', 'KENNETT, UNITED STATES', 'LIVERMORE, UNITED STATES', 'Low Activity', 1169],
                                ['AF6210', 'ADA, UNITED STATES', 'CORDELE, UNITED STATES', 'Low Activity', 1130],
                                ['JO1351', 'BARTLESVILLE, UNITED STATES', 'EGEGIK, UNITED STATES', 'Low Activity', 1125],
                                ['SL4313', 'POTTSVILLE, UNITED STATES', 'GLENDALE, UNITED STATES', 'Low Activity', 1082],
                                ['BU3152', 'VICTORIA, UNITED STATES', 'SAFFORD, UNITED STATES', 'Low Activity', 1053],
                                ['CU1931', 'RALEIGH/ DURHAM, UNITED STATES', 'SAFFORD, UNITED STATES', 'Low Activity', 1044],
                                ['HO1523', 'WINCHESTER, UNITED STATES', 'ARDMORE, UNITED STATES', 'Low Activity', 1041],
                                ['NA3042', 'SANTA PAULA, UNITED STATES', 'KONGIGANAK, UNITED STATES', 'Very Low Activity', 954],
                                ['EL4980', 'WATERVILLE, UNITED STATES', 'HOQUIAM, UNITED STATES', 'Very Low Activity', 921],
                                ['PH9706', 'GREEN BAY, UNITED STATES', 'DANVILLE, UNITED STATES', 'Very Low Activity', 479]]]

        alias_counter = 0
        total_aliases = 26
        total_queries = 4

        # open the test folder and read the files inside
        if os_name == 'Windows':
            print("Windows OS Detected")
            directory = os.getcwd()
            grading_directory = os.getcwd() + '\\tempgrades'
            answer = open(f"{directory}\\week09answers.txt", "w")

        elif os_name == 'Linux':
            print("Linux Detected")
            directory = '/home/student/Desktop/itm220grading'
            grading_directory = '/home/student/Desktop/itm220grading/tempgrades'
            answer = open(f"{directory}/week09answers.txt", "w")

        elif os_name == 'Darwin':
            print("MacOS Detected")
            directory = os.getcwd()
            grading_directory = os.getcwd() + '/tempgrades'
            answer = open(f"{directory}/week09answers.txt", "w")
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
                    file_contents = file_contents.replace("WITH", "-- ~\nWITH")
                    file_contents = file_contents.replace("SELECT", "-- ~\nSELECT")
                    file_contents = file_contents.replace("(-- ~\nSELECT", "(SELECT")
                    file_contents = file_contents.replace(" -- ~\nSELECT", "SELECT")
                    file_contents = file_contents.replace(")\n-- ~\nSELECT", ")\nSELECT")
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
                        # Filter out SELECT, USE and WITH commands
                sqlCommands = [command for command in sqlCommands if (not command.lower().startswith('select *') and command.lower().startswith('select')) or command.lower().startswith('use') or command.lower().startswith('with')]
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
                query1_function_list = []
                query2_clause_list = []
                query2_function_list = []
                query3_clause_list = []
                query3_function_list = []
                query4_clause_list = []
                query4_function_list = []
                
                for command in sqlCommands:
                    a_number += 1
                    
                    # debug.write(f"Query {a_number}. {command}\n")            
                    if a_number == 1 and not command.lower().__contains__('use'):
                        answer.write(f"USE airportdb; Statement NOT FOUND\n")

                    q1_join_counter = 0
                    q1_concat_counter = 0
                    q1_date_format_counter = 0
                    if a_number == 2: # Query 1
                        if command.lower().__contains__('select'):
                            if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                                for word in command.split():
                                    if word.lower() == 'as':
                                        alias_counter += 1
                            if not command.lower().__contains__(' as '):
                                query1_clause_list.append(f"Alias NOT used")
                            if not command.lower().__contains__('from'):
                                query1_clause_list.append(f"FROM Clause NOT used")
                            if command.lower().__contains__('inner join') or command.lower().__contains__('join'):
                                for word in command.split():
                                    if word.lower() == 'inner join' or word.lower() == 'join':
                                        q1_join_counter += 1
                                if q1_join_counter < 4:
                                    query1_clause_list.append(f"Less than 4 JOIN Clauses used")
                                else:
                                    query1_clause_list.append(f"JOIN Clauses used {q1_join_counter}/4 times")
                            if not command.lower().__contains__('inner join') or not command.lower().__contains__('join'):
                                query1_clause_list.append(f"JOIN Clause NOT used")
                            if not command.lower().__contains__('where'):
                                query1_clause_list.append(f"WHERE Clause NOT used")
                            if not command.lower().__contains__('and'):
                                query1_clause_list.append(f"AND operator NOT used")
                            if not command.lower().__contains__('order by'):
                                query1_clause_list.append(f"ORDER BY Clause NOT used")
                            if command.lower().__contains__('concat'):
                                for word in command.split():
                                    if word.lower() == 'concat(ag.city,' or word.lower() == 'concat(ag2.city,':
                                        q1_concat_counter += 1
                                query1_function_list.append(f"CONCAT function used {q1_concat_counter} times")
                            if not command.lower().__contains__('concat'):
                                query1_function_list.append(f"CONCAT function NOT used")
                            if command.lower().__contains__('date_format'):
                                for word in command.split():
                                    if word.lower() == 'date_format(f.departure,' or word.lower() == 'date_format(f.arrival,':
                                        q1_date_format_counter += 1
                                if q1_date_format_counter < 2:
                                    query1_function_list.append(f"DATE_FORMAT function used less than 2 times")
                                query1_function_list.append(f"DATE_FORMAT function used {q1_date_format_counter} times")
                            if not command.lower().__contains__('date_format'):
                                query1_function_list.append(f"DATE_FORMAT function NOT used")
                            if not command.lower().__contains__('\'%b %d, %Y %h:%i %p\''):
                                query1_function_list.append(f"Date format NOT correct ('%b %d, %Y %h:%i %p')")
                    
                    q2_join_counter = 0
                    q2_concat_counter = 0
                    q2_count_counter = 0
                    q2_case_counter = 0
                    if a_number == 3: # Query 2
                        if command.lower().__contains__('select'):
                            if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                                for word in command.split():
                                    if word.lower() == 'as':
                                        alias_counter += 1
                            if not command.lower().__contains__(' as '):
                                query2_clause_list.append(f"Alias NOT used")
                            if not command.lower().__contains__('from'):
                                query2_clause_list.append(f"FROM Clause NOT used")
                            if command.lower().__contains__('inner join') or command.lower().__contains__('join'):
                                for word in command.split():
                                    if word.lower() == 'inner join' or word.lower() == 'join':
                                        q2_join_counter += 1
                                if q2_join_counter < 6:
                                    query2_clause_list.append(f"Less than 6 JOIN Clauses used")
                                else:
                                    query2_clause_list.append(f"JOIN Clauses used {q2_join_counter} times")
                            if not command.lower().__contains__('inner join') or not command.lower().__contains__('join'):
                                query2_clause_list.append(f"JOIN Clause NOT used")
                            if not command.lower().__contains__('where'):
                                query2_clause_list.append(f"WHERE Clause NOT used")
                            if not command.lower().__contains__('and'):
                                query2_clause_list.append(f"AND operator NOT used")
                            if not command.lower().__contains__('order by'):
                                query2_clause_list.append(f"ORDER BY Clause NOT used")
                            if command.lower().__contains__('concat'):
                                for word in command.split():
                                    if word.lower() == 'concat(ag.city,' or word.lower() == 'concat(ag2.city,' or word.lower() == 'concat(ap.capacity':
                                        q2_concat_counter += 1
                                query2_function_list.append(f"CONCAT function used {q2_concat_counter} times")
                            if not command.lower().__contains__('concat'):
                                query2_function_list.append(f"CONCAT function NOT used")
                            if command.lower().__contains__('count'):
                                for word in command.split():
                                    if word.lower() == 'count(b.passenger_id)' or word.lower() == '(count(b.passenger_id))' or word.lower() == '(count(b.passenger_id)' or word.lower() == '(count(b.passenger_id)),':
                                        q2_count_counter += 1
                                if q2_count_counter < 6:
                                    query2_function_list.append(f"COUNT function used less than 6 times")
                                query2_function_list.append(f"COUNT function used {q2_count_counter} times")
                            if not command.lower().__contains__('count'):
                                query2_function_list.append(f"COUNT function NOT used")
                            if command.lower().__contains__('case'):
                                for word in command.split():
                                    if word.lower() == 'case':
                                        q2_case_counter += 1
                                if q2_case_counter < 2:
                                    query2_function_list.append(f"CASE function used less than 2 times")
                                query2_function_list.append(f"CASE function used {q2_case_counter} times")

                    q3_join_counter = 0
                    q3_case_counter = 0
                    q3_sum_counter = 0
                    if a_number == 4: # Query 3
                        if command.lower().__contains__('select'):
                            if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                                for word in command.split():
                                    if word.lower() == 'as':
                                        alias_counter += 1
                            if not command.lower().__contains__(' as '):
                                query3_clause_list.append(f"Alias NOT used")
                            if not command.lower().__contains__('from'):
                                query3_clause_list.append(f"FROM Clause NOT used")
                            if command.lower().__contains__('inner join') or command.lower().__contains__('join'):
                                for word in command.split():
                                    if word.lower() == 'inner join' or word.lower() == 'join':
                                        q3_join_counter += 1
                                if q3_join_counter < 4:
                                    query3_clause_list.append(f"Less than 4 JOIN Clauses used")
                                else:
                                    query3_clause_list.append(f"JOIN Clauses used {q3_join_counter} times")
                            if not command.lower().__contains__('inner join') or not command.lower().__contains__('join'):
                                query3_clause_list.append(f"JOIN Clause NOT used")
                            if not command.lower().__contains__('where'):
                                query3_clause_list.append(f"WHERE Clause NOT used")
                            if not command.lower().__contains__('and'):
                                query3_clause_list.append(f"AND operator NOT used")
                            if command.lower().__contains__('case'):
                                for word in command.split():
                                    if word.lower() == 'sum(case':
                                        q3_case_counter += 1
                                if q3_case_counter < 7:
                                    query3_function_list.append(f"CASE function used less than 7 times")
                                query3_function_list.append(f"CASE function used {q3_case_counter} times")
                            if not command.lower().__contains__('case'):
                                query3_function_list.append(f"CASE function NOT used")
                            if command.lower().__contains__('sum'):
                                for word in command.split():
                                    if word.lower() == 'sum(case' or word.lower() == 'sum(sunday' or word.lower() == 'sum(monday' or word.lower() == 'sum(tuesday' or word.lower() == 'sum(wednesday' or word.lower() == 'sum(thursday' or word.lower() == 'sum(friday' or word.lower() == 'sum(saturday':
                                        q3_sum_counter += 1
                                if q3_sum_counter < 8:
                                    query3_function_list.append(f"SUM function used less than 8 times")
                                query3_function_list.append(f"SUM function used {q3_sum_counter} times")

                    q4_join_counter = 0
                    q4_count_counter = 0
                    q4_concat_counter = 0
                    if a_number == 5: # Query 4
                        if command.lower().__contains__('select'):
                            if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                                for word in command.split():
                                    if word.lower() == 'as':
                                        alias_counter += 1
                            if not command.lower().__contains__(' as '):
                                query4_clause_list.append(f"Alias NOT used")
                            if not command.lower().__contains__('from'):
                                query4_clause_list.append(f"FROM Clause NOT used")
                            if command.lower().__contains__('inner join') or command.lower().__contains__('join'):
                                for word in command.split():
                                    if word.lower() == 'inner join' or word.lower() == 'join':
                                        q4_join_counter += 1
                                if q4_join_counter < 5:
                                    query4_clause_list.append(f"Less than 5 JOIN Clauses used")
                                else:
                                    query4_clause_list.append(f"JOIN Clauses used {q4_join_counter} times")
                            if not command.lower().__contains__('inner join') or not command.lower().__contains__('join'):
                                query4_clause_list.append(f"JOIN Clause NOT used")
                            if not command.lower().__contains__('where'):
                                query4_clause_list.append(f"WHERE Clause NOT used")
                            if not command.lower().__contains__('and'):
                                query4_clause_list.append(f"AND operator NOT used")
                            if not command.lower().__contains__('group by'):
                                query4_clause_list.append(f"GROUP BY Clause NOT used")
                            if not command.lower().__contains__('order by'):
                                query4_clause_list.append(f"ORDER BY Clause NOT used")
                            if command.lower().__contains__('concat'):
                                for word in command.split():
                                    if word.lower() == 'concat(ag.city,' or word.lower() == 'concat(ag2.city,':
                                        q4_concat_counter += 1
                                query4_function_list.append(f"CONCAT function used {q4_concat_counter} times")
                            if not command.lower().__contains__('concat'):
                                query4_function_list.append(f"CONCAT function NOT used")
                            if command.lower().__contains__('count'):
                                for word in command.split():
                                    if word.lower() == 'count(b.passenger_id)':
                                        q4_count_counter += 1
                                if q4_count_counter < 6:
                                    query4_function_list.append(f"COUNT function used less than 6 times")
                                query4_function_list.append(f"COUNT function used {q4_count_counter} times")
                            if not command.lower().__contains__('count'):
                                query4_function_list.append(f"COUNT function NOT used")
                            


                    # pass each list to a function
                    # the function will do all the replacing and formatting
                    # then return the list
                    
                    new_query1c_list = format_list(query1_clause_list)
                    new_query1f_list = format_list(query1_function_list)
                    new_query2c_list = format_list(query2_clause_list)
                    new_query2f_list = format_list(query2_function_list)
                    new_query3c_list = format_list(query3_clause_list)
                    new_query3f_list = format_list(query3_function_list)
                    new_query4c_list = format_list(query4_clause_list)
                    new_query4f_list = format_list(query4_function_list)

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
                            # answer.write("------QUERY------\n")
                            # answer.write(f"{command}\n")
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

                            answer.write("----FUNCTIONS----\n")
                            if a_number == 2:
                                # debug.write(new_query1_list)
                                if len(new_query1f_list) != 0:
                                    answer.write(f"{new_query1f_list}\n")
                                else:
                                    answer.write(f"All functions accounted for\n")
                            if a_number == 3:
                                # debug.write(new_query2_list)
                                if len(new_query2f_list) != 0:
                                    answer.write(f"{new_query2f_list}\n")
                                else:
                                    answer.write(f"All functions accounted for\n")
                            if a_number == 4:
                                # debug.write(new_query3_list)
                                if len(new_query3f_list) != 0:
                                    answer.write(f"{new_query3f_list}\n")
                                else:
                                    answer.write(f"All functions accounted for\n")
                            if a_number == 5:
                                # debug.write(new_query4_list)
                                if len(new_query4f_list) != 0:
                                    answer.write(f"{new_query4f_list}\n")
                                else:
                                    answer.write(f"All functions accounted for\n")
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
                    os.remove(f"{directory}\\week09answers.txt")
                elif os_name == 'Linux' or os_name == 'Darwin':
                    os.remove(f"{directory}/week09answers.txt")
                print("Files Deleted")
            else:
                f.close()
                print("Files Kept")

