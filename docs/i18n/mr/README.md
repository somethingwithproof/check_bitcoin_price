# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · **मराठी** · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

कॉन्फिग करण्यायोग्य चेतावणी आणि गंभीर मर्यादांसह Bitcoin किमतीचे निरीक्षण करण्यासाठी Nagios/Icinga प्लगइन.

## वैशिष्ट्ये

- एकाधिक चलनांमध्ये Bitcoin किमतीचे निरीक्षण करा (USD, EUR, GBP, इ.)
- कॉन्फिग करण्यायोग्य चेतावणी आणि गंभीर मर्यादा (उच्च आणि निम्न)
- कामगिरी डेटासह मानक Nagios प्लगइन आउटपुट
- CoinGecko API वापरते (मोफत, API की आवश्यक नाही)
- कस्टम API एंडपॉइंट्ससाठी समर्थन
- कॉन्फिग करण्यायोग्य टाइमआउट
- विक्रेत्याच्या टाइमस्टॅम्पचा वापर करून कोट ताजेपणा तपासणी, एक तासाच्या डीफॉल्ट मर्यादेसह
- दर मर्यादा आणि तात्पुरत्या API अपयशांसाठी मर्यादित पुनर्प्रयत्न
- सर्व प्रयत्नांसाठी एकच अंतिम मुदत आणि प्रत्येक प्रतिसादावर 64 KiB ची मर्यादा
- २४ तासांच्या निरपेक्ष टक्केवारी बदलावर वैकल्पिक अलर्ट
- कामगिरी डेटामध्ये किमतीच्या मर्यादा, विनंतीचा कालावधी आणि कोटचे वय

## इन्स्टॉलेशन

### GitHub Releases मधून

[GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) वरून `.deb`, `.rpm`, `.tar.gz`, wheel आणि `SHA256SUMS` फाइल्स डाउनलोड करा. `sha256sum --ignore-missing --check SHA256SUMS` सह डाउनलोडची पडताळणी करा. 1.0.0 नंतरच्या रिलीझमध्ये स्वाक्षरी केलेला बिल्ड प्रोव्हेनन्स देखील असतो; `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` सह मालमत्ता या रिपॉझिटरीच्या रिलीझ वर्कफ्लोमधून आल्याची खात्री करा.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

निवडलेल्या रिलीझमधील फाइलनावे वापरा. नेटिव्ह पॅकेजेस `/usr/bin/check_bitcoin_price` आणि `/usr/lib/nagios/plugins/check_bitcoin_price` इन्स्टॉल करतात; RPM मध्ये `/usr/lib64/nagios/plugins/check_bitcoin_price` देखील प्रदान केले जाते. पॅकेज केलेली कमांड Python आयसोलेटेड मोडमध्ये चालवते, त्यामुळे ती `PYTHONPATH` आणि कार्यरत डिरेक्टरीमधील मॉड्यूल्सकडे दुर्लक्ष करते; सिस्टम पॅकेज मॅनेजर Python आणि `requests` अवलंबित्वे सोडवतो. त्यामध्ये आर्किटेक्चर-स्वतंत्र Python कोड असतो आणि त्यासाठी Python 3.12 किंवा नवीन आवृत्ती देणारे वितरण आवश्यक असते.

### सोर्स कोडमधून

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### डेव्हलपमेंटसाठी

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## वापर

### मूलभूत वापर

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### मर्यादांसह

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### स्वतंत्र मर्यादा

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### भिन्न चलन

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### कस्टम टाइमआउट

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### ताजेपणा आणि पुनर्प्रयत्न बजेट

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

विक्रेत्याचा टाइमस्टॅम्प असलेला कोट डीफॉल्टनुसार जास्तीत जास्त एक तास जुना असावा.
जेव्हा `--max-age` अनुपस्थित असते, तेव्हा फक्त किंमत परत करणारे एंडपॉइंट्स वापरण्यायोग्य राहतात.
`--max-age` सह, गहाळ, अवैध, भविष्यातील किंवा जुने विक्रेता टाइमस्टॅम्प `UNKNOWN` परत
करतात; प्लगइन विक्रेत्याच्या कोट वेळेऐवजी स्थानिक फेच वेळ वापरत नाही. नेमक्या
वयाच्या मर्यादेवर असलेला टाइमस्टॅम्प स्वीकार्य राहतो. भविष्यातील टाइमस्टॅम्प नेहमी नाकारले जातात.

