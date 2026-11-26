# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · **ไทย** · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

ปลั๊กอินสำหรับ Nagios/Icinga เพื่อติดตามราคา Bitcoin พร้อมเกณฑ์แจ้งเตือนระดับ warning และ critical ที่กำหนดค่าได้

## คุณสมบัติ

- ติดตามราคา Bitcoin ในหลายสกุลเงิน (USD, EUR, GBP เป็นต้น)
- กำหนดเกณฑ์ warning และ critical ได้ (ทั้งค่าสูงและค่าต่ำ)
- ส่งผลลัพธ์มาตรฐานของปลั๊กอิน Nagios พร้อมข้อมูลประสิทธิภาพ (performance data)
- ใช้ CoinGecko API (ฟรี ไม่ต้องใช้ API key)
- รองรับ API endpoint แบบกำหนดเอง
- กำหนดค่า timeout ได้
- ตรวจสอบความสดใหม่ของราคาโดยใช้ timestamp จากผู้ให้บริการ โดยมีขีดจำกัดเริ่มต้นหนึ่งชั่วโมง
- รองรับการลองใหม่ (retry) แบบจำกัดจำนวนเมื่อถูกจำกัดอัตรา (rate limit) หรือเกิดข้อผิดพลาดชั่วคราวจาก API
- ใช้กำหนดเวลา (deadline) เดียวร่วมกันสำหรับทุกความพยายามในการเรียก และจำกัดขนาดการตอบกลับไม่เกิน 64 KiB ต่อครั้ง
- รองรับการแจ้งเตือนเพิ่มเติมเมื่อราคาเปลี่ยนแปลงเป็นเปอร์เซ็นต์ในรอบ 24 ชั่วโมง (ค่าสัมบูรณ์)
- แสดงเกณฑ์ราคา ระยะเวลาของคำขอ และอายุของราคาในข้อมูลประสิทธิภาพ

## การติดตั้ง

<a name="from-github-releases"></a>

### จาก GitHub Releases

