# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · **తెలుగు** · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

కాన్ఫిగర్ చేయగల warning మరియు critical థ్రెషోల్డ్‌లతో Bitcoin ధరను పర్యవేక్షించే Nagios/Icinga ప్లగ్ఇన్.

## ఫీచర్లు

- బహుళ కరెన్సీలలో (USD, EUR, GBP, మొదలైనవి) Bitcoin ధరను పర్యవేక్షించడం
- కాన్ఫిగర్ చేయగల warning మరియు critical థ్రెషోల్డ్‌లు (అధిక మరియు అల్ప)
- పనితీరు డేటాతో కూడిన ప్రామాణిక Nagios ప్లగ్ఇన్ అవుట్‌పుట్
- CoinGecko API ని ఉపయోగిస్తుంది (ఉచితం, API కీ అవసరం లేదు)
- కస్టమ్ API ఎండ్‌పాయింట్‌లకు మద్దతు
- కాన్ఫిగర్ చేయగల గడువు
- ఒక గంట డిఫాల్ట్ పరిమితితో వెండర్ టైమ్‌స్టాంప్‌లను ఉపయోగించి కోట్ తాజాదనం తనిఖీలు
- రేటు పరిమితులు మరియు తాత్కాలిక API వైఫల్యాల కోసం పరిమిత రీట్రైలు
- అన్ని ప్రయత్నాలకు కలిపి ఒకే గడువు మరియు ప్రతి ప్రతిస్పందనపై 64 KiB పరిమితి
- 24 గంటల సంపూర్ణ శాతం కదలికపై ఐచ్ఛిక అలర్ట్‌లు
- పనితీరు డేటాలో ధర థ్రెషోల్డ్‌లు, అభ్యర్థన వ్యవధి మరియు కోట్ వయస్సు

## ఇన్‌స్టాలేషన్

### GitHub Releases నుండి

[GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) నుండి `.deb`, `.rpm`, `.tar.gz`, wheel, మరియు `SHA256SUMS` ఫైళ్లను డౌన్‌లోడ్ చేయండి. `sha256sum --ignore-missing --check SHA256SUMS` తో డౌన్‌లోడ్‌ను ధృవీకరించండి. 1.0.0 తర్వాత విడుదలలు సంతకం చేసిన బిల్డ్ ప్రొవెనెన్స్‌ను కూడా కలిగి ఉంటాయి; `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` తో ఆ ఫైల్ ఈ రిపోజిటరీ యొక్క రిలీజ్ వర్క్‌ఫ్లో నుండి వచ్చిందని నిర్ధారించండి.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

ఎంచుకున్న రిలీజ్ నుండి ఫైల్ పేర్లను ఉపయోగించండి. నేటివ్ ప్యాకేజీలు `/usr/bin/check_bitcoin_price` మరియు `/usr/lib/nagios/plugins/check_bitcoin_price` ను ఇన్‌స్టాల్ చేస్తాయి; RPM `/usr/lib64/nagios/plugins/check_bitcoin_price` ను కూడా అందిస్తుంది. ప్యాకేజ్ చేయబడిన కమాండ్ Python ను ఐసోలేటెడ్ మోడ్‌లో నడుపుతుంది, కాబట్టి ఇది `PYTHONPATH` మరియు వర్కింగ్ డైరెక్టరీలోని మాడ్యూళ్లను విస్మరిస్తుంది; సిస్టమ్ ప్యాకేజీ మేనేజర్ Python మరియు `requests` డిపెండెన్సీలను పరిష్కరిస్తుంది. ఇవి ఆర్కిటెక్చర్-స్వతంత్ర Python కోడ్‌ను కలిగి ఉంటాయి మరియు Python 3.12 లేదా అంతకంటే కొత్త వెర్షన్‌ను అందించే డిస్ట్రిబ్యూషన్ అవసరం.

### సోర్స్ నుండి

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### డెవలప్‌మెంట్ కోసం

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## వినియోగం

### ప్రాథమిక వినియోగం

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### థ్రెషోల్డ్‌లతో

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### వ్యక్తిగత థ్రెషోల్డ్‌లు

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### వేరే కరెన్సీ

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### కస్టమ్ గడువు

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### తాజాదనం మరియు రీట్రై బడ్జెట్

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

