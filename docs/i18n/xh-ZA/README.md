# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · **isiXhosa** · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Iplagini ye-Nagios/Icinga yokubeka iliso kwixabiso le-Bitcoin enemida yesilumkiso neyobuzaza enokuqwalaselwa.

## Iimpawu

- Beka iliso kwixabiso le-Bitcoin kwiimali ezininzi (USD, EUR, GBP, njl.njl.)
- Imida yesilumkiso neyobuzaza enokuqwalaselwa (ephezulu nesezantsi)
- Iziphumo eziqhelekileyo zeplagini ye-Nagios ezinedatha yokusebenza
- Isebenzisa i-CoinGecko API (isimahla, akukho sitshixo se-API sifunekayo)
- Inkxaso yee-endpoint ze-API zokuzikhethela
- Ixesha lokulinda elinokuqwalaselwa
- Ukuhlolwa kokutsha kwamaxabiso kusetyenziswa izitempu zexesha zomthengisi, ngomda ongagqibekanga weyure enye
- Iinzame eziphindaphindiweyo ezinomda kwimida yesantya kunye nokusilela kwethutyana kwe-API
- Umda omnye wexesha kuzo zonke iinzame kunye nomda we-64 KiB kwimpendulo nganye
- Izilumkiso zokuzikhethela kwintshukumo epheleleyo yepesenti kwiiyure ezingama-24
- Imida yexabiso, ubude bexesha lesicelo, kunye nobudala bexabiso elinikiweyo kwidatha yokusebenza

## Ufakelo

### Ukusuka kwi-GitHub Releases

