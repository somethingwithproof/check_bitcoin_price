# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · **বাংলা** · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

কনফিগারযোগ্য warning এবং critical থ্রেশহোল্ডসহ Bitcoin-এর মূল্য পর্যবেক্ষণের জন্য একটি Nagios/Icinga প্লাগইন।

## বৈশিষ্ট্যসমূহ

- একাধিক মুদ্রায় (USD, EUR, GBP ইত্যাদি) Bitcoin-এর মূল্য পর্যবেক্ষণ
- কনফিগারযোগ্য warning এবং critical থ্রেশহোল্ড (উচ্চ এবং নিম্ন)
- পারফরম্যান্স ডেটাসহ স্ট্যান্ডার্ড Nagios প্লাগইন আউটপুট
- CoinGecko API ব্যবহার করে (বিনামূল্যে, কোনো API কী প্রয়োজন নেই)
- কাস্টম API এন্ডপয়েন্টের জন্য সমর্থন
- কনফিগারযোগ্য টাইমআউট
- ভেন্ডর টাইমস্ট্যাম্প ব্যবহার করে কোটের সতেজতা যাচাই, ডিফল্ট এক ঘণ্টার সীমাসহ
- রেট লিমিট এবং সাময়িক API ত্রুটির জন্য সীমিত পুনঃচেষ্টা
- সব প্রচেষ্টার জন্য একটি সময়সীমা এবং প্রতিটি রেসপন্সে 64 KiB সীমা
- 24 ঘণ্টার পরম শতাংশ পরিবর্তনের ওপর ঐচ্ছিক সতর্কতা
- পারফরম্যান্স ডেটায় মূল্য থ্রেশহোল্ড, অনুরোধের সময়কাল এবং কোটের বয়স

## ইনস্টলেশন

### GitHub Releases থেকে

[GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) থেকে `.deb`, `.rpm`, `.tar.gz`, wheel এবং `SHA256SUMS` ফাইল ডাউনলোড করুন। `sha256sum --ignore-missing --check SHA256SUMS` দিয়ে ডাউনলোড যাচাই করুন। 1.0.0-এর পরবর্তী রিলিজগুলোতে স্বাক্ষরিত বিল্ড প্রোভেন্যান্সও থাকে; `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` দিয়ে নিশ্চিত করুন যে কোনো অ্যাসেট এই রিপোজিটরির রিলিজ ওয়ার্কফ্লো থেকে এসেছে।

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

নির্বাচিত রিলিজ থেকে ফাইলের নামগুলো ব্যবহার করুন। নেটিভ প্যাকেজগুলো `/usr/bin/check_bitcoin_price` এবং `/usr/lib/nagios/plugins/check_bitcoin_price` ইনস্টল করে; RPM প্যাকেজটি `/usr/lib64/nagios/plugins/check_bitcoin_price`-ও সরবরাহ করে। প্যাকেজ করা কমান্ডটি Python-কে isolated মোডে চালায়, তাই এটি `PYTHONPATH` এবং ওয়ার্কিং ডিরেক্টরির মডিউলগুলো উপেক্ষা করে; সিস্টেম প্যাকেজ ম্যানেজার Python এবং `requests` ডিপেন্ডেন্সি সমাধান করে। এগুলোতে আর্কিটেকচার-নিরপেক্ষ Python কোড থাকে এবং Python 3.12 বা তার পরবর্তী সংস্করণ সরবরাহ করে এমন ডিস্ট্রিবিউশন প্রয়োজন।

### সোর্স থেকে

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### ডেভেলপমেন্টের জন্য

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## ব্যবহারবিধি

### মৌলিক ব্যবহার

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### থ্রেশহোল্ডসহ

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### পৃথক থ্রেশহোল্ড

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### ভিন্ন মুদ্রা

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### কাস্টম টাইমআউট

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### সতেজতা এবং পুনঃচেষ্টার বাজেট

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

