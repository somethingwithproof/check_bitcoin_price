# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · **العربية** · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

إضافة لنظامي Nagios وIcinga لمراقبة سعر Bitcoin مع عتبات تحذير وعتبات حرجة قابلة للتكوين.

## الميزات

- مراقبة سعر Bitcoin بعملات متعددة (USD وEUR وGBP وغيرها)
- عتبات تحذير وعتبات حرجة قابلة للتكوين (الحد الأعلى والحد الأدنى)
- مخرجات قياسية لإضافات Nagios مع بيانات الأداء
- يستخدم واجهة برمجة تطبيقات CoinGecko (مجانية، ولا تتطلب مفتاح API)
- دعم نقاط نهاية API مخصصة
- مهلة زمنية قابلة للتكوين
- التحقق من حداثة السعر باستخدام الطوابع الزمنية للمزود، بحد افتراضي يبلغ ساعة واحدة
- محاولات إعادة محدودة لحدود المعدل والإخفاقات المؤقتة في API
- موعد نهائي واحد لجميع المحاولات وسقف يبلغ 64 KiB لكل استجابة
- تنبيهات اختيارية حول التغير المئوي المطلق خلال 24 ساعة
- عتبات السعر ومدة الطلب وعمر عرض السعر ضمن بيانات الأداء

## التثبيت

<a name="from-github-releases"></a>

### من إصدارات GitHub

