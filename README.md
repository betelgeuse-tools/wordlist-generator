# Mask Wordlist Generator

A simple and customizable wordlist generator based on mask patterns.\
Useful for CTFs, password cracking, or automation where you need tailored wordlists.

---

## Features

- Use masks like `?l`, `?a`, `?n`, or your own **keyword** with `?k`.
- Custom charset combinations.
- Dynamic expansion of passwords.
- Progress feedback during generation.

---

## Mask Symbols

| Symbol | Meaning                                            |
| ------ | -------------------------------------------------- |
| `?a`   | All letters (upper+lowercase), digits, and symbols |
| `?l`   | All letters (upper+lowercase) and digits           |
| `?n`   | Digits only (`0-9`)                                |
| `?k`   | Insert your custom keyword anywhere                |

---

## Example Usage

```bash
python3 Wordlist_Generator.py -m "?k?a?a?n?n" -k "john_doe" -o wordlist.txt
```

**Explanation:**

- `?k` will be replaced by your keyword (`john_doe`).
- `?a` will pick a random letter/digit/symbol.
- `?n` will pick a random digit (`0-9`).
- All combinations following this pattern will be generated.

Example outputs:

```
john_doeA8
john_doeB7
john_doe0Z
john_doe$4
...
```

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/betelgeuse-tools/wordlist-generator.git
cd wordlist-generator
```

**Required packages** (also can be installed manually):

```bash
pip install colorama
```


---

## License

This project is licensed under the **MIT License** — feel free to use, modify, and share!

---

## Author

> Made with ❤️ by **Betelgeuse** (April 09, 2025)

