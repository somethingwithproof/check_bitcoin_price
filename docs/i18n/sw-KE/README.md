# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · **Kiswahili** · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Programu-jalizi ya Nagios/Icinga ya kufuatilia bei ya Bitcoin yenye viwango vya onyo na hatari vinavyoweza kusanidiwa.

## Vipengele

- Fuatilia bei ya Bitcoin katika sarafu mbalimbali (USD, EUR, GBP, n.k.)
- Viwango vya onyo na hatari vinavyoweza kusanidiwa (vya juu na vya chini)
- Matokeo ya kawaida ya programu-jalizi ya Nagios pamoja na data ya utendakazi
- Hutumia API ya CoinGecko (bure, haihitaji ufunguo wa API)
- Usaidizi wa ncha maalum za API
- Muda wa kuisha unaoweza kusanidiwa
- Ukaguzi wa upya wa bei kwa kutumia mihuri ya muda ya mtoa huduma, ukiwa na kikomo cha chaguo-msingi cha saa moja
- Majaribio machache tena kwa vikomo vya kasi na hitilafu za muda za API
- Muda mmoja wa mwisho kwa majaribio yote na kikomo cha 64 KiB kwa kila jibu
- Arifa za hiari kuhusu mabadiliko kamili ya asilimia katika saa 24
- Viwango vya bei, muda wa ombi, na umri wa bei katika data ya utendakazi

## Usakinishaji

<a name="from-github-releases"></a>

### Kutoka kwa Matoleo ya GitHub

