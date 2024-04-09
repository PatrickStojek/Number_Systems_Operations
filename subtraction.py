def odejmowanie_pod_kreską(liczba1, liczba2, podstawa):
    if not (2 <= podstawa <= 33):
        raise ValueError("Podstawa systemu liczbowego musi być między 2 a 33")
    
    def zamiana_na_dziesiętne(cyfra, podstawa):
        if cyfra.isdigit():
            return int(cyfra)
        else:
            wartość = ord(cyfra.upper()) - 55
            if wartość >= podstawa:
                raise ValueError("Cyfra nie jest prawidłowa dla podanej podstawy systemu")
            return wartość
    
    def zamiana_na_system(liczba, podstawa):
        if liczba == 0:
            return '0'
        system = ''
        while liczba:
            reszta = liczba % podstawa
            if reszta < 10:
                system = str(reszta) + system
            else:
                system = chr(reszta + 55) + system
            liczba //= podstawa
        return system
        
    print(zamiana_na_system(123,16))
    # Upewnij się, że liczba1 jest większa lub równa liczba2
    if int(liczba1, podstawa) < int(liczba2, podstawa):
        liczba1, liczba2 = liczba2, liczba1
    
    max_length = max(len(str(liczba1)), len(str(liczba2)))
    result = ''
    borrow = 0
    
    for i in range(1, max_length + 1):
        digit1 = zamiana_na_dziesiętne(str(liczba1)[-i], podstawa) if i <= len(str(liczba1)) else 0
        digit2 = zamiana_na_dziesiętne(str(liczba2)[-i], podstawa) if i <= len(str(liczba2)) else 0
        
        difference = digit1 - digit2 - borrow
        
        if difference < 0:
            difference += podstawa
            borrow = 1
        else:
            borrow = 0
        
        result = zamiana_na_system(difference, podstawa) + result
    
    return result

# Przykładowe użycie
liczba1 = '7B'
liczba2 = '7B'
podstawa = 16
wynik = odejmowanie_pod_kreską(liczba1, liczba2, podstawa)
print("Wynik odejmowania pod kreską w systemie o podstawie", podstawa, ":", wynik)
