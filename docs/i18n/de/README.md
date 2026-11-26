# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · **Deutsch** · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Ein Nagios/Icinga-Plugin zur Überwachung des Bitcoin-Preises mit konfigurierbaren Warn- und kritischen Schwellenwerten.

## Funktionen

- Überwachung des Bitcoin-Preises in mehreren Währungen (USD, EUR, GBP usw.)
- Konfigurierbare Warn- und kritische Schwellenwerte (Ober- und Untergrenzen)
- Standardkonforme Nagios-Plugin-Ausgabe mit Leistungsdaten
- Nutzung der CoinGecko-API (kostenlos, kein API-Schlüssel erforderlich)
- Unterstützung für benutzerdefinierte API-Endpunkte
- Konfigurierbarer Timeout
- Aktualitätsprüfung von Kursen anhand von Anbieter-Zeitstempeln mit einem Standardlimit von einer Stunde
- Begrenzte Wiederholungsversuche bei Rate-Limits und vorübergehenden API-Fehlern
- Ein gemeinsames Zeitlimit für alle Versuche sowie eine Obergrenze von 64 KiB pro Antwort
- Optionale Alarme bei absoluter prozentualer 24-Stunden-Änderung
- Preisschwellenwerte, Anfragedauer und Kursalter in den Leistungsdaten

## Installation

### Über GitHub Releases

Laden Sie `.deb`, `.rpm`, `.tar.gz`, Wheel und `SHA256SUMS` von [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) herunter. Überprüfen Sie den Download mit `sha256sum --ignore-missing --check SHA256SUMS`. Releases nach 1.0.0 enthalten zusätzlich signierte Build-Provenienz-Nachweise; bestätigen Sie mit `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`, dass ein Asset aus dem Release-Workflow dieses Repositorys stammt.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Verwenden Sie die Dateinamen des ausgewählten Releases. Native Pakete installieren `/usr/bin/check_bitcoin_price` und `/usr/lib/nagios/plugins/check_bitcoin_price`; das RPM-Paket stellt außerdem `/usr/lib64/nagios/plugins/check_bitcoin_price` bereit. Der paketierte Befehl führt Python im isolierten Modus aus und ignoriert daher `PYTHONPATH` sowie Module im Arbeitsverzeichnis; der Paketmanager des Systems löst die Abhängigkeiten zu Python und `requests` auf. Die Pakete enthalten architekturunabhängigen Python-Code und erfordern eine Distribution mit Python 3.12 oder neuer.

### Aus dem Quellcode

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Für die Entwicklung

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Verwendung

### Grundlegende Verwendung

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Mit Schwellenwerten

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Einzelne Schwellenwerte

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Andere Währung

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Benutzerdefinierter Timeout

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Aktualität und Wiederholungsbudget

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Ein Kurs mit Anbieter-Zeitstempel darf standardmäßig höchstens eine Stunde alt sein.
Endpunkte, die nur einen Preis zurückliefern, bleiben nutzbar, wenn `--max-age` nicht angegeben ist.
Mit `--max-age` führen fehlende, ungültige, in der Zukunft liegende oder veraltete Anbieter-Zeitstempel zu
`UNKNOWN`; das Plugin ersetzt die Kurszeit des Anbieters nicht durch die lokale
Abrufzeit. Ein Zeitstempel exakt am Alterslimit bleibt zulässig. Zeitstempel in der Zukunft
werden immer abgelehnt.

