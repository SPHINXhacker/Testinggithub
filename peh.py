import sys
import asyncio
from time import sleep
from random import choice
import aiohttp
from pyrogram import Client
from pyrogram import errors as py_errors
from os import system, name
from colorama import init, Fore, Style
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

init()

is_steal = False

example_usernames = ['nadiimi67']

class SpadSec:
    colors = [Fore.RED, Fore.BLUE, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.YELLOW]

    def cleaner(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def logo_printer(self):
        self.cleaner()
        logo = """
███████╗██████╗  █████╗ ██████╗ ███████╗███████╗ ██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════
███████╗██████╔╝███████║██║  ██║███████╗█████╗  ██║
╚════██║██╔═══╝ ██╔══██║██║  ██║╚════██║██╔══╝  ██║
███████║██║     ██║  ██║██████╔╝███████║███████╗╚██████╗
╚══════╝╚═╝     ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝
        """

        _logo_enumer = 0
        for char in logo:
            if _logo_enumer <= 343:
                sys.stdout.write(f"{choice(self.colors)}{char}{Style.RESET_ALL}")
                sys.stdout.flush()
                _logo_enumer += 1
                sleep(0.002)
            else:
                sys.stdout.write(f"{self.colors[3]}{char}{Style.RESET_ALL}")
                sys.stdout.flush()
                sleep(0.002)


class Stealer:
    colors = [Fore.RED, Fore.BLUE, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.YELLOW]

    async def create_channel(self, username):
        async with Client(
                "nadimi27",
                api_id=28074609,
                api_hash="1dd95048086379887dcdd5af8bdebc4a",
                takeout=False
        ) as client:
            try:
                channel = await client.create_channel(username, "@nadiimi")
                await client.set_chat_username(channel.id, username)
                print(f"{Fore.YELLOW}Stolen {username}{Style.RESET_ALL}")
            except py_errors.UsernameInvalid:
                print(f"{Fore.RED}{username} is invalid.{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")
                return

    async def checker(self, usernames):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context), connector_owner=False) as session:
            try:
                tasks = []
                for username in usernames:
                    tasks.append(self.check_username(session, username))

                await asyncio.gather(*tasks)
            except Exception as e:
                print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")

    async def check_username(self, session, username):
        try:
            async with session.get(f"https://t.me/{username}", timeout=5) as response:
                text = await response.text()
                if "</a> right away." in text:
                    await self.create_channel(username)
                    await asyncio.sleep(5)
                else:
                    print(f"{Fore.RED}{username} is taken.{Style.RESET_ALL}")
        except (aiohttp.ClientError, aiohttp.ClientConnectorError) as e:
            print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")
            await asyncio.sleep(1)
        except SystemExit:
            raise

async def main():
    try:
        logo = SpadSec()
        logo.logo_printer()

        usernames = example_usernames

        print(f"{Fore.YELLOW}Usernames: {', '.join(usernames)}{Style.RESET_ALL}")

        while True:
            chunked_usernames = [usernames[i:i + 13] for i in range(0, len(usernames), 13)]
            steal = Stealer()
            await asyncio.gather(*[steal.checker(chunk) for chunk in chunked_usernames])
            await asyncio.sleep(0.5)
            if is_steal:
                break

    except KeyboardInterrupt:
        print(f"{Fore.YELLOW}\nGoodbye <3{Style.RESET_ALL}")


if __name__ == "__main__":
    asyncio.run(main())
