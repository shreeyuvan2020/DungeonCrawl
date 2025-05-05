import paramiko
import socket
import threading
import curses
import sys
import traceback
# Server settings
HOST = "0.0.0.0"
PORT = 2222
HOST_KEY = paramiko.RSAKey(filename="game_ssh_key")

class GameSSHServer(paramiko.ServerInterface):
    def check_auth_none(self, username):
        return paramiko.AUTH_SUCCESSFUL

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True
    def check_channel_shell_request(self, channel):
        return True
def run_curses_app(channel):
    try:
        sys.stdin = channel.makefile("r")
        sys.stdout = channel.makefile("w")
        sys.stderr = channel.makefile("w")
        from firstlevel import main
        curses.wrapper(main)
    except Exception as e:
        print(f"Error running curses app: {e}")
        traceback.print_exc()
def handle_client(client_socket):
    try:
        transport = paramiko.Transport(client_socket)
        transport.add_server_key(HOST_KEY)
        server = GameSSHServer()
        transport.start_server(server=server)
        print("Skibidi channel activated")
        channel = transport.accept(20)
        print("Skibidi channel opened")
        if channel is None:
            print("No channel opened")
            return
        run_curses_app(channel)
        print("Skibidi aura activated the channel is auramaxxing rn")
    except Exception as e:
        print(f"The skibidi channel is not goonmaxxing: {e}")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        if "transport" in locals():
            transport.close()
        client_socket.close()

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(100)
        print(f"Listening on {HOST}:{PORT}")
    except Exception as e:
        print(f"Server startup error: {e}")
        return

    while True:
        try:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
        except Exception as e:
            print(f"Server loop error: {e}")

if __name__ == "__main__":
    main()