যে কোটে ভেন্ডর টাইমস্ট্যাম্প থাকে তা ডিফল্টভাবে সর্বোচ্চ এক ঘণ্টা পুরোনো হতে পারবে।
`--max-age` অনুপস্থিত থাকলে শুধু মূল্য ফেরত দেয় এমন এন্ডপয়েন্টগুলোও ব্যবহারযোগ্য থাকে।
`--max-age` দিলে অনুপস্থিত, অবৈধ, ভবিষ্যতের বা পুরোনো ভেন্ডর টাইমস্ট্যাম্পের ক্ষেত্রে
`UNKNOWN` ফেরত আসে; প্লাগইনটি ভেন্ডরের কোট সময়ের পরিবর্তে স্থানীয় সংগ্রহের সময়
ব্যবহার করে না। ঠিক বয়স সীমার সমান টাইমস্ট্যাম্প গ্রহণযোগ্য থাকে। ভবিষ্যতের
টাইমস্ট্যাম্প সবসময় প্রত্যাখ্যান করা হয়।

ডিফল্টভাবে একবার পুনঃচেষ্টা করার অনুমতি থাকে। শুধুমাত্র সংযোগ ত্রুটি, টাইমআউট এবং
HTTP 408/429/500/502/503/504 রেসপন্সগুলোর ক্ষেত্রে পুনঃচেষ্টা করা হয়। ব্যাকঅফ 0.5 সেকেন্ড
থেকে শুরু হয় এবং পরবর্তী পুনঃচেষ্টাগুলোতে দ্বিগুণ হয়; `Retry-After` সেকেন্ড এবং HTTP তারিখ
অগ্রাধিকার পায়। সব প্রচেষ্টা, রেসপন্স পড়া, JSON ডিকোডিং এবং পুনঃচেষ্টার অপেক্ষা
`--timeout` বাজেটের অংশ ব্যবহার করে। যে পুনঃচেষ্টার অপেক্ষা বাজেটে কুলায় না তা সঙ্গে সঙ্গে `UNKNOWN` ফেরত দেয়
এবং টাইমআউট নয়, বরং যে ত্রুটিটির কারণে এটি ঘটেছে (যেমন `HTTP 429` বা `ConnectionError`)
তা রিপোর্ট করে। অথেনটিকেশন ব্যর্থতা, অন্যান্য স্থায়ী HTTP ত্রুটি, অবৈধ JSON এবং 64 KiB-এর বেশি
ডিকোড করা ডেটাসম্পন্ন রেসপন্সগুলোর ক্ষেত্রে পুনঃচেষ্টা করা হয় না। পুনঃচেষ্টা নিষ্ক্রিয় করতে
`--retries 0` ব্যবহার করুন।

### ফলব্যাক কোট উৎস

CoinGecko-সামঞ্জস্যপূর্ণ এন্ডপয়েন্টগুলোর সাথে পুনরাবৃত্তিযোগ্য `--fallback-url URL` অপশন ব্যবহার করুন।
উদাহরণস্বরূপ, `--fallback-url https://quotes.example.org/simple/price` যোগ করুন।
প্রতিটি উৎস তার পুনঃচেষ্টাসহ অবশিষ্ট অনুরোধের সময়সীমার একটি সমান অংশ পায়।
কোনো সাময়িক ব্যর্থতা বা সেই অংশের চেয়ে দীর্ঘ পুনঃচেষ্টার বিলম্ব হলে পরবর্তী উৎসে এগিয়ে যায়।
TLS যাচাইকরণ ব্যর্থতা, স্থায়ী HTTP ত্রুটি এবং অবৈধ কোট `UNKNOWN` ফেরত দেয়। প্রতিটি কোট রেসপন্স
সর্বোচ্চ 64 KiB ডিকোড করা ডেটার মধ্যে সীমাবদ্ধ। ফলব্যাক কনফিগার করা থাকলে, স্ট্যাটাসটি URL
প্রিন্ট না করেই উত্তরদাতা উৎসকে `primary`, `fallback1` ইত্যাদি হিসেবে চিহ্নিত করে।

### স্বল্প-মেয়াদী পরিবর্তন

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