ดาวน์โหลดไฟล์ `.deb`, `.rpm`, `.tar.gz`, wheel และ `SHA256SUMS` ได้จาก [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) ตรวจสอบไฟล์ที่ดาวน์โหลดด้วย `sha256sum --ignore-missing --check SHA256SUMS` รีลีสหลังเวอร์ชัน 1.0.0 ยังมาพร้อม build provenance ที่มีการลงลายมือชื่อดิจิทัล สามารถยืนยันได้ว่าไฟล์มาจาก release workflow ของรีโพสิทอรีนี้ด้วยคำสั่ง `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

ใช้ชื่อไฟล์จากรีลีสที่เลือก แพ็กเกจแบบ native จะติดตั้ง `/usr/bin/check_bitcoin_price` และ `/usr/lib/nagios/plugins/check_bitcoin_price` โดยไฟล์ RPM จะติดตั้ง `/usr/lib64/nagios/plugins/check_bitcoin_price` เพิ่มเติมด้วย คำสั่งที่แพ็กเกจติดตั้งมาจะรัน Python ในโหมด isolated จึงไม่สนใจ `PYTHONPATH` และโมดูลในไดเรกทอรีทำงาน โดยตัวจัดการแพ็กเกจของระบบจะจัดการ dependency ของ Python และ `requests` ให้เอง แพ็กเกจเหล่านี้มีโค้ด Python ที่ไม่ขึ้นกับสถาปัตยกรรมเครื่อง และต้องใช้ดิสทริบิวชันที่มี Python 3.12 ขึ้นไป

### จากซอร์สโค้ด

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### สำหรับการพัฒนา

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## การใช้งาน

### การใช้งานพื้นฐาน

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### การใช้งานร่วมกับเกณฑ์แจ้งเตือน

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### การกำหนดเกณฑ์แยกแต่ละค่า

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### การเปลี่ยนสกุลเงิน

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### การกำหนด Timeout เอง

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### ความสดใหม่ของข้อมูลและงบประมาณการลองใหม่

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

ราคาที่มี timestamp จากผู้ให้บริการต้องมีอายุไม่เกินหนึ่งชั่วโมงตามค่าเริ่มต้น
Endpoint ที่ส่งคืนเฉพาะราคาจะยังคงใช้งานได้เมื่อไม่ได้ระบุ `--max-age`
เมื่อระบุ `--max-age` หาก timestamp จากผู้ให้บริการขาดหาย ไม่ถูกต้อง เป็นเวลาในอนาคต หรือเก่าเกินกำหนด ปลั๊กอินจะคืนค่า `UNKNOWN` โดยจะไม่นำเวลาดึงข้อมูลในเครื่องมาใช้แทนเวลาอ้างอิงราคาของผู้ให้บริการ Timestamp ที่ตรงกับขีดจำกัดอายุพอดีจะยังคงยอมรับได้ ส่วน timestamp ที่เป็นเวลาในอนาคตจะถูกปฏิเสธเสมอ

ค่าเริ่มต้นอนุญาตให้ลองใหม่ได้หนึ่งครั้ง เฉพาะข้อผิดพลาดในการเชื่อมต่อ, timeout และการตอบกลับ HTTP 408/429/500/502/503/504 เท่านั้นที่จะถูกลองใหม่ ระยะเวลารอ (backoff) เริ่มต้นที่ 0.5 วินาทีและเพิ่มขึ้นเป็นสองเท่าในการลองใหม่ครั้งถัดไป โดยค่า `Retry-After` แบบวินาทีและ HTTP date จะมีลำดับความสำคัญเหนือกว่า ความพยายามทั้งหมด การอ่านการตอบกลับ การถอดรหัส JSON และการรอเพื่อลองใหม่จะใช้เวลาจากงบประมาณ `--timeout` ร่วมกัน หากระยะเวลารอเพื่อลองใหม่ไม่พอดีกับเวลาที่เหลือ ระบบจะคืนค่า `UNKNOWN` ทันทีและรายงานความล้มเหลวที่ทำให้เกิดการลองใหม่ เช่น `HTTP 429` หรือ `ConnectionError` แทนที่จะรายงานว่า timeout ข้อผิดพลาดด้านการยืนยันตัวตน, HTTP error ถาวรอื่นๆ, JSON ที่ไม่ถูกต้อง และการตอบกลับที่มีขนาดข้อมูลหลังถอดรหัสเกิน 64 KiB จะไม่ถูกลองใหม่ ใช้ `--retries 0` เพื่อปิดการลองใหม่

### แหล่งข้อมูลราคาสำรอง

ใช้ตัวเลือก `--fallback-url URL` แบบระบุซ้ำได้กับ endpoint ที่เข้ากันได้กับ CoinGecko
ตัวอย่างเช่น เพิ่ม `--fallback-url https://quotes.example.org/simple/price`
แต่ละแหล่งข้อมูลจะได้รับส่วนแบ่งเวลาจากกำหนดเวลา (deadline) ที่เหลือของคำขอเท่าๆ กัน รวมถึงการลองใหม่ของแหล่งนั้นด้วย ความล้มเหลวชั่วคราวหรือระยะเวลารอลองใหม่ที่นานกว่าส่วนแบ่งเวลาดังกล่าวจะเลื่อนไปใช้แหล่งข้อมูลถัดไป ความล้มเหลวในการตรวจสอบ TLS, HTTP error ถาวร และราคาที่ไม่ถูกต้องจะคืนค่า UNKNOWN การตอบกลับราคาแต่ละครั้งถูกจำกัดขนาดข้อมูลหลังถอดรหัสไม่เกิน 64 KiB
เมื่อมีการกำหนดค่าแหล่งสำรอง สถานะจะระบุแหล่งข้อมูลที่ตอบกลับเป็น `primary`, `fallback1` และลำดับถัดไป โดยไม่แสดง URL ของแหล่งข้อมูลนั้น

### การเปลี่ยนแปลงราคาในช่วงเวลาสั้น

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

