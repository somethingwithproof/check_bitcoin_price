# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · **Filipino** · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Isang Nagios/Icinga plugin para i-monitor ang presyo ng Bitcoin gamit ang mga nako-configure na warning at critical threshold.

## Mga Tampok

- I-monitor ang presyo ng Bitcoin sa iba't ibang currency (USD, EUR, GBP, atbp.)
- Mga nako-configure na warning at critical threshold (mataas at mababa)
- Karaniwang output ng Nagios plugin na may performance data
- Gumagamit ng CoinGecko API (libre, hindi kailangan ng API key)
- Suporta para sa mga custom na API endpoint
- Nako-configure na timeout
- Mga pagsusuri sa pagiging bago ng quote gamit ang mga vendor timestamp, na may isang oras na default na limitasyon
- May hangganang mga pagsubok muli (bounded retries) para sa mga rate limit at pansamantalang pagkabigo ng API
- Isang deadline para sa lahat ng pagsubok at 64 KiB na limitasyon sa bawat tugon
- Opsyonal na mga alerto para sa absolute 24-hour percentage movement
- Mga price threshold, tagal ng request, at edad ng quote sa performance data

## Pag-install

<a name="from-github-releases"></a>

### Mula sa GitHub Releases

I-download ang `.deb`, `.rpm`, `.tar.gz`, wheel, at `SHA256SUMS` na mga file mula sa [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). I-verify ang na-download gamit ang `sha256sum --ignore-missing --check SHA256SUMS`. Ang mga release pagkatapos ng 1.0.0 ay may kasamang signed build provenance; kumpirmahing galing sa release workflow ng repository na ito ang isang asset gamit ang `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Gamitin ang mga filename mula sa napiling release. Ini-install ng mga native package ang `/usr/bin/check_bitcoin_price` at `/usr/lib/nagios/plugins/check_bitcoin_price`; nagbibigay rin ang RPM ng `/usr/lib64/nagios/plugins/check_bitcoin_price`. Pinapatakbo ng naka-package na command ang Python sa isolated mode, kaya binabalewala nito ang `PYTHONPATH` at ang mga module sa working directory; nilulutas ng system package manager ang mga dependency ng Python at `requests`. Naglalaman ang mga ito ng architecture-independent na Python code at nangangailangan ng distribution na may Python 3.12 o mas bago.

### Mula sa Source

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Para sa Development

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Paggamit

### Pangunahing Paggamit

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### May Mga Threshold

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Mga Indibidwal na Threshold

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Ibang Currency

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Custom na Timeout

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Pagiging Bago ng Quote at Retry Budget

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Ang isang quote na may vendor timestamp ay dapat na hindi hihigit sa isang oras ang tanda bilang default.
Ang mga endpoint na nagbabalik lamang ng presyo ay nananatiling magagamit kapag wala ang `--max-age`.
Kapag may `--max-age`, ang kulang, hindi wasto, nasa hinaharap, o luma nang vendor timestamp ay nagbabalik ng
`UNKNOWN`; hindi ipinapalit ng plugin ang lokal na oras ng pagkuha para sa oras ng quote ng vendor.
Ang timestamp na eksaktong nasa limitasyon ng edad ay nananatiling katanggap-tanggap. Ang mga timestamp
sa hinaharap ay palaging tinatanggihan.

Ang default ay nagpapahintulot ng isang pagsubok muli (retry). Tanging mga connection error, timeout, at mga tugon na HTTP
408/429/500/502/503/504 ang sinusubukang muli. Nagsisimula ang backoff sa 0.5 segundo at
nadodoble para sa mga kasunod na pagsubok muli; ang `Retry-After` sa segundo at mga HTTP date ang
inuuna. Lahat ng pagsubok, pagbasa ng tugon, pag-decode ng JSON, at paghihintay sa retry ay nagbabahagi sa
budget ng `--timeout`. Ang paghihintay sa retry na hindi kasya sa budget ay agad na nagbabalik ng `UNKNOWN`
at nag-uulat ng pagkabigo na nagdulot nito, tulad ng `HTTP 429` o `ConnectionError`,
hindi isang timeout. Ang mga pagkabigo sa authentication, iba pang permanenteng HTTP error, hindi wastong
JSON, at mga tugon na mas malaki sa 64 KiB ng na-decode na data ay hindi sinusubukang muli. Gamitin ang
`--retries 0` upang i-disable ang mga pagsubok muli.

### Mga Fallback na Pinagmulan ng Quote

Gamitin ang nauulit na mga opsyong `--fallback-url URL` sa mga endpoint na tugma sa CoinGecko.
Halimbawa, idagdag ang `--fallback-url https://quotes.example.org/simple/price`.
Bawat pinagmulan ay nakakakuha ng pantay na bahagi ng natitirang deadline ng request, kabilang ang mga
retry nito. Ang pansamantalang pagkabigo o pagkaantala ng retry na mas mahaba kaysa sa bahaging iyon ay lumilipat sa
susunod na pinagmulan. Ang mga pagkabigo sa pag-verify ng TLS, permanenteng HTTP error, at hindi wastong
quote ay nagbabalik ng UNKNOWN. Bawat tugon ng quote ay limitado sa 64 KiB ng na-decode na data.
Kapag naka-configure ang mga fallback, tinutukoy ng status ang sumagot na pinagmulan bilang
`primary`, `fallback1`, at iba pa, nang hindi ipinapakita ang URL nito.

