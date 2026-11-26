# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · **Polski** · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Wtyczka dla Nagios/Icinga do monitorowania ceny Bitcoin z konfigurowalnymi progami ostrzegawczymi i krytycznymi.

## Funkcje

- Monitorowanie ceny Bitcoin w wielu walutach (USD, EUR, GBP itd.)
- Konfigurowalne progi ostrzegawcze i krytyczne (górne i dolne)
- Standardowe wyjście wtyczki Nagios wraz z danymi wydajnościowymi
- Wykorzystanie CoinGecko API (darmowe, bez wymaganego klucza API)
- Obsługa niestandardowych punktów końcowych API
- Konfigurowalny limit czasu
- Sprawdzanie aktualności notowań na podstawie znaczników czasu dostawcy, z domyślnym limitem jednej godziny
- Ograniczone ponawianie prób przy limitach zapytań i tymczasowych błędach API
- Jeden wspólny limit czasu dla wszystkich prób oraz limit 64 KiB dla każdej odpowiedzi
- Opcjonalne alerty dla bezwzględnej 24-godzinnej zmiany procentowej
- Progi cenowe, czas trwania żądania i wiek notowania w danych wydajnościowych

## Instalacja

### Z wydań GitHub

Pobierz pliki `.deb`, `.rpm`, `.tar.gz`, wheel oraz `SHA256SUMS` ze strony [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Zweryfikuj pobrane pliki za pomocą `sha256sum --ignore-missing --check SHA256SUMS`. Wydania nowsze niż 1.0.0 zawierają również podpisane poświadczenie kompilacji; potwierdź, że zasób pochodzi z przepływu wydania tego repozytorium za pomocą `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Użyj nazw plików z wybranego wydania. Pakiety natywne instalują `/usr/bin/check_bitcoin_price` oraz `/usr/lib/nagios/plugins/check_bitcoin_price`; pakiet RPM dostarcza dodatkowo `/usr/lib64/nagios/plugins/check_bitcoin_price`. Spakietowane polecenie uruchamia Pythona w trybie izolowanym, dzięki czemu ignoruje `PYTHONPATH` oraz moduły w katalogu roboczym; systemowy menedżer pakietów rozwiązuje zależności Pythona i biblioteki `requests`. Pakiety zawierają kod Pythona niezależny od architektury i wymagają dystrybucji zapewniającej Pythona 3.12 lub nowszego.

### Ze źródeł

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Środowisko deweloperskie

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Użycie

### Podstawowe użycie

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Z progami

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Indywidualne progi

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Inna waluta

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Niestandardowy limit czasu

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Aktualność danych i budżet ponowień

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Notowanie zawierające znacznik czasu dostawcy może mieć domyślnie najwyżej godzinę.
Punkty końcowe zwracające wyłącznie cenę pozostają użyteczne, gdy nie podano opcji `--max-age`.
Przy użyciu `--max-age` brakujący, nieprawidłowy, przyszły lub przestarzały znacznik czasu dostawcy zwraca
`UNKNOWN`; wtyczka nie zastępuje czasu notowania dostawcy lokalnym czasem pobrania.
Znacznik czasu równy dokładnie limitowi wieku pozostaje akceptowalny. Znaczniki czasu
z przyszłości są zawsze odrzucane.

Domyślnie dozwolona jest jedna ponowna próba. Ponawiane są wyłącznie błędy połączenia, przekroczenia limitu czasu oraz odpowiedzi HTTP
408/429/500/502/503/504. Czas oczekiwania zaczyna się od 0.5 sekundy i
podwaja przy kolejnych próbach; wartość `Retry-After` w sekundach oraz daty HTTP mają
pierwszeństwo. Wszystkie próby, odczyt odpowiedzi, dekodowanie JSON oraz oczekiwanie między próbami współdzielą
budżet czasu określony w `--timeout`. Jeśli czas oczekiwania przed ponowną próbą nie mieści się w budżecie, wtyczka natychmiast zwraca `UNKNOWN`
i zgłasza błąd, który wywołał ponowienie, taki jak `HTTP 429` lub `ConnectionError`,
a nie przekroczenie limitu czasu. Błędy uwierzytelniania, inne trwałe błędy HTTP, nieprawidłowy
JSON oraz odpowiedzi większe niż 64 KiB zdekodowanych danych nie są ponawiane. Użyj
`--retries 0`, aby wyłączyć ponawianie prób.

### Zapasowe źródła notowań

Użyj powtarzalnych opcji `--fallback-url URL` z punktami końcowymi zgodnymi z CoinGecko.
Przykładowo dodaj `--fallback-url https://quotes.example.org/simple/price`.
Każde źródło otrzymuje równą część pozostałego czasu żądania, wliczając jego
ponowne próby. Błąd przejściowy lub opóźnienie ponowienia dłuższe niż ta część powoduje przejście do
kolejnego źródła. Błędy weryfikacji TLS, trwałe błędy HTTP oraz nieprawidłowe
notowania zwracają UNKNOWN. Każda odpowiedź z notowaniem jest ograniczona do 64 KiB zdekodowanych danych.
Gdy skonfigurowano źródła zapasowe, status identyfikuje odpowiadające źródło jako
`primary`, `fallback1` itd., bez wypisywania jego adresu URL.

### Zmiana krótkookresowa

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Zapewnij użytkownikowi monitorującemu prywatny katalog stanu z prawem zapisu w lokalnym systemie plików Linux lub
macOS. Pozostaw sąsiedni plik `.lock` na miejscu pomiędzy kolejnymi sprawdzeniami. Używaj
osobnego pliku stanu dla każdego okna czasowego. Waluty mają w nim niezależne historie.
Domyślne okno wynosi 3600 sekund. Każde prawidłowe notowanie wymaga znacznika czasu dostawcy
mieszczącego się w oknie oraz w limicie wieku, który wynosi jedną godzinę, chyba że `--max-age` ustawia
inny limit. Wtyczka porównuje bieżącą cenę
z najstarszą wcześniejszą dodatnią ceną w tym oknie i raportuje
faktyczny czas, jaki upłynął, w sekundach. Powtarzające się znaczniki czasu nie tworzą dodatkowych próbek.
Pierwsza próbka, wygasła historia lub uszkodzony JSON rozpoczynają nowy punkt odniesienia;
metryka okna pozostaje nieznana do czasu pojawienia się porównywalnej próbki. Pozostałe alerty nadal
działają. Brak możliwości zapisu stanu, plik stanu lub plik blokady będący dowiązaniem symbolicznym albo notowanie starsze
niż najnowsza zapisana próbka zwracają UNKNOWN. Metryka ze znakiem `bitcoin_move_window`
używa symetrycznych zakresów ostrzegawczych i krytycznych. Wartość równa dokładnie progowi nie wywołuje alertu.

Wtyczka otwiera katalog stanu raz na sprawdzenie i operuje względem niego, dzięki czemu
podmiana elementu ścieżki w trakcie sprawdzania nie może przekierować blokady, odczytu
ani zapisu. Dowiązania symboliczne w części ścieżki będącej katalogiem są rozwiązywane podczas
uruchamiania sprawdzenia, co zapewnia działanie dowiązań systemowych takich jak `/var` w systemie macOS.
Katalog stanu oraz jego katalogi nadrzędne nie mogą zatem być zapisywalne dla innych
użytkowników. Pliki stanu i blokady są tworzone z uprawnieniami 0600.

### Dzienna zmiana procentowa

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Progi zmiany mierzą wartość bezwzględną podawanej przez CoinGecko 24-godzinnej
zmiany procentowej ze znakiem w wybranej walucie. Zmiana równa dokładnie progowi nie
wywołuje alertu. Jeśli podano oba progi, wartość ostrzegawcza nie może przekraczać krytycznej.
Brakujące lub nieprawidłowe wymagane dane o zmianie zwracają `UNKNOWN`. Alerty cenowe i alerty zmiany
można łączyć; wygrywa najwyższy poziom ważności, przy czym przy tym samym poziomie pierwszeństwo ma cena.

## Opcje wiersza poleceń

| Opcja | Opis |
|-------|------|
| `-w`, `--warning` | Zakres progu ostrzegawczego (format: LOW:HIGH) |
| `-c`, `--critical` | Zakres progu krytycznego (format: LOW:HIGH) |
| `--warning-low` | Próg ostrzegawczy dla niskiej ceny |
| `--warning-high` | Próg ostrzegawczy dla wysokiej ceny |
| `--critical-low` | Próg krytyczny dla niskiej ceny |
| `--critical-high` | Próg krytyczny dla wysokiej ceny |
| `--currency` | Kod waluty składający się z 2-16 liter lub cyfr (domyślnie: usd) |
| `--timeout` | Całkowity budżet czasu żądania API i ponowień w sekundach, z obsługą wartości ułamkowych (domyślnie: 10) |
| `--retries` | Dodatkowe próby przy błędach przejściowych, 0–5 (domyślnie: 1) |
| `--max-age` | Maksymalny wiek notowania dostawcy w sekundach wraz z wymogiem znacznika czasu; notowania ze znacznikiem czasu mają domyślnie limit 3600 |
| `--warning-change` | Limit ostrzegawczy dla bezwzględnej 24-godzinnej zmiany procentowej |
| `--critical-change` | Limit krytyczny dla bezwzględnej 24-godzinnej zmiany procentowej |
| `--api-url` | Podstawowy adres URL API |
| `--fallback-url` | Dodatkowy kompatybilny punkt końcowy; podaj wielokrotnie w preferowanej kolejności |
| `--state-file` | Plik JSON z historią zmian |
| `--move-window` | Okno zmiany w sekundach (domyślnie: 3600) |
| `--warning-move`, `--critical-move` | Bezwzględne progi zmiany w oknie w procentach |
| `-v`, `--verbose` | Włącz szczegółowe wyjście |
| `-V`, `--version` | Wyświetl wersję |
| `-h`, `--help` | Wyświetl komunikat pomocy |

## Konfiguracja Nagios

### Definicja polecenia

Ustaw makro zasobów Nagios `$USER1$` na katalog wtyczek (pakiety natywne używają `/usr/lib/nagios/plugins`). Dodaj do konfiguracji poleceń Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Definicja usługi

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

### Konfiguracja Icinga2

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

## Kody wyjścia

Nieprawidłowe argumenty, niedodatni limit czasu, błędne zakresy progów oraz źle sformatowane
ceny z API zwracają `UNKNOWN` (kod wyjścia 3). Progi muszą być skończonymi, nieujemnymi
liczbami, przy czym każda dolna granica nie może być większa od górnej. Waluta musi
składać się z 2-16 liter lub cyfr. Nieprawidłowa konfiguracja jest odrzucana przed nawiązaniem kontaktu
z API. Ceny muszą być skończone i nieujemne, podane jako liczby JSON lub zwykłe
ciągi dziesiętne, takie jak `"43521.5"`. Odpowiedź niezawierająca żądanej waluty
wskazuje ją w komunikacie, na przykład `Response has no EUR price`. Nieprawidłowe odpowiedzi nie generują
danych wydajnościowych. Szczegółowa diagnostyka trafia na stderr,
dzięki czemu stdout zawiera pojedynczy wiersz statusu monitoringu.

| Kod | Status | Opis |
|-----|--------|------|
| 0 | OK | Cena mieści się w akceptowalnym zakresie |
| 1 | WARNING | Cena przekroczyła próg ostrzegawczy |
| 2 | CRITICAL | Cena przekroczyła próg krytyczny |
| 3 | UNKNOWN | Wystąpił błąd (awaria API, przekroczenie limitu czasu itp.) |

## Dane wydajnościowe

Wtyczka generuje dane wydajnościowe w standardowym formacie Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Dane wydajnościowe dla ceny zawierają skonfigurowane zakresy ostrzegawcze/krytyczne oraz
minimum równe zero. Progi są wypisywane w pełnej notacji dziesiętnej, nigdy zaokrąglane
ani w zapisie wykładniczym, dzięki czemu duże wartości takie jak `14500000:16250000` pozostają łatwe do parsowania. Czas żądania obejmuje wszystkie próby oraz oczekiwanie między nimi. Wiek notowania jest
wypisywany tylko wtedy, gdy dostawca podaje prawidłowy znacznik czasu; zmiana dzienna jest wypisywana,
gdy jest dostępna. Zakresy zmiany są symetryczne względem zera. Nieprawidłowe lub przestarzałe dane
zwracają `UNKNOWN` bez danych wydajnościowych dotyczących ceny. Metryk tych można używać z
narzędziami do rysowania wykresów, takimi jak PNP4Nagios, Grafana czy InfluxDB.

## API

Wtyczka domyślnie korzysta z [CoinGecko API](https://www.coingecko.com/en/api), które jest darmowe i nie wymaga klucza API. Obowiązują limity zapytań.

Niestandardowe punkty końcowe muszą stosować ten sam format odpowiedzi: `bitcoin.<currency>` dla
ceny, `bitcoin.last_updated_at` dla znacznika czasu UNIX w sekundach oraz
`bitcoin.<currency>_24h_change` dla dziennej zmiany procentowej ze znakiem. Gdy nie podano
`--max-age` ani progów zmiany, wymagana jest wyłącznie cena. Obecny w odpowiedzi znacznik czasu
jest jednak zawsze weryfikowany: nie może pochodzić z przyszłości ani być starszy niż jedna
godzina. Zdekodowana odpowiedź musi mieścić się w 64 KiB.

Obsługiwane waluty to między innymi: usd, eur, gbp, jpy, aud, cad, chf, cny i wiele innych.

## Bezpieczeństwo

Poniższe mechanizmy są zaimplementowane w bieżącym kodzie. Ograniczają one to, co błędnie działający punkt końcowy lub lokalny użytkownik może zrobić
hostowi monitorującemu; nie gwarantują natomiast wiarygodności samego notowania.

- Certyfikaty HTTPS są weryfikowane zgodnie z domyślnymi ustawieniami `requests` i żadna opcja
  nie wyłącza tej weryfikacji. Niestandardowy `--api-url` używający zwykłego `http://` nie ma
  takiej ochrony.
- Rozwiązywanie DNS, połączenie, odczyt, ponowienia i czas oczekiwania dzielą wspólny limit `--timeout`.
  Zdalny serwer wysyłający dane powoli nie może go przedłużyć.
- Każda odpowiedź jest ograniczona do 64 KiB po dekompresji, a treść przekierowań
  jest odrzucana bez odczytu.
- Błędy żądań wypisują wyłącznie kod statusu HTTP lub klasę błędu, ponieważ niestandardowy
  `--api-url` może zawierać dane uwierzytelniające.
- Polecenie instalowane przez pakiety `.deb` oraz `.rpm` uruchamia Pythona w trybie izolowanym.
  Ignoruje ono `PYTHONPATH`, katalog site użytkownika oraz moduły w katalogu roboczym.
  Instalacja przez `pip` używa standardowego skryptu konsolowego i korzysta
  ze środowiska, w którym została zainstalowana.
- Stan zmiany ceny jest odczytywany i zapisywany bez podążania za dowiązaniami symbolicznymi pod
  nazwą pliku stanu lub blokady, względem katalogu otwieranego raz na sprawdzenie.
- Zasoby wydania zawierają poświadczenia pochodzenia kompilacji oprócz pliku
  `SHA256SUMS`; zobacz [Z wydań GitHub](#from-github-releases).

## Aktualizacja z wersji 1.0.0

Zmiany te wchodzą w skład wersji 2.0.0.

- Notowanie ze znacznikiem czasu dostawcy starszym niż jedna godzina zwraca `UNKNOWN`, chyba że
  podano większą wartość `--max-age`. Punkty końcowe niezwracające znacznika czasu działają bez zmian.
- `--currency` akceptuje wyłącznie od 2 do 16 liter lub cyfr.
- Ciągi liczbowe z separatorami cyfr lub otaczającymi spacjami są odrzucane.
- Oczekiwanie na ponowienie, które nie mieści się w budżecie, zgłasza błąd źródłowy
  zamiast `API request timed out`.
- Pakiety natywne nie uwzględniają już `PYTHONPATH`.
- Progi wynoszące milion lub więcej pojawiają się w danych wydajnościowych jako zwykłe
  liczby dziesiętne zamiast zapisu wykładniczego.

## Lokalizacja

Pomoc CLI, błędy walidacji oraz opisy statusów wtyczki obsługują 45 ustawień regionalnych (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) przy użyciu wbudowanych katalogów ładowanych przez stdlib. Rozpoznawanie sprawdza kolejno `--lang`, następnie `LC_ALL`, `LC_MESSAGES` i `LANG`, z powrotem do `en`. Prefiksy statusów Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) oraz dane wydajnościowe pozostają niezmienione we wszystkich lokalizacjach.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Rozwój projektu

Zainstaluj [mise](https://mise.jdx.dev/getting-started.html), a następnie uruchom powyższą konfigurację deweloperską. Plik `mise.toml` przypina wersje Pythona i uv. Narzędzia deweloperskie są zadeklarowane w `pyproject.toml` i rozwiązane w zatwierdzonym pliku `uv.lock`.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Po konfiguracji zainstaluj hooki zatwierdzania:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Użyj `mise exec -- uv add --dev <tool>` lub `mise exec -- uv add <dependency>`, aby zaktualizować zależności, i zatwierdź zarówno `pyproject.toml`, jak i `uv.lock`.

CI testuje Pythona 3.12 i 3.13 na systemie Linux oraz Pythona 3.13 na systemie macOS. Każdy PR uruchamia również walidację pakietów, audyt zależności i CodeQL, a także instaluje pakiet `.deb` w Ubuntu i `.rpm` w Fedorze. Zbudowane dystrybucje są dostępne jako artefakt `distributions` w uruchomieniach CI.

Wersja pakietu i CLI pochodzi z `check_bitcoin_price/__init__.py`. Zobacz [proces wydawania wersji](../../../CONTRIBUTING.md#releases), aby poznać zasady podbijania wersji i automatycznej publikacji zasobów wydań GitHub.

## Współtworzenie

Zobacz [CONTRIBUTING.md](../../../CONTRIBUTING.md), aby poznać przepływ pracy deweloperskiej oraz wymagania dotyczące podpisanych zatwierdzeń.

## Licencja

Ten projekt jest udostępniany na licencji MIT - szczegóły w pliku [LICENSE](../../../LICENSE).

## Autor

Thomas Vincent

## Podziękowania

- [CoinGecko](https://www.coingecko.com/) za udostępnienie darmowego API kryptowalutowego
- [Wytyczne tworzenia wtyczek Nagios](https://nagios-plugins.org/doc/guidelines.html)
