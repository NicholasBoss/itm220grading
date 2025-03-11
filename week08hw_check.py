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
                        [[' a'], ['Turbo B'], ['Jon B'], 
                        ['Pimp C'], ['Chuck D'], ['Heavy D'], ['Barry D'], 
                        ['Kenny G'], ['Warren G'], 
                        ['Anthony DiFranco, I'], ['Joe Pichler, I'], ['Ross Bagley, I'], 
                        ['Josh Byrne, I'], ['Juan Carlos, I'], ['Eric Austin, I'], 
                        ['Gregory Smith, I'], ['Peter Sjoberg, I'], ['LL Cool J'], 
                        ['David J'], ['Ray J'], ['Ya Kidd K'], ['Baby M'], ['Master P'], 
                        ['Mr. T'], ['Tony Jackson, V'], ['Mark Morris, V'], 
                        ['Morgan Smith, V'], ['Brett Anderson, V'], ['Mark Allen, V'], 
                        ['Peter Phillips, V'], ['Steve Burns, V'], ['Peter Sullivan, V'], 
                        ['Patrick Scott, V'], ['Nick Brown, V'], ['Adam Levine, V'], 
                        ['Josh McGuire, V'], ['Patrick Flynn, V'], ['Eric Harris, V'], 
                        ['Stephen Murphy, V'], ['David Reynolds, V'], ['Michael Lange, V'], 
                        ['Sandy , V'], ['Patrick Halladay, V'], ['Jeff Howard, V'], 
                        ['Morgan Miller, V'], ['Michael Cronin, V'], ['Andrew White, V'], 
                        ['Neal X'], ['James Scott, X'], ['Terminator X'], ['Scott Taylor, X'], 
                        ['Michael Moore, X']],
                        # ---------------------------------------------------------------------
                        # Question 2
                        # ---------------------------------------------------------------------
                        [['Inez Foxx'], ['Nikki Sixx'], ['Jamie Foxx'], 
                        ['Corey Foxx'], ['John Murphy, XXX'], ['Gunner Sixx']],
                        # ---------------------------------------------------------------------
                        # Question 3
                        # ---------------------------------------------------------------------
                        [['Boeing 747', ' Die Boeing 747']],
                        # ---------------------------------------------------------------------
                        # Question 4
                        # ---------------------------------------------------------------------
                        [['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Domiziano Arcangeli', '$2.47', '$2', '$2'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Rob Johnson', '$10.79', '$11', '$10'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Dennis Arduini', '$18.37', '$18', '$18'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Manny Malhotra', '$19.63', '$20', '$19'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Myles Murphy', '$21.23', '$21', '$21'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Piotr Adamczyk', '$24.73', '$25', '$24'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Jared Micah Herman', '$25.15', '$25', '$25'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Michelle Kwan', '$27.79', '$28', '$27'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Albert Belle', '$35.23', '$35', '$35'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Hitomi Manaka', '$35.25', '$35', '$35'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Famke Janssen', '$35.27', '$35', '$35'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Bryan Sandifer', '$38.61', '$39', '$38'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Tom Smothers', '$40.31', '$40', '$40'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Robert Duncan McNeill', '$44.14', '$44', '$44'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Troy Hudson', '$46.90', '$47', '$46'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Peerless Price', '$52.52', '$53', '$52'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Kelly Hendry', '$54.25', '$54', '$54'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Rasheed Marshall', '$60.45', '$60', '$60'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Otis Smith', '$63.62', '$64', '$63'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Edi Brokoli', '$66.77', '$67', '$66'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Wilmont Perry', '$74.56', '$75', '$74'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Emma Wray', '$79.43', '$79', '$79'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Bertrand Blier', '$86.05', '$86', '$86'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'John Buck', '$86.18', '$86', '$86'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Francesco Caruso', '$96.93', '$97', '$96'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Tristan Ulloa', '$103.08', '$103', '$103'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Spencer Reid', '$103.13', '$103', '$103'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Yaroslav Korolev', '$103.99', '$104', '$103'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Braddon Mendelson', '$110.04', '$110', '$110'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Konstantin Pushkarev', '$112.85', '$113', '$112'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Roselyn Sanchez', '$117.35', '$117', '$117'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'George Martin', '$119.94', '$120', '$119'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Dakota Brinkman', '$119.98', '$120', '$119'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Yvan Cournoyer', '$121.66', '$122', '$121'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Niki Taylor', '$124.32', '$124', '$124'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Eva Longoria Parker', '$125.19', '$125', '$125'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Kai Fischer, II', '$127.67', '$128', '$127'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Michael Weatherly', '$130.80', '$131', '$130'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Philip Mayor', '$131.82', '$132', '$131'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Ruben Studdard', '$132.51', '$133', '$132'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Collien Fernandes', '$133.17', '$133', '$133'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Katherine Berman', '$135.12', '$135', '$135'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Andreas Karrer', '$135.58', '$136', '$135'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Charles Bronfman', '$137.73', '$138', '$137'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'James Paul Roeske, II', '$138.93', '$139', '$138'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Jean-Francois Jacques', '$143.27', '$143', '$143'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Doug DeVore', '$157.34', '$157', '$157'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Ben Curtis', '$162.56', '$163', '$162'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Michael Pitt, II', '$170.01', '$170', '$170'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Justin Griffith', '$173.26', '$173', '$173'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Kenoy Kennedy', '$176.58', '$177', '$176'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Jussi Timonen', '$183.23', '$183', '$183'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Vincent Gallo', '$189.85', '$190', '$189'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'John Barnes', '$191.60', '$192', '$191'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Scott McEwan', '$193.12', '$193', '$193'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'David Doerksen', '$194.56', '$195', '$194'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Steve Farris', '$200.42', '$200', '$200'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Ellen Burstyn', '$202.63', '$203', '$202'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Austin Sanders', '$203.60', '$204', '$203'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Eric Kretz', '$209.30', '$209', '$209'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Doug Bass', '$213.82', '$214', '$213'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Jason Webster', '$214.35', '$214', '$214'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Michael Naegel, II', '$220.50', '$221', '$220'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Brandon Backe', '$224.05', '$224', '$224'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Earl Riley', '$226.73', '$227', '$226'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Devon Werkheiser', '$229.33', '$229', '$229'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Dan Capecci', '$236.11', '$236', '$236'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Jack Sojka', '$239.33', '$239', '$239'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Damian Smith', '$244.93', '$245', '$244'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', ' Arcy', '$253.49', '$253', '$253'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'John Dye', '$256.08', '$256', '$256'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Alistair Griffin', '$256.80', '$257', '$256'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'George Linberger', '$259.72', '$260', '$259'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Peter Frodin', '$262.92', '$263', '$262'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Michael Geary', '$263.76', '$264', '$263'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Elizardo Ramirez', '$269.97', '$270', '$269'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Bryan Fletcher', '$280.65', '$281', '$280'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Don Davis', '$283.42', '$283', '$283'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Mick Jones', '$284.02', '$284', '$284'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Marc Robert Epstein', '$284.06', '$284', '$284'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Dan Goodspeed', '$284.60', '$285', '$284'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', ' Mireia', '$285.02', '$285', '$285'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Graham McGrath', '$290.66', '$291', '$290'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Terrence Barber', '$293.23', '$293', '$293'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Alfred Molina', '$293.61', '$294', '$293'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Tim Belcher', '$296.84', '$297', '$296'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Patrick Ewing', '$300.41', '$300', '$300'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Nate Kaeding', '$301.14', '$301', '$301'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Ed Jasper', '$301.33', '$301', '$301'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Billy Francis', '$303.98', '$304', '$303'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Arthur Crenshaw', '$312.69', '$313', '$312'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Brian L. Hunter', '$312.76', '$313', '$312'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Krist Novoselic', '$314.30', '$314', '$314'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Ian McShane', '$314.85', '$315', '$314'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Mike Miller', '$315.21', '$315', '$315'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Antonio De la Torre', '$322.22', '$322', '$322'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Charlie Thompson', '$323.26', '$323', '$323'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Lee Loughnane', '$329.99', '$330', '$329'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Ricky Martin', '$332.65', '$333', '$332'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Dawn Lyn', '$333.02', '$333', '$333'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Niklas Kronwall', '$333.18', '$333', '$333'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Richie Sambora', '$336.78', '$337', '$336'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'David Brooks', '$339.71', '$340', '$339'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Chris Poston', '$342.97', '$343', '$342'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Carlos Garay', '$344.95', '$345', '$344'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Jane Seymour', '$345.68', '$346', '$345'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Haloti Ngata', '$347.77', '$348', '$347'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Joe West', '$348.71', '$349', '$348'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Richard Rust', '$350.86', '$351', '$350'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Martin Kellett', '$354.09', '$354', '$354'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', ' Hara', '$354.10', '$354', '$354'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Nigel Olsson', '$357.62', '$358', '$357'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Leah Pinsent', '$359.68', '$360', '$359'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Dwayne Schintzius', '$363.38', '$363', '$363'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Cynthia Nixon', '$364.08', '$364', '$364'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Tyra Banks', '$371.94', '$372', '$371'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Lamont Bentley', '$372.49', '$372', '$372'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Joe Lepsis', '$382.93', '$383', '$382'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Seimone Augustus', '$392.38', '$392', '$392'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Chad Dukes', '$393.38', '$393', '$393'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Leslie Joan Corn', '$394.67', '$395', '$394'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Joe Johnson', '$396.66', '$397', '$396'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Noel McCalla', '$399.23', '$399', '$399'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Jens Becker', '$401.63', '$402', '$401'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Davis Drewiske', '$404.90', '$405', '$404'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Tone Lohr', '$406.70', '$407', '$406'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Ben Perry, III', '$413.38', '$413', '$413'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Jim Anderson', '$416.74', '$417', '$416'],
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Glenn Gregory', '$417.41', '$417', '$417'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Robert Bradford', '$418.93', '$419', '$418'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Irma Thomas', '$420.38', '$420', '$420'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Roy Adams', '$421.07', '$421', '$421'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Ian Grushka', '$426.14', '$426', '$426'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Gunilla Poppe', '$426.58', '$427', '$426'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Junior Tagaloa', '$428.62', '$429', '$428'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Wim Peters, II', '$429.62', '$430', '$429'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Chosei Funahara', '$444.43', '$444', '$444'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Simon Fraser', '$449.58', '$450', '$449'],
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Max Perlich', '$456.82', '$457', '$456'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Gabor Harsanyi', '$457.39', '$457', '$457'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Sara Bruner', '$459.41', '$459', '$459'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'John McTiernan', '$460.45', '$460', '$460'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Taurean Green', '$460.75', '$461', '$460'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Jason Zent', '$463.23', '$463', '$463'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Coby Karl', '$473.36', '$473', '$473'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Lynda Johnson', '$476.82', '$477', '$476'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Lucas Belvaux', '$477.28', '$477', '$477'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Tom Flynn, III', '$478.03', '$478', '$478'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Augie Ojeda', '$481.21', '$481', '$481'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Ernest Thomas', '$485.68', '$486', '$485'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Simon Dekassian', '$488.32', '$488', '$488'], 
                         ['AF1837', 'Jun 01, 2015 07:24:00 AM', 'Eric Stults', '$491.15', '$491', '$491']],
                        # ---------------------------------------------------------------------
                        # Question 5
                        # ---------------------------------------------------------------------
                        [['Jun 01, 2015 03:40:00 AM', 'Jun 02, 2015 01:00:00 AM', 21, 1, 9], 
                         ['Jun 01, 2015 01:36:00 AM', 'Jun 01, 2015 10:53:00 PM', 21, 0, 9], 
                         ['Jun 01, 2015 10:30:00 AM', 'Jun 02, 2015 07:50:00 AM', 21, 1, 9], 
                         ['Jun 01, 2015 07:03:00 AM', 'Jun 02, 2015 04:08:00 AM', 21, 1, 9], 
                         ['Jun 01, 2015 09:27:00 PM', 'Jun 02, 2015 07:13:00 PM', 21, 1, 9], 
                         ['Jun 01, 2015 09:12:00 PM', 'Jun 02, 2015 07:02:00 PM', 21, 1, 9], 
                         ['Jun 01, 2015 09:47:00 AM', 'Jun 02, 2015 06:55:00 AM', 21, 1, 9], 
                         ['Jun 01, 2015 02:17:00 PM', 'Jun 02, 2015 11:44:00 AM', 21, 1, 9], 
                         ['Jun 01, 2015 01:43:00 PM', 'Jun 02, 2015 11:15:00 AM', 21, 1, 9], 
                         ['Jun 01, 2015 10:20:00 AM', 'Jun 02, 2015 07:45:00 AM', 21, 1, 9]],
                        # ---------------------------------------------------------------------
                        # Question 6
                        # ---------------------------------------------------------------------
                        [['AL9073', 'Maria Barranco', 1], 
                         ['AL9073', 'Paul Benedict', 2], 
                         ['AL9073', 'Dewon Brazelton', 3], 
                         ['AL9073', 'Billy Aaron Brown', 4], 
                         ['AL9073', 'Genevieve Bujold', 5], 
                         ['AL9073', 'Edna Campbell', 6], 
                         ['AL9073', 'Dick Cavett', 7], 
                         ['AL9073', 'Charlotte Church', 8], 
                         ['AL9073', 'Tony Chursky', 9], 
                         ['AL9073', 'Lola Falana', 10], 
                         ['AL9073', 'Willie Fears', 11], 
                         ['AL9073', 'Aaron Flacconi', 12], 
                         ['AL9073', 'Ulrike Folkerts', 13], 
                         ['AL9073', 'Christine Harwart', 14], 
                         ['AL9073', 'Lauren Hewett', 15], 
                         ['AL9073', 'Dinah Hinz', 16], 
                         ['AL9073', 'Paul Jones', 17], 
                         ['AL9073', 'Brad Leeb', 18], 
                         ['AL9073', 'Carlton Liggins', 19], 
                         ['AL9073', 'Tony Lowery', 20], 
                         ['AL9073', 'Geordie Lyall', 21], 
                         ['AL9073', 'Mark Macon', 22], 
                         ['AL9073', 'Eddie Rabbitt', 23], 
                         ['AL9073', 'Kady Riklis', 24], 
                         ['AL9073', 'Todd Yoder', 25]]]

