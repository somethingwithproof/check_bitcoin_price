# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · **فارسی** · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

یک افزونه Nagios/Icinga برای پایش قیمت Bitcoin با آستانه‌های قابل پیکربندی هشدار و بحرانی.

## ویژگی‌ها

- پایش قیمت Bitcoin در ارزهای مختلف (USD، EUR، GBP و غیره)
- آستانه‌های قابل پیکربندی هشدار و بحرانی (حد بالا و پایین)
- خروجی استاندارد افزونه Nagios همراه با داده‌های کارایی
- استفاده از API سرویس CoinGecko (رایگان، بدون نیاز به کلید API)
- پشتیبانی از نقطه‌های پایانی سفارشی API
- زمان انتظار قابل پیکربندی
- بررسی تازگی نرخ با استفاده از برچسب زمانی ارائه‌دهنده، با محدودیت پیش‌فرض یک‌ساعته
- تلاش‌های مجدد محدود برای محدودیت نرخ درخواست و خطاهای موقت API
- یک مهلت زمانی واحد برای همه تلاش‌ها و سقف ۶۴ KiB برای هر پاسخ
- هشدارهای اختیاری بر اساس قدر مطلق درصد تغییرات ۲۴ ساعته
- ثبت آستانه‌های قیمت، مدت‌زمان درخواست و سن نرخ در داده‌های کارایی

## نصب

### از طریق GitHub Releases

فایل‌های `.deb`، `.rpm`، `.tar.gz`، wheel و `SHA256SUMS` را از [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) دانلود کنید. صحت فایل دانلودشده را با `sha256sum --ignore-missing --check SHA256SUMS` بررسی کنید. نسخه‌های پس از 1.0.0 دارای گواهی امضاشده منشأ ساخت نیز هستند؛ با دستور `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` مطمئن شوید که فایل از گردش‌کار انتشار همین مخزن آمده است.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

از نام فایل‌های نسخه انتخاب‌شده استفاده کنید. بسته‌های بومی فایل‌های `/usr/bin/check_bitcoin_price` و `/usr/lib/nagios/plugins/check_bitcoin_price` را نصب می‌کنند؛ بسته RPM فایل `/usr/lib64/nagios/plugins/check_bitcoin_price` را نیز فراهم می‌کند. دستور بسته‌بندی‌شده، Python را در حالت ایزوله اجرا می‌کند، بنابراین `PYTHONPATH` و ماژول‌های موجود در دایرکتوری کاری را نادیده می‌گیرد؛ مدیر بسته سیستم وابستگی‌های Python و `requests` را برطرف می‌کند. این بسته‌ها شامل کد Python مستقل از معماری هستند و به توزیعی نیاز دارند که Python 3.12 یا جدیدتر را ارائه دهد.

### از کد منبع

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### برای توسعه

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## نحوه استفاده

### استفاده پایه

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### همراه با آستانه‌ها

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### آستانه‌های جداگانه

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### ارز متفاوت

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### زمان انتظار سفارشی

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### تازگی نرخ و بودجه تلاش مجدد

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

نرخی که دارای برچسب زمانی ارائه‌دهنده است، به‌طور پیش‌فرض باید حداکثر یک ساعت قدمت داشته باشد.
نقطه‌های پایانی که فقط قیمت برمی‌گردانند، در نبود `--max-age` همچنان قابل استفاده هستند.
با فعال بودن `--max-age`، برچسب‌های زمانی ناموجود، نامعتبر، مربوط به آینده یا منقضی‌شده وضعیت `UNKNOWN` را برمی‌گردانند؛ افزونه زمان دریافت محلی را جایگزین زمان نرخ ارائه‌دهنده نمی‌کند.
برچسب زمانی که دقیقاً در مرز محدودیت سنی باشد همچنان پذیرفته می‌شود. برچسب‌های زمانی آینده همیشه رد می‌شوند.

در حالت پیش‌فرض یک تلاش مجدد مجاز است. تنها خطاهای اتصال، اتمام زمان انتظار و پاسخ‌های HTTP 408/429/500/502/503/504 دوباره تلاش می‌شوند.
زمان انتظار بین تلاش‌ها از ۰.۵ ثانیه شروع می‌شود و برای تلاش‌های بعدی دو برابر می‌گردد؛ ثانیه‌های `Retry-After` و تاریخ‌های HTTP اولویت دارند.
همه تلاش‌ها، خواندن پاسخ‌ها، رمزگشایی JSON و انتظارهای تلاش مجدد از بودجه `--timeout` استفاده می‌کنند.
اگر زمان انتظار برای تلاش مجدد در این بودجه جا نگیرد، بلافاصله وضعیت `UNKNOWN` برگردانده می‌شود و خطایی که باعث آن شده، مانند `HTTP 429` یا `ConnectionError`، گزارش می‌شود، نه خطای اتمام زمان انتظار.
خطاهای احراز هویت، سایر خطاهای دائمی HTTP، JSON نامعتبر و پاسخ‌های بزرگ‌تر از ۶۴ KiB داده رمزگشایی‌شده دوباره تلاش نمی‌شوند.
برای غیرفعال کردن تلاش مجدد از `--retries 0` استفاده کنید.