डीफॉल्टनुसार एक पुनर्प्रयत्न करण्याची परवानगी आहे. फक्त कनेक्शन त्रुटी, टाइमआउट आणि HTTP
408/429/500/502/503/504 प्रतिसादांसाठीच पुनर्प्रयत्न केला जातो. बॅकऑफ 0.5 सेकंदांपासून
सुरू होतो आणि पुढील पुनर्प्रयत्नांसाठी दुप्पट होतो; `Retry-After` सेकंद आणि HTTP तारखांना
प्राधान्य दिले जाते. सर्व प्रयत्न, प्रतिसाद वाचन, JSON डिकोडिंग आणि पुनर्प्रयत्न प्रतीक्षा
`--timeout` बजेट सामायिक करतात. बजेटमध्ये न बसणारी पुनर्प्रयत्न प्रतीक्षा त्वरित `UNKNOWN`
परत करते आणि टाइमआउटऐवजी ज्यामुळे ती उद्भवली ते अपयश कळवते, जसे की `HTTP 429` किंवा
`ConnectionError`. प्रमाणीकरण अपयश, इतर कायमस्वरूपी HTTP त्रुटी, अवैध JSON आणि डिकोड
केलेल्या डेटाच्या 64 KiB पेक्षा मोठे प्रतिसाद यांचा पुनर्प्रयत्न केला जात नाही. पुनर्प्रयत्न
अक्षम करण्यासाठी `--retries 0` वापरा.

### फॉलबॅक कोट स्त्रोत

CoinGecko-सुसंगत एंडपॉइंट्ससह पुनरावृत्ती करण्यायोग्य `--fallback-url URL` पर्याय वापरा.
उदाहरणार्थ, `--fallback-url https://quotes.example.org/simple/price` जोडा.
प्रत्येक स्त्रोताला त्याच्या पुनर्प्रयत्नांसह उर्वरित विनंती अंतिम मुदतीचा समान वाटा मिळतो.
तात्पुरते अपयश किंवा त्या वाट्यापेक्षा जास्त पुनर्प्रयत्न विलंब झाल्यास पुढील स्त्रोताकडे
वळवले जाते. TLS पडताळणी अपयश, कायमस्वरूपी HTTP त्रुटी आणि अवैध कोट्स UNKNOWN परत करतात.
प्रत्येक कोट प्रतिसाद डिकोड केलेल्या डेटाच्या 64 KiB पर्यंत मर्यादित आहे. जेव्हा फॉलबॅक
कॉन्फिग केलेले असतात, तेव्हा स्थिती त्याची URL न छापता उत्तर देणारा स्त्रोत `primary`,
`fallback1` इत्यादी म्हणून ओळखते.

### अल्प-कालावधीतील हालचाल

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

मॉनिटरिंग वापरकर्त्याला स्थानिक Linux किंवा macOS फाइलसिस्टमवर खाजगी लेखनयोग्य स्टेट
डिरेक्टरी द्या. तपासण्यांच्या दरम्यान शेजारील `.lock` फाइल जागीच ठेवा. प्रत्येक विंडोसाठी
स्वतंत्र स्टेट फाइल वापरा. त्यामध्ये चलनांचा स्वतंत्र इतिहास असतो. डीफॉल्ट विंडो 3600
सेकंद आहे. प्रत्येक वैध कोटसाठी विंडो आणि वय मर्यादेत असलेला विक्रेता टाइमस्टॅम्प आवश्यक
असतो, जो `--max-age` ने दुसरा सेट न केल्यास एक तास असतो. प्लगइन वर्तमान किमतीची तुलना
त्या विंडोमधील सर्वात जुन्या पूर्वीच्या सकारात्मक किमतीशी करतो आणि प्रत्यक्ष गेलेले सेकंद
कळवतो. पुनरावृत्ती झालेले टाइमस्टॅम्प अतिरिक्त नमुने तयार करत नाहीत. पहिला नमुना,
कालबाह्य इतिहास किंवा दूषित JSON नवीन आधाररेषा सुरू करतो; तुलना करण्यायोग्य नमुना मिळेपर्यंत
विंडो मेट्रिक अज्ञात राहतो. इतर अलर्ट अजूनही लागू होतात. लेखनयोग्य नसलेली स्थिती,
सिम्बॉलिक-लिंक स्टेट किंवा लॉक फाइल, किंवा नवीनतम नोंदवलेल्या नमुन्यापेक्षा जुना कोट
UNKNOWN परत करतो. चिन्हांकित `bitcoin_move_window` मेट्रिक सममितीय चेतावणी आणि गंभीर
श्रेणी वापरते. मर्यादेवरील समानतेमुळे अलर्ट होत नाही.

