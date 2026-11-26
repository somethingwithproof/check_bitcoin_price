# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · **العربية (المغرب)** · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

إضافة ديال Nagios/Icinga باش تراقب ثمن Bitcoin بعتبات ديال التحذير والخطر لي تقدر تضبطهم كيف بغيتي.

## المميزات

- مراقبة ثمن Bitcoin بعدة عملات (USD، EUR، GBP، إلخ.)
- عتبات ديال التحذير والخطر قابلة للتعديل (العالية والهابطة)
- مخرجات قياسية ديال إضافات Nagios مع بيانات الأداء
- كيستعمل CoinGecko API (فابور وبلا ما يحتاج مفتاح API)
- دعم نقاط نهاية API مخصصة
- مهلة انتظار (timeout) قابلة للتعديل
- التحقق من حداثة التسعيرة باستعمال الطوابع الزمنية ديال المزود، بحد افتراضي ديال ساعة وحدة
- إعادة محاولة محدودة فاش كيكون تقييد ديال الطلبات ولا أعطال مؤقتة فـ API
- مهلة وحدة لجميع المحاولات وسقف ديال 64 KiB لكل جواب
- تنبيهات اختيارية على نسبة التغيير المطلقة فـ 24 ساعة
- عتبات الثمن، مدة الطلب، وعمر التسعيرة فبيانات الأداء

## التثبيت

<a name="from-github-releases"></a>

### من GitHub Releases

تيليشارجي ملفات `.deb`، `.rpm`، `.tar.gz`، wheel، و `SHA256SUMS` من [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). تحقق من التحميل بـ `sha256sum --ignore-missing --check SHA256SUMS`. الإصدارات لي من بعد 1.0.0 فيهم حتى إثبات مصدر البناء موقّع؛ باش تتأكد بلي الملف جاي من مسار الإصدار ديال هاد المستودع، استعمل `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

استعمل أسماء الملفات ديال الإصدار لي ختاريتي. الحزم الأصلية كتنصّب `/usr/bin/check_bitcoin_price` و `/usr/lib/nagios/plugins/check_bitcoin_price`؛ وحزمة RPM كتعطي حتى `/usr/lib64/nagios/plugins/check_bitcoin_price`. الأمر المنصّب كيخدم Python فالوضع المعزول، يعني كيتجاهل `PYTHONPATH` والموديلات لي فمجلد الخدمة؛ ومدير حزم النظام كيتكلف بتبعيات Python و `requests`. هاد الحزم فيهم كود Python مستقل على المعمارية وخاصهم توزيعة فيها Python 3.12 ولا كتر.

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

## الاستعمال

### الاستعمال الأساسي

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### مع العتبات

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### عتبات فردية

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### عملة خرا

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### مهلة مخصصة

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### حداثة التسعيرة وميزانية إعادة المحاولة

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

أي تسعيرة فيها طابع زمني ديال المزود ما خاصهاش تفوت ساعة وحدة افتراضياً.
نقاط النهاية لي كترجع غير الثمن بوحدو كتبقى خدامة فاش كيكون `--max-age` ما كاينش.
ملي كيتستعمل `--max-age`، إيلا كان الطابع الزمني ديال المزود ناقص، ماشي صالح، فالمستقبل، ولا قديم، الإضافة كترجع `UNKNOWN`؛ الإضافة ما كتعوضش وقت التسعيرة ديال المزود بوقت الجلب المحلي.
الطابع الزمني لي جا نيشان فالحد الأقصى ديال العمر كيبقى مقبول. أما الطوابع الزمنية لي فالمستقبل فدائماً مرفوضين.

الإعداد الافتراضي كيسمح بمحاولة إعادة وحدة. غير أخطاء الاتصال، انتهاء المهلة، وأجوبة HTTP 408/429/500/502/503/504 هوما لي كيتعاودو. وقت الانتظار (backoff) كيبدا بـ 0.5 ثانية وكيتضاعف فالمحاولات لي من بعد؛ ثواني وتواريخ HTTP فـ `Retry-After` عندهم الأولوية. جميع المحاولات، قراءة الأجوبة، فك تشفير JSON، وأوقات الانتظار كيتقاسمو ميزانية `--timeout`. إيلا كان وقت الانتظار ما كيقدش فالميزانية، كترجع الإضافة `UNKNOWN` مباشرة وكتبلغ على العطل لي سببو، بحال `HTTP 429` ولا `ConnectionError`، ماشي انتهاء المهلة. فشل المصادقة، أخطاء HTTP الدائمة الخرى، JSON لي ماشي صالح، والأجوبة لي كبر من 64 KiB ديال البيانات المفكوكة ما كيتعاودوش. استعمل `--retries 0` باش تعطل إعادة المحاولة.

### مصادر تسعير احتياطية

استعمل خيارات `--fallback-url URL` لي تقدر تعاودهم مع نقاط نهاية متوافقة مع CoinGecko.
مثلاً، زيد `--fallback-url https://quotes.example.org/simple/price`.
كل مصدر كياخد حصة متساوية من الوقت لي بقى فمهلة الطلب، بما فيها محاولات الإعادة ديالو.
أي عطل مؤقت ولا تأخير إعادة أطول من ديك الحصة كيدوز مباشرة للمصدر لي من بعدو.
فشل التحقق من TLS، أخطاء HTTP الدائمة، والتسعيرات لي ماشي صالحة كيرجعو UNKNOWN.
كل جواب تسعيرة محدود فـ 64 KiB ديال البيانات المفكوكة.
ملي كيكونو المصادر الاحتياطية مضبوطين، الحالة كتحدد المصدر لي جاوب بـ `primary`، `fallback1`، وهكذا، بلا ما تطبع الرابط (URL) ديالو.

