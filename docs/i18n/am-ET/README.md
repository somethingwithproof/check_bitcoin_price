# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · **አማርኛ** · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

የBitcoin ዋጋን በሚዋቀሩ የማስጠንቀቂያ እና የአስቸኳይ ገደቦች ለመከታተል የሚያገለግል የNagios/Icinga ተሰኪ።

## ባህሪያት

- የBitcoin ዋጋን በተለያዩ ምንዛሬዎች (USD፣ EUR፣ GBP እና ሌሎችም) መከታተል
- የሚዋቀሩ የማስጠንቀቂያ እና የአስቸኳይ ገደቦች (ከፍተኛ እና ዝቅተኛ)
- ከአፈጻጸም ውሂብ ጋር መደበኛ የNagios ተሰኪ ውጤት
- የCoinGecko API ይጠቀማል (ነጻ፣ የAPI ቁልፍ አያስፈልግም)
- ለብጁ የAPI መዳረሻ ነጥቦች ድጋፍ
- የሚዋቀር የጊዜ ገደብ
- የአቅራቢውን የጊዜ ማህተም በመጠቀም የዋጋ ጥቅስ ወቅታዊነትን መፈተሽ፣ በነባሪ የአንድ ሰዓት ገደብ ያለው
- ለፍጥነት ገደቦች እና ለጊዜያዊ የAPI ብልሽቶች የተገደበ ዳግም ሙከራ
- ለሁሉም ሙከራዎች አንድ የጊዜ ገደብ እና ለእያንዳንዱ ምላሽ የ64 KiB ጣሪያ
- በፍጹም የ24 ሰዓት የመቶኛ እንቅስቃሴ ላይ አማራጭ ማንቂያዎች
- የዋጋ ገደቦች፣ የጥያቄ ቆይታ እና የዋጋ ጥቅስ ዕድሜ በአፈጻጸም ውሂብ ውስጥ

## መጫን

### ከGitHub Releases

የ`.deb`፣ `.rpm`፣ `.tar.gz`፣ wheel እና `SHA256SUMS` ፋይሎችን ከ[GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) ያውርዱ። የወረደውን ፋይል በ`sha256sum --ignore-missing --check SHA256SUMS` ያረጋግጡ። ከ1.0.0 በኋላ ያሉ ልቀቶች የተፈረመ የግንባታ ምንጭ ማረጋገጫም ይዘዋል፤ አንድ ፋይል ከዚህ ማከማቻ የልቀት የስራ ሂደት የመጣ መሆኑን በ`gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` ያረጋግጡ።

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

ከተመረጠው ልቀት የተገኙትን የፋይል ስሞች ይጠቀሙ። ቤተኛ ጥቅሎች `/usr/bin/check_bitcoin_price` እና `/usr/lib/nagios/plugins/check_bitcoin_price`ን ይጭናሉ፤ RPM ደግሞ `/usr/lib64/nagios/plugins/check_bitcoin_price`ን ያቀርባል። የታሸገው ትዕዛዝ Pythonን በተነጠለ ሁኔታ ስለሚያስኬድ `PYTHONPATH`ን እና በስራ ማውጫው ውስጥ ያሉ ሞጁሎችን ችላ ይላል፤ የስርዓቱ ጥቅል አስተዳዳሪ የPython እና የ`requests` ጥገኞችን ይፈታል። ከስነ-ህንጻ ነጻ የሆነ የPython ኮድ የያዙ ሲሆን Python 3.12 ወይም ከዚያ በላይ የሚያቀርብ ስርጭት ያስፈልጋቸዋል።

### ከምንጭ ኮድ

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### ለልማት

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## አጠቃቀም

### መሰረታዊ አጠቃቀም

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### ከገደቦች ጋር

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### የተናጠል ገደቦች

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### የተለየ ምንዛሬ

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### ብጁ የጊዜ ገደብ

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### ወቅታዊነት እና የዳግም ሙከራ በጀት

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

