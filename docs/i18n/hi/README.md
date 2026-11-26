# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · **हिन्दी** · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

कॉन्फ़िगर करने योग्य चेतावनी और गंभीर सीमाओं के साथ Bitcoin की कीमत की निगरानी करने के लिए एक Nagios/Icinga प्लगइन।

## विशेषताएं

- कई मुद्राओं (USD, EUR, GBP, आदि) में Bitcoin की कीमत की निगरानी
- कॉन्फ़िगर करने योग्य चेतावनी और गंभीर सीमाएं (उच्च और निम्न)
- प्रदर्शन डेटा के साथ मानक Nagios प्लगइन आउटपुट
- CoinGecko API का उपयोग करता है (निःशुल्क, किसी API कुंजी की आवश्यकता नहीं)
- कस्टम API एंडपॉइंट के लिए समर्थन
- कॉन्फ़िगर करने योग्य टाइमआउट
- वेंडर टाइमस्टैम्प का उपयोग करके कोट की ताजगी की जांच, एक घंटे की डिफ़ॉल्ट सीमा के साथ
- दर सीमाओं और अस्थायी API विफलताओं के लिए सीमित पुनः प्रयास
- सभी प्रयासों के लिए एक समय-सीमा और प्रत्येक प्रतिक्रिया पर 64 KiB की सीमा
- निरपेक्ष 24-घंटे के प्रतिशत बदलाव पर वैकल्पिक अलर्ट
- प्रदर्शन डेटा में कीमत सीमाएं, अनुरोध अवधि और कोट की आयु

## इंस्टॉलेशन

### GitHub रिलीज़ से

[GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) से `.deb`, `.rpm`, `.tar.gz`, wheel और `SHA256SUMS` फ़ाइलें डाउनलोड करें। डाउनलोड को `sha256sum --ignore-missing --check SHA256SUMS` से सत्यापित करें। 1.0.0 के बाद के रिलीज़ में हस्ताक्षरित बिल्ड प्रोवेनेंस भी शामिल है; `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` के साथ पुष्टि करें कि कोई एसेट इस रिपॉजिटरी के रिलीज़ वर्कफ़्लो से आया है।

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

चयनित रिलीज़ से फ़ाइलनामों का उपयोग करें। नेटिव पैकेज `/usr/bin/check_bitcoin_price` और `/usr/lib/nagios/plugins/check_bitcoin_price` इंस्टॉल करते हैं; RPM पैकेज `/usr/lib64/nagios/plugins/check_bitcoin_price` भी प्रदान करता है। पैकेज किया गया कमांड Python को आइसोलेटेड मोड में चलाता है, इसलिए यह `PYTHONPATH` और कार्यशील निर्देशिका में मौजूद मॉड्यूल को अनदेखा करता है; सिस्टम पैकेज प्रबंधक Python और `requests` निर्भरताओं को हल करता है। इनमें आर्किटेक्चर-स्वतंत्र Python कोड होता है और इनके लिए ऐसे डिस्ट्रीब्यूशन की आवश्यकता होती है जो Python 3.12 या उससे नया संस्करण प्रदान करता हो।

### सोर्स से

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### डेवलपमेंट के लिए

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## उपयोग

### बुनियादी उपयोग

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### सीमाओं के साथ

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### व्यक्तिगत सीमाएं

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### अलग मुद्रा

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

### ताजगी और पुनः प्रयास बजट

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

डिफ़ॉल्ट रूप से वेंडर टाइमस्टैम्प वाला कोट अधिकतम एक घंटे पुराना होना चाहिए।
ऐसे एंडपॉइंट जो केवल कीमत लौटाते हैं, वे `--max-age` न होने पर भी उपयोग करने योग्य रहते हैं।
`--max-age` के साथ, अनुपस्थित, अमान्य, भविष्य के या पुराने वेंडर टाइमस्टैम्प
`UNKNOWN` लौटाते हैं; प्लगइन वेंडर के कोट समय के स्थान पर स्थानीय फ़ेच समय का
उपयोग नहीं करता है। आयु सीमा के ठीक बराबर का टाइमस्टैम्प स्वीकार्य रहता है।
भविष्य के टाइमस्टैम्प हमेशा अस्वीकार कर दिए जाते हैं।