### الحركة على نافذة زمنية قصيرة

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

عطي لمستخدم المراقبة مجلد حالة خاص وقابل للكتابة على نظام ملفات محلي فـ Linux ولا macOS.
خلي ملف `.lock` لي حداه فبلاصتو بين عمليات الفحص. استعمل ملف حالة بوحدو لكل نافذة.
العملات عندهم تاريخ مستقل وسط الملف. النافذة الافتراضية هي 3600 ثانية.
كل تسعيرة صالحة خاص يكون عندها طابع زمني ديال المزود داخل النافذة وداخل حد العمر، لي هو ساعة وحدة إلا إيلا حدد `--max-age` مدة خرا.
الإضافة كتقارن الثمن الحالي مع أقدم ثمن موجب سبق فديك النافذة وكتعطي الثواني الحقيقية لي دازت.
الطوابع الزمنية المكررة ما كتزيدش عينات جداد.
العينة اللولة، التاريخ لي سالات صلاحيتو، ولا JSON المخسر كيبداو خط أساس جديد؛ ومقياس النافذة كيبقى غير معروف حتى تكون شي عينة صالحة للمقارنة.
التنبيهات الخرى كتبقى خدامة.
إيلا كانت الحالة غير قابلة للكتابة، ولا ملف الحالة أو القفل عبارة عن رابط رمزي (symbolic link)، ولا التسعيرة أقدم من أحدث عينة مسجلة، الإضافة كترجع UNKNOWN.
مقياس `bitcoin_move_window` الموقّع كيستعمل مجالات تحذير وخطر متماثلة. التساوي نيشان مع الحد ما كيطلقش تنبيه.

الإضافة كتحل مجلد الحالة مرة وحدة فكل فحص وكتخدم بالنسبة ليه، باش حتى إيلا تبدل شي جزء من المسار وسط الفحص ما يقدرش يحوّل القفل، القراءة، ولا الكتابة.
الروابط الرمزية فجزء المجلد ديال المسار كيتبعو فاش كيبدا الفحص، وهكا كيبقاو روابط النظام بحال `/var` فـ macOS خدامين.
داكشي علاش مجلد الحالة والمجلدات لي فوقو ما خاصهمش يكونو قابلين للكتابة من طرف مستخدمين آخرين.
ملفات الحالة والقفل كيتصاوبو بالصلاحية 0600.

