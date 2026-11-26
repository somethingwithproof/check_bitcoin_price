# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · **Malagasy** · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Plugin Nagios/Icinga hanaraha-maso ny vidin'ny Bitcoin miaraka amin'ny fetra fampitandremana sy fetra sarotra azo amboarina.

## Endri-javatra

- Manara-maso ny vidin'ny Bitcoin amin'ny sandam-bola maro (USD, EUR, GBP, sns.)
- Fetra fampitandremana sy fetra sarotra azo amboarina (ambony sy ambany)
- Vokatra plugin Nagios manara-penitra miaraka amin'ny angon-drakitra momba ny fahaiza-miasa
- Mampiasa ny CoinGecko API (maimaim-poana, tsy mila fanalahidy API)
- Manohana adiresy API namboarina
- Fe-potoana (timeout) azo amboarina
- Fanamarinana ny fahavaozan'ny vidiny amin'ny alalan'ny mari-potoan'ny mpamatsy, miaraka amin'ny fetra adiny iray raha tsy voafaritra
- Fanandramana indray voafetra rehefa tratran'ny fetran'ny fangatahana na olana vonjimaika avy amin'ny API
- Fe-potoana tokana ho an'ny fanandramana rehetra ary fetra 64 KiB ho an'ny valiny tsirairay
- Fampandrenesana azo safidiana amin'ny fiovan'ny isan-jato tanteraka tao anatin'ny 24 ora
- Fetra vidiny, faharetan'ny fangatahana, ary ny taonan'ny vidiny ao amin'ny angon-drakitra momba ny fahaiza-miasa

## Fametrahana

<a name="from-github-releases"></a>

### Avy amin'ny GitHub Releases

Alaivo ny rakitra `.deb`, `.rpm`, `.tar.gz`, wheel, ary `SHA256SUMS` avy amin'ny [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Hamarino ny rakitra nalaina amin'ny alalan'ny `sha256sum --ignore-missing --check SHA256SUMS`. Ny famoahana taorian'ny 1.0.0 koa dia mitondra porofo voasonia momba ny fiavian'ny fanamboarana; hamarino fa avy amin'ny fizotran'ny famoahana ato amin'ity tahiry ity ny rakitra iray amin'ny alalan'ny `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Ampiasao ny anaran-drakitra avy amin'ny famoahana voafidy. Ny fonosana teratany dia mametraka ny `/usr/bin/check_bitcoin_price` sy ny `/usr/lib/nagios/plugins/check_bitcoin_price`; ny RPM koa dia manome ny `/usr/lib64/nagios/plugins/check_bitcoin_price`. Ny baiko ao anatin'ny fonosana dia mandefa ny Python amin'ny fomba mitokana (isolated mode), ka tsy miraharaha ny `PYTHONPATH` sy ny modely ao amin'ny lahatahiry iasana; ny mpitantana fonosan'ny rafitra no mamaha ny fiankinan-dohan'ny Python sy `requests`. Mirakitra kaody Python tsy miankina amin'ny maritrano izy ireo ary mitaky fizarana manome Python 3.12 na vaovao kokoa.

### Avy amin'ny loharanon-kaody

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Ho an'ny fampivoarana

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Fampiasana

### Fampiasana fototra

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Miaraka amin'ny fetra

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Fetra tsirairay

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Vola hafa

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Fe-potoana namboarina

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Fahavaozan'ny vidiny sy ny fetran'ny fanandramana indray

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Ny vidiny misy mari-potoana avy amin'ny mpamatsy dia tsy maintsy adiny iray farafahabetsany raha tsy voafaritra hafa.
Ny adiresy mamerina ny vidiny ihany dia mbola azo ampiasaina rehefa tsy misy `--max-age`.
Rehefa ampiasaina ny `--max-age`, ny mari-potoana avy amin'ny mpamatsy izay tsy hita, tsy manan-kery, amin'ny hoavy, na lany daty dia mamerina `UNKNOWN`; tsy manolo ny fotoan'ny vidin'ny mpamatsy amin'ny fotoana nakana azy teo an-toerana ny plugin. Ny mari-potoana mifanandrify tsara amin'ny fetran'ny taona dia mbola ekena. Ny mari-potoana amin'ny hoavy dia lavina hatrany.

Ny fampiasana mahazatra dia mamela fanandramana indray indray mandeha. Ny hadisoana fifandraisana, ny fahalanian'ny fe-potoana, ary ny valiny HTTP 408/429/500/502/503/504 ihany no andramana indray. Manomboka amin'ny 0.5 segondra ny fotoana fiandrasana ary mitombo avo roa heny amin'ny fanandramana indray manaraka; ny segondra `Retry-After` sy ny daty HTTP no mahazo laharam-pahamehana. Ny fanandramana rehetra, ny famakiana valiny, ny fandikana JSON, ary ny fiandrasana fanandramana indray dia mizara ny tetibolan'ny `--timeout`. Raha tsy tafiditra ao anatin'izany ny fotoana fiandrasana fanandramana indray dia mamerina `UNKNOWN` avy hatrany izy ary mitatitra ny hadisoana nahatonga izany, toy ny `HTTP 429` na `ConnectionError`, fa tsy fahalanian'ny fe-potoana. Tsy andramana indray ny tsy fahombiazan'ny fanamarinana maha-izy, ny hadisoana HTTP maharitra hafa, ny JSON tsy manan-kery, ary ny valiny mihoatra ny 64 KiB aorian'ny fandikana. Ampiasao ny `--retries 0` mba hanafoanana ny fanandramana indray.

### Loharanom-bidy vonjy maika

Ampiasao ny safidy azo averina `--fallback-url URL` miaraka amin'ny adiresy mifanaraka amin'ny CoinGecko.
Ohatra, ampio `--fallback-url https://quotes.example.org/simple/price`.
Ny loharano tsirairay dia mahazo anjara mitovy amin'ny fe-potoana fangatahana tavela, tafiditra ao ny fanandramany indray. Ny tsy fahombiazana vonjimaika na ny fotoana fiandrasana fanandramana indray lava noho izany anjara izany dia mampandroso mankany amin'ny loharano manaraka. Ny tsy fahombiazan'ny fanamarinana TLS, ny hadisoana HTTP maharitra ary ny vidiny tsy manan-kery dia mamerina UNKNOWN. Ny valim-bidy tsirairay dia voafetra ho 64 KiB amin'ny angona voadika.
Rehefa misy loharano vonjy maika voafikirakira, ny toe-javatra dia manondro ny loharano namaly ho `primary`, `fallback1`, sy ny sisa, nefa tsy mampiseho ny URL-ny.