వెండర్ టైమ్‌స్టాంప్‌ను కలిగి ఉన్న కోట్ డిఫాల్ట్‌గా గరిష్టంగా ఒక గంట పాతది మాత్రమే అయి ఉండాలి.
`--max-age` లేనప్పుడు కేవలం ధరను మాత్రమే తిరిగి ఇచ్చే ఎండ్‌పాయింట్‌లు ఉపయోగకరంగానే ఉంటాయి.
`--max-age` ఉన్నప్పుడు, లేని, చెల్లని, భవిష్యత్తు లేదా పాతబడిన వెండర్ టైమ్‌స్టాంప్‌లు
`UNKNOWN` ను తిరిగి ఇస్తాయి; వెండర్ కోట్ సమయానికి బదులుగా లోకల్ ఫెచ్ సమయాన్ని ప్లగ్ఇన్ ప్రత్యామ్నాయంగా ఉపయోగించదు. వయస్సు పరిమితి వద్ద ఖచ్చితంగా ఉన్న టైమ్‌స్టాంప్ ఆమోదయోగ్యంగా ఉంటుంది. భవిష్యత్తు టైమ్‌స్టాంప్‌లు ఎల్లప్పుడూ తిరస్కరించబడతాయి.

డిఫాల్ట్ ఒక రీట్రైకి అనుమతిస్తుంది. కేవలం కనెక్షన్ లోపాలు, టైమ్‌అవుట్‌లు మరియు HTTP
408/429/500/502/503/504 ప్రతిస్పందనలు మాత్రమే రీట్రై చేయబడతాయి. బ్యాక్‌ఆఫ్ 0.5 సెకన్లతో మొదలై
తదుపరి రీట్రైలకు రెట్టింపు అవుతుంది; `Retry-After` సెకన్లు మరియు HTTP తేదీలకు
ప్రాధాన్యత ఉంటుంది. అన్ని ప్రయత్నాలు, ప్రతిస్పందన రీడ్‌లు, JSON డీకోడింగ్ మరియు రీట్రై వేచి ఉండే సమయాలు
`--timeout` బడ్జెట్‌ను పంచుకుంటాయి. బడ్జెట్‌లో ఇమడలేని రీట్రై వేచి ఉండే సమయం వెంటనే `UNKNOWN` ను తిరిగి ఇస్తుంది
మరియు టైమ్‌అవుట్‌ను కాకుండా దానికి కారణమైన వైఫల్యాన్ని (ఉదాహరణకు `HTTP 429` లేదా `ConnectionError`)
నివేదిస్తుంది. ప్రామాణీకరణ వైఫల్యాలు, ఇతర శాశ్వత HTTP లోపాలు, చెల్లని
JSON మరియు 64 KiB కంటే పెద్ద డీకోడ్ చేసిన డేటా ప్రతిస్పందనలు రీట్రై చేయబడవు. రీట్రైలను నిలిపివేయడానికి
`--retries 0` ఉపయోగించండి.

### ఫాల్‌బ్యాక్ కోట్ మూలాలు

CoinGecko-అనుకూల ఎండ్‌పాయింట్‌లతో పునరావృతం చేయగల `--fallback-url URL` ఆప్షన్‌లను ఉపయోగించండి.
ఉదాహరణకు, `--fallback-url https://quotes.example.org/simple/price` ని జోడించండి.
ప్రతి మూలానికి దాని రీట్రైలతో సహా మిగిలిన అభ్యర్థన గడువులో సమాన వాటా లభిస్తుంది. తాత్కాలిక
వైఫల్యం లేదా ఆ వాటా కంటే ఎక్కువ రీట్రై ఆలస్యం తదుపరి మూలానికి మారుతుంది. TLS ధృవీకరణ
వైఫల్యాలు, శాశ్వత HTTP లోపాలు మరియు చెల్లని కోట్‌లు UNKNOWN ను తిరిగి ఇస్తాయి. ప్రతి కోట్
ప్రతిస్పందన 64 KiB డీకోడ్ చేసిన డేటాకు పరిమితం చేయబడింది. ఫాల్‌బ్యాక్‌లు కాన్ఫిగర్ చేయబడినప్పుడు,
దాని URL ను ప్రింట్ చేయకుండానే సమాధానమిచ్చే మూలాన్ని `primary`, `fallback1` మరియు అలాగే తదుపరి వాటిగా
స్థితి గుర్తిస్తుంది.

