# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · **Svenska** · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Ett Nagios/Icinga-plugin för att övervaka Bitcoin-priset med konfigurerbara varnings- och kritiska tröskelvärden.

## Funktioner

- Övervaka Bitcoin-priset i flera valutor (USD, EUR, GBP med flera)
- Konfigurerbara varnings- och kritiska tröskelvärden (högt och lågt)
- Standardutdata för Nagios-plugin med prestandadata
- Använder CoinGecko API (kostnadsfritt, ingen API-nyckel krävs)
- Stöd för anpassade API-slutpunkter
- Konfigurerbar tidsgräns
- Aktualitetskontroller för kurser med leverantörens tidsstämplar, med en standardgräns på en timme
- Begränsade återförsök vid hastighetsbegränsningar och tillfälliga API-fel
- En gemensam tidsgräns för alla försök och en gräns på 64 KiB per svar
- Valfria larm vid absolut procentuell rörelse under 24 timmar
- Priströsklar, svarstid för begäran och kursens ålder i prestandadata

## Installation

### Från GitHub Releases

Hämta `.deb`, `.rpm`, `.tar.gz`, wheel och `SHA256SUMS`-filer från [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Verifiera en hämtning med `sha256sum --ignore-missing --check SHA256SUMS`. Utgåvor efter 1.0.0 innehåller även signerad byggproveniens; bekräfta att en fil kommer från det här arkivets utgivningsarbetsflöde med `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Använd filnamnen från den valda utgåvan. Inbyggda paket installerar `/usr/bin/check_bitcoin_price` och `/usr/lib/nagios/plugins/check_bitcoin_price`; RPM-paketet tillhandahåller även `/usr/lib64/nagios/plugins/check_bitcoin_price`. Det paketerade kommandot kör Python i isolerat läge, så det ignorerar `PYTHONPATH` och moduler i arbetskatalogen; systemets pakethanterare löser beroenden för Python och `requests`. De innehåller arkitekturoberoende Python-kod och kräver en distribution som tillhandahåller Python 3.12 eller senare.

### Från källkod

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### För utveckling

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Användning

### Grundläggande användning

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Med tröskelvärden

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Individuella tröskelvärden

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Annan valuta

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Anpassad tidsgräns

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Aktualitet och budget för återförsök

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

En kurs som har en leverantörstidsstämpel får som standard vara högst en timme
gammal. Slutpunkter som bara returnerar ett pris fortsätter att fungera när
`--max-age` utelämnas. Med `--max-age` returnerar saknade, ogiltiga, framtida
eller föråldrade leverantörstidsstämplar `UNKNOWN`; pluginet ersätter inte
leverantörens kurstid med den lokala hämtningstiden. En tidsstämpel som ligger
exakt på åldersgränsen godtas. Framtida tidsstämplar avvisas alltid.

Som standard tillåts ett återförsök. Endast anslutningsfel, tidsgränser och
HTTP-svaren 408/429/500/502/503/504 försöks igen. Fördröjningen börjar på 0,5
sekunder och fördubblas vid efterföljande återförsök; `Retry-After` i sekunder
och HTTP-datum har företräde. Alla försök, svarsläsningar, JSON-avkodning och
väntetider för återförsök delar på budgeten för `--timeout`. Om en väntetid för
återförsök inte ryms returneras `UNKNOWN` omedelbart med det fel som utlöste
försöket, till exempel `HTTP 429` eller `ConnectionError`, inte ett
tidsgränsfel. Autentiseringsfel, andra permanenta HTTP-fel, ogiltig JSON och
svar större än 64 KiB avkodad data försöks inte igen. Använd `--retries 0` för
att inaktivera återförsök.

### Reservkällor för kurser

Använd upprepningsbara `--fallback-url URL`-flaggor med CoinGecko-kompatibla
slutpunkter. Lägg till exempel till
`--fallback-url https://quotes.example.org/simple/price`. Varje källa får en
lika stor andel av den återstående tidsfristen för begäran, inklusive sina
återförsök. Ett tillfälligt fel eller en fördröjning för återförsök som är
längre än den andelen går vidare till nästa källa. Fel vid TLS-verifiering,
permanenta HTTP-fel och ogiltiga kurser returnerar UNKNOWN. Varje kurssvar är
begränsat till 64 KiB avkodad data. När reservkällor är konfigurerade anger
statusen den svarande källan som `primary`, `fallback1` och så vidare, utan att
skriva ut dess URL.

### Rörelse under kort tidsfönster

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Ge övervakningsanvändaren en privat skrivbar tillståndskatalog på ett lokalt
Linux- eller macOS-filsystem. Behåll den intilliggande `.lock`-filen på plats
mellan kontroller. Använd en separat tillståndsfil per tidsfönster. Valutor har
oberoende historik i den. Standardfönstret är 3600 sekunder. Varje giltig kurs
behöver en leverantörstidsstämpel inom tidsfönstret och åldersgränsen, som är
en timme om inte `--max-age` anger något annat. Pluginet jämför det aktuella
priset med det äldsta tidigare positiva priset i det fönstret och rapporterar
den faktiska förflutna tiden i sekunder. Upprepade tidsstämplar skapar inga
ytterligare mätpunkter. En första mätpunkt, utgången historik eller skadad JSON
startar en ny baslinje; fönstermätvärdet är okänt tills det finns en jämförbar
mätpunkt. Andra larm gäller fortfarande. Ej skrivbart tillstånd, en tillstånds-
eller låsfil som är en symbolisk länk, eller en kurs som är äldre än den senast
registrerade mätpunkten returnerar UNKNOWN. Det teckensatta mätvärdet
`bitcoin_move_window` använder symmetriska varnings- och kritiska intervall.
Likhet vid en gräns utlöser inget larm.

Pluginet öppnar tillståndskatalogen en gång per kontroll och arbetar relativt
till den, så en sökvägskomponent som byts ut under kontrollen kan inte
omdirigera låsningen, läsningen eller skrivningen. Symboliska länkar i
katalogdelen av sökvägen följs när kontrollen startar, vilket gör att
plattformslänkar som `/var` på macOS fortsätter att fungera.
Tillståndskatalogen och dess överordnade kataloger får därför inte vara
skrivbara av andra användare. Tillstånds- och låsfiler skapas med rättigheterna
0600.

### Daglig procentuell rörelse

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Förändringströsklar mäter absolutvärdet av CoinGeckos teckensatta 24-timmars
procentuella förändring i vald valuta. En förändring exakt på en tröskel
utlöser inget larm. Om båda trösklarna anges får varningsvärdet inte överstiga
det kritiska värdet. Saknad eller ogiltig nödvändig förändringsdata returnerar
`UNKNOWN`. Pris- och förändringslarm kan kombineras; högsta allvarlighetsgrad
vinner, och pris har företräde när allvarlighetsgraderna är lika.

## Kommandoradsflaggor

| Flagga | Beskrivning |
|--------|-------------|
| `-w`, `--warning` | Varningsintervall för tröskelvärde (format: LOW:HIGH) |
| `-c`, `--critical` | Kritiskt intervall för tröskelvärde (format: LOW:HIGH) |
| `--warning-low` | Varningströskel för lågt pris |
| `--warning-high` | Varningströskel för högt pris |
| `--critical-low` | Kritisk tröskel för lågt pris |
| `--critical-high` | Kritisk tröskel för högt pris |
| `--currency` | Valutakod på 2–16 bokstäver eller siffror (standard: usd) |
| `--timeout` | Total budget i sekunder för API-begäran och återförsök, inklusive decimaltal (standard: 10) |
| `--retries` | Ytterligare försök vid tillfälliga fel, 0–5 (standard: 1) |
| `--max-age` | Maximal ålder i sekunder för leverantörskurs och krav på tidsstämpel; tidsstämplade kurser har standardvärdet 3600 |
| `--warning-change` | Varningsgräns för absolut procentuell rörelse under 24 timmar |
| `--critical-change` | Kritisk gräns för absolut procentuell rörelse under 24 timmar |
| `--api-url` | Primär API-URL |
| `--fallback-url` | Ytterligare kompatibel slutpunkt; upprepa i önskad ordning |
| `--state-file` | JSON-fil för rörelsehistorik |
| `--move-window` | Rörelsefönster i sekunder (standard: 3600) |
| `--warning-move`, `--critical-move` | Absoluta rörelsetrösklar i procent för tidsfönstret |
| `-v`, `--verbose` | Aktivera utförlig utdata |
| `-V`, `--version` | Visa version |
| `-h`, `--help` | Visa hjälpmeddelande |

## Nagios-konfiguration

### Kommandodefinition

Ställ in Nagios-resursmakrot `$USER1$` till pluginkatalogen (de inbyggda paketen använder `/usr/lib/nagios/plugins`). Lägg till i din Nagios-konfiguration för kommandon:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Tjänstedefinition

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

### Icinga2-konfiguration

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

## Slutkoder

Ogiltiga argument, icke-positiva tidsgränser, ogiltiga tröskelintervall och
felaktigt formaterade API-priser returnerar `UNKNOWN` (slutkod 3).
Tröskelvärden måste vara ändliga, icke-negativa tal där varje nedre gräns inte
är större än sin övre gräns. Valutan måste bestå av 2–16 bokstäver eller
siffror. Ogiltig konfiguration avvisas innan API:et kontaktas. Priser måste
vara ändliga och icke-negativa, angivna som JSON-tal eller enkla
decimalsträngar som `"43521.5"`. Ett svar utan den begärda valutan anger den,
till exempel `Response has no EUR price`. Ogiltiga svar skickar inga
prestandadata. Utförlig diagnostik skrivs till stderr så att stdout bara
innehåller en enstaka övervakningsstatusrad.

| Kod | Status | Beskrivning |
|-----|--------|-------------|
| 0 | OK | Priset ligger inom godkänt intervall |
| 1 | WARNING | Priset passerade varningströskeln |
| 2 | CRITICAL | Priset passerade den kritiska tröskeln |
| 3 | UNKNOWN | Ett fel inträffade (API-fel, tidsgräns osv.) |

## Prestandadata

Pluginet skriver ut prestandadata i standardformat för Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Prestandadata för priset inkluderar konfigurerade varnings-/kritiska intervall
och ett minimum på noll. Tröskelvärden skrivs ut i full decimalnotation, aldrig
avrundade eller i exponentform, så att stora värden som `14500000:16250000`
förblir tolkningsbara. Svarstiden inkluderar alla försök och fördröjningar.
Kursens ålder matas endast ut när leverantören anger en giltig tidsstämpel;
daglig förändring matas ut när den är tillgänglig. Förändringsintervall är
symmetriska kring noll. Ogiltig eller föråldrad data ger `UNKNOWN` utan
prisprestandadata. Dessa mätvärden kan användas med grafverktyg som
PNP4Nagios, Grafana eller InfluxDB.

## API

Detta plugin använder [CoinGecko API](https://www.coingecko.com/en/api) som standard, vilket är kostnadsfritt och inte kräver någon API-nyckel. Hastighetsbegränsningar gäller.

Anpassade slutpunkter måste använda samma svarsstruktur: `bitcoin.<currency>`
för pris, `bitcoin.last_updated_at` för UNIX-tidsstämpel i sekunder och
`bitcoin.<currency>_24h_change` för teckensatt daglig procentuell rörelse.
Endast pris krävs när `--max-age` och förändringströsklarna utelämnas. En
tidsstämpel som finns med kontrolleras ändå: den får inte ligga i framtiden
eller vara mer än en timme gammal. Det avkodade svaret måste rymmas inom
64 KiB.

Valutor som stöds inkluderar bland annat: usd, eur, gbp, jpy, aud, cad, chf, cny och många fler.

## Säkerhet

Åtgärderna nedan är implementerade i den aktuella koden. De begränsar vad en
felaktigt fungerande slutpunkt eller en lokal användare kan göra mot
övervakningsvärden; de gör inte själva kursen pålitlig.

- HTTPS-certifikat verifieras med standardinställningarna i `requests`, och
  ingen flagga inaktiverar verifieringen. En anpassad `--api-url` som använder
  vanlig `http://` har inget sådant skydd.
- DNS, anslutning, läsningar, återförsök och fördröjning delar på tidsfristen
  för `--timeout`. En motpart som skickar data långsamt kan inte förlänga den.
- Varje svar är begränsat till 64 KiB efter dekomprimering, och
  omdirigeringskroppar kasseras olästa.
- Fel vid begäran skriver bara ut en HTTP-status eller en felklass, eftersom en
  anpassad `--api-url` kan innehålla autentiseringsuppgifter.
- Kommandot som installeras av `.deb` och `.rpm` kör Python i isolerat läge.
  Det ignorerar `PYTHONPATH`, användarens site-katalog och moduler i
  arbetskatalogen. En `pip`-installation använder det vanliga konsolskriptet
  och följer den miljö där den installerats.
- Rörelsetillstånd läses och skrivs utan att följa en symbolisk länk vid
  tillstånds- eller låsfilnamnet, relativt till en katalog som öppnas en gång
  per kontroll.
- Utgåvans tillgångar har intyg om byggproveniens utöver `SHA256SUMS`; se
  [Från GitHub Releases](#from-github-releases).

## Uppgradering från 1.0.0

Dessa ändringar ingår i 2.0.0.

- En kurs med en leverantörstidsstämpel som är äldre än en timme returnerar
  `UNKNOWN` om inte ett större värde för `--max-age` anges. Slutpunkter som
  inte returnerar någon tidsstämpel påverkas inte.
- `--currency` godtar endast 2–16 bokstäver eller siffror.
- Numeriska strängar med sifferavgränsare eller omgivande blanksteg avvisas.
- En väntetid för återförsök som inte ryms i budgeten rapporterar det
  underliggande felet i stället för `API request timed out`.
- De inbyggda paketen tar inte längre hänsyn till `PYTHONPATH`.
- Tröskelvärden på en miljon eller mer visas i prestandadata som vanliga
  decimaltal i stället för exponentnotation.

## Lokalisering

Hjälptext i CLI, valideringsfel och pluginets statusbeskrivningar har stöd för 45 språkversioner (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) med hjälp av inbäddade kataloger som laddas via standardbiblioteket. Upplösningen kontrollerar `--lang`, sedan `LC_ALL`, `LC_MESSAGES` och `LANG`, och faller tillbaka till `en`. Nagios statusprefix (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) och prestandadata förblir oförändrade på alla språk.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Utveckling

Installera [mise](https://mise.jdx.dev/getting-started.html) och kör sedan utvecklingsinstallationen ovan. `mise.toml` låser versionerna av Python och uv. Utvecklingsverktyg deklareras i `pyproject.toml` och löses i den incheckade filen `uv.lock`.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Installera commit-hooks efter installationen:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Använd `mise exec -- uv add --dev <tool>` eller `mise exec -- uv add <dependency>` för att uppdatera beroenden och checka in både `pyproject.toml` och `uv.lock`.

CI testar Python 3.12 och 3.13 på Linux samt Python 3.13 på macOS. Varje PR kör även paketvalidering, beroendegranskning och CodeQL, samt installerar `.deb` på Ubuntu och `.rpm` på Fedora. Byggda distributioner finns tillgängliga som artefakten `distributions` i CI-körningar.

Paketets och CLI:ets version kommer från `check_bitcoin_price/__init__.py`. Se [utgivningsprocessen](../../../CONTRIBUTING.md#releases) för versionshöjningar och automatisk publicering av GitHub-utgåvetillgångar.

## Bidra

Se [CONTRIBUTING.md](../../../CONTRIBUTING.md) för utvecklingsarbetsflöde och krav på signerade commits (signed-off).

## Licens

Detta projekt är licensierat under MIT-licensen - se filen [LICENSE](../../../LICENSE) för detaljer.

## Författare

Thomas Vincent

## Tack till

- [CoinGecko](https://www.coingecko.com/) för tillhandahållandet av ett kostnadsfritt API för kryptovalutor
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
