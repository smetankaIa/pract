def calculate_amoebas(hours):
   
 
    amoebas = 1  # Breakpoint 1: Проверка начального значения
    
    
    divisions = hours // 3  # Breakpoint 2: Проверка расчета деления
    
    
    for _ in range(divisions):
        amoebas *= 2  # Breakpoint 3: Проверка умножения в цикле
        
    return amoebas

def main():
    
    n = int(input("Введите количество 3-часовых интервалов (n): "))  # Breakpoint 4: Проверка входных значений
    
   
    for i in range(1, n + 1):
        hours = i * 3
        amoebas = calculate_amoebas(hours)
        print(f"После {hours} часов: {amoebas} амеб")  # Breakpoint 5: Проверка вывода

if __name__ == "__main__":
    main()