### స్వల్ప-వ్యవధి కదలిక

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

లోకల్ Linux లేదా macOS ఫైల్‌సిస్టమ్‌పై మానిటరింగ్ యూజర్‌కు ఒక ప్రైవేట్ వ్రాయదగిన స్టేట్ డైరెక్టరీని ఇవ్వండి. చెక్‌ల మధ్య సహోదర `.lock` ఫైల్‌ను అలాగే ఉంచండి. ప్రతి విండోకు ప్రత్యేక స్టేట్ ఫైల్‌ను ఉపయోగించండి. దాని లోపల కరెన్సీలకు స్వతంత్ర చరిత్రలు ఉంటాయి.
డిఫాల్ట్ విండో 3600 సెకన్లు. ప్రతి చెల్లుబాటు అయ్యే కోట్‌కు విండో మరియు వయస్సు పరిమితిలోపు
వెండర్ టైమ్‌స్టాంప్ అవసరం, `--max-age` మరొకటి సెట్ చేయకపోతే అది ఒక గంట ఉంటుంది. ప్లగ్ఇన్ ప్రస్తుత
ధరను ఆ విండోలోని అత్యంత పాత మునుపటి సానుకూల ధరతో పోల్చి, గడిచిన
వాస్తవ సెకన్లను నివేదిస్తుంది. పునరావృత టైమ్‌స్టాంప్‌లు అదనపు నమూనాలను సృష్టించవు.
మొదటి నమూనా, గడువు ముగిసిన చరిత్ర, లేదా చెడిపోయిన JSON కొత్త బేస్‌లైన్‌ను ప్రారంభిస్తుంది;
పోల్చదగిన నమూనా ఉండే వరకు విండో మెట్రిక్ unknown గా ఉంటుంది. ఇతర అలర్ట్‌లు ఇప్పటికీ
వర్తిస్తాయి. వ్రాయలేని స్టేట్, సింబాలిక్-లింక్ స్టేట్ లేదా లాక్ ఫైల్, లేదా కొత్తగా రికార్డ్ చేసిన
నమూనా కంటే పాత కోట్ UNKNOWN ను తిరిగి ఇస్తుంది. సంతకం చేసిన `bitcoin_move_window` మెట్రిక్
సుష్ట warning మరియు critical పరిధులను ఉపయోగిస్తుంది. పరిమితి వద్ద సమానత్వం అలర్ట్ చేయదు.

ప్లగ్ఇన్ ప్రతి చెక్‌కు ఒకసారి స్టేట్ డైరెక్టరీని తెరిచి దానికి సాపేక్షంగా పనిచేస్తుంది, కాబట్టి
చెక్ సమయంలో మార్చబడిన పాత్ భాగం లాక్, రీడ్ లేదా రైట్‌ను మళ్లించలేదు. చెక్ ప్రారంభమైనప్పుడు
పాత్ యొక్క డైరెక్టరీ భాగంలోని సింబాలిక్ లింక్‌లు అనుసరించబడతాయి, ఇది macOS లోని `/var` వంటి
ప్లాట్‌ఫారమ్ లింక్‌లను ఉపయోగపడేలా ఉంచుతుంది. కాబట్టి స్టేట్ డైరెక్టరీ మరియు దాని పూర్వీకులు ఇతర
వినియోగదారులచే వ్రాయదగినవి కాకూడదు. స్టేట్ మరియు లాక్ ఫైల్‌లు మోడ్ 0600 తో సృష్టించబడతాయి.

### రోజువారీ శాతం కదలిక

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

మార్పు థ్రెషోల్డ్‌లు ఎంచుకున్న కరెన్సీలో CoinGecko యొక్క సంతకం చేసిన 24-గంటల శాతం
మార్పు యొక్క సంపూర్ణ విలువను కొలుస్తాయి. సరిగ్గా థ్రెషోల్డ్ వద్ద ఉన్న మార్పు అలర్ట్ చేయదు.
రెండు థ్రెషోల్డ్‌లు అందించబడితే, warning విలువ critical కంటే మించకూడదు.
అవసరమైన మార్పు డేటా లేకపోవడం లేదా చెల్లకపోవడం `UNKNOWN` ను తిరిగి ఇస్తుంది. ధర మరియు మార్పు
అలర్ట్‌లను కలపవచ్చు; అత్యధిక తీవ్రత గెలుస్తుంది, తీవ్రతలు సమానంగా ఉన్నప్పుడు ధరకు ప్రాధాన్యత
ఉంటుంది.

