import argparse
import threading
import argparse
import pythonosc
from pythonosc import osc_server
from pythonosc import dispatcher

def receive_VMC_OSC_BlendShape(unused_addr,BlendShapeName_args,Value):
	print("BlendShapeName:" + BlendShapeName_args + "\n")
	#print("BlendShapeValue:" + str(Value) + "\n")

def receive_VMC_OSC_Pos(unused_addr,BoneName,Value0,Value1,Value2,Value3,Value4,Value5,Value6):
	print("BoneName:"+BoneName + "\n")
	#print("BoneValues:" + str(Value0) + "," + str(Value1) + "," + str(Value2) + "," + str(Value3) + "," + str(Value4) + "," + str(Value5) + "," + str(Value6) + "\n")
	
if __name__ == "__main__":
	vmc_dispatcher = dispatcher.Dispatcher()
	vmc_dispatcher.map("/VMC/Ext/Blend/Val", receive_VMC_OSC_BlendShape)
	vmc_dispatcher.map("/VMC/Ext/Bone/Pos", receive_VMC_OSC_Pos)

	vmc_recieve_server = osc_server.ThreadingOSCUDPServer(("", 39540), vmc_dispatcher)

	vmc_recieve_thread = threading.Thread(target=vmc_recieve_server.serve_forever)
	vmc_recieve_thread.start()
