# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · **اردو** · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

قابلِ ترتیب warning اور critical حدوں کے ساتھ Bitcoin کی قیمت کی نگرانی کے لیے ایک Nagios/Icinga پلگ ان۔

## خصوصیات

- متعدد کرنسیوں (USD، EUR، GBP، وغیرہ) میں Bitcoin کی قیمت کی نگرانی
- قابلِ ترتیب warning اور critical حدیں (بالائی اور زیریں)
- کارکردگی کے ڈیٹا کے ساتھ معیاری Nagios پلگ ان آؤٹ پٹ
- CoinGecko API کا استعمال (مفت، کسی API کلید کی ضرورت نہیں)
- حسبِ ضرورت API اینڈ پوائنٹس کی معاونت
- قابلِ ترتیب ٹائم آؤٹ
- وینڈر ٹائم اسٹیمپ استعمال کرتے ہوئے کوٹ کی تازگی کی جانچ، ایک گھنٹے کی طے شدہ حد کے ساتھ
- شرح کی حدود اور عارضی API ناکامیوں کے لیے محدود دوبارہ کوششیں
- تمام کوششوں کے لیے ایک ہی ڈیڈ لائن اور ہر جواب پر 64 KiB کی حد
- 24 گھنٹے کی مطلق فیصد حرکت پر اختیاری الرٹس
- کارکردگی کے ڈیٹا میں قیمت کی حدیں، درخواست کا دورانیہ، اور کوٹ کی عمر

## تنصیب

<a name="from-github-releases"></a>

### GitHub Releases سے

[GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) سے `.deb`، `.rpm`، `.tar.gz`، wheel، اور `SHA256SUMS` فائلیں ڈاؤن لوڈ کریں۔ ڈاؤن لوڈ کی تصدیق `sha256sum --ignore-missing --check SHA256SUMS` سے کریں۔ 1.0.0 کے بعد کی ریلیزز میں دستخط شدہ بلڈ پروونینس بھی شامل ہے؛ `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` کے ذریعے تصدیق کریں کہ ایسٹ اسی ریپازٹری کے ریلیز ورک فلو سے آیا ہے۔

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

منتخب کردہ ریلیز سے فائلوں کے نام استعمال کریں۔ مقامی پیکجز `/usr/bin/check_bitcoin_price` اور `/usr/lib/nagios/plugins/check_bitcoin_price` نصب کرتے ہیں؛ RPM پیکج `/usr/lib64/nagios/plugins/check_bitcoin_price` بھی فراہم کرتا ہے۔ پیکج شدہ کمانڈ Python کو آئسولیٹڈ موڈ میں چلاتی ہے، اس لیے یہ `PYTHONPATH` اور ورکنگ ڈائریکٹری میں موجود ماڈیولز کو نظر انداز کرتی ہے؛ سسٹم پیکج مینیجر Python اور `requests` کی انحصاریت کو حل کرتا ہے۔ ان میں آرکیٹیکچر سے آزاد Python کوڈ موجود ہوتا ہے اور ان کے لیے Python 3.12 یا اس سے جدید ورژن فراہم کرنے والی ڈسٹری بیوشن درکار ہوتی ہے۔

### سورس کوڈ سے

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### ڈیولپمنٹ کے لیے

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## استعمال

### بنیادی استعمال

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### حدود کے ساتھ

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### انفرادی حدود

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### مختلف کرنسی

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### حسبِ ضرورت ٹائم آؤٹ

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### تازگی اور دوبارہ کوششوں کا بجٹ

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

جس کوٹ میں وینڈر کا ٹائم اسٹیمپ شامل ہو وہ طے شدہ طور پر زیادہ سے زیادہ ایک گھنٹہ پرانا ہونا چاہیے۔
وہ اینڈ پوائنٹس جو صرف قیمت واپس کرتے ہیں `--max-age` نہ ہونے کی صورت میں قابلِ استعمال رہتے ہیں۔
`--max-age` کے ساتھ، غائب، غلط، مستقبل کے، یا پرانے وینڈر ٹائم اسٹیمپس
`UNKNOWN` واپس کرتے ہیں؛ پلگ ان وینڈر کے کوٹ کے وقت کی جگہ مقامی fetch کا وقت
استعمال نہیں کرتا۔ عین عمر کی حد پر موجود ٹائم اسٹیمپ قابلِ قبول رہتا ہے۔ مستقبل کے
ٹائم اسٹیمپس ہمیشہ مسترد کیے جاتے ہیں۔

