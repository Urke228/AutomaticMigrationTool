from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



# Initialize the array of serial numbers, tenant variable, and domain variable

serial_numbers = ["476939", "458233", "464490"]  # Add more serial numbers as needed
tenant = "LEP"
domain = "COM"
failed_serial_numbers = []
successful_serial_numbers = []

service = Service(executable_path="C:/Users/BOSS/Documents/GitHub/AutomaticMigrationTool/aisproject/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Wait for the cookie consent button to be present and click it
time.sleep(1)  # Adjust the sleep time if necessary
accept_button = driver.find_element(By.XPATH, "//div[@class='QS5gu sy4vM' and text()='Sprejmi vse']")
accept_button.click()

# Navigate to the desired URL directly
driver.get("https://admintool.enspire.danfoss.com/")

# Wait for a few seconds to see the result
time.sleep(10)

for serial in serial_numbers:
    try:
        # Refresh the page to ensure it's in the correct state
        driver.refresh()
        time.sleep(1)  # Adjust the sleep time if necessary

        # Click on the "Migration ⬆️" button
        migration_button = driver.find_element(By.XPATH, "//button[@class='sc-ikJyIC hwUNQh']//span[text()='Migration ⬆️']")
        migration_button.click()

        # Wait for the page to load after clicking the button
        time.sleep(1)  # Adjust the sleep time if necessary

        # Enter the serial number into the specified input field
        serial_number_input = driver.find_element(By.XPATH, "//input[@id='react-select-2-input']")
        serial_number_input.clear()  # Clear any existing text
        serial_number_input.send_keys(serial)

        # Wait for the input to be processed
        time.sleep(1)  # Adjust the sleep time if necessary

        # Click on the "Add Device Serial/s" button
        add_device_button = driver.find_element(By.CLASS_NAME, "css-13uh85-menu")
        add_device_button.click()

        # Wait for the input to be processed
        time.sleep(1)  # Adjust the sleep time if necessary

        # Click on the tenant input field and enter the tenant variable
        tenant_input = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
        tenant_input.click()
        tenant_input.send_keys(tenant)
        time.sleep(1)
        tenant_input.send_keys(Keys.ENTER)

        # Wait for the input to be processed
        time.sleep(1)  # Adjust the sleep time if necessary

        # Click on the domain input field and enter the domain variable
        domain_input = driver.find_element(By.XPATH, "//input[@id='react-select-4-input']")
        domain_input.click()
        domain_input.send_keys(domain)
        time.sleep(1)
        domain_input.send_keys(Keys.ENTER)

        # Wait for the input to be processed
        time.sleep(1)  # Adjust the sleep time if necessary

        # Click on the "Select devices" button
        select_devices_button = driver.find_element(By.XPATH, "//span[text()='Select devices']")
        select_devices_button.click()

        # Wait for the input to be processed
        time.sleep(1)  # Adjust the sleep time if necessary







        # Click on the "Migrate Metadata" button
        migrate_metadata_button = driver.find_element(By.XPATH, "//span[text()='Migrate Metadata']")
        migrate_metadata_button.click()

        time.sleep(2)

        # Check the text of the migrate button
        migrate_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Migrate')]")
        if migrate_button.text == "Migrate 1 items":
            migrate_button.click()
            time.sleep(2)
            # Check for success notification
            success = False
            for _ in range(3):
                time.sleep(4)
                notification = driver.find_element(By.XPATH, "//h5[@class='sc-iqVWFU sc-eWfVMQ bbrroB fNRzXp']")
                if notification.text == "Success":
                    print(f"{serial} - Metadata migration successful.")
                    success = True
                    break
            if success:
                back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
                back_button.click()
            else:
                print(f"{serial} - Metadata migration failed.")
                failed_serial_numbers.append(serial)
                raise Exception("Migration failed.")
        else:
            # Click the "Refresh" button and check for changes up to 3 times
            for _ in range(3):
                refresh_button = driver.find_element(By.XPATH, "//span[text()='Refresh']")
                refresh_button.click()
                time.sleep(2)
                migrate_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Migrate')]")
                if migrate_button.text == "Migrate 1 items":
                    migrate_button.click()
                    success = False
                    for _ in range(3):
                        time.sleep(4)
                        notification = driver.find_element(By.XPATH, "//h5[@class='sc-iqVWFU sc-eWfVMQ bbrroB fNRzXp']")
                        if notification.text == "Success":
                            print(f"{serial} - Metadata migration successful.")
                            success = True
                            break
                    if success:
                        back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
                        back_button.click()
                    else:
                        print(f"{serial} - Metadata migration failed.")
                        failed_serial_numbers.append(serial)
                        raise Exception("Migration failed.")
                    break
                time.sleep(2)
            else:
                print(f"{serial} - No metadata to migrate.")
                back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
                back_button.click()









        # Wait for a few seconds to see the result
        time.sleep(2)




        
        
        
        # Click on the "Migrate Gateway Meters" button
        migrate_gateway_meters_button = driver.find_element(By.XPATH, "//span[text()='Migrate Gateway Meters']")
        migrate_gateway_meters_button.click()

        # Wait for 1 second
        time.sleep(1)

        # Check the text of the migrate button
        migrate_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Migrate')]")
        if migrate_button.text == "Migrate 0 items":
            for _ in range(3):
                refresh_button = driver.find_element(By.XPATH, "//span[text()='Refresh']")
                refresh_button.click()
                time.sleep(1)
                migrate_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Migrate')]")
                if migrate_button.text == "Migrate 1 items":
                    migrate_button.click()
                    time.sleep(3)
                    # Check for success notification
                    success = False
                    for _ in range(3):
                        time.sleep(4)
                        notification = driver.find_element(By.XPATH, "//h5[@class='sc-iqVWFU sc-eWfVMQ bbrroB fNRzXp']")
                        if notification.text == "Success":
                            print(f"{serial} - Gateway meters migration successful.")
                            success = True
                            break
                    if success:
                        back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
                        back_button.click()
                    else:
                        print(f"{serial} - gateway meters migration failed.")
                        failed_serial_numbers.append(serial)
                        raise Exception("Migration failed.")
                    break
            else:
                print(f"{serial} - No gateway meters data to migrate.")
                back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
                back_button.click()
        else:
            migrate_button.click()
            time.sleep(3)
            # Check for success notification
            success = False
            for _ in range(3):
                time.sleep(4)
                notification = driver.find_element(By.XPATH, "//h5[@class='sc-iqVWFU sc-eWfVMQ bbrroB fNRzXp']")
                if notification.text == "Success":
                    print(f"{serial} - Gateway meters migration successful.")
                    success = True
                    break
            if success:
                back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
                back_button.click()
            else:
                print(f"{serial} - gateway meters migration failed.")
                failed_serial_numbers.append(serial)
                raise Exception("Migration failed.")






        time.sleep(2)





        # Click on the "Migrate Configurable Inputs" button
        migrate_configurable_inputs_button = driver.find_element(By.XPATH, "//span[text()='Migrate Configurable Inputs']")
        migrate_configurable_inputs_button.click()

        # Wait for 5 seconds
        time.sleep(3)

        # Check the text of the migrate button
        migrate_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Migrate')]")
        if migrate_button.text == "Migrate 0 items":
            print(f"{serial} - No data to migrate for configurable inputs.")
            time.sleep(1)
            back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
            back_button.click()
        else:
            migrate_button.click()
            success = False
            for _ in range(4):
                time.sleep(5)
                notification = driver.find_element(By.XPATH, "//h5[@class='sc-iqVWFU sc-eWfVMQ bbrroB fNRzXp']")
                if notification.text == "Success":
                    print(f"{serial} - Configurable inputs successfully migrated.")
                    success = True
                    break
            if success:
                back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
                back_button.click()
            else:
                print(f"{serial} - Migration FAILED for configurable inputs.")
                failed_serial_numbers.append(serial)
                raise Exception("Migration failed.")







        # Wait for a few seconds to see the result
        time.sleep(2)







        # Click on the "Migrate Readings Data" button
        migrate_readings_data_button = driver.find_element(By.XPATH, "//span[text()='Migrate Readings Data']")
        migrate_readings_data_button.click()

        # Wait for 5 seconds
        time.sleep(3)

        # Check for error alert
        try:
            error_alert = driver.find_element(By.XPATH, "//div[@data-testid='alert-wrapper']//div[@data-testid='icon' and @id='error']")
            print(f"{serial} - Error alert found: Cannot load readings items for provided params.")
            back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
            back_button.click()
        except:
            # Check the text of the migrate button and click it if it says "Migrate X items"
            migrate_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Migrate')]")
            if "Migrate 0 items" in migrate_button.text:
                print(f"{serial} - No readings data to migrate.")
                back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
                back_button.click()
            elif "Migrate" in migrate_button.text:
                migrate_button.click()
                # Wait for the success notification (up to 1 minute)
                success = False
                for _ in range(20):
                    time.sleep(5)
                    notification = driver.find_element(By.XPATH, "//h5[@class='sc-iqVWFU sc-eWfVMQ bbrroB fNRzXp']")
                    if notification.text == "Success":
                        print(f"{serial} - Readings data migration successful.")
                        success = True
                        break
                if success:
                    successful_serial_numbers.append(serial)
                    back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
                    back_button.click()
                else:
                    print(f"{serial} - Readings data migration failed.")
                    failed_serial_numbers.append(serial)
                    raise Exception("Migration failed.")
            else:
                back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
                back_button.click()





        print(f"{serial} - ALL DATA SUCCESSFULLY MIGRATED.")
        print("\n")



        time.sleep(1)



        home_button = driver.find_element(By.XPATH, "//span[text()='HOME']")
        home_button.click()
        


        time.sleep(1)




    except Exception as e:
         print(f"An error occurred with serial {serial}: {e}")
         failed_serial_numbers.append(serial)
         back_button = driver.find_element(By.XPATH, "//span[text()='BACK']")
         back_button.click()
         time.sleep(1)
         home_button = driver.find_element(By.XPATH, "//span[text()='HOME']")
         home_button.click()



time.sleep(1)


# Close the browser
driver.quit()


# Print failed serial numbers
if failed_serial_numbers:
    print("Failed serial numbers:", failed_serial_numbers)
else:
    print("All serial numbers processed successfully.")



# Print successful serial numbers
if successful_serial_numbers:
    print("Successful serial numbers:", successful_serial_numbers)
else:
    print("No serial numbers were successfully processed.")