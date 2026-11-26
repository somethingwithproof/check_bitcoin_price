# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · **Igbo** · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Ngwa mgbakwunye Nagios/Icinga iji nyochaa ọnụahịa Bitcoin nwere ókè ịdọ aka ná ntị na ókè dị oke mkpa enwere ike ịhazi.

## Atụmatụ

- Nyochaa ọnụahịa Bitcoin n'ọtụtụ ego mba (USD, EUR, GBP, na ndị ọzọ)
- Ókè ịdọ aka ná ntị na ókè dị oke mkpa enwere ike ịhazi (elu na ala)
- Mpụta ọkọlọtọ nke ngwa mgbakwunye Nagios nwere data arụmọrụ
- Na-eji CoinGecko API (n'efu, achọghị igodo API)
- Nkwado maka isi njedebe API omenala
- Oge njedebe enwere ike ịhazi
- Nlele ịdị ọhụrụ nke ọnụahịa site n'iji akara oge nke onye na-enye ya, nwere ókè ndabara nke otu awa
- Nnwale ọzọ nwere ókè maka ókè ọnụọgụ arịrịọ na ọdịda API nwa oge
- Otu oge njedebe maka nnwale niile yana ókè 64 KiB maka azịza ọ bụla
- Ọkwa nhọrọ maka mgbanwe pasentị zuru oke n'ime awa 24
- Ókè ọnụahịa, oge arịrịọ, na oge ọnụahịa dịrị n'ime data arụmọrụ

## Nwụnye

### Site na GitHub Releases

Budata faịlụ `.deb`, `.rpm`, `.tar.gz`, wheel, na `SHA256SUMS` site na [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Nyochaa nbudata site n'iji `sha256sum --ignore-missing --check SHA256SUMS`. Mwepụta ndị bịara mgbe 1.0.0 gasịrị nwekwara ihe akaebe mmepụta bịanyere aka; kwado na akụ sitere na usoro mwepụta nke ebe nchekwa a site n'iji `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Jiri aha faịlụ ndị sitere na mwepụta a họọrọ. Ngwugwu sistemụ na-etinye `/usr/bin/check_bitcoin_price` na `/usr/lib/nagios/plugins/check_bitcoin_price`; RPM na-enyekwa `/usr/lib64/nagios/plugins/check_bitcoin_price`. Iwu dị na ngwugwu na-agba Python n'ọnọdụ dịpụrụ adịpụ, yabụ ọ na-eleghara `PYTHONPATH` na modul ndị dị na folda ọrụ anya; njikwa ngwugwu sistemụ na-edozi ndabere Python na `requests`. Ha nwere koodu Python na-adabereghị n'ụdị ngwaike ma chọọ nkesa na-enye Python 3.12 ma ọ bụ nke ọhụrụ karịa.

### Site na Isi Koodu

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Maka Mmepe

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Ojiji

### Ojiji Mbụ

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Site na Ókè

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Ókè Nke Ọ Bụla

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Ego Mba Dị Iche

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Oge Njedebe Omenala

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Ịdị Ọhụrụ na Mmemme Nnwale Ọzọ

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Ọnụahịa nwere akara oge nke onye na-enye ya ekwesịghị ịkarị otu awa kemgbe e wepụtara ya dị ka ndabara.
Isi njedebe ndị na-eweghachi naanị ọnụahịa ka nwere ike ịrụ ọrụ mgbe `--max-age` adịghị.
Mgbe e ji `--max-age`, akara oge na-efu, na-ezighị ezi, nke ọdịnihu, ma ọ bụ nke ochie na-eweghachi
`UNKNOWN`; ngwa mgbakwunye anaghị eji oge nbudata mpaghara dochie oge ọnụahịa
nke onye na-enye ya. Akara oge dabara kpọmkwem n'ókè oge ahụ ka dị mma. A na-ajụ akara oge
ọdịnihu mgbe niile.

Ndabara na-enye ohere otu nnwale ọzọ. Naanị njehie njikọ, oge njedebe, na azịza HTTP
408/429/500/502/503/504 ka a na-anwale ọzọ. Oge nchere na-amalite na sekọnd 0.5 ma
na-amụba okpukpu abụọ maka nnwale ọzọ ndị na-eso ya; sekọnd `Retry-After` na ụbọchị HTTP
na-ebute ụzọ. Nnwale niile, ịgụ azịza, ntụgharị JSON, na nchere nnwale ọzọ na-ekerịta
mmemme `--timeout`. Oge nchere nnwale ọzọ na-agaghị abata n'ime oge ahụ na-eweghachi `UNKNOWN` ozugbo
ma kọọ ọdịda kpatara ya, dị ka `HTTP 429` ma ọ bụ `ConnectionError`,
ọ bụghị oge njedebe. A naghị anwale ọzọ ọdịda nkwenye njirimara, njehie HTTP ndị ọzọ na-adịgide adịgide,
JSON na-ezighị ezi, na azịza buru ibu karịa 64 KiB nke data a tụgharịrị. Jiri
`--retries 0` iji gbanyụọ nnwale ọzọ.

### Isi Mmalite Ọnụahịa Ndabere

Jiri nhọrọ `--fallback-url URL` enwere ike ikwughachi ya na isi njedebe kwekọrọ na CoinGecko.
Dị ka ọmụmaatụ, tinye `--fallback-url https://quotes.example.org/simple/price`.
Isi mmalite ọ bụla na-enweta oke nha nhata nke oge njedebe arịrịọ fọdụrụ, gụnyere
nnwale ọzọ ya. Ọdịda nwa oge ma ọ bụ igbu oge nnwale ọzọ karịrị oke ahụ na-aga n'ihu na
isi mmalite na-esote. Ọdịda nyocha TLS, njehie HTTP na-adịgide adịgide, na ọnụahịa na-ezighị ezi
na-eweghachi UNKNOWN. Azịza ọnụahịa ọ bụla nwere ókè nke 64 KiB nke data a tụgharịrị.
Mgbe a haziri ndabere, ọnọdụ ahụ na-akọwa isi mmalite zara dị ka
`primary`, `fallback1`, na ndị ọzọ, n'ebipụtaghị URL ya.

### Mgbanwe N'ime Oge Mkpirikpi

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Nye onye ọrụ nlekota folda ọnọdụ nkeonwe enwere ike ide ihe na ya na sistemụ faịlụ Linux ma ọ bụ
macOS dị n'ime ngwaọrụ. Debe faịlụ `.lock` dị n'akụkụ ya n'ọnọdụ ya n'etiti nlele. Jiri
faịlụ ọnọdụ dị iche maka oge windo ọ bụla. Ego mba nwere akụkọ ihe mere eme dị iche iche n'ime ya.
Oge windo ndabara bụ sekọnd 3600. Ọnụahịa ziri ezi ọ bụla chọrọ akara oge onye na-enye ya
dị n'ime oge windo na ókè oge, nke bụ otu awa belụsọ ma `--max-age` setịpụrụ
nke ọzọ. Ngwa mgbakwunye na-atụnyere ọnụahịa
dị ugbu a na ọnụahịa mbụ kacha ochie karịrị efu n'ime windo ahụ ma kọọ
sekọnd ole gafere n'ezie. Akara oge e kwughachiri anaghị emepụta nlele ọzọ.
Nlele mbụ, akụkọ ihe mere eme gafere oge, ma ọ bụ JSON mebiri emebi na-amalite ntọala ọhụrụ;
metric windo amaghị ihe ọ bụ ruo mgbe enwere nlele enwere ike iji tụnyere. Ọkwa ndị ọzọ ka
na-arụ ọrụ. Ọnọdụ a na-apụghị ide ihe na ya, faịlụ ọnọdụ ma ọ bụ faịlụ mkpọchi bụ njikọ akara, ma ọ bụ ọnụahịa ochie
karịa nlele ọhụrụ e dekọrọ na-eweghachi UNKNOWN. Metric `bitcoin_move_window` nwere akara mgbakwunye/mwepụ
na-eji ókè ịdọ aka ná ntị na ókè dị oke mkpa hà nhata n'akụkụ abụọ. Nha nhata kpọmkwem n'ókè anaghị ewepụta ọkwa.

Ngwa mgbakwunye na-emepe folda ọnọdụ otu ugboro maka nlele ọ bụla ma na-arụ ọrụ n'ihe metụtara ya, yabụ
akụkụ ụzọ a gbanwere n'oge nlele enweghị ike ịtụgharị mkpọchi, ọgụgụ,
ma ọ bụ odide. A na-eso njikọ akara dị n'akụkụ folda nke ụzọ ahụ mgbe
nlele malitere, nke na-eme ka njikọ sistemụ dị ka `/var` na macOS nọgide na-arụ ọrụ. Ya mere,
ndị ọrụ ndị ọzọ ekwesịghị inwe ikike ide ihe na folda ọnọdụ na folda ndị nna nna ya. A na-emepụta faịlụ ọnọdụ na faịlụ mkpọchi site na mode 0600.

### Mgbanwe Pasentị Kwa Ụbọchị

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Ókè mgbanwe na-atụ uru zuru oke nke mgbanwe pasentị awa 24 nwere akara nke CoinGecko
n'ego mba a họọrọ. Mgbanwe dabara kpọmkwem n'ókè anaghị
ewepụta ọkwa. Ọ bụrụ na e nyere ókè abụọ ahụ, ịdọ aka ná ntị ekwesịghị ịkarị nke dị oke mkpa.
Data mgbanwe achọrọ na-efu ma ọ bụ na-ezighị ezi na-eweghachi `UNKNOWN`. Enwere ike ijikọ ọkwa ọnụahịa na mgbanwe;
ọkwa kacha sie ike na-emeri, ebe ọnụahịa na-ebute ụzọ
mgbe ọkwa abụọ ahụ hà nhata.

## Nhọrọ Ahịrị Iwu

| Nhọrọ | Nkọwa |
|--------|-------------|
| `-w`, `--warning` | Ókè ịdọ aka ná ntị (ụdị: LOW:HIGH) |
| `-c`, `--critical` | Ókè dị oke mkpa (ụdị: LOW:HIGH) |
| `--warning-low` | Ókè ịdọ aka ná ntị maka ọnụahịa dị ala |
| `--warning-high` | Ókè ịdọ aka ná ntị maka ọnụahịa dị elu |
| `--critical-low` | Ókè dị oke mkpa maka ọnụahịa dị ala |
| `--critical-high` | Ókè dị oke mkpa maka ọnụahịa dị elu |
| `--currency` | Koodu ego mba nwere mkpụrụedemede ma ọ bụ ọnụọgụ 2-16 (ndabara: usd) |
| `--timeout` | Ngụkọta mmemme oge arịrịọ/nnwale ọzọ API na sekọnd, gụnyere ọnụọgụ ntụpọ (ndabara: 10) |
| `--retries` | Nnwale ọzọ nwa oge agbakwunyere, 0–5 (ndabara: 1) |
| `--max-age` | Oge kacha elu nke ọnụahịa onye na-enye ya na sekọnd ma chọọ akara oge; ọnụahịa nwere akara oge nwere ndabara nke 3600 |
| `--warning-change` | Ókè ịdọ aka ná ntị maka mgbanwe pasentị zuru oke n'ime awa 24 |
| `--critical-change` | Ókè dị oke mkpa maka mgbanwe pasentị zuru oke n'ime awa 24 |
| `--api-url` | URL API mbụ |
| `--fallback-url` | Isi njedebe ọzọ kwekọrọ; kwughachi n'usoro a họọrọ |
| `--state-file` | Faịlụ JSON nke akụkọ mgbanwe |
| `--move-window` | Oge windo mgbanwe na sekọnd (ndabara: 3600) |
| `--warning-move`, `--critical-move` | Ókè mgbanwe zuru oke nke windo na pasentị |
| `-v`, `--verbose` | Gbanye mpụta nkọwa zuru ezu |
| `-V`, `--version` | Gosi ụdị |
| `-h`, `--help` | Gosi ozi enyemaka |

## Nhazi Nagios

### Nkọwa Iwu

Hazie macro akụ Nagios `$USER1$` ka ọ bụrụ folda ngwa mgbakwunye (ngwugwu sistemụ na-eji `/usr/lib/nagios/plugins`). Tinye na nhazi iwu Nagios gị:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Nkọwa Ọrụ

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

### Nhazi Icinga2

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

## Koodu Ọpụpụ

Arụmụka na-ezighị ezi, oge njedebe bụ efu ma ọ bụ nke na-erughị efu, ókè na-ezighị ezi, na ọnụahịa API
mebiri emebi na-eweghachi `UNKNOWN` (ọpụpụ 3). Ókè ga-abụrịrị ọnụọgụ nwere njedebe bụ efu ma ọ bụ karịa,
ebe ókè ala ọ bụla agaghị akarị ókè elu ya. Ego mba ga-abụrịrị
mkpụrụedemede ma ọ bụ ọnụọgụ 2-16. A na-ajụ nhazi na-ezighị ezi tupu ịkpọtụrụ
API. Ọnụahịa ga-abụrịrị nke nwere njedebe ma bụrụ efu ma ọ bụ karịa, e nyere dị ka ọnụọgụ JSON ma ọ bụ eriri
ọnụọgụ ntụpọ dị mfe dị ka `"43521.5"`. Azịza na-enweghị ego mba a rịọrọ
na-akpọ aha ya, dị ka ọmụmaatụ `Response has no EUR price`. Azịza na-ezighị ezi anaghị ewepụta
data arụmọrụ. Nchọpụta nkọwa zuru ezu na-aga na stderr
ka stdout nwee naanị otu ahịrị ọnọdụ nlekota.

| Koodu | Ọnọdụ | Nkọwa |
|------|--------|-------------|
| 0 | OK | Ọnụahịa dị n'ime ókè a nabatara |
| 1 | WARNING | Ọnụahịa gafere ókè ịdọ aka ná ntị |
| 2 | CRITICAL | Ọnụahịa gafere ókè dị oke mkpa |
| 3 | UNKNOWN | Njehie mere (ọdịda API, oge njedebe, na ndị ọzọ) |

## Data Arụmọrụ

Ngwa mgbakwunye na-ewepụta data arụmọrụ n'ụdị ọkọlọtọ Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Data arụmọrụ ọnụahịa gụnyere ókè ịdọ aka ná ntị/dị oke mkpa a haziri na
opekempe efu. A na-ebipụta ókè n'ụdị ọnụọgụ ntụpọ zuru ezu, a naghị agbakọ ya n'ụzọ mkpirikpi
ma ọ bụ n'ụdị exponent, ka ọnụọgụ buru ibu dị ka `14500000:16250000` nọgide na-adị mfe ịgụ. Oge arịrịọ gụnyere nnwale niile na oge nchere. A na-ewepụta oge ọnụahịa dịrị
naanị mgbe onye na-enye ya nyere akara oge ziri ezi; a na-ewepụta mgbanwe kwa ụbọchị
mgbe ọ dị. Ókè mgbanwe hà nhata n'akụkụ efu. Data na-ezighị ezi ma ọ bụ nke ochie
na-ewepụta `UNKNOWN` n'enweghị data arụmọrụ ọnụahịa. Enwere ike iji metrics ndị a na
ngwaọrụ eserese dị ka PNP4Nagios, Grafana, ma ọ bụ InfluxDB.

## API

Ngwa mgbakwunye a na-eji [CoinGecko API](https://www.coingecko.com/en/api) dị ka ndabara, nke dị n'efu ma achọghị igodo API. Ókè ọnụọgụ arịrịọ dị irè.

Isi njedebe omenala ga-ejirịrị otu ụdị azịza ahụ: `bitcoin.<currency>` maka
ọnụahịa, `bitcoin.last_updated_at` maka sekọnd akara oge UNIX, na
`bitcoin.<currency>_24h_change` maka mgbanwe pasentị kwa ụbọchị nwere akara. Naanị ọnụahịa
ka a chọrọ mgbe `--max-age` na ókè mgbanwe adịghị. A ka na-elele akara oge
dị n'ebe ahụ: o kwesịghị ịbụ nke ọdịnihu ma ọ bụ karịa otu
awa. Azịza a tụgharịrị ga-abatarịrị n'ime 64 KiB.

Ego mba a na-akwado gụnyere: usd, eur, gbp, jpy, aud, cad, chf, cny, na ọtụtụ ndị ọzọ.

## Nchekwa

A na-etinye usoro ndị dị n'okpuru na koodu dị ugbu a. Ha na-egbochi ihe isi njedebe na-akpa àgwà ọjọọ ma ọ bụ onye ọrụ mpaghara nwere ike ime
igwe nlekota; ha anaghị eme ka ọnụahịa ahụ n'onwe ya bụrụ nke a pụrụ ịtụkwasị obi.

- A na-enyocha asambodo HTTPS site na ndabara `requests`, ma enweghị nhọrọ
  na-agbanyụ nyocha. `--api-url` omenala nke na-eji `http://` nkịtị enweghị
  nchedo dị otú ahụ.
- DNS, njikọ, ọgụgụ, nnwale ọzọ, na oge nchere na-ekerịta oge njedebe `--timeout`.
  Onye mmekọ na-ezipụ data nwayọọ nwayọọ enweghị ike ịgbatị ya.
- Azịza ọ bụla nwere ókè nke 64 KiB mgbe a tọpụsịrị ya, a na-atụfukwa ahụ ntụgharị
  n'agụghị ya.
- Ọdịda arịrịọ na-ebipụta naanị ọnọdụ HTTP ma ọ bụ ụdị njehie, n'ihi na
  `--api-url` omenala nwere ike ịnwe nzere njirimara.
- Iwu nke `.deb` na `.rpm` tinyere na-agba Python n'ọnọdụ dịpụrụ adịpụ.
  Ọ na-eleghara `PYTHONPATH`, folda saịtị onye ọrụ, na modul ndị dị na folda
  ọrụ anya. Nwụnye `pip` na-eji edemede console ọkọlọtọ ma na-eso
  gburugburu ebe etinyere ya.
- A na-agụ ma na-ede ọnọdụ mgbanwe n'esoghị njikọ akara dị na
  aha faịlụ ọnọdụ ma ọ bụ faịlụ mkpọchi, n'ihe metụtara folda e mepere otu ugboro maka nlele ọ bụla.
- Akụ mwepụta bu ihe akaebe mmepụta na mgbakwunye na
  `SHA256SUMS`; lee [Site na GitHub Releases](#from-github-releases).

## Nkwalite site na 1.0.0

Mgbanwe ndị a na-abịa na 2.0.0.

- Ọnụahịa nwere akara oge onye na-enye ya karịrị otu awa na-eweghachi `UNKNOWN` belụsọ ma
  e nyere `--max-age` ka ukwuu. Isi njedebe ndị na-adịghị eweghachi akara oge enweghị mmetụta.
- `--currency` na-anabata naanị mkpụrụedemede ma ọ bụ ọnụọgụ 2-16.
- A na-ajụ eriri ọnụọgụ nwere nkewa ọnụọgụ ma ọ bụ oghere gbara ya gburugburu.
- Oge nchere nnwale ọzọ nke na-abaghị n'ime mmemme oge na-akọ ọdịda kpatara ya
  kama `API request timed out`.
- Ngwugwu sistemụ anaghịzi asọpụrụ `PYTHONPATH`.
- Ókè nke otu nde ma ọ bụ karịa na-apụta na data arụmọrụ dị ka ọnụọgụ ntụpọ
  nkịtị kama ụdị exponent.

## Nsụgharị Mpaghara

Enyemaka CLI, njehie nkwenye, na nkọwa ọnọdụ ngwa mgbakwunye na-akwado asụsụ mpaghara 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) site n'iji katalọgụ etinyere n'ime ya nke stdlib na-ebunye. Nchọpụta asụsụ na-elele `--lang`, mgbe ahụ `LC_ALL`, `LC_MESSAGES`, na `LANG`, na-alaghachi na `en` ma ọ bụrụ na enweghị. Mmalite ọnọdụ Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) na data arụmọrụ anaghị agbanwe n'asụsụ mpaghara niile.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Mmepe

Wụnye [mise](https://mise.jdx.dev/getting-started.html), wee mee nhazi mmepe dị n'elu. `mise.toml` na-edobe ụdị Python na uv. A kọwapụtara ngwa mmepe na `pyproject.toml` ma dozie ha na `uv.lock` etinyere na git.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Wụnye commit hooks mgbe nhazi gasịrị:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Jiri `mise exec -- uv add --dev <tool>` ma ọ bụ `mise exec -- uv add <dependency>` iji melite ndabere ma tinye ma `pyproject.toml` ma `uv.lock` na commit.

CI na-elele Python 3.12 na 3.13 na Linux yana Python 3.13 na macOS. PR ọ bụla na-agbakwa nkwenye ngwugwu, nyocha ndabere, na CodeQL, ma na-etinye `.deb` na Ubuntu na `.rpm` na Fedora. Nkesa a rụpụtara dị ka artifact `distributions` na ọsọ CI.

Ụdị ngwugwu na CLI sitere na `check_bitcoin_price/__init__.py`. Lee [usoro mwepụta](../../../CONTRIBUTING.md#releases) maka ịkwalite ụdị na mbipụta akpaaka nke akụ mwepụta GitHub.

## Ntinye Aka

Lee [CONTRIBUTING.md](../../../CONTRIBUTING.md) maka usoro ọrụ mmepe na ihe achọrọ maka commit bịanyere aka.

## Akwụkwọ Ikike

A nyere ọrụ a ikike n'okpuru MIT License - lee faịlụ [LICENSE](../../../LICENSE) maka nkọwa zuru ezu.

## Onye Odee

Thomas Vincent

## Ekele

- [CoinGecko](https://www.coingecko.com/) maka inye API cryptocurrency n'efu
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
