def mnożenie_pod_kreską(liczba1, liczba2, podstawa):
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
    
    max_length = max(len(str(liczba1)), len(str(liczba2)))
    partial_results = []
    
    for i in range(1, len(str(liczba2)) + 1):
        digit2 = zamiana_na_dziesiętne(str(liczba2)[-i], podstawa)
        carry = 0
        partial_result = ''
        
        for j in range(1, len(str(liczba1)) + 1):
            digit1 = zamiana_na_dziesiętne(str(liczba1)[-j], podstawa)
            product = digit1 * digit2 + carry
            carry = product // podstawa
            partial_result = zamiana_na_system(product % podstawa, podstawa) + partial_result
        
        if carry:
            partial_result = zamiana_na_system(carry, podstawa) + partial_result
        
        partial_result += '0' * (i - 1)
        partial_results.append(partial_result)
    
    final_result = '0'
    
    for partial_result in partial_results:
        final_result = mnożenie_pod_kreską(final_result, partial_result, podstawa)
    
    return final_result

# Przykładowe użycie
liczba1 = '7B'
liczba2 = 'AF6'
podstawa = 16
wynik = mnożenie_pod_kreską(liczba1, liczba2, podstawa)
print("Wynik mnożenia pod kreską w systemie o podstawie", podstawa, ":", wynik)
