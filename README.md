On the Python side:

6/9/2025: I'm using python-osc to send and recieve data using udp. All that's there now is a default handler and a basic server that recieves messages from the sonifier_comm patch. 

On the Max side:

6/9/2025: Port 7000 can recieve simple messages sent from Python, which are displayed in the Max console. The udpsend object is set up to send a number to the Python console. 

Future plans:

Get a databse working with Python so that I can start populating it with data to sonify. I plan on using MySQL. 

I will figure out exactly how I want to sonify things later. The Python end will mostly be used for formulating the data the way I want and communicating with the database. 
The Max end will likely come later and be the last thing that's completed since that's where the artistic stuff will happen. 

Potential incorporations include algorithmic composition, custom Javascript subpatches for specific needs that may arise, and Jitter visuals. 
Sonifying multiple types of data at the same time using multithreading to make this a multimedia project is my main goal after the main project is developed. 