Standardmäßig ist ein Wiederholungsversuch erlaubt. Nur Verbindungsfehler, Timeouts und HTTP-Antworten
mit den Statuscodes 408/429/500/502/503/504 werden erneut versucht. Das Backoff beginnt bei 0,5 Sekunden und
verdoppelt sich bei weiteren Versuchen; `Retry-After`-Sekunden und HTTP-Datumsangaben haben
Vorrang. Alle Versuche, das Lesen von Antworten, das JSON-Dekodieren und Wartezeiten zwischen Wiederholungen teilen sich
das Budget von `--timeout`. Passt eine Wartezeit nicht mehr in das Budget, gibt das Plugin sofort `UNKNOWN` zurück
und meldet den auslösenden Fehler, wie `HTTP 429` oder `ConnectionError`,
statt eines Timeouts. Authentifizierungsfehler, andere dauerhafte HTTP-Fehler, ungültiges
JSON und Antworten mit mehr als 64 KiB dekodierter Daten werden nicht erneut versucht. Mit
`--retries 0` deaktivieren Sie Wiederholungsversuche.

### Fallback-Kursquellen

Verwenden Sie wiederholbare `--fallback-url URL`-Optionen mit CoinGecko-kompatiblen Endpunkten.
Fügen Sie zum Beispiel `--fallback-url https://quotes.example.org/simple/price` hinzu.
Jede Quelle erhält einen gleichen Anteil an der verbleibenden Anfragefrist einschließlich ihrer
Wiederholungsversuche. Ein vorübergehender Fehler oder eine Wiederholungsverzögerung, die diesen Anteil überschreitet, wechselt zur
nächsten Quelle. TLS-Verifizierungsfehler, dauerhafte HTTP-Fehler und ungültige
Kurse geben UNKNOWN zurück. Jede Kursantwort ist auf 64 KiB dekodierter Daten begrenzt.
Wenn Fallbacks konfiguriert sind, identifiziert der Status die antwortende Quelle als
`primary`, `fallback1` usw., ohne deren URL auszugeben.

### Kurzzeit-Kursbewegung

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Geben Sie dem Monitoring-Benutzer ein privates, beschreibbares Zustandsverzeichnis auf einem lokalen Linux- oder
macOS-Dateisystem. Belassen Sie die zugehörige `.lock`-Datei zwischen den Prüfungen an Ort und Stelle. Verwenden Sie pro
Zeitfenster eine eigene Zustandsdatei. Währungen führen darin unabhängige Verläufe.
Das Standard-Zeitfenster beträgt 3600 Sekunden. Jeder gültige Kurs benötigt einen Anbieter-Zeitstempel
innerhalb des Zeitfensters und des Alterslimits, das ohne anderslautendes `--max-age` bei einer Stunde
liegt. Das Plugin vergleicht den aktuellen
Preis mit dem ältesten früheren positiven Preis in diesem Zeitfenster und meldet die
tatsächlich verstrichenen Sekunden. Wiederholte Zeitstempel erzeugen keine zusätzlichen Messpunkte.
Ein erster Messpunkt, ein abgelaufener Verlauf oder beschädigtes JSON startet eine neue Basislinie; die
Zeitfenster-Metrik ist unbekannt, bis ein vergleichbarer Messpunkt vorliegt. Andere Alarme greifen
weiterhin. Ein nicht beschreibbarer Zustand, ein symbolischer Link als Zustands- oder Lock-Datei oder ein Kurs, der älter
als der neueste aufgezeichnete Messpunkt ist, gibt UNKNOWN zurück. Die vorzeichenbehaftete Metrik `bitcoin_move_window`
verwendet symmetrische Warn- und kritische Bereiche. Ein Wert genau auf dem Grenzwert löst keinen Alarm aus.

Das Plugin öffnet das Zustandsverzeichnis einmal pro Prüfung und arbeitet relativ dazu, sodass
eine während der Prüfung ausgetauschte Pfadkomponente das Sperren, Lesen oder Schreiben nicht umleiten kann.
Symbolische Links im Verzeichnisteil des Pfades werden beim Start der Prüfung aufgelöst, wodurch
Plattform-Links wie `/var` unter macOS nutzbar bleiben. Das
Zustandsverzeichnis und seine übergeordneten Verzeichnisse dürfen daher für andere
Benutzer nicht beschreibbar sein. Zustands- und Lock-Dateien werden mit dem Modus 0600 erstellt.

