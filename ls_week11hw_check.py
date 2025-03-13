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
                                [
                                ['2015-06-01 16:09:00', '2015-08-31 16:09:00', '3', 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM'], 
                                ['2015-06-04 01:24:00', '2015-08-29 01:24:00', '3', 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM'], 
                                ['2015-06-04 15:59:00', '2015-08-28 15:59:00', '3', 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM']
                                ],
                                # ---------------------------------------------------------------------
                                # Question 2
                                # ---------------------------------------------------------------------
                                [
                                [39, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-01 16:09:00', 'TR4484'],
                                [29, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-03 16:09:00', 'TR4484'],
                                [75, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-04 01:24:00', 'BR4656'],
                                [196, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-05 01:24:00', 'BR4656'],
                                [31, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-06 01:24:00', 'BR4656'],
                                [31, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-08 16:09:00', 'TR4484'],
                                [67, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-10 16:09:00', 'TR4484'],
                                [43, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-11 01:24:00', 'BR4656'],
                                [208, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-12 01:24:00', 'BR4656'],
                                [60, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-13 01:24:00', 'BR4656'],
                                [24, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-15 16:09:00', 'TR4484'],
                                [35, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-17 16:09:00', 'TR4484'],
                                [54, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-18 01:24:00', 'BR4656'],
                                [65, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-19 01:24:00', 'BR4656'],
                                [79, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-20 01:24:00', 'BR4656'],
                                [37, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-22 16:09:00', 'TR4484'],
                                [40, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-24 16:09:00', 'TR4484'],
                                [162, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-25 01:24:00', 'BR4656'],
                                [206, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-26 01:24:00', 'BR4656'],
                                [80, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-27 01:24:00', 'BR4656'],
                                [204, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-06-29 16:09:00', 'TR4484'],
                                [72, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-01 16:09:00', 'TR4484'],
                                [24, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-02 01:24:00', 'BR4656'],
                                [57, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-03 01:24:00', 'BR4656'],
                                [94, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-04 01:24:00', 'BR4656'],
                                [43, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-06 16:09:00', 'TR4484'],
                                [312, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-08 16:09:00', 'TR4484'],
                                [54, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-09 01:24:00', 'BR4656'],
                                [59, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-10 01:24:00', 'BR4656'],
                                [208, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-11 01:24:00', 'BR4656'],
                                [34, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-13 16:09:00', 'TR4484'],
                                [40, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-15 16:09:00', 'TR4484'],
                                [35, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-16 01:24:00', 'BR4656'],
                                [178, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-17 01:24:00', 'BR4656'],
                                [154, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-18 01:24:00', 'BR4656'],
                                [31, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-20 16:09:00', 'TR4484'],
                                [39, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-22 16:09:00', 'TR4484'],
                                [204, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-23 01:24:00', 'BR4656'],
                                [53, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-24 01:24:00', 'BR4656'],
                                [57, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-25 01:24:00', 'BR4656'],
                                [336, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-27 16:09:00', 'TR4484'],
                                [28, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-29 16:09:00', 'TR4484'],
                                [48, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-30 01:24:00', 'BR4656'],
                                [195, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-07-31 01:24:00', 'BR4656'],
                                [214, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-01 01:24:00', 'BR4656'],
                                [340, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-03 16:09:00', 'TR4484'],
                                [25, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-05 16:09:00', 'TR4484'],
                                [28, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-06 01:24:00', 'BR4656'],
                                [195, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-07 01:24:00', 'BR4656'],
                                [67, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-08 01:24:00', 'BR4656'],
                                [75, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-10 16:09:00', 'TR4484'],
                                [182, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-12 16:09:00', 'TR4484'],
                                [56, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-13 01:24:00', 'BR4656'],
                                [70, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-14 01:24:00', 'BR4656'],
                                [157, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-15 01:24:00', 'BR4656'],
                                [185, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-17 16:09:00', 'TR4484'],
                                [310, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-19 16:09:00', 'TR4484'],
                                [25, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-20 01:24:00', 'BR4656'],
                                [44, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-21 01:24:00', 'BR4656'],
                                [75, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-22 01:24:00', 'BR4656'],
                                [164, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-24 16:09:00', 'TR4484'],
                                [22, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-26 16:09:00', 'TR4484'],
                                [42, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-27 01:24:00', 'BR4656'],
                                [190, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-28 01:24:00', 'BR4656'],
                                [193, 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-29 01:24:00', 'BR4656'],
                                [38, 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', '2015-08-31 16:09:00', 'TR4484'],
                                [44, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-06-04 15:59:00', 'NA1933'],
                                [35, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-06-05 15:59:00', 'NA1933'],
                                [85, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-06-11 15:59:00', 'NA1933'],
                                [21, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-06-12 15:59:00', 'NA1933'],
                                [298, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-06-18 15:59:00', 'NA1933'],
                                [108, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-06-19 15:59:00', 'NA1933'],
                                [196, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-06-25 15:59:00', 'NA1933'],
                                [209, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-06-26 15:59:00', 'NA1933'],
                                [106, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-07-02 15:59:00', 'NA1933'],
                                [47, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-07-03 15:59:00', 'NA1933'],
                                [85, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-07-09 15:59:00', 'NA1933'],
                                [199, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-07-10 15:59:00', 'NA1933'],
                                [55, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-07-16 15:59:00', 'NA1933'],
                                [186, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-07-17 15:59:00', 'NA1933'],
                                [49, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-07-23 15:59:00', 'NA1933'],
                                [40, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-07-24 15:59:00', 'NA1933'],
                                [164, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-07-30 15:59:00', 'NA1933'],
                                [36, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-07-31 15:59:00', 'NA1933'],
                                [25, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-08-06 15:59:00', 'NA1933'],
                                [40, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-08-07 15:59:00', 'NA1933'],
                                [180, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-08-13 15:59:00', 'NA1933'],
                                [53, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-08-14 15:59:00', 'NA1933'],
                                [38, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-08-20 15:59:00', 'NA1933'],
                                [37, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-08-21 15:59:00', 'NA1933'],
                                [186, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-08-27 15:59:00', 'NA1933'],
                                [213, 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', '2015-08-28 15:59:00', 'NA1933']
                                ],
                                # ---------------------------------------------------------------------
                                # Question 3
                                # ---------------------------------------------------------------------
                                [
                                ['$1,018,288.14', 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', 'BR4656'], 
                                ['$707,653.94', 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', 'TR4484'], 
                                ['$669,993.38', 'MANCHESTER UNITED KINGDOM', 'YEOVIL UNITED KINGDOM', 'NA1933']
                                ],
                                # ---------------------------------------------------------------------
                                # Question 4
                                # ---------------------------------------------------------------------
                                [
                                ['$254.37', 'EDINBURGH UNITED KINGDOM', 'MONA UNITED KINGDOM', 'TR4484'], 
                                ['$252.36', 'PERTH UNITED KINGDOM', 'MONA UNITED KINGDOM', 'BR4656']
                                ],
                                # ---------------------------------------------------------------------
                                # Question 5
                                # ---------------------------------------------------------------------
                                [
                                ['KI2173', 'DETROIT, UNITED STATES', 'SANTA MONICA, UNITED STATES', 'High Activity', 13787, '$3,449,706.17', '$250.21'],
                                ['SE9793', 'WILLOWS, UNITED STATES', 'TRENTON, UNITED STATES', 'High Activity', 13681, '$3,459,987.28', '$252.90'],
                                ['HU1379', 'MILLEDGEVILLE, UNITED STATES', 'NORTH EAST, UNITED STATES', 'High Activity', 12812, '$3,207,175.64', '$250.33'],
                                ['HA4967', 'JACKSON, UNITED STATES', 'PHILADELPHIA, UNITED STATES', 'High Activity', 12742, '$3,221,111.58', '$252.79'],
                                ['PO1627', 'MUSKOGEE, UNITED STATES', 'BURLINGTON, UNITED STATES', 'High Activity', 12585, '$3,162,273.90', '$251.27'],
                                ['SE2863', 'TRAVERSE CITY, UNITED STATES', 'STAUNTON-WAYNESBORO-HARRISONB*, UNITED STATES', 'High Activity', 12486, '$3,143,306.41', '$251.75'],
                                ['MA1915', 'BLACKSTONE, UNITED STATES', 'ORANGE CITY, UNITED STATES', 'High Activity', 12294, '$3,101,133.44', '$252.25'],
                                ['YU9000', 'MERRILL, UNITED STATES', 'WESTERLY, UNITED STATES', 'High Activity', 12016, '$3,032,391.01', '$252.36'],
                                ['YU7366', 'FLORA, UNITED STATES', 'MOLINE, UNITED STATES', 'High Activity', 11879, '$2,975,415.72', '$250.48'],
                                ['FA2773', 'CHOTEAU, UNITED STATES', 'ROUNDUP, UNITED STATES', 'High Activity', 11850, '$2,962,858.15', '$250.03'],
                                ['YU6410', 'MENOMINEE, UNITED STATES', 'INDIANOLA, UNITED STATES', 'High Activity', 11702, '$2,934,889.30', '$250.80'],
                                ['VA8541', 'MARYSVILLE, UNITED STATES', 'TAMPA, UNITED STATES', 'High Activity', 11395, '$2,859,118.52', '$250.91'],
                                ['ER8710', 'WARREN, UNITED STATES', 'WARROAD, UNITED STATES', 'High Activity', 11039, '$2,769,099.53', '$250.85'],
                                ['FA2056', 'VINCENNES, UNITED STATES', 'JACKSON, UNITED STATES', 'High Activity', 10773, '$2,691,266.03', '$249.82'],
                                ['PO1509', 'UTICA, UNITED STATES', 'IDAHO FALLS, UNITED STATES', 'High Activity', 10740, '$2,711,904.76', '$252.51'],
                                ['YU5775', 'CHARLOTTE, UNITED STATES', 'ANIAK, UNITED STATES', 'High Activity', 10691, '$2,685,441.61', '$251.19'],
                                ['CZ8966', 'CORONA, UNITED STATES', 'MANNING, UNITED STATES', 'High Activity', 10582, '$2,676,589.51', '$252.94'],
                                ['ET5618', 'FALLON, UNITED STATES', 'DAYTONA BEACH, UNITED STATES', 'High Activity', 10563, '$2,629,219.66', '$248.91'],
                                ['HU4662', 'EASTMAN, UNITED STATES', 'CAMP RIPLEY, UNITED STATES', 'High Activity', 10549, '$2,648,213.94', '$251.04'],
                                ['LU5617', 'CHAPPELL, UNITED STATES', 'WEST PLAINS, UNITED STATES', 'High Activity', 10537, '$2,660,048.62', '$252.45'],
                                ['MI2776', 'MOBILE, UNITED STATES', 'RED WING, UNITED STATES', 'High Activity', 10423, '$2,637,904.40', '$253.08'],
                                ['YU4735', "ST MARY'S, UNITED STATES", 'HARRISBURG, UNITED STATES', 'High Activity', 10038, '$2,524,855.98', '$251.53'],
                                ['NI3099', 'CAMP RIPLEY, UNITED STATES', 'SALT LAKE CITY, UNITED STATES', 'Medium Activity', 9907, '$2,484,543.49', '$250.79'],
                                ['ME9662', 'DE QUEEN, UNITED STATES', 'JASPER, UNITED STATES', 'Medium Activity', 9880, '$2,471,395.72', '$250.14'],
                                ['OM9293', 'MONROEVILLE, UNITED STATES', 'CAMBRIDGE, UNITED STATES', 'Medium Activity', 9828, '$2,460,646.13', '$250.37'],
                                ['YU5941', 'CELINA, UNITED STATES', 'CHARLEVOIX, UNITED STATES', 'Medium Activity', 9819, '$2,466,012.48', '$251.15'],
                                ['DE7084', 'GREENVILLE, UNITED STATES', 'DEMING, UNITED STATES', 'Medium Activity', 9735, '$2,450,783.01', '$251.75'],
                                ['MI9290', 'DAYTON, UNITED STATES', 'FRIDAY HARBOR, UNITED STATES', 'Medium Activity', 9708, '$2,437,342.06', '$251.07'],
                                ['JA2267', 'MESA, UNITED STATES', 'MANISTIQUE, UNITED STATES', 'Medium Activity', 9666, '$2,409,204.99', '$249.25'],
                                ['OM2569', 'BELUGA, UNITED STATES', 'FESTUS, UNITED STATES', 'Medium Activity', 9636, '$2,396,149.17', '$248.67'],
                                ['PE1747', 'REED CITY, UNITED STATES', 'CAMBRIDGE, UNITED STATES', 'Medium Activity', 9608, '$2,422,586.96', '$252.14'],
                                ['UK2667', 'CRESCO, UNITED STATES', 'LA JUNTA, UNITED STATES', 'Medium Activity', 9498, '$2,385,982.69', '$251.21'],
                                ['AN2405', 'CELINA, UNITED STATES', 'TUCSON, UNITED STATES', 'Medium Activity', 9489, '$2,380,764.93', '$250.90'],
                                ['LA9078', 'NAPA, UNITED STATES', 'CHARITON, UNITED STATES', 'Medium Activity', 9487, '$2,375,691.79', '$250.42'],
                                ['TO2549', 'GLENWOOD, UNITED STATES', 'DUGWAY PROVING GROUND, UNITED STATES', 'Medium Activity', 9459, '$2,362,590.47', '$249.77'],
                                ['GI1545', 'MERIDIAN, UNITED STATES', 'ANGOLA, UNITED STATES', 'Medium Activity', 9415, '$2,355,408.40', '$250.18'],
                                ['FI4432', 'MARYSVILLE, UNITED STATES', 'MOSES LAKE, UNITED STATES', 'Medium Activity', 9376, '$2,355,039.92', '$251.18'],
                                ['CH1176', 'CAPE GIRARDEAU, UNITED STATES', 'DELAWARE, UNITED STATES', 'Medium Activity', 9348, '$2,337,223.61', '$250.02'],
                                ['MI8878', 'CAMPBELLSVILLE, UNITED STATES', 'ESCANABA, UNITED STATES', 'Medium Activity', 9343, '$2,374,341.77', '$254.13'],
                                ['YE1968', 'PROVINCETOWN, UNITED STATES', 'PASO ROBLES, UNITED STATES', 'Medium Activity', 9258, '$2,311,924.42', '$249.72'],
                                ['PE7892', 'ERWIN, UNITED STATES', 'GREAT BARRINGTON, UNITED STATES', 'Medium Activity', 9182, '$2,274,766.78', '$247.74'],
                                ['BA3076', 'ROXBORO, UNITED STATES', 'LAMAR, UNITED STATES', 'Medium Activity', 9169, '$2,318,607.38', '$252.87'],
                                ['MI3896', 'OWATONNA, UNITED STATES', 'LAKEHURST, UNITED STATES', 'Medium Activity', 9151, '$2,260,830.96', '$247.06'],
                                ['ET1300', 'LEMMON, UNITED STATES', 'POMPANO BEACH, UNITED STATES', 'Medium Activity', 9009, '$2,261,058.25', '$250.98'],
                                ['BA4118', 'NEW YORK, UNITED STATES', 'HAMMOND, UNITED STATES', 'Medium Activity', 9005, '$2,278,430.64', '$253.02'],
                                ['BE6699', 'BATESVILLE, UNITED STATES', 'OCALA, UNITED STATES', 'Medium Activity', 8994, '$2,240,516.50', '$249.11'],
                                ['CZ1716', 'THOMASTON, UNITED STATES', 'ROCKDALE, UNITED STATES', 'Medium Activity', 8945, '$2,255,393.01', '$252.14'],
                                ['SE2030', 'SIOUX CENTER, UNITED STATES', 'MINNEAPOLIS, UNITED STATES', 'Medium Activity', 8914, '$2,234,815.47', '$250.71'],
                                ['KO9219', 'PITTSBURGH, UNITED STATES', 'KEY WEST, UNITED STATES', 'Medium Activity', 8907, '$2,236,647.76', '$251.11'],
                                ['LA7059', 'GARY, UNITED STATES', 'MINDEN, UNITED STATES', 'Medium Activity', 8889, '$2,227,346.70', '$250.57'],
                                ['JE5614', 'PONTIAC, UNITED STATES', 'DAVENPORT, UNITED STATES', 'Medium Activity', 8878, '$2,214,377.18', '$249.42'],
                                ['OM5436', 'WASHINGTON, UNITED STATES', 'PHILADELPHIA, UNITED STATES', 'Medium Activity', 8850, '$2,230,453.70', '$252.03'],
                                ['LI8159', 'NECEDAH, UNITED STATES', 'SPOKANE, UNITED STATES', 'Medium Activity', 8849, '$2,221,019.53', '$250.99'],
                                ['MI8337', 'ELKIN, UNITED STATES', 'CHEHALIS, UNITED STATES', 'Medium Activity', 8834, '$2,230,097.80', '$252.44'],
                                ['WA4076', 'KENOSHA, UNITED STATES', 'WICHITA, UNITED STATES', 'Medium Activity', 8783, '$2,205,742.20', '$251.14'],
                                ['IR7835', 'DECORAH, UNITED STATES', 'MT POCONO, UNITED STATES', 'Medium Activity', 8768, '$2,232,387.39', '$254.61'],
                                ['GR4548', 'VENICE, UNITED STATES', 'GREAT BEND, UNITED STATES', 'Medium Activity', 8764, '$2,205,691.78', '$251.68'],
                                ['DE4317', 'WINTER HAVEN, UNITED STATES', 'HERMISTON, UNITED STATES', 'Medium Activity', 8745, '$2,190,437.24', '$250.48'],
                                ['CZ7237', 'REDWOOD FALLS, UNITED STATES', 'CHEFORNAK, UNITED STATES', 'Medium Activity', 8739, '$2,170,178.47', '$248.33'],
                                ['AZ1358', 'PARIS, UNITED STATES', 'ALAMOGORDO, UNITED STATES', 'Medium Activity', 8710, '$2,207,807.15', '$253.48'],
                                ['PU2662', 'BISHOP, UNITED STATES', 'ANDREWS, UNITED STATES', 'Medium Activity', 8587, '$2,140,459.49', '$249.27'],
                                ['RO8923', 'ALGONA, UNITED STATES', 'RUGBY, UNITED STATES', 'Medium Activity', 8572, '$2,143,282.94', '$250.03'],
                                ['WA6519', 'BIRMINGHAM, UNITED STATES', 'WADENA, UNITED STATES', 'Medium Activity', 8545, '$2,140,846.06', '$250.54'],
                                ['IC9093', 'FT WORTH, UNITED STATES', 'TUSCALOOSA, UNITED STATES', 'Medium Activity', 8509, '$2,130,550.09', '$250.39'],
                                ['FA6442', 'MONTICELLO, UNITED STATES', 'OLYMPIA, UNITED STATES', 'Medium Activity', 8481, '$2,118,720.22', '$249.82'],
                                ['WE8883', 'SAN DIEGO, UNITED STATES', 'ATHENS, UNITED STATES', 'Medium Activity', 8467, '$2,116,134.25', '$249.93'],
                                ['PE9943', 'EMPORIA, UNITED STATES', 'SYLVANIA, UNITED STATES', 'Medium Activity', 8448, '$2,113,045.12', '$250.12'],
                                ['IR1736', 'ANDREWS, UNITED STATES', 'AKRON, UNITED STATES', 'Medium Activity', 8443, '$2,140,370.26', '$253.51'],
                                ['TU7887', 'ROCHESTER, UNITED STATES', 'NANTUCKET, UNITED STATES', 'Medium Activity', 8421, '$2,123,248.04', '$252.14'],
                                ['BU1446', 'MARSHFIELD, UNITED STATES', 'SIKESTON, UNITED STATES', 'Medium Activity', 8420, '$2,126,989.40', '$252.61'],
                                ['PU1065', 'COLUMBUS, UNITED STATES', 'OCONTO, UNITED STATES', 'Medium Activity', 8399, '$2,110,397.99', '$251.27'],
                                ['MO6027', 'WICHITA, UNITED STATES', 'WALLA WALLA, UNITED STATES', 'Medium Activity', 8383, '$2,106,558.42', '$251.29'],
                                ['KE2605', 'EASTLAND, UNITED STATES', 'DUBUQUE, UNITED STATES', 'Medium Activity', 8380, '$2,105,721.61', '$251.28'],
                                ['IS3636', 'PENSACOLA, UNITED STATES', 'DE KALB, UNITED STATES', 'Medium Activity', 8314, '$2,081,173.56', '$250.32'],
                                ['JE1595', 'AIKEN, UNITED STATES', 'GUYMON, UNITED STATES', 'Medium Activity', 8307, '$2,088,559.23', '$251.42'],
                                ['AU4085', 'CUMMING, UNITED STATES', 'HOQUIAM, UNITED STATES', 'Medium Activity', 8304, '$2,075,791.62', '$249.97'],
                                ['EG8566', 'EL DORADO, UNITED STATES', 'OTTUMWA, UNITED STATES', 'Medium Activity', 8266, '$2,059,771.72', '$249.19'],
                                ['CA6407', 'FT STEWART, UNITED STATES', 'EMPORIA, UNITED STATES', 'Medium Activity', 8238, '$2,072,785.70', '$251.61'],
                                ['YU3645', 'CLEARFIELD, UNITED STATES', 'POTEAU, UNITED STATES', 'Medium Activity', 8232, '$2,063,328.83', '$250.65'],
                                ['YU5789', 'FT BRIDGER, UNITED STATES', 'COCOA BEACH, UNITED STATES', 'Medium Activity', 8219, '$2,048,069.95', '$249.19'],
                                ['LU2246', 'SHELBYVILLE, UNITED STATES', 'CHATTANOOGA, UNITED STATES', 'Medium Activity', 8207, '$2,074,914.55', '$252.82'],
                                ['SU1676', 'DAVENPORT, UNITED STATES', 'COLORADO CITY, UNITED STATES', 'Medium Activity', 8194, '$2,075,376.05', '$253.28'],
                                ['AU6385', 'APPLE VALLEY, UNITED STATES', 'WACO, UNITED STATES', 'Medium Activity', 8131, '$2,037,814.22', '$250.62'],
                                ['SA1082', 'DECATUR, UNITED STATES', 'STANTON, UNITED STATES', 'Medium Activity', 8131, '$2,058,614.88', '$253.18'],
                                ['CH1136', 'DILLON, UNITED STATES', 'WAVERLY, UNITED STATES', 'Medium Activity', 8089, '$2,036,780.30', '$251.80'],
                                ['SA1559', 'WALLA WALLA, UNITED STATES', 'PHOENIX, UNITED STATES', 'Medium Activity', 8077, '$2,004,762.55', '$248.21'],
                                ['CO8648', 'PITTSBURG, UNITED STATES', 'BANNING, UNITED STATES', 'Medium Activity', 8074, '$2,024,266.62', '$250.71'],
                                ['TA6155', 'FLORA, UNITED STATES', 'SANTA ANA, UNITED STATES', 'Medium Activity', 8055, '$2,013,102.55', '$249.92'],
                                ['ET6479', 'MARYSVILLE, UNITED STATES', 'KAKE, UNITED STATES', 'Medium Activity', 8036, '$2,023,172.05', '$251.76'],
                                ['GR7164', 'HAWTHORNE, UNITED STATES', 'HUTCHINSON, UNITED STATES', 'Medium Activity', 8016, '$2,028,854.06', '$253.10'],
                                ['AR1842', 'SIREN, UNITED STATES', 'SALEM, UNITED STATES', 'Medium Activity', 8009, '$2,002,874.22', '$250.08'],
                                ['CH2955', 'MIDDLETON I, UNITED STATES', 'OAKLAND, UNITED STATES', 'Medium Activity', 7977, '$1,989,607.75', '$249.42'],
                                ['TA8728', 'OXFORD, UNITED STATES', 'CINCINNATI, UNITED STATES', 'Medium Activity', 7932, '$1,987,586.90', '$250.58'],
                                ['CZ2670', 'MAPLE LAKE, UNITED STATES', 'CHICAGO, UNITED STATES', 'Medium Activity', 7895, '$2,004,638.50', '$253.91'],
                                ['AN2706', 'CLEVELAND, UNITED STATES', 'HEBBRONVILLE, UNITED STATES', 'Medium Activity', 7864, '$1,971,914.66', '$250.75'],
                                ['VE9785', 'PULLMAN/ MOSCOW, UNITED STATES', 'OKLAHOMA CITY, UNITED STATES', 'Medium Activity', 7863, '$1,964,603.23', '$249.85'],
                                ['OM3770', 'PETERSBURG, UNITED STATES', 'WHITEVILLE, UNITED STATES', 'Medium Activity', 7856, '$1,968,877.15', '$250.62'],
                                ['ST1861', 'CORNELIA, UNITED STATES', 'ROSEAU, UNITED STATES', 'Medium Activity', 7853, '$1,975,083.26', '$251.51'],
                                ['EL2581', 'CHARLESTON, UNITED STATES', 'ERIE, UNITED STATES', 'Medium Activity', 7829, '$1,973,814.22', '$252.12'],
                                ['KA5277', 'SIOUX FALLS, UNITED STATES', 'OCONTO, UNITED STATES', 'Medium Activity', 7821, '$1,968,839.44', '$251.74'],
                                ['BA4153', 'ENDICOTT, UNITED STATES', 'WILLIMANTIC, UNITED STATES', 'Medium Activity', 7793, '$1,969,407.76', '$252.71'],
                                ['NO7935', 'NAPA, UNITED STATES', 'ST LOUIS, UNITED STATES', 'Medium Activity', 7762, '$1,947,119.40', '$250.85'],
                                ['LA7187', 'ROCHESTER, UNITED STATES', 'CINCINNATI, UNITED STATES', 'Medium Activity', 7754, '$1,919,604.52', '$247.56'],
                                ['SW6072', 'KOTZEBUE, UNITED STATES', 'PARSONS, UNITED STATES', 'Medium Activity', 7737, '$1,947,797.19', '$251.75'],
                                ['EG7409', 'SAGINAW, UNITED STATES', 'WAYNE, UNITED STATES', 'Medium Activity', 7697, '$1,940,692.02', '$252.14'],
                                ['UZ1338', 'MORRILTON, UNITED STATES', 'RANTOUL, UNITED STATES', 'Medium Activity', 7657, '$1,922,073.15', '$251.02'],
                                ['MY8586', 'SHEEP MOUNTAIN, UNITED STATES', 'BEATRICE, UNITED STATES', 'Medium Activity', 7622, '$1,935,013.39', '$253.87'],
                                ['IC1681', 'PENSACOLA, UNITED STATES', 'LOMPOC, UNITED STATES', 'Medium Activity', 7619, '$1,908,059.13', '$250.43'],
                                ['MY1066', 'NENANA, UNITED STATES', 'DANVILLE, UNITED STATES', 'Medium Activity', 7616, '$1,910,535.16', '$250.86'],
                                ['SP5709', 'ALAMOGORDO, UNITED STATES', 'NOVATO, UNITED STATES', 'Medium Activity', 7602, '$1,917,221.40', '$252.20'],
                                ['CY2880', 'ALABASTER, UNITED STATES', 'MARSHALLTOWN, UNITED STATES', 'Medium Activity', 7570, '$1,884,173.08', '$248.90'],
                                ['BH8009', 'TOLEDO, UNITED STATES', 'MOLOKAI, HAWAII, UNITED STATES', 'Medium Activity', 7569, '$1,911,044.55', '$252.48'],
                                ['UK4877', 'HUNTSVILLE, UNITED STATES', 'MACON, UNITED STATES', 'Medium Activity', 7564, '$1,915,971.90', '$253.30'],
                                ['SU1328', 'BATTLE MOUNTAIN, UNITED STATES', 'ALEXANDER CITY, UNITED STATES', 'Medium Activity', 7529, '$1,889,547.70', '$250.97'],
                                ['CZ2050', 'LAS VEGAS, UNITED STATES', 'FRANKLIN, UNITED STATES', 'Medium Activity', 7519, '$1,869,171.70', '$248.59'],
                                ['EG7584', 'BROKEN BOW, UNITED STATES', 'HOPKINSVILLE, UNITED STATES', 'Medium Activity', 7510, '$1,896,194.63', '$252.49'],
                                ['RW1474', 'FARMINGDALE, UNITED STATES', 'DOUGLAS BISBEE, UNITED STATES', 'Medium Activity', 7496, '$1,903,040.43', '$253.87'],
                                ['AU4409', 'LYONS, UNITED STATES', 'READING, UNITED STATES', 'Medium Activity', 7490, '$1,903,178.42', '$254.10'],
                                ['HO7035', 'RUSSELL, UNITED STATES', 'NORWOOD, UNITED STATES', 'Medium Activity', 7488, '$1,889,046.82', '$252.28'],
                                ['SU8712', 'WASKISH, UNITED STATES', 'RIVERTON, UNITED STATES', 'Medium Activity', 7456, '$1,866,152.69', '$250.29'],
                                ['EL6868', 'ROCHESTER, UNITED STATES', 'LEXINGTON, UNITED STATES', 'Medium Activity', 7454, '$1,872,774.88', '$251.24'],
                                ['AF5675', 'RALEIGH/ DURHAM, UNITED STATES', 'ROCKPORT, UNITED STATES', 'Medium Activity', 7445, '$1,869,398.69', '$251.09'],
                                ['KI8766', 'FT RUCKER, UNITED STATES', 'CRYSTAL RIVER, UNITED STATES', 'Medium Activity', 7445, '$1,887,551.50', '$253.53'],
                                ['CZ9540', 'SANDERSVILLE, UNITED STATES', 'UPLAND, UNITED STATES', 'Medium Activity', 7421, '$1,846,823.66', '$248.86'],
                                ['DA9563', 'LE MARS, UNITED STATES', 'BATAVIA, UNITED STATES', 'Medium Activity', 7418, '$1,864,024.69', '$251.28'],
                                ['OM1698', 'FERGUS FALLS, UNITED STATES', 'SHERIDAN, UNITED STATES', 'Medium Activity', 7409, '$1,860,489.18', '$251.11'],
                                ['TH4435', 'SUSSEX, UNITED STATES', 'OLIVIA, UNITED STATES', 'Medium Activity', 7389, '$1,840,855.44', '$249.13'],
                                ['UN1107', 'FITCHBURG, UNITED STATES', 'ATLANTA, UNITED STATES', 'Medium Activity', 7382, '$1,862,945.30', '$252.36'],
                                ['AM9379', 'LEMMON, UNITED STATES', 'GRUNDY, UNITED STATES', 'Medium Activity', 7364, '$1,851,398.17', '$251.41'],
                                ['SW4247', 'EASTPORT, UNITED STATES', 'NEW PHILADELPHIA, UNITED STATES', 'Medium Activity', 7360, '$1,879,776.29', '$255.40'],
                                ['KE8199', 'PORT HEIDEN, UNITED STATES', 'MELBOURNE, UNITED STATES', 'Medium Activity', 7351, '$1,854,557.20', '$252.29'],
                                ['RU4766', 'FRANKLIN, UNITED STATES', 'DELTA, UNITED STATES', 'Medium Activity', 7350, '$1,836,552.11', '$249.87'],
                                ['DJ8160', 'ALTUS, UNITED STATES', 'WEST BEND, UNITED STATES', 'Medium Activity', 7344, '$1,829,897.98', '$249.17'],
                                ['CE1110', 'FAIRFIELD, UNITED STATES', 'OLNEY, UNITED STATES', 'Medium Activity', 7315, '$1,837,905.71', '$251.25'],
                                ['GR8934', 'RIDGELY, UNITED STATES', 'SIERRA ARMY DEPOT, UNITED STATES', 'Medium Activity', 7302, '$1,857,024.10', '$254.32'],
                                ['WE4320', 'MARTINSBURG, UNITED STATES', 'SARASOTA/ BRADENTON, UNITED STATES', 'Medium Activity', 7293, '$1,831,232.23', '$251.09'],
                                ['CR6390', 'BRIGHAM CITY, UNITED STATES', 'HETTINGER, UNITED STATES', 'Medium Activity', 7290, '$1,814,886.78', '$248.96'],
                                ['AR8197', 'APPLETON, UNITED STATES', 'FT LAUDERDALE, UNITED STATES', 'Medium Activity', 7268, '$1,851,206.67', '$254.71'],
                                ['ER4338', 'KAMUELA, UNITED STATES', 'GLENS FALLS, UNITED STATES', 'Medium Activity', 7259, '$1,816,772.83', '$250.28'],
                                ['ZI8976', 'GAINESVILLE, UNITED STATES', 'MISSOULA, UNITED STATES', 'Medium Activity', 7248, '$1,817,133.95', '$250.71'],
                                ['AM6317', 'REEDSVILLE, UNITED STATES', 'BRIDGEWATER, UNITED STATES', 'Medium Activity', 7229, '$1,828,179.29', '$252.90'],
                                ['AL6672', 'FT BRAGG, UNITED STATES', 'FRONT ROYAL, UNITED STATES', 'Medium Activity', 7214, '$1,793,660.79', '$248.64'],
                                ['ZI6264', 'EAST HAMPTON, UNITED STATES', 'HAYWARD, UNITED STATES', 'Medium Activity', 7198, '$1,793,878.85', '$249.22'],
                                ['DJ1059', 'FRANKFORT, UNITED STATES', 'HARRISBURG, UNITED STATES', 'Medium Activity', 7190, '$1,805,537.76', '$251.12'],
                                ['ES6187', 'CRETE, UNITED STATES', 'ORLANDO, UNITED STATES', 'Medium Activity', 7178, '$1,811,863.51', '$252.42'],
                                ['DO7105', 'AFTON, UNITED STATES', 'NEW BERN, UNITED STATES', 'Medium Activity', 7159, '$1,795,326.52', '$250.78'],
                                ['CZ5688', 'SAN MARCOS, UNITED STATES', 'BROOKSVILLE, UNITED STATES', 'Medium Activity', 7158, '$1,801,656.40', '$251.70'],
                                ['BU5810', 'COMPTON, UNITED STATES', 'LONGVILLE, UNITED STATES', 'Medium Activity', 7130, '$1,788,261.93', '$250.81'],
                                ['CU2020', 'RANTOUL, UNITED STATES', 'GREENVILLE, UNITED STATES', 'Medium Activity', 7125, '$1,777,006.77', '$249.40'],
                                ['IS5932', 'BARTOW, UNITED STATES', 'RUSH CITY, UNITED STATES', 'Medium Activity', 7118, '$1,796,750.26', '$252.42'],
                                ['TH1991', 'BROOKINGS, UNITED STATES', 'ROUNDUP, UNITED STATES', 'Medium Activity', 7109, '$1,793,506.36', '$252.29'],
                                ['TR3103', 'ORLANDO, UNITED STATES', 'DETROIT LAKES, UNITED STATES', 'Medium Activity', 7094, '$1,788,666.61', '$252.14'],
                                ['CY1488', 'BRUNSWICK, UNITED STATES', 'ORD, UNITED STATES', 'Medium Activity', 7092, '$1,764,888.95', '$248.86'],
                                ['BR1926', 'LOGAN, UNITED STATES', 'KEARNEY, UNITED STATES', 'Medium Activity', 7084, '$1,777,851.57', '$250.97'],
                                ['AU9197', 'RUTHERFORDTON, UNITED STATES', 'FAIRFIELD, UNITED STATES', 'Medium Activity', 7061, '$1,763,051.47', '$249.69'],
                                ['ER1039', 'UNALAKLEET, UNITED STATES', 'ROBINSON, UNITED STATES', 'Medium Activity', 7060, '$1,788,483.95', '$253.33'],
                                ['DJ2862', 'MYRTLE BEACH, UNITED STATES', 'INDIANAPOLIS, UNITED STATES', 'Medium Activity', 7043, '$1,767,950.21', '$251.02'],
                                ['RU9151', 'GAITHERSBURG, UNITED STATES', 'OGDENSBURG, UNITED STATES', 'Medium Activity', 7029, '$1,751,453.62', '$249.18'],
                                ['SO8920', 'ST INIGOES, UNITED STATES', 'VAN NUYS, UNITED STATES', 'Medium Activity', 6999, '$1,759,685.08', '$251.42'],
                                ['EL2769', 'HARTFORD, UNITED STATES', 'STUTTGART, UNITED STATES', 'Medium Activity', 6984, '$1,759,493.67', '$251.93'],
                                ['JE9502', 'NAPA, UNITED STATES', 'HARRISON, UNITED STATES', 'Medium Activity', 6983, '$1,742,498.48', '$249.53'],
                                ['CO3502', 'CHARLEVOIX, UNITED STATES', 'SAN ANDREAS, UNITED STATES', 'Medium Activity', 6953, '$1,741,805.50', '$250.51'],
                                ['NA8198', 'WILKES-BARRE, UNITED STATES', 'MINNEAPOLIS, UNITED STATES', 'Medium Activity', 6949, '$1,729,741.24', '$248.92'],
                                ['YU1039', 'GRIFFIN, UNITED STATES', 'FT COLLINS-LOVELAND, UNITED STATES', 'Medium Activity', 6929, '$1,743,378.86', '$251.61'],
                                ['YE1695', 'WAGNER, UNITED STATES', 'FREEPORT, UNITED STATES', 'Medium Activity', 6926, '$1,717,048.05', '$247.91'],
                                ['SW5037', 'PORTERVILLE, UNITED STATES', 'LAKELAND, UNITED STATES', 'Medium Activity', 6880, '$1,729,913.93', '$251.44'],
                                ['SW2230', 'BILOXI, UNITED STATES', 'WISCASSET, UNITED STATES', 'Medium Activity', 6872, '$1,718,825.06', '$250.12'],
                                ['SE9624', 'GOSHEN, UNITED STATES', 'PONTIAC, UNITED STATES', 'Medium Activity', 6855, '$1,742,102.00', '$254.14'],
                                ['UN6147', 'KNOB NOSTER, UNITED STATES', 'DAHLGREN, UNITED STATES', 'Medium Activity', 6824, '$1,702,259.49', '$249.45'],
                                ['WA9878', 'SCAPPOOSE, UNITED STATES', 'BURNS, UNITED STATES', 'Medium Activity', 6820, '$1,701,482.88', '$249.48'],
                                ['PE6721', 'ALBANY, UNITED STATES', 'BEAUFORT, UNITED STATES', 'Medium Activity', 6813, '$1,698,247.82', '$249.27'],
                                ['ER3915', 'CAPE NEWENHAM, UNITED STATES', 'GRAND RAPIDS, UNITED STATES', 'Medium Activity', 6804, '$1,708,490.72', '$251.10'],
                                ['BA5867', 'MINOT, UNITED STATES', 'WASHINGTON, UNITED STATES', 'Medium Activity', 6801, '$1,702,256.99', '$250.30'],
                                ['VI4917', 'OAK ISLAND, UNITED STATES', 'YAKIMA, UNITED STATES', 'Medium Activity', 6790, '$1,699,639.46', '$250.32'],
                                ['IR8147', 'BATTLE CREEK, UNITED STATES', 'DELAWARE, UNITED STATES', 'Medium Activity', 6787, '$1,709,413.00', '$251.87'],
                                ['MA1427', 'FREMONT, UNITED STATES', 'HERMISTON, UNITED STATES', 'Medium Activity', 6730, '$1,678,813.89', '$249.45'],
                                ['SU2268', 'LAKE CHARLES, UNITED STATES', 'MIDDLETON I, UNITED STATES', 'Medium Activity', 6689, '$1,680,382.21', '$251.22'],
                                ['UR5878', 'GAINESVILLE, UNITED STATES', 'ADA, UNITED STATES', 'Medium Activity', 6674, '$1,659,952.89', '$248.72'],
                                ['TR3884', 'SAN MARCOS, UNITED STATES', 'MITCHELL, UNITED STATES', 'Medium Activity', 6667, '$1,682,324.83', '$252.34'],
                                ['TR7790', 'MOUNTAIN VIEW, UNITED STATES', 'DULUTH, UNITED STATES', 'Medium Activity', 6642, '$1,684,745.52', '$253.65'],
                                ['CR1931', 'HEMET, UNITED STATES', 'THERMOPOLIS, UNITED STATES', 'Medium Activity', 6641, '$1,665,666.55', '$250.82'],
                                ['NA7435', 'SEDONA, UNITED STATES', 'BATTLE CREEK, UNITED STATES', 'Medium Activity', 6635, '$1,658,467.98', '$249.96'],
                                ['ES1054', 'FREDERICK, UNITED STATES', 'FARMINGTON, UNITED STATES', 'Medium Activity', 6617, '$1,649,758.45', '$249.32'],
                                ['UN1633', 'KNOB NOSTER, UNITED STATES', 'PONCA CITY, UNITED STATES', 'Medium Activity', 6613, '$1,657,797.16', '$250.69'],
                                ['DE4536', 'GUTHRIE, UNITED STATES', 'SAULT STE MARIE, UNITED STATES', 'Medium Activity', 6598, '$1,654,323.40', '$250.73'],
                                ['MY6003', 'HOLYOKE, UNITED STATES', 'LYONS, UNITED STATES', 'Medium Activity', 6586, '$1,652,060.66', '$250.84'],
                                ['AR9453', 'LITTLE FALLS, UNITED STATES', 'HOUSTON, UNITED STATES', 'Medium Activity', 6578, '$1,663,295.34', '$252.86'],
                                ['HA7134', 'OTTAWA, UNITED STATES', 'NEW YORK, UNITED STATES', 'Medium Activity', 6552, '$1,637,183.54', '$249.88'],
                                ['KO4843', 'CALEDONIA, UNITED STATES', 'NASHVILLE, UNITED STATES', 'Medium Activity', 6520, '$1,643,360.10', '$252.05'],
                                ['FA1933', 'MILWAUKEE, UNITED STATES', 'SPRINGFIELD, UNITED STATES', 'Medium Activity', 6515, '$1,617,835.68', '$248.32'],
                                ['GA4322', 'JACKSONVILLE, UNITED STATES', 'NORFOLK, UNITED STATES', 'Medium Activity', 6511, '$1,648,920.60', '$253.25'],
                                ['UK2951', 'DRUMMOND, UNITED STATES', 'ALLIANCE, UNITED STATES', 'Medium Activity', 6480, '$1,641,907.46', '$253.38'],
                                ['RE8542', 'MULLEN, UNITED STATES', 'CRAIG, UNITED STATES', 'Medium Activity', 6478, '$1,632,053.63', '$251.94'],
                                ['AU7110', 'MARATHON, UNITED STATES', 'SHISHMAREF, UNITED STATES', 'Medium Activity', 6464, '$1,622,054.69', '$250.94'],
                                ['IN4127', 'SULLIVAN, UNITED STATES', 'JACKSONVILLE, UNITED STATES', 'Medium Activity', 6455, '$1,606,703.35', '$248.91'],
                                ['IN6795', 'OAHU, UNITED STATES', 'VANDALIA, UNITED STATES', 'Medium Activity', 6425, '$1,624,828.40', '$252.89'],
                                ['SI6262', 'DECORAH, UNITED STATES', 'KAPOLEI, UNITED STATES', 'Medium Activity', 6406, '$1,599,907.27', '$249.75'],
                                ['AN8979', 'CHANDLER, UNITED STATES', 'WARROAD, UNITED STATES', 'Medium Activity', 6393, '$1,609,638.98', '$251.78'],
                                ['AZ8820', 'SEVIERVILLE, UNITED STATES', 'HAINES, UNITED STATES', 'Medium Activity', 6377, '$1,603,273.22', '$251.41'],
                                ['UR4131', 'BALTIMORE, UNITED STATES', 'MONTROSE, UNITED STATES', 'Medium Activity', 6373, '$1,607,264.20', '$252.20'],
                                ['LA1237', 'ALBUQUERQUE, UNITED STATES', 'CHARLES CITY, UNITED STATES', 'Medium Activity', 6334, '$1,608,036.79', '$253.87'],
                                ['NO9525', 'WATERTOWN, UNITED STATES', 'WALNUT RIDGE, UNITED STATES', 'Medium Activity', 6287, '$1,568,990.30', '$249.56'],
                                ['JO9003', 'ROSEBURG, UNITED STATES', 'MILLEDGEVILLE, UNITED STATES', 'Medium Activity', 6285, '$1,578,704.16', '$251.19'],
                                ['IT1776', 'HENDERSON, UNITED STATES', 'HOOPER BAY, UNITED STATES', 'Medium Activity', 6268, '$1,590,556.70', '$253.76'],
                                ['ZI3151', 'BRUNSWICK, UNITED STATES', 'CAMP ROBINSON, UNITED STATES', 'Medium Activity', 6267, '$1,555,642.04', '$248.23'],
                                ['GH8991', 'KAUNAKAKAI, UNITED STATES', 'GAITHERSBURG, UNITED STATES', 'Medium Activity', 6265, '$1,584,718.57', '$252.95'],
                                ['RO4754', 'COLUMBUS-W POINT-STARKVILLE, UNITED STATES', 'SALLISAW, UNITED STATES', 'Medium Activity', 6253, '$1,547,050.36', '$247.41'],
                                ['CU2063', 'WICHITA, UNITED STATES', 'PAXSON, UNITED STATES', 'Medium Activity', 6249, '$1,557,023.15', '$249.16'],
                                ['VE3232', 'MALDEN, UNITED STATES', 'TAMPA, UNITED STATES', 'Medium Activity', 6247, '$1,576,838.86', '$252.42'],
                                ['JO1759', 'GREELEY, UNITED STATES', 'PONTIAC, UNITED STATES', 'Medium Activity', 6230, '$1,563,678.92', '$250.99'],
                                ['UN5290', 'ATOKA, UNITED STATES', 'HAVRE, UNITED STATES', 'Medium Activity', 6224, '$1,585,599.13', '$254.76'],
                                ['IV5446', 'SUMMERSVILLE, UNITED STATES', 'ALTUS, UNITED STATES', 'Medium Activity', 6222, '$1,585,591.56', '$254.84'],
                                ['OM5991', 'LEMOORE, UNITED STATES', 'CHARLEVOIX, UNITED STATES', 'Medium Activity', 6221, '$1,564,525.06', '$251.49'],
                                ['SO7743', 'COLUMBUS, UNITED STATES', 'CHEROKEE, UNITED STATES', 'Medium Activity', 6204, '$1,577,730.75', '$254.31'],
                                ['KY4949', 'FALLON, UNITED STATES', 'BROOKSVILLE, UNITED STATES', 'Medium Activity', 6189, '$1,558,291.06', '$251.78'],
                                ['TO5208', 'TEKAMAH, UNITED STATES', 'GRAND PRAIRIE, UNITED STATES', 'Medium Activity', 6160, '$1,554,075.25', '$252.28'],
                                ['UG7248', 'CHICAGO/ PROSPECT HGTS/ WHEELI, UNITED STATES', 'ANGOLA, UNITED STATES', 'Medium Activity', 6159, '$1,547,958.13', '$251.33'],
                                ['MO7962', 'LAKE CITY, UNITED STATES', 'HARRISBURG, UNITED STATES', 'Medium Activity', 6155, '$1,537,778.51', '$249.84'],
                                ['UG3109', 'SAN FRANCISCO, UNITED STATES', 'BENTON HARBOR, UNITED STATES', 'Medium Activity', 6140, '$1,535,463.51', '$250.08'],
                                ['QA1273', 'PAXSON, UNITED STATES', 'SOUTH LAKE TAHOE, UNITED STATES', 'Medium Activity', 6111, '$1,529,739.25', '$250.33'],
                                ['SA8177', "O'NEILL, UNITED STATES", 'PASCAGOULA, UNITED STATES', 'Medium Activity', 6110, '$1,546,738.52', '$253.15'],
                                ['WA4222', 'LOST RIVER, UNITED STATES', 'MORRISVILLE, UNITED STATES', 'Medium Activity', 6093, '$1,533,966.84', '$251.76'],
                                ['GH1728', 'EAGLE, UNITED STATES', 'ARDMORE, UNITED STATES', 'Medium Activity', 6076, '$1,533,074.92', '$252.32'],
                                ['WA1665', 'SAGINAW, UNITED STATES', 'PARKERSBURG, UNITED STATES', 'Medium Activity', 6069, '$1,528,746.09', '$251.89'],
                                ['AM5320', 'AUSTIN, UNITED STATES', 'ODESSA, UNITED STATES', 'Medium Activity', 6065, '$1,522,223.26', '$250.98'],
                                ['MO5174', 'WABASH, UNITED STATES', 'SEWARD, UNITED STATES', 'Medium Activity', 6050, '$1,512,920.86', '$250.07'],
                                ['IT7474', 'NORFOLK, UNITED STATES', 'BINGHAMTON, UNITED STATES', 'Medium Activity', 6043, '$1,528,656.43', '$252.96'],
                                ['MY1319', 'MINOT, UNITED STATES', 'MOULTRIE, UNITED STATES', 'Medium Activity', 6039, '$1,525,639.38', '$252.63'],
                                ['RU7114', 'BAD AXE, UNITED STATES', 'OAK ISLAND, UNITED STATES', 'Medium Activity', 6019, '$1,501,993.81', '$249.54'],
                                ['NA8789', 'PORTLAND, UNITED STATES', 'PETERSBURG, UNITED STATES', 'Medium Activity', 6012, '$1,528,165.70', '$254.19'],
                                ['DJ4637', 'TAMPA, UNITED STATES', 'JESUP, UNITED STATES', 'Medium Activity', 5974, '$1,506,895.89', '$252.24'],
                                ['ES8845', 'OROVILLE, UNITED STATES', 'ST FRANCIS, UNITED STATES', 'Medium Activity', 5974, '$1,514,356.43', '$253.49'],
                                ['TA7838', 'ST GEORGE, UNITED STATES', 'LIVERMORE, UNITED STATES', 'Medium Activity', 5964, '$1,512,431.05', '$253.59'],
                                ['SE1211', 'DODGE CITY, UNITED STATES', 'PROVIDENCE, UNITED STATES', 'Medium Activity', 5950, '$1,476,600.86', '$248.17'],
                                ['BR8974', 'DELANO, UNITED STATES', 'PEORIA, UNITED STATES', 'Medium Activity', 5948, '$1,512,858.53', '$254.35'],
                                ['CR2424', 'DANVILLE, UNITED STATES', 'BLYTHE, UNITED STATES', 'Medium Activity', 5943, '$1,499,126.74', '$252.25'],
                                ['GA8856', 'KOKOMO, UNITED STATES', 'SAND POINT, UNITED STATES', 'Medium Activity', 5933, '$1,474,710.28', '$248.56'],
                                ['SP5726', 'LYNCHBURG, UNITED STATES', 'PLATINUM, UNITED STATES', 'Medium Activity', 5925, '$1,488,258.54', '$251.18'],
                                ['VE1320', 'NORTH MYRTLE BEACH, UNITED STATES', 'DAHLGREN, UNITED STATES', 'Medium Activity', 5896, '$1,488,565.16', '$252.47'],
                                ['CE1850', 'SHELL LAKE, UNITED STATES', 'ST PAUL I, UNITED STATES', 'Medium Activity', 5884, '$1,468,781.40', '$249.62'],
                                ['SR1923', 'HANKSVILLE, UNITED STATES', 'MOKAPU, UNITED STATES', 'Medium Activity', 5873, '$1,457,343.81', '$248.14'],
                                ['AF5169', 'INDIANAPOLIS, UNITED STATES', 'MOSINEE, UNITED STATES', 'Medium Activity', 5867, '$1,482,913.74', '$252.76'],
                                ['JA1317', 'FT HOOD, UNITED STATES', 'CORVALLIS, UNITED STATES', 'Medium Activity', 5836, '$1,470,257.38', '$251.93'],
                                ['CO4638', 'DETROIT-GROSSE ILE, UNITED STATES', 'SAND POINT, UNITED STATES', 'Medium Activity', 5813, '$1,445,048.32', '$248.59'],
                                ['TA1877', 'MITCHELL, UNITED STATES', 'LIVINGSTON, UNITED STATES', 'Medium Activity', 5809, '$1,452,566.46', '$250.05'],
                                ['AL8474', 'ANCHORAGE, UNITED STATES', 'IOWA CITY, UNITED STATES', 'Medium Activity', 5798, '$1,470,697.30', '$253.66'],
                                ['MI3429', 'ALBION, UNITED STATES', 'MARION-WYTHEVILLE, UNITED STATES', 'Medium Activity', 5796, '$1,462,826.22', '$252.39'],
                                ['CY4389', 'ALMA, UNITED STATES', 'COOK, UNITED STATES', 'Medium Activity', 5780, '$1,430,678.06', '$247.52'],
                                ['EG6927', 'PORTLAND, UNITED STATES', 'GREENVILLE, UNITED STATES', 'Medium Activity', 5780, '$1,456,855.94', '$252.05'],
                                ['FA7732', 'GLADWIN, UNITED STATES', 'SPOKANE, UNITED STATES', 'Medium Activity', 5747, '$1,459,212.71', '$253.91'],
                                ['KO1764', 'SEVIERVILLE, UNITED STATES', 'BRIGHAM CITY, UNITED STATES', 'Medium Activity', 5730, '$1,441,706.47', '$251.61'],
                                ['DA2455', 'KIDRON, UNITED STATES', 'MONTROSE, UNITED STATES', 'Medium Activity', 5719, '$1,459,858.60', '$255.26'],
                                ['DE1609', 'MANASSAS, UNITED STATES', 'OROVILLE, UNITED STATES', 'Medium Activity', 5717, '$1,418,848.93', '$248.18'],
                                ['TR6023', 'IDA GROVE, UNITED STATES', 'IMPERIAL, UNITED STATES', 'Medium Activity', 5716, '$1,431,680.66', '$250.47'],
                                ['TH8111', 'ALEXANDRIA, UNITED STATES', 'EAU CLAIRE, UNITED STATES', 'Medium Activity', 5705, '$1,441,017.87', '$252.59'],
                                ['UR1624', 'AMERY, UNITED STATES', 'MISSOULA, UNITED STATES', 'Medium Activity', 5692, '$1,421,498.26', '$249.74'],
                                ['KY7837', 'SALT LAKE CITY, UNITED STATES', 'POTTSTOWN, UNITED STATES', 'Medium Activity', 5682, '$1,426,654.84', '$251.08'],
                                ['SA8852', 'MARSHALL, UNITED STATES', 'PONTIAC, UNITED STATES', 'Medium Activity', 5646, '$1,398,722.30', '$247.74'],
                                ['CY1964', 'KOKOMO, UNITED STATES', 'BALTIMORE, UNITED STATES', 'Medium Activity', 5643, '$1,418,898.09', '$251.44'],
                                ['NA3144', 'CODY, UNITED STATES', 'CHEFORNAK, UNITED STATES', 'Medium Activity', 5627, '$1,404,558.47', '$249.61'],
                                ['TO1460', 'ALBION, UNITED STATES', 'SHELBY, UNITED STATES', 'Medium Activity', 5627, '$1,425,418.36', '$253.32'],
                                ['RO4820', 'ORLANDO, UNITED STATES', 'BURBANK, UNITED STATES', 'Medium Activity', 5624, '$1,410,433.26', '$250.79'],
                                ['LE1327', 'COFFEYVILLE, UNITED STATES', 'DUBUQUE, UNITED STATES', 'Medium Activity', 5621, '$1,387,030.19', '$246.76'],
                                ['AL1547', 'ROCKY MOUNT, UNITED STATES', 'MINNEAPOLIS, UNITED STATES', 'Medium Activity', 5612, '$1,399,790.19', '$249.43'],
                                ['VE1350', 'ROCKPORT, UNITED STATES', 'MIAMI, UNITED STATES', 'Medium Activity', 5610, '$1,396,017.62', '$248.84'],
                                ['NA3702', 'TWENTYNINE PALMS, UNITED STATES', 'PARK FALLS, UNITED STATES', 'Medium Activity', 5606, '$1,416,621.81', '$252.70'],
                                ['RU7901', 'ROME, UNITED STATES', 'CARTERSVILLE, UNITED STATES', 'Medium Activity', 5601, '$1,402,004.16', '$250.31'],
                                ['NA1312', 'LANCASTER, UNITED STATES', 'SANTA FE, UNITED STATES', 'Medium Activity', 5597, '$1,417,999.75', '$253.35'],
                                ['GE2570', 'DWIGHT, UNITED STATES', 'WICHITA, UNITED STATES', 'Medium Activity', 5579, '$1,393,559.65', '$249.79'],
                                ['FA5517', 'MC RAE, UNITED STATES', 'DILLINGHAM, UNITED STATES', 'Medium Activity', 5568, '$1,389,278.53', '$249.51'],
                                ['WA1176', 'WILLOUGHBY, UNITED STATES', 'SPARTANBURG, UNITED STATES', 'Medium Activity', 5565, '$1,402,183.92', '$251.96'],
                                ['MI1413', 'BAKER CITY, UNITED STATES', 'WATONGA, UNITED STATES', 'Medium Activity', 5547, '$1,391,413.55', '$250.84'],
                                ['ST8898', 'LAS CRUCES, UNITED STATES', 'ARCO, UNITED STATES', 'Medium Activity', 5535, '$1,367,088.06', '$246.99'],
                                ['FI7683', 'HAMMOND, UNITED STATES', 'HAZLETON, UNITED STATES', 'Medium Activity', 5500, '$1,374,999.42', '$250.00'],
                                ['WE7788', 'SHENANDOAH, UNITED STATES', 'FITCHBURG, UNITED STATES', 'Medium Activity', 5499, '$1,384,587.33', '$251.79'],
                                ['UG5815', 'OTTAWA, UNITED STATES', 'MONTICELLO, UNITED STATES', 'Medium Activity', 5493, '$1,379,665.14', '$251.17'],
                                ['HU1082', 'LANCASTER, UNITED STATES', 'FOREST CITY, UNITED STATES', 'Medium Activity', 5487, '$1,357,833.27', '$247.46'],
                                ['AR8607', 'MARION, UNITED STATES', 'CLAY CENTER, UNITED STATES', 'Medium Activity', 5453, '$1,370,615.34', '$251.35'],
                                ['ET1007', 'FT WORTH, UNITED STATES', 'BIRCHWOOD, UNITED STATES', 'Medium Activity', 5451, '$1,374,407.38', '$252.14'],
                                ['SO8504', 'ASH FLAT, UNITED STATES', 'LANCASTER, UNITED STATES', 'Medium Activity', 5444, '$1,368,065.24', '$251.30'],
                                ['YE8116', 'WISCASSET, UNITED STATES', 'KEENE, UNITED STATES', 'Medium Activity', 5421, '$1,371,565.89', '$253.01'],
                                ['SP5715', 'YANKTON, UNITED STATES', 'SAN ANTONIO, UNITED STATES', 'Medium Activity', 5416, '$1,334,799.41', '$246.45'],
                                ['UK4314', 'JACKSON, UNITED STATES', 'HANCOCK, UNITED STATES', 'Medium Activity', 5416, '$1,360,583.33', '$251.22'],
                                ['LU2432', 'MANISTIQUE, UNITED STATES', 'AHOSKIE, UNITED STATES', 'Medium Activity', 5402, '$1,365,293.57', '$252.74'],
                                ['RE6294', 'PITTSBURG, UNITED STATES', 'WESTMINSTER, UNITED STATES', 'Medium Activity', 5388, '$1,350,675.50', '$250.68'],
                                ['MA6003', 'HARLAN, UNITED STATES', 'TWIN FALLS, UNITED STATES', 'Medium Activity', 5384, '$1,355,781.73', '$251.82'],
                                ['LU5657', 'WAUCHULA, UNITED STATES', 'NORFOLK, UNITED STATES', 'Medium Activity', 5358, '$1,332,901.43', '$248.77'],
                                ['BU4491', 'TANANA, UNITED STATES', 'FESTUS, UNITED STATES', 'Medium Activity', 5345, '$1,328,411.83', '$248.53'],
                                ['KI9835', 'JACKSON, UNITED STATES', 'FARIBAULT, UNITED STATES', 'Medium Activity', 5336, '$1,332,968.61', '$249.81'],
                                ['TA8715', 'KEY WEST, UNITED STATES', 'SPENCER, UNITED STATES', 'Medium Activity', 5324, '$1,341,810.98', '$252.03'],
                                ['QA4904', 'NASHVILLE, UNITED STATES', 'BOUNTIFUL, UNITED STATES', 'Medium Activity', 5309, '$1,332,741.92', '$251.03'],
                                ['AZ1323', 'WORTHINGTON, UNITED STATES', 'PENSACOLA, UNITED STATES', 'Medium Activity', 5306, '$1,311,287.48', '$247.13'],
                                ['HA9884', 'PENN YAN, UNITED STATES', 'TOMS RIVER, UNITED STATES', 'Medium Activity', 5305, '$1,339,440.35', '$252.49'],
                                ['MO3131', 'COLUMBUS, UNITED STATES', 'KNOXVILLE, UNITED STATES', 'Medium Activity', 5301, '$1,321,754.34', '$249.34'],
                                ['YE3740', 'SELINSGROVE, UNITED STATES', 'SAN DIEGO, UNITED STATES', 'Medium Activity', 5281, '$1,314,385.58', '$248.89'],
                                ['CU2802', 'KEMMERER, UNITED STATES', 'TIN CITY, UNITED STATES', 'Medium Activity', 5216, '$1,313,226.96', '$251.77'],
                                ['SE7649', 'WINCHESTER, UNITED STATES', 'DECATUR, UNITED STATES', 'Medium Activity', 5214, '$1,298,009.21', '$248.95'],
                                ['CZ1539', 'JASPER, UNITED STATES', 'TOLEDO, UNITED STATES', 'Medium Activity', 5188, '$1,286,649.37', '$248.00'],
                                ['IN2177', 'WELLINGTON, UNITED STATES', 'SALISBURY, UNITED STATES', 'Medium Activity', 5184, '$1,314,038.54', '$253.48'],
                                ['UZ1553', 'TUSCALOOSA, UNITED STATES', 'LOUISBURG, UNITED STATES', 'Medium Activity', 5142, '$1,279,430.74', '$248.82'],
                                ['EL1896', 'HOBART, UNITED STATES', 'FT BELVOIR, UNITED STATES', 'Medium Activity', 5137, '$1,282,379.75', '$249.64'],
                                ['UR7539', 'TETERBORO, UNITED STATES', 'CARIBOU, UNITED STATES', 'Medium Activity', 5120, '$1,280,897.63', '$250.18'],
                                ['GE9943', 'PALM SPRINGS, UNITED STATES', 'FRIENDLY, UNITED STATES', 'Medium Activity', 5111, '$1,305,493.27', '$255.43'],
                                ['UN1252', 'SIOUX CENTER, UNITED STATES', 'BRUNSWICK, UNITED STATES', 'Medium Activity', 5103, '$1,271,048.33', '$249.08'],
                                ['AF5511', 'MOAB, UNITED STATES', 'DUNCAN, UNITED STATES', 'Medium Activity', 5101, '$1,284,184.46', '$251.75'],
                                ['TR5561', 'YAKIMA, UNITED STATES', 'LEMMON, UNITED STATES', 'Medium Activity', 5096, '$1,254,924.21', '$246.26'],
                                ['RE2124', 'PASCAGOULA, UNITED STATES', 'COLUMBIA, UNITED STATES', 'Medium Activity', 5091, '$1,273,236.97', '$250.10'],
                                ['RU8104', 'LADYSMITH, UNITED STATES', 'ALAMOGORDO, UNITED STATES', 'Medium Activity', 5081, '$1,290,902.65', '$254.06'],
                                ['IN5659', 'WESTFIELD/ SPRINGFIELD, UNITED STATES', 'NEW ORLEANS, UNITED STATES', 'Medium Activity', 5076, '$1,278,080.91', '$251.79'],
                                ['ZA4906', 'RAPID CITY, UNITED STATES', 'VACAVILLE, UNITED STATES', 'Medium Activity', 5051, '$1,264,899.95', '$250.43'],
                                ['CR1704', 'SANDERSVILLE, UNITED STATES', 'DWIGHT, UNITED STATES', 'Medium Activity', 5041, '$1,261,920.20', '$250.33'],
                                ['MA1579', 'FAREWELL LAKE, UNITED STATES', 'MORGANTON, UNITED STATES', 'Medium Activity', 5036, '$1,269,937.00', '$252.17'],
                                ['BR4248', 'SAFFORD, UNITED STATES', 'LITTLE ROCK, UNITED STATES', 'Medium Activity', 5034, '$1,251,799.91', '$248.67'],
                                ['IT8955', 'INYOKERN, UNITED STATES', 'KERRVILLE, UNITED STATES', 'Low Activity', 4999, '$1,246,585.91', '$249.37'],
                                ['RW1840', 'AMES, UNITED STATES', 'BILOXI, UNITED STATES', 'Low Activity', 4992, '$1,253,463.57', '$251.09'],
                                ['ME3758', 'POINT MC INTYRE, UNITED STATES', 'PORT HEIDEN, UNITED STATES', 'Low Activity', 4978, '$1,266,844.81', '$254.49'],
                                ['AL4631', 'REXBURG, UNITED STATES', 'HENDERSON, UNITED STATES', 'Low Activity', 4969, '$1,262,569.88', '$254.09'],
                                ['SA6469', 'TELLURIDE, UNITED STATES', 'GAITHERSBURG, UNITED STATES', 'Low Activity', 4965, '$1,253,269.80', '$252.42'],
                                ['SU1241', 'LINCOLNTON, UNITED STATES', 'JACKSONVILLE, UNITED STATES', 'Low Activity', 4955, '$1,236,619.55', '$249.57'],
                                ['IN6123', 'SALLISAW, UNITED STATES', 'OMAHA, UNITED STATES', 'Low Activity', 4928, '$1,231,265.48', '$249.85'],
                                ['GU1200', 'WAPAKONETA, UNITED STATES', 'CUMBERLAND, UNITED STATES', 'Low Activity', 4914, '$1,230,417.74', '$250.39'],
                                ['QA1677', 'SANTA PAULA, UNITED STATES', 'HARLAN, UNITED STATES', 'Low Activity', 4911, '$1,233,189.34', '$251.11'],
                                ['BR4921', 'TOMPKINSVILLE, UNITED STATES', 'HAWTHORNE, UNITED STATES', 'Low Activity', 4909, '$1,252,280.55', '$255.10'],
                                ['BA6328', 'SLEETMUTE, UNITED STATES', 'OGDEN, UNITED STATES', 'Low Activity', 4900, '$1,220,171.48', '$249.01'],
                                ['UR9705', 'VALPARAISO, UNITED STATES', 'NORTH ADAMS, UNITED STATES', 'Low Activity', 4889, '$1,213,533.53', '$248.22'],
                                ['GH9790', 'GREENFIELD, UNITED STATES', 'MONTGOMERY, UNITED STATES', 'Low Activity', 4886, '$1,246,035.57', '$255.02'],
                                ['VE5573', 'DEVILS LAKE, UNITED STATES', 'MOUNT PLEASANT, UNITED STATES', 'Low Activity', 4885, '$1,214,500.68', '$248.62'],
                                ['IV7414', 'HATTERAS, UNITED STATES', 'SARASOTA/ BRADENTON, UNITED STATES', 'Low Activity', 4877, '$1,227,771.18', '$251.75'],
                                ['AR6955', 'GULKANA, UNITED STATES', 'MERIDIAN, UNITED STATES', 'Low Activity', 4858, '$1,210,093.30', '$249.09'],
                                ['KO2721', 'NORFOLK, UNITED STATES', 'BIRMINGHAM, UNITED STATES', 'Low Activity', 4832, '$1,205,806.77', '$249.55'],
                                ['YE5186', 'MINOCQUA-WOODRUFF, UNITED STATES', 'OMAHA, UNITED STATES', 'Low Activity', 4823, '$1,199,693.07', '$248.74'],
                                ['CH3914', 'ATWOOD, UNITED STATES', 'BENTONVILLE, UNITED STATES', 'Low Activity', 4808, '$1,198,090.54', '$249.19'],
                                ['RE5456', 'FT HUACHUCA, UNITED STATES', 'ROGERSVILLE, UNITED STATES', 'Low Activity', 4789, '$1,207,543.70', '$252.15'],
                                ['ST8550', 'MOUNTAIN HOME, UNITED STATES', 'HAZEN, UNITED STATES', 'Low Activity', 4788, '$1,209,187.08', '$252.55'],
                                ['AU3342', 'CHEROKEE, UNITED STATES', 'FENTRESS, UNITED STATES', 'Low Activity', 4786, '$1,210,572.65', '$252.94'],
                                ['CU6108', 'GRAND FORKS, UNITED STATES', 'NEWCASTLE, UNITED STATES', 'Low Activity', 4765, '$1,189,717.07', '$249.68'],
                                ['NI9531', 'CHEROKEE, UNITED STATES', "COEUR D'ALENE, UNITED STATES", 'Low Activity', 4764, '$1,210,221.02', '$254.03'],
                                ['ZA5582', 'SAVOONGA, UNITED STATES', 'ANDREWS, UNITED STATES', 'Low Activity', 4753, '$1,188,230.77', '$250.00'],
                                ['UK7348', 'TWIN FALLS, UNITED STATES', 'HAZLEHURST, UNITED STATES', 'Low Activity', 4715, '$1,180,562.66', '$250.38'],
                                ['BO9148', 'RICHMOND, UNITED STATES', 'PALM SPRINGS, UNITED STATES', 'Low Activity', 4706, '$1,171,237.63', '$248.88'],
                                ['TH1462', 'COLD BAY, UNITED STATES', 'LEWISTON, UNITED STATES', 'Low Activity', 4681, '$1,177,111.28', '$251.47'],
                                ['WE5545', 'MADISON, UNITED STATES', 'JAMESTOWN, UNITED STATES', 'Low Activity', 4680, '$1,180,568.14', '$252.26'],
                                ['JO8839', 'DANVILLE, UNITED STATES', 'DENVER, UNITED STATES', 'Low Activity', 4667, '$1,165,104.54', '$249.65'],
                                ['CU8668', 'HARLINGEN, UNITED STATES', 'LADYSMITH, UNITED STATES', 'Low Activity', 4661, '$1,158,192.33', '$248.49'],
                                ['CH7513', 'WILLMAR, UNITED STATES', 'WHEATLAND, UNITED STATES', 'Low Activity', 4639, '$1,160,805.03', '$250.23'],
                                ['GA7657', 'CEDAR RAPIDS, UNITED STATES', 'MC MINNVILLE, UNITED STATES', 'Low Activity', 4639, '$1,173,459.40', '$252.96'],
                                ['SU1915', 'HARLINGEN, UNITED STATES', 'MONROE, UNITED STATES', 'Low Activity', 4627, '$1,183,170.95', '$255.71'],
                                ['SP3497', 'RICE LAKE, UNITED STATES', 'HILLSBORO, UNITED STATES', 'Low Activity', 4601, '$1,157,822.60', '$251.65'],
                                ['IC2874', 'PALACIOS, UNITED STATES', 'HAILEY, UNITED STATES', 'Low Activity', 4597, '$1,154,902.09', '$251.23'],
                                ['RU5293', 'GREYBULL, UNITED STATES', 'PRICE, UNITED STATES', 'Low Activity', 4589, '$1,137,547.89', '$247.89'],
                                ['AZ2625', 'PHILADELPHIA, UNITED STATES', 'GREENFIELD, UNITED STATES', 'Low Activity', 4584, '$1,158,273.55', '$252.68'],
                                ['BA2869', 'BATESVILLE, UNITED STATES', 'TIN CITY, UNITED STATES', 'Low Activity', 4582, '$1,147,793.13', '$250.50'],
                                ['SO7968', 'MARATHON, UNITED STATES', 'WEST BEND, UNITED STATES', 'Low Activity', 4577, '$1,147,289.97', '$250.66'],
                                ['KA3789', 'MANHATTAN, UNITED STATES', 'DANBURY, UNITED STATES', 'Low Activity', 4575, '$1,134,744.83', '$248.03'],
                                ['ZI6188', 'ELIZABETH CITY, UNITED STATES', 'WISCASSET, UNITED STATES', 'Low Activity', 4572, '$1,136,042.03', '$248.48'],
                                ['KU2457', 'HASTINGS, UNITED STATES', 'WASHINGTON, UNITED STATES', 'Low Activity', 4564, '$1,127,913.93', '$247.13'],
                                ['EL3960', 'RALEIGH/ DURHAM, UNITED STATES', 'WRIGHTSTOWN, UNITED STATES', 'Low Activity', 4552, '$1,141,920.57', '$250.86'],
                                ['KU1452', 'ADRIAN, UNITED STATES', 'QUINHAGAK, UNITED STATES', 'Low Activity', 4552, '$1,154,488.67', '$253.62'],
                                ['JO1064', 'POINT HOPE, UNITED STATES', 'WARROAD, UNITED STATES', 'Low Activity', 4549, '$1,155,475.29', '$254.01'],
                                ['HA7026', 'ELKHART, UNITED STATES', 'FALLON, UNITED STATES', 'Low Activity', 4545, '$1,146,403.79', '$252.23'],
                                ['KI7489', 'TEHACHAPI, UNITED STATES', 'CINCINNATI, UNITED STATES', 'Low Activity', 4540, '$1,135,088.63', '$250.02'],
                                ['NI2913', 'BLYTHEVILLE, UNITED STATES', 'STARKVILLE, UNITED STATES', 'Low Activity', 4534, '$1,136,669.63', '$250.70'],
                                ['UG1501', 'MICHIGAN CITY, UNITED STATES', 'BUCKLAND, UNITED STATES', 'Low Activity', 4529, '$1,130,602.31', '$249.64'],
                                ['RO1090', 'LORAIN/ ELYRIA, UNITED STATES', 'SHREVEPORT, UNITED STATES', 'Low Activity', 4522, '$1,131,428.45', '$250.21'],
                                ['KO3866', 'UTICA, UNITED STATES', 'MASON, UNITED STATES', 'Low Activity', 4488, '$1,121,031.45', '$249.78'],
                                ['BH4662', 'DUBLIN, UNITED STATES', 'SPARREVOHN, UNITED STATES', 'Low Activity', 4464, '$1,111,817.65', '$249.06'],
                                ['SI6378', 'MONTE VISTA, UNITED STATES', 'NAPLES, UNITED STATES', 'Low Activity', 4462, '$1,120,565.12', '$251.14'],
                                ['DA3014', 'ARTESIA, UNITED STATES', 'ATLANTA, UNITED STATES', 'Low Activity', 4453, '$1,111,681.99', '$249.65'],
                                ['KA1073', 'WAGNER, UNITED STATES', 'DE LAND, UNITED STATES', 'Low Activity', 4446, '$1,125,719.65', '$253.20'],
                                ['ZA9495', 'MUSCATINE, UNITED STATES', 'FT SCOTT, UNITED STATES', 'Low Activity', 4441, '$1,113,130.65', '$250.65'],
                                ['ES3957', 'TAMPA, UNITED STATES', 'SEARCY, UNITED STATES', 'Low Activity', 4434, '$1,116,381.71', '$251.78'],
                                ['JA1786', 'RALEIGH/ DURHAM, UNITED STATES', 'FOSTORIA, UNITED STATES', 'Low Activity', 4434, '$1,132,699.70', '$255.46'],
                                ['DE8785', 'WILMINGTON, UNITED STATES', 'OMAHA, UNITED STATES', 'Low Activity', 4432, '$1,113,964.88', '$251.35'],
                                ['VA2178', 'WILLOW, UNITED STATES', 'BREMERTON, UNITED STATES', 'Low Activity', 4417, '$1,103,451.91', '$249.82'],
                                ['HA3425', 'GRAND PRAIRIE, UNITED STATES', 'MONTEVIDEO, UNITED STATES', 'Low Activity', 4382, '$1,103,344.95', '$251.79'],
                                ['GH4246', 'GLENS FALLS, UNITED STATES', 'DENISON, UNITED STATES', 'Low Activity', 4373, '$1,093,759.01', '$250.12'],
                                ['NE7662', 'WACO, UNITED STATES', 'NASHUA, UNITED STATES', 'Low Activity', 4373, '$1,085,864.39', '$248.31'],
                                ['RE9932', 'ELIZABETHTOWN, UNITED STATES', 'AKRON, UNITED STATES', 'Low Activity', 4372, '$1,099,294.22', '$251.44'],
                                ['SR7387', 'EL DORADO, UNITED STATES', 'UGNU KUPARUK, UNITED STATES', 'Low Activity', 4366, '$1,101,363.70', '$252.26'],
                                ['IC4901', 'WILLIAMSBURG, UNITED STATES', 'EUGENE, UNITED STATES', 'Low Activity', 4356, '$1,106,534.84', '$254.03'],
                                ['SP1410', 'KLAMATH FALLS, UNITED STATES', 'MT PLEASANT, UNITED STATES', 'Low Activity', 4311, '$1,091,952.57', '$253.29'],
                                ['BU1169', 'SOUTH HILL, UNITED STATES', 'SEDALIA, UNITED STATES', 'Low Activity', 4302, '$1,072,182.60', '$249.23'],
                                ['NE4498', 'OPELOUSAS, UNITED STATES', 'OAK ISLAND, UNITED STATES', 'Low Activity', 4288, '$1,075,716.04', '$250.87'],
                                ['AZ1409', 'GRIFFIN, UNITED STATES', 'WICHITA, UNITED STATES', 'Low Activity', 4287, '$1,085,186.89', '$253.13'],
                                ['CR5783', 'MONTROSE, UNITED STATES', 'MT HOLLY, UNITED STATES', 'Low Activity', 4285, '$1,081,124.20', '$252.30'],
                                ['EG1255', 'LYNCHBURG, UNITED STATES', 'IMMOKALEE, UNITED STATES', 'Low Activity', 4263, '$1,062,500.52', '$249.24'],
                                ['EQ4385', 'BURLINGTON, UNITED STATES', 'WINDOW ROCK, UNITED STATES', 'Low Activity', 4263, '$1,071,401.31', '$251.33'],
                                ['AF1363', 'CANADIAN, UNITED STATES', 'INDIANAPOLIS, UNITED STATES', 'Low Activity', 4249, '$1,067,889.96', '$251.33'],
                                ['SO7110', 'CHICAGO/ PROSPECT HGTS/ WHEELI, UNITED STATES', 'SAC CITY, UNITED STATES', 'Low Activity', 4245, '$1,058,270.84', '$249.30'],
                                ['KY1862', 'WASKISH, UNITED STATES', 'BENTONVILLE, UNITED STATES', 'Low Activity', 4212, '$1,054,891.93', '$250.45'],
                                ['SP3786', 'ALAMOGORDO, UNITED STATES', 'PINE MOUNTAIN, UNITED STATES', 'Low Activity', 4206, '$1,048,772.35', '$249.35'],
                                ['UG3979', 'DE KALB, UNITED STATES', 'PITTSBURGH, UNITED STATES', 'Low Activity', 4201, '$1,059,652.09', '$252.24'],
                                ['JA8621', 'PORTLAND, UNITED STATES', 'DUMAS, UNITED STATES', 'Low Activity', 4199, '$1,063,114.91', '$253.18'],
                                ['IT3475', 'VAN NUYS, UNITED STATES', 'RALEIGH/ DURHAM, UNITED STATES', 'Low Activity', 4179, '$1,043,619.47', '$249.73'],
                                ['DJ1033', 'DETROIT LAKES, UNITED STATES', 'BEAUFORT, UNITED STATES', 'Low Activity', 4173, '$1,048,598.76', '$251.28'],
                                ['BR7165', 'QUILLAYUTE, UNITED STATES', 'FREEPORT, UNITED STATES', 'Low Activity', 4153, '$1,046,279.02', '$251.93'],
                                ['BO1531', 'GABBS, UNITED STATES', 'FAIRBURY, UNITED STATES', 'Low Activity', 4148, '$1,029,202.71', '$248.12'],
                                ['AM6843', 'COLUMBUS, UNITED STATES', 'ELIZABETH CITY, UNITED STATES', 'Low Activity', 4126, '$1,014,313.02', '$245.83'],
                                ['AN5831', 'PALMDALE, UNITED STATES', 'ELIZABETH CITY, UNITED STATES', 'Low Activity', 4126, '$1,036,495.51', '$251.21'],
                                ['NI6895', 'WILLOWS, UNITED STATES', 'BOONVILLE, UNITED STATES', 'Low Activity', 4122, '$1,036,732.68', '$251.51'],
                                ['IC8086', 'KNOXVILLE, UNITED STATES', 'WESTMINSTER, UNITED STATES', 'Low Activity', 4121, '$1,042,415.06', '$252.95'],
                                ['GI4807', 'BARTER I LRRS, UNITED STATES', 'RAPID CITY, UNITED STATES', 'Low Activity', 4107, '$1,006,828.54', '$245.15'],
                                ['KY1985', 'KONGIGANAK, UNITED STATES', 'FAREWELL, UNITED STATES', 'Low Activity', 4104, '$1,034,207.25', '$252.00'],
                                ['UK9814', 'NORTH VERNON, UNITED STATES', 'ALBANY, UNITED STATES', 'Low Activity', 4096, '$1,001,080.37', '$244.40'],
                                ['GR5936', 'FT HOOD, UNITED STATES', 'OSCODA, UNITED STATES', 'Low Activity', 4095, '$1,032,585.95', '$252.16'],
                                ['KU8767', 'SALMON, UNITED STATES', 'LAWRENCE, UNITED STATES', 'Low Activity', 4090, '$1,020,486.01', '$249.51'],
                                ['DA7841', 'WINDER, UNITED STATES', 'CHAPEL HILL, UNITED STATES', 'Low Activity', 4089, '$1,043,851.02', '$255.28'],
                                ['BR1764', 'CONNERSVILLE, UNITED STATES', 'SUPERIOR, UNITED STATES', 'Low Activity', 4078, '$1,015,657.39', '$249.06'],
                                ['EG8772', 'ALBION, UNITED STATES', 'YAKIMA, UNITED STATES', 'Low Activity', 4066, '$1,029,865.90', '$253.29'],
                                ['FA6242', 'FAIRFIELD, UNITED STATES', 'KANAB, UNITED STATES', 'Low Activity', 4060, '$1,029,653.82', '$253.61'],
                                ['QA9393', 'LOUISA, UNITED STATES', 'HAZEN, UNITED STATES', 'Low Activity', 4058, '$1,041,400.51', '$256.63'],
                                ['UR1926', 'KENOSHA, UNITED STATES', 'NORWOOD, UNITED STATES', 'Low Activity', 4044, '$1,021,941.21', '$252.71'],
                                ['HA6897', 'UNALAKLEET, UNITED STATES', 'MC MINNVILLE, UNITED STATES', 'Low Activity', 4038, '$1,012,950.90', '$250.85'],
                                ['CE8523', 'MARFA, UNITED STATES', 'JOLIET, UNITED STATES', 'Low Activity', 4017, '$1,011,536.26', '$251.81'],
                                ['GI3520', 'GOSHEN, UNITED STATES', 'NEW BERN, UNITED STATES', 'Low Activity', 4014, '$995,318.83', '$247.96'],
                                ['SW1316', 'SAN JOSE, UNITED STATES', 'WICHITA, UNITED STATES', 'Low Activity', 3982, '$1,012,455.91', '$254.26'],
                                ['KU1005', 'BOULDER JUNCTION, UNITED STATES', 'RENSSELAER, UNITED STATES', 'Low Activity', 3972, '$999,236.53', '$251.57'],
                                ['NE6793', 'HANA, UNITED STATES', 'HUTCHINSON, UNITED STATES', 'Low Activity', 3966, '$1,003,240.50', '$252.96'],
                                ['TO9094', 'NEW YORK, UNITED STATES', 'MINNEAPOLIS, UNITED STATES', 'Low Activity', 3963, '$995,588.71', '$251.22'],
                                ['ZA2310', 'FRANKFORT, UNITED STATES', 'MC CALL, UNITED STATES', 'Low Activity', 3955, '$996,339.13', '$251.92'],
                                ['DO7839', 'THOMSON, UNITED STATES', 'MT PLEASANT, UNITED STATES', 'Low Activity', 3952, '$1,004,367.77', '$254.14'],
                                ['SI7973', 'PAHOKEE, UNITED STATES', 'KEARNEY, UNITED STATES', 'Low Activity', 3940, '$987,017.17', '$250.51'],
                                ['JA4117', 'LINCOLN, UNITED STATES', 'CLEVELAND, UNITED STATES', 'Low Activity', 3926, '$983,665.04', '$250.55'],
                                ['BO6504', 'BUFFALO, UNITED STATES', 'NEWTON, UNITED STATES', 'Low Activity', 3920, '$975,347.88', '$248.81'],
                                ['LE7234', 'MOUNT PLEASANT, UNITED STATES', 'LAKE HAVASU CITY, UNITED STATES', 'Low Activity', 3920, '$984,915.79', '$251.25'],
                                ['PE2895', 'SHELDON, UNITED STATES', 'OAK ISLAND, UNITED STATES', 'Low Activity', 3919, '$977,055.12', '$249.31'],
                                ['TH7797', 'QUAKERTOWN, UNITED STATES', 'LEXINGTON, UNITED STATES', 'Low Activity', 3916, '$975,539.53', '$249.12'],
                                ['NE6274', 'WINSLOW, UNITED STATES', 'HAYWARD, UNITED STATES', 'Low Activity', 3869, '$979,527.14', '$253.17'],
                                ['FR1028', 'JANESVILLE, UNITED STATES', 'LOS ANGELES, UNITED STATES', 'Low Activity', 3813, '$959,658.24', '$251.68'],
                                ['TH3514', 'MANHATTAN, UNITED STATES', 'FRYEBURG, UNITED STATES', 'Low Activity', 3804, '$950,412.38', '$249.85'],
                                ['WA5338', 'GRINNELL, UNITED STATES', 'STAUNTON-WAYNESBORO-HARRISONB*, UNITED STATES', 'Low Activity', 3776, '$952,620.84', '$252.28'],
                                ['SR4214', 'CONNERSVILLE, UNITED STATES', 'MINERAL WELLS, UNITED STATES', 'Low Activity', 3723, '$947,499.62', '$254.50'],
                                ['BR8503', 'FT SUMNER, UNITED STATES', 'SARATOGA, UNITED STATES', 'Low Activity', 3715, '$928,253.15', '$249.87'],
                                ['HA5622', 'ONTONAGON, UNITED STATES', 'CADILLAC, UNITED STATES', 'Low Activity', 3703, '$913,310.95', '$246.64'],
                                ['AL8273', 'PAXSON, UNITED STATES', 'JASPER, UNITED STATES', 'Low Activity', 3667, '$912,722.45', '$248.90'],
                                ['UG8873', 'MADISON, UNITED STATES', 'MONROE, UNITED STATES', 'Low Activity', 3653, '$916,886.13', '$251.00'],
                                ['GI3143', 'PLATTSMOUTH, UNITED STATES', 'REED CITY, UNITED STATES', 'Low Activity', 3651, '$896,164.13', '$245.46'],
                                ['EG3901', 'COMPTON, UNITED STATES', 'FAIRBURY, UNITED STATES', 'Low Activity', 3638, '$927,102.72', '$254.84'],
                                ['BH1799', 'COLUMBUS, UNITED STATES', 'ATLANTA, UNITED STATES', 'Low Activity', 3628, '$912,222.51', '$251.44'],
                                ['EQ9427', 'RED OAK, UNITED STATES', 'DE KALB, UNITED STATES', 'Low Activity', 3614, '$898,542.94', '$248.63'],
                                ['EC9462', 'WEIRWOOD, UNITED STATES', 'GREENWOOD, UNITED STATES', 'Low Activity', 3594, '$909,270.64', '$253.00'],
                                ['MI9412', 'CHARLESTON, UNITED STATES', 'ASPEN, UNITED STATES', 'Low Activity', 3579, '$907,235.55', '$253.49'],
                                ['LU9907', 'DURANGO, UNITED STATES', 'SAVANNAH, UNITED STATES', 'Low Activity', 3553, '$881,841.50', '$248.20'],
                                ['MY6984', 'BELUGA, UNITED STATES', 'CAMP DOUGLAS, UNITED STATES', 'Low Activity', 3544, '$883,009.29', '$249.16'],
                                ['FI5995', 'MT PLEASANT, UNITED STATES', 'IRONWOOD, UNITED STATES', 'Low Activity', 3530, '$894,499.35', '$253.40'],
                                ['ME3104', 'LAWTON, UNITED STATES', 'MOBERLY, UNITED STATES', 'Low Activity', 3504, '$885,253.49', '$252.64'],
                                ['BE6763', 'WABASH, UNITED STATES', 'SANFORD, UNITED STATES', 'Low Activity', 3491, '$891,757.16', '$255.44'],
                                ['GR9521', 'MANISTIQUE, UNITED STATES', 'TORRINGTON, UNITED STATES', 'Low Activity', 3485, '$880,738.87', '$252.72'],
                                ['KE3030', 'HOBBS, UNITED STATES', 'MOBRIDGE, UNITED STATES', 'Low Activity', 3480, '$862,597.41', '$247.87'],
                                ['PU8380', 'REXBURG, UNITED STATES', 'VACAVILLE, UNITED STATES', 'Low Activity', 3467, '$869,600.30', '$250.82'],
                                ['UK8861', 'TEXARKANA, UNITED STATES', 'BENNETTSVILLE, UNITED STATES', 'Low Activity', 3449, '$870,965.23', '$252.53'],
                                ['JA6456', 'NEW MADRID, UNITED STATES', 'QUINHAGAK, UNITED STATES', 'Low Activity', 3410, '$859,816.72', '$252.15'],
                                ['MY2827', 'MIDLAND, UNITED STATES', 'PASCO, UNITED STATES', 'Low Activity', 3394, '$830,239.64', '$244.62'],
                                ['WA4177', 'WAYNESBORO, UNITED STATES', 'CLIFTON-MORENCI, UNITED STATES', 'Low Activity', 3352, '$844,659.71', '$251.99'],
                                ['IT1363', 'MANKATO, UNITED STATES', 'MADISON, UNITED STATES', 'Low Activity', 3343, '$851,357.67', '$254.67'],
                                ['DO3710', 'GARDNER, UNITED STATES', 'MOBILE, UNITED STATES', 'Low Activity', 3327, '$840,318.34', '$252.58'],
                                ['EQ1356', 'WEIRWOOD, UNITED STATES', 'CAPE GIRARDEAU, UNITED STATES', 'Low Activity', 3321, '$823,028.52', '$247.83'],
                                ['HO4948', 'PRESTON, UNITED STATES', 'BLYTHEVILLE, UNITED STATES', 'Low Activity', 3287, '$831,219.41', '$252.88'],
                                ['AR4872', 'GREENVILLE, UNITED STATES', 'THOMSON, UNITED STATES', 'Low Activity', 3280, '$819,939.56', '$249.98'],
                                ['UR1647', 'DOUGLAS, UNITED STATES', 'PERRY, UNITED STATES', 'Low Activity', 3221, '$812,453.00', '$252.24'],
                                ['GU5728', 'MORRISTOWN, UNITED STATES', 'TOCCOA, UNITED STATES', 'Low Activity', 3205, '$793,435.06', '$247.56'],
                                ['KE7574', 'FAYETTEVILLE/ SPRINGDALE/ ROGE, UNITED STATES', 'CHIGNIK, UNITED STATES', 'Low Activity', 3200, '$794,692.17', '$248.34'],
                                ['TU2789', 'AMES, UNITED STATES', 'GARY, UNITED STATES', 'Low Activity', 3197, '$792,338.69', '$247.84'],
                                ['SU9286', 'MILLINOCKET, UNITED STATES', 'LEESBURG, UNITED STATES', 'Low Activity', 3178, '$791,429.52', '$249.03'],
                                ['IN7951', 'APALACHICOLA, UNITED STATES', 'STUART, UNITED STATES', 'Low Activity', 3175, '$807,628.33', '$254.37'],
                                ['KE4962', 'MANKATO, UNITED STATES', 'FT POLK, UNITED STATES', 'Low Activity', 3173, '$799,372.60', '$251.93'],
                                ['PH3107', 'MERRILL, UNITED STATES', 'HEBER SPRINGS, UNITED STATES', 'Low Activity', 3137, '$769,140.14', '$245.18'],
                                ['OM2143', 'YANKTON, UNITED STATES', 'ST CLOUD, UNITED STATES', 'Low Activity', 3130, '$794,045.47', '$253.69'],
                                ['IC4688', 'PINE MOUNTAIN, UNITED STATES', 'SAVANNA, UNITED STATES', 'Low Activity', 3125, '$788,010.25', '$252.16'],
                                ['IT1944', 'PETERSBURG, UNITED STATES', 'MEXIA, UNITED STATES', 'Low Activity', 3117, '$788,379.56', '$252.93'],
                                ['SW6446', 'HUSLIA, UNITED STATES', 'ALICEVILLE, UNITED STATES', 'Low Activity', 3112, '$792,359.71', '$254.61'],
                                ['PA1482', 'WILLOW, UNITED STATES', 'CLEVELAND, UNITED STATES', 'Low Activity', 3069, '$770,179.52', '$250.95'],
                                ['SI3566', 'SPARREVOHN, UNITED STATES', 'KENANSVILLE, UNITED STATES', 'Low Activity', 3056, '$765,616.86', '$250.53'],
                                ['EG1536', 'GREEN BAY, UNITED STATES', 'AKRON, UNITED STATES', 'Low Activity', 3035, '$750,483.47', '$247.28'],
                                ['PA4921', 'RUIDOSO, UNITED STATES', 'SELMER, UNITED STATES', 'Low Activity', 3028, '$764,040.03', '$252.32'],
                                ['DE6893', 'CONNERSVILLE, UNITED STATES', 'WAHPETON, UNITED STATES', 'Low Activity', 3019, '$750,085.78', '$248.46'],
                                ['AF4041', 'MARKSVILLE, UNITED STATES', 'WOODWARD, UNITED STATES', 'Low Activity', 3016, '$768,413.65', '$254.78'],
                                ['BO1663', 'ASTORIA, UNITED STATES', 'MOORELAND, UNITED STATES', 'Low Activity', 2987, '$759,706.86', '$254.34'],
                                ['UG4187', 'UGNU KUPARUK, UNITED STATES', 'CLARKSDALE, UNITED STATES', 'Low Activity', 2987, '$758,202.40', '$253.83'],
                                ['PA2514', 'CHATTANOOGA, UNITED STATES', 'WISCASSET, UNITED STATES', 'Low Activity', 2977, '$753,976.29', '$253.27'],
                                ['FR9337', 'FARMINGTON, UNITED STATES', 'AUBURN, UNITED STATES', 'Low Activity', 2968, '$756,350.22', '$254.83'],
                                ['ST2257', 'RED OAK, UNITED STATES', 'LIVINGSTON, UNITED STATES', 'Low Activity', 2964, '$728,487.49', '$245.78'],
                                ['CE4126', 'CASA GRANDE, UNITED STATES', 'CRESCENT CITY, UNITED STATES', 'Low Activity', 2941, '$735,004.55', '$249.92'],
                                ['MI4717', 'VERSAILLES, UNITED STATES', 'DECATUR, UNITED STATES', 'Low Activity', 2918, '$728,437.91', '$249.64'],
                                ['NO9017', 'STURGEON BAY, UNITED STATES', 'NEOSHO, UNITED STATES', 'Low Activity', 2911, '$734,290.64', '$252.25'],
                                ['SL3645', 'JACKSONVILLE, UNITED STATES', 'MEXIA, UNITED STATES', 'Low Activity', 2898, '$741,602.83', '$255.90'],
                                ['SU3807', 'FRANKFORT, UNITED STATES', 'CLARION, UNITED STATES', 'Low Activity', 2874, '$727,808.09', '$253.24'],
                                ['CY1974', 'HATTIESBURG-LAUREL, UNITED STATES', 'PASO ROBLES, UNITED STATES', 'Low Activity', 2863, '$722,008.11', '$252.19'],
                                ['MI1352', 'ERROL, UNITED STATES', 'INDIANAPOLIS, UNITED STATES', 'Low Activity', 2845, '$707,544.01', '$248.70'],
                                ['IT1277', 'HOQUIAM, UNITED STATES', 'LUSK, UNITED STATES', 'Low Activity', 2818, '$696,361.47', '$247.11'],
                                ['EG4371', 'BEAVER FALLS, UNITED STATES', 'PLATTSBURGH, UNITED STATES', 'Low Activity', 2781, '$684,266.28', '$246.05'],
                                ['OM4727', 'PLATTSMOUTH, UNITED STATES', 'CORPUS CHRISTI, UNITED STATES', 'Low Activity', 2775, '$700,566.30', '$252.46'],
                                ['KO2336', 'PATTERSON, UNITED STATES', 'IOWA CITY, UNITED STATES', 'Low Activity', 2748, '$685,184.36', '$249.34'],
                                ['KO1317', 'ROUNDUP, UNITED STATES', 'MENOMINEE, UNITED STATES', 'Low Activity', 2727, '$686,903.82', '$251.89'],
                                ['DJ3110', 'TOLEDO, UNITED STATES', 'CHICAGO, UNITED STATES', 'Low Activity', 2723, '$682,889.76', '$250.79'],
                                ['BU1379', 'JOPLIN, UNITED STATES', 'HATTIESBURG, UNITED STATES', 'Low Activity', 2719, '$677,844.79', '$249.30'],
                                ['KY2342', 'MT STERLING, UNITED STATES', 'BLOCK ISLAND, UNITED STATES', 'Low Activity', 2671, '$667,965.74', '$250.08'],
                                ['HO2613', 'LEWISBURG, UNITED STATES', 'SAN ANTONIO, UNITED STATES', 'Low Activity', 2634, '$663,859.19', '$252.03'],
                                ['CA3610', 'ORMOND BEACH, UNITED STATES', 'RENSSELAER, UNITED STATES', 'Low Activity', 2623, '$655,506.33', '$249.91'],
                                ['LU3137', 'THREE RIVERS, UNITED STATES', 'FT RILEY, UNITED STATES', 'Low Activity', 2622, '$656,189.32', '$250.26'],
                                ['TU9140', 'NAPA, UNITED STATES', 'WILLIMANTIC, UNITED STATES', 'Low Activity', 2607, '$653,183.93', '$250.55'],
                                ['AU7928', 'MATTOON-CHARLESTON, UNITED STATES', 'OKLAHOMA CITY, UNITED STATES', 'Low Activity', 2606, '$652,653.16', '$250.44'],
                                ['DJ5687', 'BOCA RATON, UNITED STATES', 'CALEDONIA, UNITED STATES', 'Low Activity', 2583, '$660,145.23', '$255.57'],
                                ['ES1102', 'READING, UNITED STATES', 'ST PETERSBURG, UNITED STATES', 'Low Activity', 2564, '$640,390.39', '$249.76'],
                                ['CU3699', 'HAYDEN, UNITED STATES', 'FRANKLIN, UNITED STATES', 'Low Activity', 2562, '$643,460.17', '$251.16'],
                                ['UZ1192', 'KLAMATH FALLS, UNITED STATES', 'FLEMINGSBURG, UNITED STATES', 'Low Activity', 2559, '$640,261.35', '$250.20'],
                                ['PH2954', 'JACKSONVILLE, UNITED STATES', 'COLUMBUS, UNITED STATES', 'Low Activity', 2546, '$640,724.22', '$251.66'],
                                ['DJ9528', 'COLORADO CITY, UNITED STATES', 'SALMON, UNITED STATES', 'Low Activity', 2498, '$622,426.47', '$249.17'],
                                ['JA4415', 'MARANA, UNITED STATES', 'MINDEN, UNITED STATES', 'Low Activity', 2387, '$601,756.38', '$252.10'],
                                ['EG6129', 'THOMASTON, UNITED STATES', 'NEW YORK, UNITED STATES', 'Low Activity', 2346, '$597,392.59', '$254.64'],
                                ['ER9027', 'INDEPENDENCE, UNITED STATES', 'GREENWOOD, UNITED STATES', 'Low Activity', 2339, '$587,241.76', '$251.07'],
                                ['KU1172', 'MEADE, UNITED STATES', 'WARSAW, UNITED STATES', 'Low Activity', 2319, '$568,807.59', '$245.28'],
                                ['SL9463', 'ST PAUL, UNITED STATES', 'AMARILLO, UNITED STATES', 'Low Activity', 2297, '$568,950.80', '$247.69'],
                                ['BO3305', 'EGEGIK, UNITED STATES', 'GRAND FORKS, UNITED STATES', 'Low Activity', 2240, '$553,252.95', '$246.99'],
                                ['SL7796', 'OLATHE, UNITED STATES', 'REXBURG, UNITED STATES', 'Low Activity', 2225, '$560,648.90', '$251.98'],
                                ['SL8636', 'KENAI, UNITED STATES', 'MANISTIQUE, UNITED STATES', 'Low Activity', 2192, '$540,512.41', '$246.58'],
                                ['EL8065', 'STATESBORO, UNITED STATES', 'SYLACAUGA, UNITED STATES', 'Low Activity', 2172, '$543,266.01', '$250.12'],
                                ['GU9630', 'CHEFORNAK, UNITED STATES', 'MEXIA, UNITED STATES', 'Low Activity', 2120, '$529,392.82', '$249.71'],
                                ['UN1806', 'CHAPPELL, UNITED STATES', 'CHILLICOTHE, UNITED STATES', 'Low Activity', 2112, '$529,514.95', '$250.72'],
                                ['PH1229', 'RIVERTON, UNITED STATES', 'ROCKFORD, UNITED STATES', 'Low Activity', 2096, '$522,057.82', '$249.07'],
                                ['MA3384', 'NOGALES, UNITED STATES', 'TOPEKA, UNITED STATES', 'Low Activity', 2063, '$520,552.46', '$252.33'],
                                ['MA7716', 'TACOMA, UNITED STATES', 'HETTINGER, UNITED STATES', 'Low Activity', 2058, '$523,690.84', '$254.47'],
                                ['UG4477', 'MULLEN, UNITED STATES', 'MARION-WYTHEVILLE, UNITED STATES', 'Low Activity', 2032, '$516,940.95', '$254.40'],
                                ['RU6111', 'MT POCONO, UNITED STATES', 'GREENVILLE, UNITED STATES', 'Low Activity', 1946, '$486,923.79', '$250.22'],
                                ['PH4565', 'KETCHIKAN, UNITED STATES', 'WASHINGTON, UNITED STATES', 'Low Activity', 1921, '$468,813.68', '$244.05'],
                                ['GU8557', 'TELLURIDE, UNITED STATES', 'WARSAW, UNITED STATES', 'Low Activity', 1870, '$471,860.48', '$252.33'],
                                ['BR5762', 'LOMPOC, UNITED STATES', 'ALBUQUERQUE, UNITED STATES', 'Low Activity', 1760, '$431,356.48', '$245.09'],
                                ['YE8931', 'MONROE, UNITED STATES', 'ELK CITY, UNITED STATES', 'Low Activity', 1734, '$427,135.57', '$246.33'],
                                ['OM1745', 'WATERTOWN, UNITED STATES', 'CLINTON, UNITED STATES', 'Low Activity', 1724, '$429,152.55', '$248.93'],
                                ['PO2519', 'BIRMINGHAM, UNITED STATES', 'TETERBORO, UNITED STATES', 'Low Activity', 1707, '$441,229.19', '$258.48'],
                                ['BA9434', 'LINCOLN, UNITED STATES', 'CARIBOU, UNITED STATES', 'Low Activity', 1693, '$422,516.09', '$249.57'],
                                ['LE6208', 'PLANT CITY, UNITED STATES', 'FT YUKON, UNITED STATES', 'Low Activity', 1669, '$411,923.92', '$246.81'],
                                ['SL7953', 'LATROBE, UNITED STATES', 'MC ALESTER, UNITED STATES', 'Low Activity', 1668, '$415,190.71', '$248.92'],
                                ['JO1796', 'PULLMAN/ MOSCOW, UNITED STATES', 'SPRINGHILL, UNITED STATES', 'Low Activity', 1657, '$417,291.12', '$251.84'],
                                ['SL5666', 'ROGERS, UNITED STATES', 'BATESVILLE, UNITED STATES', 'Low Activity', 1639, '$410,365.07', '$250.38'],
                                ['SE5025', 'MARYSVILLE, UNITED STATES', 'MERRILL, UNITED STATES', 'Low Activity', 1634, '$428,890.70', '$262.48'],
                                ['UK2852', 'RAMONA, UNITED STATES', 'HOLLYWOOD, UNITED STATES', 'Low Activity', 1590, '$387,490.95', '$243.71'],
                                ['PH3740', 'ROCKDALE, UNITED STATES', 'LANSING, UNITED STATES', 'Low Activity', 1546, '$377,827.73', '$244.39'],
                                ['PH6652', 'ELIZABETHTOWN, UNITED STATES', 'OMAHA, UNITED STATES', 'Low Activity', 1518, '$375,932.28', '$247.65'],
                                ['ME2896', 'OLNEY-NOBLE, UNITED STATES', 'ROME, UNITED STATES', 'Low Activity', 1517, '$374,472.92', '$246.85'],
                                ['KA7447', 'ARTESIA, UNITED STATES', 'SPRINGFIELD, UNITED STATES', 'Low Activity', 1463, '$365,533.40', '$249.85'],
                                ['UZ4793', 'SELMER, UNITED STATES', 'NUIQSUT, UNITED STATES', 'Low Activity', 1355, '$335,750.07', '$247.79'],
                                ['LI6241', 'MONTROSE, UNITED STATES', 'WACO, UNITED STATES', 'Low Activity', 1260, '$319,346.08', '$253.45'],
                                ['TO8949', 'SPRINGFIELD/ CHICOPEE, UNITED STATES', 'BURLINGTON, UNITED STATES', 'Low Activity', 1194, '$297,583.76', '$249.23'],
                                ['KU2440', 'KENNETT, UNITED STATES', 'LIVERMORE, UNITED STATES', 'Low Activity', 1169, '$292,380.25', '$250.11'],
                                ['AF6210', 'ADA, UNITED STATES', 'CORDELE, UNITED STATES', 'Low Activity', 1130, '$283,269.83', '$250.68'],
                                ['JO1351', 'BARTLESVILLE, UNITED STATES', 'EGEGIK, UNITED STATES', 'Low Activity', 1125, '$282,343.74', '$250.97'],
                                ['SL4313', 'POTTSVILLE, UNITED STATES', 'GLENDALE, UNITED STATES', 'Low Activity', 1082, '$267,457.99', '$247.19'],
                                ['BU3152', 'VICTORIA, UNITED STATES', 'SAFFORD, UNITED STATES', 'Low Activity', 1053, '$262,994.20', '$249.76'],
                                ['CU1931', 'RALEIGH/ DURHAM, UNITED STATES', 'SAFFORD, UNITED STATES', 'Low Activity', 1044, '$257,310.48', '$246.47'],
                                ['HO1523', 'WINCHESTER, UNITED STATES', 'ARDMORE, UNITED STATES', 'Low Activity', 1041, '$257,649.90', '$247.50'],
                                ['NA3042', 'SANTA PAULA, UNITED STATES', 'KONGIGANAK, UNITED STATES', 'Very Low Activity', 954, '$235,549.58', '$246.91'],
                                ['EL4980', 'WATERVILLE, UNITED STATES', 'HOQUIAM, UNITED STATES', 'Very Low Activity', 921, '$229,983.35', '$249.71'],
                                ['PH9706', 'GREEN BAY, UNITED STATES', 'DANVILLE, UNITED STATES', 'Very Low Activity', 479, '$116,985.87', '$244.23']
                                ]
                                ]

        alias_counter = 0
        total_aliases = 25
        total_queries = 5

        # open the test folder and read the files inside
        if os_name == 'Windows':
            print("Windows OS Detected")
            directory = os.getcwd()
            grading_directory = os.getcwd() + '\\tempgrades'
            answer = open(f"{directory}\\week11answers.txt", "w")

        elif os_name == 'Linux':
            print("Linux Detected")
            directory = '/home/student/Desktop/itm220grading'
            grading_directory = '/home/student/Desktop/itm220grading/tempgrades'
            answer = open(f"{directory}/week11answers.txt", "w")

        elif os_name == 'Darwin':
            print("MacOS Detected")
            directory = os.getcwd()
            grading_directory = os.getcwd() + '/tempgrades'
            answer = open(f"{directory}/week11answers.txt", "w")
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
                query1_function_list = []
                query2_clause_list = []
                query2_function_list = []
                query3_clause_list = []
                query3_function_list = []
                query4_clause_list = []
                query4_function_list = []
                query5_clause_list = []
                query5_function_list = []

                for command in sqlCommands:
                    a_number += 1
                    
                    # debug.write(f"Query {a_number}. {command}\n")            
                    if a_number == 1 and not command.lower().__contains__('use'):
                        answer.write(f"USE airportdb; Statement NOT FOUND\n")

                    q1_join_counter = 0
                    q1_concat_counter = 0
                    if a_number == 2: # Query 1
                        if command.lower().__contains__('select'):
                            if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                                for word in command.split():
                                    if word.lower() == 'as':
                                        alias_counter += 1
                            if not command.lower().__contains__('from'):
                                query1_clause_list.append(f"FROM Clause NOT used")
                            if command.lower().__contains__('inner join') or command.lower().__contains__('join'):
                                for word in command.split():
                                    if word.lower() == 'join':
                                        q1_join_counter += 1
                                query1_function_list.append(f"INNER JOIN used {q1_join_counter}/4 times")
                            if not command.lower().__contains__('inner join') or not command.lower().__contains__('join'):
                                query1_clause_list.append(f"INNER JOIN Clause NOT used")
                            if not command.lower().__contains__('where'):
                                query1_clause_list.append(f"WHERE Clause NOT used")
                            if not command.lower().__contains__('group by'):
                                query1_clause_list.append(f"GROUP BY Clause NOT used")
                            if command.lower().__contains__('concat'):
                                for word in command.split():
                                    if word.lower() == 'concat(ag.city,' or word.lower() == 'concat(ag2.city,':
                                        q1_concat_counter += 1
                                query1_function_list.append(f"CONCAT used {q1_concat_counter}/4 times")
                            if not command.lower().__contains__('concat'):
                                query1_function_list.append(f"CONCAT function NOT used")
                            if not command.lower().__contains__('min'):
                                query1_function_list.append(f"MIN function NOT used")
                            if not command.lower().__contains__('max'):
                                query1_function_list.append(f"MAX function NOT used")
                            if not command.lower().__contains__('round'):
                                query1_function_list.append(f"ROUND function NOT used")
                            if not command.lower().__contains__('datediff'):
                                query1_function_list.append(f"DATEDIFF function NOT used")
                    
                    q2_join_counter = 0
                    q2_concat_counter = 0
                    if a_number == 3: # Query 2
                        if command.lower().__contains__('select'):
                            if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                                for word in command.split():
                                    if word.lower() == 'as':
                                        alias_counter += 1
                            if not command.lower().__contains__('from'):
                                query2_clause_list.append(f"FROM Clause NOT used")
                            if command.lower().__contains__('inner join') or command.lower().__contains__('join'):
                                for word in command.split():
                                    if word.lower() == 'join':
                                        q2_join_counter += 1
                                query2_function_list.append(f"INNER JOIN used {q2_join_counter}/4 times")
                            if not command.lower().__contains__('inner join') or not command.lower().__contains__('join'):
                                query2_clause_list.append(f"INNER JOIN Clause NOT used")
                            if not command.lower().__contains__('where'):
                                query2_clause_list.append(f"WHERE Clause NOT used")
                            if not command.lower().__contains__('group by'):
                                query2_clause_list.append(f"GROUP BY Clause NOT used")
                            if command.lower().__contains__('concat'):
                                for word in command.split():
                                    if word.lower() == 'concat(ag.city,' or word.lower() == 'concat(ag2.city,':
                                        q2_concat_counter += 1
                                query2_function_list.append(f"CONCAT used {q2_concat_counter}/4 times")
                            if not command.lower().__contains__('count'):
                                query2_function_list.append(f"COUNT function NOT used")
                            

                    q3_join_counter = 0
                    q3_concat_counter = 0
                    if a_number == 4: # Query 3
                        if command.lower().__contains__('select'):
                            if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                                for word in command.split():
                                    if word.lower() == 'as':
                                        alias_counter += 1
                            if not command.lower().__contains__('from'):
                                query3_clause_list.append(f"FROM Clause NOT used")
                            if command.lower().__contains__('inner join') or command.lower().__contains__('join'):
                                for word in command.split():
                                    if word.lower() == 'join':
                                        q3_join_counter += 1
                                query3_function_list.append(f"INNER JOIN used {q3_join_counter}/4 times")
                            if not command.lower().__contains__('inner join') or not command.lower().__contains__('join'):
                                query3_clause_list.append(f"INNER JOIN Clause NOT used")
                            if not command.lower().__contains__('where'):
                                query3_clause_list.append(f"WHERE Clause NOT used")
                            if not command.lower().__contains__('group by'):
                                query3_clause_list.append(f"GROUP BY Clause NOT used")
                            if not command.lower().__contains__('order by'):
                                query3_clause_list.append(f"ORDER BY Clause NOT used")
                            if command.lower().__contains__('concat'):
                                for word in command.split():
                                    if word.lower() == 'concat(ag.city,' or word.lower() == 'concat(ag2.city,' or word.lower() == 'concat(\'$\',':
                                        q3_concat_counter += 1
                                query3_function_list.append(f"CONCAT used {q3_concat_counter}/5 times")
                            if not command.lower().__contains__('sum'):
                                query3_function_list.append(f"SUM function NOT used")

                    q4_join_counter = 0
                    q4_concat_counter = 0
                    if a_number == 5: # Query 4
                        if command.lower().__contains__('select'):
                            if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                                for word in command.split():
                                    if word.lower() == 'as':
                                        alias_counter += 1
                            if not command.lower().__contains__('from'):
                                query4_clause_list.append(f"FROM Clause NOT used")
                            if command.lower().__contains__('inner join') or command.lower().__contains__('join'):
                                for word in command.split():
                                    if word.lower() == 'join':
                                        q4_join_counter += 1
                                query4_function_list.append(f"INNER JOIN used {q4_join_counter}/4 times")
                            if not command.lower().__contains__('inner join') or not command.lower().__contains__('join'):
                                query4_clause_list.append(f"INNER JOIN Clause NOT used")
                            if not command.lower().__contains__('where'):
                                query4_clause_list.append(f"WHERE Clause NOT used")
                            if not command.lower().__contains__('group by'):
                                query4_clause_list.append(f"GROUP BY Clause NOT used")
                            if not command.lower().__contains__('having'):
                                query4_clause_list.append(f"HAVING Clause NOT used")
                            if command.lower().__contains__('concat'):
                                for word in command.split():
                                    if word.lower() == 'concat(ag.city,' or word.lower() == 'concat(ag2.city,' or word.lower() == 'concat(\'$\',':
                                        q4_concat_counter += 1
                                query4_function_list.append(f"CONCAT used {q4_concat_counter}/5 times")
                            if not command.lower().__contains__('avg'):
                                query4_function_list.append(f"AVG function NOT used")
                            
                    q5_join_counter = 0
                    q5_concat_counter = 0
                    q5_count_counter = 0
                    if a_number == 6: # Query 5
                        if command.lower().__contains__('select'):
                            if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                                for word in command.split():
                                    if word.lower() == 'as':
                                        alias_counter += 1
                            if not command.lower().__contains__('from'):
                                query5_clause_list.append(f"FROM Clause NOT used")
                            if command.lower().__contains__('inner join') or command.lower().__contains__('join'):
                                for word in command.split():
                                    if word.lower() == 'join':
                                        q5_join_counter += 1
                                query5_function_list.append(f"INNER JOIN used {q5_join_counter}/4 times")
                            if not command.lower().__contains__('inner join') or not command.lower().__contains__('join'):
                                query5_clause_list.append(f"INNER JOIN Clause NOT used")
                            if not command.lower().__contains__('where'):
                                query5_clause_list.append(f"WHERE Clause NOT used")
                            if not command.lower().__contains__('group by'):
                                query5_clause_list.append(f"GROUP BY Clause NOT used")
                            if not command.lower().__contains__('order by'):
                                query5_clause_list.append(f"ORDER BY Clause NOT used")
                            if not command.lower().__contains__('case'):
                                query5_clause_list.append(f"CASE Clause NOT used")
                            if command.lower().__contains__('concat'):
                                for word in command.split():
                                    if word.lower() == 'concat(ag.city,' or word.lower() == 'concat(ag2.city,' or word.lower() == 'concat(\'$\',':
                                        q5_concat_counter += 1
                                query5_function_list.append(f"CONCAT used {q5_concat_counter}/5 times")
                            if not command.lower().__contains__('sum'):
                                query5_function_list.append(f"SUM function NOT used")
                            if command.lower().__contains__('count'):
                                for word in command.split():
                                    if word.lower() == 'count(b.passenger_id)' or word.lower() == 'count(p.passenger_id)' or word.lower() == 'count(b.passenger_id),':
                                        q5_count_counter += 1
                                query5_function_list.append(f"COUNT used {q5_count_counter}/2 times")


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
                    new_query5c_list = format_list(query5_clause_list)
                    new_query5f_list = format_list(query5_function_list)

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
                            elif a_number == 6:
                                # debug.write(new_query5_list)
                                if len(new_query5c_list) == 0:
                                    answer.write(f"All Clauses accounted for\n")
                                else:
                                    answer.write(f"{new_query5c_list}\n")

                            answer.write("----FUNCTIONS----\n")
                            if a_number == 2:
                                # debug.write(new_query1_list)
                                if len(new_query1f_list) != 0:
                                    answer.write(f"{new_query1f_list}\n")
                                else:
                                    answer.write(f"All Functions accounted for\n")
                            if a_number == 3:
                                # debug.write(new_query2_list)
                                if len(new_query2f_list) != 0:
                                    answer.write(f"{new_query2f_list}\n")
                                else:
                                    answer.write(f"All Functions accounted for\n")
                            if a_number == 4:
                                # debug.write(new_query3_list)
                                if len(new_query3f_list) != 0:
                                    answer.write(f"{new_query3f_list}\n")
                                else:
                                    answer.write(f"All Functions accounted for\n")
                            if a_number == 5:
                                # debug.write(new_query4_list)
                                if len(new_query4f_list) != 0:
                                    answer.write(f"{new_query4f_list}\n")
                                else:
                                    answer.write(f"All Functions accounted for\n")
                            if a_number == 6:
                                # debug.write(new_query5_list)
                                if len(new_query5f_list) != 0:
                                    answer.write(f"{new_query5f_list}\n")
                                else:
                                    answer.write(f"All Functions accounted for\n")
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
                    os.remove(f"{directory}\\week11answers.txt")
                elif os_name == 'Linux' or os_name == 'Darwin':
                    os.remove(f"{directory}/week11answers.txt")
                print("Files Deleted")
            else:
                f.close()
                print("Files Kept")