### منابع جایگزین نرخ

از گزینه‌های تکرارپذیر `--fallback-url URL` با نقطه‌های پایانی سازگار با CoinGecko استفاده کنید.
برای مثال، `--fallback-url https://quotes.example.org/simple/price` را اضافه کنید.
هر منبع سهم برابری از مهلت زمانی باقی‌مانده درخواست، از جمله تلاش‌های مجدد خود، دریافت می‌کند.
خطای موقت یا تأخیر تلاش مجدد طولانی‌تر از آن سهم، باعث رفتن به منبع بعدی می‌شود.
خطاهای تأیید TLS، خطاهای دائمی HTTP و نرخ‌های نامعتبر وضعیت UNKNOWN برمی‌گردانند.
هر پاسخ نرخ به ۶۴ KiB داده رمزگشایی‌شده محدود است.
هنگام پیکربندی منابع جایگزین، وضعیت خروجی منبع پاسخ‌دهنده را بدون چاپ URL آن به‌صورت `primary`، `fallback1` و به همین ترتیب مشخص می‌کند.

### تغییرات در بازه کوتاه

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

به کاربر پایش یک دایرکتوری وضعیت خصوصی با دسترسی نوشتن روی فایل‌سیستم محلی Linux یا macOS بدهید.
فایل هم‌جوار `.lock` را بین بررسی‌ها سر جای خود نگه دارید.
برای هر بازه زمانی از یک فایل وضعیت جداگانه استفاده کنید. ارزها در داخل آن تاریخچه مستقلی دارند.
بازه پیش‌فرض ۳۶۰۰ ثانیه است. هر نرخ معتبر به برچسب زمانی ارائه‌دهنده در محدوده این بازه و محدودیت سنی نیاز دارد که اگر `--max-age` مقدار دیگری تعیین نکند، یک ساعت است.
افزونه قیمت فعلی را با قدیمی‌ترین قیمت مثبت قبلی در آن بازه مقایسه می‌کند و ثانیه‌های سپری‌شده واقعی را گزارش می‌دهد.
برچسب‌های زمانی تکراری نمونه جدیدی ایجاد نمی‌کنند.
اولین نمونه، تاریخچه منقضی‌شده یا JSON خراب یک مبنای جدید شروع می‌کند؛ معیار بازه تا زمانی که نمونه قابل مقایسه‌ای وجود نداشته باشد نامشخص است.
سایر هشدارها همچنان اعمال می‌شوند. وضعیت غیرقابل نوشتن، فایل وضعیت یا قفل به‌صورت پیوند نمادین یا نرخی قدیمی‌تر از جدیدترین نمونه ثبت‌شده وضعیت UNKNOWN برمی‌گرداند.
معیار علامت‌دار `bitcoin_move_window` از بازه‌های متقارن هشدار و بحرانی استفاده می‌کند. برابری دقیق با یک حد هشدار ایجاد نمی‌کند.

افزونه دایرکتوری وضعیت را یک‌بار در هر بررسی باز می‌کند و به‌صورت نسبی نسبت به آن عمل می‌کند، بنابراین جایگزین شدن یک بخش از مسیر در حین بررسی نمی‌تواند قفل، خواندن یا نوشتن را تغییر مسیر دهد.
پیوندهای نمادین در بخش دایرکتوری مسیر هنگام شروع بررسی دنبال می‌شوند که باعث می‌شود پیوندهای سیستمی مانند `/var` در macOS قابل استفاده بمانند.
بنابراین دایرکتوری وضعیت و دایرکتوری‌های والد آن نباید برای سایر کاربران قابل نوشتن باشند.
فایل‌های وضعیت و قفل با سطح دسترسی 0600 ایجاد می‌شوند.

### درصد تغییرات روزانه

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

