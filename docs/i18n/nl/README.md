# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · **Nederlands** · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Een Nagios/Icinga-plugin voor het monitoren van de Bitcoin-koers met configureerbare waarschuwings- en kritieke drempelwaarden.

## Functies

- De Bitcoin-koers monitoren in meerdere valuta's (USD, EUR, GBP, enz.)
- Configureerbare waarschuwings- en kritieke drempelwaarden (hoog en laag)
- Standaard Nagios-pluginuitvoer met prestatiegegevens
- Gebruikt de CoinGecko API (gratis, geen API-sleutel vereist)
- Ondersteuning voor aangepaste API-endpoints
- Configureerbare time-out
- Controles op actualiteit van koersen met tijdstempels van de aanbieder, met een standaardlimiet van één uur
- Begrensde herhaalpogingen bij rate limits en tijdelijke API-storingen
- Eén deadline voor alle pogingen en een limiet van 64 KiB per antwoord
- Optionele meldingen bij absolute procentuele koersbeweging over 24 uur
- Koersdrempels, aanvraagduur en koersouderdom in prestatiegegevens

## Installatie

### Vanaf GitHub Releases

Download `.deb`-, `.rpm`-, `.tar.gz`-, wheel- en `SHA256SUMS`-bestanden van [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Verifieer een download met `sha256sum --ignore-missing --check SHA256SUMS`. Releases na 1.0.0 bevatten ook ondertekende build provenance; bevestig dat een bestand afkomstig is uit de releaseworkflow van deze repository met `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Gebruik de bestandsnamen van de gekozen release. Native pakketten installeren `/usr/bin/check_bitcoin_price` en `/usr/lib/nagios/plugins/check_bitcoin_price`; het RPM-pakket levert ook `/usr/lib64/nagios/plugins/check_bitcoin_price`. De verpakte opdracht voert Python uit in geïsoleerde modus, waardoor `PYTHONPATH` en modules in de werkmap worden genegeerd; de pakketbeheerder van het systeem lost de afhankelijkheden voor Python en `requests` op. Ze bevatten architectuuronafhankelijke Python-code en vereisen een distributie met Python 3.12 of nieuwer.

### Vanuit de broncode

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Voor ontwikkeling

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Gebruik

### Basisgebruik

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Met drempelwaarden

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Individuele drempelwaarden

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Andere valuta

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Aangepaste time-out

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Actualiteit en budget voor herhaalpogingen

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Een koers die een tijdstempel van de aanbieder bevat, mag standaard maximaal één uur oud zijn.
Endpoints die alleen een koers retourneren blijven bruikbaar wanneer `--max-age` ontbreekt.
Met `--max-age` retourneren ontbrekende, ongeldige, toekomstige of verouderde tijdstempels van de aanbieder
`UNKNOWN`; de plugin vervangt de tijdstempel van de aanbieder niet door de lokale ophaaltijd. Een tijdstempel precies op de ouderdomslimiet blijft acceptabel. Toekomstige
tijdstempels worden altijd geweigerd.

Standaard is één herhaalpoging toegestaan. Alleen verbindingsfouten, time-outs en HTTP-antwoorden
408/429/500/502/503/504 worden opnieuw geprobeerd. De backoff begint bij 0,5 seconden en
wordt voor volgende pogingen verdubbeld; `Retry-After`-seconden en HTTP-datums krijgen
voorrang. Alle pogingen, het lezen van antwoorden, JSON-decodering en wachttijden voor herhaalpogingen delen
het `--timeout`-budget. Een wachttijd die niet binnen het budget past, retourneert direct `UNKNOWN`
en meldt de fout die ertoe leidde, zoals `HTTP 429` of `ConnectionError`,
en geen time-out. Authenticatiefouten, andere permanente HTTP-fouten, ongeldige
JSON en antwoorden groter dan 64 KiB aan gedecodeerde gegevens worden niet opnieuw geprobeerd. Gebruik
`--retries 0` om herhaalpogingen uit te schakelen.

### Terugvalbronnen voor koersen

Gebruik herhaalbare `--fallback-url URL`-opties met CoinGecko-compatibele endpoints.
Voeg bijvoorbeeld `--fallback-url https://quotes.example.org/simple/price` toe.
Elke bron krijgt een gelijk deel van de resterende aanvraagdeadline, inclusief bijbehorende
herhaalpogingen. Een tijdelijke fout of een herhaalvertraging langer dan dat deel schakelt door naar
de volgende bron. Fouten bij TLS-verificatie, permanente HTTP-fouten en ongeldige
koersen retourneren UNKNOWN. Elk koersantwoord is beperkt tot 64 KiB aan gedecodeerde gegevens.
Wanneer terugvalbronnen zijn geconfigureerd, identificeert de status de antwoordende bron als
`primary`, `fallback1`, enzovoort, zonder de URL ervan weer te geven.

### Koersbeweging op korte termijn

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Geef de monitoringgebruiker een eigen beschrijfbare statusmap op een lokaal Linux- of
macOS-bestandssysteem. Laat het naastgelegen `.lock`-bestand tussen controles staan. Gebruik een
afzonderlijk statusbestand per tijdsvenster. Valuta's hebben daarin onafhankelijke geschiedenissen.
Het standaardvenster is 3600 seconden. Elke geldige koers vereist een tijdstempel van de aanbieder
binnen het venster en de ouderdomslimiet, die één uur is tenzij `--max-age` een andere waarde
instelt. De plugin vergelijkt de huidige
koers met de oudste eerdere positieve koers in dat venster en rapporteert het
werkelijk verstreken aantal seconden. Herhaalde tijdstempels voegen geen extra metingen toe.
Een eerste meting, verlopen geschiedenis of beschadigde JSON start een nieuwe basislijn; de
venstermetriek is onbekend totdat er een vergelijkbare meting is. Andere meldingen blijven wel
van toepassing. Een niet-beschrijfbare status, een symbolische link als status- of vergrendelingsbestand, of een koers ouder
dan de nieuwste vastgelegde meting retourneert UNKNOWN. De metriek `bitcoin_move_window` met teken
gebruikt symmetrische waarschuwings- en kritieke bereiken. Gelijkheid aan een limiet geeft geen melding.

De plugin opent de statusmap eenmaal per controle en werkt relatief ten opzichte daarvan, zodat
een padcomponent dat tijdens de controle wordt vervangen de vergrendeling, het lezen
of het schrijven niet kan omleiden. Symbolische links in het mapgedeelte van het pad worden gevolgd wanneer
de controle start, waardoor platformlinks zoals `/var` op macOS bruikbaar blijven. De
statusmap en bovenliggende mappen mogen daarom niet beschrijfbaar zijn voor andere
gebruikers. Status- en vergrendelingsbestanden worden aangemaakt met modus 0600.

### Dagelijkse procentuele beweging

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Drempelwaarden voor verandering meten de absolute waarde van CoinGecko's procentuele 24-uursverandering met teken in de gekozen valuta. Een verandering precies op een drempelwaarde geeft
geen melding. Als beide drempelwaarden worden opgegeven, mag warning niet hoger zijn dan critical.
Ontbrekende of ongeldige vereiste veranderingsgegevens retourneren `UNKNOWN`. Koers- en veranderingsmeldingen
kunnen worden gecombineerd; de hoogste ernst wint, waarbij koers voorrang krijgt
wanneer de ernst gelijk is.

## Opdrachtregelopties

| Optie | Beschrijving |
|-------|--------------|
| `-w`, `--warning` | Drempelwaardebereik voor waarschuwing (formaat: LOW:HIGH) |
| `-c`, `--critical` | Kritiek drempelwaardebereik (formaat: LOW:HIGH) |
| `--warning-low` | Waarschuwingsdrempel voor lage koers |
| `--warning-high` | Waarschuwingsdrempel voor hoge koers |
| `--critical-low` | Kritieke drempel voor lage koers |
| `--critical-high` | Kritieke drempel voor hoge koers |
| `--currency` | Valutacode van 2-16 letters of cijfers (standaard: usd) |
| `--timeout` | Totaal budget voor API-aanvraag/herhaalpogingen in seconden, inclusief decimale waarden (standaard: 10) |
| `--retries` | Extra tijdelijke pogingen, 0–5 (standaard: 1) |
| `--max-age` | Maximale ouderdom van aanbiederskoers in seconden en vereist een tijdstempel; koersen met tijdstempel zijn standaard 3600 |
| `--warning-change` | Waarschuwingslimiet voor absolute procentuele beweging over 24 uur |
| `--critical-change` | Kritieke limiet voor absolute procentuele beweging over 24 uur |
| `--api-url` | Primaire API-URL |
| `--fallback-url` | Extra compatibel endpoint; herhaal in volgorde van voorkeur |
| `--state-file` | JSON-bestand met bewegingsgeschiedenis |
| `--move-window` | Bewegingsvenster in seconden (standaard: 3600) |
| `--warning-move`, `--critical-move` | Drempelwaarden voor absolute vensterbeweging in procenten |
| `-v`, `--verbose` | Uitgebreide uitvoer inschakelen |
| `-V`, `--version` | Versie tonen |
| `-h`, `--help` | Hulptekst tonen |

## Nagios-configuratie

### Opdrachtdefinitie

Stel de Nagios-resourcemacro `$USER1$` in op de pluginmap (de native pakketten gebruiken `/usr/lib/nagios/plugins`). Voeg toe aan je Nagios-opdrachtconfiguratie:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Servicedefinitie

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

### Icinga2-configuratie

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

## Exitcodes

Ongeldige argumenten, niet-positieve time-outs, ongeldige drempelwaardebereiken en misvormde
API-koersen retourneren `UNKNOWN` (exit 3). Drempelwaarden moeten eindige, niet-negatieve
getallen zijn, waarbij elke ondergrens niet groter is dan de bovengrens. De valuta moet
uit 2-16 letters of cijfers bestaan. Een ongeldige configuratie wordt geweigerd voordat contact wordt opgenomen met
de API. Koersen moeten eindig en niet-negatief zijn, opgegeven als JSON-getallen of gewone
decimale tekenreeksen zoals `"43521.5"`. Een antwoord zonder de gevraagde valuta
noemt deze, bijvoorbeeld `Response has no EUR price`. Ongeldige antwoorden leveren geen
prestatiegegevens op. Uitgebreide diagnostiek gaat naar stderr
zodat stdout één enkele monitoringstatusregel bevat.

| Code | Status | Beschrijving |
|------|--------|--------------|
| 0 | OK | Koers ligt binnen acceptabel bereik |
| 1 | WARNING | Koers heeft waarschuwingsdrempel overschreden |
| 2 | CRITICAL | Koers heeft kritieke drempel overschreden |
| 3 | UNKNOWN | Fout opgetreden (API-storing, time-out, enz.) |

## Prestatiegegevens

De plugin levert prestatiegegevens in het standaard Nagios-formaat:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Prestatiegegevens voor de koers bevatten de geconfigureerde warning/critical-bereiken en een
minimum van nul. Drempelwaarden worden in volledige decimale notatie afgedrukt, nooit afgerond
of in exponentiële notatie, zodat grote waarden zoals `14500000:16250000` verwerkbaar blijven. De aanvraagtijd omvat alle pogingen en backoff. Koersouderdom wordt
alleen uitgevoerd wanneer de aanbieder een geldige tijdstempel levert; dagelijkse verandering wordt uitgevoerd
wanneer beschikbaar. Veranderingsbereiken zijn symmetrisch rond nul. Ongeldige of verouderde gegevens
leveren `UNKNOWN` op zonder koersprestatiegegevens. Deze metrieken kunnen worden gebruikt met
grafiektools zoals PNP4Nagios, Grafana of InfluxDB.

## API

Deze plugin gebruikt standaard de [CoinGecko API](https://www.coingecko.com/en/api), die gratis is en geen API-sleutel vereist. Er gelden rate limits.

Aangepaste endpoints moeten dezelfde antwoordstructuur gebruiken: `bitcoin.<currency>` voor
koers, `bitcoin.last_updated_at` voor UNIX-tijdstempelseconden, en
`bitcoin.<currency>_24h_change` voor dagelijkse procentuele beweging met teken. Alleen de koers
is vereist wanneer `--max-age` en de veranderingsdrempels ontbreken. Een aanwezige
tijdstempel wordt nog steeds gecontroleerd: deze mag niet in de toekomst liggen of meer dan één
uur oud zijn. Het gedecodeerde antwoord moet binnen 64 KiB passen.

Ondersteunde valuta's zijn onder andere: usd, eur, gbp, jpy, aud, cad, chf, cny en nog veel meer.

## Beveiliging

Onderstaande maatregelen zijn in de huidige code geïmplementeerd. Ze beperken wat een foutief handelend endpoint of een lokale gebruiker kan aanrichten op de
monitoringhost; ze maken de koers zelf niet betrouwbaar.

- HTTPS-certificaten worden geverifieerd met de standaardwaarden van `requests`, en geen enkele optie
  schakelt verificatie uit. Een aangepaste `--api-url` die gewoon `http://` gebruikt heeft een dergelijke
  bescherming niet.
- DNS, verbinding, leesbewerkingen, herhaalpogingen en backoff delen de `--timeout`-deadline. Een
  peer die langzaam gegevens verzendt, kan deze niet verlengen.
- Elk antwoord is na decompressie beperkt tot 64 KiB, en redirect-bodies
  worden ongelezen weggegooid.
- Aanvraagfouten drukken alleen een HTTP-status of een foutklasse af, omdat een aangepaste
  `--api-url` inloggegevens kan bevatten.
- De opdracht die door `.deb` en `.rpm` wordt geïnstalleerd, voert Python uit in geïsoleerde modus.
  Deze negeert `PYTHONPATH`, de user site-map en modules in de werkmap.
  Een `pip`-installatie gebruikt het standaard consolescript en volgt
  de omgeving waarin deze is geïnstalleerd.
- Bewegingsstatus wordt gelezen en geschreven zonder een symbolische link te volgen bij de
  naam van het status- of vergrendelingsbestand, relatief ten opzichte van een map die eenmaal per controle wordt geopend.
- Releasebestanden bevatten build provenance-attestaties naast
  `SHA256SUMS`; zie [Vanaf GitHub Releases](#from-github-releases).

## Upgraden vanaf 1.0.0

Deze wijzigingen worden geleverd in 2.0.0.

- Een koers met een tijdstempel van de aanbieder die ouder is dan één uur retourneert `UNKNOWN`, tenzij een
  hogere `--max-age` wordt opgegeven. Endpoints die geen tijdstempel retourneren blijven ongewijzigd.
- `--currency` accepteert alleen 2-16 letters of cijfers.
- Numerieke tekenreeksen met scheidingstekens voor cijfers of omliggende spaties worden geweigerd.
- Een wachttijd voor een herhaalpoging die niet in het budget past, meldt de onderliggende fout
  in plaats van `API request timed out`.
- De native pakketten respecteren `PYTHONPATH` niet langer.
- Drempelwaarden van één miljoen of meer verschijnen in prestatiegegevens als gewone
  decimalen in plaats van in exponentiële notatie.

## Lokalisatie

CLI-hulp, validatiefouten en statusbeschrijvingen van de plugin ondersteunen 45 talen (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) met behulp van meegeleverde catalogi die via de stdlib worden geladen. De resolutie controleert achtereenvolgens `--lang`, `LC_ALL`, `LC_MESSAGES` en `LANG`, en valt terug op `en`. Nagios-statusvoorvoegsels (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) en prestatiegegevens blijven in alle talen ongewijzigd.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Ontwikkeling

Installeer [mise](https://mise.jdx.dev/getting-started.html) en voer vervolgens de ontwikkelingsinstallatie hierboven uit. `mise.toml` legt Python en uv vast. Ontwikkeltools zijn gedeclareerd in `pyproject.toml` en opgelost in het vastgelegde `uv.lock`.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Installeer de commit-hooks na de installatie:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Gebruik `mise exec -- uv add --dev <tool>` of `mise exec -- uv add <dependency>` om afhankelijkheden bij te werken en commit zowel `pyproject.toml` als `uv.lock`.

CI controleert Python 3.12 en 3.13 op Linux en Python 3.13 op macOS. Elke PR voert ook pakketvalidatie, afhankelijkheidsaudits en CodeQL uit, en installeert het `.deb`-pakket op Ubuntu en het `.rpm`-pakket op Fedora. Gebouwde distributies zijn beschikbaar als het artefact `distributions` bij CI-runs.

De pakket- en CLI-versie komt uit `check_bitcoin_price/__init__.py`. Zie [het releaseproces](../../../CONTRIBUTING.md#releases) voor versieverhogingen en geautomatiseerde publicatie van GitHub-releasebestanden.

## Bijdragen

Zie [CONTRIBUTING.md](../../../CONTRIBUTING.md) voor de ontwikkelingsworkflow en de vereisten voor ondertekende commits.

## Licentie

Dit project is gelicentieerd onder de MIT-licentie - zie het bestand [LICENSE](../../../LICENSE) voor details.

## Auteur

Thomas Vincent

## Dankwoord

- [CoinGecko](https://www.coingecko.com/) voor het aanbieden van een gratis cryptocurrency-API
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
