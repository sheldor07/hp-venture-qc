import socket
import threading
import time


class MockTelnetServer:
    def __init__(self, host="localhost", port=23, image_path="input/sample_image.jpg"):
        self.host = host
        self.port = port
        self.image_path = image_path
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Mock Telnet server started on {self.host}:{self.port}")

    def handle_client(self, client_socket):
        try:
            # Send initial prompt
            client_socket.sendall(b"Welcome to Mock Camera\nlogin: ")
            time.sleep(1)

            # Read username
            client_socket.recv(1024)
            client_socket.sendall(b"Password: ")
            time.sleep(1)

            # Read password
            client_socket.recv(1024)
            client_socket.sendall(b"\n> ")

            while True:
                # Read command
                command = client_socket.recv(1024).strip()
                if command == b"GI":
                    # Read and send image data
                    with open(self.image_path, "rb") as image_file:
                        image_data = image_file.read()
                        client_socket.sendall(image_data + b"\n> ")
                else:
                    client_socket.sendall(b"Unknown command\n> ")
        except ConnectionResetError:
            print("Client disconnected")
        finally:
            client_socket.close()

    def start(self):
        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                print(f"Connection from {addr}")
                client_handler = threading.Thread(
                    target=self.handle_client, args=(client_socket,)
                )
                client_handler.start()
        except KeyboardInterrupt:
            print("Shutting down server")
        finally:
            self.server_socket.close()


if __name__ == "__main__":
    server = MockTelnetServer(image_path="sample_image.jpg")
    server.start()