آستانه‌های تغییر، قدر مطلق درصد تغییر ۲۴ ساعته علامت‌دار CoinGecko را در ارز انتخاب‌شده اندازه‌گیری می‌کنند.
تغییری که دقیقاً برابر با یک آستانه باشد هشدار ایجاد نمی‌کند.
اگر هر دو آستانه ارائه شوند، مقدار هشدار نباید از مقدار بحرانی بیشتر باشد.
داده‌های تغییر مورد نیاز ناموجود یا نامعتبر وضعیت `UNKNOWN` برمی‌گردانند.
هشدارهای قیمت و تغییر را می‌توان ترکیب کرد؛ بالاترین سطح شدت برنده می‌شود و در صورت برابر بودن شدت‌ها، قیمت اولویت دارد.

## گزینه‌های خط فرمان

| گزینه | توضیحات |
|--------|-------------|
| `-w`, `--warning` | بازه آستانه هشدار (قالب: LOW:HIGH) |
| `-c`, `--critical` | بازه آستانه بحرانی (قالب: LOW:HIGH) |
| `--warning-low` | آستانه هشدار برای قیمت پایین |
| `--warning-high` | آستانه هشدار برای قیمت بالا |
| `--critical-low` | آستانه بحرانی برای قیمت پایین |
| `--critical-high` | آستانه بحرانی برای قیمت بالا |
| `--currency` | کد ارز شامل ۲ تا ۱۶ حرف یا رقم (پیش‌فرض: usd) |
| `--timeout` | بودجه کل درخواست/تلاش مجدد API بر حسب ثانیه، شامل مقادیر اعشاری (پیش‌فرض: ۱۰) |
| `--retries` | تلاش‌های مجدد اضافی برای خطاهای موقت، ۰ تا ۵ (پیش‌فرض: ۱) |
| `--max-age` | حداکثر سن نرخ ارائه‌دهنده بر حسب ثانیه و الزامی کردن برچسب زمانی؛ نرخ‌های دارای برچسب زمانی به‌طور پیش‌فرض ۳۶۰۰ |
| `--warning-change` | حد هشدار برای قدر مطلق درصد تغییرات ۲۴ ساعته |
| `--critical-change` | حد بحرانی برای قدر مطلق درصد تغییرات ۲۴ ساعته |
| `--api-url` | نشانی URL اصلی API |
| `--fallback-url` | نقطه پایانی سازگار اضافی؛ به ترتیب اولویت تکرار کنید |
| `--state-file` | فایل JSON تاریخچه تغییرات |
| `--move-window` | بازه زمانی تغییرات بر حسب ثانیه (پیش‌فرض: ۳۶۰۰) |
| `--warning-move`, `--critical-move` | آستانه‌های قدر مطلق تغییر در بازه بر حسب درصد |
| `-v`, `--verbose` | فعال‌سازی خروجی پرجزئیات |
| `-V`, `--version` | نمایش نسخه |
| `-h`, `--help` | نمایش پیام راهنما |

## پیکربندی Nagios

### تعریف دستور

ماکروی منبع `$USER1$` در Nagios را روی دایرکتوری افزونه‌ها تنظیم کنید (بسته‌های بومی از `/usr/lib/nagios/plugins` استفاده می‌کنند). مورد زیر را به پیکربندی دستورات Nagios خود اضافه کنید:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### تعریف سرویس

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

### پیکربندی Icinga2

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

## کدهای خروج

آرگومان‌های نامعتبر، زمان‌های انتظار غیرمثبت، بازه‌های آستانه نامعتبر و قیمت‌های ناقص در پاسخ API وضعیت `UNKNOWN` (کد خروج ۳) برمی‌گردانند.
آستانه‌ها باید اعداد متناهی و نامنفی باشند و هر حد پایین نباید از حد بالای خود بیشتر باشد.
کد ارز باید ۲ تا ۱۶ حرف یا رقم باشد. پیکربندی نامعتبر پیش از برقراری ارتباط با API رد می‌شود.
قیمت‌ها باید متناهی و نامنفی باشند و به‌صورت اعداد JSON یا رشته‌های اعشاری ساده مانند `"43521.5"` ارائه شوند.
پاسخی که ارز درخواستی را نداشته باشد نام آن را ذکر می‌کند، برای مثال `Response has no EUR price`.
پاسخ‌های نامعتبر داده کارایی تولید نمی‌کنند. اطلاعات عیب‌یابی پرجزئیات به stderr ارسال می‌شود تا stdout تنها شامل یک خط وضعیت پایش باشد.

| کد | وضعیت | توضیحات |
|------|--------|-------------|
| 0 | OK | قیمت در بازه قابل قبول است |
| 1 | WARNING | قیمت از آستانه هشدار عبور کرده است |
| 2 | CRITICAL | قیمت از آستانه بحرانی عبور کرده است |
| 3 | UNKNOWN | خطایی رخ داده است (خطای API، اتمام زمان انتظار و غیره) |

