# Team-7
| Name        | Github Username           |
| ------------- |:-------------:|
| Daniel Rodriguez      | drod7946 |
| Jayden Hamilton      | jswizzle325      |
| Austen Lee | buzzerstrafe      |
| Yannick Tchio Tiombo | yttiombo      |

Instructions:

Tkinter should is installed with many default python installations, but it is best to install to be safe. CustomTkinter will need to be installed. 
The Psycopg2, Pillow, and PyGame libraries are necessary to run the program, and are installed through pip. 
Run all of the following commands prior to starting the program to ensure that all necessary libraries are installed:
```
sudo apt install python3-pip
sudo apt-get install python3-tk
pip install Pillow
pip install customtkinter
pip install psycopg2-binary
pip install pygame
```

To run this program, you will need two terminal windows, with both being located in the Team-7 folder on your local machine.

Terminal 1
Run the command:
```
python3 python_traffic_generator_v2.py
```
Enter equipment ids for the players. It is acceptable to just use 1, 2, 3, 4. Leave this terminal waiting.

Terminal 2
Run the command:
```
python3 main.py
```
This will run the main functional body of the program. Enter the player IDs in the first column for their respective teams.
Press enter. If this is a new player, the program will prompt you to enter a name.
For the commands, either the on-screen button or the corresponding key will work. 
Press F12 to clear all names in the game. Press F7 to change the IP address if necessary.
When you are ready to begin the game, press F5. The countdown screen will appear and the music track will begin playing near the 15 second mark.
Once the game begins, the first terminal will begin sending and receiving data with the main program, and scores will update on the play action screen.
After the 6 minute timer is complete, the program will ask if you would like to return to the player entry screen. If not, the program can be closed at this point.
The traffic generator will stop automatically after the game is completed. 


