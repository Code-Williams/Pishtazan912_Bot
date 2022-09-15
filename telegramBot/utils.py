import time
def check_number(number, driver):
    number_page = driver.get(f"https://rond.ir/Sims/{number}")
    try:
        number_text = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div[1]/div[2]/div/span")
    except:
        number_text = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/span")

    number_text = number_text.text.strip()
    if number_text == "سیم کارت مورد نظر یافت نشد.": return False
    return number_text

def write_description(number, link, driver):
    try:
        price = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div[1]/table[1]/tbody/tr[3]/td[2]/span").text.strip()
        info = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div[1]/table[1]/tbody/tr[5]/td[2]").text.strip()
        is_number_round = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div[1]/table[1]/tbody/tr[11]/td[2]").text.strip()
        round_type = "معمولی"
        if is_number_round == "رند": round_type = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div[1]/table[1]/tbody/tr[13]/td[2]").text.strip()
    except:
        price = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/table[1]/tbody/tr[3]/td[2]/span").text.strip()
        info = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/table[1]/tbody/tr[5]/td[2]").text.strip()
        is_number_round = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/table[1]/tbody/tr[11]/td[2]").text.strip()
        round_type = "معمولی"
        if is_number_round == "رند": round_type = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[1]/div[2]/table[1]/tbody/tr[13]/td[2]").text.strip()

    description = f"""{number}
وضعیت: {info}

نقد و قابل اقساط

قیمت نقدی: {price} تومان 

نوع رندی: {round_type}
_
راه ارتباطی:
🆔 @pishtazan_admin1 

تلفن تماس:
📞09121030892
📞 09122005350
☎️ 02122049375

📌آدرس : زعفرانیه، مقدس اردبیلی ، روبرو مسجد طالقانی ،  پ۹۶ ،طبقه دوم ، واحد 6

📁برای مشاهده تمام خطوط ۹۱۲ از طريق لینک زیر اقدام فرمایید👇👇{link}
برای محاسبه اقساط وارد لینک شوید
👇👇
http://pishtaza-912.ir/

➡️ @Pishtazan912"""
    print(number)
    number_file = open(f'posts/{number.replace(" ", "")}.txt', "w")
    number_file.write(description)
    number_file.close()