### Paggalaw sa Maikling Panahon (Short-window movement)

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Bigyan ang monitoring user ng pribadong writable state directory sa isang lokal na Linux o
macOS filesystem. Panatilihing nakalagay ang katabing `.lock` file sa pagitan ng mga pagsusuri. Gumamit ng
hiwalay na state file para sa bawat window. Ang mga currency ay may mga hiwalay na history sa loob nito.
Ang default na window ay 3600 segundo. Bawat wastong quote ay nangangailangan ng vendor timestamp
sa loob ng window at ng limitasyon ng edad, na isang oras maliban kung magtakda ng iba ang `--max-age`.
Ikinukumpara ng plugin ang kasalukuyang presyo sa pinakalumang naunang positibong presyo sa window na iyon at iniuulat ang
aktwal na lumipas na segundo. Ang mga paulit-ulit na timestamp ay hindi lumilikha ng karagdagang sample.
Ang unang sample, nag-expire na history, o sirang JSON ay nagsisimula ng bagong baseline; ang
window metric ay unknown hanggang sa magkaroon ng maihahambing na sample. Ang ibang mga alerto ay patuloy pa ring
umiiral. Ang hindi masusulatan na state, symbolic-link na state o lock file, o quote na mas luma
kaysa sa pinakabagong naitalang sample ay nagbabalik ng UNKNOWN. Ang may sign na `bitcoin_move_window` metric
ay gumagamit ng magkatugmang (symmetric) warning at critical range. Ang pagkapantay sa limitasyon ay hindi nag-aalerto.

Binubuksan ng plugin ang state directory nang isang beses bawat pagsusuri at gumagana nang kaugnay dito, kaya
ang bahagi ng path na pinalitan habang isinasagawa ang pagsusuri ay hindi makakapag-redirect sa lock, pagbasa,
o pagsulat. Ang mga symbolic link sa bahagi ng directory ng path ay sinusundan kapag
nagsimula ang pagsusuri, na nagpapanatiling magagamit ng mga platform link tulad ng `/var` sa macOS. Kaya ang
state directory at ang mga parent nito ay hindi dapat masulatan ng ibang mga user.
Ang mga state at lock file ay nililikha gamit ang mode 0600.

### Pang-araw-araw na Porsyento ng Paggalaw

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Sinusukat ng mga change threshold ang absolute value ng may sign na 24-hour
percentage change ng CoinGecko sa napiling currency. Ang pagbabagong eksaktong nasa threshold ay hindi
nag-aalerto. Kung parehong ibinigay ang dalawang threshold, ang warning ay hindi dapat lumagpas sa critical.
Ang kulang o hindi wastong kinakailangang change data ay nagbabalik ng `UNKNOWN`. Maaaring pagsamahin ang mga price at change
alert; ang pinakamataas na kalubhaan ang mananaig, kung saan nauuna ang presyo
kapag magkapantay ang kalubhaan.

## Mga Opsyon sa Command Line

| Opsyon | Paglalarawan |
|--------|--------------|
| `-w`, `--warning` | Warning threshold range (format: LOW:HIGH) |
| `-c`, `--critical` | Critical threshold range (format: LOW:HIGH) |
| `--warning-low` | Warning threshold para sa mababang presyo |
| `--warning-high` | Warning threshold para sa mataas na presyo |
| `--critical-low` | Critical threshold para sa mababang presyo |
| `--critical-high` | Critical threshold para sa mataas na presyo |
| `--currency` | Currency code na may 2-16 na letra o numero (default: usd) |
| `--timeout` | Kabuuang API request/retry budget sa segundo, kabilang ang mga fractional value (default: 10) |
| `--retries` | Karagdagang pansamantalang pagsubok, 0-5 (default: 1) |
| `--max-age` | Pinakamataas na edad ng vendor quote sa segundo at nangangailangan ng timestamp; ang mga may timestamp na quote ay may default na 3600 |
| `--warning-change` | Warning limit para sa absolute 24-hour percentage movement |
| `--critical-change` | Critical limit para sa absolute 24-hour percentage movement |
| `--api-url` | Pangunahing API URL |
| `--fallback-url` | Karagdagang tugmang endpoint; ulitin ayon sa gustong pagkakasunod-sunod |
| `--state-file` | JSON movement history file |
| `--move-window` | Movement window sa segundo (default: 3600) |
| `--warning-move`, `--critical-move` | Mga absolute window movement threshold sa porsyento |
| `-v`, `--verbose` | I-enable ang verbose output |
| `-V`, `--version` | Ipakita ang bersyon |
| `-h`, `--help` | Ipakita ang mensahe ng tulong |

