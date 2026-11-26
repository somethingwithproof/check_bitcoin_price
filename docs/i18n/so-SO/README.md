# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · **Soomaali** · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Ku-xir Nagios/Icinga ah oo lagula socdo qiimaha Bitcoin iyada oo leh xadad digniin iyo halis ah oo la habayn karo.

## Astaamaha

- La soco qiimaha Bitcoin lacago kala duwan (USD, EUR, GBP, iwm.)
- Xadad digniin iyo halis ah oo la habayn karo (sare iyo hoose)
- Soo-saarka caadiga ah ee ku-xirka Nagios oo wata xogta waxqabadka
- Wuxuu isticmaalaa CoinGecko API (bilaash ah, uma baahna furaha API)
- Taageero loogu talagalay barta API ee gaarka ah
- Waqti-dhammaad la habayn karo
- Hubinta cusboonaanta qiimaha iyada oo la adeegsanayo waqtiga bixiyaha, oo leh xad caadi ah oo hal saac ah
- Isku-dayo celin oo xaddidan marka ay jiraan xadaynta codsiyada ama cilado ku-meel-gaar ah oo API
- Hal waqti-dhammaad oo loogu talagalay dhammaan isku-dayada iyo xad 64 KiB ah jawaab kasta
- Digniino ikhtiyaari ah oo ku saabsan isbeddelka boqolkiiba ee 24-saac ee buuxa
- Xadadka qiimaha, muddada codsiga, iyo da'da qiimaha oo ku jira xogta waxqabadka

## Rakibidda

### Ka soo dejinta GitHub Releases

