from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server
import socket

MAIN_IN = 7001
MAIN_OUT = 7000

sender_client = udp_client.SimpleUDPClient("127.0.0.1", MAIN_OUT)
sender_client.send_message("/data", 12345)

def handlebar(address, *args):
    print(f"default handle bar attached at {address}: {args}")

if __name__ == "__main__":
    test_disp = dispatcher.Dispatcher()
    test_disp.map("/msp_data", handlebar)

    test_server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", MAIN_IN), test_disp)
    print(f"Listening on {test_server.server_address}")

    try:
        test_server.serve_forever()
    except KeyboardInterrupt:
        print("Interrupted; shutting down the server")
        test_server.shutdown()
    except Exception as ex:
        print(f"Server error: {ex}")
        test_server.shutdown()
