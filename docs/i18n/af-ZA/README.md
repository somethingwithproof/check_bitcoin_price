# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

**Afrikaans** · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

'n Nagios/Icinga-inprop om die Bitcoin-prys te monitor met konfigureerbare waarskuwings- en kritieke drumpelwaardes.

## Kenmerke

- Monitor die Bitcoin-prys in verskeie geldeenhede (USD, EUR, GBP, ens.)
- Konfigureerbare waarskuwings- en kritieke drumpelwaardes (hoog en laag)
- Standaard Nagios-inpropafvoer met werkverrigtingsdata
- Gebruik die CoinGecko API (gratis, geen API-sleutel word vereis nie)
- Ondersteuning vir pasgemaakte API-eindpunte
- Konfigureerbare uitteltyd
- Kwotasievarsheidskontroles met behulp van verskaffertydstempels, met 'n versteklimiet van een uur
- Begrensde herpogings vir koerslimiete en tydelike API-foute
- Een sperdatum vir alle pogings en 'n limiet van 64 KiB op elke antwoord
- Opsionele waarskuwings vir absolute 24-uur-persentasiebeweging
- Prysdrumpelwaardes, versoekduur en kwotasie-ouderdom in werkverrigtingsdata

## Installasie

<a name="from-github-releases"></a>

### Vanaf GitHub Releases