طے شدہ ترتیب ایک بار دوبارہ کوشش کی اجازت دیتی ہے۔ صرف کنکشن کی خرابیوں، ٹائم آؤٹس، اور HTTP
408/429/500/502/503/504 جوابات پر دوبارہ کوشش کی جاتی ہے۔ بیک آف 0.5 سیکنڈ سے شروع ہوتا ہے اور
بعد کی کوششوں کے لیے دوگنا ہو جاتا ہے؛ `Retry-After` کے سیکنڈز اور HTTP تاریخوں کو
ترجیح حاصل ہوتی ہے۔ تمام کوششیں، جواب پڑھنا، JSON ڈی کوڈنگ، اور دوبارہ کوشش کا انتظار سب مل کر
`--timeout` کا بجٹ استعمال کرتے ہیں۔ اگر دوبارہ کوشش کا انتظار اس بجٹ میں پورا نہ آ سکے تو فوراً `UNKNOWN` واپس آتا ہے
اور ٹائم آؤٹ کے بجائے اس خرابی کی اطلاع دی جاتی ہے جس کی وجہ سے دوبارہ کوشش کی گئی، جیسے `HTTP 429` یا `ConnectionError`۔
تصدیقی ناکامیوں، دیگر مستقل HTTP خرابیوں، غلط
JSON، اور ڈی کوڈ شدہ ڈیٹا کے 64 KiB سے بڑے جوابات پر دوبارہ کوشش نہیں کی جاتی۔ دوبارہ کوششوں کو غیر فعال کرنے کے لیے
`--retries 0` استعمال کریں۔

### متبادل کوٹ ذرائع

CoinGecko سے مطابقت رکھنے والے اینڈ پوائنٹس کے ساتھ دہرائے جا سکنے والے `--fallback-url URL` اختیارات استعمال کریں۔
مثال کے طور پر، `--fallback-url https://quotes.example.org/simple/price` شامل کریں۔
ہر ذریعے کو درخواست کی باقی ماندہ ڈیڈ لائن کا برابر حصہ ملتا ہے، بشمول اس کی
دوبارہ کوششوں کے۔ عارضی ناکامی یا اس حصے سے زیادہ طویل دوبارہ کوشش کی تاخیر
اگلے ذریعے کی طرف منتقل کر دیتی ہے۔ TLS تصدیق کی ناکامیاں، مستقل HTTP خرابیاں اور غلط
کوٹس UNKNOWN واپس کرتے ہیں۔ ہر کوٹ جواب ڈی کوڈ شدہ ڈیٹا کے 64 KiB تک محدود ہے۔
جب fallbacks ترتیب دیے گئے ہوں تو اسٹیٹس جواب دینے والے ذریعے کی شناخت
`primary`، `fallback1` وغیرہ کے طور پر کرتا ہے، بغیر اس کا URL پرنٹ کیے۔

### قلیل مدتی حرکت

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

مانیٹرنگ صارف کو مقامی Linux یا macOS فائل سسٹم پر ایک نجی اور قابلِ تحریر اسٹیٹ ڈائریکٹری دیں۔ چیک کے درمیان ساتھ والی `.lock` فائل کو اپنی جگہ رہنے دیں۔ فی ونڈو ایک علیحدہ اسٹیٹ فائل استعمال کریں۔ اس کے اندر کرنسیوں کی الگ الگ ہسٹری محفوظ ہوتی ہے۔
طے شدہ ونڈو 3600 سیکنڈ ہے۔ ہر درست کوٹ کے لیے ونڈو اور عمر کی حد کے اندر وینڈر ٹائم اسٹیمپ درکار ہوتا ہے، جو ایک گھنٹہ ہے جب تک `--max-age` کوئی اور حد مقرر نہ کرے۔ پلگ ان موجودہ
قیمت کا موازنہ اس ونڈو میں سب سے پرانی پچھلی مثبت قیمت سے کرتا ہے اور گزرے ہوئے
اصل سیکنڈز کی اطلاع دیتا ہے۔ دہرائے گئے ٹائم اسٹیمپس اضافی نمونے نہیں بناتے۔
پہلا نمونہ، زائد المیعاد ہسٹری، یا خراب JSON ایک نئی بیس لائن شروع کرتا ہے؛ جب تک کوئی قابلِ موازنہ نمونہ نہ ہو
ونڈو میٹرک unknown رہتا ہے۔ دیگر الرٹس بدستور لاگو رہتے ہیں۔
ناقابلِ تحریر اسٹیٹ، سمبولک لنک اسٹیٹ یا لاک فائل، یا تازہ ترین ریکارڈ شدہ نمونے سے پرانا
کوٹ UNKNOWN واپس کرتا ہے۔ علامتی `bitcoin_move_window` میٹرک
متناسب warning اور critical حدود استعمال کرتا ہے۔ عین حد کے برابر ہونے پر الرٹ جاری نہیں ہوتا۔

