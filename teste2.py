def reverse(string) -> str:
    palavras = string.split(" ")
    return " ".join(reversed(palavras))

print(reverse("Ola Mundo"))
