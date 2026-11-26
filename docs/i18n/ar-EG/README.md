# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · **العربية (مصر)** · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

إضافة (بلجن) لـ Nagios/Icinga لمراقبة سعر Bitcoin مع حدود تحذير (warning) وحدود حرجة (critical) تقدر تظبطها زي ما تحب.

## المميزات

- مراقبة سعر Bitcoin بأكتر من عملة (USD وEUR وGBP وغيرهم)
- حدود تحذير وحدود حرجة قابلة للتعديل (للحد الأعلى والأدنى)
- مخرجات قياسية لبلجن Nagios مع بيانات الأداء (performance data)
- بيستخدم CoinGecko API (مجاني ومش محتاج مفتاح API)
- دعم لنقاط نهاية (API endpoints) مخصصة
- مهلة انتظار (timeout) قابلة للتعديل
- فحص حداثة السعر باستخدام الطوابع الزمنية من المصدر (vendor timestamps)، بحد افتراضي ساعة واحدة
- إعادة محاولة محدودة لمشاكل حد الطلبات (rate limits) والأعطال المؤقتة في الـ API
- مهلة نهائية واحدة لكل المحاولات، وحد أقصى 64 KiB لكل استجابة
- تنبيهات اختيارية لو حصل تغيّر بنسبة مئوية مطلقة خلال 24 ساعة
- إظهار حدود السعر ومدة الطلب وعمر السعر في بيانات الأداء

## التثبيت

### من GitHub Releases

نزّل ملفات `.deb` و`.rpm` و`.tar.gz` وwheel و`SHA256SUMS` من [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). واتأكد من سلامة التنزيل باستخدام `sha256sum --ignore-missing --check SHA256SUMS`. كمان الإصدارات اللي بعد 1.0.0 معاها إثبات بناء موقّع (signed build provenance)؛ تقدر تتأكد إن الملف طالع من workflow الإصدار بتاع الريبو ده عن طريق `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

استخدم أسماء الملفات بتاعة الإصدار اللي اخترته. الحزم الأصلية بتثبّت `/usr/bin/check_bitcoin_price` و`/usr/lib/nagios/plugins/check_bitcoin_price`؛ وحزمة الـ RPM بتوفر كمان `/usr/lib64/nagios/plugins/check_bitcoin_price`. الأمر اللي متثبّت من الحزمة بيشغّل Python في الوضع المعزول (isolated mode)، يعني بيتجاهل `PYTHONPATH` وأي موديولات في الفولدر الحالي؛ ومدير حزم النظام هو اللي بيثبّت Python واعتمادية `requests`. الحزم دي فيها كود Python مستقل عن المعمارية ومحتاجة توزيعة بتوفر Python 3.12 أو أحدث.

### من الكود المصدري

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### للتطوير

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## الاستخدام

### الاستخدام الأساسي

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### مع حدود التنبيه

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### حدود فردية

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### عملة مختلفة

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### مهلة انتظار مخصصة

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### حداثة السعر وميزانية إعادة المحاولة

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

أي سعر جاي معاه طابع زمني من المصدر لازم ما يكونش أقدم من ساعة واحدة بشكل افتراضي.
نقاط النهاية اللي بترجّع السعر بس بتفضل شغالة عادي لو مش مستخدم `--max-age`.
أما لو استخدمت `--max-age`، فأي طابع زمني ناقص أو غير صالح أو في المستقبل أو قديم بيرجّع `UNKNOWN`؛ الإضافة مش بتحط وقت الجلب المحلي مكان وقت السعر اللي جاي من المصدر. الطابع الزمني اللي واصل لحد العمر بالظبط بيعتبر مقبول. والطوابع الزمنية اللي في المستقبل مرفوضة دايماً.

الإعداد الافتراضي بيسمح بمحاولة إعادة واحدة. إعادة المحاولة بتحصل بس مع أخطاء الاتصال، انتهاء المهلة (timeouts)، واستجابات HTTP اللي هي 408/429/500/502/503/504. وقت الانتظار بين المحاولات (backoff) بيبدأ من 0.5 ثانية وبيتضاعف مع كل محاولة بعدها؛ وبيبقى للأولوية قيمة `Retry-After` بالثواني أو تواريخ HTTP لو موجودة. كل المحاولات وقراءة الاستجابة وفك تشفير JSON وفترات الانتظار بيتشاركوا في نفس ميزانية `--timeout`. لو وقت الانتظار بتاع إعادة المحاولة مش هيكفّي المهلة المتبقية، الإضافة بترجّع `UNKNOWN` فوراً وبتبلّغ بالخطأ اللي سببها، زي `HTTP 429` أو `ConnectionError`، مش بتقول إنه timeout. أخطاء المصادقة، وأخطاء HTTP الدائمة التانية، وبيانات JSON غير الصالحة، والاستجابات الأكبر من 64 KiB بعد فك التشفير ما بيتعملش ليها إعادة محاولة. استخدم `--retries 0` عشان توقف إعادة المحاولة.

### مصادر أسعار بديلة (Fallback)

استخدم خيارات `--fallback-url URL` القابلة للتكرار مع نقاط نهاية متوافقة مع CoinGecko.
مثلاً، ضيف `--fallback-url https://quotes.example.org/simple/price`.
كل مصدر بياخد نصيب متساوي من الوقت المتبقي من مهلة الطلب، شاملة محاولات الإعادة بتاعته. لو حصل عطل مؤقت أو تأخير إعادة محاولة أطول من النصيب ده، الإضافة بتتنقل للمصدر اللي بعده. أما فشل التحقق من شهادات TLS، وأخطاء HTTP الدائمة، والأسعار غير الصالحة فبترجّع UNKNOWN. كل استجابة سعر ليها حد أقصى 64 KiB من البيانات بعد فك التشفير.
لما تكون مضبّط مصادر بديلة، رسالة الحالة بتحدد المصدر اللي رد باسم `primary` أو `fallback1` وهكذا، من غير ما تطبع رابط الـ URL بتاعه.