پلگ ان فی چیک ایک بار اسٹیٹ ڈائریکٹری کھولتا ہے اور اس کے حوالے سے کام کرتا ہے، تاکہ
چیک کے دوران تبدیل کیا گیا کوئی پاتھ کمپوننٹ لاک، پڑھنے،
یا لکھنے کو ری ڈائریکٹ نہ کر سکے۔ چیک شروع ہونے پر پاتھ کے ڈائریکٹری حصے میں موجود سمبولک لنکس کی پیروی کی جاتی ہے،
جس سے macOS پر `/var` جیسے پلیٹ فارم لنکس قابلِ استعمال رہتے ہیں۔ لہذا
اسٹیٹ ڈائریکٹری اور اس کی بالائی ڈائریکٹریز دیگر صارفین کے لیے قابلِ تحریر نہیں ہونی
چاہئیں۔ اسٹیٹ اور لاک فائلیں موڈ 0600 کے ساتھ بنائی جاتی ہیں۔

### یومیہ فیصد حرکت

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

تبدیلی کی حدیں منتخب کرنسی میں CoinGecko کی علامتی 24 گھنٹے کی
فیصد تبدیلی کی مطلق قدر کی پیمائش کرتی ہیں۔ عین حد کے برابر تبدیلی پر
الرٹ جاری نہیں ہوتا۔ اگر دونوں حدیں فراہم کی جائیں تو warning کی حد critical سے زیادہ نہیں ہونی چاہیے۔
مطلوبہ تبدیلی کا ڈیٹا غائب یا غلط ہونے پر `UNKNOWN` واپس آتا ہے۔ قیمت اور تبدیلی کے
الرٹس کو یکجا کیا جا سکتا ہے؛ سب سے زیادہ شدت کو ترجیح ملتی ہے، اور
شدت برابر ہونے پر قیمت کو ترجیح دی جاتی ہے۔

## کمانڈ لائن اختیارات

| اختیار | تفصیل |
|--------|-------------|
| `-w`، `--warning` | Warning حد کی رینج (فارمیٹ: LOW:HIGH) |
| `-c`، `--critical` | Critical حد کی رینج (فارمیٹ: LOW:HIGH) |
| `--warning-low` | کم قیمت کے لیے warning حد |
| `--warning-high` | زیادہ قیمت کے لیے warning حد |
| `--critical-low` | کم قیمت کے لیے critical حد |
| `--critical-high` | زیادہ قیمت کے لیے critical حد |
| `--currency` | 2-16 حروف یا ہندسوں پر مشتمل کرنسی کوڈ (طے شدہ: usd) |
| `--timeout` | سیکنڈز میں کل API درخواست/دوبارہ کوشش کا بجٹ، بشمول کسری قدریں (طے شدہ: 10) |
| `--retries` | اضافی عارضی کوششیں، 0-5 (طے شدہ: 1) |
| `--max-age` | سیکنڈز میں وینڈر کوٹ کی زیادہ سے زیادہ عمر اور ٹائم اسٹیمپ کا تقاضا؛ ٹائم اسٹیمپ والے کوٹس طے شدہ طور پر 3600 ہیں |
| `--warning-change` | 24 گھنٹے کی مطلق فیصد حرکت کے لیے warning حد |
| `--critical-change` | 24 گھنٹے کی مطلق فیصد حرکت کے لیے critical حد |
| `--api-url` | بنیادی API URL |
| `--fallback-url` | اضافی مطابقت پذیر اینڈ پوائنٹ؛ ترجیحی ترتیب میں دہرائیں |
| `--state-file` | JSON حرکت کی ہسٹری فائل |
| `--move-window` | سیکنڈز میں حرکت کی ونڈو (طے شدہ: 3600) |
| `--warning-move`، `--critical-move` | فیصد میں ونڈو حرکت کی مطلق حدود |
| `-v`، `--verbose` | تفصیلی آؤٹ پٹ فعال کریں |
| `-V`، `--version` | ورژن دکھائیں |
| `-h`، `--help` | مدد کا پیغام دکھائیں |