### Fiovan'ny vidiny ao anatin'ny fe-potoana fohy

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Omeo lahatahiry fitahirizana toe-javatra manokana azo soratana ao amin'ny rafi-drakitra Linux na macOS an-toerana ny mpampiasa fanaraha-maso. Tazony eo amin'ny toerany ny rakitra `.lock` mifanila aminy eo anelanelan'ny fanamarinana. Mampiasà rakitra toe-javatra samihafa isaky ny fe-potoana (window). Manana tantara mahaleo tena ao anatiny ny sandam-bola tsirairay.
Ny fe-potoana mahazatra dia 3600 segondra. Ny vidiny manan-kery tsirairay dia mila mari-potoan'ny mpamatsy ao anatin'ny fe-potoana sy ny fetran'ny taona, izay adiny iray raha tsy misy hafa napetraky ny `--max-age`. Ampitahain'ny plugin amin'ny vidiny miabo taloha indrindra tao anatin'izany fe-potoana izany ny vidiny ankehitriny ary tateriny ny tena segondra lasa. Tsy mamorona santionany fanampiny ny mari-potoana miverimberina.
Ny santionany voalohany, ny tantara lany daty, na ny JSON simba dia manomboka fototra vaovao; mijanona ho tsy fantatra ny metrika fe-potoana mandra-pisian'ny santionany azo ampitahaina. Mbola mihatra ihany ny fampandrenesana hafa. Mamerina UNKNOWN ny toe-javatra tsy azo soratana, ny rakitra toe-javatra na hidy izay rohy famantarana (symbolic link), na ny vidiny taloha noho ny santionany vaovao indrindra voarakitra. Ny metrika misy marika `bitcoin_move_window` dia mampiasa fetra fampitandremana sy sarotra mitovy roa tonta (symmetric). Ny fitoviana amin'ny fetra dia tsy miteraka fampandrenesana.

Sokafan'ny plugin indray mandeha isaky ny fanamarinana ny lahatahiry toe-javatra ary miasa mifandray amin'izany izy, ka tsy afaka manova lalana ny hidy, ny famakiana, na ny fanoratana ny singan-dalana soloina mandritra ny fanamarinana. Ny rohy famantarana ao amin'ny ampahany lahatahiry amin'ny lalana dia arahina rehefa manomboka ny fanamarinana, izay mitazona ho azo ampiasaina ny rohin'ny sehatra toy ny `/var` amin'ny macOS. Noho izany dia tsy tokony ho azon'ny mpampiasa hafa soratana ny lahatahiry toe-javatra sy ny lahatahiry ray aman-dreniny. Ny rakitra toe-javatra sy hidy dia foronina miaraka amin'ny fomba 0600.