### نسبة التغيير اليومي

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

عتبات التغيير كيقيسو القيمة المطلقة ديال نسبة التغيير فـ 24 ساعة الموقّعة ديال CoinGecko بالعملة لي ختاريتي.
التغيير لي جا نيشان فالعتبة ما كيطلقش تنبيه. إيلا عطيتي العتبات بجوج، عتبة التحذير ما خاصهاش تفوت عتبة الخطر.
إيلا كانت بيانات التغيير المطلوبة ناقصة ولا ماشي صالحة، الإضافة كترجع `UNKNOWN`.
تقدر تجمع تنبيهات الثمن والتغيير؛ الدرجة الأعلى هي لي كتغلب، والثمن عندو الأولوية فاش كيتساواو درجات الخطورة.

## خيارات سطر الأوامر

| الخيار | الوصف |
|--------|-------|
| `-w`, `--warning` | مجال عتبة التحذير (الصيغة: LOW:HIGH) |
| `-c`, `--critical` | مجال عتبة الخطر (الصيغة: LOW:HIGH) |
| `--warning-low` | عتبة التحذير للثمن الهابط |
| `--warning-high` | عتبة التحذير للثمن العالي |
| `--critical-low` | عتبة الخطر للثمن الهابط |
| `--critical-high` | عتبة الخطر للثمن العالي |
| `--currency` | رمز العملة من 2 حتى لـ 16 حرف ولا رقم (الافتراضي: usd) |
| `--timeout` | الميزانية الكاملة ديال طلب API وإعادة المحاولة بالثواني، بما فيها الأرقام العشرية (الافتراضي: 10) |
| `--retries` | محاولات إضافية للأعطال المؤقتة، من 0 حتى لـ 5 (الافتراضي: 1) |
| `--max-age` | أقصى عمر لتسعيرة المزود بالثواني وكيفرض وجود طابع زمني؛ التسعيرات لي فيها طابع زمني كتستعمل 3600 افتراضياً |
| `--warning-change` | حد التحذير لنسبة التغيير المطلقة فـ 24 ساعة |
| `--critical-change` | حد الخطر لنسبة التغيير المطلقة فـ 24 ساعة |
| `--api-url` | رابط API الرئيسي |
| `--fallback-url` | نقطة نهاية متوافقة إضافية؛ عاودها حسب الترتيب المفضل |
| `--state-file` | ملف JSON لتاريخ حركة الثمن |
| `--move-window` | نافذة الحركة بالثواني (الافتراضي: 3600) |
| `--warning-move`, `--critical-move` | عتبات الحركة المطلقة داخل النافذة بالنسبة المئوية |
| `-v`, `--verbose` | تفعيل المخرجات المفصلة |
| `-V`, `--version` | عرض رقم الإصدار |
| `-h`, `--help` | عرض رسالة المساعدة |

## إعدادات Nagios

### تعريف الأمر

ضبط ماكرو الموارد ديال Nagios `$USER1$` على مجلد الإضافات (الحزم الأصلية كتستعمل `/usr/lib/nagios/plugins`). زيد هاد الشي فإعدادات الأوامر ديال Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### تعريف الخدمة

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

## رموز الخروج

المعطيات لي ماشي صالحة، المهل لي ماشي موجبة، مجالات العتبات الخاطئة، وأثمان API المخسرة كيرجعو `UNKNOWN` (رمز الخروج 3).
العتبات خاصهم يكونو أرقام منتهية وماشي سالبة، مع كل حد أدنى ما كيفوتش الحد الأعلى ديالو.
العملة خاصها تكون بين 2 و 16 حرف ولا رقم. الإعدادات الخاطئة كترفض قبل ما يتصل بـ API.
الأثمان خاصهم يكونو منتهين وماشي سالبين، على شكل أرقام JSON ولا سلاسل عشرية عادية بحال `"43521.5"`.
أي جواب ما فيهش العملة المطلوبة كيسميها، مثلاً `Response has no EUR price`.
الأجوبة لي ماشي صالحة ما كتخرجش بيانات الأداء.
التشخيصات المفصلة كتمشي لـ stderr باش stdout يبقى فيه غير سطر واحد ديال حالة المراقبة.