## కమాండ్ లైన్ ఆప్షన్లు

| ఆప్షన్ | వివరణ |
|--------|-------------|
| `-w`, `--warning` | Warning థ్రెషోల్డ్ పరిధి (ఫార్మాట్: LOW:HIGH) |
| `-c`, `--critical` | Critical థ్రెషోల్డ్ పరిధి (ఫార్మాట్: LOW:HIGH) |
| `--warning-low` | తక్కువ ధర కోసం Warning థ్రెషోల్డ్ |
| `--warning-high` | అధిక ధర కోసం Warning థ్రెషోల్డ్ |
| `--critical-low` | తక్కువ ధర కోసం Critical థ్రెషోల్డ్ |
| `--critical-high` | అధిక ధర కోసం Critical థ్రెషోల్డ్ |
| `--currency` | 2-16 అక్షరాలు లేదా అంకెల కరెన్సీ కోడ్ (డిఫాల్ట్: usd) |
| `--timeout` | సెకన్లలో మొత్తం API అభ్యర్థన/రీట్రై బడ్జెట్, భిన్న విలువలతో సహా (డిఫాల్ట్: 10) |
| `--retries` | అదనపు తాత్కాలిక ప్రయత్నాలు, 0–5 (డిఫాల్ట్: 1) |
| `--max-age` | సెకన్లలో గరిష్ట వెండర్ కోట్ వయస్సు మరియు టైమ్‌స్టాంప్ అవసరం; టైమ్‌స్టాంప్ ఉన్న కోట్‌లు డిఫాల్ట్‌గా 3600 |
| `--warning-change` | 24 గంటల సంపూర్ణ శాతం కదలిక కోసం Warning పరిమితి |
| `--critical-change` | 24 గంటల సంపూర్ణ శాతం కదలిక కోసం Critical పరిమితి |
| `--api-url` | ప్రాథమిక API URL |
| `--fallback-url` | అదనపు అనుకూల ఎండ్‌పాయింట్; ప్రాధాన్యత క్రమంలో పునరావృతం చేయండి |
| `--state-file` | JSON కదలిక చరిత్ర ఫైల్ |
| `--move-window` | సెకన్లలో కదలిక విండో (డిఫాల్ట్: 3600) |
| `--warning-move`, `--critical-move` | శాతంలో సంపూర్ణ విండో కదలిక థ్రెషోల్డ్‌లు |
| `-v`, `--verbose` | వివరమైన అవుట్‌పుట్‌ను ప్రారంభించండి |
| `-V`, `--version` | వెర్షన్‌ను చూపించు |
| `-h`, `--help` | సహాయ సందేశాన్ని చూపించు |

## Nagios కాన్ఫిగరేషన్

### కమాండ్ నిర్వచనం

Nagios రిసోర్స్ మాక్రో `$USER1$` ని ప్లగ్ఇన్ డైరెక్టరీకి సెట్ చేయండి (నేటివ్ ప్యాకేజీలు `/usr/lib/nagios/plugins` ని ఉపయోగిస్తాయి). మీ Nagios కమాండ్స్ కాన్ఫిగరేషన్‌కు జోడించండి:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### సర్వీస్ నిర్వచనం

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

### Icinga2 కాన్ఫిగరేషన్

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

## ఎగ్జిట్ కోడ్‌లు

చెల్లని ఆర్గ్యుమెంట్లు, ధనాత్మకం కాని టైమ్‌అవుట్‌లు, చెల్లని థ్రెషోల్డ్ పరిధులు మరియు తప్పుగా ఫార్మాట్ చేయబడిన
API ధరలు `UNKNOWN` (ఎగ్జిట్ 3) ను తిరిగి ఇస్తాయి. థ్రెషోల్డ్‌లు పరిమితమైన, రుణాత్మకం కాని
సంఖ్యలుగా ఉండాలి, ప్రతి దిగువ పరిమితి దాని ఎగువ పరిమితి కంటే ఎక్కువగా ఉండకూడదు. కరెన్సీ తప్పనిసరిగా
2-16 అక్షరాలు లేదా అంకెలతో ఉండాలి. API ని సంప్రదించడానికి ముందే చెల్లని కాన్ఫిగరేషన్ తిరస్కరించబడుతుంది.
ధరలు పరిమితమైనవి మరియు రుణాత్మకం కానివిగా ఉండాలి, ఇవి JSON సంఖ్యలుగా లేదా సాధారణ
దశాంశ స్ట్రింగ్‌లుగా (ఉదాహరణకు `"43521.5"`) ఇవ్వబడాలి. అభ్యర్థించిన కరెన్సీ లేని ప్రతిస్పందన
దాని పేరును చూపుతుంది, ఉదాహరణకు `Response has no EUR price`. చెల్లని ప్రతిస్పందనలు
పనితీరు డేటాను విడుదల చేయవు. వివరమైన డయాగ్నస్టిక్స్ stderr కు వెళ్తాయి,
తద్వారా stdout లో ఒకే ఒక మానిటరింగ్ స్థితి లైన్ ఉంటుంది.

