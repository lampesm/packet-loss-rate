# packet-loss-rate

In this project, you will learn how to monitor packets passing through your network interface and calculate the percentage of errors.

# requirements

- tshark
- poetry
- python3.6+

# Installation

Add the Wireshark and TShark repository:

`sudo add-apt-repository -y ppa:wireshark-dev/stable`

Install TShark:

`sudo apt install -y tshark`

Run the following command to add current user to a wireshark group:

`sudo usermod -a -G wireshark $USER`

In order to make changes to take effect, logout and login to your machine. After reconnection, you can check TShark version:

`tshark --version`

Execute tshark command without any arguments to start capturing packets on default network interface:

`tshark`

We can find network interfaces which are available to the TShark with command:

`tshark -D`

The -i option allows to capture packets on specific network interface.

`tshark -i ens33`

You can use the following commands to view more options from tshark

`tshark --help`

`man tshark`