### Tägliche prozentuale Kursbewegung

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Änderungsschwellenwerte messen den Absolutwert der vorzeichenbehafteten 24-Stunden-Prozentänderung von CoinGecko
in der gewählten Währung. Eine Änderung genau auf dem Schwellenwert löst keinen
Alarm aus. Werden beide Schwellenwerte angegeben, darf der Warnwert den kritischen Wert nicht überschreiten.
Fehlende oder ungültige erforderliche Änderungsdaten geben `UNKNOWN` zurück. Preis- und Änderungsalarme
lassen sich kombinieren; der höchste Schweregrad gewinnt, wobei der Preis bei gleichem Schweregrad Vorrang hat.

## Befehlszeilenoptionen

| Option | Beschreibung |
|--------|--------------|
| `-w`, `--warning` | Warnschwellenbereich (Format: LOW:HIGH) |
| `-c`, `--critical` | Kritischer Schwellenbereich (Format: LOW:HIGH) |
| `--warning-low` | Warnschwellenwert für niedrigen Preis |
| `--warning-high` | Warnschwellenwert für hohen Preis |
| `--critical-low` | Kritischer Schwellenwert für niedrigen Preis |
| `--critical-high` | Kritischer Schwellenwert für hohen Preis |
| `--currency` | Währungscode aus 2-16 Buchstaben oder Ziffern (Standard: usd) |
| `--timeout` | Gesamtes Budget für API-Anfragen und Wiederholungen in Sekunden, einschließlich Dezimalwerten (Standard: 10) |
| `--retries` | Zusätzliche Versuche bei vorübergehenden Fehlern, 0–5 (Standard: 1) |
| `--max-age` | Maximales Alter des Anbieter-Kurses in Sekunden mit Pflicht zum Zeitstempel; Kurse mit Zeitstempel verwenden standardmäßig 3600 |
| `--warning-change` | Warngrenze für die absolute prozentuale 24-Stunden-Änderung |
| `--critical-change` | Kritische Grenze für die absolute prozentuale 24-Stunden-Änderung |
| `--api-url` | Primäre API-URL |
| `--fallback-url` | Zusätzlicher kompatibler Endpunkt; in bevorzugter Reihenfolge wiederholbar |
| `--state-file` | JSON-Datei für den Bewegungsverlauf |
| `--move-window` | Zeitfenster für Kursbewegungen in Sekunden (Standard: 3600) |
| `--warning-move`, `--critical-move` | Schwellenwerte für absolute Bewegungen im Zeitfenster in Prozent |
| `-v`, `--verbose` | Ausführliche Ausgabe aktivieren |
| `-V`, `--version` | Version anzeigen |
| `-h`, `--help` | Hilfemeldung anzeigen |

## Nagios-Konfiguration

### Befehlsdefinition

Setzen Sie das Nagios-Ressourcenmakro `$USER1$` auf das Plugin-Verzeichnis (native Pakete verwenden `/usr/lib/nagios/plugins`). Fügen Sie Ihrer Nagios-Befehlskonfiguration Folgendes hinzu:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Service-Definition

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

### Icinga2-Konfiguration

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

## Exit-Codes

Ungültige Argumente, nicht-positive Timeouts, ungültige Schwellenwertbereiche und fehlerhaft formatierte
API-Preise geben `UNKNOWN` (Exit-Code 3) zurück. Schwellenwerte müssen endliche, nicht-negative
Zahlen sein, wobei jede Untergrenze höchstens so groß wie die zugehörige Obergrenze sein darf. Die Währung muss
aus 2-16 Buchstaben oder Ziffern bestehen. Eine ungültige Konfiguration wird bereits vor der Kontaktaufnahme
mit der API abgewiesen. Preise müssen endlich und nicht-negativ sein und als JSON-Zahlen oder einfache
Dezimalzeichenketten wie `"43521.5"` vorliegen. Fehlt die angeforderte Währung in der Antwort,
wird sie namentlich genannt, zum Beispiel `Response has no EUR price`. Ungültige Antworten geben keine
Leistungsdaten aus. Ausführliche Diagnosemeldungen gehen nach stderr,
sodass stdout eine einzelne Monitoring-Statuszeile enthält.