የአቅራቢ የጊዜ ማህተም የያዘ የዋጋ ጥቅስ በነባሪ ከአንድ ሰዓት በላይ የቆየ መሆን የለበትም። ዋጋ ብቻ የሚመልሱ የመዳረሻ ነጥቦች `--max-age` ሳይሰጥ ጥቅም ላይ መዋል ይችላሉ። ከ`--max-age` ጋር የጎደሉ፣ ልክ ያልሆኑ፣ የወደፊት ወይም ያረጁ የአቅራቢ የጊዜ ማህተሞች `UNKNOWN` ይመልሳሉ፤ ተሰኪው ለአቅራቢው የዋጋ ጥቅስ ሰዓት ምትክ የአካባቢውን የማምጫ ሰዓት አይተካም። በትክክል በዕድሜ ገደቡ ላይ ያለ የጊዜ ማህተም ተቀባይነት አለው። የወደፊት የጊዜ ማህተሞች ሁልጊዜ ውድቅ ይደረጋሉ።

ነባሪው አንድ ዳግም ሙከራ ይፈቅዳል። የግንኙነት ስህተቶች፣ የጊዜ ማለቂያዎች እና የHTTP 408/429/500/502/503/504 ምላሾች ብቻ በድጋሚ ይሞከራሉ። የመጠበቂያ ጊዜው ከ0.5 ሰከንድ ይጀምርና ለተከታዮቹ ዳግም ሙከራዎች በእጥፍ ይጨምራል፤ የ`Retry-After` ሰከንዶች እና የHTTP ቀናት ቅድሚያ ይሰጣቸዋል። ሁሉም ሙከራዎች፣ የምላሽ ንባቦች፣ የJSON ዲኮዲንግ እና የዳግም ሙከራ መጠበቂያዎች የ`--timeout` በጀቱን ይጋራሉ። በበጀቱ ውስጥ የማይገባ የዳግም ሙከራ መጠበቂያ ወዲያውኑ `UNKNOWN` ይመልሳል እና የጊዜ ማለቂያ ሳይሆን ያስከተለውን ብልሽት፣ ለምሳሌ `HTTP 429` ወይም `ConnectionError`ን ሪፖርት ያደርጋል። የማረጋገጫ ብልሽቶች፣ ሌሎች ቋሚ የHTTP ስህተቶች፣ ልክ ያልሆነ JSON እና ከ64 KiB በላይ ዲኮድ የተደረገ ውሂብ ያላቸው ምላሾች በድጋሚ አይሞከሩም። ዳግም ሙከራዎችን ለማሰናከል `--retries 0`ን ይጠቀሙ።

### ተለዋጭ የዋጋ ጥቅስ ምንጮች

ከCoinGecko ጋር ተኳሃኝ ከሆኑ የመዳረሻ ነጥቦች ጋር ሊደገሙ የሚችሉ `--fallback-url URL` አማራጮችን ይጠቀሙ። ለምሳሌ `--fallback-url https://quotes.example.org/simple/price`ን ያክሉ። እያንዳንዱ ምንጭ ዳግም ሙከራዎቹን ጨምሮ ከቀረው የጥያቄ የጊዜ ገደብ እኩል ድርሻ ያገኛል። ጊዜያዊ ብልሽት ወይም ከዚያ ድርሻ በላይ የሆነ የዳግም ሙከራ መዘግየት ወደ ቀጣዩ ምንጭ ያልፋል። የTLS ማረጋገጫ ብልሽቶች፣ ቋሚ የHTTP ስህተቶች እና ልክ ያልሆኑ የዋጋ ጥቅሶች UNKNOWN ይመልሳሉ። እያንዳንዱ የዋጋ ጥቅስ ምላሽ በ64 KiB ዲኮድ የተደረገ ውሂብ የተገደበ ነው። ተለዋጭ ምንጮች ሲዋቀሩ፣ ሁኔታው ምላሽ የሰጠውን ምንጭ URL ሳያትም እንደ `primary`፣ `fallback1` እና የመሳሰሉት ይለያል።

### የአጭር ጊዜ መስኮት እንቅስቃሴ

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

