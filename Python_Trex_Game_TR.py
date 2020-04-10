from PIL import ImageGrab, ImageOps #Pillow kütüphanesini ekliyoruz çünkü ekrannın belirli bir bölgesindeki pixel değerlerini öğrenmek istiyoruz.
import pyautogui #Pyautogui, python üzerinde mouse ve klavye kontrolü için kullanılır.
import time #Time, python üzerinde süre kontrolü için kullanılır.
from numpy import * #Numpy, bazı hesaplar yapmak için kullanılır.

class kordinatlar(): 
    replay = (340, 390) 
    dinozor = (202, 441)  
    #Aşağıdaki değerler bizim kaktüsün olup olmadığını kontrol etmek için gereken kordinatlar.
    #Bu kordinatları bulmak için bir tutorial koyacağım.
    # x = 220 (Kaktüsün olup olmadığını kontrol etmek için gerekli olan kordinat) 
    # y = 466   (Kaktüsün yarısının kordinatı) 

def yeniden_baslat(): 
    pyautogui.click(kordinatlar.replay) #Pyautogui kütüphanesinin "click" modülünü kullanarak oyunu yeniden başlatıyoruz.
    
def space_bas():  #pressSpace 
    pyautogui.keyDown('space') #Pyautogui kütüphanesinin "keyDown" modülünü kullanarak space(boşluk) tuşuna basacak.   
    time.sleep(0.05) #sleep, bir delay fonksiyonudur.
    print('Zıplandı') #Ekrana zıplandı yazacak.
    pyautogui.keyUp('space') #Pyautogui kütüphanesinin "keyUp" modülünü kullanarak space(boşluk) tuşuna basma bırakılacak.

def imageGrab(): #Burası bot'un en önemli kısmı. #imageGrab, ekranın ss almasını sağlayan bir modül.
    taranacak_alan = (kordinatlar.dinozor[0] + 63, kordinatlar.dinozor[1], kordinatlar.dinozor[0] + 100, kordinatlar.dinozor[1]+30) #Burada taranacak alan'nın neresi olduğu belirleniyor. Burası tutorial izlemeden yapılacak bir yer değil ama ortalama değerler bunlar ben ekranı ikiye ayırıp bir tarafa editörü bir tarafa oyunu koyunca en uygun bu değerleri buldum.
    image = ImageGrab.grab (taranacak_alan)   #Burada ImageGrab kullanılarak taranacak_alan ss alınır.  
    grayImage = ImageOps.grayscale(image)  #Çekilen ss'i gri tonlarına çevirir.
    a = array(grayImage.getcolors())      #Pixel değerleri alınır.
    print(a.sum())                      #pixel değerleri ekrana yazdırılır.
    return(a.sum())                    #pixel değerleri return edilir.

def main():     
    yeniden_baslat()
    while True:
        if (imageGrab()!=1357):  #Buradaki değer pixel değerlerine göre değişir. taranacak_alan ile ilgili 
            time.sleep(0.1)
            space_bas()

                    
   
main()                               #Program çalıştırılır.                                                                                                                                                                                                                                                                                                                   

#Not: İnternetteki birçok kaynaktan yararlanılmıştır. Thanks to "The PC Geek".