प्लगइन प्रत्येक तपासणीसाठी स्टेट डिरेक्टरी एकदा उघडतो आणि तिच्या सापेक्ष काम करतो,
त्यामुळे तपासणीदरम्यान बदललेला पथ घटक लॉक, वाचन किंवा लेखन पुनर्निर्देशित करू शकत नाही.
तपासणी सुरू झाल्यावर पथाच्या डिरेक्टरी भागातील सिम्बॉलिक लिंक्सचे अनुसरण केले जाते,
ज्यामुळे macOS वरील `/var` सारख्या प्लॅटफॉर्म लिंक्स वापरण्यायोग्य राहतात. त्यामुळे स्टेट
डिरेक्टरी आणि तिचे पूर्वज इतर वापरकर्त्यांसाठी लेखनयोग्य नसावेत. स्टेट आणि लॉक फाइल्स
मोड 0600 सह तयार केल्या जातात.

### दैनिक टक्केवारीतील हालचाल

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

बदलाच्या मर्यादा निवडलेल्या चलनातील CoinGecko च्या चिन्हांकित 24-तासांच्या टक्केवारी
बदलाचे निरपेक्ष मूल्य मोजतात. नेमक्या मर्यादेवर असलेल्या बदलामुळे अलर्ट होत नाही. दोन्ही
मर्यादा दिल्यास, चेतावणी मर्यादा गंभीर मर्यादेपेक्षा जास्त नसावी. गहाळ किंवा अवैध आवश्यक
बदल डेटा `UNKNOWN` परत करतो. किंमत आणि बदलाचे अलर्ट एकत्र केले जाऊ शकतात; सर्वोच्च
तीव्रता जिंकते, आणि तीव्रता समान असल्यास किमतीला प्राधान्य दिले जाते.

## कमांड लाइन पर्याय

| पर्याय | वर्णन |
|--------|-------|
| `-w`, `--warning` | चेतावणी मर्यादा श्रेणी (स्वरूप: LOW:HIGH) |
| `-c`, `--critical` | गंभीर मर्यादा श्रेणी (स्वरूप: LOW:HIGH) |
| `--warning-low` | कमी किमतीसाठी चेतावणी मर्यादा |
| `--warning-high` | उच्च किमतीसाठी चेतावणी मर्यादा |
| `--critical-low` | कमी किमतीसाठी गंभीर मर्यादा |
| `--critical-high` | उच्च किमतीसाठी गंभीर मर्यादा |
| `--currency` | 2-16 अक्षरे किंवा अंकांचा चलन कोड (डीफॉल्ट: usd) |
| `--timeout` | सेकंदांमध्ये एकूण API विनंती/पुनर्प्रयत्न बजेट, अपूर्णांक मूल्यांसह (डीफॉल्ट: 10) |
| `--retries` | अतिरिक्त तात्पुरते प्रयत्न, 0–5 (डीफॉल्ट: 1) |
| `--max-age` | सेकंदांमध्ये कमाल विक्रेता कोट वय आणि टाइमस्टॅम्प आवश्यक करा; टाइमस्टॅम्प केलेले कोट्स डीफॉल्टनुसार 3600 |
| `--warning-change` | 24-तासांच्या निरपेक्ष टक्केवारी हालचालीसाठी चेतावणी मर्यादा |
| `--critical-change` | 24-तासांच्या निरपेक्ष टक्केवारी हालचालीसाठी गंभीर मर्यादा |
| `--api-url` | प्राथमिक API URL |
| `--fallback-url` | अतिरिक्त सुसंगत एंडपॉइंट; पसंतीच्या क्रमाने पुन्हा वापरा |
| `--state-file` | JSON हालचाल इतिहास फाइल |
| `--move-window` | सेकंदांमध्ये हालचाल विंडो (डीफॉल्ट: 3600) |
| `--warning-move`, `--critical-move` | टक्केवारीत निरपेक्ष विंडो हालचाल मर्यादा |
| `-v`, `--verbose` | सविस्तर आउटपुट सक्षम करा |
| `-V`, `--version` | आवृत्ती दर्शवा |
| `-h`, `--help` | मदत संदेश दर्शवा |

