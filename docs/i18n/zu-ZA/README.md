# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · **isiZulu**

</details>

I-plugin ye-Nagios/Icinga yokuqapha intengo ye-Bitcoin enemikhawulo yezexwayiso neyokubucayi engalungiselelwa.

## Izici

- Qapha intengo ye-Bitcoin ngezimali eziningi (USD, EUR, GBP, njll.)
- Imikhawulo yezexwayiso neyokubucayi engalungiselelwa (ephezulu nephansi)
- Umphumela ojwayelekile we-plugin ye-Nagios onedatha yokusebenza
- Isebenzisa i-CoinGecko API (mahhala, akudingeki ukhiye we-API)
- Ukusekelwa kwamaphoyinti okugcina e-API enziwe ngokwezifiso
- Isikhathi sokuphela esingalungiselelwa
- Ukuhlola ubusha benani usebenzisa izitembu zesikhathi zomthengisi, ngomkhawulo ojwayelekile wehora elilodwa
- Ukuzama kabusha okunomkhawulo kwemingcele yezinga nokwehluleka kwesikhashana kwe-API
- Umnqamulajuqu owodwa wayo yonke imizamo kanye nomkhawulo we-64 KiB emphendulweni ngayinye
- Izaziso ozikhethela zona ekunyakazeni kwephesenti kwamahora angu-24 (inani eliphelele)
- Imikhawulo yentengo, ubude besikhathi sesicelo, kanye nobudala benani kudatha yokusebenza

## Ukufakwa

### Kusuka ku-GitHub Releases

