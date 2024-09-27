"""Chercher à savoir si une chaîne de caractère est bien un palindrome ou non"""

#### Fonction secondaire
import string
def ispalindrome(s):
    """
    Retourner si s est un palindrome ou pas

    Args:
    s: chaîne de caractère
    """
    intt="éèêëàâçô"
    outt="eeeeaaco"
    table=str.maketrans(intt,outt)

    for k in string.punctuation:
        s=s.lower().replace(" ","").replace(k,"").translate(table)

    if s==s[::-1]:
        return True
    return None

#### Fonction principale

def main():
    """
    Retourne pour chaque mot si c'est un palindrome ou pas

    Args:
    s: chaîne de caractère

    >>> ispalindrome("radar")
    True
    >>> ispalindrome("kayak")
    True
    >>> ispalindrome("level")
    True
    >>> ispalindrome("rotor")
    True
    >>> ispalindrome("civique")
    False
    >>> ispalindrome("deifie")
    False
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