## Nagios कॉन्फिगरेशन

### कमांड व्याख्या

Nagios संसाधन मॅक्रो `$USER1$` प्लगइन डिरेक्टरीवर सेट करा (नेटिव्ह पॅकेजेस `/usr/lib/nagios/plugins` वापरतात). तुमच्या Nagios कमांड्स कॉन्फिगरेशनमध्ये जोडा:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### सेवा व्याख्या

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

### Icinga2 कॉन्फिगरेशन

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

## एक्झिट कोड्स

अवैध युक्तिवाद, सकारात्मक नसलेले टाइमआउट, अवैध मर्यादा श्रेणी आणि विकृत API किमती
`UNKNOWN` (एक्झिट 3) परत करतात. मर्यादा मर्यादित, ऋण नसलेल्या संख्या असाव्यात, ज्यामध्ये
प्रत्येक निम्न मर्यादा तिच्या उच्च मर्यादेपेक्षा मोठी नसावी. चलन 2-16 अक्षरे किंवा अंकांचे
असावे. API शी संपर्क साधण्यापूर्वीच अवैध कॉन्फिगरेशन नाकारले जाते. किमती मर्यादित आणि
ऋण नसलेल्या असाव्यात, ज्या JSON संख्या किंवा `"43521.5"` सारख्या साध्या दशांश स्ट्रिंग
म्हणून दिल्या जातात. विनंती केलेल्या चलनाशिवाय आलेला प्रतिसाद त्याचे नाव नमूद करतो,
उदाहरणार्थ `Response has no EUR price`. अवैध प्रतिसाद कामगिरी डेटा उत्सर्जित करत नाहीत.
सविस्तर निदान stderr वर जाते जेणेकरून stdout मध्ये एकच मॉनिटरिंग स्थिती ओळ राहील.

| कोड | स्थिती | वर्णन |
|-----|--------|-------|
| 0 | OK | किंमत स्वीकार्य मर्यादेत आहे |
| 1 | WARNING | किमतीने चेतावणी मर्यादा ओलांडली |
| 2 | CRITICAL | किमतीने गंभीर मर्यादा ओलांडली |
| 3 | UNKNOWN | त्रुटी आली (API अपयश, टाइमआउट, इ.) |

## कामगिरी डेटा

प्लगइन मानक Nagios स्वरूपात कामगिरी डेटा आउटपुट करतो:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

किंमत कामगिरी डेटामध्ये कॉन्फिग केलेल्या चेतावणी/गंभीर श्रेणी आणि किमान शून्य मूल्य
समाविष्ट असते. मर्यादा पूर्ण दशांश चिन्हांकित पद्धतीत छापल्या जातात, कधीही गोल केल्या जात
नाहीत किंवा घातांक स्वरूपात नसतात, त्यामुळे `14500000:16250000` सारख्या मोठ्या मूल्यांचे
विश्लेषण करणे सोपे राहते. विनंती वेळेत सर्व प्रयत्न आणि बॅकऑफ समाविष्ट असतात. विक्रेता
वैध टाइमस्टॅम्प पुरवतो तेव्हाच कोट वय उत्सर्जित केले जाते; उपलब्ध असताना दैनिक बदल उत्सर्जित
केला जातो. बदलाच्या श्रेणी शून्याभोवती सममितीय असतात. अवैध किंवा जुना डेटा किंमत कामगिरी
डेटाशिवाय `UNKNOWN` तयार करतो. हे मेट्रिक्स PNP4Nagios, Grafana, किंवा InfluxDB सारख्या
ग्राफिंग टूल्ससह वापरले जाऊ शकतात.

