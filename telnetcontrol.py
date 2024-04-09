import asyncio
import telnetlib3
from threading import Thread
from asyncio import Future
from concurrent.futures import ThreadPoolExecutor


class TelnetClient:
    def __init__(self, ip, port=23, verbose=True):
        self.ip = ip
        self.port = port
        self.verbose = verbose
        self.reader = None
        self.writer = None
        self.executor = ThreadPoolExecutor(max_workers=1)

        # Initialize the loop here, but don't start it yet
        self.loop = asyncio.new_event_loop()

    def start_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def connect(self):
        # Make sure the loop is running in its own thread.
        if not self.loop.is_running():
            self.thread = Thread(target=self.start_loop)
            self.thread.start()

        # Wait for the connection to be established before returning.
        conn_future = asyncio.run_coroutine_threadsafe(self._connect(), self.loop)
        conn_future.result()  # This will raise exceptions if the connection failed

    async def _connect(self):
        self.reader, self.writer = await telnetlib3.open_connection(
            self.ip, self.port, connect_minwait=1.0
        )
        # Wait for a welcome message or connection confirmation for 3 seconds.
        try:
            welcome_message = await asyncio.wait_for(self.reader.read(1024), 3)
            if welcome_message and self.verbose:
                print(f"Received initial message: {welcome_message}")
        except asyncio.TimeoutError:
            # If no message is received in 3 seconds, just move on.
            if self.verbose:
                print("No initial message received within 3 seconds.")
        except Exception as e:
            # Catch any other exceptions that may occur.
            if self.verbose:
                print(f"An error occurred while receiving the initial message: {e}")
        # Proceed with other operations, assuming the connection is now ready.

        except asyncio.TimeoutError:
            # If no message is received in 3 seconds, just move on.
            if self.verbose:
                print("No initial message received within 3 seconds.")
        except Exception as e:
            # Catch any other exceptions that may occur.
            if self.verbose:
                print(f"An error occurred while receiving the initial message: {e}")
        # Proceed with other operations, assuming the connection is now ready.

    def send_command(self, command):
        future = asyncio.run_coroutine_threadsafe(
            self._send_command(command), self.loop
        )
        return future.result()  # Wait for the result synchronously

    async def _send_command(self, command):
        if self.verbose:
            print(f"Sent: {command}")
        self.writer.write(command + "\r\n")  # Send command with CR LF
        await self.writer.drain()  # Ensure the command is sent out

        response = ""
        while True:
            try:
                chunk = await asyncio.wait_for(self.reader.read(1024), timeout=3)
                if chunk:
                    response += chunk
                    # Check for a known prompt or end-of-message indicator
                    if response.strip().endswith(">"):
                        break
            except asyncio.TimeoutError:
                # Break the loop if there's a timeout waiting for the response
                break

        # Final processing of the response
        response = response.strip(">").strip()
        if self.verbose:
            print(f"Received: {response}")
        return response

    def close(self):
        asyncio.run_coroutine_threadsafe(self._close(), self.loop)
        # This is to stop the loop and join the thread:
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join()
        self.executor.shutdown(wait=True)

    async def _close(self):
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join()  # Move the join here to ensure it waits for the loop to stop

    def __del__(self):
        self.close()
        self.thread.join()