डिफ़ॉल्ट रूप से एक पुनः प्रयास की अनुमति है। केवल कनेक्शन त्रुटियां, टाइमआउट और HTTP
408/429/500/502/503/504 प्रतिक्रियाओं का ही पुनः प्रयास किया जाता है। बैकऑफ़ 0.5 सेकंड से शुरू होता है और
बाद के पुनः प्रयासों के लिए दोगुना हो जाता है; `Retry-After` सेकंड और HTTP तिथियों को
प्राथमिकता दी जाती है। सभी प्रयास, प्रतिक्रिया पठन, JSON डिकोडिंग और पुनः प्रयास प्रतीक्षाएं
`--timeout` बजट साझा करती हैं। यदि कोई पुनः प्रयास प्रतीक्षा बजट में फिट नहीं हो सकती, तो वह तुरंत `UNKNOWN` लौटाती है
और टाइमआउट के बजाय उस विफलता की रिपोर्ट करती है जिसके कारण वह उत्पन्न हुई थी, जैसे `HTTP 429` या `ConnectionError`।
प्रमाणीकरण विफलताओं, अन्य स्थायी HTTP त्रुटियों, अमान्य JSON और डिकोड किए गए डेटा के 64 KiB से बड़ी
प्रतिक्रियाओं का पुनः प्रयास नहीं किया जाता है। पुनः प्रयास अक्षम करने के लिए
`--retries 0` का उपयोग करें।

### फ़ॉलबैक कोट स्रोत

CoinGecko-संगत एंडपॉइंट के साथ दोहराने योग्य `--fallback-url URL` विकल्पों का उपयोग करें।
उदाहरण के लिए, `--fallback-url https://quotes.example.org/simple/price` जोड़ें।
प्रत्येक स्रोत को उसके पुनः प्रयासों सहित शेष अनुरोध समय-सीमा का बराबर हिस्सा मिलता है।
कोई अस्थायी विफलता या उस हिस्से से अधिक लंबी पुनः प्रयास देरी अगले स्रोत पर आगे बढ़ जाती है।
TLS सत्यापन विफलताएं, स्थायी HTTP त्रुटियां और अमान्य कोट UNKNOWN लौटाते हैं।
प्रत्येक कोट प्रतिक्रिया डिकोड किए गए डेटा के 64 KiB तक सीमित है।
जब फ़ॉलबैक कॉन्फ़िगर किए जाते हैं, तो स्थिति उत्तर देने वाले स्रोत के URL को प्रिंट किए बिना उसे
`primary`, `fallback1` आदि के रूप में पहचानती है।

### लघु-अवधि बदलाव

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

निगरानी उपयोगकर्ता को स्थानीय Linux या macOS फ़ाइल सिस्टम पर एक निजी लिखने योग्य स्टेट निर्देशिका दें।
जांचों के बीच सहवर्ती `.lock` फ़ाइल को यथास्थान रखें। प्रत्येक विंडो के लिए एक
अलग स्टेट फ़ाइल का उपयोग करें। इसके भीतर मुद्राओं का स्वतंत्र इतिहास होता है।
डिफ़ॉल्ट विंडो 3600 सेकंड है। प्रत्येक मान्य कोट के लिए विंडो और आयु सीमा के भीतर एक
वेंडर टाइमस्टैम्प आवश्यक है, जो `--max-age` द्वारा कोई अन्य सीमा निर्धारित न किए जाने तक
एक घंटा होती है। प्लगइन वर्तमान कीमत की तुलना उस विंडो में सबसे पुरानी पिछली धनात्मक कीमत से करता है
और वास्तविक बीते हुए सेकंड की रिपोर्ट करता है। दोहराए गए टाइमस्टैम्प अतिरिक्त नमूने नहीं बनाते हैं।
पहला नमूना, समाप्त हो चुका इतिहास या दूषित JSON एक नई आधाररेखा शुरू करता है; तुलना योग्य नमूना
मिलने तक विंडो मेट्रिक अज्ञात रहता है। अन्य अलर्ट फिर भी लागू होते हैं।
लिखने योग्य न होने वाली स्टेट, सिंबॉलिक-लिंक स्टेट या लॉक फ़ाइल, या नवीनतम रिकॉर्ड किए गए नमूने से
पुराना कोट UNKNOWN लौटाता है। चिह्नित `bitcoin_move_window` मेट्रिक
सममित चेतावनी और गंभीर श्रेणियों का उपयोग करता है। सीमा पर समानता होने पर अलर्ट नहीं होता है।