## API

हे प्लगइन डीफॉल्टनुसार [CoinGecko API](https://www.coingecko.com/en/api) वापरते, जे मोफत आहे आणि त्यासाठी API की आवश्यक नाही. दर मर्यादा लागू होतात.

कस्टम एंडपॉइंट्सने समान प्रतिसाद स्वरूप वापरणे आवश्यक आहे: किमतीसाठी `bitcoin.<currency>`,
UNIX टाइमस्टॅम्प सेकंदांसाठी `bitcoin.last_updated_at`, आणि चिन्हांकित दैनिक टक्केवारी
हालचालीसाठी `bitcoin.<currency>_24h_change`. जेव्हा `--max-age` आणि बदलाच्या मर्यादा
अनुपस्थित असतात तेव्हा फक्त किंमत आवश्यक असते. उपस्थित असलेला टाइमस्टॅम्प तरीही तपासला
जातो: तो भविष्यातील किंवा एक तासापेक्षा जास्त जुना नसावा. डिकोड केलेला प्रतिसाद 64 KiB
मध्ये बसला पाहिजे.

समर्थित चलनांमध्ये हे समाविष्ट आहे: usd, eur, gbp, jpy, aud, cad, chf, cny, आणि बरेच काही.

## सुरक्षा

खालील उपाययोजना सध्याच्या कोडमध्ये लागू केल्या आहेत. चुकीचे वर्तन करणारा एंडपॉइंट
किंवा स्थानिक वापरकर्ता मॉनिटरिंग होस्टवर काय करू शकतो यावर त्या मर्यादा घालतात; त्या कोट
स्वतः विश्वासार्ह बनवत नाहीत.

- HTTPS प्रमाणपत्रे `requests` डीफॉल्टसह पडताळली जातात आणि कोणताही पर्याय पडताळणी अक्षम
  करत नाही. साधे `http://` वापरणाऱ्या कस्टम `--api-url` ला असे कोणतेही संरक्षण नसते.
- DNS, कनेक्शन, वाचन, पुनर्प्रयत्न आणि बॅकऑफ `--timeout` अंतिम मुदत सामायिक करतात.
  हळूवारपणे डेटा पाठवणारा पीअर ती वाढवू शकत नाही.
- डीकॉम्प्रेशननंतर प्रत्येक प्रतिसाद 64 KiB पर्यंत मर्यादित असतो आणि रीडायरेक्ट बॉडीज
  न वाचता टाकून दिल्या जातात.
- विनंती अपयशांमध्ये फक्त HTTP स्थिती किंवा त्रुटी वर्ग छापला जातो, कारण कस्टम
  `--api-url` मध्ये क्रेडेन्शियल्स असू शकतात.
- `.deb` आणि `.rpm` द्वारे इन्स्टॉल केलेली कमांड Python आयसोलेटेड मोडमध्ये चालवते.
  ती `PYTHONPATH`, वापरकर्ता साइट डिरेक्टरी आणि कार्यरत डिरेक्टरीमधील मॉड्यूल्सकडे दुर्लक्ष
  करते. `pip` इन्स्टॉलेशन मानक कन्सोल स्क्रिप्ट वापरते आणि ज्या वातावरणात इन्स्टॉल केले आहे
  त्याचे अनुसरण करते.
- हालचालीची स्थिती स्टेट किंवा लॉक फाइलच्या नावावरील सिम्बॉलिक लिंकचे अनुसरण न करता,
  प्रत्येक तपासणीसाठी एकदा उघडलेल्या डिरेक्टरीच्या सापेक्ष वाचली आणि लिहिली जाते.
- रिलीझ मालमत्तांमध्ये `SHA256SUMS` व्यतिरिक्त बिल्ड प्रोव्हेनन्स अटेस्टेशन्स असतात;
  [GitHub Releases मधून](#from-github-releases) पहा.

## 1.0.0 मधून अपग्रेड करणे

हे बदल 2.0.0 मध्ये समाविष्ट आहेत.

- मोठे `--max-age` दिले नसल्यास, एक तासापेक्षा जुना विक्रेता टाइमस्टॅम्प असलेला कोट
  `UNKNOWN` परत करतो. टाइमस्टॅम्प न देणाऱ्या एंडपॉइंट्सवर परिणाम होत नाही.
- `--currency` फक्त 2-16 अक्षरे किंवा अंक स्वीकारतो.
- अंक विभाजक किंवा सभोवतालच्या मोकळ्या जागा असलेल्या संख्यात्मक स्ट्रिंग नाकारल्या जातात.
- बजेटमध्ये न बसणारी पुनर्प्रयत्न प्रतीक्षा `API request timed out` ऐवजी मूळ अपयश कळवते.
- नेटिव्ह पॅकेजेस यापुढे `PYTHONPATH` चा मान राखत नाहीत.
- दहा लाख किंवा त्याहून अधिक मर्यादा कामगिरी डेटामध्ये घातांक चिन्हांकित पद्धतीऐवजी साध्या
  दशांश स्वरूपात दिसतात.

## स्थानिकीकरण

CLI मदत, पडताळणी त्रुटी आणि प्लगइन स्थिती वर्णने बंडल केलेल्या stdlib-लोड केलेल्या कॅटलॉगचा वापर करून 45 लोकेल्स (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) समर्थित करतात. निराकरण प्रथम `--lang`, नंतर `LC_ALL`, `LC_MESSAGES`, आणि `LANG` तपासते, आणि शेवटी `en` वर परत येते. Nagios स्थिती उपसर्ग (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) आणि कामगिरी डेटा सर्व लोकेल्समध्ये अपरिवर्तित राहतात.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## डेव्हलपमेंट

[mise](https://mise.jdx.dev/getting-started.html) इन्स्टॉल करा, नंतर वरील डेव्हलपमेंट सेटअप चालवा. `mise.toml` हे Python आणि uv पिन करते. डेव्हलपमेंट टूल्स `pyproject.toml` मध्ये घोषित केलेली आहेत आणि कमिट केलेल्या `uv.lock` मध्ये निश्चित केलेली आहेत.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

सेटअप नंतर कमिट हुक्स इन्स्टॉल करा:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

अवलंबित्वे अद्यतनित करण्यासाठी `mise exec -- uv add --dev <tool>` किंवा `mise exec -- uv add <dependency>` वापरा आणि `pyproject.toml` आणि `uv.lock` दोन्ही कमिट करा.

CI Linux वर Python 3.12 आणि 3.13 आणि macOS वर Python 3.13 तपासते. प्रत्येक PR मध्ये पॅकेज पडताळणी, अवलंबित्व ऑडिटिंग आणि CodeQL देखील चालते, तसेच Ubuntu वर `.deb` आणि Fedora वर `.rpm` इन्स्टॉल केले जाते. बिल्ड केलेली वितरणे CI रन्सवर `distributions` आर्टिफॅक्ट म्हणून उपलब्ध आहेत.

पॅकेज आणि CLI आवृत्ती `check_bitcoin_price/__init__.py` मधून येते. आवृत्ती वाढवण्यासाठी आणि GitHub रिलीझ मालमत्तांच्या स्वयंचलित प्रकाशनासाठी [रिलीझ प्रक्रिया](../../../CONTRIBUTING.md#releases) पहा.

## योगदान

डेव्हलपमेंट वर्कफ्लो आणि साइन-ऑफ केलेल्या कमिट आवश्यकतांसाठी [CONTRIBUTING.md](../../../CONTRIBUTING.md) पहा.

## परवाना

हा प्रकल्प MIT License अंतर्गत परवानाकृत आहे - तपशिलांसाठी [LICENSE](../../../LICENSE) फाइल पहा.

## लेखक

Thomas Vincent

## आभार

- मोफत क्रिप्टोकरन्सी API प्रदान केल्याबद्दल [CoinGecko](https://www.coingecko.com/)
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
