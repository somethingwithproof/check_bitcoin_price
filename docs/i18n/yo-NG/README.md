# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · **Yorùbá** · [isiZulu](../zu-ZA/README.md)

</details>

Àfikún Nagios/Icinga láti ṣàbójútó iye owó Bitcoin pẹ̀lú àwọn ààlà ìkìlọ̀ àti eléwu tí a lè ṣètò.

## Àwọn Ẹ̀yà Pàtàkì

- Ṣàbójútó iye owó Bitcoin ní oríṣiríṣi owó orílẹ̀-èdè (USD, EUR, GBP, àti bẹ́ẹ̀ bẹ́ẹ̀ lọ)
- Àwọn ààlà ìkìlọ̀ àti eléwu tí a lè ṣètò (òkè àti ìsàlẹ̀)
- Àbájáde àfikún Nagios tí ó wà ní ìlànà pẹ̀lú dátà ìṣiṣẹ́
- Ó ń lo CoinGecko API (ọ̀fẹ́ ni, kò nílò kọ́kọ́rọ́ API)
- Àtìlẹ́yìn fún àwọn ojú-ọ̀nà API àdáni
- Àkókò ìdádúró tí a lè ṣètò
- Àwọn àyẹ̀wò ìṣẹ̀ṣẹ̀-jáde iye owó nípa lílo àmì-àkókò olùpèsè, pẹ̀lú ààlà àkókò wákàtí kan gẹ́gẹ́ bí àìyípadà
- Àwọn ìtúngbìyànjú tí ó ní ààlà fún ààlà ìwọ̀n ìbéèrè àti ìkùnà API ìgbà díẹ̀
- Ààlà àkókò kan ṣoṣo fún gbogbo ìgbìyànjú àti ààlà 64 KiB lórí ìdáhùn kọ̀ọ̀kan
- Àwọn ìtànijí àṣàyàn lórí ìyípadà ìpín nínú ọgọ́rùn-ún wákàtí 24 ní pàtó
- Àwọn ààlà iye owó, àkókò ìbéèrè, àti ọjọ́-orí iye owó nínú dátà ìṣiṣẹ́

## Ìfisílé

### Láti Àwọn Ìtúsílẹ̀ GitHub

