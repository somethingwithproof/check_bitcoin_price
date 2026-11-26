# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (28 locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [Bosanski](../bs/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Hrvatski](../hr/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · **Српски** · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Nagios/Icinga додатак за праћење цене Биткоина са подесивим праговима упозорења и критичног стања.

## Могућности

- Праћење цене Биткоина у више валута (USD, EUR, GBP итд.)
- Подесиви прагови упозорења и критичног стања (горњи и доњи)
- Стандардни испис Nagios додатка са подацима о перформансама
- Користи CoinGecko API (бесплатан, без потребе за API кључем)
- Подршка за прилагођене крајње тачке API-ја
- Подесиво временско ограничење
- Провере свежине котација помоћу временских ознака добављача, са подразумеваним ограничењем од једног сата
- Ограничени поновни покушаји за ограничења броја захтева и привремене грешке API-ја
- Јединствени рок за све покушаје и ограничење од 64 KiB за сваки одговор
- Опциона упозорења на апсолутно 24-часовно процентуално кретање
- Прагови цене, трајање захтева и старост котације у подацима о перформансама

## Инсталација

### Са GitHub Releases

Преузмите датотеке `.deb`, `.rpm`, `.tar.gz`, wheel и `SHA256SUMS` са [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Проверите преузету датотеку командом `sha256sum --ignore-missing --check SHA256SUMS`. Издања после верзије 1.0.0 садрже и потписане доказе порекла изградње; потврдите да ресурс потиче из радног тока издања овог репозиторијума командом `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Користите називе датотека из изабраног издања. Изворни пакети инсталирају `/usr/bin/check_bitcoin_price` и `/usr/lib/nagios/plugins/check_bitcoin_price`; RPM пакет додатно пружа `/usr/lib64/nagios/plugins/check_bitcoin_price`. Упакована команда покреће Python у изолованом режиму, па игнорише `PYTHONPATH` и модуле у радном директоријуму; системски менаџер пакета решава зависности за Python и `requests`. Пакети садрже Python код независан од архитектуре и захтевају дистрибуцију која пружа Python 3.12 или новији.

### Из изворног кода

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### За развој

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Употреба

### Основна употреба

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Са праговима

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Појединачни прагови

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Друга валута

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Прилагођено временско ограничење

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Свежина котације и буџет поновних покушаја

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Котација која носи временску ознаку добављача подразумевано сме бити стара највише један сат.
Крајње тачке које враћају само цену остају употребљиве када `--max-age` и `--state-file` нису задати.
Уз `--max-age`, недостајуће, неважеће, будуће или застареле временске ознаке добављача враћају `UNKNOWN`; додатак не замењује време котације добављача локалним временом преузимања. Временска ознака тачно на граници старости остаје прихватљива. Будуће временске ознаке се увек одбијају.

Подразумевано је дозвољен један поновни покушај. Понављају се само грешке мрежне везе, истеци времена и HTTP одговори 408/429/500/502/503/504. Чекање почиње од 0.5 секунди и удвостручује се за наредне покушаје; секунде из заглавља `Retry-After` и HTTP датуми имају предност. Сви покушаји, читање одговора, декодирање JSON-а и чекања између покушаја деле буџет `--timeout`. Чекање за поновни покушај које не може да стане у буџет одмах враћа `UNKNOWN` и у извештају наводи грешку која га је изазвала, као што је `HTTP 429` или `ConnectionError`, а не истек времена. Грешке аутентификације, друге трајне HTTP грешке, неважећи JSON и одговори већи од 64 KiB декодираних података се не понављају. Користите `--retries 0` да искључите поновне покушаје.

### Резервни извори котација

Користите поновљиве опције `--fallback-url URL` са крајњим тачкама компатибилним са CoinGecko API-јем.
На пример, додајте `--fallback-url https://quotes.example.org/simple/price`.
Сваки сервер добија једнак део преосталог рока захтева, укључујући своје поновне покушаје. Привремена грешка или кашњење поновног покушаја дуже од тог дела прелази на следећи извор. Грешке TLS провере, трајне HTTP грешке и неважеће котације враћају UNKNOWN. Сваки одговор са котацијом ограничен је на 64 KiB декодираних података. Када су резервни извори подешени, статус означава извор који је одговорио као `primary`, `fallback1` итд., без исписивања његовог URL-а.

### Кретање у кратком прозору

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Обезбедите кориснику за надзор приватни директоријум стања са правом писања на локалном Linux или macOS систему датотека. Задржите пратећу `.lock` датотеку на истом месту између провера. Користите засебну датотеку стања за сваки прозор. Валуте унутар ње имају независне историје. Подразумевани прозор износи 3600 секунди. Свака важећа котација мора имати временску ознаку добављача унутар прозора и границе старости, која износи један сат осим ако `--max-age` не задаје другу вредност. Додатак пореди тренутну цену са најстаријом ранијом позитивном ценом у том прозору и пријављује стварно протекле секунде. Поновљене временске ознаке не стварају додатне узорке. Први узорак, истекла историја или оштећен JSON започињу нову почетну вредност; метрика прозора остаје непозната док не постоји упоредив узорак. Остала упозорења и даље важе. Стање у које није могуће писати, симболичка веза уместо датотеке стања или закључавања, или котација старија од најновијег забележеног узорка враћају UNKNOWN. Предзначена метрика `bitcoin_move_window` користи симетричне опсеге упозорења и критичног стања. Једнакост на граници не покреће упозорење.

Додатак отвара директоријум стања једном по провери и ради релативно у односу на њега, тако да компонента путање замењена током провере не може преусмерити закључавање, читање нити писање. Симболичке везе у делу путање који представља директоријум прате се на почетку провере, чиме системске везе попут `/var` на macOS рачунару остају употребљиве. Директоријум стања и његови надређени директоријуми зато не смеју бити доступни за писање другим корисницима. Датотеке стања и закључавања креирају се са дозволама 0600.

### Дневно процентуално кретање

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Прагови промене мере апсолутну вредност CoinGecko предзначене 24-часовне процентуалне промене у изабраној валути. Промена тачно на прагу не покреће упозорење. Ако су наведена оба прага, упозорење не сме премашити критични праг. Недостајући или неважећи обавезни подаци о промени враћају `UNKNOWN`. Упозорења за цену и промену могу се комбиновати; побеђује највиши ниво озбиљности, при чему цена има предност када су нивои једнаки.

## Опције командне линије

| Опција | Опис |
|--------|-------------|
| `-w`, `--warning` | Опсег прагова упозорења (формат: LOW:HIGH) |
| `-c`, `--critical` | Опсег критичних прагова (формат: LOW:HIGH) |
| `--warning-low` | Праг упозорења за ниску цену |
| `--warning-high` | Праг упозорења за високу цену |
| `--critical-low` | Критични праг за ниску цену |
| `--critical-high` | Критични праг за високу цену |
| `--currency` | Код валуте од 2-16 слова или цифара (подразумевано: usd) |
| `--timeout` | Укупни буџет за API захтеве и поновне покушаје у секундама, укључујући децималне вредности (подразумевано: 10) |
| `--retries` | Додатни покушаји код привремених грешака, 0-5 (подразумевано: 1) |
| `--max-age` | Максимална старост котације добављача у секундама уз обавезну временску ознаку; котације са ознаком подразумевано имају 3600 |
| `--warning-change` | Граница упозорења за апсолутно 24-часовно процентуално кретање |
| `--critical-change` | Критична граница за апсолутно 24-часовно процентуално кретање |
| `--api-url` | Примарни URL API-ја |
| `--fallback-url` | Додатна компатибилна крајња тачка; понављајте жељеним редоследом |
| `--state-file` | JSON датотека историје кретања |
| `--move-window` | Прозор кретања у секундама (подразумевано: 3600) |
| `--warning-move`, `--critical-move` | Апсолутни прагови кретања у прозору у процентима |
| `-v`, `--verbose` | Омогући детаљан испис |
| `-V`, `--version` | Прикажи верзију |
| `-h`, `--help` | Прикажи поруку помоћи |

## Подешавања за Nagios

### Дефиниција команде

Поставите Nagios ресурсни макро `$USER1$` на директоријум додатака (изворни пакети користе `/usr/lib/nagios/plugins`). Додајте у ваша Nagios подешавања команди:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Дефиниција сервиса

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

### Подешавања за Icinga2

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

## Излазни кодови

Неважећи аргументи, непозитивна временска ограничења, неважећи опсези прагова и погрешно обликоване цене са API-ја враћају `UNKNOWN` (излаз 3). Прагови морају бити коначни, ненегативни бројеви, при чему свака доња граница не сме бити већа од горње границе. Валута мора имати 2-16 слова или цифара. Неважећа подешавања конфигурације одбијају се пре контактирања API-ја. Цене морају бити коначне и ненегативне, задате као JSON бројеви или обични децимални низови знакова као што је `"43521.5"`. Одговор без тражене валуте наводи њен назив, на пример `Response has no EUR price`. Неважећи одговори не исписују податке о перформансама. Детаљна дијагностика шаље се на stderr тако да stdout садржи један ред статуса надзора.

| Код | Статус | Опис |
|------|--------|-------------|
| 0 | OK | Цена је унутар прихватљивог опсега |
| 1 | WARNING | Цена је прешла праг упозорења |
| 2 | CRITICAL | Цена је прешла критични праг |
| 3 | UNKNOWN | Дошло је до грешке (грешка API-ја, истек времена итд.) |

## Подаци о перформансама

Додатак исписује податке о перформансама у стандардном Nagios формату:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Подаци о перформансама за цену обухватају подешене опсеге упозорења/критичног стања и минимум нула. Прагови се исписују у пуном децималном запису, никада заокружени нити у експоненцијалном облику, тако да велике вредности попут `14500000:16250000` остају погодне за рашчлањивање. Време захтева обухвата све покушаје и чекања. Старост котације исписује се само када добављач достави важећу временску ознаку; дневна промена исписује се када је доступна. Опсези промене симетрични су око нуле. Неважећи или застарели подаци дају `UNKNOWN` без података о перформансама цене. Ове метрике могу се користити са алатима за цртање графикона као што су PNP4Nagios, Grafana или InfluxDB.

## API

Овај додатак подразумевано користи [CoinGecko API](https://www.coingecko.com/en/api), који је бесплатан и не захтева API кључ. Примењују се ограничења броја захтева.

Прилагођене крајње тачке морају користити исти облик одговора: `bitcoin.<currency>` за цену, `bitcoin.last_updated_at` за секунде UNIX временске ознаке и `bitcoin.<currency>_24h_change` за предзначено дневно процентуално кретање. Само цена је обавезна када `--max-age`, `--state-file` и прагови промене нису наведени. Присутна временска ознака се ипак проверава: не сме бити у будућности нити старија од једног сата. Декодирани одговор мора да стане у 64 KiB.

Подржане валуте укључују: usd, eur, gbp, jpy, aud, cad, chf, cny и многе друге.

## Безбедност

Мере наведене у наставку примењене су у тренутном коду. Оне ограничавају шта неисправна крајња тачка или локални корисник могу учинити рачунару за надзор; саме по себи не чине котацију поузданом.

- HTTPS сертификати проверавају се подразумеваним подешавањима библиотеке `requests`, и ниједна опција не искључује проверу. Прилагођени `--api-url` који користи обични `http://` нема такву заштиту.
- DNS, мрежна веза, читања, поновни покушаји и чекања деле рок `--timeout`. Сервер који споро шаље податке не може да га продужи.
- Сваки одговор ограничен је на 64 KiB након декомпресије, а тела преусмеравања се одбацују без читања.
- Грешке захтева исписују само HTTP статус или класу грешке, јер прилагођени `--api-url` може садржати приступне податке.
- Команда инсталирана путем `.deb` и `.rpm` пакета покреће Python у изолованом режиму. Игнорише `PYTHONPATH`, кориснички site директоријум и модуле у радном директоријуму. Инсталација преко `pip` користи стандардну конзолну скрипту и прати окружење у којем је инсталирана.
- Стање кретања чита се и записује без праћења симболичке везе на називу датотеке стања или закључавања, релативно у односу на директоријум отворен једном по провери.
- Ресурси издања носе атестације порекла изградње поред `SHA256SUMS`; погледајте [Са GitHub Releases](#са-github-releases).

## Надоградња са верзије 1.0.0

Ове измене стижу у верзији 2.0.0.

- Котација са временском ознаком добављача старијом од једног сата враћа `UNKNOWN` осим ако није задат већи `--max-age`. Крајње тачке које не враћају временску ознаку остају непромењене.
- `--currency` прихвата само 2-16 слова или цифара.
- Нумерички низови са раздвајачима цифара или околним размацима се одбијају.
- Чекање поновног покушаја које не стане у буџет пријављује основну грешку уместо `API request timed out`.
- Изворни пакети више не уважавају `PYTHONPATH`.
- Прагови од једног милиона или више приказују се у подацима о перформансама као обични децимални бројеви уместо експоненцијалног записа.

## Локализација

Помоћ у командној линији, грешке провере и описи статуса додатка подржавају 48 локалитета (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`) помоћу уграђених каталога учитаних преко стандардне библиотеке. Одређивање проверава `--lang`, затим `LC_ALL`, `LC_MESSAGES` и `LANG`, уз повратак на `en`. Nagios префикси статуса (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) и подаци о перформансама остају непромењени у свим локалитетима.

```bash
check_bitcoin_price --lang sr
LANG=sr_RS.UTF-8 check_bitcoin_price --help
```

## Развој

Инсталирајте [mise](https://mise.jdx.dev/getting-started.html), затим покрените горња подешавања за развој. `mise.toml` закључава верзије за Python и алат uv. Развојни алати наведени су у `pyproject.toml` и разрешени у приложеној датотеци `uv.lock`.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Инсталирајте git кукице (commit hooks) након подешавања:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Користите `mise exec -- uv add --dev <tool>` или `mise exec -- uv add <dependency>` за ажурирање зависности и комитујте обе датотеке `pyproject.toml` и `uv.lock`.

CI проверава Python 3.12 и 3.13 на Linux-у и Python 3.13 на macOS-у. Сваки PR такође покреће проверу пакета, ревизију зависности и CodeQL, и инсталира `.deb` на Ubuntu и `.rpm` на Fedora систему. Изграђене дистрибуције доступне су као артефакт `distributions` у CI покретањима.

Верзија пакета и CLI-ја долази из `check_bitcoin_price/__init__.py`. Погледајте [процес издања](../../../CONTRIBUTING.md#releases) за ажурирање верзије и аутоматизовано објављивање ресурса GitHub издања.

## Допринос

Погледајте [CONTRIBUTING.md](../../../CONTRIBUTING.md) за ток развоја и захтеве за потписаним комитовима.

## Лиценца

Овај пројекат је лиценциран под MIT лиценцом - погледајте датотеку [LICENSE](../../../LICENSE) за детаље.

## Аутор

Thomas Vincent

## Захвалнице

- [CoinGecko](https://www.coingecko.com/) за пружање бесплатног API-ја за криптовалуте
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