กำหนดไดเรกทอรีสถานะส่วนตัวที่เขียนได้บนระบบไฟล์ Linux หรือ macOS ในเครื่องให้ผู้ใช้ที่ใช้รันการมอนิเตอร์ เก็บไฟล์ `.lock` ที่อยู่คู่กันไว้ระหว่างการตรวจสอบ และใช้ไฟล์สถานะแยกกันสำหรับแต่ละช่วงเวลา (window) โดยสกุลเงินต่างๆ จะมีประวัติแยกจากกันภายในไฟล์นั้น
ช่วงเวลาเริ่มต้นคือ 3600 วินาที ราคาที่ถูกต้องแต่ละรายการต้องมี timestamp จากผู้ให้บริการที่อยู่ภายในช่วงเวลาและขีดจำกัดอายุ ซึ่งคือหนึ่งชั่วโมงเว้นแต่ `--max-age` จะกำหนดเป็นอย่างอื่น ปลั๊กอินจะเปรียบเทียบราคาปัจจุบันกับราคาที่เป็นบวกที่เก่าที่สุดก่อนหน้านั้นในช่วงเวลาดังกล่าว และรายงานจำนวนวินาทีที่ผ่านไปจริง Timestamp ที่ซ้ำกันจะไม่สร้างตัวอย่างข้อมูลเพิ่มเติม
ตัวอย่างข้อมูลแรก ประวัติที่หมดอายุ หรือ JSON ที่เสียหายจะเริ่มต้นค่าฐาน (baseline) ใหม่ โดยค่าเมทริกของช่วงเวลาจะเป็น unknown จนกว่าจะมีตัวอย่างข้อมูลที่เปรียบเทียบได้ ส่วนการแจ้งเตือนอื่นๆ ยังคงทำงานตามปกติ สถานะที่ไม่สามารถเขียนได้ ไฟล์สถานะหรือไฟล์ lock ที่เป็น symbolic link หรือราคาที่เก่ากว่าตัวอย่างข้อมูลล่าสุดที่บันทึกไว้จะคืนค่า UNKNOWN เมทริก `bitcoin_move_window` แบบมีเครื่องหมายใช้ช่วง warning และ critical แบบสมมาตร ค่าที่เท่ากับขีดจำกัดพอดีจะไม่แจ้งเตือน

ปลั๊กอินจะเปิดไดเรกทอรีสถานะหนึ่งครั้งต่อการตรวจสอบและทำงานอ้างอิงกับไดเรกทอรีนั้น ดังนั้นส่วนประกอบของพาธที่ถูกแทนที่ระหว่างการตรวจสอบจึงไม่สามารถเปลี่ยนเส้นทางไฟล์ lock การอ่าน หรือการเขียนได้ Symbolic link ในส่วนไดเรกทอรีของพาธจะถูกติดตามเมื่อเริ่มการตรวจสอบ ซึ่งทำให้ลิงก์ของแพลตฟอร์มอย่าง `/var` บน macOS ยังคงใช้งานได้ ดังนั้นไดเรกทอรีสถานะและไดเรกทอรีระดับบนจึงต้องไม่อนุญาตให้ผู้ใช้อื่นเขียนได้ ไฟล์สถานะและไฟล์ lock จะถูกสร้างด้วยโหมด 0600

### การเปลี่ยนแปลงเป็นเปอร์เซ็นต์รายวัน

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

เกณฑ์การเปลี่ยนแปลงจะวัดค่าสัมบูรณ์ของการเปลี่ยนแปลงเป็นเปอร์เซ็นต์ในรอบ 24 ชั่วโมงของ CoinGecko ในสกุลเงินที่เลือก การเปลี่ยนแปลงที่ตรงกับเกณฑ์พอดีจะไม่แจ้งเตือน หากระบุทั้งสองเกณฑ์ ค่า warning ต้องไม่เกินค่า critical ข้อมูลการเปลี่ยนแปลงที่ขาดหายหรือไม่ถูกต้องจะคืนค่า `UNKNOWN` สามารถใช้การแจ้งเตือนด้านราคาและการเปลี่ยนแปลงร่วมกันได้ โดยระดับความรุนแรงสูงสุดจะเป็นฝ่ายชนะ และหากระดับความรุนแรงเท่ากัน ราคาจะมีลำดับความสำคัญสูงกว่า