### التحرك خلال فترة قصيرة

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

ادي لمستخدم المراقبة فولدر حالة (state directory) خاص وقابل للكتابة على نظام ملفات محلي في Linux أو macOS. سيب ملف `.lock` اللي جنبه في مكانه بين الفحوصات. واستخدم ملف حالة منفصل لكل فترة زمنية (window). كل عملة بيبقى ليها سجل مستقل جواه.
الفترة الافتراضية هي 3600 ثانية. كل سعر صالح لازم يكون معاه طابع زمني من المصدر جوا الفترة دي وجوا حد العمر، واللي هو ساعة واحدة إلا لو `--max-age` محدد قيمة تانية. الإضافة بتقارن السعر الحالي بأقدم سعر موجب سابق جوا الفترة دي وبتعرض عدد الثواني الفعلي اللي عدّى. الطوابع الزمنية المتكررة مش بتعمل عينات زيادة.
أول عينة، أو سجل منتهي الصلاحية، أو ملف JSON تالف بيبدأوا نقطة أساس (baseline) جديدة؛ ومقياس الفترة بيبقى غير معروف لحد ما يكون فيه عينة ينفع تتقارن. باقي التنبيهات بتفضل شغالة عادي. لو ملف الحالة مش قابل للكتابة، أو كان ملف الحالة أو القفل عبارة عن رابط رمزي (symbolic link)، أو جه سعر أقدم من أحدث عينة متسجلة، الإضافة بترجّع UNKNOWN. مقياس `bitcoin_move_window` اللي بإشارة بيستخدم نطاقات تحذير وحرجة متماثلة. والتساوي بالظبط عند الحد مش بيطلع تنبيه.

الإضافة بتفتح فولدر الحالة مرة واحدة في كل فحص وبتشتغل بشكل نسبي ليه، عشان لو جزء من المسار اتغيّر أثناء الفحص ما يقدرش يوجّه القفل أو القراءة أو الكتابة لمكان تاني. الروابط الرمزية في جزء الفولدر من المسار بيتم تتبعها وقت بداية الفحص، وده بيخلي روابط النظام زي `/var` على macOS تفضل شغالة. عشان كده فولدر الحالة والفولدرات اللي فوقه لازم ما يكونوش قابلين للكتابة من مستخدمين تانيين. ملفات الحالة والقفل بتتعمل بصلاحيات 0600.