ለመከታተያ ተጠቃሚው በአካባቢያዊ የLinux ወይም macOS ፋይል ስርዓት ላይ የግል ሊጻፍበት የሚችል የሁኔታ ማውጫ ይስጡት። ተጓዳኝ የሆነውን `.lock` ፋይል በፍተሻዎች መካከል በቦታው ያቆዩት። ለእያንዳንዱ መስኮት የተለየ የሁኔታ ፋይል ይጠቀሙ። ምንዛሬዎች በውስጡ ራሳቸውን የቻሉ ታሪኮች አሏቸው። ነባሪው መስኮት 3600 ሰከንድ ነው። እያንዳንዱ ትክክለኛ የዋጋ ጥቅስ በመስኮቱ እና በዕድሜ ገደቡ ውስጥ ያለ የአቅራቢ የጊዜ ማህተም ያስፈልገዋል፤ ይህም `--max-age` ሌላ ካልወሰነ በስተቀር አንድ ሰዓት ነው። ተሰኪው የአሁኑን ዋጋ በዚያ መስኮት ውስጥ ካለው በጣም ቀደምት አዎንታዊ ዋጋ ጋር ያነጻጽርና ትክክለኛውን ያለፈ ሰከንድ ሪፖርት ያደርጋል። የተደጋገሙ የጊዜ ማህተሞች ተጨማሪ ናሙናዎችን አይፈጥሩም። የመጀመሪያ ናሙና፣ ጊዜው ያለፈበት ታሪክ ወይም የተበላሸ JSON አዲስ መነሻ ይጀምራል፤ የሚነጻጸር ናሙና እስኪኖር ድረስ የመስኮቱ መለኪያ ያልታወቀ ይሆናል። ሌሎች ማንቂያዎች አሁንም ተፈጻሚ ይሆናሉ። ሊጻፍበት የማይችል ሁኔታ፣ የሲምቦሊክ አገናኝ ሁኔታ ወይም መቆለፊያ ፋይል፣ ወይም ከአዲሱ ከተመዘገበው ናሙና በፊት የነበረ የዋጋ ጥቅስ UNKNOWN ይመልሳል። ምልክት ያለው `bitcoin_move_window` መለኪያ ተመሳሳይ የማስጠንቀቂያ እና የአስቸኳይ ክልሎችን ይጠቀማል። በትክክል ከገደቡ ጋር እኩል መሆን ማንቂያ አያስነሳም።

ተሰኪው በእያንዳንዱ ፍተሻ የሁኔታ ማውጫውን አንድ ጊዜ ከፍቶ ከእሱ አንጻር ይሰራል፤ ስለዚህ በፍተሻው ወቅት የተቀየረ የመንገድ ክፍል መቆለፊያውን፣ ንባቡን ወይም ጽሑፉን ወደ ሌላ አቅጣጫ ማዞር አይችልም። በመንገዱ የማውጫ ክፍል ውስጥ ያሉ ሲምቦሊክ አገናኞች ፍተሻው ሲጀምር ይከተላሉ፤ ይህም በmacOS ላይ እንደ `/var` ያሉ የመድረክ አገናኞች ጥቅም ላይ እንዲውሉ ያደርጋል። ስለዚህ የሁኔታ ማውጫው እና የበላይ ማውጫዎቹ በሌሎች ተጠቃሚዎች ሊጻፍባቸው አይገባም። የሁኔታ እና የመቆለፊያ ፋይሎች በ0600 ፈቃድ ይፈጠራሉ።

### ዕለታዊ የመቶኛ እንቅስቃሴ

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

የለውጥ ገደቦች በተመረጠው ምንዛሬ ውስጥ የCoinGeckoን ምልክት ያለው የ24 ሰዓት የመቶኛ ለውጥ ፍጹም ዋጋ ይለካሉ። በትክክል በገደቡ ላይ ያለ ለውጥ ማንቂያ አያስነሳም። ሁለቱም ገደቦች ከተሰጡ ማስጠንቀቂያው ከአስቸኳዩ መብለጥ የለበትም። የሚያስፈልግ የለውጥ ውሂብ ሲጎድል ወይም ልክ ካልሆነ `UNKNOWN` ይመልሳል። የዋጋ እና የለውጥ ማንቂያዎች ሊጣመሩ ይችላሉ፤ ከፍተኛው የክብደት ደረጃ ያሸንፋል፣ የክብደት ደረጃዎቹ እኩል ሲሆኑ ደግሞ ዋጋው ቅድሚያ ይወስዳል።