মনিটরিং ব্যবহারকারীকে একটি স্থানীয় Linux বা macOS ফাইলসিস্টেমে ব্যক্তিগত লেখার যোগ্য স্টেট ডিরেক্টরি দিন।
চেকগুলোর মাঝখানে পাশের `.lock` ফাইলটি জায়গায় রেখে দিন। প্রতিটি উইন্ডোর জন্য আলাদা স্টেট
ফাইল ব্যবহার করুন। এর ভেতরে মুদ্রাগুলোর স্বতন্ত্র ইতিহাস থাকে। ডিফল্ট উইন্ডো 3600 সেকেন্ড।
প্রতিটি বৈধ কোটের জন্য উইন্ডো এবং বয়স সীমার মধ্যে একটি ভেন্ডর টাইমস্ট্যাম্প থাকা প্রয়োজন,
যা `--max-age` অন্য কোনো মান নির্ধারণ না করলে এক ঘণ্টা থাকে। প্লাগইনটি বর্তমান মূল্যের সাথে
সেই উইন্ডোর সবচেয়ে পুরোনো পূর্ববর্তী ধনাত্মক মূল্যের তুলনা করে এবং প্রকৃত অতিবাহিত সেকেন্ড
রিপোর্ট করে। পুনরাবৃত্ত টাইমস্ট্যাম্প অতিরিক্ত নমুনা তৈরি করে না। প্রথম নমুনা, মেয়াদোত্তীর্ণ ইতিহাস
বা ক্ষতিগ্রস্ত JSON একটি নতুন বেসলাইন শুরু করে; তুলনাযোগ্য নমুনা না থাকা পর্যন্ত উইন্ডো মেট্রিক
অজানা থাকে। অন্যান্য সতর্কতা তখনও প্রযোজ্য থাকে। লেখার অযোগ্য স্টেট, সিম্বলিক-লিঙ্ক স্টেট বা
লক ফাইল, অথবা সর্বশেষ রেকর্ড করা নমুনার চেয়ে পুরোনো কোট `UNKNOWN` ফেরত দেয়। চিহ্নযুক্ত
`bitcoin_move_window` মেট্রিকটি প্রতিসম warning এবং critical রেঞ্জ ব্যবহার করে। সীমার সমান
মানে সতর্কতা জারি হয় না।

প্লাগইনটি প্রতি চেকে একবার স্টেট ডিরেক্টরি খোলে এবং এর সাপেক্ষে কাজ করে, তাই চেক চলাকালীন
প্রতিস্থাপিত কোনো পাথ অংশ লক, পড়া বা লেখাকে পুনঃনির্দেশ করতে পারে না। চেক শুরু হওয়ার সময়
পাথের ডিরেক্টরি অংশের সিম্বলিক লিঙ্কগুলো অনুসরণ করা হয়, যা macOS-এ `/var`-এর মতো প্ল্যাটফর্ম
লিঙ্কগুলো ব্যবহারযোগ্য রাখে। তাই স্টেট ডিরেক্টরি এবং এর পূর্ববর্তী ডিরেক্টরিগুলো অন্য ব্যবহারকারীদের
দ্বারা লেখার যোগ্য হওয়া উচিত নয়। স্টেট এবং লক ফাইলগুলো 0600 মোডে তৈরি করা হয়।

### দৈনিক শতাংশ পরিবর্তন

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

পরিবর্তনের থ্রেশহোল্ডগুলো নির্বাচিত মুদ্রায় CoinGecko-এর চিহ্নযুক্ত 24-ঘণ্টার শতাংশ পরিবর্তনের
পরম মান পরিমাপ করে। ঠিক থ্রেশহোল্ডের সমান পরিবর্তনে সতর্কতা জারি হয় না। উভয় থ্রেশহোল্ড
সরবরাহ করা হলে, warning অবশ্যই critical-কে অতিক্রম করবে না। প্রয়োজনীয় পরিবর্তনের ডেটা অনুপস্থিত বা
অবৈধ হলে `UNKNOWN` ফেরত আসে। মূল্য এবং পরিবর্তনের সতর্কতা একত্রিত করা যায়; সর্বোচ্চ তীব্রতা
প্রাধান্য পায়, এবং তীব্রতা সমান হলে মূল্য অগ্রাধিকার পায়।