### Fiovan'ny isan-jato isan'andro

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Ny fetran'ny fiovana dia mandrefy ny sanda tanteraka (absolute value) an'ny fiovan'ny isan-jato misy marika tao anatin'ny 24 ora avy amin'ny CoinGecko amin'ny sandam-bola voafidy. Ny fiovana mifanandrify tsara amin'ny fetra dia tsy miteraka fampandrenesana. Raha samy omena ny fetra roa, dia tsy tokony hihoatra ny fetra sarotra ny fetra fampitandremana. Ny angona fiovana ilaina izay tsy hita na tsy manan-kery dia mamerina `UNKNOWN`. Azo atambatra ny fampandrenesana momba ny vidiny sy ny fiovana; ny haavon'ny hamafiny ambony indrindra no maharesy, ary ny vidiny no mahazo laharam-pahamehana rehefa mitovy ny hamafiny.

## Safidy amin'ny tsipika baiko

| Safidy | Famaritana |
|--------|------------|
| `-w`, `--warning` | Fetra fampitandremana (endrika: LOW:HIGH) |
| `-c`, `--critical` | Fetra sarotra (endrika: LOW:HIGH) |
| `--warning-low` | Fetra fampitandremana ho an'ny vidiny ambany |
| `--warning-high` | Fetra fampitandremana ho an'ny vidiny ambony |
| `--critical-low` | Fetra sarotra ho an'ny vidiny ambany |
| `--critical-high` | Fetra sarotra ho an'ny vidiny ambony |
| `--currency` | Kaodin-tsandam-bola misy litera na isa 2-16 (mahazatra: usd) |
| `--timeout` | Tetibolan'ny fangatahana/fanandramana indray API manontolo amin'ny segondra, tafiditra ao ny isa misy faingo (mahazatra: 10) |
| `--retries` | Fanandramana vonjimaika fanampiny, 0–5 (mahazatra: 1) |
| `--max-age` | Taona farafahabetsan'ny vidin'ny mpamatsy amin'ny segondra ary mitaky mari-potoana; ny vidiny misy mari-potoana dia 3600 raha tsy voafaritra |
| `--warning-change` | Fetra fampitandremana ho an'ny fiovan'ny isan-jato tanteraka ao anatin'ny 24 ora |
| `--critical-change` | Fetra sarotra ho an'ny fiovan'ny isan-jato tanteraka ao anatin'ny 24 ora |
| `--api-url` | URL API fototra |
| `--fallback-url` | Adiresy mifanaraka fanampiny; avereno araka ny filaharan'ny safidy |
| `--state-file` | Rakitra JSON misy ny tantaran'ny fihetsiky ny vidiny |
| `--move-window` | Fe-potoana fanaraha-maso ny fihetsika amin'ny segondra (mahazatra: 3600) |
| `--warning-move`, `--critical-move` | Fetra tanteraka ho an'ny fihetsika ao anatin'ny fe-potoana amin'ny isan-jato |
| `-v`, `--verbose` | Alefa ny famoahana antsipiriany |
| `-V`, `--version` | Asehoy ny kinova |
| `-h`, `--help` | Asehoy ny hafatra fanampiana |

## Fikirakirana Nagios

### Famaritana baiko

Apetraho amin'ny lahatahiry plugin ny macro loharanon'ny Nagios `$USER1$` (ny fonosana teratany dia mampiasa `/usr/lib/nagios/plugins`). Ampio ao amin'ny fikirakirana baiko Nagios-nao:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Famaritana serivisy

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

### Fikirakirana Icinga2

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

## Kaody fivoahana

Ny tohan-kevitra tsy manan-kery, ny fe-potoana tsy mihoatra ny aotra, ny fetra tsy manan-kery, ary ny vidiny API simba endrika dia mamerina `UNKNOWN` (fivoahana 3). Ny fetra dia tsy maintsy isa voafetra sy tsy latsaky ny aotra, ary ny fetra ambany tsirairay dia tsy tokony hihoatra ny fetra ambony mifandraika aminy. Ny sandam-bola dia tsy maintsy litera na isa 2-16. Lavina ny fikirakirana tsy manan-kery alohan'ny hifandraisana amin'ny API. Ny vidiny dia tsy maintsy isa voafetra sy tsy latsaky ny aotra, omena ho isa JSON na tady isa tsotra toy ny `"43521.5"`. Ny valiny tsy misy ny sandam-bola nangatahina dia manonona izany, ohatra `Response has no EUR price`. Tsy mamoaka angon-drakitra momba ny fahaiza-miasa ny valiny tsy manan-kery. Mankany amin'ny stderr ny fanadihadiana amin'ny antsipiriany mba ho andalana toe-javatra fanaraha-maso tokana ihany no ao amin'ny stdout.

