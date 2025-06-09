#!/usr/bin/python3
#! coding: utf-8

"""coded by Br3noAraujo"""

import math
import os
import time

# Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    banner = f"""
{WHITE}   ____          _ {RED}__  ___     __     {RESET}
{WHITE}  / __/__  ___ _(_){RED}  |/  /__  / /____ {RESET}
{WHITE} / _// _ \/ _ `/ /{RED} /|_/ / _ \/ __/ _ \\{RESET}
{WHITE}/___/_//_/\_, /_/{RED}_/  /_/\___/\__/\___/{RESET}
{WHITE}         /___/                        {RESET}
"""
    print(banner)
    print(f"{WHITE}Developed by Br3no{RED}Araujo{RESET}\n")

def calculate_displacement(bore, stroke, cylinders):
    """
    Calculates engine displacement in cubic centimeters (cc)
    """
    radius = bore / 2
    area = math.pi * (radius ** 2)
    displacement_per_cylinder = area * stroke
    total_displacement = displacement_per_cylinder * cylinders
    return total_displacement / 1000  # Converting to cc

def main():
    clear_screen()
    show_banner()
    
    try:
        print(f"{YELLOW}Example input for a 600cc motorcycle:{RESET}")
        print(f"{WHITE}Bore: 67mm")
        print(f"Stroke: 42.5mm")
        print(f"Cylinders: 4{RESET}")
        print(f"\n{CYAN}Enter your motorcycle data:{RESET}")
        
        bore = input(f"{GREEN}Enter cylinder bore (mm): {RESET}").replace(",", ".")
        bore = float(bore)
        
        stroke = input(f"{GREEN}Enter piston stroke (mm): {RESET}").replace(",", ".")
        stroke = float(stroke)
        
        cylinders = int(input(f"{GREEN}Enter number of cylinders: {RESET}"))

        displacement = calculate_displacement(bore, stroke, cylinders)
        
        print(f"\n{GREEN}=== Result ==={RESET}")
        print(f"{WHITE}Total displacement: {GREEN}{displacement:.2f} cc{RESET}")
        
    except ValueError:
        print(f"\n{RED}Error: Please enter valid numeric values.{RESET}")
    
    print(f"\n{CYAN}Press Enter to exit...{RESET}")
    input()

if __name__ == "__main__":
    main()