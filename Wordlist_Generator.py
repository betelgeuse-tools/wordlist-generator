import argparse
from itertools import product
import string
from colorama import Fore, Style, init

init(autoreset=True)

# === Custom charsets ===
charsets = {
    "?a": string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.?",
    "?l": string.ascii_letters + string.digits,
    "?n": string.digits
}

# === Banner ===
def banner():
    print(f"""
{Fore.WHITE}{Style.BRIGHT}
----------------------------------
██     ██  ██████       
██     ██ ██            
██  █  ██ ██   ███      
██ ███ ██ ██    ██      
  ███ ███   ██████   
----------------------------------

{Fore.MAGENTA}[+] Author : Betelgeuse{Style.RESET_ALL}
{Fore.MAGENTA}[+] Tool	 : Mask Wordlist Generator{Style.RESET_ALL}
{Fore.MAGENTA}[+] Date	 : April 09, 2025{Style.RESET_ALL}

""")

# === Expand mask into char groups ===
def expand_mask(mask, keyword):
    expanded = []
    i = 0
    while i < len(mask):
        if mask[i] == '?' and i + 1 < len(mask):
            key = mask[i:i+2]
            if key == "?k":
                expanded.append([keyword])
            else:
                expanded.append(charsets.get(key, [key]))
            i += 2
        else:
            expanded.append([mask[i]])
            i += 1
    return expanded

# === Generate all combinations ===
def generate_from_mask(mask: str, keyword: str, output_file: str):
    slots = expand_mask(mask, keyword)
    total = 0

    with open(output_file, "w", encoding="utf-8") as f:
        for i in range(1, len(slots) + 1):
            current = slots[:i]
            for combo in product(*current):
                f.write(''.join(combo) + "\n")
                total += 1
                if total % 100000 == 0:
                    print(f"{Fore.YELLOW}[+] {total} passwords generated...")

    print(f"{Fore.GREEN}[✓] Done. Total: {Style.BRIGHT}{total}{Style.RESET_ALL}")
    return total

# === Args ===
def parse_args():
    parser = argparse.ArgumentParser(description="Mask wordlist generator")
    parser.add_argument("-m", "--mask", required=True, help="Mask, e.g. ?k?a?n?n")
    parser.add_argument("-o", "--output", required=True, help="Output file")
    parser.add_argument("-k", "--keyword", required=True, help="Keyword for ?k")
    return parser.parse_args()

# === Main ===
def main():
    banner()
    args = parse_args()
    generate_from_mask(args.mask, args.keyword, args.output)

if __name__ == "__main__":
    main()