## কমান্ড লাইন অপশন

| অপশন | বিবরণ |
|--------|-------------|
| `-w`, `--warning` | warning থ্রেশহোল্ড রেঞ্জ (ফরম্যাট: LOW:HIGH) |
| `-c`, `--critical` | critical থ্রেশহোল্ড রেঞ্জ (ফরম্যাট: LOW:HIGH) |
| `--warning-low` | নিম্ন মূল্যের জন্য warning থ্রেশহোল্ড |
| `--warning-high` | উচ্চ মূল্যের জন্য warning থ্রেশহোল্ড |
| `--critical-low` | নিম্ন মূল্যের জন্য critical থ্রেশহোল্ড |
| `--critical-high` | উচ্চ মূল্যের জন্য critical থ্রেশহোল্ড |
| `--currency` | 2-16 অক্ষর বা অঙ্কের মুদ্রা কোড (ডিফল্ট: usd) |
| `--timeout` | ভগ্নাংশ মানসহ সেকেন্ডে মোট API অনুরোধ/পুনঃচেষ্টার বাজেট (ডিফল্ট: 10) |
| `--retries` | অতিরিক্ত সাময়িক প্রচেষ্টা, 0–5 (ডিফল্ট: 1) |
| `--max-age` | সেকেন্ডে সর্বোচ্চ ভেন্ডর কোটের বয়স এবং টাইমস্ট্যাম্প আবশ্যক করে; টাইমস্ট্যাম্পযুক্ত কোটের ডিফল্ট 3600 |
| `--warning-change` | 24 ঘণ্টার পরম শতাংশ পরিবর্তনের জন্য warning সীমা |
| `--critical-change` | 24 ঘণ্টার পরম শতাংশ পরিবর্তনের জন্য critical সীমা |
| `--api-url` | প্রাথমিক API URL |
| `--fallback-url` | অতিরিক্ত সামঞ্জস্যপূর্ণ এন্ডপয়েন্ট; পছন্দের ক্রমে পুনরাবৃত্তি করুন |
| `--state-file` | JSON পরিবর্তনের ইতিহাস ফাইল |
| `--move-window` | সেকেন্ডে পরিবর্তনের উইন্ডো (ডিফল্ট: 3600) |
| `--warning-move`, `--critical-move` | শতাংশে পরম উইন্ডো পরিবর্তনের থ্রেশহোল্ড |
| `-v`, `--verbose` | বিস্তারিত আউটপুট সক্রিয় করুন |
| `-V`, `--version` | সংস্করণ দেখান |
| `-h`, `--help` | সহায়তা বার্তা দেখান |

## Nagios কনফিগারেশন

### কমান্ড সংজ্ঞা

Nagios রিসোর্স ম্যাক্রো `$USER1$`-কে প্লাগইন ডিরেক্টরিতে সেট করুন (নেটিভ প্যাকেজগুলো `/usr/lib/nagios/plugins` ব্যবহার করে)। আপনার Nagios কমান্ড কনফিগারেশনে যোগ করুন:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### সার্ভিস সংজ্ঞা

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

### Icinga2 কনফিগারেশন

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

## এক্সিট কোড