Ṣe ìgbàsílẹ̀ àwọn fáìlì `.deb`, `.rpm`, `.tar.gz`, wheel, àti `SHA256SUMS` láti [Àwọn Ìtúsílẹ̀ GitHub](https://github.com/somethingwithproof/check_bitcoin_price/releases). Ṣàyẹ̀wò ìgbàsílẹ̀ kan pẹ̀lú `sha256sum --ignore-missing --check SHA256SUMS`. Àwọn ìtúsílẹ̀ lẹ́yìn 1.0.0 tún ní ẹ̀rí ìpilẹ̀ṣẹ̀ ìkọ́lé tí a fọwọ́ sí; fìdí rẹ̀ múlẹ̀ pé ohun-ìní kan wá láti ìṣàn-iṣẹ́ ìtúsílẹ̀ ibi-ìpamọ́ yìí pẹ̀lú `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Lo àwọn orúkọ fáìlì láti inú ìtúsílẹ̀ tí o yàn. Àwọn páákẹ́ẹ̀jì abínibí máa ń fi `/usr/bin/check_bitcoin_price` àti `/usr/lib/nagios/plugins/check_bitcoin_price` sílẹ̀; RPM náà tún ń pèsè `/usr/lib64/nagios/plugins/check_bitcoin_price`. Àṣẹ tí a dì sínú páákẹ́ẹ̀jì máa ń ṣiṣẹ́ Python ní ipò ìyàsọ́tọ̀, nítorí náà ó máa ń fojú fo `PYTHONPATH` àti àwọn mọ́dùlù nínú àkójọpọ̀-fáìlì iṣẹ́; olùṣàkóso páákẹ́ẹ̀jì ètò ló ń yanjú àwọn ìgbẹ́kẹ̀lé Python àti `requests`. Wọ́n ní kóòdù Python tí kò gbára lé irú ẹ̀rọ pàtó kan, wọ́n sì nílò ìpèsè ètò tí ó ń pèsè Python 3.12 tàbí tuntun jù bẹ́ẹ̀ lọ.

### Láti Orísun Kóòdù

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Fún Ìdàgbàsókè

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Ìlò

### Ìlò Ìpìlẹ̀

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Pẹ̀lú Àwọn Ààlà

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Àwọn Ààlà Kọ̀ọ̀kan

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Owó Orílẹ̀-èdè Mìíràn

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Àkókò Ìdádúró Àdáni

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Ìṣẹ̀ṣẹ̀-jáde àti Ìṣúná Ìtúngbìyànjú

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Iye owó tí ó ní àmì-àkókò olùpèsè kò gbọ́dọ̀ ju wákàtí kan lọ gẹ́gẹ́ bí àìyípadà.
Àwọn ojú-ọ̀nà tí ó ń dá iye owó nìkan padà ṣì ṣeé lò nígbà tí `--max-age` kò bá sí.
Pẹ̀lú `--max-age`, àmì-àkókò olùpèsè tí ó sọnù, tí kò tọ́, tí ó wà ní ọjọ́ iwájú, tàbí tí ó ti pẹ́ jù máa ń dá `UNKNOWN` padà; àfikún náà kì í fi àkókò ìgbàwọlé abẹ́lé rọ́pò àkókò iye owó olùpèsè. Àmì-àkókò tí ó wà ní ààlà ọjọ́-orí gẹ́lẹ́ ṣì jẹ́ ìtẹ́wọ́gbà. Àwọn àmì-àkókò ọjọ́ iwájú ni a máa ń kọ̀ nígbà gbogbo.

Ìṣètò àìyípadà gba ìtúngbìyànjú kan láàyè. Àṣìṣe ìjápọ̀, àkókò ìdádúró, àti àwọn ìdáhùn HTTP 408/429/500/502/503/504 nìkan ni a máa ń túngbìyànjú. Àkókò ìdádúró-padà bẹ̀rẹ̀ ní ìṣẹ́jú-àáyá 0.5, ó sì máa ń di ìlọ́po méjì fún àwọn ìtúngbìyànjú tí ó tẹ̀lé e; àwọn ìṣẹ́jú-àáyá `Retry-After` àti àwọn déètì HTTP ni ó ní àkọ́kọ́. Gbogbo ìgbìyànjú, kíkà ìdáhùn, ìtúmọ̀ JSON, àti ìdádúró ìtúngbìyànjú pín ìṣúná `--timeout`. Ìdádúró ìtúngbìyànjú tí kò lè gbà sínú àkókò náà máa ń dá `UNKNOWN` padà lẹ́sẹ̀kẹsẹ̀, ó sì ń ròyìn ìkùnà tí ó fà á, bíi `HTTP 429` tàbí `ConnectionError`, kì í ṣe àkókò ìdádúró. Àwọn ìkùnà ìdánimọ̀, àwọn àṣìṣe HTTP mìíràn tí kì í ṣe ìgbà díẹ̀, JSON tí kò tọ́, àti àwọn ìdáhùn tí ó tóbi ju 64 KiB dátà tí a túmọ̀ lọ kì í ṣe ohun tí a ń túngbìyànjú. Lo `--retries 0` láti pa ìtúngbìyànjú.

### Àwọn orísun iye owó ìfẹ̀yìntì

Lo àwọn àṣàyàn `--fallback-url URL` tí a lè tún ṣe pẹ̀lú àwọn ojú-ọ̀nà tí ó bá CoinGecko mu.
Fún àpẹẹrẹ, fi `--fallback-url https://quotes.example.org/simple/price` kún un.
Orísun kọ̀ọ̀kan gba ìpín dọ́gba nínú ààlà àkókò ìbéèrè tí ó kù, pẹ̀lú àwọn ìtúngbìyànjú rẹ̀. Ìkùnà ìgbà díẹ̀ tàbí ìdádúró ìtúngbìyànjú tí ó gùn ju ìpín yẹn lọ máa ń tẹ̀síwájú sí orísun tí ó kàn. Àwọn ìkùnà ìfìdímúlẹ̀ TLS, àwọn àṣìṣe HTTP tí kì í ṣe ìgbà díẹ̀ àti àwọn iye owó tí kò tọ́ máa ń dá UNKNOWN padà. Ìdáhùn iye owó kọ̀ọ̀kan ní ààlà 64 KiB ti dátà tí a túmọ̀.
Nígbà tí a bá ṣètò àwọn ìfẹ̀yìntì, ipò náà máa ń fi orísun tí ó dáhùn hàn gẹ́gẹ́ bí `primary`, `fallback1`, àti bẹ́ẹ̀ bẹ́ẹ̀ lọ, láì tẹ URL rẹ̀ jáde.

### Ìyípadà àkókò kúkúrú

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Fún olùmúlò ìṣàbójútó ní àkójọpọ̀-fáìlì ipò àdáni tí ó ṣeé kọ sí lórí ètò fáìlì abẹ́lé Linux tàbí macOS. Fi fáìlì `.lock` ẹgbẹ́ rẹ̀ sípò rẹ̀ láàárín àwọn àyẹ̀wò. Lo fáìlì ipò ọ̀tọ̀ọ̀tọ̀ fún fèrèsé kọ̀ọ̀kan. Àwọn owó orílẹ̀-èdè ní àwọn ìtàn olómìnira nínú rẹ̀.
Fèrèsé àìyípadà jẹ́ ìṣẹ́jú-àáyá 3600. Iye owó títọ́ kọ̀ọ̀kan nílò àmì-àkókò olùpèsè láàárín fèrèsé àti ààlà ọjọ́-orí, èyí tí ó jẹ́ wákàtí kan àyàfi tí `--max-age` bá ṣètò òmíràn. Àfikún náà máa ń fi iye owó lọ́wọ́lọ́wọ́ wé iye owó rere tí ó pẹ́ jù lọ tẹ́lẹ̀ nínú fèrèsé yẹn, ó sì ń ròyìn iye ìṣẹ́jú-àáyá gidi tí ó ti kọjá. Àwọn àmì-àkókò tí a tún ṣe kì í dá àwọn àpẹẹrẹ àfikún sílẹ̀.
Àpẹẹrẹ àkọ́kọ́, ìtàn tí ó ti parí àkókò rẹ̀, tàbí JSON tí ó bàjẹ́ máa ń bẹ̀rẹ̀ ìpìlẹ̀ tuntun; òṣùwọ̀n fèrèsé náà yóò jẹ́ àìmọ̀ títí tí àpẹẹrẹ tí a lè fi wé e yóò fi wà. Àwọn ìtànijí mìíràn ṣì ń ṣiṣẹ́. Ipò tí kò ṣeé kọ sí, fáìlì ipò tàbí ìtìpa tí ó jẹ́ ìjápọ̀ àmì, tàbí iye owó tí ó pẹ́ ju àpẹẹrẹ tuntun jù lọ tí a kọ sílẹ̀ máa ń dá UNKNOWN padà. Òṣùwọ̀n `bitcoin_move_window` tí ó ní àmì ń lo àwọn ààlà ìkìlọ̀ àti eléwu dọ́gba. Ìdọ́gba ní ààlà kò ní tan ìtànijí.

Àfikún náà máa ń ṣí àkójọpọ̀-fáìlì ipò lẹ́ẹ̀kan fún àyẹ̀wò kọ̀ọ̀kan, ó sì ń ṣiṣẹ́ ní ìbámu pẹ̀lú rẹ̀, kí apá ọ̀nà kan tí a rọ́pò lákòókò àyẹ̀wò má baà lè yí ìtìpa, kíkà, tàbí kíkọ sí ibòmíràn. A máa ń tẹ̀lé àwọn ìjápọ̀ àmì ní apá àkójọpọ̀-fáìlì ti ọ̀nà náà nígbà tí àyẹ̀wò bá bẹ̀rẹ̀, èyí tí ó ń jẹ́ kí àwọn ìjápọ̀ pèpéle bíi `/var` lórí macOS ṣì ṣeé lò. Nítorí náà, àkójọpọ̀-fáìlì ipò àti àwọn àkójọpọ̀-fáìlì òbí rẹ̀ kò gbọ́dọ̀ ṣeé kọ sí fún àwọn olùmúlò mìíràn. A máa ń dá àwọn fáìlì ipò àti ìtìpa sílẹ̀ pẹ̀lú ipò àṣẹ 0600.

### Ìyípadà Ìpín Nínú Ọgọ́rùn-ún Ojoojúmọ́

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Àwọn ààlà ìyípadà máa ń wọn iye pàtó ti ìyípadà ìpín nínú ọgọ́rùn-ún wákàtí 24 tí ó ní àmì ti CoinGecko nínú owó orílẹ̀-èdè tí a yàn. Ìyípadà tí ó wà ní ààlà gẹ́lẹ́ kò ní tan ìtànijí. Tí a bá pèsè ààlà méjèèjì, ìkìlọ̀ kò gbọ́dọ̀ ju eléwu lọ.
Dátà ìyípadà tí a nílò tí ó sọnù tàbí tí kò tọ́ máa ń dá `UNKNOWN` padà. A lè so àwọn ìtànijí iye owó àti ìyípadà pọ̀; ìwọ̀n líle tí ó ga jù lọ ni yóò borí, pẹ̀lú iye owó tí ó ń gba àkọ́kọ́ nígbà tí ìwọ̀n líle bá dọ́gba.

## Àwọn Àṣàyàn Láìnì Àṣẹ

| Àṣàyàn | Àpèjúwe |
|--------|---------|
| `-w`, `--warning` | Àkàwé ààlà ìkìlọ̀ (ìṣètò: LOW:HIGH) |
| `-c`, `--critical` | Àkàwé ààlà eléwu (ìṣètò: LOW:HIGH) |
| `--warning-low` | Ààlà ìkìlọ̀ fún iye owó kékeré |
| `--warning-high` | Ààlà ìkìlọ̀ fún iye owó gíga |
| `--critical-low` | Ààlà eléwu fún iye owó kékeré |
| `--critical-high` | Ààlà eléwu fún iye owó gíga |
| `--currency` | Kóòdù owó orílẹ̀-èdè ti lẹ́tà tàbí nọ́ńbà 2-16 (àìyípadà: usd) |
| `--timeout` | Àpapọ̀ ìṣúná ìbéèrè/ìtúngbìyànjú API ní ìṣẹ́jú-àáyá, pẹ̀lú àwọn iye ìdá (àìyípadà: 10) |
| `--retries` | Àwọn ìgbìyànjú ìgbà díẹ̀ àfikún, 0–5 (àìyípadà: 1) |
| `--max-age` | Ọjọ́-orí iye owó olùpèsè tí ó pọ̀ jù lọ ní ìṣẹ́jú-àáyá, ó sì nílò àmì-àkókò; àwọn iye owó tí ó ní àmì-àkókò ní àìyípadà 3600 |
| `--warning-change` | Ààlà ìkìlọ̀ fún ìyípadà ìpín nínú ọgọ́rùn-ún wákàtí 24 ní pàtó |
| `--critical-change` | Ààlà eléwu fún ìyípadà ìpín nínú ọgọ́rùn-ún wákàtí 24 ní pàtó |
| `--api-url` | URL API àkọ́kọ́ |
| `--fallback-url` | Ojú-ọ̀nà àfikún tí ó bá a mu; tún ṣe é ní ìtòlẹ́sẹẹsẹ tí o fẹ́ |
| `--state-file` | Fáìlì ìtàn ìyípadà JSON |
| `--move-window` | Fèrèsé ìyípadà ní ìṣẹ́jú-àáyá (àìyípadà: 3600) |
| `--warning-move`, `--critical-move` | Àwọn ààlà ìyípadà fèrèsé ní pàtó ní ìpín nínú ọgọ́rùn-ún |
| `-v`, `--verbose` | Tan àbájáde alálàyé kíkún |
| `-V`, `--version` | Fi ẹ̀yà hàn |
| `-h`, `--help` | Fi ìfiranṣẹ́ ìrànlọ́wọ́ hàn |

## Ìṣètò Nagios

### Ìtumọ̀ Àṣẹ

Ṣètò mákírò ohun-èlò Nagios `$USER1$` sí àkójọpọ̀-fáìlì àfikún (àwọn páákẹ́ẹ̀jì abínibí ń lo `/usr/lib/nagios/plugins`). Fi kún ìṣètò àwọn àṣẹ Nagios rẹ:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Ìtumọ̀ Iṣẹ́

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

### Ìṣètò Icinga2

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

## Àwọn Kóòdù Ìjáde

Àwọn àríyànjiyàn tí kò tọ́, àwọn àkókò ìdádúró tí kì í ṣe rere, àwọn àkàwé ààlà tí kò tọ́, àti àwọn iye owó API tí kò dára máa ń dá `UNKNOWN` padà (ìjáde 3). Àwọn ààlà gbọ́dọ̀ jẹ́ nọ́ńbà tí ó ní òpin, tí kì í ṣe òdì, pẹ̀lú ààlà ìsàlẹ̀ kọ̀ọ̀kan tí kò ju ààlà òkè rẹ̀ lọ. Owó orílẹ̀-èdè gbọ́dọ̀ jẹ́ lẹ́tà tàbí nọ́ńbà 2-16. A máa ń kọ ìṣètò tí kò tọ́ sílẹ̀ kí a tó kàn sí API. Àwọn iye owó gbọ́dọ̀ ní òpin kí wọ́n má sì jẹ́ òdì, tí a fúnni gẹ́gẹ́ bí nọ́ńbà JSON tàbí okùn dẹ́símà lásán bíi `"43521.5"`. Ìdáhùn láìsí owó orílẹ̀-èdè tí a béèrè máa ń dárúkọ rẹ̀, fún àpẹẹrẹ `Response has no EUR price`. Àwọn ìdáhùn tí kò tọ́ kì í tú dátà ìṣiṣẹ́ jáde. Àwọn àyẹ̀wò alálàyé kíkún máa ń lọ sí stderr kí stdout lè ní ìlà ipò ìṣàbójútó kan ṣoṣo.

| Kóòdù | Ipò | Àpèjúwe |
|-------|-----|---------|
| 0 | OK | Iye owó wà láàárín àkàwé ìtẹ́wọ́gbà |
| 1 | WARNING | Iye owó kọjá ààlà ìkìlọ̀ |
| 2 | CRITICAL | Iye owó kọjá ààlà eléwu |
| 3 | UNKNOWN | Àṣìṣe ṣẹlẹ̀ (ìkùnà API, àkókò ìdádúró, àti bẹ́ẹ̀ bẹ́ẹ̀ lọ) |

## Dátà Ìṣiṣẹ́

Àfikún náà máa ń tú dátà ìṣiṣẹ́ jáde ní ìṣètò Nagios tí ó wà ní ìlànà:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Dátà ìṣiṣẹ́ iye owó ní àwọn àkàwé ìkìlọ̀/eléwu tí a ṣètò àti òdo gẹ́gẹ́ bí ó kéré jù lọ. A máa ń tẹ àwọn ààlà jáde ní kíkọ dẹ́símà kíkún, láì yí i ká tàbí fi sínú ìṣètò oní-agbára, kí àwọn iye ńlá bíi `14500000:16250000` lè ṣeé túmọ̀. Àkókò ìbéèrè ní gbogbo ìgbìyànjú àti ìdádúró-padà. A máa ń tú ọjọ́-orí iye owó jáde nìkan nígbà tí olùpèsè bá pèsè àmì-àkókò títọ́; a máa ń tú ìyípadà ojoojúmọ́ jáde nígbà tí ó bá wà. Àwọn àkàwé ìyípadà dọ́gba yí òdo ká. Dátà tí kò tọ́ tàbí tí ó ti pẹ́ jù máa ń mú `UNKNOWN` jáde láìsí dátà ìṣiṣẹ́ iye owó. A lè lo àwọn òṣùwọ̀n wọ̀nyí pẹ̀lú àwọn irinṣẹ́ àwòrán ìṣirò bíi PNP4Nagios, Grafana, tàbí InfluxDB.

## API

Àfikún yìí ń lo [CoinGecko API](https://www.coingecko.com/en/api) gẹ́gẹ́ bí àìyípadà, èyí tí ó jẹ́ ọ̀fẹ́ tí kò sì nílò kọ́kọ́rọ́ API. Àwọn ààlà ìwọ̀n ìbéèrè wà.

Àwọn ojú-ọ̀nà àdáni gbọ́dọ̀ lo ìṣètò ìdáhùn kan náà: `bitcoin.<currency>` fún iye owó, `bitcoin.last_updated_at` fún àwọn ìṣẹ́jú-àáyá àmì-àkókò UNIX, àti `bitcoin.<currency>_24h_change` fún ìyípadà ìpín nínú ọgọ́rùn-ún ojoojúmọ́ tí ó ní àmì. Iye owó nìkan ni a nílò nígbà tí `--max-age` àti àwọn ààlà ìyípadà kò bá sí. A ṣì máa ń ṣàyẹ̀wò àmì-àkókò tí ó bá wà: kò gbọ́dọ̀ wà ní ọjọ́ iwájú tàbí ju wákàtí kan lọ. Ìdáhùn tí a túmọ̀ gbọ́dọ̀ gbà sínú 64 KiB.

Àwọn owó orílẹ̀-èdè tí a ṣe àtìlẹ́yìn fún ní: usd, eur, gbp, jpy, aud, cad, chf, cny, àti ọ̀pọ̀lọpọ̀ mìíràn.

## Ààbò

Àwọn ìgbésẹ̀ ìsàlẹ̀ yìí ni a ti ṣe àmúlò nínú kóòdù lọ́wọ́lọ́wọ́. Wọ́n ń dín ohun tí ojú-ọ̀nà tí kò hùwà dáadáa tàbí olùmúlò abẹ́lé kan lè ṣe sí ẹ̀rọ ìṣàbójútó kù; wọn kò sọ iye owó fúnra rẹ̀ di èyí tí ó ṣeé gbẹ́kẹ̀lé.

- A máa ń fìdí àwọn ìwé-ẹ̀rí HTTPS múlẹ̀ pẹ̀lú àwọn àìyípadà `requests`, kò sì sí àṣàyàn kankan tí ó ń pa ìfìdímúlẹ̀. `--api-url` àdáni tí ó ń lo `http://` lásán kò ní irú ààbò bẹ́ẹ̀.
- DNS, ìjápọ̀, kíkà, àwọn ìtúngbìyànjú, àti ìdádúró-padà pín ààlà àkókò `--timeout`. Ẹ̀rọ ẹlẹgbẹ́ kan tí ó ń fi dátà ránṣẹ́ díẹ̀díẹ̀ kò lè fà á gùn.
- Ìdáhùn kọ̀ọ̀kan ní ààlà 64 KiB lẹ́yìn ìtú-ìfúnpa, a sì máa ń da ara ìtọ́sí-ìbòmíràn nù láì kà á.
- Àwọn ìkùnà ìbéèrè máa ń tẹ ipò HTTP tàbí ẹ̀ka àṣìṣe nìkan jáde, nítorí `--api-url` àdáni kan lè ní àwọn ẹ̀rí-ìdánimọ̀ nínú.
- Àṣẹ tí `.deb` àti `.rpm` fi sílẹ̀ máa ń ṣiṣẹ́ Python ní ipò ìyàsọ́tọ̀. Ó máa ń fojú fo `PYTHONPATH`, àkójọpọ̀-fáìlì ojú-òpó olùmúlò, àti àwọn mọ́dùlù nínú àkójọpọ̀-fáìlì iṣẹ́. Ìfisílé `pip` kan ń lo ìwé-àṣẹ kọ́nsóòlù tí ó wà ní ìlànà, ó sì ń tẹ̀lé àyíká tí a fi í sí.
- A máa ń ka ipò ìyípadà, a sì ń kọ ọ́ láì tẹ̀lé ìjápọ̀ àmì ní orúkọ fáìlì ipò tàbí ìtìpa, ní ìbámu pẹ̀lú àkójọpọ̀-fáìlì tí a ṣí lẹ́ẹ̀kan fún àyẹ̀wò kọ̀ọ̀kan.
- Àwọn ohun-ìní ìtúsílẹ̀ ní àwọn ẹ̀rí ìpilẹ̀ṣẹ̀ ìkọ́lé ní àfikún sí `SHA256SUMS`; wo [Láti Àwọn Ìtúsílẹ̀ GitHub](#from-github-releases).

## Ìgbésókè láti 1.0.0

Àwọn àyípadà wọ̀nyí wà nínú 2.0.0.

- Iye owó tí ó ní àmì-àkókò olùpèsè tí ó ju wákàtí kan lọ máa ń dá `UNKNOWN` padà àyàfi tí a bá fúnni ní `--max-age` tí ó tóbi jù. Àwọn ojú-ọ̀nà tí kì í dá àmì-àkókò padà kò ní ipa kankan.
- `--currency` gba lẹ́tà tàbí nọ́ńbà 2-16 nìkan.
- A máa ń kọ àwọn okùn nọ́ńbà tí ó ní àwọn ìpínyà nọ́ńbà tàbí ààyè yí i ká sílẹ̀.
- Ìdádúró ìtúngbìyànjú tí kò gbà sínú ìṣúná àkókò máa ń ròyìn ìkùnà ìpìlẹ̀ dípò `API request timed out`.
- Àwọn páákẹ́ẹ̀jì abínibí kò tẹ̀lé `PYTHONPATH` mọ́.
- Àwọn ààlà ti mílíọ̀nù kan tàbí jù bẹ́ẹ̀ lọ máa ń hàn nínú dátà ìṣiṣẹ́ gẹ́gẹ́ bí dẹ́símà lásán dípò ìṣètò oní-agbára.

## Ìtúmọ̀ Èdè Àdúgbò

Ìrànlọ́wọ́ CLI, àwọn àṣìṣe ìfìdímúlẹ̀, àti àwọn àpèjúwe ipò àfikún ń ṣe àtìlẹ́yìn fún àwọn èdè àdúgbò 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) nípa lílo àwọn àkójọ èdè tí a kó pọ̀ tí stdlib ń gbé sókè. Ìpinnu èdè máa ń ṣàyẹ̀wò `--lang`, lẹ́yìn náà `LC_ALL`, `LC_MESSAGES`, àti `LANG`, tí ó sì ń padà sí `en`. Àwọn ìṣáájú ipò Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) àti dátà ìṣiṣẹ́ kò yí padà káàkiri gbogbo àwọn èdè àdúgbò.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Ìdàgbàsókè

Ṣe ìfisílé [mise](https://mise.jdx.dev/getting-started.html), lẹ́yìn náà ṣiṣẹ́ ìṣètò ìdàgbàsókè lókè. `mise.toml` so Python àti uv mọ́lẹ̀. A kéde àwọn irinṣẹ́ ìdàgbàsókè nínú `pyproject.toml`, a sì yanjú wọn nínú `uv.lock` tí a ti fi sílẹ̀.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Ṣe ìfisílé àwọn ìkọ́ commit lẹ́yìn ìṣètò:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Lo `mise exec -- uv add --dev <tool>` tàbí `mise exec -- uv add <dependency>` láti ṣe àtúnṣe àwọn ìgbẹ́kẹ̀lé kí o sì fi `pyproject.toml` àti `uv.lock` méjèèjì sílẹ̀.

CI máa ń ṣàyẹ̀wò Python 3.12 àti 3.13 lórí Linux àti Python 3.13 lórí macOS. Gbogbo PR tún ń ṣiṣẹ́ ìfìdímúlẹ̀ páákẹ́ẹ̀jì, àyẹ̀wò ààbò ìgbẹ́kẹ̀lé, àti CodeQL, ó sì ń fi `.deb` sílẹ̀ lórí Ubuntu àti `.rpm` lórí Fedora. Àwọn ìpèsè tí a kọ́ wà gẹ́gẹ́ bí ohun-ìní `distributions` lórí àwọn ìṣiṣẹ́ CI.

Ẹ̀yà páákẹ́ẹ̀jì àti CLI wá láti inú `check_bitcoin_price/__init__.py`. Wo [ìlànà ìtúsílẹ̀](../../../CONTRIBUTING.md#releases) fún ìgbésókè ẹ̀yà àti ìtẹ̀jáde aládàáṣe ti àwọn ohun-ìní ìtúsílẹ̀ GitHub.

## Ìkópa

Wo [CONTRIBUTING.md](../../../CONTRIBUTING.md) fún ìṣàn-iṣẹ́ ìdàgbàsókè àti àwọn ohun tí a nílò fún commit tí a fọwọ́ sí.

## Ìwé-àṣẹ

Iṣẹ́ àkànṣe yìí wà lábẹ́ Ìwé-àṣẹ MIT - wo fáìlì [LICENSE](../../../LICENSE) fún àwọn àlàyé kíkún.

## Òǹkọ̀wé

Thomas Vincent

## Ìdúpẹ́

- [CoinGecko](https://www.coingecko.com/) fún pípèsè API owó kírípítò ọ̀fẹ́
- [Àwọn Ìtọ́sọ́nà Ìdàgbàsókè Àfikún Nagios](https://nagios-plugins.org/doc/guidelines.html)