## Nagios ترتیب

### کمانڈ کی تعریف

Nagios ریسورس میکرو `$USER1$` کو پلگ ان ڈائریکٹری پر سیٹ کریں (مقامی پیکجز `/usr/lib/nagios/plugins` استعمال کرتے ہیں)۔ اپنی Nagios کمانڈز کی ترتیب میں شامل کریں:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### سروس کی تعریف

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

### Icinga2 ترتیب

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

## ایگزٹ کوڈز

غلط دلائل، غیر مثبت ٹائم آؤٹس، غلط حدوں کی رینج، اور خراب ساختہ
API قیمتیں `UNKNOWN` (exit 3) واپس کرتی ہیں۔ حدیں محدود، غیر منفی
اعداد ہونی چاہئیں، جن میں ہر زیریں حد اپنی بالائی حد سے بڑی نہ ہو۔ کرنسی
2-16 حروف یا ہندسوں پر مشتمل ہونی چاہیے۔ API سے رابطہ کرنے سے پہلے ہی غلط ترتیب کو مسترد کر دیا جاتا ہے۔
قیمتیں محدود اور غیر منفی ہونی چاہئیں، جو JSON اعداد یا سادہ
اعشاری سٹرنگز جیسے `"43521.5"` کی صورت میں دی گئی ہوں۔ اگر جواب میں مطلوبہ کرنسی موجود نہ ہو
تو اس کا نام بتایا جاتا ہے، مثلاً `Response has no EUR price`۔ غلط جوابات
کارکردگی کا ڈیٹا خارج نہیں کرتے۔ تفصیلی تشخیصی پیغامات stderr پر جاتے ہیں
تاکہ stdout پر مانیٹرنگ اسٹیٹس کی صرف ایک ہی سطر رہے۔

| کوڈ | حالت | تفصیل |
|------|--------|-------------|
| 0 | OK | قیمت قابلِ قبول حد کے اندر ہے |
| 1 | WARNING | قیمت نے warning حد پار کر لی |
| 2 | CRITICAL | قیمت نے critical حد پار کر لی |
| 3 | UNKNOWN | خرابی پیش آئی (API ناکامی، ٹائم آؤٹ، وغیرہ) |

## کارکردگی کا ڈیٹا

پلگ ان معیاری Nagios فارمیٹ میں کارکردگی کا ڈیٹا آؤٹ پٹ کرتا ہے:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

قیمت کے کارکردگی کے ڈیٹا میں ترتیب دی گئی warning/critical حدود اور
کم از کم صفر شامل ہوتا ہے۔ حدیں مکمل اعشاری علامت میں پرنٹ کی جاتی ہیں، کبھی راؤنڈ نہیں کی جاتیں
اور نہ ہی exponent فارم میں ہوتی ہیں، تاکہ بڑی قدریں جیسے `14500000:16250000` قابلِ تجزیہ رہیں۔ درخواست کے وقت میں تمام کوششیں اور بیک آف شامل ہوتے ہیں۔ کوٹ کی عمر
صرف اس وقت ظاہر کی جاتی ہے جب وینڈر درست ٹائم اسٹیمپ فراہم کرے؛ یومیہ تبدیلی دستیاب ہونے پر
ظاہر کی جاتی ہے۔ تبدیلی کی رینجز صفر کے گرد متناسب ہوتی ہیں۔ غلط یا پرانا ڈیٹا
قیمت کے کارکردگی کے ڈیٹا کے بغیر `UNKNOWN` پیدا کرتا ہے۔ ان میٹرکس کو
PNP4Nagios، Grafana، یا InfluxDB جیسے گرافنگ ٹولز کے ساتھ استعمال کیا جا سکتا ہے۔

