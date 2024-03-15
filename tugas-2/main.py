import os
import re
import colorama
import subprocess

colorama.init()
print(f"{colorama.Fore.YELLOW}Running tests for:{colorama.Style.RESET_ALL} {os.path.dirname(os.getcwd())}")

all_modules = list(filter(lambda s: "main.py" in s.lower(), 
                        [a for a in list(map(lambda d: list(map(lambda f: 
                        os.path.join(os.getcwd(), d, f), os.listdir(d))),
                        filter(lambda d: os.path.isdir(d),os.listdir(".")))) for a in a]))

for module in all_modules:
    print(f"\nRunning {module}")
    output = subprocess.check_output(["python", module]).decode('utf-8')
    colored_output = ' '.join([[f"{colorama.Fore.RED}False{colorama.Style.RESET_ALL}", 
                                f"{colorama.Fore.GREEN}True{colorama.Style.RESET_ALL}"][val.strip().lower() == "true"]
                               if val.strip().lower() in ["true", "false"] 
                               else val
                               for val in re.split(" +", output, flags=re.I|re.M)])
    print(colored_output)