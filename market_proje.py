import os

class Market:
    def __init__(self):
        """
        Market sınıfının yapıcı metodu.
        product.txt dosyasını oluşturur veya var olan dosyayı kullanır.
        """
        self.file_name = "product.txt"
        # Dosya yoksa oluşturur
        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()
            print(f"{self.file_name} dosyası oluşturuldu.")

    def __del__(self):
        """
        Market sınıfının yıkıcı metodu.
        Program sonlandığında çağrılır.
        """
        print("Market nesnesi yok edildi ve dosya kapatıldı.")

    def list_product(self):
        """
        product.txt dosyasındaki tüm ürünleri listeler.
        """
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                products = file.read().splitlines()
                if not products:
                    print("Henüz hiç ürün eklenmemiş.")
                    return
                
                print("\n=== ÜRÜN LİSTESİ ===")
                print("No  Ürün Adı        Kategori        Fiyat    Stok")
                print("-" * 50)
                for index, product in enumerate(products, 1):
                    name, category, price, stock = product.split(',')
                    print(f"{index:<4}{name:<15}{category:<15}{price:<9}{stock}")
                print("-" * 50)
        except Exception as e:
            print(f"Ürünler listelenirken bir hata oluştu: {e}")

    def add_product(self):
        """
        Kullanıcıdan alınan bilgilerle yeni bir ürün ekler.
        """
        try:
            print("\n=== ÜRÜN EKLEME ===")
            name = input("Ürün Adı: ")
            category = input("Kategori: ")
            while True:
                try:
                    price = float(input("Fiyat: "))
                    break
                except ValueError:
                    print("Lütfen geçerli bir fiyat giriniz!")
            
            while True:
                try:
                    stock = int(input("Stok Miktarı: "))
                    break
                except ValueError:
                    print("Lütfen geçerli bir stok miktarı giriniz!")

            product = f"{name},{category},{price},{stock}\n"
            
            with open(self.file_name, 'a', encoding='utf-8') as file:
                file.write(product)
            print("\nÜrün başarıyla eklendi.")
        except Exception as e:
            print(f"Ürün eklenirken bir hata oluştu: {e}")

    def delete_product(self):
        """
        Kullanıcının seçtiği ürünü siler.
        """
        try:
            self.list_product()
            with open(self.file_name, 'r', encoding='utf-8') as file:
                products = file.read().splitlines()
                
            if not products:
                print("Silinecek ürün bulunmamaktadır.")
                return

            while True:
                try:
                    product_num = int(input("\nSilmek istediğiniz ürünün numarasını girin: "))
                    if 1 <= product_num <= len(products):
                        break
                    else:
                        print("Geçersiz ürün numarası! Lütfen listeden bir numara seçin.")
                except ValueError:
                    print("Lütfen geçerli bir sayı girin!")

            # Seçilen ürünü listeden çıkar
            deleted_product = products.pop(product_num - 1)
            
            # Güncellenmiş listeyi dosyaya yaz
            with open(self.file_name, 'w', encoding='utf-8') as file:
                file.write('\n'.join(products))
                if products:  # Eğer hala ürün varsa son satıra new line ekle
                    file.write('\n')
            
            print(f"\nÜrün başarıyla silindi: {deleted_product.split(',')[0]}")
        except Exception as e:
            print(f"Ürün silinirken bir hata oluştu: {e}")

def display_menu():
    """
    Ana menüyü görüntüler.
    """
    print("\n*** MARKET OTOMASYON SİSTEMİ ***")
    print("1) Ürünleri Listele")
    print("2) Ürün Ekle")
    print("3) Ürün Sil")
    print("4) Çıkış")
    print("-" * 30)

def main():
    """
    Ana program döngüsü.
    """
    market = Market()
    
    while True:
        display_menu()
        choice = input("Seçiminizi yapın (1-4): ")
        
        if choice == '1':
            market.list_product()
        elif choice == '2':
            market.add_product()
        elif choice == '3':
            market.delete_product()
        elif choice == '4':
            print("\nProgram sonlandırılıyor...")
            break
        else:
            print("\nGeçersiz seçim! Lütfen 1-4 arasında bir seçim yapın.")

if __name__ == "__main__":
    main()
