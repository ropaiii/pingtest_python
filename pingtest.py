import subprocess
import sys

def pingtest_run(ip : str) -> bool:
    cmd : str = f"ping {ip}"
    print(f"Pinging {ip}...")
    try:
        output : int = subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        if output == 0:
            return True
        else:
            return False
    except subprocess.TimeoutExpired:
        return False
    except Exception:
        return False


def main(filename : str) -> None:


    try:
        with open(filename, "r") as file:
            ipadresslist : list = [line.strip() for line in file if line.strip()]
            successip: list = list()
            failsip: list = list()

        if not ipadresslist:
            print("No IP-adresses found!!!!")
            return

        for ip in ipadresslist:
            if pingtest_run(ip):
                print("Ping test successful!!!")
                successip.append(ip)

            else:
                print("Ping test failed!!!")
                failsip.append(ip)

        print("\nSuccessful IP-adresses:")
        for i in successip:
            print(i)
        print("\nFailed IP-adresses:")
        for i in failsip:
            print(i)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Usage: python pingtest.py filename")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
