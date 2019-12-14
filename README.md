Currently, this botnet command and control center runs on localhost. In order to run, use the command 'flask run' in the root directory. Then navigate to http://localhost:5000/. 

This project is the framework for a botnet that operates through ssh. Users can add bots they have found by completing the host, username, and password fields. Then, by entering a unix command the command field, all the bots in the network will do the same command. This process takes a little while (up to a minute).

An example of bots that could be added to this network are ones that have ssh ports open with no authentication required or ones with default usernames and passwords. This is how some of the most well-known botnets were built. A simple search on Shodan yielded hundreds of IoT devices with weak ssh security.
