from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# إعداد خيارات Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # تشغيل بدون واجهة رسومية (مهم للسحابة)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# تهيئة المتصفح
driver = webdriver.Chrome(options=chrome_options)

# فتح صفحة ويب (مثلاً Google)
driver.get("https://www.google.com")
print("تم فتح Chrome بنجاح! العنوان الحالي:", driver.current_url)

# إغلاق المتصفح
driver.quit()