Ka soo deji faylasha `.deb`, `.rpm`, `.tar.gz`, wheel, iyo `SHA256SUMS` bogga [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Ku xaqiiji soo-dejinta adiga oo adeegsanaya `sha256sum --ignore-missing --check SHA256SUMS`. Sii-daynta ka dambeysa 1.0.0 waxay sidoo kale wataan caddaynta asalka dhismaha ee saxeexan; ku xaqiiji in hantidu ka timid nidaamka sii-daynta ee kaydkan adiga oo adeegsanaya `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Isticmaal magacyada faylasha ee sii-daynta la doortay. Xirmooyinka nidaamku waxay rakibaan `/usr/bin/check_bitcoin_price` iyo `/usr/lib/nagios/plugins/check_bitcoin_price`; xirmada RPM waxay sidoo kale bixisaa `/usr/lib64/nagios/plugins/check_bitcoin_price`. Taliska xirmaysan wuxuu Python ku socodsiiyaa hab go'doonsan, sidaas darteed wuu iska indha-tiraa `PYTHONPATH` iyo qaybaha ku jira galka shaqada; maareeyaha xirmooyinka nidaamku wuxuu xalliyaa ku-tiirsanaanta Python iyo `requests`. Waxay ka kooban yihiin koodh Python ah oo aan ku xirnayn qaab-dhismeedka qalabka, waxayna u baahan yihiin nidaam bixiya Python 3.12 ama ka cusub.

### Ka rakibidda Koodhka Asalka ah

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Loogu talagalay Horumarinta

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Isticmaalka

### Isticmaalka Aasaasiga ah

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Isticmaalka Xadadka

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Xadad Gaar-gaar ah

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Lacag Kale

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Waqti-dhammaad Gaar ah

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Cusboonaanta Xogta iyo Miisaaniyadda Isku-dayga Celinta

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Qiimaha wata waqtiga bixiyaha waa inuu ugu badnaan jiraa hal saac si caadi ah.
Baraha API ee soo celiya qiimaha oo keliya way sii shaqaynayaan marka `--max-age` la maqnaado.
Marka la isticmaalo `--max-age`, waqtiyada bixiyaha ee maqan, aan saxnayn, mustaqbalka ah, ama duugoobay waxay soo celiyaan
`UNKNOWN`; ku-xirku kuma beddelo waqtiga bixiyaha waqtiga qalabka gudaha laga soo qaaday. Waqtiga si sax ah u taagan xadka da'da waa la aqbali karaa. Waqtiyada mustaqbalka ah had iyo jeer waa la diidaa.

Habka caadiga ah wuxuu oggol yahay hal isku-day celin ah. Keliya ciladaha xiriirka, waqti-dhammaadka, iyo jawaabaha HTTP
408/429/500/502/503/504 ayaa dib loogu celinayaa. Sugitaanka dib-u-dhacu wuxuu ka bilowdaa 0.5 ilbiriqsi, wuxuuna laba-laabmaa isku-dayada xiga; ilbiriqsiyada `Retry-After` iyo taariikhaha HTTP ayaa mudnaanta leh. Dhammaan isku-dayada, akhrinta jawaabaha, furfurista JSON, iyo sugitaanka isku-dayga celinta waxay wadaagaan miisaaniyadda `--timeout`. Sugitaan isku-day celin oo aan ku habboonayn miisaaniyadda wuxuu isla markiiba soo celiyaa `UNKNOWN` wuxuuna soo sheegaa ciladdii sababtay, sida `HTTP 429` ama `ConnectionError`, ee ma aha waqti-dhammaad. Ciladaha xaqiijinta aqoonsiga, ciladaha kale ee joogtada ah ee HTTP, JSON aan saxnayn, iyo jawaabaha ka weyn 64 KiB ee xogta la furfuray dib looguma celiyo. Isticmaal `--retries 0` si aad u joojiso isku-dayada celinta.

### Ilaha Kaydka ah ee Qiimaha

Isticmaal ikhtiyaarrada `--fallback-url URL` ee lagu celcelin karo oo leh baraha API ee la jaanqaada CoinGecko.
Tusaale ahaan, ku dar `--fallback-url https://quotes.example.org/simple/price`.
Il kastaa waxay heshaa saami isle'eg oo ka mid ah waqtiga codsiga ee haray, oo ay ku jiraan isku-dayadeeda celinta. Cilad ku-meel-gaar ah ama dib-u-dhac isku-day celin oo ka dheer saamigaas waxay u gudbisaa isha xigta. Ciladaha xaqiijinta TLS, ciladaha joogtada ah ee HTTP iyo qiimayaasha aan saxnayn waxay soo celiyaan UNKNOWN. Jawaab kasta oo qiime ah waxay ku xaddidan tahay 64 KiB oo xog la furfuray ah.
Marka ilaha kaydka ah la habeeyo, xaaladdu waxay tilmaantaa isha ka jawaabtay sida `primary`, `fallback1`, iyo wixii la mid ah, iyada oo aan daabicin URL-keeda.

### Dhaqdhaqaaqa Muddada Gaaban

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Sii isticmaalaha kormeerka gal xaaladeed gaar ah oo wax lagu qori karo oo ku yaal nidaamka faylasha maxalliga ah ee Linux ama macOS. Ku hay faylka `.lock` ee la socda meeshiisa inta u dhaxaysa hubinnada. U isticmaal fayl xaaladeed gaar ah muddo kasta. Lacaguhu waxay ku dhex leeyihiin taariikho madax-bannaan.
Muddada caadiga ah waa 3600 ilbiriqsi. Qiime kasta oo sax ah wuxuu u baahan yahay waqti bixiye oo ku dhex jira muddada iyo xadka da'da, kaas oo ah hal saac haddii aan `--max-age` dejin mid kale. Ku-xirku wuxuu isbarbardhigaa qiimaha hadda jira iyo qiimihii toganaa ee ugu da'da weynaa ee muddadaas ku jiray, wuxuuna soo sheegaa ilbiriqsiyada dhabta ah ee ka soo wareegay. Waqtiyada soo noqnoqda ma abuuraan muunado dheeraad ah.
Muunadda koowaad, taariikhda dhacday, ama JSON kharribmay waxay bilaabaan saldhig cusub; cabbirka muddadu wuxuu ahaanayaa mid aan la aqoon ilaa laga helo muunad la isbarbardhigi karo. Digniinaha kale weli way shaqaynayaan. Xaalad aan wax lagu qori karin, fayl xaaladeed ama quful oo ah xiriiriye calaamad ah (symbolic link), ama qiime ka da' weyn muunaddii ugu dambeysay ee la duubay waxay soo celiyaan UNKNOWN. Cabbirka saxeexan ee `bitcoin_move_window` wuxuu adeegsadaa xadad digniin iyo halis ah oo isku dheellitiran. Sinnaanta ku aaddan xadku ma keento digniin.

Ku-xirku wuxuu furaa galka xaaladda hal mar hubin kasta wuxuuna u shaqeeyaa si ku xiran galkaas, sidaas darteed qayb jid ah oo la beddelay inta hubintu socoto ma weecin karto qufulka, akhrinta, ama qorista. Xiriiriyayaasha calaamadda ah ee ku jira qaybta galka ee jidka waa la raacaa marka hubintu bilaabato, taas oo ka dhigaysa xiriiriyayaasha nidaamka sida `/var` ee macOS kuwo la isticmaali karo. Sidaas darteed galka xaaladda iyo galalka ka sarreeya waa inaanay u furnayn qorista isticmaalayaasha kale. Faylasha xaaladda iyo qufulka waxaa lagu abuuraa ogolaanshaha 0600.

### Dhaqdhaqaaqa Boqolkiiba ee Maalinlaha ah

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Xadadka isbeddelku waxay cabbiraan qiimaha buuxa ee isbeddelka boqolkiiba ee 24-saac ee saxeexan ee CoinGecko ee lacagta la doortay. Isbeddel si sax ah u taagan xadka ma keeno digniin. Haddii labada xadba la bixiyo, digniintu waa inaanay ka badnaan halista.
Xogta isbeddelka ee loo baahan yahay oo maqan ama aan saxnayn waxay soo celisaa `UNKNOWN`. Digniinaha qiimaha iyo isbeddelka waa la isku dari karaa; darajada ugu sarraysa ayaa guulaysata, iyada oo qiimuhu mudnaanta leeyahay marka darajooyinku isku mid yihiin.

## Ikhtiyaarrada Khadka Taliska

| Ikhtiyaar | Sharaxaad |
|--------|-------------|
| `-w`, `--warning` | Xadka digniinta (qaabka: LOW:HIGH) |
| `-c`, `--critical` | Xadka halista (qaabka: LOW:HIGH) |
| `--warning-low` | Xadka digniinta ee qiimaha hoose |
| `--warning-high` | Xadka digniinta ee qiimaha sare |
| `--critical-low` | Xadka halista ee qiimaha hoose |
| `--critical-high` | Xadka halista ee qiimaha sare |
| `--currency` | Koodhka lacagta ee ka kooban 2-16 xaraf ama tiro (caadiga: usd) |
| `--timeout` | Wadarta miisaaniyadda codsiga API iyo isku-dayga celinta ee ilbiriqsiyada, oo ay ku jiraan tirooyinka jajabka ah (caadiga: 10) |
| `--retries` | Isku-dayo dheeraad ah oo ku-meel-gaar ah, 0 ilaa 5 (caadiga: 1) |
| `--max-age` | Da'da ugu badan ee qiimaha bixiyaha ilbiriqsiyo ahaan iyada oo la dalbanayo waqti; qiimayaasha waqtiga leh waxay caadi ahaan yihiin 3600 |
| `--warning-change` | Xadka digniinta ee dhaqdhaqaaqa boqolkiiba ee 24-saac ee buuxa |
| `--critical-change` | Xadka halista ee dhaqdhaqaaqa boqolkiiba ee 24-saac ee buuxa |
| `--api-url` | URL-ka aasaasiga ah ee API |
| `--fallback-url` | Bar API dheeraad ah oo la jaanqaada; ku celi sida loo kala doorbido |
| `--state-file` | Faylka JSON ee taariikhda dhaqdhaqaaqa |
| `--move-window` | Muddada dhaqdhaqaaqa ilbiriqsiyo ahaan (caadiga: 3600) |
| `--warning-move`, `--critical-move` | Xadadka dhaqdhaqaaqa muddada ee buuxa boqolkiiba ahaan |
| `-v`, `--verbose` | Daar soo-saarka faahfaahsan |
| `-V`, `--version` | Muuji nooca |
| `-h`, `--help` | Muuji fariinta caawinta |

## Habaynta Nagios

### Qeexidda Taliska

U deji macro-ga kheyraadka Nagios ee `$USER1$` galka ku-xirrada (xirmooyinka nidaamku waxay isticmaalaan `/usr/lib/nagios/plugins`). Ku dar habaynta talisyada Nagios-kaaga:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Qeexidda Adeegga

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

### Habaynta Icinga2

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

## Koodhadhka Ka-bixidda

Doodaha aan saxnayn, waqti-dhammaadyada aan toganayn, xadadka aan saxnayn, iyo qiimayaasha API ee qaabkoodu qaldan yahay waxay soo celiyaan `UNKNOWN` (ka-bixidda 3). Xadadku waa inay noqdaan tirooyin xaddidan oo aan tabanayn, iyada oo xad kasta oo hoose aanu ka weynayn xadkiisa sare. Lacagtu waa inay ahaataa 2-16 xaraf ama tiro. Habaynta aan saxnayn waxaa la diidaa ka hor inta aan lala xiriirin API. Qiimayaashu waa inay ahaadaan kuwo xaddidan oo aan tabanayn, oo loo bixiyay tirooyin JSON ah ama xarfo tobanle ah oo caadi ah sida `"43521.5"`. Jawaab aan lahayn lacagta la codsaday way magacawdaa, tusaale ahaan `Response has no EUR price`. Jawaabaha aan saxnayn ma soo saaraan xogta waxqabadka. Baaritaannada faahfaahsan waxay aadaan stderr si stdout ugu koobnaado hal sadar oo xaaladda kormeerka ah.

| Koodh | Xaalad | Sharaxaad |
|------|--------|-------------|
| 0 | OK | Qiimuhu wuxuu ku jiraa xadka la aqbali karo |
| 1 | WARNING | Qiimuhu wuxuu dhaafay xadka digniinta |
| 2 | CRITICAL | Qiimuhu wuxuu dhaafay xadka halista |
| 3 | UNKNOWN | Cilad ayaa dhacday (cilad API, waqti-dhammaad, iwm.) |

## Xogta Waxqabadka

Ku-xirku wuxuu soo saaraa xogta waxqabadka qaabka caadiga ah ee Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Xogta waxqabadka qiimaha waxaa ku jira xadadka digniinta iyo halista ee la habeeyay iyo ugu yaraan eber. Xadadka waxaa loo daabacaa qaab tobanle oo buuxa, marna lama soo gaabiyo mana la geliyo qaab jibaar (exponent), si qiimayaasha waaweyn sida `14500000:16250000` ay u ahaadaan kuwo la akhrin karo. Waqtiga codsigu wuxuu ka kooban yahay dhammaan isku-dayada iyo dib-u-dhacyada. Da'da qiimaha waxaa la soo saaraa oo keliya marka bixiyuhu keeno waqti sax ah; isbeddelka maalinlaha ah waxaa la soo saaraa marka la heli karo. Xadadka isbeddelku waxay isku dheellitiran yihiin hareeraha eber. Xogta aan saxnayn ama duugoobay waxay soo saartaa `UNKNOWN` iyada oo aan lahayn xogta waxqabadka qiimaha. Cabbirradan waxaa lagula isticmaali karaa qalabka sawiridda garaafyada sida PNP4Nagios, Grafana, ama InfluxDB.

## API

Ku-xirkani wuxuu si caadi ah u isticmaalaa [CoinGecko API](https://www.coingecko.com/en/api), kaas oo bilaash ah oo aan u baahnayn furaha API. Xadaynta codsiyada way khusaysaa.

Baraha API ee gaarka ah waa inay isticmaalaan qaab jawaab oo isku mid ah: `bitcoin.<currency>` oo loogu talagalay qiimaha, `bitcoin.last_updated_at` oo loogu talagalay ilbiriqsiyada waqtiga UNIX, iyo `bitcoin.<currency>_24h_change` oo loogu talagalay dhaqdhaqaaqa boqolkiiba ee maalinlaha ah ee saxeexan. Keliya qiimaha ayaa loo baahan yahay marka `--max-age` iyo xadadka isbeddelku maqan yihiin. Waqtiga jira weli waa la hubiyaa: waa inaanu noqon mustaqbal ama ka da' weyn hal saac. Jawaabta la furfuray waa inay ku jirtaa 64 KiB.

Lacagaha la taageero waxaa ka mid ah: usd, eur, gbp, jpy, aud, cad, chf, cny, iyo kuwo kale oo badan.

## Amniga

Tallaabooyinka hoose waxaa laga hirgeliyay koodhka hadda jira. Waxay xaddidaan waxa bar API oo si xun u dhaqmaysa ama isticmaale maxalli ah ku samayn karo kombiyuutarka kormeerka; ma hubiyaan in qiimaha laftiisu yahay mid la isku hallayn karo.

- Shahaadooyinka HTTPS waxaa lagu xaqiijiyaa hababka caadiga ah ee `requests`, mana jiro ikhtiyaar joojiya xaqiijinta. Bar `--api-url` gaar ah oo adeegsata `http://` caadi ah ma laha ilaalintaas.
- DNS, xiriirka, akhrinta, isku-dayada celinta, iyo dib-u-dhacyadu waxay wadaagaan waqti-dhammaadka `--timeout`. Qayb xogta si tartiib ah u soo dirta ma dheerayn karto muddadaas.
- Jawaab kastaa waxay ku xaddidan tahay 64 KiB ka dib marka la furfuro, jidhka jawaabaha dib-u-hagiddana (redirect bodies) waa la tuuraa iyada oo aan la akhrin.
- Ciladaha codsigu waxay daabacaan oo keliya xaaladda HTTP ama nooca ciladda, sababtoo ah `--api-url` gaar ah waxaa ku jiri kara aqoonsiyo sir ah.
- Taliska ay rakibaan `.deb` iyo `.rpm` wuxuu Python ku socodsiiyaa hab go'doonsan. Wuu iska indha-tiraa `PYTHONPATH`, galka site-ka isticmaalaha, iyo qaybaha ku jira galka shaqada. Rakibidda `pip` waxay isticmaashaa qoraalka caadiga ah ee console-ka waxayna raacdaa deegaanka lagu rakibay.
- Xaaladda dhaqdhaqaaqa waxaa loo akhriyaa loona qoraa iyada oo aan la raacin xiriiriye calaamad ah oo ku yaal magaca faylka xaaladda ama qufulka, iyada oo loo eegayo gal hal mar la furay hubin kasta.
- Hantida sii-daynta waxay wataan caddaymaha asalka dhismaha marka lagu daro `SHA256SUMS`; eeg [Ka soo dejinta GitHub Releases](#from-github-releases).

## U-cusboonaysiinta laga bilaabo 1.0.0

Isbeddelladan waxay ku jiraan nooca 2.0.0.

- Qiime wata waqti bixiye oo ka da' weyn hal saac wuxuu soo celiyaa `UNKNOWN` haddii aan la siin `--max-age` ka weyn. Baraha aan soo celin waqti waxba ma saamaynayso.
- `--currency` wuxuu aqbalaa oo keliya 2-16 xaraf ama tiro.
- Xarfaha tirooyinka leh kala-saarayaal lambar ama meelo bannaan oo hareeraha ah waa la diidaa.
- Sugitaan isku-day celin oo aan ku jirin miisaaniyadda wuxuu soo sheegaa ciladda hoose halkii uu ka sheegi lahaa `API request timed out`.
- Xirmooyinka nidaamku mar dambe ma tixgeliyaan `PYTHONPATH`.
- Xadadka gaaraya hal milyan ama ka badan waxay xogta waxqabadka uga muuqdaan tirooyin tobanle ah oo caadi ah halkii ay ka ahaan lahaayeen qaab jibaar.

## Deegaamaynta Luqadaha

Caawinta CLI, ciladaha xaqiijinta, iyo sharaxaadda xaaladda ku-xirku waxay taageeraan 45 luqadood (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) iyaga oo adeegsanaya kaydad lagu raray maktabadda caadiga ah (stdlib). Go'aaminta luqaddu waxay hubisaa `--lang`, ka dibna `LC_ALL`, `LC_MESSAGES`, iyo `LANG`, iyada oo ugu dambayn ku laabata `en`. Horgalayaasha xaaladda Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) iyo xogta waxqabadku isma beddelaan dhammaan luqadaha.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Horumarinta

Rakib [mise](https://mise.jdx.dev/getting-started.html), ka dibna socodsii diyaarinta horumarinta ee kor ku xusan. `mise.toml` wuxuu xiraa noocyada Python iyo uv. Qalabka horumarinta waxaa lagu qeexay `pyproject.toml` waxaana lagu xalliyay `uv.lock` ee kaydka ku jira.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Rakib qabsatooyinka commit-ka (commit hooks) ka dib diyaarinta:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Isticmaal `mise exec -- uv add --dev <tool>` ama `mise exec -- uv add <dependency>` si aad u cusboonaysiiso ku-tiirsanaanta oo aad u kaydiso labada fayl ee `pyproject.toml` iyo `uv.lock`.

CI waxay hubisaa Python 3.12 iyo 3.13 ee Linux iyo Python 3.13 ee macOS. PR kasta wuxuu sidoo kale socodsiiyaa xaqiijinta xirmooyinka, baaritaanka ku-tiirsanaanta, iyo CodeQL, wuxuuna ku rakibaa `.deb` Ubuntu iyo `.rpm` Fedora. Xirmooyinka la dhisay waxaa laga heli karaa qaybta `distributions` ee socodsiinta CI.

Nooca xirmada iyo CLI wuxuu ka yimaadaa `check_bitcoin_price/__init__.py`. Eeg [nidaamka sii-daynta](../../../CONTRIBUTING.md#releases) si aad u ogaato kordhinta nooca iyo daabacaadda tooska ah ee hantida sii-daynta GitHub.

## Ka-qaybqaadashada

Eeg [CONTRIBUTING.md](../../../CONTRIBUTING.md) si aad u hesho habka horumarinta iyo shuruudaha commit-yada saxeexan.

## Shatiga

Mashruucan waxaa lagu shatiyeeyay Shatiga MIT - eeg faylka [LICENSE](../../../LICENSE) faahfaahin dheeraad ah.

## Qoraaga

Thomas Vincent

## Mahadcelinta

- [CoinGecko](https://www.coingecko.com/) bixinta API bilaash ah oo loogu talagalay lacagaha dhijitaalka ah
- [Tilmaamaha Horumarinta Ku-xirrada Nagios](https://nagios-plugins.org/doc/guidelines.html)