Khuphela iifayile ze-`.deb`, `.rpm`, `.tar.gz`, i-wheel, kunye ne-`SHA256SUMS` ukusuka kwi-[GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Qinisekisa ukhuphelo nge-`sha256sum --ignore-missing --check SHA256SUMS`. Iinguqulelo ezikhutshwe emva kwe-1.0.0 zikwanobungqina bemvelaphi yokwakhiwa obusayiniweyo; qinisekisa ukuba ifayile ivela kwinkqubo yokukhupha yale repository nge-`gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Sebenzisa amagama eefayile ukusuka kwinguqulelo ekhethiweyo. Iipakethe zemveli zifaka i-`/usr/bin/check_bitcoin_price` kunye ne-`/usr/lib/nagios/plugins/check_bitcoin_price`; i-RPM ikwabonelela nge-`/usr/lib64/nagios/plugins/check_bitcoin_price`. Umyalelo opakishiweyo usebenzisa i-Python kwimowudi eyodwa, ngoko ke awuyihoyi i-`PYTHONPATH` kunye neemodyuli ezikwisilawuli esisebenzayo; umphathi weepakethe wenkqubo usombulula izixhomekeko ze-Python kunye ne-`requests`. Ziqulethe ikhowudi ye-Python engaxhomekekanga kuyilo lwezixhobo kwaye zifuna unikezelo olubonelela nge-Python 3.12 okanye entsha.

### Ukusuka kwiKhowudi yoMthombo

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Ukwenzela uPhuhliso

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Usetyenziso

### Usetyenziso oluSisiseko

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Ngemida

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Imida eyodwa

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Imali eyahlukileyo

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Ixesha lokuLinda lokuzikhethela

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Ukutsha kweXabiso kunye noHlahlo-lwabiwo lweeNzame eziPhindaphindiweyo

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Ixabiso elinikiweyo elinesitempu sexesha somthengisi kufuneka lingadluli kwiyure enye ngokungagqibekanga.
Ii-endpoint ezibuyisa ixabiso kuphela zihlala zisebenziseka xa i-`--max-age` ingekho.
Nge-`--max-age`, izitempu zexesha zomthengisi ezingekhoyo, ezingasebenziyo, zexesha elizayo, okanye ezindala zibuyisa
u-`UNKNOWN`; iplagini ayithathi ixesha lokulanda lasekhaya ilisebenzise endaweni yexesha lexabiso
lomthengisi. Isitempu sexesha esisemdeni ngqo wobudala sihlala samkelekile. Izitempu zexesha
zexesha elizayo zisoloko zikhatywa.

Okungagqibekanga kuvumela ukuzama kwakhona kanye. Ziimpazamo zokudibanisa, ukuphelelwa lixesha, kunye neempendulo ze-HTTP
408/429/500/502/503/504 kuphela ezizamwa kwakhona. Ixesha lokulinda phakathi kweenzame liqala nge-0.5 yesekhondi kwaye
liphindaphindeke kabini kwiinzame ezilandelayo; imizuzwana ye-`Retry-After` kunye nemihla ye-HTTP zithatha
indawo yokuqala. Zonke iinzame, ukufundwa kweempendulo, ukuguqulela i-JSON, kunye nokulinda kokuzama kwakhona zabelana
ngohlahlo-lwabiwo lwe-`--timeout`. Ukulinda kokuzama kwakhona okungangeniyo kweli xesha kubuyisa u-`UNKNOWN` ngoko nangoko
kwaye kuxele ukusilela okukubangeleyo, njenge-`HTTP 429` okanye `ConnectionError`,
hayi ukuphelelwa lixesha. Ukusilela kokungqinisiswa, ezinye iimpazamo ze-HTTP ezisisigxina, i-JSON engasebenziyo,
kunye neempendulo ezinkulu kune-64 KiB zedatha eguqulelweyo azizamwa kwakhona. Sebenzisa
u-`--retries 0` ukucima ukuzama kwakhona.

### Imithombo yamaxabiso yokungena endaweni (fallback)

Sebenzisa iinketho eziphindaphindekayo ze-`--fallback-url URL` ezinee-endpoint ezihambelana ne-CoinGecko.
Umzekelo, yongeza u-`--fallback-url https://quotes.example.org/simple/price`.
Umthombo ngamnye ufumana isabelo esilinganayo sexesha eliseleyo lomda wesicelo, kubandakanya neenzame
zawo eziphindaphindiweyo. Ukusilela kwethutyana okanye ulibaziseko lokuzama kwakhona olude kuneso sabelo ludlulela
kumthombo olandelayo. Ukusilela kokuqinisekiswa kwe-TLS, iimpazamo ze-HTTP ezisisigxina, kunye namaxabiso
angasebenziyo kubuyisa u-UNKNOWN. Impendulo nganye yexabiso ilinganiselwe kwi-64 KiB yedatha eguqulelweyo.
Xa imithombo yokungena endaweni iqwalaselwe, imo ichonga umthombo ophendulayo njenge-`primary`,
`fallback1`, njalo njalo, ngaphandle kokushicilela i-URL yawo.

### Intshukumo yexabiso kwithuba elifutshane

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Nika umsebenzisi wokubeka iliso isilawuli semo sabucala esibhalekayo kwisixokelelwano seefayile sasekhaya se-Linux okanye
se-macOS. Gcina ifayile ehlobene nayo ye-`.lock` isendaweni yayo phakathi kovavanyo ngalunye. Sebenzisa
ifayile yemo eyahlukileyo ngethuba ngalinye. Iimali zineembali ezizimeleyo ngaphakathi kuyo.
Ithuba elingagqibekanga yimizuzwana engama-3600. Ixabiso ngalinye elisebenzayo lifuna isitempu sexesha somthengisi
esingaphakathi kwelo thuba nakumda wobudala, oyiyure enye ngaphandle kokuba i-`--max-age` imisele
omnye. Iplagini ithelekisa ixabiso
langoku nelona xabiso lidala langaphambili elingaphezulu kweqanda kwelo thuba kwaye ixele
imizuzwana yangempela edlulileyo. Izitempu zexesha eziphindaphindiweyo azidali iisampulu ezongezelelweyo.
Isampulu yokuqala, imbali ephelelwe lixesha, okanye i-JSON eyonakeleyo iqala isiseko esitsha;
imetrikhi yethuba ayaziwa de kubekho isampulu enokuthelekiswa. Ezinye izilumkiso zisasebenza.
Imo engabhalekiyo, ifayile yemo okanye ye-lock eyi-symbolic link, okanye ixabiso elidala
kunesampulu entsha erekhodiweyo kubuyisa u-UNKNOWN. Imetrikhi enophawu ye-`bitcoin_move_window`
isebenzisa imida yesilumkiso neyobuzaza elinganayo macala omabini. Ukulingana nomda akuvelisi silumkiso.

Iplagini ivula isilawuli semo kanye ngovavanyo ngalunye kwaye isebenza ngokunxulumene naso, ngoko ke
inxalenye yendlela etshintshwe ngexesha lovavanyo ayinakuthumela kwelinye icala i-lock, ukufunda,
okanye ukubhala. Ii-symbolic link ezikwinxalenye yesilawuli yendlela ziyalandelwa xa
uvavanyo luqala, nto leyo egcina amakhonkco eqonga afana ne-`/var` kwi-macOS esebenziseka.
Ngoko ke isilawuli semo kunye nezilawuli eziphezulu zaso akufuneki zibhaleke ngabanye
abasebenzisi. Iifayile zemo neze-lock zidalwa ngemowudi engu-0600.

### Intshukumo yePesenti yeMihla ngeMihla

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Imida yotshintsho ilinganisa ixabiso elipheleleyo lotshintsho lwepesenti enophawu lweeyure ezingama-24
lwe-CoinGecko ngemali ekhethiweyo. Utshintsho olusemdeni ngqo aluvelisi
silumkiso. Ukuba yomibini imida inikiwe, isilumkiso akufuneki sidlule kubuzaza.
Idatha yotshintsho efunekayo engekho okanye engasebenziyo ibuyisa u-`UNKNOWN`. Izilumkiso zexabiso nezotshintsho
zingadityaniswa; obona buzaza buphezulu buyaphumelela, ixabiso lithatha indawo yokuqala
xa ubuzaza bulingana.

## Iinketho zoMgca woMyalelo

| Ukhetho | Inkcazelo |
|--------|-------------|
| `-w`, `--warning` | Uluhlu lomda wesilumkiso (ifomathi: LOW:HIGH) |
| `-c`, `--critical` | Uluhlu lomda wobuzaza (ifomathi: LOW:HIGH) |
| `--warning-low` | Umda wesilumkiso wexabiso eliphantsi |
| `--warning-high` | Umda wesilumkiso wexabiso eliphezulu |
| `--critical-low` | Umda wobuzaza wexabiso eliphantsi |
| `--critical-high` | Umda wobuzaza wexabiso eliphezulu |
| `--currency` | Ikhowudi yemali yoonobumba okanye amanani ama-2-16 (okungagqibekanga: usd) |
| `--timeout` | Uhlahlo-lwabiwo lilonke lwexesha lesicelo/lokuzama kwakhona lwe-API ngemizuzwana, kubandakanya amanani anamaqhezu (okungagqibekanga: 10) |
| `--retries` | Iinzame ezongezelelweyo zethutyana, 0-5 (okungagqibekanga: 1) |
| `--max-age` | Owona budala buninzi bexabiso lomthengisi ngemizuzwana kwaye bufune isitempu sexesha; amaxabiso anezitempu zexesha asebenzisa ama-3600 ngokungagqibekanga |
| `--warning-change` | Umda wesilumkiso kwintshukumo epheleleyo yepesenti yeeyure ezingama-24 |
| `--critical-change` | Umda wobuzaza kwintshukumo epheleleyo yepesenti yeeyure ezingama-24 |
| `--api-url` | I-URL ye-API eyintloko |
| `--fallback-url` | Enye i-endpoint ehambelanayo; phindaphinda ngolandelelwano olukhethiweyo |
| `--state-file` | Ifayile ye-JSON yembali yentshukumo |
| `--move-window` | Ithuba lentshukumo ngemizuzwana (okungagqibekanga: 3600) |
| `--warning-move`, `--critical-move` | Imida yentshukumo epheleleyo yethuba ngepesenti |
| `-v`, `--verbose` | Vula iziphumo ezinabileyo |
| `-V`, `--version` | Bonisa inguqulelo |
| `-h`, `--help` | Bonisa umyalezo woncedo |

## Uqwalaselo lwe-Nagios

### Inkcazelo yoMyalelo

Seta imakro yezibonelelo ze-Nagios u-`$USER1$` kwisilawuli seeplagini (iipakethe zemveli zisebenzisa i-`/usr/lib/nagios/plugins`). Yongeza kuqwalaselo lwakho lwemiyalelo ye-Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Inkcazelo yeNkonzo

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

### Uqwalaselo lwe-Icinga2

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

## Iikhowudi zokuPhuma

Ii-argument ezingasebenziyo, amaxesha okulinda angekho ngaphezu kweqanda, uluhlu lwemida olungasebenziyo, kunye namaxabiso
e-API angaqhelekanga kubuyisa u-`UNKNOWN` (ukuphuma 3). Imida kufuneka ibe ngamanani anesiphelo, angekho ngaphantsi
kweqanda, apho umda ngamnye osezantsi ungadluliyo kumda wawo ophezulu. Imali kufuneka
ibe ngoonobumba okanye amanani ama-2-16. Uqwalaselo olungasebenziyo luyakhatywa phambi kokudibana
ne-API. Amaxabiso kufuneka abe nesiphelo kwaye angabi ngaphantsi kweqanda, anikwe njengamanani e-JSON okanye imicu
yedesimali eqhelekileyo efana no-`"43521.5"`. Impendulo engenayo imali eceliweyo
iyayixela, umzekelo `Response has no EUR price`. Iimpendulo ezingasebenziyo azikhuphi
datha yokusebenza. Ukuxilonga okunabileyo kuya kwi-stderr
ukuze i-stdout ibe nomgca omnye wemo yokubeka iliso.

| Ikhowudi | Imo | Inkcazelo |
|------|--------|-------------|
| 0 | OK | Ixabiso lingaphakathi koluhlu olwamkelekileyo |
| 1 | WARNING | Ixabiso lidlule umda wesilumkiso |
| 2 | CRITICAL | Ixabiso lidlule umda wobuzaza |
| 3 | UNKNOWN | Kwenzeke impazamo (ukusilela kwe-API, ukuphelelwa lixesha, njl.njl.) |

## Idatha yokuSebenza

Iplagini ikhupha idatha yokusebenza kwifomathi eqhelekileyo ye-Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Idatha yokusebenza yexabiso ibandakanya uluhlu lwemida yesilumkiso/yobuzaza oluqwalaselweyo kunye
nobuncinci beqanda. Imida ishicilelwa ngenotheyishini epheleleyo yedesimali, ingaze isondezwe
okanye ibe kwifom ye-exponent, ukuze amaxabiso amakhulu afana no-`14500000:16250000` ahlale efundeka. Ixesha lesicelo libandakanya zonke iinzame kunye nexesha lokulinda phakathi kwazo. Ubudala bexabiso elinikiweyo
bukhutshwa kuphela xa umthengisi ebonelela ngesitempu sexesha esisebenzayo; utshintsho lwemihla ngemihla lukhutshwa
xa lukhona. Uluhlu lotshintsho lulingana macala omabini ukusuka eqandeni. Idatha engasebenziyo okanye endala
ivelisa u-`UNKNOWN` ngaphandle kwedatha yokusebenza yexabiso. Ezi metrikhi zingasetyenziswa
nezixhobo zokwenza iigrafu ezifana ne-PNP4Nagios, i-Grafana, okanye i-InfluxDB.

## I-API

Le plagini isebenzisa i-[CoinGecko API](https://www.coingecko.com/en/api) ngokungagqibekanga, esimahla kwaye engafuni sitshixo se-API. Imida yesantya iyasebenza.

Ii-endpoint zokuzikhethela kufuneka zisebenzise ubume bempendulo obufanayo: `bitcoin.<currency>`
kwixabiso, `bitcoin.last_updated_at` kwimizuzwana yesitempu sexesha se-UNIX, kunye ne-`bitcoin.<currency>_24h_change` kwintshukumo yepesenti enophawu yemihla ngemihla. Lixabiso kuphela
elifunekayo xa i-`--max-age` kunye nemida yotshintsho zingekho. Isitempu sexesha
esikhoyo sisahlolwa: akufuneki sibe sesexesha elizayo okanye sidlule kwiyure enye
ubudala. Impendulo eguqulelweyo kufuneka ingene kwi-64 KiB.

Iimali ezixhaswayo zibandakanya: usd, eur, gbp, jpy, aud, cad, chf, cny, nezinye ezininzi.

## Ukhuseleko

Amanyathelo angezantsi aphunyezwe kwikhowudi yangoku. Anciphisa oko kunokwenziwa yi-endpoint engaziphathanga kakuhle okanye umsebenzisi wasekhaya
kwihost yokubeka iliso; akenzi xabiso ngokwalo lithembeke.

- Izatifikethi ze-HTTPS ziqinisekiswa ngeesetingi ezingagqibekanga ze-`requests`, kwaye akukho lukhetho
  lucima uqinisekiso. I-`--api-url` yokuzikhethela esebenzisa i-`http://` eqhelekileyo ayinalo
  olu khuseleko.
- I-DNS, udibaniso, ukufunda, ukuzama kwakhona, kunye nexesha lokulinda phakathi kweenzame zabelana ngomda wexesha we-`--timeout`.
  Iqabane elithumela idatha kancinci alinakuwulula.
- Impendulo nganye ilinganiselwe kwi-64 KiB emva kokukhululwa koxinzelelo, kwaye imizimba yeempendulo zokuthumela kwenye indawo
  ilahlwa ingafundwanga.
- Ukusilela kwesicelo kushicilela kuphela imo ye-HTTP okanye iklasi yempazamo, kuba i-`--api-url`
  yokuzikhethela inokuqulatha iziqinisekiso zokungena.
- Umyalelo ofakwe yi-`.deb` kunye ne-`.rpm` usebenzisa i-Python kwimowudi eyodwa.
  Awuyihoyi i-`PYTHONPATH`, isilawuli sesayithi somsebenzisi, kunye neemodyuli ezikwisilawuli esisebenzayo.
  Ufakelo lwe-`pip` lusebenzisa iskripthi sekhonsoli esiqhelekileyo kwaye lulandela
  indawo olufakwe kuyo.
- Imo yentshukumo ifundwa kwaye ibhalwe ngaphandle kokulandela i-symbolic link kwigama
  lefayile yemo okanye ye-lock, ngokunxulumene nesilawuli esivulwe kanye ngovavanyo ngalunye.
- Iifayile zenguqulelo ziqulethe iziqinisekiso zemvelaphi yokwakhiwa ukongeza
  kwi-`SHA256SUMS`; jonga [Ukusuka kwi-GitHub Releases](#from-github-releases).

## Ukuphucula ukusuka ku-1.0.0

Olu tshintsho luza kwi-2.0.0.

- Ixabiso elinesitempu sexesha somthengisi esidala kuneyure enye libuyisa u-`UNKNOWN` ngaphandle kokuba
  kunikwe i-`--max-age` enkulu. Ii-endpoint ezingabuyisi sitempu sexesha azichaphazeleki.
- I-`--currency` yamkela oonobumba okanye amanani ama-2-16 kuphela.
- Imicu yamanani enabahluli bamanani okanye izithuba ezijikelezileyo iyaliwa.
- Ukulinda kokuzama kwakhona okungangeniyo kuhlahlo-lwabiwo kuxela ukusilela okuyintloko
  endaweni ye-`API request timed out`.
- Iipakethe zemveli azisayihloniphi i-`PYTHONPATH`.
- Imida yesigidi esinye okanye ngaphezulu ivela kwidatha yokusebenza njengamanani edesimali
  aqhelekileyo endaweni yenotheyishini ye-exponent.

## Iilwimi noGuqulelo

Uncedo lwe-CLI, iimpazamo zokuqinisekisa, kunye neenkcazelo zemo yeplagini zixhasa iilwimi ezingama-45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) kusetyenziswa iikhathalogu ezifakwe ngaphakathi ezilayishwa nge-stdlib. Ukukhethwa kolwimi kuhlolisisa u-`--lang`, emva koko u-`LC_ALL`, `LC_MESSAGES`, kunye no-`LANG`, kubuyele ku-`en` xa zingekho. Iziqalo zemo ze-Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) kunye nedatha yokusebenza zihlala zingatshintshanga kuzo zonke iilwimi.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Uphuhliso

Faka i-[mise](https://mise.jdx.dev/getting-started.html), emva koko usebenzise ucwangciso lophuhliso olungentla. I-`mise.toml` igxininisa iinguqulelo ze-Python kunye ne-uv. Izixhobo zophuhliso zichazwe kwi-`pyproject.toml` kwaye zisombululwe kwi-`uv.lock` efakwe kwi-commit.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Faka ii-commit hook emva kocwangciso:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Sebenzisa i-`mise exec -- uv add --dev <tool>` okanye i-`mise exec -- uv add <dependency>` ukuhlaziya izixhomekeko kwaye ufake zombini i-`pyproject.toml` ne-`uv.lock` kwi-commit.

I-CI ihlola i-Python 3.12 ne-3.13 kwi-Linux kunye ne-Python 3.13 kwi-macOS. Yonke i-PR iphinda iqhube uqinisekiso lweepakethe, uphicotho lwezixhomekeko, kunye ne-CodeQL, kwaye ifake i-`.deb` kwi-Ubuntu kunye ne-`.rpm` kwi-Fedora. Iinguqulelo ezakhiweyo zifumaneka njenge-artifact ye-`distributions` kwimisebenzi ye-CI.

Inguqulelo yepakethe neye-CLI ivela kwi-`check_bitcoin_price/__init__.py`. Jonga [inkqubo yokukhupha iinguqulelo](../../../CONTRIBUTING.md#releases) ukufumana ukunyuswa kwenguqulelo kunye nokupapashwa ngokuzenzekelayo kweefayile zenguqulelo ye-GitHub.

## Ukufaka iGalelo

Jonga i-[CONTRIBUTING.md](../../../CONTRIBUTING.md) ngomsebenzi wophuhliso kunye neemfuno zee-commit ezisayiniweyo.

## Ilayisensi

Le projekthi inelayisensi phantsi kwe-MIT License - jonga ifayile ye-[LICENSE](../../../LICENSE) ngeenkcukacha.

## Umbhali

Thomas Vincent

## Imibulelo

- [CoinGecko](https://www.coingecko.com/) ngokubonelela nge-API ye-cryptocurrency yasimahla
- [Izikhokelo zoPhuhliso lweePlagini ze-Nagios](https://nagios-plugins.org/doc/guidelines.html)
