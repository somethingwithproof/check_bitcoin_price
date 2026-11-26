# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · **Kinyarwanda** · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Umugereka wa Nagios/Icinga wo gukurikirana igiciro cya Bitcoin ufite imipaka y'imbuzi n'iy'akaga ishobora kugenwa uko ubishaka.

## Ibiranga

- Gukurikirana igiciro cya Bitcoin mu mafaranga atandukanye (USD, EUR, GBP, n'andi)
- Imipaka y'imbuzi n'iy'akaga ishobora kugenwa (hejuru no hasi)
- Ibisubizo bisanzwe by'umugereka wa Nagios birimo amakuru y'imikorere
- Ikoresha CoinGecko API (ubuntu, nta rufunguzo rwa API rukenewe)
- Ishyigikira aderesi za API zihariye
- Igihe ntarengwa cyo gutegereza gishobora kugenwa
- Igenzura ry'ubushya bw'igiciro hifashishijwe ikimenyetso cy'igihe cy'uwatanze amakuru, rifite umupaka usanzwe w'isaha imwe
- Kongera kugerageza kugira umupaka mu gihe hari imipaka y'ubusabe cyangwa amakosa y'agateganyo ya API
- Igihe ntarengwa kimwe ku bigeragezo byose n'umupaka wa 64 KiB kuri buri gisubizo
- Imbuzi zihitamo ku ihinduka ry'ijanisha ry'amasaha 24
- Imipaka y'ibiciro, igihe ubusabe bwamaze, n'igihe igiciro kimaze mu makuru y'imikorere

## Gushyiraho porogaramu

<a name="from-github-releases"></a>

### Uvuye kuri GitHub Releases

Kuramo amadosiye ya `.deb`, `.rpm`, `.tar.gz`, wheel, na `SHA256SUMS` kuri [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Genzura ibyakuwemo ukoresheje `sha256sum --ignore-missing --check SHA256SUMS`. Verisiyo zasohotse nyuma ya 1.0.0 zinafite ibimenyetso byasinywe bigaragaza aho zubakiwe; emeza ko idosiye yavuye mu mikorere yo gusohora verisiyo y'ubu bubiko ukoresheje `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Koresha amazina y'amadosiye ya verisiyo wahisemo. Amapaki asanzwe ya sisitemu ashyiraho `/usr/bin/check_bitcoin_price` na `/usr/lib/nagios/plugins/check_bitcoin_price`; ipaki ya RPM inatanga `/usr/lib64/nagios/plugins/check_bitcoin_price`. Ibwiriza riri mu ipaki ritangiza Python mu buryo bwigenga, ku buryo ryirengagiza `PYTHONPATH` n'ibice (modules) biri mu bubiko burimo gukorerwamo; umuyobozi w'amapaki wa sisitemu akemura ibisabwa bya Python na `requests`. Birimo kode ya Python itashingiye ku bwoko bw'imashini kandi bisaba sisitemu itanga Python 3.12 cyangwa izisumbuyeho.

### Uvuye ku isoko ya kode

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Ku bagenzuzi n'abakora porogaramu

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Imikoreshereze

### Imikoreshereze y'ibanze

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Ukoresheje imipaka

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Imipaka itandukanye

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Irindi faranga

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Igihe ntarengwa cyihariye

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Ubushya bw'amakuru n'umubare wo kongera kugerageza

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Igiciro gifite ikimenyetso cy'igihe cy'uwagitanze kigomba kuba kitarengeje isaha imwe ubusanzwe.
Aderesi za API zitanga igiciro gusa zikomeza gukoreshwa igihe `--max-age` itatanzwe.
Iyo `--max-age` ikoreshejwe, ikimenyetso cy'igihe kibuze, kidahuye, cy'igihe kizaza, cyangwa gishaje gisubiza
`UNKNOWN`; umugereka ntabwo usimbuza igihe cy'uwatanze igiciro igihe cyafatiwe
ku mashini yawe. Ikimenyetso cy'igihe kiri neza ku mupaka w'igihe gikomeza kwemerwa. Ibimenyetso
by'igihe biri imbere mu gihe kizaza bihita byangwa buri gihe.

Ubusanzwe yemera kongera kugerageza inshuro imwe. Amakosa yo guhuzwa n'umuyoboro, kurenza igihe ntarengwa, n'ibisubizo bya HTTP
408/429/500/502/503/504 nibyo byonyine byongerwa kugeragezwa. Igihe cyo gutegereza gitangira ku masegonda 0.5
kikikuba kabiri ku zindi nshuro zikurikiraho; amasegonda ya `Retry-After` n'amatariki ya HTTP bihabwa
agaciro mbere. Ibigeragezo byose, gusoma ibisubizo, guhindura JSON, no gutegereza kongera kugerageza bisangira
igihe ntarengwa cya `--timeout`. Igihe cyo gutegereza kongera kugerageza kitakwira gisubiza `UNKNOWN` ako kanya
kikagaragaza ikosa ryabiteye, nka `HTTP 429` cyangwa `ConnectionError`,
aho kugaragaza kurenza igihe. Amakosa yo kwemeza umwirondoro, andi makosa ahoraho ya HTTP, JSON itari
yo, n'ibisubizo birengeje 64 KiB by'amakuru yasomwe ntibyongerwa kugeragezwa. Koresha
`--retries 0` kugira ngo uhagarike kongera kugerageza.

### Ahandi hantu ho kwisunga h'ibiciro

Koresha amahitamo ashobora gusubirwamo ya `--fallback-url URL` ukoresheje aderesi zihura na CoinGecko.
Urugero, ongeraho `--fallback-url https://quotes.example.org/simple/price`.
Buri soko ihabwa umugabane ungana w'igihe ntarengwa gisigaye cy'ubusabe, harimo
n'inshuro zayo zo kongera kugerageza. Ikosa ry'agateganyo cyangwa igihe cyo gutegereza kongera kugerageza kirenze uwo mugabane bihita bikomereza ku
yindi soko ikurikira. Amakosa yo kugenzura TLS, amakosa ahoraho ya HTTP n'ibiciro bitari byo
bisubiza UNKNOWN. Buri gisubizo cy'igiciro gifite umupaka wa 64 KiB by'amakuru yasomwe.
Iyo amasoko yo kwisunga yagenwe, imiterere igaragaza isoko yashubije nka
`primary`, `fallback1`, n'izindi zikurikira, iterekanye URL yayo.

### Ihinduka mu gihe gito

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Ha umukoresha ukurikirana ububiko bwihariye bwandikwamo ku sisitemu y'amadosiye ya Linux cyangwa
macOS iri ku mashini. Guma usiga idosiye ya `.lock` iri kumwe nayo hagati y'amagenzura. Koresha
idosiye y'imiterere itandukanye kuri buri gihe cyagenwe. Amafaranga atandukanye agira amateka yigenga muri yo.
Igihe rusange ni amasegonda 3600. Buri giciro cyemewe gikeneye ikimenyetso cy'igihe cy'uwagitanze
kiri muri icyo gihe no mu mupaka w'ubushya, ari wo isaha imwe keretse iyo `--max-age` yagennye
ikindi. Umugereka ugereranya igiciro cy'ubu
n'igiciro cya kera cyane cyabanje kirenze zeru muri icyo gihe kandi ukagaragaza
amasegonda nyayo yashize. Ibimenyetso by'igihe bisubirwamo ntibirema ingero nshya.
Urugero rwa mbere, amateka yarangiye igihe, cyangwa JSON yangiritse bitangiza urufatiro rushya;
igipimo cy'igihe kiba kitazwi kugeza habonetse urugero rushobora kugereranywa. Izindi mbuzi zikomeza
gukurikizwa. Idosiye y'imiterere itandikwamo, idosiye y'imiterere cyangwa ya lock iri ku ihuza ry'ikimenyetso (symbolic link), cyangwa igiciro gishaje
kurusha urugero ruheruka kubikwa bisubiza UNKNOWN. Igipimo gifite ikimenyetso cya `bitcoin_move_window`
gikoresha imipaka ingana ku mpande zombi y'imbuzi n'iy'akaga. Kungana neza n'umupaka ntibitanga imbuzi.

Umugereka ufungura ububiko bw'imiterere rimwe kuri buri genzura kandi ugakorera muri bwo, ku buryo
igice cy'inzira gisimbuwe mu gihe cy'igenzura kidashobora kuyobya lock, isoma,
cyangwa iyandika. Amahuza y'ikimenyetso (symbolic links) ari mu gice cy'ububiko bw'inzira akurikizwa iyo
igenzura ritangiye, ibi bituma amahuza ya sisitemu nka `/var` kuri macOS akomeza gukora.
Ububiko bw'imiterere n'ububiko bububanziriza ntibugomba rero kwandikwamo n'abandi
bakoresha. Amadosiye y'imiterere na lock akorwa afite uburenganzira bwa mode 0600.

### Ihinduka ry'ijanisha ry'umunsi

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Imipaka y'ihinduka ipima agaciro nyako k'ihinduka ry'ijanisha ry'amasaha 24 rifite ikimenyetso ritangwa na CoinGecko
mu ifaranga ryahiswemo. Ihinduka riri neza ku mupaka ntiritanga
imbuzi. Niba imipaka yombi itanzwe, uw'imbuzi ntugomba kurenga uw'akaga.
Amakuru y'ihinduka akenewe abuze cyangwa atari yo asubiza `UNKNOWN`. Imbuzi z'igiciro n'iz'ihinduka
zishobora guhuzwa; urwego rukomeye kurusha izindi nirwo rutsinda, aho igiciro gihabwa uburemere mbere
iyo inzego zingana.

## Amahitamo y'umurongo w'amabwiriza

| Ihitamo | Ibisobanuro |
|--------|-------------|
| `-w`, `--warning` | Urutonde rw'umupaka w'imbuzi (imiterere: LOW:HIGH) |
| `-c`, `--critical` | Urutonde rw'umupaka w'akaga (imiterere: LOW:HIGH) |
| `--warning-low` | Umupaka w'imbuzi ku giciro cyo hasi |
| `--warning-high` | Umupaka w'imbuzi ku giciro cyo hejuru |
| `--critical-low` | Umupaka w'akaga ku giciro cyo hasi |
| `--critical-high` | Umupaka w'akaga ku giciro cyo hejuru |
| `--currency` | Kode y'ifaranga igizwe n'inyuguti cyangwa imibare 2-16 (ubusanzwe: usd) |
| `--timeout` | Igihe ntarengwa cyose cy'ubusabe/kongera kugerageza kwa API mu masegonda, harimo n'imibare y'ibice (ubusanzwe: 10) |
| `--retries` | Inshuro z'inyongera zo kongera kugerageza ku makosa y'agateganyo, 0-5 (ubusanzwe: 1) |
| `--max-age` | Igihe ntarengwa cy'ubushya bw'igiciro mu masegonda no gusaba ikimenyetso cy'igihe; ibiciro bifite ikimenyetso cy'igihe bifite ubusanzwe 3600 |
| `--warning-change` | Umupaka w'imbuzi ku ihinduka nyako ry'ijanisha ry'amasaha 24 |
| `--critical-change` | Umupaka w'akaga ku ihinduka nyako ry'ijanisha ry'amasaha 24 |
| `--api-url` | URL y'ibanze ya API |
| `--fallback-url` | Indi aderesi ihuye nayo; isubiremo ukurikije uko uzirutanya |
| `--state-file` | Idosiye ya JSON y'amateka y'ihinduka |
| `--move-window` | Igihe cy'ihinduka mu masegonda (ubusanzwe: 3600) |
| `--warning-move`, `--critical-move` | Imipaka y'ihinduka nyako mu gihe cyagenwe ku ijanisha |
| `-v`, `--verbose` | Kwemeza ibisubizo birambuye |
| `-V`, `--version` | Kwerekana verisiyo |
| `-h`, `--help` | Kwerekana ubutumwa bw'ubufasha |

## Igenamiterere rya Nagios

### Ishyirwaho ry'ibwiriza

Shyira makro y'umutungo wa Nagios `$USER1$` ku bubiko bw'imigereka (amapaki asanzwe akoresha `/usr/lib/nagios/plugins`). Ongeraho mu igenamiterere ry'amabwiriza rya Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Ishyirwaho rya serivisi

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

### Igenamiterere rya Icinga2

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

## Kode zo gusohoka

Ibipimo bitari byo, igihe ntarengwa kitarenze zeru, imipaka itari yo, n'ibiciro bya API
bifite imiterere mibi bisubiza `UNKNOWN` (gusohoka 3). Imipaka igomba kuba imibare irangira kandi itari munsi ya zeru,
aho buri mupaka wo hasi utarenga uwo hejuru. Ifaranga rigomba
kuba inyuguti cyangwa imibare 2-16. Igenamiterere ritari ryo ryangwa mbere yo kuvugana
na API. Ibiciro bigomba kuba imibare irangira kandi itari munsi ya zeru, bitanzwe nk'imibare ya JSON cyangwa inyuguti
zisanzwe z'imibare y'ibice nka `"43521.5"`. Igisubizo kidafite ifaranga ryasabwe
kirivuga mu izina, urugero `Response has no EUR price`. Ibisubizo bitari byo ntibitanga
amakuru y'imikorere. Amakuru arambuye y'isuzuma ajya kuri stderr
kugira ngo stdout igire umurongo umwe gusa w'imiterere y'ikurikirana.

| Kode | Imiterere | Ibisobanuro |
|------|--------|-------------|
| 0 | OK | Igiciro kiri mu rugero rwemewe |
| 1 | WARNING | Igiciro cyarenze umupaka w'imbuzi |
| 2 | CRITICAL | Igiciro cyarenze umupaka w'akaga |
| 3 | UNKNOWN | Habaye ikosa (kunanirwa kwa API, kurenza igihe, n'ibindi) |

## Amakuru y'imikorere

Umugereka utanga amakuru y'imikorere mu miterere isanzwe ya Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Amakuru y'imikorere y'igiciro arimo imipaka y'imbuzi/iy'akaga yagenwe n'urugero
rwo hasi rwa zeru. Imipaka yandikwa mu buryo bwuzuye bw'imibare isanzwe, ntabwo ihindurwa ngo icibwe bugufi
cyangwa ngo yandikwe mu buryo bwa exponent, kugira ngo imibare minini nka `14500000:16250000` ikomeze gusomeka neza. Igihe cy'ubusabe gikubiyemo ibigeragezo byose n'igihe cyo gutegereza. Igihe igiciro kimaze
gitangwa gusa iyo uwatanze amakuru yatanze ikimenyetso cy'igihe cyemewe; ihinduka ry'umunsi ritangwa
iyo rihari. Imipaka y'ihinduka irangana ku mpande zombi za zeru. Amakuru atari yo cyangwa ashaje
atanga `UNKNOWN` nta makuru y'imikorere y'igiciro. Ibi bipimo bishobora gukoreshwa
n'ibikoresho bishushanya imibare nka PNP4Nagios, Grafana, cyangwa InfluxDB.

## API

Uyu mugereka ukoresha [CoinGecko API](https://www.coingecko.com/en/api) ubusanzwe, akaba ari ubuntu kandi ntusaba urufunguzo rwa API. Imipaka y'ubusabe irakurikizwa.

Aderesi za API zihariye zigomba gukoresha imiterere imwe y'igisubizo: `bitcoin.<currency>` ku
giciro, `bitcoin.last_updated_at` ku masegonda ya UNIX timestamp, na
`bitcoin.<currency>_24h_change` ku ihinduka ry'ijanisha ry'umunsi rifite ikimenyetso. Igiciro gusa
nicyo gisabwa iyo `--max-age` n'imipaka y'ihinduka bitatanzwe. Ikimenyetso cy'igihe
gihari gikomeza kugenzurwa: ntigishobora kuba kiri mu gihe kizaza cyangwa ngo kirenze isaha imwe
gishaje. Igisubizo cyasomwe kigomba gukwira muri 64 KiB.

Amafaranga ashyigikiwe arimo: usd, eur, gbp, jpy, aud, cad, chf, cny, n'andi menshi.

## Umutekano

Ingamba ziri hasi aha zashyizwe mu bikorwa muri kode ihari ubu. Zigabanya ibyo aderesi ya API ikora nabi cyangwa umukoresha uri ku mashini yashobora gukora ku
mashini ikurikirana; ntizigira igiciro ubwacyo icyo kwizerwa.

- Ibyemezo bya HTTPS bigenzurwa hakoreshejwe igenamiterere risanzwe rya `requests`, kandi nta hitamo
  rihagarika iri genzura. Aderesi yihariye ya `--api-url` ikoresha `http://` isanzwe nta
  burinzi nk'ubu ifite.
- DNS, guhuza umuyoboro, gusoma, kongera kugerageza, no gutegereza bisangira igihe ntarengwa cya `--timeout`. Uwo
  muvugana wohereza amakuru buhoro ntashobora kongera icyo gihe.
- Buri gisubizo gifite umupaka wa 64 KiB nyuma yo gufungurwa, kandi ibiri mu bisubizo byohereza ahandi
  birajugunywa bitasomwe.
- Amakosa y'ubusabe yerekana gusa imiterere ya HTTP cyangwa ubwoko bw'ikosa, kuko `--api-url`
  yihariye ishobora kuba irimo imyirondoro y'ibanga.
- Ibwiriza rishyirwaho na `.deb` na `.rpm` ritangiza Python mu buryo bwigenga.
  Ryirengagiza `PYTHONPATH`, ububiko bw'umukoresha, n'ibice biri mu bubiko burimo
  gukorerwamo. Gushyiraho ukoresheje `pip` bikoresha inyandiko isanzwe ya console kandi bigakurikiza
  ibidukikije yashyizwemo.
- Imiterere y'ihinduka isomwa ikanandikwa hadakurikijwe ihuza ry'ikimenyetso (symbolic link) ku izina
  ry'idosiye y'imiterere cyangwa iya lock, bijyanye n'ububiko bufungurwa rimwe kuri buri genzura.
- Amadosiye ya verisiyo zisohoka afite ibimenyetso by'aho yubakiwe hiyongereyeho
  `SHA256SUMS`; reba [Uvuye kuri GitHub Releases](#from-github-releases).

## Kuvugurura uvuye kuri 1.0.0

Izi mpinduka zisohoka muri 2.0.0.

- Igiciro gifite ikimenyetso cy'igihe cy'uwagitanze gishaje kurusha isaha imwe gisubiza `UNKNOWN` keretse iyo
  hatanzwe `--max-age` nini. Aderesi zidatanga ikimenyetso cy'igihe ntizibigirwaho ingaruka.
- `--currency` yemera gusa inyuguti cyangwa imibare 2-16.
- Inyuguti z'imibare zifite ibitandukanya imibare cyangwa imyanya irimo ubusa ku mpande zirangwa.
- Igihe cyo gutegereza kongera kugerageza kitakwira mu gihe cyagenwe kigaragaza ikosa nyaryo ryabiteye
  aho kwerekana `API request timed out`.
- Amapaki asanzwe ya sisitemu ntakireba `PYTHONPATH`.
- Imipaka ya miliyoni imwe cyangwa irenga igaragara mu makuru y'imikorere nk'imibare isanzwe
  aho kuba mu buryo bwa exponent.

## Igenandimi

Ubufasha bwa CLI, amakosa yo kugenzura, n'ibisobanuro by'imiterere y'umugereka bishyigikira indimi n'uturere 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) hakoreshejwe katalogi zihari zisomwa na stdlib. Guhitamo ururimi kugenzura `--lang`, hanyuma `LC_ALL`, `LC_MESSAGES`, na `LANG`, bitakunda hagasubirwa kuri `en`. Amagambo abanza y'imiterere ya Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) n'amakuru y'imikorere ntibihinduka mu ndimi zose.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Iterambere

Shyiraho [mise](https://mise.jdx.dev/getting-started.html), hanyuma ukoreshe itegura ry'iterambere riri haruguru. `mise.toml` igenzura verisiyo ya Python na uv. Ibikoresho by'iterambere byanditse muri `pyproject.toml` kandi bigenwa muri `uv.lock` ibitse mu bubiko.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Shyiraho commit hooks nyuma yo gutegura:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Koresha `mise exec -- uv add --dev <tool>` cyangwa `mise exec -- uv add <dependency>` kugira ngo uvugurure ibikenerwa kandi ubike hamwe `pyproject.toml` na `uv.lock`.

CI igenzura Python 3.12 na 3.13 kuri Linux na Python 3.13 kuri macOS. Buri PR inakora igenzura ry'amapaki, isuzuma ry'ibikenerwa, na CodeQL, kandi igashyiraho `.deb` kuri Ubuntu na `.rpm` kuri Fedora. Amapaki yubatswe aboneka nk'igikoresho cya `distributions` mu mikorere ya CI.

Verisiyo y'ipaki na CLI ituruka muri `check_bitcoin_price/__init__.py`. Reba [uburyo bwo gusohora verisiyo](../../../CONTRIBUTING.md#releases) ku bijyanye no kuzamura verisiyo no gutangaza byikora amadosiye ya GitHub release.

## Gutanga umusanzu

Reba [CONTRIBUTING.md](../../../CONTRIBUTING.md) ku mikorere y'iterambere n'ibisabwa kuri commits zisinywe.

## Uruhushya

Uyu mushinga ufite uruhushya rwa MIT License - reba idosiye ya [LICENSE](../../../LICENSE) ku bindi bisobanuro.

## Uwanditse

Thomas Vincent

## Ishimwe

- [CoinGecko](https://www.coingecko.com/) ku gutanga API y'ubuntu y'amafaranga y'ikoranabuhanga
- [Amabwiriza yo gukora imigereka ya Nagios](https://nagios-plugins.org/doc/guidelines.html)