प्लगइन प्रति जांच एक बार स्टेट निर्देशिका खोलता है और उसके सापेक्ष काम करता है, इसलिए
जांच के दौरान बदला गया कोई पथ घटक लॉक, रीड या राइट को पुनर्निर्देशित नहीं कर सकता है।
जांच शुरू होने पर पथ के निर्देशिका भाग में सिंबॉलिक लिंक का अनुसरण किया जाता है,
जिससे macOS पर `/var` जैसे प्लेटफ़ॉर्म लिंक उपयोग करने योग्य बने रहते हैं। इसलिए
स्टेट निर्देशिका और उसके पूर्वज अन्य उपयोगकर्ताओं द्वारा लिखने योग्य नहीं होने चाहिए।
स्टेट और लॉक फ़ाइलें 0600 मोड के साथ बनाई जाती हैं।

### दैनिक प्रतिशत बदलाव

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

परिवर्तन सीमाएं चयनित मुद्रा में CoinGecko के चिह्नित 24-घंटे के प्रतिशत परिवर्तन के निरपेक्ष मान को मापती हैं।
ठीक सीमा पर होने वाला परिवर्तन अलर्ट नहीं करता है। यदि दोनों सीमाएं दी गई हैं, तो चेतावनी सीमा गंभीर सीमा से अधिक नहीं होनी चाहिए।
आवश्यक परिवर्तन डेटा अनुपस्थित या अमान्य होने पर `UNKNOWN` लौटता है। कीमत और परिवर्तन अलर्ट को संयोजित किया जा सकता है;
उच्चतम गंभीरता जीतती है, और गंभीरता समान होने पर कीमत को प्राथमिकता मिलती है।

## कमांड लाइन विकल्प

| विकल्प | विवरण |
|--------|-------------|
| `-w`, `--warning` | चेतावनी सीमा श्रेणी (प्रारूप: LOW:HIGH) |
| `-c`, `--critical` | गंभीर सीमा श्रेणी (प्रारूप: LOW:HIGH) |
| `--warning-low` | निम्न कीमत के लिए चेतावनी सीमा |
| `--warning-high` | उच्च कीमत के लिए चेतावनी सीमा |
| `--critical-low` | निम्न कीमत के लिए गंभीर सीमा |
| `--critical-high` | उच्च कीमत के लिए गंभीर सीमा |
| `--currency` | 2-16 अक्षरों या अंकों का मुद्रा कोड (डिफ़ॉल्ट: usd) |
| `--timeout` | सेकंड में कुल API अनुरोध/पुनः प्रयास बजट, भिन्नात्मक मानों सहित (डिफ़ॉल्ट: 10) |
| `--retries` | अतिरिक्त अस्थायी प्रयास, 0–5 (डिफ़ॉल्ट: 1) |
| `--max-age` | सेकंड में अधिकतम वेंडर कोट आयु और टाइमस्टैम्प की आवश्यकता; टाइमस्टैम्प वाले कोट का डिफ़ॉल्ट 3600 है |
| `--warning-change` | निरपेक्ष 24-घंटे के प्रतिशत बदलाव के लिए चेतावनी सीमा |
| `--critical-change` | निरपेक्ष 24-घंटे के प्रतिशत बदलाव के लिए गंभीर सीमा |
| `--api-url` | प्राथमिक API URL |
| `--fallback-url` | अतिरिक्त संगत एंडपॉइंट; वरीयता क्रम में दोहराएं |
| `--state-file` | JSON बदलाव इतिहास फ़ाइल |
| `--move-window` | सेकंड में बदलाव विंडो (डिफ़ॉल्ट: 3600) |
| `--warning-move`, `--critical-move` | प्रतिशत में निरपेक्ष विंडो बदलाव सीमाएं |
| `-v`, `--verbose` | विस्तृत आउटपुट सक्षम करें |
| `-V`, `--version` | संस्करण दिखाएं |
| `-h`, `--help` | सहायता संदेश दिखाएं |