Landa amafayela e-`.deb`, `.rpm`, `.tar.gz`, wheel, kanye ne-`SHA256SUMS` kusuka ku-[GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Qinisekisa okulandiwe nge-`sha256sum --ignore-missing --check SHA256SUMS`. Ukukhishwa ngemva kuka-1.0.0 nakho kunobufakazi bokwakhiwa obusayiniwe; qinisekisa ukuthi ifayela livela ekuhambeni komsebenzi kokukhishwa kwale ndawo yokugcina nge-`gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Sebenzisa amagama amafayela asuka ekukhishweni okukhethiwe. Amaphakheji omthonyama afaka i-`/usr/bin/check_bitcoin_price` kanye ne-`/usr/lib/nagios/plugins/check_bitcoin_price`; i-RPM futhi ihlinzeka nge-`/usr/lib64/nagios/plugins/check_bitcoin_price`. Umyalo ofakiwe usebenzisa i-Python kumodi ehlukanisiwe, ngakho awunaki i-`PYTHONPATH` kanye namamojula asenkambeni yokusebenza; umphathi wephakheji wesistimu uxazulula ukuncika kwe-Python kanye ne-`requests`. Aqukethe ikhodi ye-Python enganciki ekwakhiweni kwesistimu futhi adinga ukusatshalaliswa okuhlinzeka nge-Python 3.12 noma entsha.

### Kusuka kukhodi yomthombo

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Okokuthuthukisa

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Ukusetshenziswa

### Ukusetshenziswa okuyisisekelo

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Ngemikhawulo

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Imikhawulo ngayinye

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Imali ehlukile

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Isikhathi sokuphela esenziwe ngokwezifiso

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Ubusha nesabelo sokuzama kabusha

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Inani elinesitembu sesikhathi somthengisi kumele lingabi lidala ngaphezu kwehora elilodwa ngokuzenzakalelayo.
Amaphoyinti okugcina abuyisa intengo kuphela ahlala esebenziseka uma i-`--max-age` ingekho.
Nge-`--max-age`, izitembu zesikhathi zomthengisi ezingekho, ezingavumelekile, zesikhathi esizayo, noma ezindala zibuyisa
i-`UNKNOWN`; i-plugin ayishintshi isikhathi sokulanda sendawo sibe isikhathi senani
somthengisi. Isitembu sesikhathi esisemkhawulweni wobudala ncamashi sihlala samukeleka. Izitembu zesikhathi
zesikhathi esizayo ziyaliwa njalo.

Okuzenzakalelayo kuvumela ukuzama kabusha kanye. Amaphutha okuxhumana, ukuphela kwesikhathi, kanye nezimpendulo
ze-HTTP 408/429/500/502/503/504 kuphela okuzanywa kabusha. Ukuhlehla kuqala emasekhondini angu-0.5 bese
kuphindeka kabili ekuzameni kabusha okulandelayo; amasekhondi e-`Retry-After` nezinsuku ze-HTTP kuyabekwa
phambili. Yonke imizamo, ukufundwa kwezimpendulo, ukuqaqwa kwe-JSON, kanye nokulinda ukuzama kabusha kuhlanganyela
isabelo se-`--timeout`. Ukulinda kokuzama kabusha okungenakungena kubuyisa i-`UNKNOWN` ngokushesha
futhi kubike ukwehluleka okukubangele, njenge-`HTTP 429` noma i-`ConnectionError`,
hhayi ukuphela kwesikhathi. Ukwehluleka kokuqinisekisa ubuwena, amanye amaphutha angunaphakade e-HTTP, i-JSON
engavumelekile, kanye nezimpendulo ezinkulu kune-64 KiB yedatha eqaqiwe akuzanywa kabusha. Sebenzisa
i-`--retries 0` ukuze ukhubaze ukuzama kabusha.

### Imithombo yamanani eyisipele

Sebenzisa izinketho eziphindaphindekayo ze-`--fallback-url URL` ngamaphoyinti okugcina ahambisana ne-CoinGecko.
Isibonelo, engeza i-`--fallback-url https://quotes.example.org/simple/price`.
Umthombo ngamunye uthola isabelo esilinganayo somnqamulajuqu wesicelo osele, kuhlanganise nokuzama kwawo
kabusha. Ukwehluleka kwesikhashana noma ukubambezeleka kokuzama kabusha okude kunaleso sabelo kudlulela
emthonjeni olandelayo. Ukwehluleka kokuqinisekiswa kwe-TLS, amaphutha angunaphakade e-HTTP namanani
angavumelekile kubuyisa i-UNKNOWN. Impendulo ngayinye yenani inomkhawulo we-64 KiB yedatha eqaqiwe.
Uma izipele zilungiselelwe, isimo sikhomba umthombo ophendulayo njenge-
`primary`, `fallback1`, njalo njalo, ngaphandle kokuphrinta i-URL yawo.

### Ukunyakaza kwesikhathi esifushane

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Nikeza umsebenzisi oqaphayo umkhombandlela wesimo oyimfihlo obhalekayo kusistimu yamafayela yasendaweni ye-Linux noma
ye-macOS. Gcina ifayela elihambisanayo le-`.lock` lisendaweni yalo phakathi kokuhlola. Sebenzisa ifayela lesimo
elihlukile ngewindi ngalinye. Izimali zinemilando ezimele ngaphakathi kwalo.
Iwindi elizenzakalelayo lingamasekhondi angu-3600. Inani ngalinye elivumelekile lidinga isitembu sesikhathi somthengisi
esingaphakathi kwewindi nomkhawulo wobudala, okuyihora elilodwa ngaphandle uma i-`--max-age` ibeka
okunye. I-plugin iqhathanisa intengo yamanje
nentengo endala yangaphambilini engaphezu kweqanda kulelo windi bese ibika amasekhondi angempela
adlulile. Izitembu zesikhathi eziphindaphindwayo azidali amasampula engeziwe.
Isampula yokuqala, umlando ophelelwe yisikhathi, noma i-JSON eyonakele kuqala isisekelo esisha;
imethrikhi yewindi ayaziwa kuze kube khona isampula eqhathanisekayo. Ezinye izaziso zisasebenza.
Isimo esingabhaleki, isixhumanisi esingokomfanekiso sesimo noma ifayela lokukhiya, noma inani elidala
kunesampula entsha erekhodiwe kubuyisa i-UNKNOWN. Imethrikhi esayiniwe ye-`bitcoin_move_window`
isebenzisa izigaba zezexwayiso nezezimo ezibucayi ezilinganayo. Ukulingana emkhawulweni akukhiphi isaziso.

I-plugin ivula umkhombandlela wesimo kanye ngokuhlola ngakunye futhi isebenza ngokuqondene nawo, ukuze
ingxenye yendlela eshintshwe ngesikhathi sokuhlola ingakwazi ukuqondisa kabusha ukukhiya, ukufunda,
noma ukubhala. Izixhumanisi ezingokomfanekiso engxenyeni yomkhombandlela yendlela ziyalandelwa lapho
ukuhlola kuqala, okugcina izixhumanisi zesikhulumi ezifana ne-`/var` ku-macOS zisebenziseka.
Umkhombandlela wesimo nemikhombandlela engaphezulu kwawo ngakho-ke akufanele ibhaleke kwabanye
abasebenzisi. Amafayela esimo nawokukhiya adalwa ngemodi engu-0600.

### Ukunyakaza kwephesenti lwansuku zonke

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Imikhawulo yoshintsho ilinganisa inani eliphelele loshintsho lwephesenti lwamahora angu-24 olusayiniwe
lwe-CoinGecko ngemali ekhethiwe. Ushintsho olusemkhawulweni ncamashi alukhiphi
isaziso. Uma yomibili imikhawulo ihlinzekiwe, isexwayiso akufanele sidlule okubucayi.
Idatha yoshintsho edingekayo engekho noma engavumelekile ibuyisa i-`UNKNOWN`. Izaziso zentengo nezoshintsho
zingahlanganiswa; ubucayi obuphezulu kakhulu buyawina, lapho intengo iba phambili
uma ubucayi bufana.

## Izinketho zomugqa womyalo

| Inketho | Incazelo |
|--------|-------------|
| `-w`, `--warning` | Ibanga lomkhawulo wesexwayiso (ifomethi: LOW:HIGH) |
| `-c`, `--critical` | Ibanga lomkhawulo obucayi (ifomethi: LOW:HIGH) |
| `--warning-low` | Umkhawulo wesexwayiso wentengo ephansi |
| `--warning-high` | Umkhawulo wesexwayiso wentengo ephezulu |
| `--critical-low` | Umkhawulo obucayi wentengo ephansi |
| `--critical-high` | Umkhawulo obucayi wentengo ephezulu |
| `--currency` | Ikhodi yemali enezinhlamvu noma izinombolo ezingu-2-16 (okuzenzakalelayo: usd) |
| `--timeout` | Isabelo sesikhathi esiphelele sesicelo/ukuzama kabusha kwe-API ngamasekhondi, kuhlanganise namanani anamafrakshini (okuzenzakalelayo: 10) |
| `--retries` | Imizamo eyengeziwe yesikhashana, 0–5 (okuzenzakalelayo: 1) |
| `--max-age` | Ubudala obukhulu benani lomthengisi ngamasekhondi futhi kudinga isitembu sesikhathi; amanani anesitembu sesikhathi azenzakalela ku-3600 |
| `--warning-change` | Umkhawulo wesexwayiso wokunyakaza kwephesenti kwamahora angu-24 (inani eliphelele) |
| `--critical-change` | Umkhawulo obucayi wokunyakaza kwephesenti kwamahora angu-24 (inani eliphelele) |
| `--api-url` | I-URL ye-API eyinhloko |
| `--fallback-url` | Iphoyinti lokugcina elengeziwe elihambisanayo; phinda ngokulandelana okuthandwayo |
| `--state-file` | Ifayela lomlando wokunyakaza le-JSON |
| `--move-window` | Iwindi lokunyakaza ngamasekhondi (okuzenzakalelayo: 3600) |
| `--warning-move`, `--critical-move` | Imikhawulo yokunyakaza kwewindi ngamaphesenti (inani eliphelele) |
| `-v`, `--verbose` | Nika amandla umphumela onemininingwane |
| `-V`, `--version` | Bonisa inguqulo |
| `-h`, `--help` | Bonisa umlayezo wosizo |

## Ukumiswa kwe-Nagios

### Incazelo yomyalo

Setha imakhro yesinsiza ye-Nagios `$USER1$` kumkhombandlela we-plugin (amaphakheji omthonyama asebenzisa i-`/usr/lib/nagios/plugins`). Engeza ekumisweni kwemiyalo yakho ye-Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Incazelo yesevisi

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

### Ukumiswa kwe-Icinga2

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

## Amakhodi okuphuma

Ama-argument angavumelekile, izikhathi zokuphela ezingekho ngaphezu kweqanda, amabanga emikhawulo angavumelekile, kanye nezintengo
ze-API ezakhiwe kabi kubuyisa i-`UNKNOWN` (ukuphuma ngo-3). Imikhawulo kumele ibe izinombolo ezinomkhawulo, ezingekho ngaphansi kweqanda,
lapho umkhawulo ngamunye ophansi ungadluli umkhawulo wawo ophezulu. Imali kumele
ibe nezinhlamvu noma izinombolo ezingu-2-16. Ukumiswa okungavumelekile kuyaliwa ngaphambi kokuxhumana
ne-API. Izintengo kumele zibe nomkhawulo futhi zingabi ngaphansi kweqanda, zinikezwe njengezinombolo ze-JSON noma izintambo
zamadesimali ezilula njenge-`"43521.5"`. Impendulo engenayo imali eceliwe
iyayisho, isibonelo `Response has no EUR price`. Izimpendulo ezingavumelekile azikhiphi
idatha yokusebenza. Ukuhlola okunemininingwane kuya ku-stderr
ukuze i-stdout iqukathe umugqa owodwa wesimo sokuqapha.

| Ikhodi | Isimo | Incazelo |
|------|--------|-------------|
| 0 | OK | Intengo ingaphakathi kwebanga elamukelekayo |
| 1 | WARNING | Intengo yeqe umkhawulo wesexwayiso |
| 2 | CRITICAL | Intengo yeqe umkhawulo obucayi |
| 3 | UNKNOWN | Kwenzeke iphutha (ukwehluleka kwe-API, ukuphela kwesikhathi, njll.) |

## Idatha yokusebenza

I-plugin ikhipha idatha yokusebenza ngefomethi ejwayelekile ye-Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Idatha yokusebenza yentengo ihlanganisa amabanga esexwayiso/okubucayi alungiselelwe kanye
nobuncane obuyiqanda. Imikhawulo iphrintwa ngokubhalwa okugcwele kwamadesimali, ayilokothi isondezwe
noma ibe sefomini le-exponent, ukuze amanani amakhulu njenge-`14500000:16250000` ahlale ehlaziyeka. Isikhathi sesicelo sihlanganisa yonke imizamo nokuhlehla. Ubudala benani
bukhishwa kuphela lapho umthengisi ehlinzeka ngesitembu sesikhathi esivumelekile; ushintsho lwansuku zonke lukhishwa
uma lutholakala. Amabanga oshintsho alingana nhlangothi zombili kweqanda. Idatha engavumelekile noma endala
ikhiqiza i-`UNKNOWN` ngaphandle kwedatha yokusebenza yentengo. Lawa mamethrikhi angasetshenziswa
ngamathuluzi okudweba amagrafu afana ne-PNP4Nagios, Grafana, noma i-InfluxDB.

## I-API

Le plugin isebenzisa i-[CoinGecko API](https://www.coingecko.com/en/api) ngokuzenzakalelayo, emahhala futhi engadingi ukhiye we-API. Imingcele yezinga iyasebenza.

Amaphoyinti okugcina enziwe ngokwezifiso kumele asebenzise isimo sempendulo esifanayo: `bitcoin.<currency>` ngentengo,
`bitcoin.last_updated_at` ngamasekhondi esitembu sesikhathi se-UNIX, kanye ne-
`bitcoin.<currency>_24h_change` ngokunyakaza kwephesenti lwansuku zonke okusayiniwe. Intengo kuphela
edingekayo uma i-`--max-age` kanye nemikhawulo yoshintsho kungekho. Isitembu sesikhathi
esikhona sisahlolwa: akufanele sibe esesikhathi esizayo noma sidlule ihora elilodwa
ubudala. Impendulo eqaqiwe kumele ingene ku-64 KiB.

Izimali ezisekelwayo zihlanganisa: usd, eur, gbp, jpy, aud, cad, chf, cny, nezinye eziningi.

## Ukuphepha

Izinyathelo ezingezansi zisetshenziswe kukhodi yamanje. Zikhawulela lokho iphoyinti lokugcina elingaziphathi kahle noma umsebenzisi wendawo angakwenza
kuseva eqaphayo; azenzi inani ngokwalo lithembeke.

- Izitifiketi ze-HTTPS ziqinisekiswa ngokuzenzakalelayo kwe-`requests`, futhi ayikho inketho
  ekhubaza ukuqinisekiswa. I-`--api-url` eyenziwe ngokwezifiso esebenzisa i-`http://` elula ayinakho
  ukuvikelwa okunjalo.
- I-DNS, ukuxhumana, ukufunda, ukuzama kabusha, nokuhlehla kuhlanganyela umnqamulajuqu we-`--timeout`.
  Uhlangothi oluxhunyiwe oluthumela idatha kancane alukwazi ukuwunweba.
- Impendulo ngayinye inomkhawulo we-64 KiB ngemva kokukhipha ukucindezelwa, futhi imizimba yokuqondisa kabusha
  ilahlwa ingafundiwe.
- Ukwehluleka kwezicelo kuphrinta kuphela isimo se-HTTP noma ikilasi lephutha, ngoba i-`--api-url`
  eyenziwe ngokwezifiso ingaqukatha iziqinisekiso.
- Umyalo ofakwe yi-`.deb` ne-`.rpm` usebenzisa i-Python kumodi ehlukanisiwe.
  Awunaki i-`PYTHONPATH`, umkhombandlela wesayithi womsebenzisi, namamojula asenkambeni
  yokusebenza. Ukufakwa kwe-`pip` kusebenzisa iskripthi sekhonsoli esijwayelekile futhi kulandela
  indawo okufakwe kuyo.
- Isimo sokunyakaza sifundwa futhi sibhalwe ngaphandle kokulandela isixhumanisi esingokomfanekiso egameni
  lefayela lesimo noma lokukhiya, ngokuqondene nomkhombandlela ovulwa kanye ngokuhlola ngakunye.
- Amafa okukhishwa athwala iziqinisekiso zobufakazi bokwakhiwa ngaphezu kwe-
  `SHA256SUMS`; bheka [Kusuka ku-GitHub Releases](#from-github-releases).

## Ukuthuthukiswa kusuka ku-1.0.0

Lezi zinguquko ziza ku-2.0.0.

- Inani elinesitembu sesikhathi somthengisi esidlule ihora elilodwa ubudala libuyisa i-`UNKNOWN` ngaphandle uma
  kunikezwe i-`--max-age` enkulu. Amaphoyinti okugcina angabuyisi isitembu sesikhathi awathinteki.
- I-`--currency` yamukela izinhlamvu noma izinombolo ezingu-2-16 kuphela.
- Izintambo zezinombolo ezinabahlukanisi bamadijithi noma izikhala ezizungezile ziyaliwa.
- Ukulinda kokuzama kabusha okungangeni esabelweni kubika ukwehluleka okuyisisekelo
  esikhundleni se-`API request timed out`.
- Amaphakheji omthonyama awasayihloniphi i-`PYTHONPATH`.
- Imikhawulo yesigidi esisodwa noma ngaphezulu ivela kudatha yokusebenza njengamadesimali
  alula esikhundleni sokubhalwa kwe-exponent.

## Ukwenza kube okwendawo

Usizo lwe-CLI, amaphutha okuqinisekisa, kanye nezincazelo zesimo ze-plugin kusekela izilimi ezingu-45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) kusetshenziswa amakhathalogi ahlanganiswe alayishwa nge-stdlib. Ukuxazululwa kuhlola i-`--lang`, bese kuba yi-`LC_ALL`, `LC_MESSAGES`, kanye ne-`LANG`, kubuyele emuva ku-`en`. Iziqalo zesimo ze-Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) kanye nedatha yokusebenza kuhlala kungashintshile kuzo zonke izilimi.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Ukuthuthukisa

Faka i-[mise](https://mise.jdx.dev/getting-started.html), bese usebenzisa ukumiswa kokuthuthukisa okungenhla. I-`mise.toml` ikhiya i-Python ne-uv. Amathuluzi okuthuthukisa amenyezelwa ku-`pyproject.toml` futhi axazululwa ku-`uv.lock` efakwe ku-commit.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Faka ama-commit hook ngemva kokumiswa:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Sebenzisa i-`mise exec -- uv add --dev <tool>` noma i-`mise exec -- uv add <dependency>` ukuze ubuyekeze ukuncika bese ufaka ku-commit kokubili i-`pyproject.toml` ne-`uv.lock`.

I-CI ihlola i-Python 3.12 ne-3.13 ku-Linux kanye ne-Python 3.13 ku-macOS. I-PR ngayinye futhi isebenzisa ukuqinisekiswa kwephakeji, ukuhlolwa kokuncika, ne-CodeQL, futhi ifaka i-`.deb` ku-Ubuntu ne-`.rpm` ku-Fedora. Ukusatshalaliswa okwakhiwe kuyatholakala njenge-artifact ye-`distributions` ekugijimeni kwe-CI.

Inguqulo yephakeji neye-CLI ivela ku-`check_bitcoin_price/__init__.py`. Bheka [inqubo yokukhishwa](../../../CONTRIBUTING.md#releases) ngokwenyuswa kwenguqulo nokushicilelwa okuzenzakalelayo kwamafa okukhishwa kwe-GitHub.

## Ukufaka isandla

Bheka i-[CONTRIBUTING.md](../../../CONTRIBUTING.md) ngokuhamba komsebenzi kokuthuthukisa kanye nezidingo zama-commit asayiniwe.

## Ilayisensi

Le phrojekthi inelayisensi ngaphansi kwe-MIT License - bheka ifayela le-[LICENSE](../../../LICENSE) ngemininingwane.

## Umbhali

Thomas Vincent

## Ukubonga

- I-[CoinGecko](https://www.coingecko.com/) ngokuhlinzeka nge-API yemali yedijithali yamahhala
- [Imihlahlandlela Yokuthuthukisa Ama-plugin e-Nagios](https://nagios-plugins.org/doc/guidelines.html)
