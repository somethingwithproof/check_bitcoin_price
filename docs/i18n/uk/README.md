# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · **Українська** · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Плагін для Nagios/Icinga для моніторингу ціни Bitcoin із налаштовуваними порогами попередження та критичного стану.

## Можливості

- Моніторинг ціни Bitcoin у різних валютах (USD, EUR, GBP тощо)
- Налаштовувані пороги попередження та критичного стану (верхній і нижній)
- Стандартний вивід плагіна Nagios із даними продуктивності
- Використовує CoinGecko API (безкоштовний, не потребує ключа API)
- Підтримка власних кінцевих точок API
- Налаштовуваний тайм-аут
- Перевірка актуальності котирувань за часовими мітками постачальника з типовим обмеженням в одну годину
- Обмежена кількість повторних спроб у разі перевищення ліміту запитів та тимчасових збоїв API
- Єдиний дедлайн для всіх спроб та обмеження розміру кожної відповіді в 64 KiB
- Необов'язкові сповіщення про абсолютну відсоткову зміну за 24 години
- Пороги ціни, тривалість запиту та вік котирування в даних продуктивності

## Встановлення

<a name="from-github-releases"></a>

### Із GitHub Releases

Завантажте файли `.deb`, `.rpm`, `.tar.gz`, wheel та `SHA256SUMS` зі сторінки [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Перевірте завантажені файли командою `sha256sum --ignore-missing --check SHA256SUMS`. Випуски після версії 1.0.0 також містять підписані дані про походження збірки; підтвердити, що ресурс створено робочим процесом випуску цього репозиторію, можна за допомогою `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Використовуйте імена файлів із вибраного випуску. Нативні пакунки встановлюють `/usr/bin/check_bitcoin_price` та `/usr/lib/nagios/plugins/check_bitcoin_price`; пакунок RPM також надає `/usr/lib64/nagios/plugins/check_bitcoin_price`. Запакована команда запускає Python в ізольованому режимі, тому ігнорує `PYTHONPATH` і модулі в робочому каталозі; залежності Python та `requests` розв'язує системний менеджер пакунків. Пакунки містять архітектурно-незалежний код Python і потребують дистрибутива з Python 3.12 або новішої версії.

### Із вихідного коду

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Для розробки

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Використання

### Базове використання

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Із порогами

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Окремі пороги

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Інша валюта

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Власний тайм-аут

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Актуальність даних і бюджет повторних спроб

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Котирування з часовою міткою постачальника типово має бути не старішим за одну годину.
Кінцеві точки, які повертають лише ціну, залишаються придатними до використання, якщо параметр `--max-age` не вказано.
Якщо `--max-age` задано, відсутні, некоректні, майбутні або застарілі часові мітки постачальника повертають `UNKNOWN`; плагін не підміняє час котирування постачальника локальним часом отримання. Часова мітка, що точно дорівнює межі віку, вважається допустимою. Майбутні часові мітки завжди відхиляються.

Типово дозволена одна повторна спроба. Повторні спроби виконуються лише при помилках з'єднання, тайм-аутах та HTTP-відповідях 408/429/500/502/503/504. Затримка перед повтором починається з 0.5 секунди та подвоюється для наступних спроб; значення `Retry-After` у секундах та HTTP-дати мають пріоритет. Усі спроби, читання відповідей, декодування JSON та очікування між повторами використовують спільний бюджет `--timeout`. Якщо очікування повтору не вкладається в бюджет, плагін негайно повертає `UNKNOWN` і повідомляє про збій, який його спричинив, наприклад `HTTP 429` або `ConnectionError`, а не про тайм-аут. Помилки автентифікації, інші постійні HTTP-помилки, некоректний JSON та відповіді обсягом понад 64 KiB декодованих даних не повторюються. Щоб вимкнути повторні спроби, використовуйте `--retries 0`.

### Резервні джерела котирувань

Використовуйте повторювані параметри `--fallback-url URL` із сумісними з CoinGecko кінцевими точками.
Наприклад, додайте `--fallback-url https://quotes.example.org/simple/price`.
Кожне джерело отримує рівну частку залишку дедлайну запиту, включно з повторними спробами. Тимчасовий збій або затримка повтору, що перевищує цю частку, передає запит наступному джерелу. Помилки перевірки TLS, постійні HTTP-помилки та некоректні котирування повертають UNKNOWN. Розмір кожної відповіді з котируванням обмежено 64 KiB декодованих даних. Коли налаштовано резервні джерела, рядок статусу вказує джерело, що відповіло, як `primary`, `fallback1` тощо, без виведення його URL.

### Зміна за короткий інтервал

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Надайте користувачу моніторингу приватний доступний для запису каталог стану в локальній файловій системі Linux або macOS. Зберігайте сусідній файл `.lock` на місці між перевірками. Використовуйте окремий файл стану для кожного інтервалу. Усередині нього валюти мають незалежні історії. Типовий інтервал становить 3600 секунд. Кожне дійсне котирування повинно мати часову мітку постачальника в межах цього інтервалу та обмеження віку, яке становить одну годину, якщо інше не задано через `--max-age`. Плагін порівнює поточну ціну з найдавнішим попереднім додатним значенням у цьому інтервалі та повідомляє фактичну кількість секунд, що минула. Повторювані часові мітки не створюють додаткових вибірок. Перша вибірка, прострочена історія або пошкоджений JSON починають нову базову лінію; метрика інтервалу має значення unknown, доки не з'явиться вибірка для порівняння. Інші сповіщення при цьому продовжують діяти. Недоступний для запису стан, символічне посилання замість файлу стану чи блокування, або котирування, старіше за найновішу записану вибірку, повертають UNKNOWN. Знакова метрика `bitcoin_move_window` використовує симетричні діапазони попередження та критичного стану. Досягнення межі рівно на її значенні не спричиняє сповіщення.

Плагін відкриває каталог стану один раз на перевірку та працює відносно нього, тож компонент шляху, підмінений під час перевірки, не може перенаправити блокування, читання чи запис. Символічні посилання в частині шляху, що відповідає за каталог, розіменовуються на початку перевірки, що дозволяє використовувати системні посилання на кшталт `/var` у macOS. Тому каталог стану та його батьківські каталоги не повинні бути доступними для запису іншим користувачам. Файли стану та блокування створюються з правами 0600.

### Добова відсоткова зміна

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Пороги зміни вимірюють абсолютне значення знакової 24-годинної відсоткової зміни CoinGecko у вибраній валюті. Зміна, що точно дорівнює порогу, не викликає сповіщення. Якщо вказано обидва пороги, поріг попередження не повинен перевищувати критичний. Відсутні або некоректні необхідні дані про зміну повертають `UNKNOWN`. Сповіщення за ціною та за зміною можна поєднувати; перемагає найвищий рівень серйозності, а при однакових рівнях пріоритет має ціна.

## Параметри командного рядка

| Параметр | Опис |
|--------|-------------|
| `-w`, `--warning` | Діапазон порогу попередження (формат: LOW:HIGH) |
| `-c`, `--critical` | Діапазон критичного порогу (формат: LOW:HIGH) |
| `--warning-low` | Поріг попередження для нижньої ціни |
| `--warning-high` | Поріг попередження для верхньої ціни |
| `--critical-low` | Критичний поріг для нижньої ціни |
| `--critical-high` | Критичний поріг для верхньої ціни |
| `--currency` | Код валюти з 2-16 літер або цифр (типово: usd) |
| `--timeout` | Загальний бюджет на запити та повтори API у секундах, включно з дробовими значеннями (типово: 10) |
| `--retries` | Додаткові спроби при тимчасових збоях, 0-5 (типово: 1) |
| `--max-age` | Максимальний вік котирування постачальника в секундах із вимогою наявності часової мітки; для котирувань із міткою типово 3600 |
| `--warning-change` | Межа попередження для абсолютної 24-годинної відсоткової зміни |
| `--critical-change` | Критична межа для абсолютної 24-годинної відсоткової зміни |
| `--api-url` | Основний URL API |
| `--fallback-url` | Додаткова сумісна кінцева точка; повторюйте в порядку пріоритету |
| `--state-file` | Файл JSON з історією змін |
| `--move-window` | Інтервал зміни в секундах (типово: 3600) |
| `--warning-move`, `--critical-move` | Абсолютні пороги зміни за інтервал у відсотках |
| `-v`, `--verbose` | Увімкнути докладний вивід |
| `-V`, `--version` | Показати версію |
| `-h`, `--help` | Показати довідкове повідомлення |

## Налаштування Nagios

### Визначення команди

Задайте ресурсний макрос Nagios `$USER1$` на каталог плагінів (нативні пакунки використовують `/usr/lib/nagios/plugins`). Додайте до вашої конфігурації команд Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Визначення сервісу

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

### Налаштування Icinga2

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

## Коди завершення

Некоректні аргументи, недодатні тайм-аути, хибні діапазони порогів та некоректно сформовані ціни від API повертають `UNKNOWN` (код завершення 3). Пороги мають бути скінченними невід'ємними числами, де кожна нижня межа не перевищує відповідну верхню межу. Валюта має складатися з 2-16 літер або цифр. Некоректна конфігурація відхиляється до звернення до API. Ціни мають бути скінченними та невід'ємними, поданими як числа JSON або звичайні десяткові рядки на кшталт `"43521.5"`. Відповідь без запитуваної валюти вказує на це прямо, наприклад `Response has no EUR price`. Некоректні відповіді не виводять даних продуктивності. Докладна діагностика спрямовується в stderr, тому stdout містить лише один рядок статусу моніторингу.

| Код | Статус | Опис |
|------|--------|-------------|
| 0 | OK | Ціна в межах допустимого діапазону |
| 1 | WARNING | Ціна перетнула поріг попередження |
| 2 | CRITICAL | Ціна перетнула критичний поріг |
| 3 | UNKNOWN | Виникла помилка (збій API, тайм-аут тощо) |

## Дані продуктивності

Плагін виводить дані продуктивності у стандартному форматі Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Дані продуктивності для ціни містять налаштовані діапазони попередження/критичного стану та мінімум нуль. Пороги виводяться в повному десятковому записі, ніколи не округляються і не подаються в експоненційній формі, щоб великі значення на кшталт `14500000:16250000` залишалися придатними для розбору. Час запиту враховує всі спроби та затримки очікування. Вік котирування виводиться лише тоді, коли постачальник надає дійсну часову мітку; добова зміна виводиться за наявності. Діапазони зміни симетричні відносно нуля. Некоректні або застарілі дані повертають `UNKNOWN` без даних продуктивності для ціни. Ці метрики можна використовувати з інструментами побудови графіків, як-от PNP4Nagios, Grafana або InfluxDB.

## API

Цей плагін типово використовує [CoinGecko API](https://www.coingecko.com/en/api), який є безкоштовним і не потребує ключа API. Застосовуються обмеження частоти запитів.

Власні кінцеві точки повинні мати таку саму структуру відповіді: `bitcoin.<currency>` для ціни, `bitcoin.last_updated_at` для секунд часової мітки UNIX і `bitcoin.<currency>_24h_change` для знакової добової відсоткової зміни. Якщо `--max-age` і пороги зміни не задані, обов'язковою є лише ціна. Проте наявна часова мітка все одно перевіряється: вона не може бути в майбутньому або старішою за одну годину. Декодована відповідь має вміщуватися в 64 KiB.

Підтримувані валюти включають: usd, eur, gbp, jpy, aud, cad, chf, cny та багато інших.

## Безпека

Наведені нижче заходи реалізовані в поточному коді. Вони обмежують те, що може заподіяти хосту моніторингу некоректна кінцева точка або локальний користувач, але не роблять саме котирування надійним.

- Сертифікати HTTPS перевіряються за типовими правилами `requests`, і жоден параметр не вимикає цю перевірку. Власний `--api-url`, що використовує звичайний `http://`, такого захисту не має.
- DNS, з'єднання, читання, повторні спроби та очікування використовують спільний дедлайн `--timeout`. Вузол, який надсилає дані повільно, не може його подовжити.
- Кожна відповідь обмежується 64 KiB після декомпресії, а тіла перенаправлень відкидаються без читання.
- Помилки запиту виводять лише статус HTTP або клас помилки, оскільки власний `--api-url` може містити облікові дані.
- Команда, встановлена з `.deb` та `.rpm`, запускає Python в ізольованому режимі. Вона ігнорує `PYTHONPATH`, каталог site користувача та модулі в робочому каталозі. Встановлення через `pip` використовує стандартний консольний скрипт і дотримується середовища, в якому воно встановлене.
- Стан зміни ціни читається й записується без переходу за символічними посиланнями на місці файлу стану або блокування, відносно каталогу, відкритого один раз на перевірку.
- Ресурси випуску мають атестації походження збірки на додачу до `SHA256SUMS`; див. [Із GitHub Releases](#from-github-releases).

## Оновлення з версії 1.0.0

Ці зміни входять до версії 2.0.0.

- Котирування з часовою міткою постачальника, старішою за одну годину, повертає `UNKNOWN`, якщо не задано більше значення `--max-age`. Кінцеві точки, що не повертають часову мітку, працюють без змін.
- `--currency` приймає лише від 2 до 16 літер або цифр.
- Числові рядки з розділювачами розрядів або пробілами навколо відхиляються.
- Затримка повторної спроби, яка не вкладається в бюджет, повідомляє про початковий збій замість `API request timed out`.
- Нативні пакунки більше не враховують `PYTHONPATH`.
- Пороги від одного мільйона і більше відображаються в даних продуктивності як звичайні десяткові числа замість експоненційного запису.

## Локалізація

Довідка CLI, помилки валідації та описи статусу плагіна підтримують 45 локалей (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) за допомогою вбудованих каталогів, що завантажуються через stdlib. Визначення локалі перевіряє `--lang`, далі `LC_ALL`, `LC_MESSAGES` і `LANG`, із резервним переходом до `en`. Префікси статусів Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) і дані продуктивності залишаються незмінними в усіх локалях.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Розробка

Встановіть [mise](https://mise.jdx.dev/getting-started.html), потім виконайте налаштування середовища розробки, описане вище. `mise.toml` фіксує версії Python і uv. Інструменти розробки оголошено у `pyproject.toml` і закомічено в `uv.lock`.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Встановіть хуки комітів після налаштування:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Використовуйте `mise exec -- uv add --dev <tool>` або `mise exec -- uv add <dependency>`, щоб оновити залежності, та закомітьте обидва файли `pyproject.toml` і `uv.lock`.

CI перевіряє Python 3.12 і 3.13 у Linux та Python 3.13 у macOS. Кожен PR також запускає валідацію пакунка, аудит залежностей і CodeQL, а також встановлює `.deb` на Ubuntu і `.rpm` на Fedora. Зібрані дистрибутиви доступні як артефакт `distributions` у запусках CI.

Версія пакунка та CLI береться з `check_bitcoin_price/__init__.py`. Див. [процес випуску](../../../CONTRIBUTING.md#releases) щодо оновлення версії та автоматизованої публікації ресурсів випуску GitHub.

## Участь у розробці

Див. [CONTRIBUTING.md](../../../CONTRIBUTING.md) щодо робочого процесу розробки та вимог до підписаних комітів.

## Ліцензія

Цей проєкт ліцензовано за ліцензією MIT - докладніше див. у файлі [LICENSE](../../../LICENSE).

## Автор

Thomas Vincent

## Подяки

- [CoinGecko](https://www.coingecko.com/) за надання безкоштовного API криптовалют
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