| కోడ్ | స్థితి | వివరణ |
|------|--------|-------------|
| 0 | OK | ధర ఆమోదయోగ్యమైన పరిధిలో ఉంది |
| 1 | WARNING | ధర warning థ్రెషోల్డ్‌ను దాటింది |
| 2 | CRITICAL | ధర critical థ్రెషోల్డ్‌ను దాటింది |
| 3 | UNKNOWN | లోపం సంభవించింది (API వైఫల్యం, టైమ్‌అవుట్, మొదలైనవి) |

## పనితీరు డేటా

ప్లగ్ఇన్ ప్రామాణిక Nagios ఫార్మాట్‌లో పనితీరు డేటాను అవుట్‌పుట్ చేస్తుంది:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

ధర పనితీరు డేటాలో కాన్ఫిగర్ చేయబడిన warning/critical పరిధులు మరియు
కనీసం సున్నా ఉంటాయి. థ్రెషోల్డ్‌లు ఎప్పుడూ రౌండ్ చేయబడకుండా లేదా ఎక్స్‌పోనెంట్ రూపంలో కాకుండా
పూర్తి దశాంశ సంజ్ఞామానంలో ముద్రించబడతాయి, కాబట్టి `14500000:16250000` వంటి పెద్ద విలువలు పార్స్ చేయడానికి అనువుగా ఉంటాయి. అభ్యర్థన సమయంలో అన్ని ప్రయత్నాలు మరియు బ్యాక్‌ఆఫ్ ఉంటాయి. వెండర్ చెల్లుబాటు అయ్యే టైమ్‌స్టాంప్‌ను అందించినప్పుడు మాత్రమే కోట్ వయస్సు విడుదల చేయబడుతుంది; అందుబాటులో ఉన్నప్పుడు రోజువారీ మార్పు విడుదల చేయబడుతుంది. మార్పు పరిధులు సున్నా చుట్టూ సుష్టంగా ఉంటాయి. చెల్లని లేదా పాతబడిన డేటా ధర పనితీరు డేటా లేకుండా `UNKNOWN` ను ఉత్పత్తి చేస్తుంది. ఈ మెట్రిక్‌లను PNP4Nagios, Grafana, లేదా InfluxDB వంటి గ్రాఫింగ్ సాధనాలతో ఉపయోగించవచ్చు.

## API

