# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (28 locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [Bosanski](../bs/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · **Hrvatski** · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Српски](../sr/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Dodatak za Nagios/Icinga za nadzor cijene Bitcoina s prilagodljivim pragovima upozorenja i kritičnog stanja.

## Značajke

- Nadzor cijene Bitcoina u više valuta (USD, EUR, GBP itd.)
- Prilagodljivi pragovi upozorenja i kritičnog stanja (gornji i donji)
- Standardni ispis dodatka Nagios s podatcima o učinkovitosti
- Koristi CoinGecko API (besplatan, bez potrebe za API ključem)
- Podrška za prilagođene krajnje točke API-ja
- Prilagodljivo vremensko ograničenje
- Provjera svježine kotacija pomoću vremenskih oznaka pružatelja, sa zadanim ograničenjem od jednog sata
- Ograničeni ponovni pokušaji za ograničenja broja zahtjeva i privremene pogreške API-ja
- Jedinstveni rok za sve pokušaje i ograničenje od 64 KiB za svaki odgovor
- Neobavezna upozorenja za apsolutno 24-satno postotno kretanje
- Pragovi cijene, trajanje zahtjeva i starost kotacije u podatcima o učinkovitosti

## Instalacija

### S GitHub Releases

Preuzmite datoteke `.deb`, `.rpm`, `.tar.gz`, wheel i `SHA256SUMS` sa stranice [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Provjerite preuzetu datoteku naredbom `sha256sum --ignore-missing --check SHA256SUMS`. Izdanja nakon inačice 1.0.0 također sadrže potpisane dokaze podrijetla gradnje; potvrdite da datoteka potječe iz tijeka izdanja ovog repozitorija naredbom `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Upotrijebite nazive datoteka iz odabranog izdanja. Izvorni paketi instaliraju `/usr/bin/check_bitcoin_price` i `/usr/lib/nagios/plugins/check_bitcoin_price`; RPM paket također pruža `/usr/lib64/nagios/plugins/check_bitcoin_price`. Zapakirana naredba pokreće Python u izoliranom načinu rada te zanemaruje `PYTHONPATH` i module u radnom direktoriju; sustavni upravitelj paketa razrješava ovisnosti za Python i `requests`. Paketi sadrže Python kôd neovisan o arhitekturi i zahtijevaju distribuciju koja pruža Python 3.12 ili noviji.

### Iz izvornog kôda

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

## Uporaba

### Osnovna uporaba

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### S pragovima

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

### Svježina i proračun ponovnih pokušaja

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Kotacija koja nosi vremensku oznaku pružatelja zadano smije biti stara najviše jedan sat.
Krajnje točke koje vraćaju samo cijenu ostaju upotrebljive kada `--max-age` i `--state-file` nisu navedeni.
Uz `--max-age`, nedostajuće, nevaljane, buduće ili zastarjele vremenske oznake pružatelja vraćaju `UNKNOWN`; dodatak ne zamjenjuje vrijeme kotacije pružatelja lokalnim vremenom dohvaćanja. Vremenska oznaka točno na granici starosti ostaje prihvatljiva. Buduće vremenske oznake uvijek se odbijaju.

Zadano je dopušten jedan ponovni pokušaj. Ponavljaju se samo pogreške mrežne veze, isteci vremena čekanja i HTTP odgovori 408/429/500/502/503/504. Odgoda započinje s 0.5 sekundi i udvostručuje se za sljedeće pokušaje; sekunde iz zaglavlja `Retry-After` i HTTP datumi imaju prednost. Svi pokušaji, čitanje odgovora, dekodiranje JSON-a i čekanja između pokušaja dijele ukupni `--timeout` proračun. Čekanje ponovnog pokušaja koje ne stane u proračun odmah vraća `UNKNOWN` i u izvješću navodi pogrešku koja ga je potaknula, poput `HTTP 429` ili `ConnectionError`, a ne istek vremena. Pogreške autentifikacije, druge trajne HTTP pogreške, nevaljan JSON i odgovori veći od 64 KiB dekodiranih podataka ne ponavljaju se. Upotrijebite `--retries 0` za isključivanje ponovnih pokušaja.

### Pričuvni izvori kotacija

Upotrijebite ponovljive mogućnosti `--fallback-url URL` s krajnjim točkama kompatibilnim s CoinGecko API-jem.
Primjerice, dodajte `--fallback-url https://quotes.example.org/simple/price`.
Svaki poslužitelj dobiva jednak udio preostalog roka zahtjeva, uključujući njegove ponovne pokušaje. Privremena pogreška ili odgoda ponovnog pokušaja dulja od tog udjela prelazi na sljedeći izvor. Pogreške TLS provjere, trajne HTTP pogreške i nevaljane kotacije vraćaju UNKNOWN. Svaki odgovor kotacije ograničen je na 64 KiB dekodiranih podataka. Kada su pričuvni izvori podešeni, status označava izvor koji je odgovorio kao `primary`, `fallback1` itd., bez ispisa njegova URL-a.

### Kretanje u kratkom prozoru

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Korisniku za nadzor dodijelite privatan direktorij za pohranu stanja s pravom pisanja na lokalnom datotečnom sustavu Linuxa ili macOS-a. Zadržite pridruženu `.lock` datoteku na mjestu između provjera. Upotrijebite zasebnu datoteku stanja za svaki prozor. Valute unutar nje imaju neovisne povijesti. Zadani prozor iznosi 3600 sekundi. Svaka valjana kotacija treba vremensku oznaku pružatelja unutar prozora i ograničenja starosti, koje iznosi jedan sat osim ako `--max-age` ne određuje drukčije. Dodatak uspoređuje trenutnu cijenu s najstarijom ranijom pozitivnom cijenom u tom prozoru i izvješćuje stvarni broj proteklih sekundi. Ponovljene vremenske oznake ne stvaraju dodatne uzorke. Prvi uzorak, istekla povijest ili oštećeni JSON započinju novu polaznu vrijednost; metrika prozora ostaje nepoznata dok ne postoji usporediv uzorak. Ostala upozorenja i dalje vrijede. Stanje u koje nije moguće zapisivati, simbolička veza umjesto datoteke stanja ili zaključavanja, ili kotacija starija od najnovijeg zabilježenog uzorka vraćaju UNKNOWN. Predznačena metrika `bitcoin_move_window` koristi simetrične raspone upozorenja i kritičnog stanja. Jednakost na ograničenju ne aktivira upozorenje.

Dodatak otvara direktorij stanja jednom po provjeri i radi relativno u odnosu na njega, stoga komponenta staze zamijenjena tijekom provjere ne može preusmjeriti zaključavanje, čitanje ni pisanje. Simboličke veze u dijelu staze koji čini direktorij slijede se na početku provjere, čime sustavne veze poput `/var` na macOS računalu ostaju upotrebljive. Direktorij stanja i njegovi nadređeni direktoriji stoga ne smiju biti dostupni za pisanje drugim korisnicima. Datoteke stanja i zaključavanja stvaraju se s ovlastima 0600.

### Dnevno postotno kretanje

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Pragovi promjene mjere apsolutnu vrijednost CoinGecko predznačene 24-satne postotne promjene u odabranoj valuti. Promjena točno na pragu ne aktivira upozorenje. Ako su zadana oba praga, upozorenje ne smije premašiti kritični prag. Nedostajući ili nevaljani obvezni podatci o promjeni vraćaju `UNKNOWN`. Upozorenja za cijenu i promjenu mogu se kombinirati; prevladava najveća razina ozbiljnosti, pri čemu cijena ima prednost kada su razine jednake.

## Mogućnosti naredbenog retka

| Mogućnost | Opis |
|--------|-------------|
| `-w`, `--warning` | Raspon pragova upozorenja (oblik: LOW:HIGH) |
| `-c`, `--critical` | Raspon kritičnih pragova (oblik: LOW:HIGH) |
| `--warning-low` | Prag upozorenja za nisku cijenu |
| `--warning-high` | Prag upozorenja za visoku cijenu |
| `--critical-low` | Kritični prag za nisku cijenu |
| `--critical-high` | Kritični prag za visoku cijenu |
| `--currency` | Oznaka valute od 2-16 slova ili znamenki (zadano: usd) |
| `--timeout` | Ukupni proračun za API zahtjeve i ponovne pokušaje u sekundama, uključujući decimalne vrijednosti (zadano: 10) |
| `--retries` | Dodatni pokušaji pri privremenim pogreškama, 0-5 (zadano: 1) |
| `--max-age` | Najveća starost kotacije pružatelja u sekundama uz obveznu vremensku oznaku; kotacije s oznakom zadano koriste 3600 |
| `--warning-change` | Ograničenje upozorenja za apsolutno 24-satno postotno kretanje |
| `--critical-change` | Kritično ograničenje za apsolutno 24-satno postotno kretanje |
| `--api-url` | Glavni URL API-ja |
| `--fallback-url` | Dodatna kompatibilna krajnja točka; ponavljajte željenim redoslijedom |
| `--state-file` | JSON datoteka povijesti kretanja |
| `--move-window` | Prozor kretanja u sekundama (zadano: 3600) |
| `--warning-move`, `--critical-move` | Apsolutni pragovi kretanja u prozoru u postocima |
| `-v`, `--verbose` | Uključi opširan ispis |
| `-V`, `--version` | Prikaži inačicu |
| `-h`, `--help` | Prikaži poruku pomoći |

## Postavke za Nagios

### Definicija naredbe

Postavite Nagios makro resursa `$USER1$` na direktorij dodataka (izvorni paketi koriste `/usr/lib/nagios/plugins`). Dodajte u postavke naredbi za Nagios:

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

### Postavke za Icinga2

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

Nevaljani argumenti, nepozitivna vremenska ograničenja, nevaljani rasponi pragova i pogrešno oblikovane cijene iz API-ja vraćaju `UNKNOWN` (izlaz 3). Pragovi moraju biti konačni, nenegativni brojevi, pri čemu svaka donja granica ne smije biti veća od svoje gornje granice. Valuta mora imati 2-16 slova ili znamenki. Nevaljane postavke konfiguracije odbijaju se prije povezivanja s API-jem. Cijene moraju biti konačne i nenegativne, zadane kao JSON brojevi ili obični decimalni nizovi znakova poput `"43521.5"`. Odgovor bez zatražene valute navodi njezinu oznaku, primjerice `Response has no EUR price`. Nevaljani odgovori ne ispisuju podatke o učinkovitosti. Opširna dijagnostika šalje se na stderr tako da stdout sadrži jedan redak statusa nadzora.

| Kod | Status | Opis |
|------|--------|-------------|
| 0 | OK | Cijena je unutar prihvatljivog raspona |
| 1 | WARNING | Cijena je prešla prag upozorenja |
| 2 | CRITICAL | Cijena je prešla kritični prag |
| 3 | UNKNOWN | Dogodila se pogreška (pogreška API-ja, istek vremena itd.) |

## Podatci o učinkovitosti

Dodatak ispisuje podatke o učinkovitosti u standardnom Nagios obliku:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Podatci o učinkovitosti za cijenu uključuju podešene raspone upozorenja/kritičnog stanja i minimum nula. Pragovi se ispisuju u punom decimalnom zapisu, nikada zaokruženi ni u eksponencijalnom obliku, pa velike vrijednosti poput `14500000:16250000` ostaju prikladne za raščlanjivanje. Vrijeme zahtjeva obuhvaća sve pokušaje i odgode. Starost kotacije ispisuje se samo kada pružatelj dostavi valjanu vremensku oznaku; dnevna promjena ispisuje se kada je dostupna. Rasponi promjene simetrični su oko nule. Nevaljani ili zastarjeli podatci daju `UNKNOWN` bez podataka o učinkovitosti cijene. Ove metrike mogu se upotrebljavati s alatima za crtanje grafova poput PNP4Nagios, Grafane ili InfluxDB-a.

## API

Ovaj dodatak zadano upotrebljava [CoinGecko API](https://www.coingecko.com/en/api), koji je besplatan i ne zahtijeva API ključ. Primjenjuju se ograničenja broja zahtjeva.

Prilagođene krajnje točke moraju koristiti isti oblik odgovora: `bitcoin.<currency>` za cijenu, `bitcoin.last_updated_at` za sekunde UNIX vremenske oznake i `bitcoin.<currency>_24h_change` za predznačeno dnevno postotno kretanje. Samo cijena je obvezna kada `--max-age`, `--state-file` i pragovi promjene nisu navedeni. Prisutna vremenska oznaka ipak se provjerava: ne smije biti u budućnosti ni starija od jednog sata. Dekodirani odgovor mora stati u 64 KiB.

Podržane valute uključuju: usd, eur, gbp, jpy, aud, cad, chf, cny i mnoge druge.

## Sigurnost

Mjere u nastavku provedene su u trenutačnom kôdu. One ograničavaju što neispravna krajnja točka ili lokalni korisnik mogu učiniti računalu za nadzor; ne čine samu kotaciju pouzdanom.

- HTTPS certifikati provjeravaju se zadanim postavkama biblioteke `requests` i nijedna mogućnost ne isključuje provjeru. Prilagođeni `--api-url` koji koristi obični `http://` nema takvu zaštitu.
- DNS, mrežna veza, čitanja, ponovni pokušaji i odgode dijele rok `--timeout`. Poslužitelj koji sporo šalje podatke ne može ga produljiti.
- Svaki odgovor ograničen je na 64 KiB nakon dekompresije, a tijela preusmjeravanja odbacuju se bez čitanja.
- Pogreške zahtjeva ispisuju samo HTTP status ili klasu pogreške jer prilagođeni `--api-url` može sadržavati vjerodajnice.
- Naredba instalirana paketima `.deb` i `.rpm` pokreće Python u izoliranom načinu rada. Zanemaruje `PYTHONPATH`, korisnički site direktorij i module u radnom direktoriju. Instalacija pomoću `pip` koristi standardnu konzolnu skriptu i slijedi okruženje u kojem je instalirana.
- Stanje kretanja čita se i zapisuje bez slijeđenja simboličke veze na nazivu datoteke stanja ili zaključavanja, relativno u odnosu na direktorij otvoren jednom po provjeri.
- Datoteke izdanja sadrže atestacije podrijetla gradnje uz `SHA256SUMS`; pogledajte [S GitHub Releases](#s-github-releases).

## Nadogradnja s inačice 1.0.0

Ove promjene isporučuju se u inačici 2.0.0.

- Kotacija s vremenskom oznakom pružatelja starijom od jednog sata vraća `UNKNOWN` osim ako nije zadan veći `--max-age`. Krajnje točke koje ne vraćaju vremensku oznaku ostaju nepromijenjene.
- `--currency` prihvaća samo 2-16 slova ili znamenki.
- Numerički nizovi s razdjelnicima znamenki ili okolnim razmacima odbijaju se.
- Odgoda ponovnog pokušaja koja ne stane u proračun izvješćuje temeljnu pogrešku umjesto `API request timed out`.
- Izvorni paketi više ne uvažavaju `PYTHONPATH`.
- Pragovi od jednog milijuna ili više pojavljuju se u podatcima o učinkovitosti kao obični decimalni brojevi umjesto eksponencijalnog zapisa.

## Lokalizacija

Pomoć u naredbenom retku, pogreške provjere valjanosti i opisi statusa dodatka podržavaju 48 lokaliteta (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`) koristeći ugrađene kataloge učitane standardnom bibliotekom. Razrješavanje provjerava `--lang`, zatim `LC_ALL`, `LC_MESSAGES` i `LANG`, uz povrat na `en`. Nagios prefiksi statusa (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) i podatci o učinkovitosti ostaju nepromijenjeni u svim lokalitetima.

```bash
check_bitcoin_price --lang hr
LANG=hr_HR.UTF-8 check_bitcoin_price --help
```

## Razvoj

Instalirajte [mise](https://mise.jdx.dev/getting-started.html), a zatim pokrenite gornje razvojne postavke. `mise.toml` zaključava inačice Pythona i alata uv. Razvojni alati navedeni su u `pyproject.toml` i razriješeni u priloženoj datoteci `uv.lock`.

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

Upotrijebite `mise exec -- uv add --dev <tool>` ili `mise exec -- uv add <dependency>` za ažuriranje ovisnosti i predajte obje datoteke `pyproject.toml` i `uv.lock`.

CI provjerava Python 3.12 i 3.13 na Linuxu te Python 3.13 na macOS-u. Svaki PR također pokreće provjeru paketa, reviziju ovisnosti i CodeQL te instalira `.deb` na Ubuntu i `.rpm` na Fedoru. Izgrađene distribucije dostupne su kao artefakt `distributions` u CI pokretanjima.

Inačica paketa i CLI-ja dolazi iz `check_bitcoin_price/__init__.py`. Pogledajte [postupak izdanja](../../../CONTRIBUTING.md#releases) za ažuriranje inačice i automatizirano objavljivanje resursa izdanja na GitHubu.

## Doprinos

Pogledajte [CONTRIBUTING.md](../../../CONTRIBUTING.md) za tijek razvoja i zahtjeve za potpisanim commitovima.

## Licenca

Ovaj projekt licenciran je pod MIT licencom - za pojedinosti pogledajte datoteku [LICENSE](../../../LICENSE).

## Autor

Thomas Vincent

## Zahvale

- [CoinGecko](https://www.coingecko.com/) za pružanje besplatnog API-ja za kriptovalute
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