## API

یہ پلگ ان طے شدہ طور پر [CoinGecko API](https://www.coingecko.com/en/api) استعمال کرتا ہے، جو مفت ہے اور اس کے لیے کسی API کلید کی ضرورت نہیں ہے۔ شرح کی حدود لاگو ہوتی ہیں۔

حسبِ ضرورت اینڈ پوائنٹس کو بھی یہی جوابی ساخت استعمال کرنی چاہیے: قیمت کے لیے `bitcoin.<currency>`،
UNIX ٹائم اسٹیمپ سیکنڈز کے لیے `bitcoin.last_updated_at`، اور
علامتی یومیہ فیصد حرکت کے لیے `bitcoin.<currency>_24h_change`۔ صرف قیمت
درکار ہوتی ہے جب `--max-age` اور تبدیلی کی حدیں موجود نہ ہوں۔ اگر ٹائم اسٹیمپ
موجود ہو تو اس کی جانچ پھر بھی کی جاتی ہے: یہ مستقبل کا یا ایک گھنٹے سے زیادہ پرانا
نہیں ہونا چاہیے۔ ڈی کوڈ شدہ جواب 64 KiB کے اندر سما جانا چاہیے۔

معاونت یافتہ کرنسیوں میں شامل ہیں: usd، eur، gbp، jpy، aud، cad، chf، cny، اور بہت سی دیگر۔

## سیکیورٹی

درج ذیل اقدامات موجودہ کوڈ میں نافذ ہیں۔ یہ ان حدود کا تعین کرتے ہیں کہ کوئی غلط برتاؤ کرنے والا اینڈ پوائنٹ یا مقامی صارف
مانیٹرنگ ہوسٹ پر کیا کر سکتا ہے؛ یہ خود کوٹ کو قابلِ اعتماد نہیں بناتے۔

- HTTPS سرٹیفکیٹس کی تصدیق `requests` کے طے شدہ اصولوں سے کی جاتی ہے، اور کوئی بھی اختیار
  تصدیق کو غیر فعال نہیں کرتا۔ سادہ `http://` استعمال کرنے والے حسبِ ضرورت `--api-url` کو
  ایسا کوئی تحفظ حاصل نہیں ہوتا۔
- DNS، کنکشن، ریڈز، دوبارہ کوششیں، اور بیک آف سب `--timeout` کی ڈیڈ لائن کا اشتراک کرتے ہیں۔ آہستہ
  ڈیٹا بھیجنے والا پیئر اسے بڑھا نہیں سکتا۔
- ہر جواب ڈی کمپریشن کے بعد 64 KiB تک محدود ہے، اور ری ڈائریکٹ باڈیز
  کو پڑھے بغیر مسترد کر دیا جاتا ہے۔
- درخواست کی ناکامیاں صرف HTTP اسٹیٹس یا ایرر کلاس پرنٹ کرتی ہیں، کیونکہ حسبِ ضرورت
  `--api-url` میں اسناد شامل ہو سکتی ہیں۔
- `.deb` اور `.rpm` کے ذریعے نصب کردہ کمانڈ Python کو آئسولیٹڈ موڈ میں چلاتی ہے۔
  یہ `PYTHONPATH`، یوزر سائٹ ڈائریکٹری، اور ورکنگ ڈائریکٹری میں موجود ماڈیولز کو
  نظر انداز کرتی ہے۔ `pip` تنصیب معیاری کنسول اسکرپٹ استعمال کرتی ہے اور اس
  ماحول کی پیروی کرتی ہے جس میں اسے نصب کیا گیا ہو۔
- حرکت کا اسٹیٹ اسٹیٹ یا لاک فائل کے نام پر سمبولک لنک کی پیروی کیے بغیر
  پڑھا اور لکھا جاتا ہے، اس ڈائریکٹری کے حوالے سے جو فی چیک ایک بار کھولی جاتی ہے۔
- ریلیز ایسٹس میں `SHA256SUMS` کے علاوہ بلڈ پروونینس تصدیقات
  بھی شامل ہوتی ہیں؛ دیکھیں [GitHub Releases سے](#from-github-releases)۔

## 1.0.0 سے اپ گریڈ کرنا

یہ تبدیلیاں 2.0.0 میں شامل ہیں۔

- ایک گھنٹے سے زیادہ پرانے وینڈر ٹائم اسٹیمپ والا کوٹ `UNKNOWN` واپس کرتا ہے جب تک کہ کوئی
  بڑا `--max-age` نہ دیا جائے۔ وہ اینڈ پوائنٹس جو کوئی ٹائم اسٹیمپ واپس نہیں کرتے متاثر نہیں ہوتے۔
- `--currency` صرف 2-16 حروف یا ہندسوں کو قبول کرتا ہے۔
- ہندسوں کے الگ کار (digit separators) یا اطراف میں خالی جگہوں والی عددی سٹرنگز مسترد کر دی جاتی ہیں۔
- دوبارہ کوشش کا انتظار جو بجٹ میں پورا نہ آئے `API request timed out` کے بجائے بنیادی خرابی
  کی اطلاع دیتا ہے۔
- مقامی پیکجز اب `PYTHONPATH` کو قبول نہیں کرتے۔
- دس لاکھ یا اس سے زیادہ کی حدیں کارکردگی کے ڈیٹا میں exponent علامت کے بجائے
  سادہ اعشاری اعداد کے طور پر ظاہر ہوتی ہیں۔

## لوکلائزیشن

CLI مدد، توثیقی خرابیاں، اور پلگ ان اسٹیٹس کی تفصیلات بنڈل شدہ stdlib-loaded کیٹلاگز کا استعمال کرتے ہوئے 45 لوکیلز (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) کی معاونت کرتی ہیں۔ ریزولوشن `--lang`، پھر `LC_ALL`، `LC_MESSAGES`، اور `LANG` کو چیک کرتی ہے، اور آخر میں `en` پر واپس آتی ہے۔ Nagios اسٹیٹس پریفکسز (`OK`، `WARNING`، `CRITICAL`، `UNKNOWN`) اور کارکردگی کا ڈیٹا تمام لوکیلز میں برقرار رہتے ہیں۔

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## ڈیولپمنٹ

[mise](https://mise.jdx.dev/getting-started.html) نصب کریں، پھر اوپر دیا گیا ڈیولپمنٹ سیٹ اپ چلائیں۔ `mise.toml` Python اور uv کو پن کرتا ہے۔ ڈیولپمنٹ ٹولز `pyproject.toml` میں اعلان کیے گئے ہیں اور کمٹ شدہ `uv.lock` میں حل کیے گئے ہیں۔

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

سیٹ اپ کے بعد کمٹ ہکس نصب کریں:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

انحصاریت کو اپ ڈیٹ کرنے کے لیے `mise exec -- uv add --dev <tool>` یا `mise exec -- uv add <dependency>` استعمال کریں اور `pyproject.toml` اور `uv.lock` دونوں کو کمٹ کریں۔

CI Linux پر Python 3.12 اور 3.13 اور macOS پر Python 3.13 کی جانچ کرتا ہے۔ ہر PR پیکج کی توثیق، انحصاریت کا آڈٹ، اور CodeQL بھی چلاتا ہے، اور Ubuntu پر `.deb` اور Fedora پر `.rpm` نصب کرتا ہے۔ بلڈ شدہ ڈسٹری بیوشنز CI رنز پر `distributions` آرٹیفیکٹ کے طور پر دستیاب ہیں۔

پیکج اور CLI ورژن `check_bitcoin_price/__init__.py` سے آتا ہے۔ ورژن بڑھانے اور GitHub ریلیز ایسٹس کی خودکار اشاعت کے لیے [ریلیز کا عمل](../../../CONTRIBUTING.md#releases) دیکھیں۔

## تعاون

ڈیولپمنٹ ورک فلو اور دستخط شدہ کمٹ کی ضروریات کے لیے [CONTRIBUTING.md](../../../CONTRIBUTING.md) دیکھیں۔

## لائسنس

یہ پروجیکٹ MIT لائسنس کے تحت جاری کیا گیا ہے - تفصیلات کے لیے [LICENSE](../../../LICENSE) فائل دیکھیں۔

## مصنف

Thomas Vincent

## اظہارِ تشکر

- مفت کرپٹو کرنسی API فراہم کرنے کے لیے [CoinGecko](https://www.coingecko.com/)
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