## የትዕዛዝ መስመር አማራጮች

| አማራጭ | መግለጫ |
|--------|--------|
| `-w`, `--warning` | የማስጠንቀቂያ ገደብ ክልል (ቅርጸት: LOW:HIGH) |
| `-c`, `--critical` | የአስቸኳይ ገደብ ክልል (ቅርጸት: LOW:HIGH) |
| `--warning-low` | ለዝቅተኛ ዋጋ የማስጠንቀቂያ ገደብ |
| `--warning-high` | ለከፍተኛ ዋጋ የማስጠንቀቂያ ገደብ |
| `--critical-low` | ለዝቅተኛ ዋጋ የአስቸኳይ ገደብ |
| `--critical-high` | ለከፍተኛ ዋጋ የአስቸኳይ ገደብ |
| `--currency` | ከ2-16 ፊደላት ወይም አሃዞች ያለው የምንዛሬ ኮድ (ነባሪ: usd) |
| `--timeout` | ክፍልፋይ እሴቶችን ጨምሮ አጠቃላይ የAPI ጥያቄ/ዳግም ሙከራ በጀት በሰከንድ (ነባሪ: 10) |
| `--retries` | ተጨማሪ ጊዜያዊ ሙከራዎች፣ ከ0 እስከ 5 (ነባሪ: 1) |
| `--max-age` | ከፍተኛው የአቅራቢ የዋጋ ጥቅስ ዕድሜ በሰከንድ እና የጊዜ ማህተም መኖርን ያስገድዳል፤ የጊዜ ማህተም ያላቸው ጥቅሶች በነባሪ 3600 ናቸው |
| `--warning-change` | ለፍጹም የ24 ሰዓት የመቶኛ እንቅስቃሴ የማስጠንቀቂያ ገደብ |
| `--critical-change` | ለፍጹም የ24 ሰዓት የመቶኛ እንቅስቃሴ የአስቸኳይ ገደብ |
| `--api-url` | ዋናው የAPI URL |
| `--fallback-url` | ተጨማሪ ተኳሃኝ የመዳረሻ ነጥብ፤ በተመረጠው ቅደም ተከተል ይድገሙት |
| `--state-file` | የJSON እንቅስቃሴ ታሪክ ፋይል |
| `--move-window` | የእንቅስቃሴ መስኮት በሰከንድ (ነባሪ: 3600) |
| `--warning-move`, `--critical-move` | በመቶኛ የፍጹም መስኮት እንቅስቃሴ ገደቦች |
| `-v`, `--verbose` | ዝርዝር ውጤትን አንቃ |
| `-V`, `--version` | ስሪቱን አሳይ |
| `-h`, `--help` | የእገዛ መልዕክቱን አሳይ |

## የNagios ውቅረት

### የትዕዛዝ ትርጓሜ

የNagios ሃብት ማክሮ `$USER1$`ን ወደ ተሰኪው ማውጫ ያቀናብሩ (ቤተኛ ጥቅሎች `/usr/lib/nagios/plugins`ን ይጠቀማሉ)። ወደ የNagios ትዕዛዞች ውቅረትዎ ያክሉ:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### የአገልግሎት ትርጓሜ

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

### የIcinga2 ውቅረት

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

## የመውጫ ኮዶች