| Code | Status | Beschreibung |
|------|--------|--------------|
| 0 | OK | Der Preis liegt im zulässigen Bereich |
| 1 | WARNING | Der Preis hat den Warnschwellenwert überschritten |
| 2 | CRITICAL | Der Preis hat den kritischen Schwellenwert überschritten |
| 3 | UNKNOWN | Ein Fehler ist aufgetreten (API-Fehler, Timeout usw.) |

## Leistungsdaten

Das Plugin gibt Leistungsdaten im Standard-Nagios-Format aus:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Die Preis-Leistungsdaten enthalten die konfigurierten Warn- und kritischen Bereiche sowie ein
Minimum von null. Schwellenwerte werden in vollständiger Dezimalschreibweise ausgegeben, niemals gerundet
oder in Exponentialschreibweise, damit große Werte wie `14500000:16250000` maschinenlesbar bleiben. Die Anfragezeit umfasst alle Versuche und Backoff-Wartezeiten. Das Kursalter wird
nur ausgegeben, wenn der Anbieter einen gültigen Zeitstempel liefert; die tägliche Änderung wird ausgegeben,
sofern verfügbar. Änderungsbereiche sind symmetrisch um null. Ungültige oder veraltete Daten
erzeugen `UNKNOWN` ohne Preis-Leistungsdaten. Diese Metriken lassen sich mit
Grafik-Tools wie PNP4Nagios, Grafana oder InfluxDB nutzen.

## API

