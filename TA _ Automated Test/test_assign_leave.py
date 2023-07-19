from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_assign_leave():
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

        # Buka halaman Assign Leave
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/leave/assignLeave")
        
        # Tunggu hingga elemen employee_name_input muncul sebelum melanjutkan
        employee_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "assignleave_txtEmployee_empName"))
        )

        # Pilih karyawan dari daftar (misalnya, pilih karyawan dengan nama "Linda Anderson")
        employee_name_input.send_keys("Linda Anderson")
        driver.find_element(By.XPATH, "//li[contains(text(), 'Linda Anderson')]").click()

        # Pilih jenis cuti dari daftar (misalnya, pilih jenis cuti "Vacation US")
        leave_type_dropdown = driver.find_element(By.ID, "assignleave_txtLeaveType")
        leave_type_dropdown.send_keys("Vacation US")
        driver.find_element(By.XPATH, "//li[contains(text(), 'Vacation US')]").click()

        # Masukkan tanggal mulai cuti dan tanggal akhir cuti
        leave_from_input = driver.find_element(By.ID, "assignleave_txtFromDate")
        leave_from_input.clear()
        leave_from_input.send_keys("2023-07-15")

        leave_to_input = driver.find_element(By.ID, "assignleave_txtToDate")
        leave_to_input.clear()
        leave_to_input.send_keys("2023-07-16")

        # Masukkan keterangan cuti
        comment_input = driver.find_element(By.ID, "assignleave_txtComment")
        comment_input.send_keys("Cuti untuk berlibur")

        # Klik tombol Assign
        assign_button = driver.find_element(By.ID, "assignBtn")
        assign_button.click()

        # Tunggu hingga pesan sukses muncul
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "assign-leave-success"))
        )

        assert "Successfully Assigned" in success_message.text

        print("Assign Leave berhasil!")

    except Exception as e:
        print("Assign Leave gagal:", e)

    finally:
        # Tutup browser setelah selesai
        driver.quit()

if __name__ == "__main__":
    test_assign_leave()
