from datetime import datetime
import time
import pygame
import os
import sys
import select  

def is_key_pressed():
   
    if os.name == 'nt': 
        return select.select([sys.stdin], [], [], 0.0)[0] != []

def get_key():
   
    if os.name == 'nt': 
        return sys.stdin.read(1).lower()

def play_alarm():
    
    pygame.mixer.init()
    
    try:
        
        pygame.mixer.music.load('2024.mp3')
        pygame.mixer.music.play()
        
        print("\nНажмите 'q' для отключения будильника")
        
        # Воспроизводим звук в цикле
        while pygame.mixer.music.get_busy():
            if is_key_pressed():
                key = get_key()
                if key == 'q':
                    print("\nБудильник отключен!")
                    pygame.mixer.music.stop()
                    break
            pygame.time.Clock().tick(10)
            
    except Exception as e:
        print(f"Ошибка воспроизведения звука: {e}")
        print("Будильник сработал!")
    finally:
        # Очистка ресурсов
        pygame.mixer.quit()

def set_alarm():
    print("=== Будильник ===")

    current_time = datetime.now()
    print(f"Текущее время: {current_time.strftime('%H:%M:%S')}")
    
  
    while True:
        try:
            alarm_time = input("Введите время будильника в формате ЧЧ:ММ: ")
            alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
            
            # Проверяем корректность введенного времени
            if 0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59:
                break
            else:
                print("Ошибка: время должно быть в диапазоне 00:00 - 23:59")
        except ValueError:
            print("Ошибка: введите время в формате ЧЧ:ММ")
    
   
    alarm_datetime = datetime.now().replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
    
   
    if alarm_datetime < current_time:
        alarm_datetime = alarm_datetime.replace(day=alarm_datetime.day + 1)
    
    print(f"Будильник установлен на: {alarm_datetime.strftime('%H:%M')}")
    
    
    while True:
        current_time = datetime.now()
        if current_time >= alarm_datetime:
            print("\nВремя просыпаться!")
            play_alarm()
            break
        time.sleep(1)

def main():
    while True:
        set_alarm()
        choice = input("\nХотите установить еще один будильник? (да/нет): ")
        if choice.lower() != 'да':
            break
    print("Программа завершена")

if __name__ == "__main__":
    main() 