Dieses Plugin nutzt standardmäßig die [CoinGecko API](https://www.coingecko.com/en/api), die kostenlos ist und keinen API-Schlüssel erfordert. Es gelten Rate-Limits.

Benutzerdefinierte Endpunkte müssen dieselbe Antwortstruktur verwenden: `bitcoin.<currency>` für den
Preis, `bitcoin.last_updated_at` für UNIX-Zeitstempelsekunden und
`bitcoin.<currency>_24h_change` für die vorzeichenbehaftete tägliche prozentuale Änderung. Nur der Preis
ist erforderlich, wenn `--max-age` und die Änderungsschwellenwerte fehlen. Ein vorhandener
Zeitstempel wird dennoch geprüft: Er darf nicht in der Zukunft liegen und nicht älter als eine Stunde
sein. Die dekodierte Antwort muss in 64 KiB passen.

Unterstützte Währungen sind unter anderem: usd, eur, gbp, jpy, aud, cad, chf, cny und viele mehr.

## Sicherheit

Die folgenden Maßnahmen sind im aktuellen Code implementiert. Sie begrenzen, welche Auswirkungen ein fehlerhafter Endpunkt oder ein lokaler Benutzer auf den
Monitoring-Host haben kann; den Kurs selbst machen sie nicht vertrauenswürdig.

- HTTPS-Zertifikate werden mit den Standardeinstellungen von `requests` überprüft, und keine Option
  deaktiviert diese Prüfung. Eine benutzerdefinierte `--api-url` mit unverschlüsseltem `http://` bietet keinen
  solchen Schutz.
- DNS, Verbindung, Lesevorgänge, Wiederholungsversuche und Backoff teilen sich das Zeitlimit von `--timeout`. Eine
  Gegenstelle, die Daten langsam sendet, kann dieses Limit nicht verlängern.
- Jede Antwort ist nach der Dekomprimierung auf 64 KiB begrenzt, und Weiterleitungs-Bodys
  werden ungelesen verworfen.
- Anfragefehler geben nur einen HTTP-Status oder eine Fehlerklasse aus, da eine benutzerdefinierte
  `--api-url` Zugangsdaten enthalten kann.
- Der durch `.deb` und `.rpm` installierte Befehl führt Python im isolierten Modus aus.
  Er ignoriert `PYTHONPATH`, das Benutzer-Site-Verzeichnis und Module im Arbeitsverzeichnis.
  Eine `pip`-Installation nutzt das Standard-Konsolenskript und folgt
  der Umgebung, in der sie installiert ist.
- Der Bewegungszustand wird relativ zu einem pro Prüfung einmal geöffneten Verzeichnis gelesen und geschrieben,
  ohne einem symbolischen Link beim Namen der Zustands- oder Lock-Datei zu folgen.
- Release-Assets tragen zusätzlich zu `SHA256SUMS` Build-Provenienz-Nachweise;
  siehe [Über GitHub Releases](#from-github-releases).

## Upgrade von 1.0.0

Diese Änderungen sind in 2.0.0 enthalten.

- Ein Kurs mit einem Anbieter-Zeitstempel, der älter als eine Stunde ist, gibt `UNKNOWN` zurück, sofern kein
  größeres `--max-age` angegeben wird. Endpunkte ohne Zeitstempel bleiben unberührt.
- `--currency` akzeptiert nur 2-16 Buchstaben oder Ziffern.
- Numerische Zeichenketten mit Zifferntrennzeichen oder umgebenden Leerzeichen werden abgelehnt.
- Eine Wiederholungswartezeit, die nicht in das Budget passt, meldet den zugrunde liegenden Fehler
  statt `API request timed out`.
- Die nativen Pakete berücksichtigen `PYTHONPATH` nicht mehr.
- Schwellenwerte ab einer Million erscheinen in den Leistungsdaten als normale
  Dezimalzahlen statt in Exponentialschreibweise.

## Lokalisierung

CLI-Hilfe, Validierungsfehler und Plugin-Statusbeschreibungen unterstützen 45 Gebietsschemata (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) über gebündelte, per stdlib geladene Kataloge. Die Auflösung prüft `--lang`, dann `LC_ALL`, `LC_MESSAGES` und `LANG`, mit Fallback auf `en`. Nagios-Statuspräfixe (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) und Leistungsdaten bleiben in allen Gebietsschemata unverändert.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Entwicklung

Installieren Sie [mise](https://mise.jdx.dev/getting-started.html) und führen Sie anschließend die oben beschriebene Entwicklungseinrichtung aus. `mise.toml` fixiert die Versionen von Python und uv. Entwicklungswerkzeuge sind in `pyproject.toml` deklariert und in der eingecheckten Datei `uv.lock` aufgelöst.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Installieren Sie nach der Einrichtung die Commit-Hooks:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Verwenden Sie `mise exec -- uv add --dev <tool>` oder `mise exec -- uv add <dependency>`, um Abhängigkeiten zu aktualisieren, und committen Sie sowohl `pyproject.toml` als auch `uv.lock`.

Die CI prüft Python 3.12 und 3.13 unter Linux sowie Python 3.13 unter macOS. Jeder PR führt außerdem Paketvalidierung, Abhängigkeitsprüfung und CodeQL aus und installiert das `.deb` unter Ubuntu sowie das `.rpm` unter Fedora. Gebaute Distributionen stehen bei CI-Läufen als `distributions`-Artefakt zur Verfügung.

Die Paket- und CLI-Version stammt aus `check_bitcoin_price/__init__.py`. Siehe [den Release-Prozess](../../../CONTRIBUTING.md#releases) für Versionserhöhungen und die automatisierte Veröffentlichung von GitHub-Release-Assets.

## Mitwirken

Siehe [CONTRIBUTING.md](../../../CONTRIBUTING.md) für den Entwicklungs-Workflow und die Anforderungen an signierte Commits.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die Datei [LICENSE](../../../LICENSE) für Details.

## Autor

Thomas Vincent

## Danksagungen

- [CoinGecko](https://www.coingecko.com/) für die Bereitstellung einer kostenlosen Kryptowährungs-API
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