ልክ ያልሆኑ መለኪያዎች፣ አዎንታዊ ያልሆኑ የጊዜ ገደቦች፣ ልክ ያልሆኑ የገደብ ክልሎች እና በትክክል ያልተቀረጹ የAPI ዋጋዎች `UNKNOWN` (መውጫ 3) ይመልሳሉ። ገደቦች ውስን እና አሉታዊ ያልሆኑ ቁጥሮች መሆን አለባቸው፤ እያንዳንዱ ዝቅተኛ ገደብም ከከፍተኛው ገደብ መብለጥ የለበትም። ምንዛሬው ከ2-16 ፊደላት ወይም አሃዞች መሆን አለበት። ልክ ያልሆነ ውቅረት APIውን ከማግኘቱ በፊት ውድቅ ይደረጋል። ዋጋዎች ውስን እና አሉታዊ ያልሆኑ ሆነው እንደ JSON ቁጥሮች ወይም እንደ `"43521.5"` ያሉ ቀላል አስርዮሽ ሕብረቁምፊዎች መሰጠት አለባቸው። የተጠየቀው ምንዛሬ የሌለበት ምላሽ ስሙን ይጠቅሳል፣ ለምሳሌ `Response has no EUR price`። ልክ ያልሆኑ ምላሾች የአፈጻጸም ውሂብ አያወጡም። stdout አንድ ነጠላ የክትትል ሁኔታ መስመር እንዲይዝ ዝርዝር የምርመራ መልዕክቶች ወደ stderr ይላካሉ።

| ኮድ | ሁኔታ | መግለጫ |
|-----|-------|--------|
| 0 | OK | ዋጋው ተቀባይነት ባለው ክልል ውስጥ ነው |
| 1 | WARNING | ዋጋው የማስጠንቀቂያ ገደቡን አልፏል |
| 2 | CRITICAL | ዋጋው የአስቸኳይ ገደቡን አልፏል |
| 3 | UNKNOWN | ስህተት ተከስቷል (የAPI ብልሽት፣ የጊዜ ማለቂያ ወዘተ) |

## የአፈጻጸም ውሂብ

ተሰኪው የአፈጻጸም ውሂብን በመደበኛ የNagios ቅርጸት ያወጣል:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

የዋጋ አፈጻጸም ውሂብ የተዋቀሩትን የማስጠንቀቂያ/አስቸኳይ ክልሎች እና የዜሮ ዝቅተኛ ገደብ ያካትታል። እንደ `14500000:16250000` ያሉ ትላልቅ እሴቶች በቀላሉ እንዲተነተኑ ገደቦች በሙሉ አስርዮሽ አጻጻፍ ይታተማሉ፤ በፍጹም አይጠጋጉም ወይም በኤክስፖነንት ቅርጸት አይጻፉም። የጥያቄ ጊዜ ሁሉንም ሙከራዎች እና የመጠበቂያ ጊዜዎችን ያካትታል። የዋጋ ጥቅስ ዕድሜ የሚወጣው አቅራቢው ትክክለኛ የጊዜ ማህተም ሲያቀርብ ብቻ ነው፤ ዕለታዊ ለውጥ ደግሞ ሲገኝ ይወጣል። የለውጥ ክልሎች በዜሮ ዙሪያ ተመሳሳይ ናቸው። ልክ ያልሆነ ወይም ያረጀ ውሂብ ያለ ዋጋ አፈጻጸም ውሂብ `UNKNOWN` ያመነጫል። እነዚህ መለኪያዎች እንደ PNP4Nagios፣ Grafana ወይም InfluxDB ካሉ የግራፍ መሳሪያዎች ጋር ጥቅም ላይ ሊውሉ ይችላሉ።

## API