| Kaody | Toe-javatra | Famaritana |
|-------|-------------|------------|
| 0 | OK | Ao anatin'ny fetra azo ekena ny vidiny |
| 1 | WARNING | Nihoatra ny fetra fampitandremana ny vidiny |
| 2 | CRITICAL | Nihoatra ny fetra sarotra ny vidiny |
| 3 | UNKNOWN | Nisy hadisoana nitranga (tsy fahombiazan'ny API, lany fe-potoana, sns.) |

## Angon-drakitra momba ny fahaiza-miasa

Mamoaka angon-drakitra momba ny fahaiza-miasa amin'ny endrika Nagios manara-penitra ny plugin:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Ny angon-drakitra momba ny fahaiza-miasa ho an'ny vidiny dia ahitana ny fetra fampitandremana/sarotra voafikirakira ary farafahakeliny aotra. Ny fetra dia atao pirinty amin'ny endrika desimaly feno, tsy boriborina na atao amin'ny endrika exponent mihitsy, mba hijanonan'ny sanda lehibe toy ny `14500000:16250000` ho azo vakina. Ny fotoanan'ny fangatahana dia ahitana ny fanandramana rehetra sy ny fotoana fiandrasana. Ny taonan'ny vidiny dia avoaka rehefa manome mari-potoana manan-kery ihany ny mpamatsy; ny fiovana isan'andro dia avoaka rehefa misy. Ny fetran'ny fiovana dia mitovy roa tonta manodidina ny aotra. Ny angona tsy manan-kery na lany daty dia miteraka `UNKNOWN` tsy misy angon-drakitra momba ny fahaiza-miasa ho an'ny vidiny. Ireo metrika ireo dia azo ampiasaina amin'ny fitaovana fanaovana sary tahaka ny PNP4Nagios, Grafana, na InfluxDB.

## API

Mampiasa ny [CoinGecko API](https://www.coingecko.com/en/api) ity plugin ity raha tsy voafaritra hafa, izay maimaim-poana ary tsy mila fanalahidy API. Mihatra ny fetran'ny tahan'ny fangatahana.

Ny adiresy namboarina dia tsy maintsy mampiasa endrika valiny mitovy: `bitcoin.<currency>` ho an'ny vidiny, `bitcoin.last_updated_at` ho an'ny segondra mari-potoana UNIX, ary `bitcoin.<currency>_24h_change` ho an'ny fiovan'ny isan-jato isan'andro misy marika. Ny vidiny ihany no takiana rehefa tsy misy `--max-age` sy ny fetran'ny fiovana. Mbola hamarinina ihany ny mari-potoana raha misy: tsy tokony ho amin'ny hoavy na mihoatra ny adiny iray ny taonany. Tsy maintsy tafiditra ao anatin'ny 64 KiB ny valiny voadika.

Ny sandam-bola tohanana dia ahitana: usd, eur, gbp, jpy, aud, cad, chf, cny, sy ny maro hafa.

## Fiarovana

Ireto fepetra eto ambany ireto dia napetraka ao amin'ny kaody ankehitriny. Mametra izay azon'ny adiresy maditra na mpampiasa an-toerana atao amin'ny mpampiantrano fanaraha-maso izy ireo; tsy mahatonga ny vidiny tenany ho azo itokisana izy ireo.

- Hamarinina amin'ny alalan'ny fepetra mahazatra an'ny `requests` ny taratasy fanamarinana HTTPS, ary tsy misy safidy manafoana ny fanamarinana. Ny `--api-url` namboarina mampiasa `http://` tsotra dia tsy manana fiarovana toy izany.
- Ny DNS, ny fifandraisana, ny famakiana, ny fanandramana indray, ary ny fotoana fiandrasana dia mizara ny fe-potoana farany `--timeout`. Ny mpiara-miasa mandefa angona miadana dia tsy afaka manitatra izany.
- Ny valiny tsirairay dia voafetra ho 64 KiB aorian'ny famahana fanerena (decompression), ary ny vatan'ny famerenana lalana (redirect) dia ariana tsy vakina.
- Ny tsy fahombiazan'ny fangatahana dia mampiseho toe-javatra HTTP na sokajy hadisoana ihany, satria ny `--api-url` namboarina dia mety mirakitra fahazoan-dalana.
- Ny baiko napetraky ny `.deb` sy `.rpm` dia mandefa ny Python amin'ny fomba mitokana. Tsy miraharaha ny `PYTHONPATH`, ny lahatahiry site-n'ny mpampiasa, ary ny modely ao amin'ny lahatahiry iasana izy. Ny fametrahana `pip` dia mampiasa ny script console mahazatra ary manaraka ny tontolo nametrahana azy.
- Ny toe-javatry ny fihetsika dia vakina sy soratana tsy manaraka rohy famantarana eo amin'ny anaran'ny rakitra toe-javatra na hidy, mifandray amin'ny lahatahiry sokafana indray mandeha isaky ny fanamarinana.
- Ny rakitra famoahana dia mitondra fanamarinana fiavian'ny fanamboarana ankoatra ny `SHA256SUMS`; jereo ny [Avy amin'ny GitHub Releases](#from-github-releases).

## Fanavaozana avy amin'ny 1.0.0

Ireto fanovana ireto dia navoaka tao amin'ny 2.0.0.

- Ny vidiny misy mari-potoana avy amin'ny mpamatsy mihoatra ny adiny iray dia mamerina `UNKNOWN` raha tsy omena `--max-age` lehibe kokoa. Tsy voakasika ny adiresy tsy mamerina mari-potoana.
- Ny `--currency` dia manaiky litera na isa 2-16 ihany.
- Lavina ny tady isa misy mpanasaraka isa na elanelana manodidina.
- Ny fotoana fiandrasana fanandramana indray tsy tafiditra ao anatin'ny tetibola dia mitatitra ny tena hadisoana fototra fa tsy `API request timed out`.
- Tsy manaja ny `PYTHONPATH` intsony ny fonosana teratany.
- Ny fetra iray tapitrisa na mihoatra dia miseho ao amin'ny angon-drakitra momba ny fahaiza-miasa ho desimaly tsotra fa tsy endrika exponent.

## Fandikana sy fampifanarahana amin'ny fiteny

Ny fanampiana CLI, ny hadisoana fanamarinana, ary ny famaritana toe-javatry ny plugin dia manohana fiteny sy faritra 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) amin'ny alalan'ny katalogy tafiditra ao anatiny izay ampakarina amin'ny stdlib. Ny famahana ny fiteny dia manamarina ny `--lang`, avy eo `LC_ALL`, `LC_MESSAGES`, ary `LANG`, ary miverina amin'ny `en` raha tsy hita. Ny tovana aloha amin'ny toe-javatra Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) sy ny angon-drakitra momba ny fahaiza-miasa dia tsy miova amin'ny fiteny rehetra.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Fampivoarana

Apetraho ny [mise](https://mise.jdx.dev/getting-started.html), avy eo tanteraho ny fanomanana fampivoarana etsy ambony. Ny `mise.toml` dia mamatotra ny kinovan'ny Python sy uv. Ny fitaovana fampivoarana dia voambara ao amin'ny `pyproject.toml` ary voavaha ao amin'ny `uv.lock` voatahiry.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Apetraho ny commit hooks aorian'ny fanomanana:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Ampiasao ny `mise exec -- uv add --dev <tool>` na `mise exec -- uv add <dependency>` hanavaozana ny fiankinan-doha ary ataovy commit ny `pyproject.toml` sy ny `uv.lock`.

Ny CI dia manamarina ny Python 3.12 sy 3.13 amin'ny Linux ary ny Python 3.13 amin'ny macOS. Ny PR tsirairay koa dia mandefa fanamarinana fonosana, fanaraha-maso fiankinan-doha, ary CodeQL, ary mametraka ny `.deb` amin'ny Ubuntu sy ny `.rpm` amin'ny Fedora. Ny fizarana namboarina dia hita ao amin'ny artifact `distributions` mandritra ny fandehan'ny CI.

Ny kinovan'ny fonosana sy ny CLI dia avy amin'ny `check_bitcoin_price/__init__.py`. Jereo ny [fizotran'ny famoahana](../../../CONTRIBUTING.md#releases) ho an'ny fampiakarana kinova sy ny famoahana mandeha ho azy ny rakitra GitHub release.

## Fandraisana anjara

Jereo ny [CONTRIBUTING.md](../../../CONTRIBUTING.md) ho an'ny fizotran'ny fampivoarana sy ny fepetra takiana amin'ny commit voasonia.

## Lisansa

Ity tetikasa ity dia eo ambany Lisansa MIT - jereo ny rakitra [LICENSE](../../../LICENSE) ho an'ny antsipiriany.

## Mpanoratra

Thomas Vincent

## Fisaorana

- [CoinGecko](https://www.coingecko.com/) amin'ny fanomezana API vola nomerika maimaim-poana
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