| الرمز | الحالة | الوصف |
|-------|--------|-------|
| 0 | OK | الثمن داخل المجال المقبول |
| 1 | WARNING | الثمن فات عتبة التحذير |
| 2 | CRITICAL | الثمن فات عتبة الخطر |
| 3 | UNKNOWN | وقع خطأ (فشل API، انتهاء المهلة، إلخ.) |

## بيانات الأداء

الإضافة كتخرج بيانات الأداء بالصيغة القياسية ديال Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

بيانات أداء الثمن فيها مجالات التحذير والخطر المضبوطة وحد أدنى ديال صفر.
العتبات كيتطبعو بالصيغة العشرية الكاملة، ما كيتقربوش وما كيتكتبوش بالصيغة الأسية، باش القيم الكبار بحال `14500000:16250000` يبقاو ساهلين فالتحليل.
مدة الطلب كتشمل جميع المحاولات وأوقات الانتظار.
عمر التسعيرة كيخرج غير ملي المزود كيعطي طابع زمني صالح؛ والتغيير اليومي كيخرج ملي كيكون متوفر.
مجالات التغيير متماثلة حول الصفر.
البيانات لي ماشي صالحة ولا القديمة كتعطي `UNKNOWN` بلا بيانات أداء الثمن.
تقدر تستعمل هاد المقاييس مع أدوات الرسوم البيانية بحال PNP4Nagios، Grafana، ولا InfluxDB.

## API