## ตัวเลือกบรรทัดคำสั่ง

| ตัวเลือก | คำอธิบาย |
|----------|----------|
| `-w`, `--warning` | ช่วงเกณฑ์ warning (รูปแบบ: LOW:HIGH) |
| `-c`, `--critical` | ช่วงเกณฑ์ critical (รูปแบบ: LOW:HIGH) |
| `--warning-low` | เกณฑ์ warning สำหรับราคาต่ำสุด |
| `--warning-high` | เกณฑ์ warning สำหรับราคาสูงสุด |
| `--critical-low` | เกณฑ์ critical สำหรับราคาต่ำสุด |
| `--critical-high` | เกณฑ์ critical สำหรับราคาสูงสุด |
| `--currency` | รหัสสกุลเงินความยาว 2-16 ตัวอักษรหรือตัวเลข (ค่าเริ่มต้น: usd) |
| `--timeout` | งบประมาณเวลารวมสำหรับคำขอ API และการลองใหม่เป็นวินาที รองรับค่าทศนิยม (ค่าเริ่มต้น: 10) |
| `--retries` | จำนวนครั้งเพิ่มเติมในการลองใหม่เมื่อเกิดข้อผิดพลาดชั่วคราว 0-5 (ค่าเริ่มต้น: 1) |
| `--max-age` | อายุสูงสุดของราคาจากผู้ให้บริการเป็นวินาทีและบังคับต้องมี timestamp (ราคาที่มี timestamp มีค่าเริ่มต้นที่ 3600) |
| `--warning-change` | ขีดจำกัด warning สำหรับการเปลี่ยนแปลงเป็นเปอร์เซ็นต์ในรอบ 24 ชั่วโมง (ค่าสัมบูรณ์) |
| `--critical-change` | ขีดจำกัด critical สำหรับการเปลี่ยนแปลงเป็นเปอร์เซ็นต์ในรอบ 24 ชั่วโมง (ค่าสัมบูรณ์) |
| `--api-url` | API URL หลัก |
| `--fallback-url` | endpoint ที่เข้ากันได้เพิ่มเติม ระบุซ้ำตามลำดับที่ต้องการ |
| `--state-file` | ไฟล์ JSON เก็บประวัติการเคลื่อนไหวของราคา |
| `--move-window` | ช่วงเวลาการเคลื่อนไหวเป็นวินาที (ค่าเริ่มต้น: 3600) |
| `--warning-move`, `--critical-move` | เกณฑ์การเคลื่อนไหวในช่วงเวลาเป็นเปอร์เซ็นต์ (ค่าสัมบูรณ์) |
| `-v`, `--verbose` | เปิดใช้งานการแสดงผลแบบละเอียด |
| `-V`, `--version` | แสดงเวอร์ชัน |
| `-h`, `--help` | แสดงข้อความช่วยเหลือ |

## การตั้งค่า Nagios

### การกำหนดคำสั่ง

กำหนดค่า Nagios resource macro `$USER1$` ให้ชี้ไปยังไดเรกทอรีปลั๊กอิน (แพ็กเกจแบบ native ใช้ `/usr/lib/nagios/plugins`) จากนั้นเพิ่มลงในไฟล์การตั้งค่าคำสั่ง Nagios ของคุณ:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### การกำหนด Service

```cfg
define service {
    use                     generic-service
    host_name               localhost
    service_description     Bitcoin Price
    check_command           check_bitcoin_price!30000:50000!25000:60000!usd
    check_interval          15
    retry_interval          5
}
```

### การตั้งค่า Icinga2