قم بتنزيل ملفات `.deb` و`.rpm` و`.tar.gz` وwheel و`SHA256SUMS` من [إصدارات GitHub](https://github.com/somethingwithproof/check_bitcoin_price/releases). تحقق من التنزيل باستخدام `sha256sum --ignore-missing --check SHA256SUMS`. تحمل الإصدارات التي تلي 1.0.0 أيضاً إثبات بناء موقّعاً؛ تأكد من أن الملف صادر عن سير عمل الإصدار لهذا المستودع باستخدام `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

استخدم أسماء الملفات من الإصدار المحدد. تثبّت الحزم الأصلية `/usr/bin/check_bitcoin_price` و`/usr/lib/nagios/plugins/check_bitcoin_price`؛ كما توفر حزمة RPM المسار `/usr/lib64/nagios/plugins/check_bitcoin_price`. يشغّل الأمر المحزّم لغة Python في الوضع المعزول، لذلك يتجاهل `PYTHONPATH` والوحدات الموجودة في مجلد العمل؛ ويتولى مدير حزم النظام حل تبعيات Python و`requests`. تحتوي هذه الحزم على شيفرة Python مستقلة عن البنية وتتطلب توزيعة توفر Python 3.12 أو أحدث.

### من المصدر

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

### مع العتبات

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### العتبات الفردية

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

### مهلة مخصصة

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### الحداثة وميزانية إعادة المحاولة

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

يجب ألا يتجاوز عمر عرض السعر الذي يحمل طابعاً زمنياً للمزود ساعة واحدة افتراضياً.
تظل نقاط النهاية التي تُرجع سعراً فقط قابلة للاستخدام عند غياب `--max-age`.
عند تحديد `--max-age`، تؤدي الطوابع الزمنية المفقودة أو غير الصالحة أو المستقبلية أو القديمة
إلى إرجاع `UNKNOWN`؛ ولا يستبدل المكوّن الإضافي وقت الجلب المحلي بوقت عرض السعر
الخاص بالمزود. يظل الطابع الزمني المطابق تماماً للحد الأقصى للعمر مقبولاً.
وتُرفض الطوابع الزمنية المستقبلية دائماً.

يسمح الإعداد الافتراضي بمحاولة إعادة واحدة. وتُعاد المحاولة فقط في حالات أخطاء الاتصال
وانتهاء المهلة واستجابات HTTP 408/429/500/502/503/504. يبدأ التراجع عند 0.5 ثانية
ويتضاعف للمحاولات اللاحقة؛ وتكون الأولوية لثواني `Retry-After` وتواريخ HTTP.
تشترك جميع المحاولات وقراءات الاستجابة وفك ترميز JSON وفترات انتظار إعادة المحاولة
في ميزانية `--timeout`. إذا تعذر استيعاب فترة انتظار إعادة المحاولة ضمن الميزانية، تُرجع الإضافة
`UNKNOWN` فوراً وتبلغ عن الإخفاق الذي استدعاها، مثل `HTTP 429` أو `ConnectionError`،
وليس انتهاء المهلة. لا تُعاد المحاولة عند إخفاقات المصادقة أو أخطاء HTTP الدائمة الأخرى
أو JSON غير الصالح أو الاستجابات التي يتجاوز حجم بياناتها المفكوكة 64 KiB. استخدم
`--retries 0` لتعطيل إعادة المحاولة.

### مصادر الأسعار الاحتياطية

استخدم خيارات `--fallback-url URL` القابلة للتكرار مع نقاط نهاية متوافقة مع CoinGecko.
على سبيل المثال، أضف `--fallback-url https://quotes.example.org/simple/price`.
يحصل كل مصدر على حصة متساوية من الموعد النهائي المتبقي للطلب، بما في ذلك محاولات
إعادته. يؤدي الإخفاق المؤقت أو تأخير إعادة المحاولة الأطول من تلك الحصة إلى الانتقال
إلى المصدر التالي. أما إخفاقات التحقق من TLS وأخطاء HTTP الدائمة وعروض الأسعار غير الصالحة
فتُرجع UNKNOWN. يُحد حجم كل استجابة سعر بمقدار 64 KiB من البيانات المفكوكة.
وعند تكوين مصادر احتياطية، تحدد الحالة المصدر المجيب بصيغة
`primary` و`fallback1` وهكذا، دون طباعة عنوان URL الخاص به.

### الحركة ضمن نافذة زمنية قصيرة

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

امنح مستخدم المراقبة مجلد حالة خاصاً قابلاً للكتابة على نظام ملفات محلي لنظام Linux أو
macOS. احتفظ بملف `.lock` المجاور في مكانه بين عمليات الفحص. استخدم ملف حالة منفصلاً
لكل نافذة زمنية، حيث تمتلك العملات سجلات تاريخية مستقلة داخله.
النافذة الافتراضية هي 3600 ثانية. يحتاج كل عرض سعر صالح إلى طابع زمني للمزود
ضمن النافذة وحد العمر، وهو ساعة واحدة ما لم يحدد `--max-age` قيمة أخرى.
تقارن الإضافة السعر الحالي بأقدم سعر موجب سابق ضمن تلك النافذة وتبلغ عن
الثواني المنقضية الفعلية. لا تنشئ الطوابع الزمنية المكررة عينات إضافية.
تبدأ العينة الأولى أو السجل المنتهي الصلاحية أو JSON التالف خط أساس جديداً؛
ويكون مقياس النافذة غير معروف حتى تتوفر عينة قابلة للمقارنة. تظل التنبيهات الأخرى
سارية. تؤدي الحالة غير القابلة للكتابة، أو كون ملف الحالة أو القفل رابطاً رمزياً، أو ورود عرض سعر
أقدم من أحدث عينة مسجلة إلى إرجاع UNKNOWN. يستخدم مقياس `bitcoin_move_window` ذو الإشارة
نطاقات تحذير وحرجة متماثلة. ولا يطلق التساوي عند الحد تنبيهاً.

تفتح الإضافة مجلد الحالة مرة واحدة لكل فحص وتعمل نسبةً إليه، بحيث لا يمكن
لأي مكون مسار يُستبدل أثناء الفحص إعادة توجيه القفل أو القراءة أو الكتابة.
يتم اتباع الروابط الرمزية في جزء المجلد من المسار عند بدء الفحص، مما يبقي
روابط المنصة مثل `/var` على نظام macOS قابلة للاستخدام. لذلك يجب ألا يكون
مجلد الحالة والمجلدات الأبوية له قابلة للكتابة من قبل مستخدمين آخرين.
وتُنشأ ملفات الحالة والقفل بالوضع 0600.

### التغير المئوي اليومي

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

تقيس عتبات التغير القيمة المطلقة للتغير المئوي ذي الإشارة خلال 24 ساعة من CoinGecko
بالعملة المحددة. لا يطلق التغير المطابق تماماً للعتبة تنبيهاً. وإذا تم تزويد كلتا
العتبتين، فيجب ألا يتجاوز التحذير المستوى الحرج. يؤدي فقدان بيانات التغير المطلوبة
أو عدم صلاحيتها إلى إرجاع `UNKNOWN`. يمكن الجمع بين تنبيهات السعر والتغير؛ وتفوز الدرجة
الأعلى خطورة، مع إعطاء الأولوية للسعر عند تساوي درجات الخطورة.

## خيارات سطر الأوامر

| الخيار | الوصف |
|--------|-------|
| `-w`, `--warning` | نطاق عتبة التحذير (التنسيق: LOW:HIGH) |
| `-c`, `--critical` | نطاق العتبة الحرجة (التنسيق: LOW:HIGH) |
| `--warning-low` | عتبة التحذير لانخفاض السعر |
| `--warning-high` | عتبة التحذير لارتفاع السعر |
| `--critical-low` | العتبة الحرجة لانخفاض السعر |
| `--critical-high` | العتبة الحرجة لارتفاع السعر |
| `--currency` | رمز العملة المكون من 2 إلى 16 حرفاً أو رقماً (الافتراضي: usd) |
| `--timeout` | إجمالي ميزانية طلب API وإعادة المحاولة بالثواني، بما في ذلك القيم الكسرية (الافتراضي: 10) |
| `--retries` | محاولات إضافية للأخطاء العابرة، 0 إلى 5 (الافتراضي: 1) |
| `--max-age` | الحد الأقصى لعمر عرض سعر المزود بالثواني واشتراط وجود طابع زمني؛ الافتراضي للعروض ذات الطابع الزمني هو 3600 |
| `--warning-change` | حد التحذير للتغير المئوي المطلق خلال 24 ساعة |
| `--critical-change` | الحد الحرج للتغير المئوي المطلق خلال 24 ساعة |
| `--api-url` | عنوان URL الأساسي لـ API |
| `--fallback-url` | نقطة نهاية متوافقة إضافية؛ كررها حسب الترتيب المفضل |
| `--state-file` | ملف سجل الحركة بصيغة JSON |
| `--move-window` | نافذة الحركة بالثواني (الافتراضي: 3600) |
| `--warning-move`, `--critical-move` | عتبات الحركة المطلقة للنافذة بالنسبة المئوية |
| `-v`, `--verbose` | تمكين المخرجات التفصيلية |
| `-V`, `--version` | عرض رقم الإصدار |
| `-h`, `--help` | عرض رسالة المساعدة |

## تكوين Nagios

### تعريف الأمر

عيّن ماكرو موارد Nagios `$USER1$` إلى مجلد الإضافات (تستخدم الحزم الأصلية `/usr/lib/nagios/plugins`). أضف إلى تكوين أوامر Nagios لديك:

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

### تكوين Icinga2

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

تُرجع الوسائط غير الصالحة والمهل الزمنية غير الموجبة ونطاقات العتبات غير الصالحة وأسعار API
المشوهة القيمة `UNKNOWN` (رمز الخروج 3). يجب أن تكون العتبات أعداداً محدودة وغير سالبة،
مع ألا يتجاوز كل حد أدنى حده الأعلى. يجب أن يتكون رمز العملة من 2 إلى 16 حرفاً أو رقماً.
يُرفض التكوين غير الصالح قبل الاتصال بـ API. يجب أن تكون الأسعار محدودة وغير سالبة، ومقدمة
كأرقام JSON أو سلاسل عشرية عادية مثل `"43521.5"`. تذكر الاستجابة التي تفتقر إلى العملة
المطلوبة اسمها، على سبيل المثال `Response has no EUR price`. لا تصدر الاستجابات غير الصالحة
بيانات أداء. وتُوجّه التشخيصات التفصيلية إلى stderr بحيث يحتوي stdout على سطر حالة مراقبة واحد فقط.

| الرمز | الحالة | الوصف |
|-------|--------|-------|
| 0 | OK | السعر ضمن النطاق المقبول |
| 1 | WARNING | تجاوز السعر عتبة التحذير |
| 2 | CRITICAL | تجاوز السعر العتبة الحرجة |
| 3 | UNKNOWN | حدث خطأ (إخفاق API أو انتهاء المهلة وما إلى ذلك) |

## بيانات الأداء

تُخرج الإضافة بيانات الأداء بتنسيق Nagios القياسي:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

تتضمن بيانات أداء السعر نطاقات التحذير والنطاقات الحرجة المكوّنة وبحد أدنى يساوي الصفر.
وتُطبع العتبات بالترميز العشري الكامل دون تقريب أو صيغة أسية أبداً، بحيث تبقى القيم الكبيرة
مثل `14500000:16250000` قابلة للتحليل. يتضمن وقت الطلب جميع المحاولات وفترات التراجع.
لا يُصدر عمر عرض السعر إلا عندما يوفّر المزود طابعاً زمنياً صالحاً؛ ويُصدر التغير اليومي
عند توفره. تكون نطاقات التغير متماثلة حول الصفر. وتنتج البيانات غير الصالحة أو القديمة الحالة
`UNKNOWN` دون بيانات أداء للسعر. يمكن استخدام هذه المقاييس مع أدوات الرسم البياني
مثل PNP4Nagios أو Grafana أو InfluxDB.

## واجهة برمجة التطبيقات (API)

تستخدم هذه الإضافة [واجهة برمجة تطبيقات CoinGecko](https://www.coingecko.com/en/api) افتراضياً، وهي مجانية ولا تتطلب مفتاح API. وتنطبق حدود المعدل.

يجب أن تستخدم نقاط النهاية المخصصة نفس بنية الاستجابة: `bitcoin.<currency>` للسعر،
و`bitcoin.last_updated_at` لثواني الطابع الزمني لنظام UNIX، و`bitcoin.<currency>_24h_change`
للتغير المئوي اليومي ذي الإشارة. لا يلزم سوى السعر عند غياب `--max-age` وعتبات التغير.
ويظل أي طابع زمني موجود خاضعاً للفحص: يجب ألا يكون في المستقبل أو أقدم من ساعة واحدة.
ويجب ألا يتجاوز حجم الاستجابة المفكوكة 64 KiB.

تشمل العملات المدعومة: usd وeur وgbp وjpy وaud وcad وchf وcny وغيرها الكثير.

## الأمان

الإجراءات المذكورة أدناه مطبقة في الشيفرة الحالية. وهي تحد مما يمكن أن تفعله نقطة نهاية سيئة
السلوك أو مستخدم محلي بمضيف المراقبة؛ لكنها لا تجعل عرض السعر نفسه موثوقاً.

- يتم التحقق من شهادات HTTPS باستخدام الإعدادات الافتراضية لمكتبة `requests`، ولا يوجد خيار
  لتعطيل التحقق. ولا يتمتع عنوان `--api-url` المخصص الذي يستخدم `http://` غير المشفر
  بهذه الحماية.
- يتشارك كل من DNS والاتصال والقراءات وإعادة المحاولة والتراجع في الموعد النهائي `--timeout`.
  ولا يمكن للطرف المقابل الذي يرسل البيانات ببطء تمديده.
- يقتصر حجم كل استجابة على 64 KiB بعد فك الضغط، ويتم تجاهل محتوى استجابات
  إعادة التوجيه دون قراءته.
- لا تطبع إخفاقات الطلب سوى حالة HTTP أو فئة الخطأ، لأن عنوان `--api-url` المخصص
  قد يحتوي على بيانات اعتماد.
- يشغّل الأمر المثبت بواسطة `.deb` و`.rpm` لغة Python في الوضع المعزول. فهو يتجاهل
  `PYTHONPATH` ومجلد موقع المستخدم والوحدات الموجودة في مجلد العمل. أما التثبيت عبر `pip`
  فيستخدم نص سطر الأوامر القياسي ويتبع البيئة المثبت فيها.
- تُقرأ حالة الحركة وتُكتب دون اتباع أي رابط رمزي عند اسم ملف الحالة أو القفل،
  نسبةً إلى مجلد يُفتح مرة واحدة لكل فحص.
- تحمل أصول الإصدار شهادات إثبات البناء بالإضافة إلى `SHA256SUMS`؛ راجع
  [من إصدارات GitHub](#from-github-releases).

## الترقية من 1.0.0

تصل هذه التغييرات في الإصدار 2.0.0.

- يُرجع عرض السعر الذي يحمل طابعاً زمنياً للمزود أقدم من ساعة واحدة القيمة `UNKNOWN` ما لم يتم
  تحديد قيمة أكبر للخيار `--max-age`. ولا تتأثر نقاط النهاية التي لا تُرجع طابعاً زمنياً.
- يقبل الخيار `--currency` ما بين 2 إلى 16 حرفاً أو رقماً فقط.
- تُرفض السلاسل الرقمية التي تحتوي على فواصل أرقام أو مسافات محيطة.
- يبلغ انتظار إعادة المحاولة الذي لا يتسع ضمن الميزانية عن الإخفاق الأساسي بدلاً من
  `API request timed out`.
- لم تعد الحزم الأصلية تأخذ `PYTHONPATH` في الحسبان.
- تظهر العتبات التي تبلغ مليوناً أو أكثر في بيانات الأداء كأعداد عشرية عادية بدلاً من
  الترميز الأسي.

## التوطين

تدعم تعليمات سطر الأوامر وأخطاء التحقق من الصحة وأوصاف حالة الإضافة 45 لغة وإعداداً محلياً (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) باستخدام كتالوجات مدمجة محملة عبر المكتبة القياسية. يتحقق حل اللغة من `--lang`، ثم `LC_ALL` و`LC_MESSAGES` و`LANG`، مع الرجوع إلى `en` عند التعذر. تظل بادئات حالة Nagios (`OK` و`WARNING` و`CRITICAL` و`UNKNOWN`) وبيانات الأداء دون تغيير عبر جميع اللغات.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## التطوير

ثبّت [mise](https://mise.jdx.dev/getting-started.html)، ثم نفّذ خطوات إعداد التطوير أعلاه. يثبت ملف `mise.toml` إصداري Python وuv. وتُعلن أدوات التطوير في `pyproject.toml` وتُحل في ملف `uv.lock` المودع.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

ثبّت خطافات الإيداع (commit hooks) بعد الإعداد:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

استخدم `mise exec -- uv add --dev <tool>` أو `mise exec -- uv add <dependency>` لتحديث التبعيات وأودِع كلاً من `pyproject.toml` و`uv.lock`.

يفحص التكامل المستمر (CI) إصداري Python 3.12 و3.13 على Linux وإصدار Python 3.13 على macOS. كما يشغّل كل طلب سحب (PR) التحقق من صحة الحزم وتدقيق التبعيات وCodeQL، ويثبّت حزمة `.deb` على Ubuntu وحزمة `.rpm` على Fedora. وتتوفر التوزيعات المبنية كعنصر `distributions` في عمليات تشغيل CI.

يأتي إصدار الحزمة وأداة سطر الأوامر من `check_bitcoin_price/__init__.py`. راجع [عملية الإصدار](../../../CONTRIBUTING.md#releases) لرفع أرقام الإصدارات والنشر التلقائي لأصول إصدارات GitHub.

## المساهمة

راجع [CONTRIBUTING.md](../../../CONTRIBUTING.md) للاطلاع على سير عمل التطوير ومتطلبات الإيداعات الموقّعة.

## الترخيص

هذا المشروع مرخص بموجب رخصة MIT. راجع ملف [LICENSE](../../../LICENSE) للتفاصيل.

## المؤلف

Thomas Vincent

## الشكر والتقدير

- [CoinGecko](https://www.coingecko.com/) لتوفير واجهة برمجة تطبيقات مجانية للعملات الرقمية
- [إرشادات تطوير إضافات Nagios](https://nagios-plugins.org/doc/guidelines.html)