ఈ ప్లగ్ఇన్ డిఫాల్ట్‌గా [CoinGecko API](https://www.coingecko.com/en/api) ని ఉపయోగిస్తుంది, ఇది ఉచితం మరియు API కీ అవసరం లేదు. రేటు పరిమితులు వర్తిస్తాయి.

కస్టమ్ ఎండ్‌పాయింట్‌లు తప్పనిసరిగా ఇదే ప్రతిస్పందన రూపాన్ని ఉపయోగించాలి: ధర కోసం `bitcoin.<currency>`,
UNIX టైమ్‌స్టాంప్ సెకన్ల కోసం `bitcoin.last_updated_at`, మరియు
సంతకం చేసిన రోజువారీ శాతం కదలిక కోసం `bitcoin.<currency>_24h_change`. `--max-age` మరియు మార్పు థ్రెషోల్డ్‌లు లేనప్పుడు కేవలం ధర మాత్రమే అవసరం. ఉన్న టైమ్‌స్టాంప్ ఇప్పటికీ తనిఖీ చేయబడుతుంది: అది భవిష్యత్తులో ఉండకూడదు లేదా ఒక గంట కంటే పాతది కాకూడదు. డీకోడ్ చేయబడిన ప్రతిస్పందన 64 KiB లోపు సరిపోవాలి.

మద్దతు ఉన్న కరెన్సీలలో ఇవి ఉన్నాయి: usd, eur, gbp, jpy, aud, cad, chf, cny, మరియు మరెన్నో.

## భద్రత

దిగువ ఉన్న చర్యలు ప్రస్తుత కోడ్‌లో అమలు చేయబడ్డాయి. తప్పుగా ప్రవర్తించే ఎండ్‌పాయింట్ లేదా లోకల్ యూజర్
మానిటరింగ్ హోస్ట్‌కు ఏమి చేయగలరో అవి పరిమితం చేస్తాయి; అవి కోట్‌ను విశ్వసనీయమైనదిగా చేయవు.

- `requests` డిఫాల్ట్‌లతో HTTPS సర్టిఫికెట్లు ధృవీకరించబడతాయి మరియు ఏ ఆప్షన్ కూడా
  ధృవీకరణను నిలిపివేయదు. సాధారణ `http://` ని ఉపయోగించే కస్టమ్ `--api-url` కి అటువంటి
  రక్షణ ఉండదు.
- DNS, కనెక్షన్, రీడ్‌లు, రీట్రైలు మరియు బ్యాక్‌ఆఫ్ `--timeout` గడువును పంచుకుంటాయి. డేటాను
  నెమ్మదిగా పంపే పీర్ దానిని పొడిగించలేదు.
- డికంప్రెషన్ తర్వాత ప్రతి ప్రతిస్పందన 64 KiB కి పరిమితం చేయబడింది మరియు రీడైరెక్ట్ బాడీలు
  చదవకుండానే విస్మరించబడతాయి.
- కస్టమ్ `--api-url` లో క్రెడెన్షియల్స్ ఉండవచ్చు కాబట్టి, అభ్యర్థన వైఫల్యాలు కేవలం HTTP స్థితి లేదా లోపం తరగతిని మాత్రమే ప్రింట్ చేస్తాయి.
- `.deb` మరియు `.rpm` ద్వారా ఇన్‌స్టాల్ చేయబడిన కమాండ్ Python ను ఐసోలేటెడ్ మోడ్‌లో నడుపుతుంది.
  ఇది `PYTHONPATH`, యూజర్ సైట్ డైరెక్టరీ మరియు వర్కింగ్ డైరెక్టరీలోని మాడ్యూళ్లను
  విస్మరిస్తుంది. `pip` ఇన్‌స్టాలేషన్ ప్రామాణిక కన్సోల్ స్క్రిప్ట్‌ను ఉపయోగిస్తుంది మరియు
  అది ఇన్‌స్టాల్ చేయబడిన ఎన్విరాన్‌మెంట్‌ను అనుసరిస్తుంది.
- ప్రతి చెక్‌కు ఒకసారి తెరిచిన డైరెక్టరీకి సాపేక్షంగా, స్టేట్ లేదా లాక్ ఫైల్ పేరు వద్ద
  సింబాలిక్ లింక్‌ను అనుసరించకుండా కదలిక స్టేట్ చదవబడుతుంది మరియు వ్రాయబడుతుంది.
- `SHA256SUMS` తో పాటు రిలీజ్ అసెట్‌లు బిల్డ్ ప్రొవెనెన్స్ అటెస్టేషన్‌లను కలిగి ఉంటాయి;
  [GitHub Releases నుండి](#from-github-releases) చూడండి.

## 1.0.0 నుండి అప్‌గ్రేడ్ చేయడం

ఈ మార్పులు 2.0.0 లో వస్తాయి.

- పెద్ద `--max-age` ఇవ్వకపోతే, ఒక గంట కంటే పాతదైన వెండర్ టైమ్‌స్టాంప్ ఉన్న కోట్ `UNKNOWN` ను తిరిగి ఇస్తుంది.
  టైమ్‌స్టాంప్ ఇవ్వని ఎండ్‌పాయింట్‌లపై ప్రభావం ఉండదు.
- `--currency` కేవలం 2-16 అక్షరాలు లేదా అంకెలను మాత్రమే అంగీకరిస్తుంది.
- అంకెల సెపరేటర్లు లేదా చుట్టూ ఖాళీలు ఉన్న సంఖ్యా స్ట్రింగ్‌లు తిరస్కరించబడతాయి.
- బడ్జెట్‌లో ఇమడని రీట్రై వేచి ఉండే సమయం `API request timed out` కి బదులుగా
  అంతర్లీన వైఫల్యాన్ని నివేదిస్తుంది.
- నేటివ్ ప్యాకేజీలు ఇకపై `PYTHONPATH` ని పాటించవు.
- ఒక మిలియన్ లేదా అంతకంటే ఎక్కువ థ్రెషోల్డ్‌లు ఎక్స్‌పోనెంట్ సంజ్ఞామానానికి బదులుగా
  సాధారణ దశాంశాలుగా పనితీరు డేటాలో కనిపిస్తాయి.

## లోకలైజేషన్

బండిల్ చేయబడిన stdlib-లోడెడ్ కేటలాగ్‌లను ఉపయోగించి CLI సహాయం, ధృవీకరణ లోపాలు మరియు ప్లగ్ఇన్ స్థితి వివరణలు 45 లోకేల్‌లకు (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) మద్దతు ఇస్తాయి. రిజల్యూషన్ `--lang`, ఆపై `LC_ALL`, `LC_MESSAGES`, మరియు `LANG` ని తనిఖీ చేసి, `en` కి ఫాల్‌బ్యాక్ అవుతుంది. Nagios స్థితి ప్రిఫిక్స్‌లు (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) మరియు పనితీరు డేటా అన్ని లోకేల్‌లలో మారకుండా ఉంటాయి.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## డెవలప్‌మెంట్

[mise](https://mise.jdx.dev/getting-started.html) ను ఇన్‌స్టాల్ చేసి, ఆపై పైన ఉన్న డెవలప్‌మెంట్ సెటప్‌ను అమలు చేయండి. `mise.toml` అనేది Python మరియు uv లను పిన్ చేస్తుంది. డెవలప్‌మెంట్ టూల్స్ `pyproject.toml` లో ప్రకటించబడ్డాయి మరియు కమిట్ చేయబడిన `uv.lock` లో పరిష్కరించబడ్డాయి.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

సెటప్ తర్వాత కమిట్ హుక్స్‌ను ఇన్‌స్టాల్ చేయండి:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

డిపెండెన్సీలను అప్‌డేట్ చేయడానికి `mise exec -- uv add --dev <tool>` లేదా `mise exec -- uv add <dependency>` ఉపయోగించండి మరియు `pyproject.toml` మరియు `uv.lock` రెండింటినీ కమిట్ చేయండి.

CI Linux పై Python 3.12 మరియు 3.13 లను మరియు macOS పై Python 3.13 ను తనిఖీ చేస్తుంది. ప్రతి PR ప్యాకేజీ ధృవీకరణ, డిపెండెన్సీ ఆడిటింగ్ మరియు CodeQL లను కూడా అమలు చేస్తుంది, మరియు Ubuntu పై `.deb` ను మరియు Fedora పై `.rpm` ను ఇన్‌స్టాల్ చేస్తుంది. నిర్మించిన డిస్ట్రిబ్యూషన్‌లు CI రన్‌లపై `distributions` ఆర్టిఫాక్ట్‌గా అందుబాటులో ఉంటాయి.

ప్యాకేజీ మరియు CLI వెర్షన్ `check_bitcoin_price/__init__.py` నుండి వస్తుంది. వెర్షన్ పెంపుదల మరియు GitHub రిలీజ్ అసెట్‌ల ఆటోమేటెడ్ ప్రచురణ కోసం [విడుదల ప్రక్రియ](../../../CONTRIBUTING.md#releases) చూడండి.

## సహకారం

డెవలప్‌మెంట్ వర్క్‌ఫ్లో మరియు సంతకం చేసిన కమిట్ అవసరాల కోసం [CONTRIBUTING.md](../../../CONTRIBUTING.md) చూడండి.

## లైసెన్స్

ఈ ప్రాజెక్ట్ MIT లైసెన్స్ కింద లైసెన్స్ చేయబడింది - వివరాల కోసం [LICENSE](../../../LICENSE) ఫైల్‌ను చూడండి.

## రచయిత

Thomas Vincent

## కృతజ్ఞతలు

- ఉచిత క్రిప్టోకరెన్సీ API ని అందించినందుకు [CoinGecko](https://www.coingecko.com/)
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