```conf
object CheckCommand "bitcoin_price" {
    command = [ PluginDir + "/check_bitcoin_price" ]

    arguments = {
        "-w" = "$bitcoin_warning$"
        "-c" = "$bitcoin_critical$"
        "--currency" = "$bitcoin_currency$"
    }
}

object Service "bitcoin-price" {
    import "generic-service"
    host_name = NodeName
    check_command = "bitcoin_price"

    vars.bitcoin_warning = "30000:50000"
    vars.bitcoin_critical = "25000:60000"
    vars.bitcoin_currency = "usd"
}
```

## รหัสสถานะออก (Exit Codes)

อาร์กิวเมนต์ที่ไม่ถูกต้อง ค่า timeout ที่ไม่เป็นบวก ช่วงเกณฑ์ที่ไม่ถูกต้อง และราคาจาก API ที่มีรูปแบบผิดพลาดจะคืนค่า `UNKNOWN` (exit 3) เกณฑ์ต้องเป็นจำนวนจำกัด (finite) ที่ไม่เป็นลบ โดยค่าขอบล่างแต่ละค่าต้องไม่มากกว่าค่าขอบบน สกุลเงินต้องมีความยาว 2-16 ตัวอักษรหรือตัวเลข การตั้งค่าที่ไม่ถูกต้องจะถูกปฏิเสธก่อนติดต่อ API ราคาต้องเป็นจำนวนจำกัดและไม่เป็นลบ โดยระบุเป็นตัวเลข JSON หรือสตริงทศนิยมปกติ เช่น `"43521.5"` การตอบกลับที่ไม่มีสกุลเงินที่ร้องขอจะระบุชื่อสกุลเงินนั้น เช่น `Response has no EUR price` การตอบกลับที่ไม่ถูกต้องจะไม่ส่งข้อมูลประสิทธิภาพ ข้อความวินิจฉัยแบบละเอียดจะถูกส่งไปยัง stderr เพื่อให้ stdout มีบรรทัดสถานะการมอนิเตอร์เพียงบรรทัดเดียว

| รหัส | สถานะ | คำอธิบาย |
|------|-------|----------|
| 0 | OK | ราคาอยู่ในช่วงที่ยอมรับได้ |
| 1 | WARNING | ราคาเกินเกณฑ์ warning |
| 2 | CRITICAL | ราคาเกินเกณฑ์ critical |
| 3 | UNKNOWN | เกิดข้อผิดพลาด (API ล้มเหลว, timeout เป็นต้น) |

## ข้อมูลประสิทธิภาพ (Performance Data)

ปลั๊กอินส่งข้อมูลประสิทธิภาพในรูปแบบมาตรฐานของ Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

ข้อมูลประสิทธิภาพของราคาประกอบด้วยช่วง warning/critical ที่กำหนดค่าไว้ และค่าต่ำสุดเป็นศูนย์ ค่าเกณฑ์จะพิมพ์ในรูปแบบทศนิยมเต็มรูป ไม่ปัดเศษหรือใช้รูปแบบเลขชี้กำลัง (exponent) เพื่อให้ค่าขนาดใหญ่อย่าง `14500000:16250000` ยังคงแยกวิเคราะห์ได้ เวลาของคำขอรวมทุกความพยายามในการเรียกและ backoff อายุของราคาจะแสดงเฉพาะเมื่อผู้ให้บริการส่ง timestamp ที่ถูกต้องมาให้ และการเปลี่ยนแปลงรายวันจะแสดงเมื่อมีข้อมูล ช่วงการเปลี่ยนแปลงมีความสมมาตรรอบศูนย์ ข้อมูลที่ไม่ถูกต้องหรือเก่าเกินไปจะคืนค่า `UNKNOWN` โดยไม่มีข้อมูลประสิทธิภาพของราคา เมทริกเหล่านี้สามารถนำไปใช้กับเครื่องมือสร้างกราฟอย่าง PNP4Nagios, Grafana หรือ InfluxDB ได้

## API