### نسبة التحرك اليومية

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

حدود التغيّر بتقيس القيمة المطلقة لنسبة التغيّر اليومية (24 ساعة) اللي جاية بإشارة من CoinGecko بالعملة المختارة. التغيّر اللي واقف بالظبط عند الحد مش بيطلع تنبيه. لو حطيت الحدين، لازم حد التحذير ما يكونش أكبر من الحد الحرج.
لو بيانات التغيّر المطلوبة ناقصة أو غير صالحة، الإضافة بترجّع `UNKNOWN`. تقدر تدمج تنبيهات السعر مع تنبيهات التغيّر؛ وأعلى درجة خطورة هي اللي بتكسب، ولو درجات الخطورة متساوية فتنبيه السعر ليه الأولوية.

## خيارات سطر الأوامر

| الخيار | الوصف |
|--------|-------------|
| `-w`, `--warning` | نطاق حد التحذير (الصيغة: LOW:HIGH) |
| `-c`, `--critical` | نطاق حد الحرج (الصيغة: LOW:HIGH) |
| `--warning-low` | حد التحذير للسعر المنخفض |
| `--warning-high` | حد التحذير للسعر المرتفع |
| `--critical-low` | الحد الحرج للسعر المنخفض |
| `--critical-high` | الحد الحرج للسعر المرتفع |
| `--currency` | كود العملة من 2 إلى 16 حرف أو رقم (الافتراضي: usd) |
| `--timeout` | إجمالي ميزانية طلب الـ API وإعادة المحاولة بالثواني، شاملة الكسور (الافتراضي: 10) |
| `--retries` | محاولات إضافية للأعطال المؤقتة، من 0 إلى 5 (الافتراضي: 1) |
| `--max-age` | أقصى عمر لسعر المصدر بالثواني مع اشتراط وجود طابع زمني؛ الأسعار اللي بطابع زمني بتاخد 3600 بشكل افتراضي |
| `--warning-change` | حد التحذير لنسبة التحرك المطلقة خلال 24 ساعة |
| `--critical-change` | الحد الحرج لنسبة التحرك المطلقة خلال 24 ساعة |
| `--api-url` | رابط الـ API الأساسي |
| `--fallback-url` | نقطة نهاية إضافية متوافقة؛ كرّرها بالترتيب اللي تفضله |
| `--state-file` | ملف JSON لسجل التحركات |
| `--move-window` | مدة فترة التحرك بالثواني (الافتراضي: 3600) |
| `--warning-move`, `--critical-move` | حدود التحرك المطلقة خلال الفترة بالنسبة المئوية |
| `-v`, `--verbose` | تفعيل المخرجات التفصيلية |
| `-V`, `--version` | عرض رقم الإصدار |
| `-h`, `--help` | عرض رسالة المساعدة |

## إعدادات Nagios

### تعريف الأمر (Command Definition)

اظبط ماكرو الموارد في Nagios اللي هو `$USER1$` على فولدر الإضافات (الحزم الأصلية بتستخدم `/usr/lib/nagios/plugins`). وضيف التالي لملف إعدادات أوامر Nagios عندك:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### تعريف الخدمة (Service Definition)

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

### إعدادات Icinga2

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

## أكواد الخروج (Exit Codes)

المعاملات غير الصالحة، ومهل الانتظار غير الموجبة، ونطاقات الحدود غير الصالحة، وأسعار الـ API اللي صيغتها غلط كلها بترجّع `UNKNOWN` (كود خروج 3). لازم الحدود تكون أرقام محدودة وغير سالبة، وكل حد أدنى ما يكونش أكبر من الحد الأعلى بتاعه. ولازم العملة تكون من 2 إلى 16 حرف أو رقم. الإعدادات الغلط بتترفض قبل ما الإضافة تكلم الـ API أصلاً. الأسعار لازم تكون أرقام محدودة وغير سالبة، سواء كأرقام JSON أو نصوص عشرية عادية زي `"43521.5"`. لو الاستجابة ما فيهاش العملة المطلوبة، الرسالة بتذكر اسمها، مثلاً `Response has no EUR price`. الاستجابات غير الصالحة مش بتطلع بيانات أداء. وتفاصيل التشخيص (verbose diagnostics) بتروح لـ stderr عشان stdout يفضل فيه سطر حالة مراقبة واحد بس.