## Nagios कॉन्फ़िगरेशन

### कमांड परिभाषा

Nagios संसाधन मैक्रो `$USER1$` को प्लगइन निर्देशिका पर सेट करें (नेटिव पैकेज `/usr/lib/nagios/plugins` का उपयोग करते हैं)। अपने Nagios कमांड कॉन्फ़िगरेशन में जोड़ें:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### सेवा परिभाषा

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

### Icinga2 कॉन्फ़िगरेशन

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

## निकास कोड

अमान्य तर्क, गैर-धनात्मक टाइमआउट, अमान्य सीमा श्रेणियां और विकृत API कीमतें
`UNKNOWN` (निकास 3) लौटाती हैं। सीमाएं परिमित, गैर-ऋणात्मक संख्याएं होनी चाहिए,
जिनमें प्रत्येक निम्न सीमा अपनी उच्च सीमा से बड़ी न हो। मुद्रा 2-16 अक्षरों या अंकों की होनी चाहिए।
API से संपर्क करने से पहले ही अमान्य कॉन्फ़िगरेशन को अस्वीकार कर दिया जाता है।
कीमतें परिमित और गैर-ऋणात्मक होनी चाहिए, जिन्हें JSON संख्याओं या `"43521.5"` जैसी
सामान्य दशमलव स्ट्रिंग के रूप में दिया गया हो। अनुरोधित मुद्रा के बिना वाली प्रतिक्रिया
उसका नाम बताती है, उदाहरण के लिए `Response has no EUR price`। अमान्य प्रतिक्रियाएं
प्रदर्शन डेटा उत्सर्जित नहीं करती हैं। विस्तृत निदान stderr पर जाते हैं
ताकि stdout में केवल एक निगरानी स्थिति पंक्ति रहे।

| कोड | स्थिति | विवरण |
|------|--------|-------------|
| 0 | OK | कीमत स्वीकार्य सीमा के भीतर है |
| 1 | WARNING | कीमत ने चेतावनी सीमा पार कर ली है |
| 2 | CRITICAL | कीमत ने गंभीर सीमा पार कर ली है |
| 3 | UNKNOWN | त्रुटि हुई (API विफलता, टाइमआउट, आदि) |

## प्रदर्शन डेटा

प्लगइन मानक Nagios प्रारूप में प्रदर्शन डेटा आउटपुट करता है:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

कीमत प्रदर्शन डेटा में कॉन्फ़िगर की गई चेतावनी/गंभीर श्रेणियां और शून्य का न्यूनतम मान शामिल होता है।
सीमाएं पूर्ण दशमलव अंकन में प्रिंट की जाती हैं, कभी भी पूर्णांकित या घातांक रूप में नहीं,
ताकि `14500000:16250000` जैसे बड़े मान पार्स करने योग्य बने रहें। अनुरोध समय में सभी प्रयास और बैकऑफ़ शामिल होते हैं।
कोट की आयु केवल तभी उत्सर्जित की जाती है जब वेंडर एक मान्य टाइमस्टैम्प प्रदान करता है; उपलब्ध होने पर दैनिक परिवर्तन
उत्सर्जित किया जाता है। परिवर्तन श्रेणियां शून्य के आसपास सममित होती हैं। अमान्य या पुराना डेटा
बिना कीमत प्रदर्शन डेटा के `UNKNOWN` उत्पन्न करता है। इन मेट्रिक्स का उपयोग
PNP4Nagios, Grafana या InfluxDB जैसे ग्राफ़िंग टूल के साथ किया जा सकता है।