অবৈধ আর্গুমেন্ট, অ-ধনাত্মক টাইমআউট, অবৈধ থ্রেশহোল্ড রেঞ্জ এবং বিকৃত API মূল্য
`UNKNOWN` (এক্সিট 3) ফেরত দেয়। থ্রেশহোল্ডগুলো অবশ্যই সসীম, অ-ঋণাত্মক সংখ্যা হতে হবে,
যেখানে প্রতিটি নিম্ন সীমা তার উচ্চ সীমার চেয়ে বড় হবে না। মুদ্রাটি অবশ্যই 2-16 অক্ষর বা
অঙ্কের হতে হবে। API-এর সাথে যোগাযোগ করার আগেই অবৈধ কনফিগারেশন প্রত্যাখ্যান করা হয়।
মূল্য অবশ্যই সসীম এবং অ-ঋণাত্মক হতে হবে, যা JSON সংখ্যা অথবা `"43521.5"`-এর মতো সাধারণ
দশমিক স্ট্রিং হিসেবে দেওয়া থাকবে। অনুরোধকৃত মুদ্রা ছাড়া কোনো রেসপন্স সেটির নাম উল্লেখ করে,
যেমন `Response has no EUR price`। অবৈধ রেসপন্স পারফরম্যান্স ডেটা নির্গত করে না।
বিস্তারিত ডায়াগনস্টিকস stderr-এ যায় যাতে stdout-এ একটি মাত্র মনিটরিং স্ট্যাটাস লাইন থাকে।

| কোড | স্ট্যাটাস | বিবরণ |
|------|--------|-------------|
| 0 | OK | মূল্য গ্রহণযোগ্য সীমার মধ্যে রয়েছে |
| 1 | WARNING | মূল্য warning থ্রেশহোল্ড অতিক্রম করেছে |
| 2 | CRITICAL | মূল্য critical থ্রেশহোল্ড অতিক্রম করেছে |
| 3 | UNKNOWN | ত্রুটি ঘটেছে (API ব্যর্থতা, টাইমআউট ইত্যাদি) |

## পারফরম্যান্স ডেটা

প্লাগইনটি স্ট্যান্ডার্ড Nagios ফরম্যাটে পারফরম্যান্স ডেটা আউটপুট দেয়:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

মূল্যের পারফরম্যান্স ডেটায় কনফিগার করা warning/critical রেঞ্জ এবং শূন্যের একটি সর্বনিম্ন মান
অন্তর্ভুক্ত থাকে। থ্রেশহোল্ডগুলো সম্পূর্ণ দশমিক নোটেশনে প্রিন্ট করা হয়, কখনোই রাউন্ড বা
এক্সপোনেন্ট আকারে নয়, যাতে `14500000:16250000`-এর মতো বড় মানগুলো পার্সযোগ্য থাকে।
অনুরোধের সময়ে সব প্রচেষ্টা এবং ব্যাকঅফ অন্তর্ভুক্ত থাকে। ভেন্ডর বৈধ টাইমস্ট্যাম্প সরবরাহ
করলেই কেবল কোটের বয়স নির্গত হয়; উপলব্ধ থাকলে দৈনিক পরিবর্তন নির্গত হয়। পরিবর্তনের রেঞ্জ
শূন্যের চারপাশে প্রতিসম। অবৈধ বা পুরোনো ডেটা মূল্যের পারফরম্যান্স ডেটা ছাড়াই `UNKNOWN` তৈরি করে।
এই মেট্রিকগুলো PNP4Nagios, Grafana বা InfluxDB-এর মতো গ্রাফিং টুলের সাথে ব্যবহার করা যায়।

## API

