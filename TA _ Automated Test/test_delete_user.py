from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_delete_user():
    # Inisialisasi WebDriver (Chrome)
    driver = webdriver.Chrome()

    # Buka halaman login
    driver.get("https://opensource-demo.orangehrmlive.com/")

    try:
        # Tunggu hingga elemen username_input muncul sebelum melanjutkan
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtUsername"))
        )

        # Tunggu hingga elemen password_input muncul sebelum melanjutkan
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtPassword"))
        )

        # Tunggu hingga tombol login_button muncul sebelum melanjutkan
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "btnLogin"))
        )

        # Masukkan nilai untuk input username dan password
        username_input.send_keys("Admin")
        password_input.send_keys("admin123")

        # Klik tombol login
        login_button.click()

        # Tunggu hingga halaman dashboard muncul
        dashboard_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Buka halaman User Management
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
        
        # Tunggu hingga tabel user_management_table muncul sebelum melanjutkan
        user_management_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "resultTable"))
        )

        # Cari baris dengan data user yang ingin dihapus (misalnya, cari user dengan username "TestUser")
        row_to_delete = user_management_table.find_element(By.XPATH, "//tr[./td[text()='TestUser']]")

        # Klik tombol hapus (delete) pada baris tersebut
        delete_button = row_to_delete.find_element(By.XPATH, "//input[@name='chkSelectRow[]']")
        delete_button.click()

        # Klik tombol "Delete" untuk menghapus user
        delete_user_button = driver.find_element(By.ID, "btnDelete")
        delete_user_button.click()

        # Konfirmasi penghapusan user dengan mengklik tombol "OK" pada dialog konfirmasi
        confirm_delete_button = driver.find_element(By.ID, "dialogDeleteBtn")
        confirm_delete_button.click()

        # Tunggu hingga pesan sukses muncul
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.message.success"))
        )

        assert "Successfully Deleted" in success_message.text

        print("Hapus Pengguna berhasil!")

    except Exception as e:
        print("Hapus Pengguna gagal:", e)

    finally:
        # Tutup browser setelah selesai
        driver.quit()

if __name__ == "__main__":
    test_delete_user()