## Configuration ng Nagios

### Depinisyon ng Command

Itakda ang Nagios resource macro na `$USER1$` sa plugin directory (gumagamit ang mga native package ng `/usr/lib/nagios/plugins`). Idagdag sa iyong configuration ng mga Nagios command:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Depinisyon ng Service

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

### Configuration ng Icinga2

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

## Mga Exit Code

Ang mga hindi wastong argumento, hindi positibong timeout, hindi wastong threshold range, at maling
pormat na presyo mula sa API ay nagbabalik ng `UNKNOWN` (exit 3). Ang mga threshold ay dapat na finite, hindi negatibong
numero, kung saan ang bawat mababang hangganan (low bound) ay hindi mas malaki sa mataas na hangganan (high bound) nito. Ang currency ay dapat
na 2-16 na letra o numero. Ang hindi wastong configuration ay tinatanggihan bago pa man makipag-ugnayan sa
API. Ang mga presyo ay dapat na finite at hindi negatibo, na ibinigay bilang mga JSON number o plain
decimal string tulad ng `"43521.5"`. Ang tugon na walang hinihiling na currency ay
binabanggit ito, halimbawa `Response has no EUR price`. Ang mga hindi wastong tugon ay hindi naglalabas ng
performance data. Ang mga verbose diagnostic ay napupunta sa stderr
upang ang stdout ay maglaman ng iisang linya ng monitoring status.

| Code | Status | Paglalarawan |
|------|--------|--------------|
| 0 | OK | Ang presyo ay nasa loob ng katanggap-tanggap na saklaw |
| 1 | WARNING | Lumagpas ang presyo sa warning threshold |
| 2 | CRITICAL | Lumagpas ang presyo sa critical threshold |
| 3 | UNKNOWN | May naganap na error (pagkabigo ng API, timeout, atbp.) |

## Performance Data

Naglalabas ang plugin ng performance data sa karaniwang format ng Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Kasama sa price performance data ang mga naka-configure na warning/critical range at
minimum na zero. Ang mga threshold ay ipinapakita sa buong decimal notation, hindi kailanman ini-round
o nasa exponent form, kaya ang malalaking halaga tulad ng `14500000:16250000` ay nananatiling na-parse. Kasama sa request time ang lahat ng pagsubok at backoff. Inilalabas lamang ang quote age
kapag nagbigay ang vendor ng wastong timestamp; inilalabas ang daily change
kapag available. Ang mga change range ay simetriko sa paligid ng zero. Ang hindi wasto o lumang data ay
nagreresulta sa `UNKNOWN` nang walang price performance data. Maaaring gamitin ang mga metric na ito sa mga
graphing tool tulad ng PNP4Nagios, Grafana, o InfluxDB.

## API