ปลั๊กอินนี้ใช้ [CoinGecko API](https://www.coingecko.com/en/api) เป็นค่าเริ่มต้น ซึ่งใช้งานได้ฟรีและไม่ต้องใช้ API key แต่มีข้อจำกัดด้านอัตราการเรียกใช้ (rate limit)

Endpoint แบบกำหนดเองต้องใช้โครงสร้างการตอบกลับเดียวกัน: `bitcoin.<currency>` สำหรับราคา, `bitcoin.last_updated_at` สำหรับ UNIX timestamp เป็นวินาที และ `bitcoin.<currency>_24h_change` สำหรับการเปลี่ยนแปลงเป็นเปอร์เซ็นต์รายวันแบบมีเครื่องหมาย เมื่อไม่ได้ระบุ `--max-age` และเกณฑ์การเปลี่ยนแปลง จะต้องการเพียงราคาเท่านั้น หากมี timestamp ส่งมาด้วย ก็ยังคงถูกตรวจสอบ: ต้องไม่เป็นเวลาในอนาคตหรือเก่าเกินหนึ่งชั่วโมง การตอบกลับหลังถอดรหัสต้องมีขนาดไม่เกิน 64 KiB

สกุลเงินที่รองรับ ได้แก่: usd, eur, gbp, jpy, aud, cad, chf, cny และอื่นๆ อีกมากมาย

## ความปลอดภัย

มาตรการด้านล่างนี้ถูกนำไปใช้แล้วในโค้ดปัจจุบัน มาตรการเหล่านี้จำกัดสิ่งที่ endpoint ที่ทำงานผิดปกติหรือผู้ใช้ในเครื่องสามารถทำกับโฮสต์ที่มอนิเตอร์ได้ แต่ไม่ได้ทำให้ตัวข้อมูลราคามีความน่าเชื่อถือในตัวเอง

- ใบรับรอง HTTPS ได้รับการตรวจสอบด้วยค่าเริ่มต้นของ `requests` และไม่มีตัวเลือกสำหรับปิดการตรวจสอบ `--api-url` แบบกำหนดเองที่ใช้ `http://` ธรรมดาจะไม่มีการป้องกันดังกล่าว
- DNS, การเชื่อมต่อ, การอ่าน, การลองใหม่ และ backoff ใช้กำหนดเวลา `--timeout` ร่วมกัน ฝั่งปลายทางที่ส่งข้อมูลช้าไม่สามารถขยายเวลานี้ได้
- การตอบกลับแต่ละครั้งถูกจำกัดขนาดไว้ที่ 64 KiB หลังการคลายการบีบอัด และเนื้อหาของ redirect จะถูกทิ้งโดยไม่อ่าน
- ความล้มเหลวของคำขอจะแสดงเพียงสถานะ HTTP หรือคลาสของข้อผิดพลาด เนื่องจาก `--api-url` แบบกำหนดเองอาจมีข้อมูลรับรอง (credentials) อยู่
- คำสั่งที่ติดตั้งโดย `.deb` และ `.rpm` จะรัน Python ในโหมด isolated โดยไม่สนใจ `PYTHONPATH`, user site directory และโมดูลในไดเรกทอรีทำงาน ส่วนการติดตั้งผ่าน `pip` จะใช้ console script มาตรฐานและทำงานตามสภาพแวดล้อมที่ติดตั้งไว้
- สถานะการเคลื่อนไหวของราคาถูกอ่านและเขียนโดยไม่ติดตาม symbolic link ที่ชื่อไฟล์สถานะหรือไฟล์ lock โดยอ้างอิงกับไดเรกทอรีที่เปิดเพียงครั้งเดียวต่อการตรวจสอบ
- ไฟล์รีลีสมาพร้อมการรับรอง build provenance นอกเหนือจาก `SHA256SUMS` ดูเพิ่มเติมที่ [จาก GitHub Releases](#from-github-releases)

## การอัปเกรดจาก 1.0.0

การเปลี่ยนแปลงเหล่านี้มาพร้อมกับเวอร์ชัน 2.0.0

- ราคาที่มี timestamp จากผู้ให้บริการเก่ากว่าหนึ่งชั่วโมงจะคืนค่า `UNKNOWN` เว้นแต่จะระบุ `--max-age` ที่มากกว่านั้น Endpoint ที่ไม่ส่งคืน timestamp จะไม่ได้รับผลกระทบ
- `--currency` ยอมรับเฉพาะตัวอักษรหรือตัวเลขความยาว 2-16 ตัวเท่านั้น
- สตริงตัวเลขที่มีตัวคั่นหลักหรือช่องว่างล้อมรอบจะถูกปฏิเสธ
- ระยะเวลารอลองใหม่ที่ไม่พอดีกับงบประมาณเวลาจะรายงานความล้มเหลวต้นเหตุแทนข้อความ `API request timed out`
- แพ็กเกจแบบ native ไม่ใช้ค่า `PYTHONPATH` อีกต่อไป
- ค่าเกณฑ์ตั้งแต่หนึ่งล้านขึ้นไปจะแสดงในข้อมูลประสิทธิภาพเป็นทศนิยมปกติแทนรูปแบบเลขชี้กำลัง

## การรองรับหลายภาษา (Localization)

วิธีใช้บน CLI ข้อผิดพลาดในการตรวจสอบความถูกต้อง และคำอธิบายสถานะของปลั๊กอินรองรับ 45 ภาษา (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) โดยใช้แค็ตตาล็อกที่รวมมาในตัวซึ่งโหลดผ่าน stdlib ลำดับการเลือกภาษาจะตรวจสอบ `--lang` จากนั้นจึงตรวจสอบ `LC_ALL`, `LC_MESSAGES` และ `LANG` โดยใช้ `en` เป็นค่าสำรอง ส่วนคำนำหน้าสถานะของ Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) และข้อมูลประสิทธิภาพจะยังคงเดิมในทุกภาษา

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## การพัฒนา

ติดตั้ง [mise](https://mise.jdx.dev/getting-started.html) จากนั้นรันการตั้งค่าสำหรับการพัฒนาด้านบน `mise.toml` ระบุเวอร์ชันของ Python และ uv เครื่องมือสำหรับการพัฒนาถูกประกาศไว้ใน `pyproject.toml` และจัดการเวอร์ชันในไฟล์ `uv.lock` ที่คอมมิตไว้

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

ติดตั้ง commit hooks หลังการตั้งค่า:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

ใช้ `mise exec -- uv add --dev <tool>` หรือ `mise exec -- uv add <dependency>` เพื่ออัปเดต dependency และคอมมิตทั้ง `pyproject.toml` และ `uv.lock`

CI ทดสอบ Python 3.12 และ 3.13 บน Linux และ Python 3.13 บน macOS ทุก PR ยังรันการตรวจสอบแพ็กเกจ การตรวจสอบ dependency และ CodeQL รวมถึงติดตั้ง `.deb` บน Ubuntu และ `.rpm` บน Fedora ไฟล์แจกจ่ายที่สร้างขึ้นพร้อมใช้งานในชื่อ artifact `distributions` บนการรัน CI

เวอร์ชันของแพ็กเกจและ CLI มาจาก `check_bitcoin_price/__init__.py` ดู [ขั้นตอนการออกรีลีส](../../../CONTRIBUTING.md#releases) สำหรับการปรับเวอร์ชันและการเผยแพร่ไฟล์รีลีสบน GitHub โดยอัตโนมัติ

## การมีส่วนร่วม

ดู [CONTRIBUTING.md](../../../CONTRIBUTING.md) สำหรับเวิร์กโฟลว์การพัฒนาและข้อกำหนดการลงลายมือชื่อยืนยันในคอมมิต (signed-off commit)

## สัญญาอนุญาต

โปรเจกต์นี้อยู่ภายใต้สัญญาอนุญาต MIT License - ดูรายละเอียดเพิ่มเติมในไฟล์ [LICENSE](../../../LICENSE)

## ผู้พัฒนา

Thomas Vincent

## กิตติกรรมประกาศ

- [CoinGecko](https://www.coingecko.com/) ที่ให้บริการ API สกุลเงินดิจิทัลฟรี
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