এই প্লাগইনটি ডিফল্টভাবে [CoinGecko API](https://www.coingecko.com/en/api) ব্যবহার করে, যা বিনামূল্যের এবং এর জন্য কোনো API কী প্রয়োজন হয় না। রেট লিমিট প্রযোজ্য।

কাস্টম এন্ডপয়েন্টগুলোতে অবশ্যই একই রেসপন্স কাঠামো ব্যবহার করতে হবে: মূল্যের জন্য `bitcoin.<currency>`,
UNIX টাইমস্ট্যাম্প সেকেন্ডের জন্য `bitcoin.last_updated_at` এবং চিহ্নযুক্ত দৈনিক শতাংশ পরিবর্তনের জন্য
`bitcoin.<currency>_24h_change`। `--max-age` এবং পরিবর্তনের থ্রেশহোল্ড অনুপস্থিত থাকলে শুধুমাত্র
মূল্য প্রয়োজন হয়। কোনো টাইমস্ট্যাম্প উপস্থিত থাকলে তা তবুও পরীক্ষা করা হয়: এটি ভবিষ্যতের বা এক ঘণ্টার
বেশি পুরোনো হওয়া যাবে না। ডিকোড করা রেসপন্স অবশ্যই 64 KiB-এর মধ্যে থাকতে হবে।

সমর্থিত মুদ্রার মধ্যে রয়েছে: usd, eur, gbp, jpy, aud, cad, chf, cny এবং আরও অনেক কিছু।

## নিরাপত্তা

নিচের ব্যবস্থাগুলো বর্তমান কোডে বাস্তবায়িত আছে। এগুলো একটি অসদাচরণকারী এন্ডপয়েন্ট বা স্থানীয় ব্যবহারকারী
মনিটরিং হোস্টের ওপর কী করতে পারে তা সীমাবদ্ধ করে; এগুলো কোটটিকে নিজেই বিশ্বাসযোগ্য করে তোলে না।

- `requests`-এর ডিফল্ট দিয়ে HTTPS সার্টিফিকেট যাচাই করা হয় এবং কোনো অপশন যাচাইকরণ নিষ্ক্রিয় করে না।
  সাধারণ `http://` ব্যবহারকারী কাস্টম `--api-url`-এ এমন কোনো সুরক্ষা থাকে না।
- DNS, সংযোগ, পড়া, পুনঃচেষ্টা এবং ব্যাকঅফ `--timeout` সময়সীমা ভাগ করে নেয়। ধীরে ডেটা পাঠানো
  কোনো পিয়ার এটিকে বাড়াতে পারে না।
- ডিকমপ্রেশনের পর প্রতিটি রেসপন্স 64 KiB-এ সীমাবদ্ধ থাকে এবং রিডাইরেক্ট বডি না পড়েই বাতিল করা হয়।
- অনুরোধ ব্যর্থ হলে শুধুমাত্র একটি HTTP স্ট্যাটাস বা একটি ত্রুটি ক্লাস প্রিন্ট করা হয়, কারণ কাস্টম
  `--api-url`-এ ক্রেডেনশিয়াল থাকতে পারে।
- `.deb` এবং `.rpm` দ্বারা ইনস্টল করা কমান্ডটি Python-কে isolated মোডে চালায়। এটি `PYTHONPATH`,
  ব্যবহারকারীর সাইট ডিরেক্টরি এবং ওয়ার্কিং ডিরেক্টরির মডিউলগুলো উপেক্ষা করে। একটি `pip` ইনস্টলেশন
  স্ট্যান্ডার্ড কনসোল স্ক্রিপ্ট ব্যবহার করে এবং যে পরিবেশে এটি ইনস্টল করা হয় তা অনুসরণ করে।
- পরিবর্তনের স্টেট প্রতি চেকে একবার খোলা একটি ডিরেক্টরির সাপেক্ষে, স্টেট বা লক ফাইলের নামে থাকা
  কোনো সিম্বলিক লিঙ্ক অনুসরণ না করেই পড়া এবং লেখা হয়।
- রিলিজ অ্যাসেটগুলোতে `SHA256SUMS` ছাড়াও বিল্ড প্রোভেন্যান্স অ্যাটেস্টেশন থাকে; দেখুন [GitHub Releases থেকে](#from-github-releases)।

## 1.0.0 থেকে আপগ্রেড করা

এই পরিবর্তনগুলো 2.0.0-এ যুক্ত হয়েছে।

- বৃহত্তর `--max-age` দেওয়া না হলে এক ঘণ্টার বেশি পুরোনো ভেন্ডর টাইমস্ট্যাম্পসহ কোট `UNKNOWN` ফেরত দেয়।
  যে এন্ডপয়েন্টগুলো কোনো টাইমস্ট্যাম্প ফেরত দেয় না সেগুলো প্রভাবিত হয় না।
- `--currency` শুধুমাত্র 2-16 অক্ষর বা অঙ্ক গ্রহণ করে।
- অঙ্ক বিভাজক বা চারপাশে স্পেস থাকা সংখ্যাগত স্ট্রিংগুলো প্রত্যাখ্যান করা হয়।
- বাজেটে না কুলানো পুনঃচেষ্টার অপেক্ষা `API request timed out`-এর পরিবর্তে মূল ব্যর্থতাটি রিপোর্ট করে।
- নেটিভ প্যাকেজগুলো আর `PYTHONPATH` অনুসরণ করে না।
- এক মিলিয়ন বা তার বেশি থ্রেশহোল্ডগুলো পারফরম্যান্স ডেটায় এক্সপোনেন্ট নোটেশনের পরিবর্তে সাধারণ
  দশমিক হিসেবে প্রদর্শিত হয়।

## স্থানীয়করণ

CLI সহায়তা, যাচাইকরণ ত্রুটি এবং প্লাগইন স্ট্যাটাস বিবরণ বান্ডেল করা stdlib-লোডেড ক্যাটালগ ব্যবহার করে 45টি লোকেল (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) সমর্থন করে। রেজোলিউশন প্রথমে `--lang`, তারপর `LC_ALL`, `LC_MESSAGES` এবং `LANG` পরীক্ষা করে এবং না পেলে `en`-এ ফিরে যায়। Nagios স্ট্যাটাস প্রিফিক্স (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) এবং পারফরম্যান্স ডেটা সব লোকেলে অপরিবর্তিত থাকে।

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## ডেভেলপমেন্ট

[mise](https://mise.jdx.dev/getting-started.html) ইনস্টল করুন, তারপর ওপরের ডেভেলপমেন্ট সেটআপটি চালান। `mise.toml` ফাইলটি Python এবং uv পিন করে। ডেভেলপমেন্ট টুলগুলো `pyproject.toml`-এ ঘোষিত এবং কমিট করা `uv.lock`-এ সমাধান করা হয়।

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

সেটআপের পর কমিট হুকগুলো ইনস্টল করুন:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

ডিপেন্ডেন্সি আপডেট করতে `mise exec -- uv add --dev <tool>` অথবা `mise exec -- uv add <dependency>` ব্যবহার করুন এবং `pyproject.toml` ও `uv.lock` উভয়ই কমিট করুন।

CI Linux-এ Python 3.12 ও 3.13 এবং macOS-এ Python 3.13 পরীক্ষা করে। প্রতিটি PR-এ প্যাকেজ যাচাইকরণ, ডিপেন্ডেন্সি অডিটিং এবং CodeQL চালানো হয় এবং Ubuntu-তে `.deb` ও Fedora-তে `.rpm` ইনস্টল করা হয়। বিল্ট ডিস্ট্রিবিউশনগুলো CI রানে `distributions` আর্টিফ্যাক্ট হিসেবে পাওয়া যায়।

প্যাকেজ এবং CLI সংস্করণ `check_bitcoin_price/__init__.py` থেকে আসে। সংস্করণ বৃদ্ধি এবং GitHub রিলিজ অ্যাসেটের স্বয়ংক্রিয় প্রকাশনার জন্য [রিলিজ প্রক্রিয়া](../../../CONTRIBUTING.md#releases) দেখুন।

## অবদান রাখা

ডেভেলপমেন্ট ওয়ার্কফ্লো এবং স্বাক্ষরিত কমিট সংক্রান্ত প্রয়োজনীয়তার জন্য [CONTRIBUTING.md](../../../CONTRIBUTING.md) দেখুন।

## লাইসেন্স

এই প্রকল্পটি MIT License-এর অধীনে লাইসেন্সকৃত - বিস্তারিত জানার জন্য [LICENSE](../../../LICENSE) ফাইলটি দেখুন।

## লেখক

Thomas Vincent

## কৃতজ্ঞতা স্বীকার

- বিনামূল্যে ক্রিপ্টোকারেন্সি API সরবরাহ করার জন্য [CoinGecko](https://www.coingecko.com/)
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