## داده‌های کارایی

افزونه داده‌های کارایی را در قالب استاندارد Nagios خروجی می‌دهد:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

داده‌های کارایی قیمت شامل بازه‌های پیکربندی‌شده هشدار/بحرانی و حداقل صفر هستند.
آستانه‌ها به‌صورت کامل در نماد اعشاری چاپ می‌شوند و هرگز گرد نمی‌شوند یا در قالب نماد علمی نمایش داده نمی‌شوند، بنابراین مقادیر بزرگ مانند `14500000:16250000` همچنان قابل تجزیه باقی می‌مانند.
زمان درخواست شامل همه تلاش‌ها و زمان‌های انتظار بین آن‌ها است.
سن نرخ تنها زمانی خروجی داده می‌شود که ارائه‌دهنده برچسب زمانی معتبر ارائه دهد؛ تغییرات روزانه در صورت در دسترس بودن خروجی داده می‌شود.
بازه‌های تغییر حول صفر متقارن هستند. داده‌های نامعتبر یا منقضی‌شده وضعیت `UNKNOWN` را بدون داده‌های کارایی قیمت تولید می‌کنند.
این معیارها را می‌توان با ابزارهای رسم نمودار مانند PNP4Nagios، Grafana یا InfluxDB استفاده کرد.

## API