| الكود | الحالة | الوصف |
|------|--------|-------------|
| 0 | OK | السعر في النطاق المقبول |
| 1 | WARNING | السعر عدّى حد التحذير |
| 2 | CRITICAL | السعر عدّى الحد الحرج |
| 3 | UNKNOWN | حصل خطأ (فشل في الـ API، انتهاء المهلة، إلخ) |

## بيانات الأداء (Performance Data)

الإضافة بتطلع بيانات الأداء بصيغة Nagios القياسية:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

بيانات أداء السعر بتشمل نطاقات التحذير والحرج اللي أنت ظبطها وحد أدنى صفر. الحدود بتتطبع بالصيغة العشرية الكاملة، من غير تقريب ومن غير صيغة أسّية (exponent form)، عشان القيم الكبيرة زي `14500000:16250000` تفضل سهلة التحليل. وقت الطلب بيشمل كل المحاولات وأوقات الانتظار بينها. عمر السعر بيطلع بس لما المصدر يبعت طابع زمني صالح؛ والتغيّر اليومي بيطلع لما يكون متاح. نطاقات التغيّر متماثلة حوالين الصفر. البيانات غير الصالحة أو القديمة بترجّع `UNKNOWN` من غير بيانات أداء للسعر. وتقدر تستخدم المقاييس دي مع أدوات رسم بياني زي PNP4Nagios أو Grafana أو InfluxDB.

## الـ API