ይህ ተሰኪ በነባሪ [CoinGecko API](https://www.coingecko.com/en/api)ን ይጠቀማል፤ ይህም ነጻ ሲሆን የAPI ቁልፍ አያስፈልገውም። የፍጥነት ገደቦች ተፈጻሚ ናቸው።

ብጁ የመዳረሻ ነጥቦች ተመሳሳይ የምላሽ ቅርጽ መጠቀም አለባቸው: ለዋጋ `bitcoin.<currency>`፣ ለUNIX የጊዜ ማህተም ሰከንዶች `bitcoin.last_updated_at` እና ለምልክት ያለው ዕለታዊ የመቶኛ እንቅስቃሴ `bitcoin.<currency>_24h_change`። `--max-age` እና የለውጥ ገደቦች በሌሉበት ጊዜ ዋጋ ብቻ ያስፈልጋል። የተካተተ የጊዜ ማህተም አሁንም ይፈተሻል: የወደፊት ወይም ከአንድ ሰዓት በላይ የቆየ መሆን የለበትም። ዲኮድ የተደረገው ምላሽ በ64 KiB ውስጥ መግባት አለበት።

የሚደገፉ ምንዛሬዎች: usd፣ eur፣ gbp፣ jpy፣ aud፣ cad፣ chf፣ cny እና ሌሎች ብዙዎችን ያካትታሉ።

## ደህንነት

ከዚህ በታች ያሉት እርምጃዎች በአሁኑ ኮድ ውስጥ ተተግብረዋል። በአግባቡ የማይሰራ የመዳረሻ ነጥብ ወይም የአካባቢ ተጠቃሚ በክትትል አስተናጋጁ ላይ ሊያደርስ የሚችለውን ይገድባሉ፤ ሆኖም የዋጋ ጥቅሱን ራሱ እምነት የሚጣልበት አያደርጉትም።

- የHTTPS የምስክር ወረቀቶች በ`requests` ነባሪዎች ይረጋገጣሉ፣ እና ማረጋገጫውን የሚያሰናክል ምንም አማራጭ የለም። ቀላል `http://` የሚጠቀም ብጁ `--api-url` እንዲህ ዓይነት ጥበቃ የለውም።
- DNS፣ ግንኙነት፣ ንባቦች፣ ዳግም ሙከራዎች እና የመጠበቂያ ጊዜዎች የ`--timeout` ገደቡን ይጋራሉ። ውሂብን በዝግታ የሚልክ አቻ ጊዜውን ማራዘም አይችልም።
- እያንዳንዱ ምላሽ ከተፈታ በኋላ በ64 KiB የተገደበ ሲሆን፣ የአቅጣጫ መቀየሪያ ምላሽ አካላት ሳይነበቡ ይጣላሉ።
- ብጁ `--api-url` የማረጋገጫ ምስጢሮችን ሊይዝ ስለሚችል የጥያቄ ብልሽቶች የHTTP ሁኔታን ወይም የስህተት ክፍልን ብቻ ያትማሉ።
- በ`.deb` እና `.rpm` የተጫነው ትዕዛዝ Pythonን በተነጠለ ሁኔታ ያስኬዳል። `PYTHONPATH`ን፣ የተጠቃሚውን የሳይት ማውጫ እና በስራ ማውጫው ውስጥ ያሉ ሞጁሎችን ችላ ይላል። የ`pip` መጫኛ መደበኛውን የኮንሶል ስክሪፕት ይጠቀማል እና የተጫነበትን አካባቢ ይከተላል።
- የእንቅስቃሴ ሁኔታ በእያንዳንዱ ፍተሻ አንድ ጊዜ ከተከፈተ ማውጫ አንጻር በሁኔታው ወይም በመቆለፊያ ፋይል ስም ላይ ሲምቦሊክ አገናኝ ሳይከተል ይነበባል እና ይጻፋል።
- የልቀት ፋይሎች ከ`SHA256SUMS` በተጨማሪ የግንባታ ምንጭ ማረጋገጫዎችን ይዘዋል፤ [ከGitHub Releases](#from-github-releases)ን ይመልከቱ።

## ከ1.0.0 ማሻሻል

እነዚህ ለውጦች በ2.0.0 ውስጥ ተካትተዋል።

- ከአንድ ሰዓት በላይ የቆየ የአቅራቢ የጊዜ ማህተም ያለው የዋጋ ጥቅስ ትልቅ `--max-age` ካልተሰጠ በስተቀር `UNKNOWN` ይመልሳል። የጊዜ ማህተም የማይመልሱ የመዳረሻ ነጥቦች አይነኩም።
- `--currency` ከ2-16 ፊደላት ወይም አሃዞችን ብቻ ይቀበላል።
- የአሃዝ መለያዎች ወይም ዙሪያውን ክፍተቶች ያሏቸው የቁጥር ሕብረቁምፊዎች ውድቅ ይደረጋሉ።
- በበጀቱ ውስጥ የማይገባ የዳግም ሙከራ መጠበቂያ ከ`API request timed out` ይልቅ መሰረታዊውን ብልሽት ሪፖርት ያደርጋል።
- ቤተኛ ጥቅሎች ከአሁን በኋላ `PYTHONPATH`ን አያከብሩም።
- አንድ ሚሊዮን ወይም ከዚያ በላይ የሆኑ ገደቦች በአፈጻጸም ውሂብ ውስጥ በኤክስፖነንት አጻጻፍ ሳይሆን እንደ ቀላል አስርዮሽ ይታያሉ።

## የቋንቋ ድጋፍ

የCLI እገዛ፣ የማረጋገጫ ስህተቶች እና የተሰኪ ሁኔታ መግለጫዎች በተካተቱ እና በstdlib በሚጫኑ ካታሎጎች 45 ቋንቋዎችን (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ይደግፋሉ። የቋንቋ አፈታት መጀመሪያ `--lang`ን፣ ቀጥሎ `LC_ALL`፣ `LC_MESSAGES` እና `LANG`ን ይፈትሻል፤ ካልተገኘ ወደ `en` ይመለሳል። የNagios ሁኔታ ቅድመ-ቅጥያዎች (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) እና የአፈጻጸም ውሂብ በሁሉም ቋንቋዎች ሳይለወጡ ይቆያሉ።

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## ልማት

[mise](https://mise.jdx.dev/getting-started.html)ን ይጫኑ፣ ከዚያ ከላይ ያለውን የልማት ማዋቀሪያ ያስኪዱ። `mise.toml` Pythonን እና uvን ያስራል። የልማት መሳሪያዎች በ`pyproject.toml` ውስጥ ተገልጸው በተመዘገበው `uv.lock` ውስጥ ይፈታሉ።

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

ከማዋቀር በኋላ የኮሚት መንጠቆዎችን ይጫኑ:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

ጥገኞችን ለማዘመን `mise exec -- uv add --dev <tool>` ወይም `mise exec -- uv add <dependency>`ን ይጠቀሙ እና ሁለቱንም `pyproject.toml` እና `uv.lock`ን ኮሚት ያድርጉ።

CI በLinux ላይ Python 3.12 እና 3.13ን፣ እንዲሁም በmacOS ላይ Python 3.13ን ይፈትሻል። እያንዳንዱ PR የጥቅል ማረጋገጫ፣ የጥገኝነት ኦዲት እና CodeQLን ያስኬዳል፤ እንዲሁም `.deb`ን በUbuntu ላይ እና `.rpm`ን በFedora ላይ ይጭናል። የተገነቡ ስርጭቶች በCI ሩጫዎች ላይ እንደ `distributions` አርቲፋክት ይገኛሉ።

የጥቅሉ እና የCLI ስሪት ከ`check_bitcoin_price/__init__.py` ይመጣል። ለስሪት ጭማሪዎች እና ለGitHub ልቀት ፋይሎች አውቶማቲክ ህትመት [የልቀት ሂደቱን](../../../CONTRIBUTING.md#releases) ይመልከቱ።

## አስተዋጽኦ ማበርከት

ለልማት የስራ ሂደት እና ለተፈረሙ የኮሚት መስፈርቶች [CONTRIBUTING.md](../../../CONTRIBUTING.md)ን ይመልከቱ።

## ፈቃድ

ይህ ፕሮጀክት በMIT ፈቃድ ስር የተፈቀደ ነው - ለዝርዝሮች የ[LICENSE](../../../LICENSE) ፋይልን ይመልከቱ።

## ደራሲ

Thomas Vincent

## ምስጋና

- ነጻ የክሪፕቶከረንሲ API በማቅረብ [CoinGecko](https://www.coingecko.com/)
- [የNagios ተሰኪዎች ልማት መመሪያዎች](https://nagios-plugins.org/doc/guidelines.html)