Gumagamit ang plugin na ito ng [CoinGecko API](https://www.coingecko.com/en/api) bilang default, na libre at hindi nangangailangan ng API key. Umiiral ang mga rate limit.

Ang mga custom na endpoint ay dapat gumamit ng parehong hugis ng tugon: `bitcoin.<currency>` para sa
presyo, `bitcoin.last_updated_at` para sa mga segundo ng UNIX timestamp, at
`bitcoin.<currency>_24h_change` para sa may sign na pang-araw-araw na porsyento ng paggalaw. Tanging presyo
lamang ang kinakailangan kapag wala ang `--max-age` at ang mga change threshold. Ang timestamp na
naroroon ay sinusuri pa rin: hindi ito dapat nasa hinaharap o mas luma sa isang oras.
Ang na-decode na tugon ay dapat kumasya sa 64 KiB.

Kasama sa mga sinusuportahang currency ang: usd, eur, gbp, jpy, aud, cad, chf, cny, at marami pang iba.

## Seguridad

Ang mga hakbang sa ibaba ay ipinatutupad sa kasalukuyang code. Nililimitahan ng mga ito kung ano ang maaaring gawin ng isang hindi maayos na endpoint o lokal na user sa
monitoring host; hindi nito ginagawang mapagkakatiwalaan ang quote mismo.

- Ang mga HTTPS certificate ay bini-verify gamit ang mga default ng `requests`, at walang opsyon na
  nagdi-disable ng verification. Ang custom na `--api-url` na gumagamit ng plain `http://` ay walang
  ganitong proteksyon.
- Ang DNS, connection, pagbasa, mga retry, at backoff ay nagbabahagi sa deadline ng `--timeout`. Ang isang
  peer na mabagal magpadala ng data ay hindi maaaring magpahaba nito.
- Bawat tugon ay limitado sa 64 KiB pagkatapos ng decompression, at ang mga redirect body
  ay itinatapon nang hindi binabasa.
- Ang mga pagkabigo sa request ay nagpi-print lamang ng HTTP status o error class, dahil ang isang custom na
  `--api-url` ay maaaring maglaman ng mga kredensyal.
- Ang command na na-install ng `.deb` at `.rpm` ay nagpapatakbo ng Python sa isolated mode.
  Binabalewala nito ang `PYTHONPATH`, ang user site directory, at mga module sa working
  directory. Ang pag-install gamit ang `pip` ay gumagamit ng karaniwang console script at sumusunod sa
  environment kung saan ito naka-install.
- Ang movement state ay binabasa at isinusulat nang hindi sumusunod sa symbolic link sa
  pangalan ng state o lock file, kaugnay ng isang directory na binubuksan nang isang beses bawat pagsusuri.
- Ang mga release asset ay may dalang build provenance attestation bukod pa sa
  `SHA256SUMS`; tingnan ang [Mula sa GitHub Releases](#from-github-releases).

## Pag-upgrade mula sa 1.0.0

Ipinapadala ang mga pagbabagong ito sa 2.0.0.

- Ang quote na may vendor timestamp na mas luma sa isang oras ay nagbabalik ng `UNKNOWN` maliban kung magbigay ng
  mas malaking `--max-age`. Hindi apektado ang mga endpoint na hindi nagbabalik ng timestamp.
- Tumatanggap lamang ang `--currency` ng 2-16 na letra o numero.
- Tinatanggihan ang mga numeric string na may mga digit separator o nakapaligid na espasyo.
- Ang paghihintay sa retry na hindi kasya sa budget ay nag-uulat ng pinagbabatayang pagkabigo
  sa halip na `API request timed out`.
- Hindi na sinusunod ng mga native package ang `PYTHONPATH`.
- Ang mga threshold na isang milyon o higit pa ay lumilitaw sa performance data bilang mga plain
  decimal sa halip na exponent notation.

## Lokalisasyon

Sinusuportahan ng tulong sa CLI, mga validation error, at mga paglalarawan ng status ng plugin ang 45 locale (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) gamit ang mga naka-bundle na catalog na ni-load ng stdlib. Sinusuri ng resolution ang `--lang`, pagkatapos ay ang `LC_ALL`, `LC_MESSAGES`, at `LANG`, at bumabalik sa `en` kung wala. Ang mga Nagios status prefix (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) at performance data ay nananatiling hindi nagbabago sa lahat ng locale.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Development

I-install ang [mise](https://mise.jdx.dev/getting-started.html), pagkatapos ay patakbuhin ang development setup sa itaas. Pini-pin ng `mise.toml` ang Python at uv. Idinedeklara ang mga development tool sa `pyproject.toml` at nilulutas sa naka-commit na `uv.lock`.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

I-install ang mga commit hook pagkatapos ng setup:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Gamitin ang `mise exec -- uv add --dev <tool>` o `mise exec -- uv add <dependency>` upang i-update ang mga dependency at i-commit ang parehong `pyproject.toml` at `uv.lock`.

Sinusuri ng CI ang Python 3.12 at 3.13 sa Linux at Python 3.13 sa macOS. Bawat PR ay nagpapatakbo rin ng package validation, dependency auditing, at CodeQL, at nag-i-install ng `.deb` sa Ubuntu at `.rpm` sa Fedora. Ang mga nabuong distribution ay available bilang `distributions` artifact sa mga pagtakbo ng CI.

Ang bersyon ng package at CLI ay nagmumula sa `check_bitcoin_price/__init__.py`. Tingnan ang [proseso ng pag-release](../../../CONTRIBUTING.md#releases) para sa mga pagtaas ng bersyon at awtomatikong paglalathala ng mga GitHub release asset.

## Pag-aambag

Tingnan ang [CONTRIBUTING.md](../../../CONTRIBUTING.md) para sa development workflow at mga kinakailangan sa signed-off commit.

## Lisensya

Ang proyektong ito ay lisensyado sa ilalim ng MIT License - tingnan ang [LICENSE](../../../LICENSE) file para sa mga detalye.

## May-akda

Thomas Vincent

## Mga Pasasalamat

- [CoinGecko](https://www.coingecko.com/) para sa pagbibigay ng libreng cryptocurrency API
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