هاد الإضافة كتستعمل [CoinGecko API](https://www.coingecko.com/en/api) افتراضياً، لي هو فابور وما كيحتاجش مفتاح API. كيتطبقو عليه حدود عدد الطلبات.

نقاط النهاية المخصصة خاصهم يستعملو نفس شكل الجواب: `bitcoin.<currency>` للثمن، `bitcoin.last_updated_at` للطابع الزمني UNIX بالثواني، و `bitcoin.<currency>_24h_change` لنسبة التغيير اليومي الموقّعة.
غير الثمن بوحدو لي ضروري فاش كيكونو `--max-age` وعتبات التغيير ما كاينينش.
إيلا كان الطابع الزمني موجود، كيتحقق منو واخا هكاك: ما خاصوش يكون فالمستقبل ولا قديم كتر من ساعة وحدة.
الجواب المفكوك خاصو يقد فـ 64 KiB.

العملات المدعومة فيهم: usd، eur، gbp، jpy، aud، cad، chf، cny، وبزاف آخرين.

## الأمان

الإجراءات لي لتحت مطبّقة فالكود الحالي. كتحد من شنو تقدر تدير شي نقطة نهاية ماشي مزيانة ولا مستخدم محلي لسيرفر المراقبة؛ ولكن ما كتضمنش مصداقية التسعيرة نفسها.

- شهادات HTTPS كيتحقق منهم بالإعدادات الافتراضية ديال `requests`، وما كاين حتى خيار كيعطل هاد التحقق. شي `--api-url` مخصص كيستعمل `http://` العادية ما عندوش هاد الحماية.
- DNS، الاتصال، القراءة، إعادة المحاولة، وأوقات الانتظار كاملين كيتقاسمو مهلة `--timeout`. أي طرف كيسيفط البيانات بشوية ما يقدرش يطوّلها.
- كل جواب محدود فـ 64 KiB من بعد فك الضغط، وأجسام إعادة التوجيه كيتلاحو بلا ما يتقراو.
- أخطاء الطلبات كطبع غير رمز حالة HTTP ولا نوع الخطأ، حيت `--api-url` المخصص يقدر يكون فيه بيانات اعتماد.
- الأمر لي كتنصّبو حزم `.deb` و `.rpm` كيخدم Python فالوضع المعزول. كيتجاهل `PYTHONPATH`، مجلد حزم المستخدم، والموديلات لي فمجلد الخدمة. التثبيت بـ `pip` كيستعمل سكريبت الكونسول العادي وكيتبع البيئة لي منصب فيها.
- حالة الحركة كتتقرا وكتتكتب بلا ما تتبع أي رابط رمزي فاسم ملف الحالة ولا القفل، بالنسبة لمجلد تحل مرة وحدة فكل فحص.
- ملفات الإصدار فيهم إثباتات مصدر البناء زيادة على `SHA256SUMS`؛ شوف [من GitHub Releases](#from-github-releases).

## الترقية من 1.0.0

هاد التغييرات جاو فالإصدار 2.0.0.

- أي تسعيرة فيها طابع زمني ديال المزود قديم كتر من ساعة كترجع `UNKNOWN` إلا إيلا عطيتي `--max-age` كبر. نقاط النهاية لي ما كترجعش طابع زمني ما كتأثرش.
- `--currency` كيقبل غير من 2 حتى لـ 16 حرف ولا رقم.
- السلاسل الرقمية لي فيها فواصل الأرقام ولا فراغات فالجناب كترفض.
- وقت انتظار إعادة المحاولة لي ما كيقدش فالميزانية كيبلغ على العطل الأصلي فبلاصة `API request timed out`.
- الحزم الأصلية ما بقاتش كتأخذ بـ `PYTHONPATH`.
- العتبات ديال مليون ولا كتر كيبانو فبيانات الأداء كأرقام عشرية عادية فبلاصة الصيغة الأسية.

## الترجمة واللغات

مساعدة سطر الأوامر، أخطاء التحقق، وأوصاف حالة الإضافة كيدعمو 45 لغة (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) باستعمال كتالوجات مدمجة كتحمّل عبر المكتبة القياسية. اختيار اللغة كيقلب فـ `--lang`، ومن بعد `LC_ALL`، `LC_MESSAGES`، و `LANG`، وكيرجع لـ `en` افتراضياً. بادئات حالة Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) وبيانات الأداء كيبقاو نفسهم فجميع اللغات.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## التطوير

نصّب [mise](https://mise.jdx.dev/getting-started.html)، ومن بعد خدم إعداد التطوير لي الفوق. ملف `mise.toml` كيثبت نسخ Python و uv. أدوات التطوير معرّفة فـ `pyproject.toml` ومحسومة فـ `uv.lock` الملتزم بيه فالمستودع.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

نصّب خطافات الالتزام (commit hooks) من بعد الإعداد:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

استعمل `mise exec -- uv add --dev <tool>` ولا `mise exec -- uv add <dependency>` باش تحدث التبعيات وادفع `pyproject.toml` و `uv.lock` بجوج.

الـ CI كيفحص Python 3.12 و 3.13 على Linux و Python 3.13 على macOS. كل PR كيخدم حتى التحقق من الحزم، تدقيق التبعيات، و CodeQL، وكينصّب `.deb` على Ubuntu و `.rpm` على Fedora. التوزيعات المبنية كيكونو متوفرين كـ artifact سميتو `distributions` فتشغيلات CI.

إصدار الحزمة وسطر الأوامر كيجي من `check_bitcoin_price/__init__.py`. شوف [مسطرة الإصدار](../../../CONTRIBUTING.md#releases) على قبل رفع رقم الإصدار والنشر الأوتوماتيكي لملفات إصدارات GitHub.

## المساهمة

شوف [CONTRIBUTING.md](../../../CONTRIBUTING.md) باش تعرف طريقة عمل التطوير ومتطلبات الالتزامات الموقّعة.

## الرخصة

هاد المشروع مرخّص برخصة MIT - شوف ملف [LICENSE](../../../LICENSE) للتفاصيل.

## المؤلف

Thomas Vincent

## شكر وتقدير

- [CoinGecko](https://www.coingecko.com/) حيت كيوفر API فابور ديال العملات الرقمية
- [إرشادات تطوير إضافات Nagios](https://nagios-plugins.org/doc/guidelines.html)
