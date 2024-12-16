# Overview

The ITM 220 Grading Repository is to be used by graders to grade assignments for the ITM 220 course. This repository is public to allow for easy cloning to the virtual machine provided for the course.

## System Requirements

Access to the AWS Instance provided by the course.

OR 

VS Code

Python 3.11 or higher (Make sure to add to PATH when installing)

MySQL Workbench

MySQL Server

Make sure to add the MySQL Server 8.0/bin folder to the PATH when installation is complete

Access to the airportdb_dump.sql file (2.5 GB). This will install an 8GB database. Normal run time to install depends on the speed of the machine but could take up to 1 hour. Ask the instructor for access to the file.

## How to Set Up the Environment

1. Clone the repository <strong>to the Desktop</strong> of the AWS Instance or your local machine.

2. Open the repository in VS Code.

3. Go to the setup folder and do either of the following
 -  If you are in the AWS instamce, run the `setup.py` file. This will verify that a `student` user exists and grant access to the `student` user for the `airportdb` database.

 - If you are on your local machine, you may need to change the password on line 20 to your root password. Run the `setup.py` file after this change. This will create a `student` user and grant access to the `student` user for the `airportdb` database.

4. Run the `airportdb_dump.sql` file from the terminal using the following command `if you are not in the AWS instance`:
```bash
mysql -u root -p airportdb < airportdb_dump.sql
```
This process will take some time to complete. (Approximately 1 hour)

## How to Grade Assignments

1. Open the assignment homework check you wish to grade. These are named `week##hw_check.py`. Each file can be run separately depending on the assignment you are grading. For assignments to be graded, on first run, the script will create a `tempgrades` folder. All SQL files to be graded will need to go here. <strong>Yes, you can grade multiple assignments at once.</strong>

2. Run the script using the Play button in the top right corner of VS Code. When run, the result will be placed in a file called `week##_answers.txt`. 

3. The `week##_answers.txt` file will contain the results of the grading. The file will contain the following information:
    - The name of the SQL file being graded
    - The total number of aliases used in the file 
    - The number of queries written in the file
    - The number of queries that passed
    - The queries that failed and details about why they failed.

Note: If a student writes comments that use any of the following words, you may have to manually edit their file to recomment the words:
- `CREATE`
- `INSERT`
- `UPDATE`
- `DELETE`
- `SELECT`

These words are used in the grading script and may cause the script to fail if they are used in comments. Even if they are pluralized or in a sentence, the script may fail.

If there are no errors and all queries pass, you may see a result simiar to the following:
```bash
***********************************
File: wk07_john_doe.sql
--------RESULTS-------
24/24 Alias Used
7/7 Queries Written
7/7 Queries Correct
***********************************

***********************************
File: wk07_john_doe.sql
--------RESULTS-------
24/24 Alias Used
7/7 Queries Written
7/7 Queries Correct
***********************************

***********************************
Total Files Graded: 2
***********************************
```

When you are done grading, you can use the prompt given in the terminal to delete all files in the `tempgrades` folder and it will also delete the answers file. This will allow you to grade the next assignment without any issues. Any answer to the prompt other than `yes` will not delete the files in case you do need to edit any files manually. You can quickly run the script again by hitting the up arrow in the terminal and pressing enter or by pressing the Play button again.
