# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · **Hausa** · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Ƙarin manhaja (plugin) na Nagios/Icinga don sa ido kan farashin Bitcoin tare da iyakokin gargaɗi da matsananci da za a iya ƙayyadewa.

## Fasaloli

- Sa ido kan farashin Bitcoin a cikin kuɗaɗe daban-daban (USD, EUR, GBP, da sauransu)
- Iyakokin gargaɗi da matsananci da za a iya ƙayyadewa (na sama da na ƙasa)
- Daidaitaccen sakamakon ƙarin manhaja na Nagios tare da bayanan aiki
- Yana amfani da CoinGecko API (kyauta, ba a buƙatar maɓallin API)
- Goyon baya ga tashoshin API na musamman
- Iyakar lokaci da za a iya ƙayyadewa
- Binciken sabunta farashi ta amfani da alamomin lokaci na mai samarwa, tare da tsohuwar iyaka ta awa ɗaya
- Ƙayyadaddun sake gwadawa don iyakokin yawan buƙatu da matsalolin API na wucin gadi
- Wa'adin lokaci guda ɗaya ga dukkan ƙoƙari da iyakar 64 KiB ga kowane amsa
- Faɗakarwa ta zaɓi kan cikakken canjin kashi cikin sa'o'i 24
- Iyakokin farashi, tsawon lokacin buƙata, da tsufan farashi a cikin bayanan aiki

## Girkawa

### Daga GitHub Releases