Laai `.deb`-, `.rpm`-, `.tar.gz`-, wheel- en `SHA256SUMS`-lêers af vanaf [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Verifieer 'n aflaai met `sha256sum --ignore-missing --check SHA256SUMS`. Vrystellings ná 1.0.0 dra ook ondertekende bouherkoms; bevestig dat 'n bate van hierdie bewaarplek se vrystellingswerkvloei af kom met `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Gebruik die lêernames van die gekose vrystelling. Inheemse pakkette installeer `/usr/bin/check_bitcoin_price` en `/usr/lib/nagios/plugins/check_bitcoin_price`; die RPM voorsien ook `/usr/lib64/nagios/plugins/check_bitcoin_price`. Die verpakte opdrag voer Python in geïsoleerde modus uit, so dit ignoreer `PYTHONPATH` en modules in die werkgids; die stelselpakketbestuurder los Python- en `requests`-afhanklikhede op. Hulle bevat argitektuur-onafhanklike Python-kode en vereis 'n verspreiding wat Python 3.12 of nuwer verskaf.

### Vanaf bronkode

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Vir ontwikkeling

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Gebruik

### Basiese gebruik

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Met drumpelwaardes

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Individuele drumpelwaardes

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Ander geldeenheid

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Pasgemaakte uitteltyd

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Varsheid en herprobeerbegroting

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

'n Kwotasie wat 'n verskaffertydstempel dra, moet by verstek hoogstens een uur oud wees.
Eindpunte wat slegs 'n prys terugstuur, bly bruikbaar wanneer `--max-age` afwesig is.
Met `--max-age` gee ontbrekende, ongeldige, toekomstige of verouderde verskaffertydstempels
`UNKNOWN` terug; die inprop vervang nie die verskaffer se kwotasietyd met die plaaslike
haal-tyd nie. 'n Tydstempel presies op die ouderdomslimiet bly aanvaarbaar. Toekomstige
tydstempels word altyd verwerp.

Die verstekwaarde laat een herpoging toe. Slegs verbindingsfoute, uitteltye en HTTP
408/429/500/502/503/504-antwoorde word weer probeer. Terugvalwagtyd begin by 0.5 sekondes en
verdubbel vir daaropvolgende herpogings; `Retry-After`-sekondes en HTTP-datums geniet
voorrang. Alle pogings, antwoordlesings, JSON-dekodering en herprobeerwagtye deel
die `--timeout`-begroting. 'n Herprobeerwagtyd wat nie pas nie, gee onmiddellik `UNKNOWN` terug
en rapporteer die fout wat dit veroorsaak het, soos `HTTP 429` of `ConnectionError`,
nie 'n uitteltyd nie. Stawingfoute, ander permanente HTTP-foute, ongeldige
JSON en antwoorde groter as 64 KiB gedekodeerde data word nie weer probeer nie. Gebruik
`--retries 0` om herpogings te deaktiveer.

### Terugval-kwotasiebronne

Gebruik herhaalbare `--fallback-url URL`-opsies met CoinGecko-versoenbare eindpunte.
Voeg byvoorbeeld `--fallback-url https://quotes.example.org/simple/price` by.
Elke bron kry 'n gelyke deel van die oorblywende versoeksperdatum, insluitend sy
herpogings. 'n Tydelike fout of 'n herprobeervertraging langer as daardie deel skuif aan na
die volgende bron. TLS-verifikasiefoute, permanente HTTP-foute en ongeldige
kwotasies gee UNKNOWN terug. Elke kwotasie-antwoord is beperk tot 64 KiB gedekodeerde data.
Wanneer terugvalbronne gekonfigureer is, identifiseer die status die antwoordende bron as
`primary`, `fallback1`, ensovoorts, sonder om sy URL te druk.

### Kortvenster-beweging

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Gee die moniteringsgebruiker 'n private skryfbare statusgids op 'n plaaslike Linux- of
macOS-lêerstelsel. Hou die aangrensende `.lock`-lêer in plek tussen kontroles. Gebruik 'n
afsonderlike statuslêer per venster. Geldeenhede het onafhanklike geskiedenisse daarin.
Die verstekvenster is 3600 sekondes. Elke geldige kwotasie benodig 'n verskaffertydstempel
binne die venster en die ouderdomslimiet, wat een uur is tensy `--max-age` 'n ander een
stel. Die inprop vergelyk die huidige
prys met die oudste vroeëre positiewe prys in daardie venster en rapporteer die
werklike verstreke sekondes. Herhaalde tydstempels skep nie bykomende monsters nie.
'n Eerste monster, vervalde geskiedenis of korrupte JSON begin 'n nuwe basislyn; die
venstermetriek is onbekend totdat daar 'n vergelykbare monster is. Ander waarskuwings geld
steeds. Onskryfbare status, 'n simboliese skakel vir die status- of grendellêer, of 'n kwotasie ouer
as die nuutste aangetekende monster gee UNKNOWN terug. Die getekende `bitcoin_move_window`-metriek
gebruik simmetriese waarskuwings- en kritieke reekse. Gelykheid by 'n limiet veroorsaak nie 'n waarskuwing nie.

Die inprop maak die statusgids een keer per kontrole oop en werk relatief daartoe, sodat
'n padkomponent wat tydens die kontrole vervang word nie die grendel, die leesaksie
of die skryfaksie kan herlei nie. Simboliese skakels in die gidsgedeelte van die pad word gevolg wanneer
die kontrole begin, wat platformskakels soos `/var` op macOS bruikbaar hou. Die
statusgids en sy ouergidse moet dus nie deur ander gebruikers skryfbaar wees nie.
Status- en grendellêers word met modus 0600 geskep.

### Daaglikse persentasiebeweging

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Veranderingsdrumpelwaardes meet die absolute waarde van CoinGecko se getekende 24-uur-
persentasieverandering in die gekose geldeenheid. 'n Verandering presies by 'n drumpelwaarde
veroorsaak nie 'n waarskuwing nie. As albei drumpelwaardes verskaf word, mag waarskuwing nie kritiek oorskry nie.
Ontbrekende of ongeldige vereiste veranderingsdata gee `UNKNOWN` terug. Prys- en veranderings-
waarskuwings kan gekombineer word; die hoogste erns wen, met prys wat voorrang geniet
wanneer ernsgrade ooreenstem.

## Opdragreëlopsies

| Opsie | Beskrywing |
|--------|-------------|
| `-w`, `--warning` | Waarskuwingsdrumpelreeks (formaat: LOW:HIGH) |
| `-c`, `--critical` | Kritieke drumpelreeks (formaat: LOW:HIGH) |
| `--warning-low` | Waarskuwingsdrumpelwaarde vir lae prys |
| `--warning-high` | Waarskuwingsdrumpelwaarde vir hoë prys |
| `--critical-low` | Kritieke drumpelwaarde vir lae prys |
| `--critical-high` | Kritieke drumpelwaarde vir hoë prys |
| `--currency` | Geldeenheidskode van 2-16 letters of syfers (verstek: usd) |
| `--timeout` | Totale API-versoek-/herprobeerbegroting in sekondes, insluitend breukwaardes (verstek: 10) |
| `--retries` | Bykomende tydelike pogings, 0-5 (verstek: 1) |
| `--max-age` | Maksimum verskafferkwotasie-ouderdom in sekondes en vereis 'n tydstempel; tydgestempelde kwotasies het 'n verstek van 3600 |
| `--warning-change` | Waarskuwingslimiet vir absolute 24-uur-persentasiebeweging |
| `--critical-change` | Kritieke limiet vir absolute 24-uur-persentasiebeweging |
| `--api-url` | Primêre API-URL |
| `--fallback-url` | Bykomende versoenbare eindpunt; herhaal in voorkeurvolgorde |
| `--state-file` | JSON-bewegingsgeskiedenislêer |
| `--move-window` | Bewegingsvenster in sekondes (verstek: 3600) |
| `--warning-move`, `--critical-move` | Absolute vensterbewegingsdrumpelwaardes in persent |
| `-v`, `--verbose` | Aktiveer breedvoerige afvoer |
| `-V`, `--version` | Wys weergawe |
| `-h`, `--help` | Wys hulpboodskap |

## Nagios-konfigurasie

### Opdragdefinisie

Stel die Nagios-hulpbronmakro `$USER1$` op die inpropgids (die inheemse pakkette gebruik `/usr/lib/nagios/plugins`). Voeg by jou Nagios-opdragkonfigurasie:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Diensdefinisie

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

### Icinga2-konfigurasie

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

## Afsluitkodes

Ongeldige argumente, nie-positiewe uitteltye, ongeldige drumpelreekse en wangevormde
API-pryse gee `UNKNOWN` (afsluitkode 3) terug. Drumpelwaardes moet eindige, nie-negatiewe
getalle wees, met elke onderste grens nie groter as sy boonste grens nie. Die geldeenheid moet
2-16 letters of syfers wees. Ongeldige konfigurasie word verwerp voordat die API gekontak word.
Pryse moet eindig en nie-negatief wees, verskaf as JSON-getalle of gewone
desimale stringe soos `"43521.5"`. 'n Antwoord sonder die aangevraagde geldeenheid
noem dit, byvoorbeeld `Response has no EUR price`. Ongeldige antwoorde lewer nie
werkverrigtingsdata nie. Breedvoerige diagnostiek gaan na stderr
sodat stdout 'n enkele moniteringstatuslyn bevat.

| Kode | Status | Beskrywing |
|------|--------|-------------|
| 0 | OK | Prys is binne aanvaarbare reeks |
| 1 | WARNING | Prys het waarskuwingsdrumpelwaarde oorskry |
| 2 | CRITICAL | Prys het kritieke drumpelwaarde oorskry |
| 3 | UNKNOWN | Fout het voorgekom (API-fout, uitteltyd, ens.) |

## Werkverrigtingsdata

Die inprop lewer werkverrigtingsdata in standaard Nagios-formaat:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Pryswerkverrigtingsdata sluit die gekonfigureerde waarskuwings-/kritieke reekse en 'n
minimum van nul in. Drumpelwaardes word in volledige desimale notasie gedruk, nooit afgerond
of in eksponentvorm nie, sodat groot waardes soos `14500000:16250000` ontleedbaar bly. Versoektyd sluit alle pogings en terugvalwagtyd in. Kwotasie-ouderdom word
slegs uitgegee wanneer die verskaffer 'n geldige tydstempel verskaf; daaglikse verandering word uitgegee
wanneer beskikbaar. Veranderingsreekse is simmetries rondom nul. Ongeldige of verouderde data
lewer `UNKNOWN` sonder pryswerkverrigtingsdata. Hierdie metrieke kan gebruik word met
grafiekhulpmiddels soos PNP4Nagios, Grafana of InfluxDB.

## API

Hierdie inprop gebruik die [CoinGecko API](https://www.coingecko.com/en/api) by verstek, wat gratis is en nie 'n API-sleutel vereis nie. Koerslimiete geld.

Pasgemaakte eindpunte moet dieselfde antwoordvorm gebruik: `bitcoin.<currency>` vir
prys, `bitcoin.last_updated_at` vir UNIX-tydstempelsekondes, en
`bitcoin.<currency>_24h_change` vir getekende daaglikse persentasiebeweging. Slegs prys
word vereis wanneer `--max-age` en die veranderingsdrumpelwaardes afwesig is. 'n Tydstempel
wat teenwoordig is, word steeds nagegaan: dit mag nie in die toekoms wees of ouer as een
uur wees nie. Die gedekodeerde antwoord moet in 64 KiB pas.

Ondersteunde geldeenhede sluit in: usd, eur, gbp, jpy, aud, cad, chf, cny, en vele meer.

## Sekuriteit

Die maatreëls hieronder is in die huidige kode geïmplementeer. Hulle beperk wat 'n wangedraende eindpunt of 'n plaaslike gebruiker aan die
moniteringsgasheer kan doen; hulle maak nie die kwotasie self betroubaar nie.

- HTTPS-sertifikate word geverifieer met die `requests`-verstekwaardes, en geen opsie
  deaktiveer verifikasie nie. 'n Pasgemaakte `--api-url` wat gewone `http://` gebruik, het nie
  sulke beskerming nie.
- DNS, verbinding, lesings, herpogings en terugvalwagtyd deel die `--timeout`-sperdatum. 'n
  Eweknie wat data stadig stuur, kan dit nie verleng nie.
- Elke antwoord is beperk tot 64 KiB ná dekompressie, en herleidingsliggame
  word ongelees weggegooi.
- Versoekfoute druk slegs 'n HTTP-status of 'n foutklas, omdat 'n pasgemaakte
  `--api-url` aanmeldbesonderhede kan bevat.
- Die opdrag wat deur die `.deb` en `.rpm` geïnstalleer word, voer Python in geïsoleerde modus uit.
  Dit ignoreer `PYTHONPATH`, die gebruikers-werfgids en modules in die werk-
  gids. 'n `pip`-installasie gebruik die standaard konsoleskrip en volg
  die omgewing waarin dit geïnstalleer is.
- Bewegingsstatus word gelees en geskryf sonder om 'n simboliese skakel by die
  status- of grendellêernaam te volg, relatief tot 'n gids wat een keer per kontrole oopgemaak word.
- Vrystellingsbates dra bouherkoms-attesterings benewens
  `SHA256SUMS`; sien [Vanaf GitHub Releases](#from-github-releases).

## Opgradering vanaf 1.0.0

Hierdie veranderinge word in 2.0.0 vrygestel.

- 'n Kwotasie met 'n verskaffertydstempel ouer as een uur gee `UNKNOWN` terug tensy 'n
  groter `--max-age` gegee word. Eindpunte wat geen tydstempel terugstuur nie, word nie geraak nie.
- `--currency` aanvaar slegs 2-16 letters of syfers.
- Numeriese stringe met syferskeiers of omliggende spasies word verwerp.
- 'n Herprobeerwagtyd wat nie in die begroting pas nie, rapporteer die onderliggende fout
  in plaas van `API request timed out`.
- Die inheemse pakkette eerbiedig nie meer `PYTHONPATH` nie.
- Drumpelwaardes van een miljoen of meer verskyn in werkverrigtingsdata as gewone
  desimale in plaas van eksponentnotasie.

## Lokalisering

CLI-hulp, validasiefoute en inpropstatusbeskrywings ondersteun 45 lokale (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) met behulp van gebundelde katalogusse wat deur die standaardbiblioteek gelaai word. Oplossing gaan `--lang` na, dan `LC_ALL`, `LC_MESSAGES` en `LANG`, en val terug na `en`. Nagios-statusvoorvoegsels (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) en werkverrigtingsdata bly onveranderd oor alle lokale heen.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Ontwikkeling

Installeer [mise](https://mise.jdx.dev/getting-started.html) en voer dan die ontwikkelingsopstelling hierbo uit. `mise.toml` pen Python en uv vas. Ontwikkelingshulpmiddels word in `pyproject.toml` verklaar en in die ingediende `uv.lock` opgelos.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Installeer die commit-hooks ná opstelling:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Gebruik `mise exec -- uv add --dev <tool>` of `mise exec -- uv add <dependency>` om afhanklikhede op te dateer en albei `pyproject.toml` en `uv.lock` in te dien.

CI toets Python 3.12 en 3.13 op Linux en Python 3.13 op macOS. Elke PR voer ook pakketvalidasie, afhanklikheidsouditering en CodeQL uit, en installeer die `.deb` op Ubuntu en die `.rpm` op Fedora. Geboude verspreidings is beskikbaar as die `distributions`-artefak op CI-lopies.

Die pakket- en CLI-weergawe kom vanaf `check_bitcoin_price/__init__.py`. Sien [die vrystellingsproses](../../../CONTRIBUTING.md#releases) vir weergawebotsings en outomatiese publikasie van GitHub-vrystellingsbates.

## Bydraes

Sien [CONTRIBUTING.md](../../../CONTRIBUTING.md) vir die ontwikkelingswerkvloei en vereistes vir ondertekende commits.

## Lisensie

Hierdie projek is gelisensieer onder die MIT-lisensie - sien die [LICENSE](../../../LICENSE)-lêer vir besonderhede.

## Outeur

Thomas Vincent

## Erkennings

- [CoinGecko](https://www.coingecko.com/) vir die verskaffing van 'n gratis kriptogeldeenheid-API
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
