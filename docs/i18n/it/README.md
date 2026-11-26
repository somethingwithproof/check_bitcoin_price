# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · **Italiano** · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Un plugin per Nagios/Icinga per monitorare il prezzo di Bitcoin con soglie di warning e critical configurabili.

## Funzionalità

- Monitoraggio del prezzo di Bitcoin in più valute (USD, EUR, GBP, ecc.)
- Soglie di warning e critical configurabili (superiore e inferiore)
- Output standard dei plugin Nagios con performance data
- Utilizza le API di CoinGecko (gratuite, senza necessità di chiave API)
- Supporto per endpoint API personalizzati
- Timeout configurabile
- Controlli di freschezza delle quotazioni tramite i timestamp del fornitore, con un limite predefinito di un'ora
- Tentativi limitati per gestire i rate limit e gli errori temporanei delle API
- Una scadenza unica per tutti i tentativi e un limite di 64 KiB per ciascuna risposta
- Avvisi opzionali sulla variazione percentuale assoluta nelle 24 ore
- Soglie di prezzo, durata della richiesta e anzianità della quotazione nei performance data

## Installazione

### Da GitHub Releases

Scarica i file `.deb`, `.rpm`, `.tar.gz`, wheel e `SHA256SUMS` da [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Verifica il download con `sha256sum --ignore-missing --check SHA256SUMS`. Le release successive alla 1.0.0 includono anche la provenienza di build firmata; verifica che un asset provenga dal workflow di release di questo repository con `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Usa i nomi dei file della release selezionata. I pacchetti nativi installano `/usr/bin/check_bitcoin_price` e `/usr/lib/nagios/plugins/check_bitcoin_price`; il pacchetto RPM fornisce inoltre `/usr/lib64/nagios/plugins/check_bitcoin_price`. Il comando pacchettizzato esegue Python in modalità isolata, quindi ignora `PYTHONPATH` e i moduli nella directory di lavoro; il gestore di pacchetti di sistema risolve le dipendenze Python e `requests`. I pacchetti contengono codice Python indipendente dall'architettura e richiedono una distribuzione che fornisca Python 3.12 o versioni successive.

### Dai sorgenti

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Per lo sviluppo

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Utilizzo

### Utilizzo di base

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Con soglie

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Soglie individuali

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Valuta diversa

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Timeout personalizzato

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Freschezza della quotazione e budget dei tentativi

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Una quotazione dotata di timestamp del fornitore non può avere più di un'ora per impostazione predefinita.
Gli endpoint che restituiscono solo il prezzo restano utilizzabili quando `--max-age` non è specificato.
Con `--max-age`, timestamp del fornitore mancanti, non validi, futuri o obsoleti restituiscono
`UNKNOWN`; il plugin non sostituisce l'orario di recupero locale al timestamp della quotazione del fornitore.
Un timestamp esattamente al limite di anzianità resta accettabile. I timestamp futuri vengono sempre rifiutati.

L'impostazione predefinita consente un solo nuovo tentativo. Vengono ritentati solo gli errori di connessione, i timeout e le risposte HTTP
408/429/500/502/503/504. Il backoff parte da 0,5 secondi e
raddoppia per i tentativi successivi; i secondi di `Retry-After` e le date HTTP hanno la
precedenza. Tutti i tentativi, le letture della risposta, la decodifica JSON e le attese tra i tentativi condividono
il budget di `--timeout`. Se un'attesa di retry non rientra nel budget residuo, viene restituito immediatamente `UNKNOWN`
segnalando l'errore che l'ha causata, ad esempio `HTTP 429` o `ConnectionError`,
e non un timeout. Errori di autenticazione, altri errori HTTP permanenti, JSON non
validi e risposte superiori a 64 KiB di dati decodificati non vengono ritentati. Usa
`--retries 0` per disabilitare i nuovi tentativi.

### Fonti di quotazione di fallback

Usa opzioni `--fallback-url URL` ripetibili con endpoint compatibili con CoinGecko.
Ad esempio, aggiungi `--fallback-url https://quotes.example.org/simple/price`.
Ciascuna fonte riceve una quota uguale della scadenza residua della richiesta, inclusi i propri
tentativi. Un errore transitorio o un ritardo di retry superiore a tale quota fa passare alla
fonte successiva. Errori di verifica TLS, errori HTTP permanenti e quotazioni non valide
restituiscono UNKNOWN. Ciascuna risposta di quotazione è limitata a 64 KiB di dati decodificati.
Quando sono configurati dei fallback, lo stato identifica la fonte che ha risposto come
`primary`, `fallback1` e così via, senza stampare il relativo URL.

### Variazione su finestra breve

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Assegna all'utente di monitoraggio una directory di stato privata e scrivibile su un filesystem locale Linux o
macOS. Mantieni il file `.lock` adiacente tra un controllo e l'altro. Usa un
file di stato separato per ciascuna finestra. Le valute mantengono cronologie indipendenti al suo interno.
La finestra predefinita è di 3600 secondi. Ogni quotazione valida richiede un timestamp del fornitore
compreso nella finestra e nel limite di anzianità, pari a un'ora a meno che `--max-age` non imposti
un valore diverso. Il plugin confronta il prezzo corrente
con il prezzo positivo precedente più vecchio in tale finestra e riporta i
secondi effettivamente trascorsi. Timestamp ripetuti non creano campioni aggiuntivi.
Un primo campione, una cronologia scaduta o un JSON corrotto avviano una nuova baseline; la
metrica della finestra resta sconosciuta finché non è disponibile un campione confrontabile. Gli altri avvisi continuano
ad applicarsi. Uno stato non scrivibile, un file di stato o di lock che sia un collegamento simbolico oppure una quotazione più vecchia
del campione registrato più recente restituiscono UNKNOWN. La metrica con segno `bitcoin_move_window`
utilizza intervalli simmetrici di warning e critical. Il raggiungimento esatto del limite non genera un avviso.

Il plugin apre la directory di stato una volta per controllo e opera in modo relativo a essa, così
un componente del percorso sostituito durante il controllo non può reindirizzare il lock, la lettura
o la scrittura. I collegamenti simbolici nella parte directory del percorso vengono seguiti all'avvio del
controllo, mantenendo utilizzabili collegamenti di piattaforma come `/var` su macOS. La
directory di stato e le directory padre non devono quindi essere scrivibili da altri
utenti. I file di stato e di lock vengono creati con permessi 0600.

### Variazione percentuale giornaliera

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Le soglie di variazione misurano il valore assoluto della variazione percentuale con segno nelle 24 ore
fornita da CoinGecko nella valuta selezionata. Una variazione esattamente pari alla soglia non
genera un avviso. Se vengono fornite entrambe le soglie, warning non deve superare critical.
Dati di variazione richiesti mancanti o non validi restituiscono `UNKNOWN`. Gli avvisi su prezzo e variazione
possono essere combinati; prevale la gravità più alta e, a parità di gravità, ha la precedenza il prezzo.

## Opzioni da riga di comando

| Opzione | Descrizione |
|--------|-------------|
| `-w`, `--warning` | Intervallo soglia di warning (formato: LOW:HIGH) |
| `-c`, `--critical` | Intervallo soglia di critical (formato: LOW:HIGH) |
| `--warning-low` | Soglia di warning per il prezzo minimo |
| `--warning-high` | Soglia di warning per il prezzo massimo |
| `--critical-low` | Soglia di critical per il prezzo minimo |
| `--critical-high` | Soglia di critical per il prezzo massimo |
| `--currency` | Codice valuta da 2 a 16 lettere o cifre (predefinito: usd) |
| `--timeout` | Budget totale in secondi per richieste API e retry, inclusi valori frazionari (predefinito: 10) |
| `--retries` | Tentativi aggiuntivi per errori transitori, 0-5 (predefinito: 1) |
| `--max-age` | Anzianità massima in secondi della quotazione del fornitore con timestamp obbligatorio; le quotazioni con timestamp usano 3600 come valore predefinito |
| `--warning-change` | Limite di warning per la variazione percentuale assoluta nelle 24 ore |
| `--critical-change` | Limite di critical per la variazione percentuale assoluta nelle 24 ore |
| `--api-url` | URL API primario |
| `--fallback-url` | Endpoint compatibile aggiuntivo; ripetere nell'ordine preferito |
| `--state-file` | File JSON per la cronologia delle variazioni |
| `--move-window` | Finestra di variazione in secondi (predefinito: 3600) |
| `--warning-move`, `--critical-move` | Soglie di variazione assoluta sulla finestra in percentuale |
| `-v`, `--verbose` | Abilita output dettagliato |
| `-V`, `--version` | Mostra la versione |
| `-h`, `--help` | Mostra il messaggio di aiuto |

## Configurazione di Nagios

### Definizione del comando

Imposta la macro di risorsa Nagios `$USER1$` sulla directory dei plugin (i pacchetti nativi usano `/usr/lib/nagios/plugins`). Aggiungi alla configurazione dei comandi di Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Definizione del servizio

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

### Configurazione di Icinga2

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

## Codici di uscita

Argomenti non validi, timeout non positivi, intervalli di soglia non validi e prezzi API malformati
restituiscono `UNKNOWN` (exit 3). Le soglie devono essere numeri finiti e non negativi,
con ciascun limite inferiore non maggiore del corrispondente limite superiore. La valuta deve
essere composta da 2-16 lettere o cifre. Una configurazione non valida viene rifiutata prima di contattare
l'API. I prezzi devono essere finiti e non negativi, forniti come numeri JSON o stringhe
decimali semplici come `"43521.5"`. Una risposta priva della valuta richiesta la indica
esplicitamente, ad esempio `Response has no EUR price`. Le risposte non valide non emettono
performance data. La diagnostica dettagliata viene inviata su stderr
in modo che stdout contenga una sola riga di stato di monitoraggio.

| Codice | Stato | Descrizione |
|------|--------|-------------|
| 0 | OK | Il prezzo rientra nell'intervallo accettabile |
| 1 | WARNING | Il prezzo ha superato la soglia di warning |
| 2 | CRITICAL | Il prezzo ha superato la soglia di critical |
| 3 | UNKNOWN | Si è verificato un errore (errore API, timeout, ecc.) |

## Performance Data

Il plugin emette i performance data nel formato standard Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

I performance data del prezzo includono gli intervalli di warning/critical configurati e un
minimo pari a zero. Le soglie vengono stampate in notazione decimale completa, mai arrotondate
né in notazione esponenziale, in modo che valori elevati come `14500000:16250000` restino facilmente analizzabili. Il tempo della richiesta include tutti i tentativi e il backoff. L'anzianità della quotazione viene
emessa solo quando il fornitore fornisce un timestamp valido; la variazione giornaliera viene emessa
quando disponibile. Gli intervalli di variazione sono simmetrici attorno allo zero. Dati non validi o obsoleti
producono `UNKNOWN` senza performance data del prezzo. Queste metriche possono essere utilizzate con
strumenti di grafici come PNP4Nagios, Grafana o InfluxDB.

## API

Questo plugin utilizza per impostazione predefinita le [API di CoinGecko](https://www.coingecko.com/en/api), che sono gratuite e non richiedono una chiave API. Si applicano limiti di frequenza (rate limit).

Gli endpoint personalizzati devono utilizzare la stessa struttura di risposta: `bitcoin.<currency>` per
il prezzo, `bitcoin.last_updated_at` per il timestamp UNIX in secondi e
`bitcoin.<currency>_24h_change` per la variazione percentuale giornaliera con segno. Solo il prezzo
è obbligatorio quando `--max-age` e le soglie di variazione sono assenti. Se è presente un timestamp,
viene comunque verificato: non deve essere nel futuro né più vecchio di un'ora.
La risposta decodificata deve rientrare in 64 KiB.

Le valute supportate includono: usd, eur, gbp, jpy, aud, cad, chf, cny e molte altre.

## Sicurezza

Le misure seguenti sono implementate nel codice attuale. Limitano ciò che un endpoint malfunzionante o un utente locale può fare all'host di monitoraggio;
non rendono di per sé affidabile la quotazione.

- I certificati HTTPS vengono verificati con le impostazioni predefinite di `requests` e nessuna opzione
  disabilita la verifica. Un `--api-url` personalizzato che usa `http://` in chiaro non dispone di
  tale protezione.
- DNS, connessione, letture, retry e backoff condividono la scadenza `--timeout`. Un
  peer che invia dati lentamente non può estenderla.
- Ciascuna risposta è limitata a 64 KiB dopo la decompressione e i corpi dei reindirizzamenti
  vengono scartati senza essere letti.
- Gli errori delle richieste stampano solo uno stato HTTP o una classe di errore, poiché un
  `--api-url` personalizzato può contenere credenziali.
- Il comando installato dai pacchetti `.deb` e `.rpm` esegue Python in modalità isolata.
  Ignora `PYTHONPATH`, la directory site dell'utente e i moduli nella directory di
  lavoro. Un'installazione tramite `pip` usa il console script standard e segue
  l'ambiente in cui è installata.
- Lo stato delle variazioni viene letto e scritto senza seguire un collegamento simbolico sul
  nome del file di stato o di lock, in modo relativo a una directory aperta una volta per controllo.
- Gli asset di release includono attestazioni di provenienza della build oltre a
  `SHA256SUMS`; consulta [Da GitHub Releases](#da-github-releases).

## Aggiornamento dalla versione 1.0.0

Queste modifiche sono incluse nella versione 2.0.0.

- Una quotazione con un timestamp del fornitore più vecchio di un'ora restituisce `UNKNOWN` a meno che
  non venga fornito un valore `--max-age` maggiore. Gli endpoint che non restituiscono alcun timestamp non sono interessati.
- `--currency` accetta solo da 2 a 16 lettere o cifre.
- Le stringhe numeriche con separatori delle cifre o spazi circostanti vengono rifiutate.
- Un'attesa di retry che non rientra nel budget segnala l'errore sottostante
  anziché `API request timed out`.
- I pacchetti nativi non tengono più conto di `PYTHONPATH`.
- Soglie pari o superiori a un milione appaiono nei performance data come decimali
  semplici anziché in notazione esponenziale.

## Localizzazione

La guida della CLI, gli errori di validazione e le descrizioni di stato del plugin supportano 45 localizzazioni (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) tramite cataloghi inclusi caricati con la stdlib. La risoluzione controlla `--lang`, quindi `LC_ALL`, `LC_MESSAGES` e `LANG`, ricorrendo infine a `en`. I prefissi di stato Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) e i performance data rimangono invariati in tutte le localizzazioni.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Sviluppo

Installa [mise](https://mise.jdx.dev/getting-started.html), quindi esegui la configurazione per lo sviluppo indicata sopra. `mise.toml` fissa le versioni di Python e uv. Gli strumenti di sviluppo sono dichiarati in `pyproject.toml` e risolti nel file `uv.lock` tracciato nel repository.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Installa gli hook di commit dopo la configurazione:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Usa `mise exec -- uv add --dev <tool>` oppure `mise exec -- uv add <dependency>` per aggiornare le dipendenze ed esegui il commit sia di `pyproject.toml` sia di `uv.lock`.

La CI verifica Python 3.12 e 3.13 su Linux e Python 3.13 su macOS. Ogni PR esegue inoltre la validazione dei pacchetti, l'audit delle dipendenze e CodeQL, e installa il pacchetto `.deb` su Ubuntu e l'`.rpm` su Fedora. Le distribuzioni compilate sono disponibili come artefatto `distributions` nelle esecuzioni della CI.

La versione del pacchetto e della CLI proviene da `check_bitcoin_price/__init__.py`. Consulta [il processo di release](../../../CONTRIBUTING.md#releases) per gli incrementi di versione e la pubblicazione automatica degli asset di release su GitHub.

## Contributi

Consulta [CONTRIBUTING.md](../../../CONTRIBUTING.md) per il flusso di lavoro di sviluppo e i requisiti dei commit con sign-off.

## Licenza

Questo progetto è rilasciato sotto licenza MIT: consulta il file [LICENSE](../../../LICENSE) per i dettagli.

## Autore

Thomas Vincent

## Ringraziamenti

- [CoinGecko](https://www.coingecko.com/) per aver fornito un'API gratuita per le criptovalute
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