الإضافة دي بتستخدم [CoinGecko API](https://www.coingecko.com/en/api) بشكل افتراضي، وهو مجاني ومش محتاج مفتاح API. بس فيه حدود لعدد الطلبات (rate limits).

نقاط النهاية المخصصة لازم تستخدم نفس شكل الاستجابة: `bitcoin.<currency>` للسعر، و`bitcoin.last_updated_at` للطابع الزمني بصيغة UNIX بالثواني، و`bitcoin.<currency>_24h_change` لنسبة التحرك اليومية بإشارتها. السعر بس هو اللي مطلوب لما يكون `--max-age` وحدود التغيّر مش مستخدمة. ولو فيه طابع زمني موجود بيتم فحصه برضه: لازم ما يكونش في المستقبل ولا أقدم من ساعة واحدة. ولازم حجم الاستجابة بعد فك التشفير ما يعديش 64 KiB.

العملات المدعومة بتشمل: usd وeur وgbp وjpy وaud وcad وchf وcny وغيرهم كتير.

## الأمان

الإجراءات اللي تحت دي متنفذة في الكود الحالي. هي بتحد من الضرر اللي ممكن تعمله نقطة نهاية مش مظبوطة أو مستخدم محلي على جهاز المراقبة؛ لكنها مش بتضمن إن السعر نفسه موثوق فيه.

- شهادات HTTPS بيتم التحقق منها بإعدادات `requests` الافتراضية، ومفيش أي خيار بيوقف التحقق. لو استخدمت `--api-url` مخصص بيبدأ بـ `http://` عادي مش هيبقى عنده الحماية دي.
- استعلامات DNS والاتصال والقراءة وإعادة المحاولة وأوقات الانتظار كلهم بيتشاركوا نفس المهلة بتاعة `--timeout`. يعني أي طرف بيبعت البيانات ببطء مش هيقدر يمط الوقت.
- كل استجابة ليها حد أقصى 64 KiB بعد فك الضغط، ومحتوى استجابات التحويل (redirect bodies) بيتم تجاهله من غير قراءة.
- أخطاء الطلبات بتطبع بس كود حالة HTTP أو نوع الخطأ، عشان رابط `--api-url` المخصص ممكن يكون فيه بيانات اعتماد (credentials).
- الأمر اللي بتثبّته حزم `.deb` و`.rpm` بيشغّل Python في الوضع المعزول. يعني بيتجاهل `PYTHONPATH`، وفولدر user site، وأي موديولات في الفولدر الحالي. أما التثبيت عن طريق `pip` فبيستخدم سكريبت الكونسول العادي وبيمشي على البيئة اللي متثبّت فيها.
- ملف حالة التحرك بيتقري ويتكتب من غير تتبع أي رابط رمزي عند اسم ملف الحالة أو القفل، وده بشكل نسبي لفولدر بيتفتح مرة واحدة لكل فحص.
- ملفات الإصدار بيكون معاها شهادات إثبات بناء (build provenance attestations) بالإضافة لـ `SHA256SUMS`؛ شوف قسم [من GitHub Releases](#from-github-releases).

## الترقية من 1.0.0

التغييرات دي نزلت في الإصدار 2.0.0.

- أي سعر جاي بطابع زمني من المصدر أقدم من ساعة بيرجّع `UNKNOWN` إلا لو حددت قيمة أكبر في `--max-age`. نقاط النهاية اللي مش بترجّع طابع زمني مش هتتأثر.
- خيار `--currency` بقى يقبل بس من 2 إلى 16 حرف أو رقم.
- النصوص الرقمية اللي فيها فواصل أرقام أو مسافات حواليها بقت تترفض.
- لو وقت انتظار إعادة المحاولة ما كفّاش الميزانية، الإضافة بتبلّغ بالخطأ الأصلي بدل رسالة `API request timed out`.
- الحزم الأصلية ما بقتش تعتمد على `PYTHONPATH`.
- الحدود اللي بتساوي مليون أو أكتر بتظهر في بيانات الأداء كأرقام عشرية عادية بدل الصيغة الأسّية.

## الترجمة والتوطين (Localization)

مساعدة سطر الأوامر، وأخطاء التحقق، ووصف حالة الإضافة بيدعموا 45 لغة ومنطقة (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) باستخدام كتالوجات مدمجة بتتحمل بمكتبة Python القياسية (stdlib). تحديد اللغة بيبص الأول على `--lang`، وبعدها `LC_ALL` و`LC_MESSAGES` و`LANG`، ولو مفيش حاجة منهم بيرجع لـ `en`. بادئات حالة Nagios (`OK` و`WARNING` و`CRITICAL` و`UNKNOWN`) وبيانات الأداء بتفضل ثابتة من غير تغيير في كل اللغات.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## التطوير

ثبّت [mise](https://mise.jdx.dev/getting-started.html)، وبعدين نفّذ خطوات إعداد التطوير اللي فوق. ملف `mise.toml` بيثبّت إصدارات Python وuv. أدوات التطوير متعرفة في `pyproject.toml` ومثبتة في ملف `uv.lock` الموجود في الريبو.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

ثبّت commit hooks بعد الإعداد:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

استخدم `mise exec -- uv add --dev <tool>` أو `mise exec -- uv add <dependency>` عشان تحدّث الاعتماديات واعمل commit لملفي `pyproject.toml` و`uv.lock` مع بعض.

الـ CI بيفحص Python 3.12 و3.13 على Linux وPython 3.13 على macOS. وكل PR كمان بيشغّل التحقق من الحزم، وتدقيق الاعتماديات، وCodeQL، وبيثبّت ملف `.deb` على Ubuntu وملف `.rpm` على Fedora. والحزم المبنية متاحة كـ artifact باسم `distributions` في تشغيلات الـ CI.

إصدار الحزمة وواجهة سطر الأوامر بيجي من `check_bitcoin_price/__init__.py`. شوف [عملية الإصدار](../../../CONTRIBUTING.md#releases) عشان تعرف إزاي ترفع الإصدار وتنشر ملفات GitHub release بشكل تلقائي.

## المساهمة

شوف [CONTRIBUTING.md](../../../CONTRIBUTING.md) عشان تعرف خطوات عمل التطوير ومتطلبات التوقيع على الـ commits (signed-off).

## الرخصة

المشروع ده مرخص تحت رخصة MIT - شوف ملف [LICENSE](../../../LICENSE) للتفاصيل.

## المؤلف

Thomas Vincent

## شكر وتقدير

- [CoinGecko](https://www.coingecko.com/) لتوفيرهم API مجاني للعملات الرقمية
- [إرشادات تطوير إضافات Nagios](https://nagios-plugins.org/doc/guidelines.html)