این افزونه به‌طور پیش‌فرض از [CoinGecko API](https://www.coingecko.com/en/api) استفاده می‌کند که رایگان است و نیازی به کلید API ندارد. محدودیت نرخ درخواست اعمال می‌شود.

نقطه‌های پایانی سفارشی باید از همان ساختار پاسخ استفاده کنند: `bitcoin.<currency>` برای قیمت، `bitcoin.last_updated_at` برای ثانیه‌های برچسب زمانی UNIX و `bitcoin.<currency>_24h_change` برای درصد تغییر روزانه علامت‌دار.
در نبود `--max-age` و آستانه‌های تغییر، فقط قیمت الزامی است.
برچسب زمانی موجود همچنان بررسی می‌شود: نباید در آینده باشد یا بیش از یک ساعت قدمت داشته باشد.
پاسخ رمزگشایی‌شده باید در ۶۴ KiB جا بگیرد.

ارزهای پشتیبانی‌شده شامل موارد زیر و بسیاری ارزهای دیگر است: usd، eur، gbp، jpy، aud، cad، chf، cny.

## امنیت

اقدامات زیر در کد فعلی پیاده‌سازی شده‌اند. این موارد کارهایی را که یک نقطه پایانی مخرب یا یک کاربر محلی می‌تواند روی میزبان پایش انجام دهد محدود می‌کنند؛ اما خود نرخ قیمت را قابل اعتماد نمی‌کنند.

- گواهینامه‌های HTTPS با پیش‌فرض‌های `requests` بررسی می‌شوند و هیچ گزینه‌ای این بررسی را غیرفعال نمی‌کند. یک `--api-url` سفارشی که از `http://` ساده استفاده کند چنین حفاظتی ندارد.
- فرایندهای DNS، اتصال، خواندن، تلاش‌های مجدد و انتظار بین تلاش‌ها همگی در مهلت زمانی `--timeout` سهیم هستند. یک همتای شبکه که داده‌ها را به کندی ارسال کند نمی‌تواند این مهلت را افزایش دهد.
- هر پاسخ پس از خارج شدن از فشرده‌سازی به ۶۴ KiB محدود می‌شود و بدنه تغییرمسیرها بدون خواندن دور ریخته می‌شود.
- خطاهای درخواست تنها وضعیت HTTP یا کلاس خطا را چاپ می‌کنند، زیرا یک `--api-url` سفارشی ممکن است حاوی اطلاعات احراز هویت باشد.
- دستور نصب‌شده توسط `.deb` و `.rpm` پایتون را در حالت ایزوله اجرا می‌کند. این حالت `PYTHONPATH`، دایرکتوری site کاربر و ماژول‌های دایرکتوری کاری را نادیده می‌گیرد. نصب از طریق `pip` از اسکریپت کنسول استاندارد استفاده می‌کند و از محیطی که در آن نصب شده پیروی می‌کند.
- وضعیت تغییرات بدون دنبال کردن پیوند نمادین در نام فایل وضعیت یا قفل، نسبت به دایرکتوری‌ای که یک‌بار در هر بررسی باز می‌شود، خوانده و نوشته می‌شود.
- فایل‌های انتشار علاوه بر `SHA256SUMS` دارای گواهی منشأ ساخت هستند؛ به بخش [از طریق GitHub Releases](#from-github-releases) مراجعه کنید.

## ارتقا از نسخه 1.0.0

این تغییرات در نسخه 2.0.0 ارائه شده‌اند.

- نرخی با برچسب زمانی ارائه‌دهنده قدیمی‌تر از یک ساعت وضعیت `UNKNOWN` برمی‌گرداند، مگر اینکه مقدار `--max-age` بزرگ‌تری تعیین شود. نقطه‌های پایانی که برچسب زمانی برنمی‌گردانند تحت تأثیر قرار نمی‌گیرند.
- گزینه `--currency` فقط ۲ تا ۱۶ حرف یا رقم را می‌پذیرد.
- رشته‌های عددی دارای جداکننده رقم یا فاصله در ابتدا و انتها رد می‌شوند.
- تأخیر تلاش مجددی که در بودجه زمانی جا نگیرد، خطای اصلی را به جای `API request timed out` گزارش می‌دهد.
- بسته‌های بومی دیگر از `PYTHONPATH` پیروی نمی‌کنند.
- آستانه‌های یک میلیون یا بیشتر در داده‌های کارایی به‌صورت اعداد اعشاری ساده به جای نماد علمی نمایش داده می‌شوند.

## بومی‌سازی

راهنمای خط فرمان، خطاهای اعتبارسنجی و توضیحات وضعیت افزونه از ۴۵ زبان (`en`، `de`، `es`، `fr`، `it`، `pt-BR`، `nl`، `ru`، `uk`، `ja`، `ko`، `zh-CN`، `zh-TW`، `ar`، `hi`، `pl`، `tr`، `sv`، `vi`، `id`، `af-ZA`، `am-ET`، `ar-EG`، `ar-MA`، `fr-MA`، `fr-SN`، `ha-NG`، `ig-NG`، `mg-MG`، `rw-RW`، `so-SO`، `sw-KE`، `xh-ZA`، `yo-NG`، `zu-ZA`، `bn`، `fa`، `he`، `mr`، `ta`، `te`، `th`، `ur`، `ms`، `fil`) با استفاده از کاتالوگ‌های همراه بسته که از طریق کتابخانه استاندارد بارگذاری می‌شوند، پشتیبانی می‌کنند. انتخاب زبان ابتدا `--lang`، سپس `LC_ALL`، `LC_MESSAGES` و `LANG` را بررسی می‌کند و در صورت نبود به `en` برمی‌گردد. پیشوندهای وضعیت Nagios (`OK`، `WARNING`، `CRITICAL`، `UNKNOWN`) و داده‌های کارایی در همه زبان‌ها بدون تغییر باقی می‌مانند.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## توسعه

[mise](https://mise.jdx.dev/getting-started.html) را نصب کنید و سپس مراحل راه‌اندازی توسعه در بالا را اجرا کنید. فایل `mise.toml` نسخه Python و uv را تثبیت می‌کند. ابزارهای توسعه در `pyproject.toml` تعریف شده و در فایل `uv.lock` ثبت‌شده حل و فصل می‌شوند.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

پس از راه‌اندازی، هوک‌های کامیت را نصب کنید:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

برای به‌روزرسانی وابستگی‌ها از `mise exec -- uv add --dev <tool>` یا `mise exec -- uv add <dependency>` استفاده کنید و هر دو فایل `pyproject.toml` و `uv.lock` را کامیت کنید.

سامانه CI نسخه‌های Python 3.12 و 3.13 را روی Linux و Python 3.13 را روی macOS بررسی می‌کند. هر PR همچنین اعتبارسنجی بسته، ممیزی وابستگی‌ها و CodeQL را اجرا می‌کند و بسته `.deb` را روی Ubuntu و `.rpm` را روی Fedora نصب می‌کند. بسته‌های ساخته‌شده به‌عنوان آرتیفکت `distributions` در اجراهای CI در دسترس هستند.

نسخه بسته و خط فرمان از `check_bitcoin_price/__init__.py` گرفته می‌شود. برای افزایش نسخه و انتشار خودکار فایل‌های انتشار GitHub به [فرایند انتشار](../../../CONTRIBUTING.md#releases) مراجعه کنید.

## مشارکت

برای آشنایی با گردش‌کار توسعه و الزامات امضای کامیت‌ها به [CONTRIBUTING.md](../../../CONTRIBUTING.md) مراجعه کنید.

## مجوز

این پروژه تحت مجوز MIT منتشر شده است؛ برای جزئیات فایل [LICENSE](../../../LICENSE) را ببینید.

## نویسنده

Thomas Vincent

## قدردانی

- [CoinGecko](https://www.coingecko.com/) برای ارائه API رایگان ارز دیجیتال
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
