from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    # Inisialisasi WebDriver (Chrome)
    driver = webdriver.Chrome()

    # Buka halaman login
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

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

        # Tunggu hingga halaman setelah login muncul (misalnya, halaman dashboard)
        dashboard_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Verifikasi bahwa Anda telah berhasil login
        assert "Welcome Admin" in driver.page_source

        print("Login berhasil!")

    except Exception as e:
        print("Login gagal:", e)

    finally:
        # Tutup browser setelah selesai
        driver.quit()

if __name__ == "__main__":
    test_login()