## API

यह प्लगइन डिफ़ॉल्ट रूप से [CoinGecko API](https://www.coingecko.com/en/api) का उपयोग करता है, जो निःशुल्क है और इसके लिए किसी API कुंजी की आवश्यकता नहीं है। दर सीमाएं लागू होती हैं।

कस्टम एंडपॉइंट को इसी प्रतिक्रिया आकार का उपयोग करना होगा: कीमत के लिए `bitcoin.<currency>`,
UNIX टाइमस्टैम्प सेकंड के लिए `bitcoin.last_updated_at` और चिह्नित दैनिक प्रतिशत बदलाव के लिए
`bitcoin.<currency>_24h_change`। जब `--max-age` और परिवर्तन सीमाएं अनुपस्थित हों,
तो केवल कीमत आवश्यक होती है। यदि कोई टाइमस्टैम्प मौजूद है, तो उसकी फिर भी जांच की जाती है:
वह भविष्य का नहीं होना चाहिए और एक घंटे से अधिक पुराना नहीं होना चाहिए। डिकोड की गई प्रतिक्रिया 64 KiB में समा जानी चाहिए।

समर्थित मुद्राओं में शामिल हैं: usd, eur, gbp, jpy, aud, cad, chf, cny, और कई अन्य।

## सुरक्षा

नीचे दिए गए उपाय वर्तमान कोड में लागू किए गए हैं। वे यह सीमित करते हैं कि कोई अनुचित व्यवहार करने वाला एंडपॉइंट या स्थानीय उपयोगकर्ता
निगरानी होस्ट के साथ क्या कर सकता है; वे स्वयं कोट को विश्वसनीय नहीं बनाते हैं।

- HTTPS प्रमाणपत्रों को `requests` डिफ़ॉल्ट के साथ सत्यापित किया जाता है, और कोई भी विकल्प
  सत्यापन को अक्षम नहीं करता है। सादा `http://` उपयोग करने वाले कस्टम `--api-url` में ऐसी कोई सुरक्षा नहीं होती है।
- DNS, कनेक्शन, रीड्स, पुनः प्रयास और बैकऑफ़ `--timeout` समय-सीमा साझा करते हैं।
  धीरे-धीरे डेटा भेजने वाला कोई पीयर इसे बढ़ा नहीं सकता है।
- प्रत्येक प्रतिक्रिया डीकम्प्रेशन के बाद 64 KiB तक सीमित है, और रीडायरेक्ट बॉडी को
  बिना पढ़े छोड़ दिया जाता है।
- अनुरोध विफलताएं केवल HTTP स्थिति या त्रुटि वर्ग प्रिंट करती हैं, क्योंकि एक कस्टम
  `--api-url` में क्रेडेंशियल हो सकते हैं।
- `.deb` और `.rpm` द्वारा इंस्टॉल किया गया कमांड Python को आइसोलेटेड मोड में चलाता है।
  यह `PYTHONPATH`, उपयोगकर्ता साइट निर्देशिका और कार्यशील निर्देशिका में मौजूद मॉड्यूल को अनदेखा करता है।
  `pip` इंस्टॉलेशन मानक कंसोल स्क्रिप्ट का उपयोग करता है और उस वातावरण का अनुसरण करता है जिसमें वह इंस्टॉल किया गया है।
- बदलाव स्टेट को प्रति जांच एक बार खोली गई निर्देशिका के सापेक्ष, स्टेट या लॉक फ़ाइल नाम पर
  किसी सिंबॉलिक लिंक का अनुसरण किए बिना पढ़ा और लिखा जाता है।
- रिलीज़ एसेट में `SHA256SUMS` के अतिरिक्त बिल्ड प्रोवेनेंस प्रमाणन भी होते हैं;
  [GitHub रिलीज़ से](#from-github-releases) देखें।

## 1.0.0 से अपग्रेड करना

ये बदलाव 2.0.0 में शामिल हैं।

- एक घंटे से अधिक पुराने वेंडर टाइमस्टैम्प वाला कोट `UNKNOWN` लौटाता है, जब तक कि कोई
  बड़ा `--max-age` न दिया गया हो। जो एंडपॉइंट कोई टाइमस्टैम्प नहीं लौटाते हैं, वे अप्रभावित रहते हैं।
- `--currency` केवल 2-16 अक्षर या अंक स्वीकार करता है।
- अंक विभाजकों या आसपास के रिक्त स्थानों वाली संख्यात्मक स्ट्रिंग्स को अस्वीकार कर दिया जाता है।
- ऐसी पुनः प्रयास प्रतीक्षा जो बजट में फिट नहीं होती है, वह `API request timed out` के बजाय
  अंतर्निहित विफलता की रिपोर्ट करती है।
- नेटिव पैकेज अब `PYTHONPATH` का सम्मान नहीं करते हैं।
- एक मिलियन या उससे अधिक की सीमाएं प्रदर्शन डेटा में घातांक अंकन के बजाय सामान्य
  दशमलव के रूप में दिखाई देती हैं।

## स्थानीयकरण

बंडल किए गए stdlib-लोड किए गए कैटलॉग का उपयोग करके CLI सहायता, सत्यापन त्रुटियां और प्लगइन स्थिति विवरण 45 लोकेल (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) का समर्थन करते हैं। रिज़ॉल्यूशन `--lang`, फिर `LC_ALL`, `LC_MESSAGES`, और `LANG` की जांच करता है, और अंत में `en` पर वापस आता है। Nagios स्थिति उपसर्ग (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) और प्रदर्शन डेटा सभी लोकेल में अपरिवर्तित रहते हैं।

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## डेवलपमेंट

[mise](https://mise.jdx.dev/getting-started.html) इंस्टॉल करें, फिर ऊपर दिया गया डेवलपमेंट सेटअप चलाएं। `mise.toml` Python और uv को पिन करता है। डेवलपमेंट टूल `pyproject.toml` में घोषित किए गए हैं और कमिट की गई `uv.lock` में हल किए गए हैं।

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

सेटअप के बाद कमिट हुक इंस्टॉल करें:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

निर्भरताओं को अपडेट करने के लिए `mise exec -- uv add --dev <tool>` या `mise exec -- uv add <dependency>` का उपयोग करें और `pyproject.toml` तथा `uv.lock` दोनों को कमिट करें।

CI Linux पर Python 3.12 और 3.13 तथा macOS पर Python 3.13 की जांच करता है। प्रत्येक PR पैकेज सत्यापन, निर्भरता ऑडिटिंग और CodeQL भी चलाता है, तथा Ubuntu पर `.deb` और Fedora पर `.rpm` इंस्टॉल करता है। निर्मित वितरण CI रन पर `distributions` आर्टिफैक्ट के रूप में उपलब्ध हैं।

पैकेज और CLI संस्करण `check_bitcoin_price/__init__.py` से आता है। संस्करण बढ़ाने और GitHub रिलीज़ एसेट के स्वचालित प्रकाशन के लिए [रिलीज़ प्रक्रिया](../../../CONTRIBUTING.md#releases) देखें।

## योगदान

डेवलपमेंट वर्कफ़्लो और साइन-ऑफ़ कमिट आवश्यकताओं के लिए [CONTRIBUTING.md](../../../CONTRIBUTING.md) देखें।

## लाइसेंस

यह प्रोजेक्ट MIT License के अंतर्गत लाइसेंस प्राप्त है - विवरण के लिए [LICENSE](../../../LICENSE) फ़ाइल देखें।

## लेखक

Thomas Vincent

## आभार

- निःशुल्क क्रिप्टोकरेंसी API प्रदान करने के लिए [CoinGecko](https://www.coingecko.com/)
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
