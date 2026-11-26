# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (28 locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · **Bosanski** · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Hrvatski](../hr/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Српски](../sr/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Nagios/Icinga dodatak za praćenje cijene Bitcoina sa podesivim pragovima upozorenja i kritičnog stanja.

## Mogućnosti

- Praćenje cijene Bitcoina u više valuta (USD, EUR, GBP itd.)
- Podesivi pragovi upozorenja i kritičnog stanja (gornji i donji)
- Standardni ispis Nagios dodatka sa podacima o performansama
- Koristi CoinGecko API (besplatan, bez potrebe za API ključem)
- Podrška za prilagođene krajnje tačke API-ja
- Podesivo vremensko ograničenje
- Provjera svježine kotacije putem vremenskih oznaka dobavljača, sa podrazumijevanim ograničenjem od jednog sata
- Ograničeni ponovni pokušaji za ograničenja učestalosti zahtjeva i privremene greške API-ja
- Jedinstven vremenski rok za sve pokušaje i ograničenje od 64 KiB za svaki odgovor
- Opciona upozorenja na apsolutno 24-satno procentualno kretanje
- Pragovi cijene, trajanje zahtjeva i starost kotacije u podacima o performansama

## Instalacija

### Sa GitHub Releases

Preuzmite `.deb`, `.rpm`, `.tar.gz`, wheel i `SHA256SUMS` datoteke sa [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Provjerite preuzetu datoteku pomoću `sha256sum --ignore-missing --check SHA256SUMS`. Izdanja nakon verzije 1.0.0 sadrže i potpisane dokaze porijekla izgradnje; potvrdite da datoteka potiče iz radnog toka izdanja ovog repozitorija pomoću `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Koristite nazive datoteka iz odabranog izdanja. Izvorni paketi instaliraju `/usr/bin/check_bitcoin_price` i `/usr/lib/nagios/plugins/check_bitcoin_price`; RPM paket dodatno pruža `/usr/lib64/nagios/plugins/check_bitcoin_price`. Upakovana naredba pokreće Python u izolovanom načinu rada, pa ignoriše `PYTHONPATH` i module u radnom direktoriju; sistemski upravitelj paketa rješava zavisnosti za Python i `requests`. Paketi sadrže Python kod nezavisan od arhitekture i zahtijevaju distribuciju sa Pythonom 3.12 ili novijim.

### Iz izvornog koda

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Za razvoj

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Upotreba

### Osnovna upotreba

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Sa pragovima

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Pojedinačni pragovi

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Druga valuta

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Prilagođeno vremensko ograničenje

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Svježina kotacije i budžet ponovnih pokušaja

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Kotacija koja sadrži vremensku oznaku dobavljača podrazumijevano smije biti stara najviše jedan sat.
Krajnje tačke koje vraćaju samo cijenu ostaju upotrebljive kada `--max-age` nije zadat.
Uz `--max-age`, nedostajuće, neispravne, buduće ili zastarjele vremenske oznake dobavljača vraćaju `UNKNOWN`; dodatak ne zamjenjuje vrijeme kotacije dobavljača lokalnim vremenom preuzimanja. Vremenska oznaka tačno na granici starosti ostaje prihvatljiva. Buduće vremenske oznake se uvijek odbijaju.

Podrazumijevano je dozvoljen jedan ponovni pokušaj. Ponavljaju se samo greške mrežne veze, istek vremena i HTTP odgovori 408/429/500/502/503/504. Čekanje počinje od 0.5 sekundi i udvostručava se za naredne pokušaje; zaglavlje `Retry-After` u sekundama i HTTP datumi imaju prednost. Svi pokušaji, čitanje odgovora, dekodiranje JSON-a i čekanje između pokušaja dijele ukupni `--timeout` budžet. Ako čekanje za ponovni pokušaj ne stane u budžet, dodatak odmah vraća `UNKNOWN` i u izvještaju navodi grešku koja ga je izazvala, kao što je `HTTP 429` ili `ConnectionError`, a ne istek vremena. Greške autentifikacije, druge trajne HTTP greške, neispravan JSON i odgovori veći od 64 KiB dekodiranih podataka se ne ponavljaju. Koristite `--retries 0` da isključite ponovne pokušaje.

### Rezervni izvori kotacija

Koristite opciju `--fallback-url URL` koja se može ponoviti sa krajnjim tačkama kompatibilnim sa CoinGecko API-jem.
Na primjer, dodajte `--fallback-url https://quotes.example.org/simple/price`.
Svaki server dobija jednak dio preostalog vremenskog roka zahtjeva, uključujući njegove ponovne pokušaje. Privremena greška ili kašnjenje ponovnog pokušaja duže od tog dijela prelazi na sljedeći izvor. Greške TLS provjere, trajne HTTP greške i neispravne kotacije vraćaju UNKNOWN. Svaki odgovor sa kotacijom ograničen je na 64 KiB dekodiranih podataka. Kada su rezervni izvori konfigurisani, status označava izvor koji je odgovorio kao `primary`, `fallback1` itd., bez ispisa njegovog URL-a.

### Kretanje u kratkom prozoru

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Osigurajte korisniku za nadzor privatni direktorij stanja sa pravom pisanja na lokalnom Linux ili macOS sistemu datoteka. Zadržite prateću `.lock` datoteku na istom mjestu između provjera. Koristite zasebnu datoteku stanja za svaki prozor. Valute unutar nje imaju nezavisne historije. Podrazumijevani prozor iznosi 3600 sekundi. Svaka validna kotacija mora imati vremensku oznaku dobavljača unutar prozora i granice starosti, koja iznosi jedan sat osim ako `--max-age` ne zadaje drugu vrijednost. Dodatak poredi trenutnu cijenu sa najstarijom prethodnom pozitivnom cijenom u tom prozoru i prijavljuje stvarno protekle sekunde. Ponovljene vremenske oznake ne stvaraju dodatne uzorke. Prvi uzorak, istekla historija ili oštećen JSON pokreću novu početnu vrijednost; metrika prozora ostaje nepoznata dok ne postoji uporediv uzorak. Ostala upozorenja i dalje vrijede. Stanje u koje nije moguće pisati, simbolička veza umjesto datoteke stanja ili zaključavanja, ili kotacija starija od najnovijeg zabilježenog uzorka vraćaju UNKNOWN. Predznačena metrika `bitcoin_move_window` koristi simetrične raspone upozorenja i kritičnog stanja. Jednakost sa granicom ne pokreće upozorenje.

Dodatak otvara direktorij stanja jednom po provjeri i radi relativno u odnosu na njega, tako da komponenta putanje zamijenjena tokom provjere ne može preusmjeriti zaključavanje, čitanje ili pisanje. Simboličke veze u dijelu putanje koji predstavlja direktorij prate se na početku provjere, čime sistemske veze poput `/var` na macOS računaru ostaju upotrebljive. Zbog toga direktorij stanja i njegovi nadređeni direktoriji ne smiju biti dostupni za pisanje drugim korisnicima. Datoteke stanja i zaključavanja kreiraju se sa dozvolama 0600.

### Dnevno procentualno kretanje

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Pragovi promjene mjere apsolutnu vrijednost CoinGecko predznačene 24-satne procentualne promjene u odabranoj valuti. Promjena tačno na pragu ne aktivira upozorenje. Ako su navedena oba praga, upozorenje ne smije premašiti kritični prag. Nedostajući ili neispravni obavezni podaci o promjeni vraćaju `UNKNOWN`. Upozorenja za cijenu i promjenu mogu se kombinovati; pobjeđuje najviši nivo ozbiljnosti, pri čemu cijena ima prednost kada su nivoi jednaki.

## Opcije komandne linije

| Opcija | Opis |
|--------|-------------|
| `-w`, `--warning` | Raspon pragova upozorenja (format: LOW:HIGH) |
| `-c`, `--critical` | Raspon kritičnih pragova (format: LOW:HIGH) |
| `--warning-low` | Prag upozorenja za nisku cijenu |
| `--warning-high` | Prag upozorenja za visoku cijenu |
| `--critical-low` | Kritični prag za nisku cijenu |
| `--critical-high` | Kritični prag za visoku cijenu |
| `--currency` | Kod valute od 2-16 slova ili cifara (podrazumijevano: usd) |
| `--timeout` | Ukupni budžet za API zahtjeve i ponovne pokušaje u sekundama, uključujući decimalne vrijednosti (podrazumijevano: 10) |
| `--retries` | Dodatni pokušaji kod privremenih grešaka, 0-5 (podrazumijevano: 1) |
| `--max-age` | Maksimalna starost kotacije dobavljača u sekundama uz obaveznu vremensku oznaku; kotacije sa oznakom podrazumijevano imaju 3600 |
| `--warning-change` | Granica upozorenja za apsolutno 24-satno procentualno kretanje |
| `--critical-change` | Kritična granica za apsolutno 24-satno procentualno kretanje |
| `--api-url` | Primarni URL API-ja |
| `--fallback-url` | Dodatna kompatibilna krajnja tačka; ponavljajte po željenom redoslijedu |
| `--state-file` | JSON datoteka historije kretanja |
| `--move-window` | Prozor kretanja u sekundama (podrazumijevano: 3600) |
| `--warning-move`, `--critical-move` | Apsolutni pragovi kretanja u prozoru u procentima |
| `-v`, `--verbose` | Omogući detaljan ispis |
| `-V`, `--version` | Prikaži verziju |
| `-h`, `--help` | Prikaži poruku pomoći |

## Nagios postavke

### Definicija naredbe

Postavite Nagios resursni makro `$USER1$` na direktorij dodataka (izvorni paketi koriste `/usr/lib/nagios/plugins`). Dodajte u svoje Nagios postavke naredbi:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Definicija servisa

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

### Icinga2 postavke

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

## Izlazni kodovi

Neispravni argumenti, nepozitivna vremenska ograničenja, neispravni rasponi pragova i pogrešno formatirane cijene sa API-ja vraćaju `UNKNOWN` (izlazni kod 3). Pragovi moraju biti konačni, nenegativni brojevi, pri čemu svaka donja granica ne smije biti veća od gornje granice. Valuta mora imati 2-16 slova ili cifara. Neispravne postavke konfiguracije odbijaju se prije kontaktiranja API-ja. Cijene moraju biti konačne i nenegativne, zadane kao JSON brojevi ili obični decimalni znakovni nizovi kao što je `"43521.5"`. Odgovor bez tražene valute navodi njen naziv, na primjer `Response has no EUR price`. Neispravni odgovori ne ispisuju podatke o performansama. Detaljna dijagnostika šalje se na stderr tako da stdout sadrži jednu statusnu liniju za nadzor.

| Kod | Status | Opis |
|------|--------|-------------|
| 0 | OK | Cijena je unutar prihvatljivog raspona |
| 1 | WARNING | Cijena je prešla prag upozorenja |
| 2 | CRITICAL | Cijena je prešla kritični prag |
| 3 | UNKNOWN | Došlo je do greške (greška API-ja, istek vremena itd.) |

## Podaci o performansama

Dodatak ispisuje podatke o performansama u standardnom Nagios formatu:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Podaci o performansama za cijenu uključuju podešene raspone upozorenja/kritičnog stanja i minimum nula. Pragovi se ispisuju u punom decimalnom zapisu, nikada zaokruženi niti u eksponencijalnom obliku, tako da velike vrijednosti kao što je `14500000:16250000` ostaju čitljive za obradu. Vrijeme zahtjeva uključuje sve pokušaje i čekanja. Starost kotacije ispisuje se samo kada dobavljač dostavi validnu vremensku oznaku; dnevna promjena ispisuje se kada je dostupna. Rasponi promjene simetrični su oko nule. Neispravni ili zastarjeli podaci daju `UNKNOWN` bez podataka o performansama cijene. Ove metrike mogu se koristiti sa alatima za grafički prikaz kao što su PNP4Nagios, Grafana ili InfluxDB.

## API

Ovaj dodatak podrazumijevano koristi [CoinGecko API](https://www.coingecko.com/en/api), koji je besplatan i ne zahtijeva API ključ. Primjenjuju se ograničenja učestalosti zahtjeva.

Prilagođene krajnje tačke moraju koristiti isti oblik odgovora: `bitcoin.<currency>` za cijenu, `bitcoin.last_updated_at` za UNIX vremensku oznaku u sekundama i `bitcoin.<currency>_24h_change` za predznačeno dnevno procentualno kretanje. Samo cijena je obavezna kada `--max-age` i pragovi promjene nisu navedeni. Prisutna vremenska oznaka se ipak provjerava: ne smije biti u budućnosti niti starija od jednog sata. Dekodirani odgovor mora stati u 64 KiB.

Podržane valute uključuju: usd, eur, gbp, jpy, aud, cad, chf, cny i mnoge druge.

## Sigurnost

Mjere navedene u nastavku implementirane su u trenutnom kodu. One ograničavaju šta neispravna krajnja tačka ili lokalni korisnik mogu učiniti računaru za nadzor; same po sebi ne čine kotaciju pouzdanom.

- HTTPS certifikati provjeravaju se podrazumijevanim postavkama biblioteke `requests` i nijedna opcija ne isključuje provjeru. Prilagođeni `--api-url` koji koristi obični `http://` nema takvu zaštitu.
- DNS, mrežna veza, čitanja, ponovni pokušaji i čekanja dijele `--timeout` rok. Server koji šalje podatke sporo ne može ga produžiti.
- Svaki odgovor ograničen je na 64 KiB nakon dekompresije, a tijela preusmjeravanja se odbacuju bez čitanja.
- Greške zahtjeva ispisuju samo HTTP status ili klasu greške, jer prilagođeni `--api-url` može sadržavati pristupne podatke.
- Naredba instalirana putem `.deb` i `.rpm` paketa pokreće Python u izolovanom načinu rada. Ignoriše `PYTHONPATH`, korisnički site direktorij i module u radnom direktoriju. Instalacija putem `pip` koristi standardnu konzolnu skriptu i prati okruženje u kojem je instalirana.
- Stanje kretanja čita se i zapisuje bez praćenja simboličke veze na nazivu datoteke stanja ili zaključavanja, relativno u odnosu na direktorij otvoren jednom po provjeri.
- Datoteke izdanja sadrže atestacije porijekla izgradnje pored `SHA256SUMS`; pogledajte [Sa GitHub Releases](#sa-github-releases).

## Nadogradnja sa verzije 1.0.0

Ove izmjene dolaze u verziji 2.0.0.

- Kotacija sa vremenskom oznakom dobavljača starijom od jednog sata vraća `UNKNOWN` osim ako nije zadat veći `--max-age`. Krajnje tačke koje ne vraćaju vremensku oznaku ostaju nepromijenjene.
- `--currency` prihvata samo 2-16 slova ili cifara.
- Numerički nizovi sa razdjelnicima cifara ili okolnim razmacima se odbijaju.
- Čekanje za ponovni pokušaj koje ne stane u budžet prijavljuje osnovnu grešku umjesto `API request timed out`.
- Izvorni paketi više ne uvažavaju `PYTHONPATH`.
- Pragovi od milion ili više prikazuju se u podacima o performansama kao obični decimalni brojevi umjesto eksponencijalnog zapisa.

## Lokalizacija

Pomoć u komandnoj liniji, greške provjere i opisi statusa dodatka podržavaju 48 lokaliteta (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`) koristeći ugrađene kataloge učitane putem standardne biblioteke. Odabir provjerava `--lang`, zatim `LC_ALL`, `LC_MESSAGES` i `LANG`, uz povratak na `en`. Nagios prefiksi statusa (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) i podaci o performansama ostaju nepromijenjeni u svim lokalitetima.

```bash
check_bitcoin_price --lang bs
LANG=bs_BA.UTF-8 check_bitcoin_price --help
```

## Razvoj

Instalirajte [mise](https://mise.jdx.dev/getting-started.html), a zatim pokrenite gornje postavke za razvoj. `mise.toml` zaključava verzije Pythona i alata uv. Razvojni alati navedeni su u `pyproject.toml` i razriješeni u priloženoj `uv.lock` datoteci.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Instalirajte commit hookove nakon postavljanja:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Koristite `mise exec -- uv add --dev <tool>` ili `mise exec -- uv add <dependency>` za ažuriranje zavisnosti i commitujte obje datoteke `pyproject.toml` i `uv.lock`.

CI provjerava Python 3.12 i 3.13 na Linuxu te Python 3.13 na macOS-u. Svaki PR također pokreće provjeru paketa, reviziju zavisnosti i CodeQL, te instalira `.deb` na Ubuntu i `.rpm` na Fedoru. Izgrađene distribucije dostupne su kao `distributions` artefakt u CI izvršavanjima.

Verzija paketa i CLI-ja dolazi iz `check_bitcoin_price/__init__.py`. Pogledajte [proces izdanja](../../../CONTRIBUTING.md#releases) za ažuriranje verzije i automatizovano objavljivanje datoteka GitHub izdanja.

## Doprinos

Pogledajte [CONTRIBUTING.md](../../../CONTRIBUTING.md) za tok razvoja i zahtjeve za potpisanim commitovima.

## Licenca

Ovaj projekat licenciran je pod MIT licencom - pogledajte datoteku [LICENSE](../../../LICENSE) za detalje.

## Autor

Thomas Vincent

## Zahvale

- [CoinGecko](https://www.coingecko.com/) za pružanje besplatnog API-ja za kriptovalute
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