alias_counter = 0
total_aliases = 18
total_queries = 6

# open the test folder and read the files inside
if os_name == 'Windows':
    print("Windows OS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '\\tempgrades'
    answer = open(f"{directory}\\week08answers.txt", "w")

elif os_name == 'Linux':
    print("Linux Detected")
    directory = '/home/student/Desktop/itm220grading'
    grading_directory = '/home/student/Desktop/itm220grading/tempgrades'
    answer = open(f"{directory}/week08answers.txt", "w")

elif os_name == 'Darwin':
    print("MacOS Detected")
    directory = os.getcwd()
    grading_directory = os.getcwd() + '/tempgrades'
    answer = open(f"{directory}/week08answers.txt", "w")
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
            file_contents = file_contents.replace("SET", "-- ~\SET")
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
        query6_clause_list = []
        query6_function_list = []
        
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
                    if not command.lower().__contains__('from'):
                        query1_clause_list.append(f"FROM Clause NOT used")  
                    if not command.lower().__contains__('where'):
                        query1_clause_list.append(f"WHERE Clause NOT used")                  
                    if not command.lower().__contains__('order by'):
                        query1_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('concat'):
                        query1_function_list.append(f"CONCAT Function NOT used")
                    if not command.lower().__contains__('length'):
                        query1_function_list.append(f"LENGTH Function NOT used")

            if a_number == 3: # Query 2
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 1 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__('from'):
                        query2_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query2_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('and'):
                        query2_clause_list.append(f"AND operator NOT used")
                    if not command.lower().__contains__('like'):
                        query2_clause_list.append(f"LIKE operator NOT used")
                    if not command.lower().__contains__('concat'):
                        query2_function_list.append(f"CONCAT Function NOT used")
                    if not command.lower().__contains__('locate'):
                        query2_function_list.append(f"LOCATE Function NOT used")
                    

            if a_number == 4: # Query 3
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 2 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__('from'):
                        query3_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query3_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('left'):
                        query3_function_list.append(f"LEFT Function NOT used")
                    if not command.lower().__contains__('substring'):
                        query3_function_list.append(f"SUBSTRING Function NOT used")
                    if not command.lower().__contains__('locate'):
                        query3_function_list.append(f"LOCATE Function NOT used")

            q4_join_counter = 0
            q4_date_format_counter = 0
            q4_concat_counter = 0
            if a_number == 5: # Query 4
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 3 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__('from'):
                        query4_clause_list.append(f"FROM Clause NOT used")
                    if command.lower().__contains__('inner join'):
                        for word in command.split():
                            if word.lower() == 'inner':
                                q4_join_counter += 1
                        query4_clause_list.append(f"INNER JOIN Clause used {q4_join_counter} times")
                    if not command.lower().__contains__('inner join'):
                        query4_clause_list.append(f"INNER JOIN Clause NOT used")
                    if not command.lower().__contains__('on'):
                        query4_clause_list.append(f"ON Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query4_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('and'):
                        query4_clause_list.append(f"AND operator NOT used")
                    if not command.lower().__contains__('order by'):
                        query4_clause_list.append(f"ORDER BY Clause NOT used")
                    if command.lower().__contains__('date_format'): # 1 total
                        for word in command.split():
                            if word.lower() == 'date_format(f.departure,':
                                q4_date_format_counter += 1
                        query4_function_list.append(f"DATE_FORMAT Function used {q4_date_format_counter} time")
                    if not command.lower().__contains__('date_format'):
                        query4_function_list.append(f"DATE_FORMAT Function NOT used")
                    if command.lower().__contains__('concat'): # 4 total
                        for word in command.split():
                            if word.lower() == 'concat(\'$\',':
                                q4_concat_counter += 1
                        query4_function_list.append(f"CONCAT Function used {q4_concat_counter} times")
                    if not command.lower().__contains__('concat'):
                        query4_function_list.append(f"CONCAT Function NOT used")
                    if command.lower().__contains__('floor'): # 1 total
                        query4_function_list.append(f"FLOOR Function used")
                    if not command.lower().__contains__('floor'):
                        query4_function_list.append(f"FLOOR Function NOT used")
                    
            q5_date_format_counter = 0
            q5_timestampdiff_counter = 0
            q5_datediff_counter = 0
            if a_number == 6: # Query 5
                if command.lower().__contains__('select'):
                    if command.lower().__contains__(') as ') or command.lower().__contains__(' as ') or command.lower().__contains__(') \''):
                    # count the number of aliases used (there should be 5 in this query)
                        for word in command.split():
                                if word.lower() == 'as':
                                    alias_counter += 1
                    if not command.lower().__contains__('from'):
                        query5_clause_list.append(f"FROM Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query5_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('order by'):
                        query5_clause_list.append(f"ORDER BY Clause NOT used")
                    if not command.lower().__contains__('limit'):
                        query5_clause_list.append(f"LIMIT Clause NOT used")
                    if command.lower().__contains__('date_format'): # 2 total
                        for word in command.split():
                            if word.lower() == 'date_format(f.departure,' or word.lower() == 'date_format(f.arrival,':
                                q5_date_format_counter += 1
                        query5_function_list.append(f"DATE_FORMAT Function used {q5_date_format_counter} times")
                    if not command.lower().__contains__('date_format'):
                        query5_function_list.append(f"DATE_FORMAT Function NOT used")
                    if command.lower().__contains__('timestampdiff'): # 3 total
                        for word in command.split():
                            if word.lower() == 'timestampdiff(hour,':
                                q5_timestampdiff_counter += 1
                        query5_function_list.append(f"TIMESTAMPDIFF Function used {q5_timestampdiff_counter} times")
                    if not command.lower().__contains__('timestampdiff'):
                        query5_function_list.append(f"TIMESTAMPDIFF Function NOT used")
                    if command.lower().__contains__('datediff'): # 2 total
                        for word in command.split():
                            if word.lower() == 'datediff(f.arrival,' or word.lower() == 'floor(datediff(now(),':
                                q5_datediff_counter += 1
                        query5_function_list.append(f"DATEDIFF Function used {q5_datediff_counter} times")
                    if not command.lower().__contains__('datediff'):
                        query5_function_list.append(f"DATEDIFF Function NOT used")
                    if not command.lower().__contains__('now()'): # 1 total
                        query5_function_list.append(f"NOW() Function NOT used")
                    if not command.lower().__contains__('floor'):
                        query5_function_list.append(f"FLOOR Function NOT used")

            q6_join_counter = 0
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
                    if command.lower().__contains__('inner join'): # 2 total
                        for word in command.split():
                            if word.lower() == 'inner':
                                q6_join_counter += 1
                        query6_clause_list.append(f"INNER JOIN Clause used {q6_join_counter} times")
                    if not command.lower().__contains__('inner join'):
                        query6_clause_list.append(f"INNER JOIN Clause NOT used")
                    if not command.lower().__contains__('where'):
                        query6_clause_list.append(f"WHERE Clause NOT used")
                    if not command.lower().__contains__('and'):
                        query6_clause_list.append(f"AND operator NOT used")
                    if not command.lower().__contains__('concat'): # 1 total
                        query6_function_list.append(f"CONCAT Function NOT used")
                    if not command.lower().__contains__('row_number()'):
                        query6_function_list.append(f"ROW_NUMBER Function NOT used")


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
            new_query6c_list = format_list(query6_clause_list)
            new_query6f_list = format_list(query6_function_list)
            

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
                    # 1 is the USE statment
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
                    elif a_number == 7:
                        # debug.write(new_query6_list)
                        if len(new_query6c_list) == 0:
                            answer.write(f"All Clauses accounted for\n")
                        else:
                            answer.write(f"{new_query6c_list}\n")

                    answer.write("----FUNCTIONS----\n")
                    if a_number == 2:
                        # debug.write(new_query1f_list)
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
                    if a_number == 7:
                        # debug.write(new_query6_list)
                        if len(new_query6f_list) != 0:
                            answer.write(f"{new_query6f_list}\n")
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
            os.remove(f"{directory}\\week08answers.txt")
        elif os_name == 'Linux' or os_name == 'Darwin':
            os.remove(f"{directory}/week08answers.txt")
        print("Files Deleted")
    else:
        f.close()
        print("Files Kept")