Sauke fayilolin `.deb`, `.rpm`, `.tar.gz`, wheel, da `SHA256SUMS` daga [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Tabbatar da ingancin fayil ɗin da aka sauke tare da `sha256sum --ignore-missing --check SHA256SUMS`. Sakin da suka biyo bayan 1.0.0 kuma suna ɗauke da shaidar asalin gini mai sa hannu; tabbatar cewa wani fayil ya fito ne daga tsarin sakin wannan ma'ajiya tare da `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Yi amfani da sunayen fayiloli daga sakin da aka zaɓa. Fakitin tsari na asali suna girka `/usr/bin/check_bitcoin_price` da `/usr/lib/nagios/plugins/check_bitcoin_price`; fakitin RPM kuma yana samar da `/usr/lib64/nagios/plugins/check_bitcoin_price`. Umarnin da ke cikin fakitin yana gudanar da Python a yanayin keɓantacce, don haka yana ƙyale `PYTHONPATH` da manhajojin da ke cikin kundin aiki; mai sarrafa fakitin tsarin yana daidaita abubuwan dogaro na Python da `requests`. Suna ƙunshe da lambar Python mai zaman kanta daga tsarin na'ura kuma suna buƙatar tsarin da ke samar da Python 3.12 ko sabo.

### Daga Lambar Asali

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Don Haɓakawa

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Amfani

### Amfani na Asali

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Tare da Iyakoki

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Iyakoki Daban-daban

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Kuɗi Daban

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Iyakar Lokaci ta Musamman

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Sabunta Farashi da Kasafin Sake Gwadawa

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Farashin da ke ɗauke da alamar lokaci ta mai samarwa dole ne ya zama bai wuce awa ɗaya ba ta tsohuwa.
Tashoshin da ke dawo da farashi kaɗai suna ci gaba da aiki lokacin da babu `--max-age`.
Tare da `--max-age`, alamomin lokaci na mai samarwa da suka ɓace, marasa inganci, na gaba, ko tsofaffi suna dawo da
`UNKNOWN`; ƙarin manhajar ba ya maye gurbin lokacin farashin mai samarwa da lokacin ɗauka na na'urar gida.
Alamar lokaci da ta yi daidai da iyakar tsufa ana karɓar ta. Alamomin lokaci na gaba koyaushe ana ƙin su.

Tsohon saitin yana ba da damar sake gwadawa sau ɗaya. Kurakuran haɗi, ƙarewar lokaci, da amsoshin HTTP
408/429/500/502/503/504 kaɗai ake sake gwadawa. Jinkirin sake gwadawa yana farawa ne daga daƙiƙa 0.5 kuma
yana ninkuwa a sake gwadawa na gaba; daƙiƙun `Retry-After` da kwanakin HTTP su ne ke gaba.
Dukkan ƙoƙari, karanta amsa, fassara JSON, da jiran sake gwadawa suna raba
kasafin lokacin `--timeout`. Jiran sake gwadawa da ba zai shiga cikin kasafin lokaci ba yana dawo da `UNKNOWN` nan take
kuma yana bayar da rahoton matsalar da ta jawo shi, kamar `HTTP 429` ko `ConnectionError`,
ba ƙarewar lokaci ba. Matsalolin tantancewa, sauran kurakuran HTTP na dindindin, JSON mara inganci,
da amsoshin da suka fi 64 KiB na bayanan da aka fassara ba a sake gwada su. Yi amfani da
`--retries 0` don kashe sake gwadawa.

### Madadin tushen farashi

Yi amfani da zaɓuɓɓukan `--fallback-url URL` da za a iya maimaitawa tare da tashoshin da suka dace da CoinGecko.
Misali, ƙara `--fallback-url https://quotes.example.org/simple/price`.
Kowane tushe yana samun rabo daidai na ragowar wa'adin buƙatar, gami da sake gwadawarsa.
Matsala ta wucin gadi ko jinkirin sake gwadawa da ya fi wannan rabon yana wucewa zuwa tushe na gaba.
Matsalolin tabbatar da TLS, kurakuran HTTP na dindindin da farashi mara inganci suna dawo da UNKNOWN.
Kowane amsar farashi an iyakance shi zuwa 64 KiB na bayanan da aka fassara.
Lokacin da aka saita madadai, matsayin yana nuna tushen da ya amsa a matsayin
`primary`, `fallback1`, da sauransu, ba tare da buga URL ɗinsa ba.

### Canjin farashi na ɗan gajeren lokaci

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Ba mai amfani da sa ido wani kundin yanayi na sirri mai yiwuwar rubutu a kan tsarin fayil na gida na Linux ko
macOS. Ajiye fayil ɗin `.lock` na kusa da shi a wurinsa tsakanin bincike. Yi amfani da
fayil ɗin yanayi daban ga kowane tagar lokaci. Kuɗaɗe suna da tarihinsu daban-daban a cikinsa.
Tsohuwar tagar lokaci ita ce daƙiƙa 3600. Kowane ingantaccen farashi yana buƙatar alamar lokaci ta mai samarwa
a cikin tagar lokacin da iyakar tsufa, wadda take awa ɗaya sai dai idan `--max-age` ya saita
wata daban. Ƙarin manhajar yana kwatanta farashin yanzu da mafi tsohon farashi mai kyau na baya a cikin wannan tagar
kuma yana bayar da rahoton ainihin daƙiƙun da suka shude. Alamomin lokaci da aka maimaita ba sa ƙirƙirar ƙarin samfura.
Samfuri na farko, tsohon tarihin da ya ƙare, ko JSON da ya lalace yana fara sabon tushe;
ma'aunin tagar yana kasancewa ba a sani ba har sai an sami samfurin da za a iya kwatantawa. Sauran faɗakarwa suna ci gaba da
aiki. Yanayin da ba a iya rubutawa, fayil ɗin yanayi ko na kullewa mai mahadar alama (symbolic link), ko farashin da ya fi
sabon samfurin da aka rubuta tsufa suna dawo da UNKNOWN. Ma'aunin `bitcoin_move_window` mai alamar ƙari ko ragi
yana amfani da jeren gargaɗi da matsananci masu daidaito a ɓangarori biyu. Daidaito a kan iyaka ba ya tayar da faɗakarwa.

Ƙarin manhajar yana buɗe kundin yanayi sau ɗaya a kowane bincike kuma yana aiki dangane da shi, don haka
wani ɓangaren hanyar da aka canja yayin binciken ba zai iya karkatar da kullewa, karantawa,
ko rubutawa ba. Ana bin mahadar alama a ɓangaren kundin hanyar lokacin da binciken ya fara,
wanda ke sa mahadar tsari kamar `/var` a kan macOS su ci gaba da aiki.
Don haka kundin yanayi da kundaye iyayensa dole ne kada su zama masu yiwuwar rubutu ga sauran
masu amfani. Ana ƙirƙirar fayilolin yanayi da na kullewa da izinin mode 0600.

### Canjin Kashi na Yau da Kullum

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Iyakokin canji suna auna cikakkiyar ƙimar canjin kashi na sa'o'i 24 mai alamar ƙari ko ragi na CoinGecko
a cikin kuɗin da aka zaɓa. Canjin da ya yi daidai da iyaka ba ya tayar da faɗakarwa.
Idan an bayar da iyakokin biyu, gargaɗi bai kamata ya wuce matsananci ba.
Bayanan canjin da ake buƙata da suka ɓace ko marasa inganci suna dawo da `UNKNOWN`. Ana iya haɗa
faɗakarwar farashi da ta canji; mafi tsanani ita ce ke yin rinjaye, tare da fifikon farashi
lokacin da tsanani ya yi daidai.

## Zaɓuɓɓukan Layin Umarni

| Zaɓi | Bayani |
|--------|-------------|
| `-w`, `--warning` | Jeren iyakar gargaɗi (tsari: LOW:HIGH) |
| `-c`, `--critical` | Jeren iyakar matsananci (tsari: LOW:HIGH) |
| `--warning-low` | Iyakar gargaɗi don ƙaramin farashi |
| `--warning-high` | Iyakar gargaɗi don babban farashi |
| `--critical-low` | Iyakar matsananci don ƙaramin farashi |
| `--critical-high` | Iyakar matsananci don babban farashi |
| `--currency` | Lambar kuɗi mai haruffa ko lambobi 2-16 (tsoho: usd) |
| `--timeout` | Jimillar kasafin lokacin buƙata/sake gwadawa na API a cikin daƙiƙa, gami da ƙimomin juzu'i (tsoho: 10) |
| `--retries` | Ƙarin ƙoƙari na matsalolin wucin gadi, 0-5 (tsoho: 1) |
| `--max-age` | Matsakaicin tsufan farashin mai samarwa a cikin daƙiƙa kuma yana buƙatar alamar lokaci; farashi mai alamar lokaci yana da tsohon 3600 |
| `--warning-change` | Iyakar gargaɗi don cikakken canjin kashi na sa'o'i 24 |
| `--critical-change` | Iyakar matsananci don cikakken canjin kashi na sa'o'i 24 |
| `--api-url` | Babban API URL |
| `--fallback-url` | Ƙarin tasha mai dacewa; maimaita a tsarin fifiko |
| `--state-file` | Fayil ɗin tarihin canji na JSON |
| `--move-window` | Tagar lokacin canji a cikin daƙiƙa (tsoho: 3600) |
| `--warning-move`, `--critical-move` | Cikakkun iyakokin canjin tagar lokaci a cikin kashi |
| `-v`, `--verbose` | Kunna cikakken fitarwa |
| `-V`, `--version` | Nuna sigar manhaja |
| `-h`, `--help` | Nuna saƙon taimako |

## Saitin Nagios

### Ma'anar Umarni

Saita macro ɗin albarkatun Nagios `$USER1$` zuwa kundin ƙarin manhaja (fakitin tsari na asali suna amfani da `/usr/lib/nagios/plugins`). Ƙara a cikin saitin umarnin Nagios ɗinka:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Ma'anar Sabis

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

### Saitin Icinga2

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

## Lambobin Fita

Hujjoji marasa inganci, iyakokin lokaci marasa ƙima mai kyau, jeren iyakoki marasa inganci, da farashin API
marasa tsari suna dawo da `UNKNOWN` (lambar fita 3). Iyakoki dole ne su zama lambobi masu iyaka kuma marasa alamar ragi,
inda kowace iyaka ta ƙasa ba za ta fi iyakar samanta ba. Lambar kuɗi dole ne
ta zama haruffa ko lambobi 2-16. Ana ƙin saiti mara inganci kafin tuntuɓar
API. Farashi dole ne su zama masu iyaka kuma marasa alamar ragi, da aka bayar a matsayin lambobin JSON ko jimlolin
lambobin goma kai tsaye kamar `"43521.5"`. Amsar da ba ta da kuɗin da aka buƙata
tana ambaton sunansa, misali `Response has no EUR price`. Amsoshi marasa inganci ba sa fitar da
bayanan aiki. Cikakkun bayanan bincike suna zuwa stderr
domin stdout ya ƙunshi layin matsayin sa ido guda ɗaya kacal.

| Lamba | Matsayi | Bayani |
|------|--------|-------------|
| 0 | OK | Farashi yana cikin iyakar da aka yarda da ita |
| 1 | WARNING | Farashi ya wuce iyakar gargaɗi |
| 2 | CRITICAL | Farashi ya wuce iyakar matsananci |
| 3 | UNKNOWN | Kuskure ya faru (matsalar API, ƙarewar lokaci, da sauransu) |

## Bayanan Aiki

Ƙarin manhajar yana fitar da bayanan aiki a daidaitaccen tsarin Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Bayanan aikin farashi sun haɗa da jeren gargaɗi/matsananci da aka saita da
mafi ƙarancin sifili. Ana buga iyakoki a cikakken tsarin lambobin goma, ba tare da rage su
ko mayar da su sigar ƙarfi (exponent) ba, don manyan ƙimomi kamar `14500000:16250000` su ci gaba da zama masu sauƙin fassara. Lokacin buƙata ya haɗa da dukkan ƙoƙari da jinkirin sake gwadawa. Ana fitar da tsufan farashi ne
kawai lokacin da mai samarwa ya ba da ingantacciyar alamar lokaci; ana fitar da canjin yau da kullum
lokacin da yake akwai. Jeren canji yana daidaita a ɓangarorin biyu na sifili. Bayanan da ba su da inganci ko tsofaffi
suna haifar da `UNKNOWN` ba tare da bayanan aikin farashi ba. Ana iya amfani da waɗannan ma'aunai tare da
kayan aikin zane kamar PNP4Nagios, Grafana, ko InfluxDB.

## API

Wannan ƙarin manhajar yana amfani da [CoinGecko API](https://www.coingecko.com/en/api) ta tsohuwa, wanda yake kyauta kuma ba ya buƙatar maɓallin API. Iyakokin yawan buƙatu suna aiki.

Tashoshin API na musamman dole ne su yi amfani da irin wannan tsarin amsa: `bitcoin.<currency>` don
farashi, `bitcoin.last_updated_at` don daƙiƙun alamar lokaci ta UNIX, da
`bitcoin.<currency>_24h_change` don canjin kashi na yau da kullum mai alamar ƙari ko ragi. Farashi kaɗai
ake buƙata lokacin da babu `--max-age` da iyakokin canji. Alamar lokaci
da take akwai har yanzu ana bincika ta: kada ta zama ta gaba ko fiye da awa
ɗaya. Amsar da aka fassara dole ne ta shiga cikin 64 KiB.

Kuɗaɗen da ake goyon baya sun haɗa da: usd, eur, gbp, jpy, aud, cad, chf, cny, da wasu da yawa.

## Tsaro

An aiwatar da matakan da ke ƙasa a cikin lambar yanzu. Suna iyakance abin da tasha mai kuskure ko mai amfani na gida zai iya yi wa
na'urar sa ido; ba sa sa farashin da kansa ya zama abin dogaro.

- Ana tabbatar da takaddun shaida na HTTPS tare da tsoffin saitunan `requests`, kuma babu zaɓin da ke
  kashe tabbatarwa. `--api-url` na musamman da ke amfani da `http://` kai tsaye ba shi da
  irin wannan kariyar.
- DNS, haɗi, karantawa, sake gwadawa, da jinkirin sake gwadawa suna raba wa'adin `--timeout`.
  Na'urar da ke aika bayanai a hankali ba za ta iya tsawaita shi ba.
- Kowane amsa an iyakance shi zuwa 64 KiB bayan buɗe matsi, kuma ana zubar da jikin
  tura buƙata (redirect) ba tare da karantawa ba.
- Matsalolin buƙata suna buga matsayin HTTP ko nau'in kuskure kaɗai, saboda `--api-url`
  na musamman na iya ƙunsar bayanan sirri na shiga.
- Umarnin da `.deb` da `.rpm` suka girka yana gudanar da Python a yanayin keɓantacce.
  Yana ƙyale `PYTHONPATH`, kundin fakitin mai amfani (user site directory), da manhajojin da ke cikin
  kundin aiki. Girkawa ta `pip` tana amfani da daidaitaccen rubutun umarni kuma tana bin
  muhallin da aka girka ta a ciki.
- Ana karanta da rubuta yanayin canji ba tare da bin mahadar alama (symbolic link) a
  sunan fayil ɗin yanayi ko na kullewa ba, dangane da kundin da aka buɗe sau ɗaya a kowane bincike.
- Fayilolin saki suna ɗauke da shaidar asalin gini baya ga
  `SHA256SUMS`; duba [Daga GitHub Releases](#from-github-releases).

## Ɗaukakawa daga 1.0.0

Waɗannan canje-canjen suna zuwa a cikin 2.0.0.

- Farashin da ke da alamar lokaci ta mai samarwa wadda ta fi awa ɗaya tsufa yana dawo da `UNKNOWN` sai dai idan an ba da
  mafi girman `--max-age`. Tashoshin da ba sa dawo da alamar lokaci abin bai shafe su ba.
- `--currency` yana karɓar haruffa ko lambobi 2-16 kaɗai.
- Ana ƙin jimlolin lambobi masu raba lambobi ko sarari a gefensu.
- Jiran sake gwadawa da bai shiga cikin kasafin lokaci ba yana bayar da rahoton matsalar asali
  maimakon `API request timed out`.
- Fakitin tsari na asali ba sa ƙara bin `PYTHONPATH`.
- Iyakokin miliyan ɗaya ko fiye suna bayyana a cikin bayanan aiki a matsayin lambobin
  goma kai tsaye maimakon sigar ƙarfi (exponent).

## Fassarar Harsuna

Taimakon CLI, kurakuran tabbatarwa, da bayanan matsayin ƙarin manhaja suna goyon bayan harsuna da yankuna 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ta amfani da kundin fassara da aka haɗa waɗanda ake ɗorawa da stdlib. Zaɓin harshe yana duba `--lang`, sannan `LC_ALL`, `LC_MESSAGES`, da `LANG`, tare da komawa ga `en` idan ba a same su ba. Kalmomin farko na matsayin Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) da bayanan aiki ba sa canzawa a dukkan harsuna.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Haɓakawa

Girka [mise](https://mise.jdx.dev/getting-started.html), sannan ka gudanar da saitin haɓakawa na sama. `mise.toml` yana ƙayyade sigar Python da uv. An bayyana kayan aikin haɓakawa a cikin `pyproject.toml` kuma an daidaita su a cikin `uv.lock` da aka yi commit ɗinsa.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Girka commit hooks bayan saiti:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Yi amfani da `mise exec -- uv add --dev <tool>` ko `mise exec -- uv add <dependency>` don sabunta abubuwan dogaro sannan ka yi commit na `pyproject.toml` da `uv.lock` tare.

CI yana duba Python 3.12 da 3.13 a kan Linux da Python 3.13 a kan macOS. Kowane PR kuma yana gudanar da tabbatar da fakiti, binciken abubuwan dogaro, da CodeQL, kuma yana girka `.deb` a kan Ubuntu da `.rpm` a kan Fedora. Fakitin da aka gina suna samuwa a matsayin kayan aikin `distributions` a gudanarwar CI.

Sigar fakitin da CLI tana fitowa ne daga `check_bitcoin_price/__init__.py`. Duba [tsarin saki](../../../CONTRIBUTING.md#releases) don ƙara lambar siga da wallafa fayilolin sakin GitHub ta atomatik.

## Ba da Gudummawa

Duba [CONTRIBUTING.md](../../../CONTRIBUTING.md) don tsarin aikin haɓakawa da ƙa'idojin commit masu sa hannu.

## Lasisi

An ba da lasisin wannan aikin ƙarƙashin MIT License - duba fayil ɗin [LICENSE](../../../LICENSE) don ƙarin bayani.

## Mawallafi

Thomas Vincent

## Godiya

- [CoinGecko](https://www.coingecko.com/) saboda samar da API na kuɗin intanet kyauta
- [Ƙa'idojin Haɓaka Ƙarin Manhajoji na Nagios](https://nagios-plugins.org/doc/guidelines.html)
