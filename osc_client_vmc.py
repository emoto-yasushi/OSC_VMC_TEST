import argparse

from pythonosc import udp_client

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", default="127.0.0.1",help="The ip of the OSC server")
	parser.add_argument("--port", type=int, default=39540,help="The port the OSC server is listening on")
	args = parser.parse_args()

	client = udp_client.SimpleUDPClient(args.ip, args.port)

	while(True):
		client.send_message("/VMC/Ext/Bone/Pos", ["Head",0.0,0.0,0.0,0.0687,0.1788,-0.0297,-0.9798])
		client.send_message("/VMC/Ext/Bone/Pos", ["Neck",0.0,0.0,0.0,0.0687,0.1788,-0.0297,-0.9798])
		client.send_message("/VMC/Ext/Bone/Pos", ["Spine",0.0,0.0,0.0,0.0687,0.1788,-0.0297,-0.9798])
		client.send_message("/VMC/Ext/Blend/Val", ["A",1.0])
		client.send_message("/VMC/Ext/Blend/Val", ["Blink_L",1.0])
		client.send_message("/VMC/Ext/Blend/Val", ["Blink_R",1.0])
		client.send_message("/VMC/Ext/Blend/Apply", "")