Pakua faili za `.deb`, `.rpm`, `.tar.gz`, wheel, na `SHA256SUMS` kutoka [Matoleo ya GitHub](https://github.com/somethingwithproof/check_bitcoin_price/releases). Thibitisha faili uliyopakua kwa `sha256sum --ignore-missing --check SHA256SUMS`. Matoleo baada ya 1.0.0 pia yana uthibitisho wa chanzo cha ujenzi uliosainiwa; thibitisha kuwa faili ilitoka kwenye mtiririko wa matoleo wa hazina hii kwa `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Tumia majina ya faili kutoka kwa toleo ulilochagua. Vifurushi asili husakinisha `/usr/bin/check_bitcoin_price` na `/usr/lib/nagios/plugins/check_bitcoin_price`; RPM pia hutoa `/usr/lib64/nagios/plugins/check_bitcoin_price`. Amri iliyosakinishwa huendesha Python katika hali iliyotengwa, hivyo hupuuza `PYTHONPATH` na moduli zilizo kwenye saraka ya kazi; kidhibiti vifurushi cha mfumo hushughulikia utegemezi wa Python na `requests`. Vina msimbo wa Python usiotegemea usanifu wa kompyuta na vinahitaji mfumo unaotoa Python 3.12 au mpya zaidi.

### Kutoka kwa Msimbo Chanzo

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Kwa Uendelezaji

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Matumizi

### Matumizi ya Msingi

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Pamoja na Viwango vya Onyo na Hatari

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Viwango Binafsi

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Sarafu Tofauti

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Muda Maalum wa Kuisha

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Upya wa Bei na Bajeti ya Majaribio

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Bei iliyo na muhuri wa muda wa mtoa huduma lazima isiwe na umri wa zaidi ya saa moja kwa chaguo-msingi.
Ncha zinazorejesha bei pekee bado zinatumika wakati `--max-age` haipo.
Pamoja na `--max-age`, mihuri ya muda ya mtoa huduma iliyokosekana, batili, ya wakati ujao, au iliyopitwa na wakati hurejesha
`UNKNOWN`; programu-jalizi haibadilishi muda wa bei wa mtoa huduma na muda wa ndani wa kupakua.
Muhuri wa muda ulio sawa na kikomo cha umri bado unakubalika. Mihuri ya muda ya wakati ujao hukataliwa kila wakati.

Chaguo-msingi huruhusu jaribio moja la marudio. Hitilafu za muunganisho pekee, muda wa kuisha, na majibu ya HTTP
408/429/500/502/503/504 ndiyo hujaribiwa tena. Muda wa kusubiri huanza kwa sekunde 0.5 na
huongezeka mara mbili kwa majaribio yanayofuata; sekunde za `Retry-After` na tarehe za HTTP hupewa
kipaumbele. Majaribio yote, usomaji wa majibu, usimbaji wa JSON, na muda wa kusubiri wa marudio hushiriki
bajeti ya `--timeout`. Kusubiri kwa marudio ambako hakuwezi kutoshea hurejesha `UNKNOWN` mara moja
na kuripoti hitilafu iliyosababisha, kama vile `HTTP 429` au `ConnectionError`,
wala si kuisha kwa muda. Kushindwa kwa uthibitishaji, hitilafu nyingine za kudumu za HTTP, JSON
batili, na majibu makubwa kuliko 64 KiB ya data iliyosimbwa hayajaribiwi tena. Tumia
`--retries 0` kuzima majaribio ya marudio.

### Vyanzo mbadala vya bei

Tumia chaguo zinazoweza kurudiwa za `--fallback-url URL` pamoja na ncha zinazooana na CoinGecko.
Kwa mfano, ongeza `--fallback-url https://quotes.example.org/simple/price`.
Kila chanzo hupata mgawo sawa wa muda uliosalia wa ombi, ikiwa ni pamoja na majaribio yake
ya marudio. Hitilafu ya muda mfupi au ucheleweshaji wa jaribio la marudio ulio mrefu kuliko mgawo huo husogeza mbele hadi
chanzo kinachofuata. Kushindwa kwa uthibitishaji wa TLS, hitilafu za kudumu za HTTP na bei
batili hurejesha UNKNOWN. Kila jibu la bei lina kikomo cha 64 KiB ya data iliyosimbwa.
Wakati vyanzo mbadala vimesanidiwa, hali hutambulisha chanzo kilichojibu kama
`primary`, `fallback1`, na kadhalika, bila kuchapisha URL yake.

### Mabadiliko ya kipindi kifupi

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Mpe mtumiaji wa ufuatiliaji saraka binafsi ya hali inayoweza kuandikwa kwenye mfumo wa faili wa ndani wa Linux au
macOS. Weka faili jirani ya `.lock` mahali pake kati ya ukaguzi. Tumia
faili tofauti ya hali kwa kila kipindi. Sarafu zina historia huru ndani yake.
Kipindi cha chaguo-msingi ni sekunde 3600. Kila bei halali inahitaji muhuri wa muda wa mtoa huduma
ulio ndani ya kipindi hicho na kikomo cha umri, ambacho ni saa moja isipokuwa `--max-age` iweke
kingine. Programu-jalizi hulinganisha bei ya sasa
na bei chanya ya awali zaidi katika kipindi hicho na kuripoti
sekunde halisi zilizopita. Mihuri ya muda inayojirudia haiundi sampuli za ziada.
Sampuli ya kwanza, historia iliyopitwa na wakati, au JSON iliyoharibika huanza msingi mpya; kipimo
cha kipindi huwa hakijulikani hadi kuwe na sampuli inayoweza kulinganishwa. Arifa nyingine bado
hutumika. Hali isiyoweza kuandikwa, faili ya hali au kufuli iliyo kiungo cha mfano, au bei ya zamani
kuliko sampuli mpya zaidi iliyorekodiwa hurejesha UNKNOWN. Kipimo chenye alama cha `bitcoin_move_window`
hutumia masafa ya ulinganifu ya onyo na hatari. Usawa kwenye kikomo hautoi arifa.

Programu-jalizi hufungua saraka ya hali mara moja kwa kila ukaguzi na hufanya kazi kuhusiana nayo, hivyo
sehemu ya njia iliyobadilishwa wakati wa ukaguzi haiwezi kuelekeza upya kufuli, usomaji,
au uandishi. Viungo vya mfano katika sehemu ya saraka ya njia hufuatwa
ukaguzi unapoanza, jambo linalowezesha viungo vya jukwaa kama `/var` kwenye macOS kuendelea kutumika. Kwa hivyo
saraka ya hali na saraka zake za juu hazipaswi kuandikwa na watumiaji
wengine. Faili za hali na kufuli huundwa kwa ruhusa za 0600.

### Mabadiliko ya Asilimia ya Kila Siku

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Viwango vya mabadiliko hupima thamani kamili ya mabadiliko ya asilimia ya saa 24 yenye alama ya CoinGecko
katika sarafu iliyochaguliwa. Mabadiliko yaliyo sawa na kiwango
hayatoi arifa. Ikiwa viwango vyote viwili vimetolewa, onyo halipaswi kuzidi hatari.
Data ya mabadiliko inayohitajika iliyokosekana au batili hurejesha `UNKNOWN`. Arifa za bei na mabadiliko
zinaweza kuunganishwa; kiwango cha juu zaidi cha uzito hushinda, huku bei ikichukua kipaumbele
uzito unapokuwa sawa.

## Chaguo za Mstari wa Amri

| Chaguo | Maelezo |
|--------|-------------|
| `-w`, `--warning` | Masafa ya kiwango cha onyo (muundo: LOW:HIGH) |
| `-c`, `--critical` | Masafa ya kiwango cha hatari (muundo: LOW:HIGH) |
| `--warning-low` | Kiwango cha onyo kwa bei ya chini |
| `--warning-high` | Kiwango cha onyo kwa bei ya juu |
| `--critical-low` | Kiwango cha hatari kwa bei ya chini |
| `--critical-high` | Kiwango cha hatari kwa bei ya juu |
| `--currency` | Msimbo wa sarafu wenye herufi au tarakimu 2-16 (chaguo-msingi: usd) |
| `--timeout` | Jumla ya bajeti ya ombi la API na marudio kwa sekunde, ikijumuisha thamani za desimali (chaguo-msingi: 10) |
| `--retries` | Majaribio ya ziada ya muda mfupi, 0–5 (chaguo-msingi: 1) |
| `--max-age` | Umri wa juu wa bei ya mtoa huduma kwa sekunde na kuhitaji muhuri wa muda; bei zenye muhuri wa muda hutumia chaguo-msingi cha 3600 |
| `--warning-change` | Kikomo cha onyo kwa mabadiliko kamili ya asilimia katika saa 24 |
| `--critical-change` | Kikomo cha hatari kwa mabadiliko kamili ya asilimia katika saa 24 |
| `--api-url` | URL kuu ya API |
| `--fallback-url` | Ncha ya ziada inayooana; rudia kwa mpangilio unaopendelea |
| `--state-file` | Faili ya JSON ya historia ya mabadiliko |
| `--move-window` | Kipindi cha mabadiliko kwa sekunde (chaguo-msingi: 3600) |
| `--warning-move`, `--critical-move` | Viwango kamili vya mabadiliko ya kipindi kwa asilimia |
| `-v`, `--verbose` | Washa maelezo ya kina |
| `-V`, `--version` | Onyesha toleo |
| `-h`, `--help` | Onyesha ujumbe wa usaidizi |

## Usanidi wa Nagios

### Ufafanuzi wa Amri

Weka makro ya rasilimali ya Nagios `$USER1$` kwenye saraka ya programu-jalizi (vifurushi asili hutumia `/usr/lib/nagios/plugins`). Ongeza kwenye usanidi wako wa amri za Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Ufafanuzi wa Huduma

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

### Usanidi wa Icinga2

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

## Misimbo ya Kutoka

Hoja batili, muda wa kuisha usio chanya, masafa batili ya viwango, na bei za API zisizo na muundo sahihi
hurejesha `UNKNOWN` (exit 3). Viwango lazima viwe nambari zenye mwisho zisizo hasi,
huku kila kikomo cha chini kikiwa hakizidi kikomo chake cha juu. Sarafu lazima
iwe herufi au tarakimu 2-16. Usanidi batili hukataliwa kabla ya kuwasiliana na
API. Bei lazima ziwe zenye mwisho na zisizo hasi, zikitolewa kama nambari za JSON au tungo
rahisi za desimali kama `"43521.5"`. Jibu lisilo na sarafu iliyoombwa
huitaja, kwa mfano `Response has no EUR price`. Majibu batili hayatoi
data ya utendakazi. Uchunguzi wa kina huenda kwenye stderr
ili stdout iwe na mstari mmoja wa hali ya ufuatiliaji.

| Msimbo | Hali | Maelezo |
|------|--------|-------------|
| 0 | OK | Bei iko ndani ya masafa yanayokubalika |
| 1 | WARNING | Bei imevuka kiwango cha onyo |
| 2 | CRITICAL | Bei imevuka kiwango cha hatari |
| 3 | UNKNOWN | Hitilafu imetokea (kushindwa kwa API, muda kuisha, n.k.) |

## Data ya Utendakazi

Programu-jalizi hutoa data ya utendakazi katika muundo wa kawaida wa Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Data ya utendakazi ya bei inajumuisha masafa ya onyo/hatari yaliyosanidiwa na
kima cha chini cha sifuri. Viwango huchapishwa kwa nukuu kamili ya desimali, havikadiriwi
wala kuwekwa katika muundo wa kipeo, ili thamani kubwa kama `14500000:16250000` ziendelee kusomeka. Muda wa ombi unajumuisha majaribio yote na muda wa kusubiri. Umri wa bei
hutolewa tu wakati mtoa huduma anapotoa muhuri wa muda halali; mabadiliko ya kila siku hutolewa
yanapopatikana. Masafa ya mabadiliko yana ulinganifu kuzunguka sifuri. Data batili au iliyopitwa na wakati
hutoa `UNKNOWN` bila data ya utendakazi ya bei. Vipimo hivi vinaweza kutumika na
zana za kuchora grafu kama PNP4Nagios, Grafana, au InfluxDB.

## API

Programu-jalizi hii hutumia [CoinGecko API](https://www.coingecko.com/en/api) kwa chaguo-msingi, ambayo ni ya bure na haihitaji ufunguo wa API. Vikomo vya kasi hutumika.

Ncha maalum lazima zitumie muundo uleule wa majibu: `bitcoin.<currency>` kwa
bei, `bitcoin.last_updated_at` kwa sekunde za muhuri wa muda wa UNIX, na
`bitcoin.<currency>_24h_change` kwa mabadiliko ya asilimia ya kila siku yenye alama. Bei pekee
ndiyo inahitajika wakati `--max-age` na viwango vya mabadiliko havipo. Muhuri wa muda
uliopo bado hukaguliwa: haupaswi kuwa wa wakati ujao au kuwa na umri wa zaidi ya saa
moja. Jibu lililosimbwa lazima litoshee katika 64 KiB.

Sarafu zinazotumika ni pamoja na: usd, eur, gbp, jpy, aud, cad, chf, cny, na nyingine nyingi.

## Usalama

Hatua zifuatazo zimetekelezwa katika msimbo wa sasa. Zinapunguza kile ambacho ncha isiyofanya kazi ipasavyo au mtumiaji wa ndani anaweza kufanya kwenye
seva ya ufuatiliaji; hazifanyi bei yenyewe iwe ya kuaminika.

- Vyeti vya HTTPS huthibitishwa kwa chaguo-msingi za `requests`, na hakuna chaguo
  linalozima uthibitishaji. `--api-url` maalum inayotumia `http://` ya kawaida haina
  ulinzi kama huo.
- DNS, muunganisho, usomaji, majaribio ya marudio, na muda wa kusubiri hushiriki muda wa mwisho wa `--timeout`.
  Mshirika anayetuma data polepole hawezi kuuongeza.
- Kila jibu lina kikomo cha 64 KiB baada ya kufunguliwa, na miili ya uelekezaji upya
  hutupwa bila kusomwa.
- Kushindwa kwa ombi huchapisha hali ya HTTP au darasa la hitilafu pekee, kwa sababu
  `--api-url` maalum inaweza kuwa na vitambulisho vya siri.
- Amri iliyosakinishwa na `.deb` na `.rpm` huendesha Python katika hali iliyotengwa.
  Hupuuza `PYTHONPATH`, saraka ya tovuti ya mtumiaji, na moduli zilizo katika saraka ya
  kazi. Usakinishaji wa `pip` hutumia hati ya kawaida ya kiweko na hufuata
  mazingira ilimosakinishwa.
- Hali ya mabadiliko husomwa na kuandikwa bila kufuata kiungo cha mfano kwenye
  jina la faili ya hali au kufuli, kuhusiana na saraka iliyofunguliwa mara moja kwa kila ukaguzi.
- Faili za toleo hubeba uthibitisho wa chanzo cha ujenzi pamoja na
  `SHA256SUMS`; tazama [Kutoka kwa Matoleo ya GitHub](#from-github-releases).

## Kuboresha kutoka 1.0.0

Mabadiliko haya yanakuja katika 2.0.0.

- Bei iliyo na muhuri wa muda wa mtoa huduma ulio na umri wa zaidi ya saa moja hurejesha `UNKNOWN` isipokuwa
  `--max-age` kubwa zaidi itolewe. Ncha zisizorejesha muhuri wa muda haziathiriwi.
- `--currency` hukubali herufi au tarakimu 2-16 pekee.
- Tungo za nambari zilizo na vitenganishi vya tarakimu au nafasi zinazozizunguka hukataliwa.
- Muda wa kusubiri wa jaribio la marudio usioenea kwenye bajeti huripoti hitilafu ya msingi
  badala ya `API request timed out`.
- Vifurushi asili haviheshimu tena `PYTHONPATH`.
- Viwango vya milioni moja au zaidi huonekana katika data ya utendakazi kama desimali za
  kawaida badala ya nukuu ya kipeo.

## Ujanibishaji

Usaidizi wa CLI, hitilafu za uthibitishaji, na maelezo ya hali ya programu-jalizi yanasaidia lugha 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) kwa kutumia katalogi zilizojumuishwa zinazopakiwa na stdlib. Uchaguzi hukagua `--lang`, kisha `LC_ALL`, `LC_MESSAGES`, na `LANG`, na kurejea kwenye `en`. Viambishi awali vya hali ya Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) na data ya utendakazi hubaki bila kubadilika katika lugha zote.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Uendelezaji

Sakinisha [mise](https://mise.jdx.dev/getting-started.html), kisha endesha usanidi wa uendelezaji ulio hapo juu. `mise.toml` hufunga toleo la Python na uv. Zana za uendelezaji zimetangazwa katika `pyproject.toml` na kutatuliwa katika `uv.lock` iliyowekwa.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Sakinisha kulabu za commit baada ya usanidi:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Tumia `mise exec -- uv add --dev <tool>` au `mise exec -- uv add <dependency>` kusasisha utegemezi na uweke `pyproject.toml` na `uv.lock` zote mbili kwenye commit.

CI hukagua Python 3.12 na 3.13 kwenye Linux na Python 3.13 kwenye macOS. Kila PR pia huendesha uthibitishaji wa vifurushi, ukaguzi wa utegemezi, na CodeQL, na husakinisha `.deb` kwenye Ubuntu na `.rpm` kwenye Fedora. Vifurushi vilivyojengwa vinapatikana kama `distributions` artifact kwenye mikimbio ya CI.

Toleo la kifurushi na CLI linatoka kwenye `check_bitcoin_price/__init__.py`. Tazama [mchakato wa kutolewa](../../../CONTRIBUTING.md#releases) kwa mabadiliko ya toleo na uchapishaji otomatiki wa faili za matoleo ya GitHub.

## Kuchangia

Tazama [CONTRIBUTING.md](../../../CONTRIBUTING.md) kwa mtiririko wa kazi ya uendelezaji na mahitaji ya commit zilizosainiwa.

## Leseni

Mradi huu umeidhinishwa chini ya Leseni ya MIT - tazama faili ya [LICENSE](../../../LICENSE) kwa maelezo zaidi.

## Mwandishi

Thomas Vincent

## Shukrani

- [CoinGecko](https://www.coingecko.com/) kwa kutoa API ya sarafu za kidijitali bila malipo
- [Miongozo ya Uendelezaji wa Programu-jalizi za Nagios](https://nagios-plugins.org/doc/guidelines.html)
