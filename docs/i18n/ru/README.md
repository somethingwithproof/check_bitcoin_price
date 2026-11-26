# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · **Русский** · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Плагин для Nagios/Icinga для мониторинга цены Bitcoin с настраиваемыми предупредительным и критическим порогами.

## Возможности

- Мониторинг цены Bitcoin в различных валютах (USD, EUR, GBP и др.)
- Настраиваемые предупредительный и критический пороги (верхний и нижний)
- Стандартный вывод плагина Nagios с данными производительности
- Использование CoinGecko API (бесплатно, API-ключ не требуется)
- Поддержка пользовательских конечных точек API
- Настраиваемый таймаут
- Проверка актуальности котировок по временным меткам поставщика с ограничением по умолчанию в один час
- Ограниченное число повторных попыток при превышении лимита запросов и временных сбоях API
- Единый дедлайн для всех попыток и ограничение размера каждого ответа в 64 КиБ
- Опциональные оповещения при абсолютном изменении курса за 24 часа в процентах
- Пороги цены, длительность запроса и возраст котировки в данных производительности

## Установка

### Из GitHub Releases

Загрузите файлы `.deb`, `.rpm`, `.tar.gz`, wheel и `SHA256SUMS` со страницы [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Проверьте загруженный файл с помощью `sha256sum --ignore-missing --check SHA256SUMS`. Релизы после версии 1.0.0 также содержат подписанное подтверждение сборки (build provenance); убедитесь, что артефакт создан рабочим процессом выпуска этого репозитория, выполнив `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Используйте имена файлов из выбранного релиза. Нативные пакеты устанавливают `/usr/bin/check_bitcoin_price` и `/usr/lib/nagios/plugins/check_bitcoin_price`; пакет RPM также предоставляет `/usr/lib64/nagios/plugins/check_bitcoin_price`. Упакованная команда запускает Python в изолированном режиме, поэтому она игнорирует `PYTHONPATH` и модули в рабочем каталоге; системный менеджер пакетов разрешает зависимости Python и `requests`. Пакеты содержат платформонезависимый код Python и требуют дистрибутив с Python 3.12 или новее.

### Из исходного кода

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Для разработки

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Использование

### Базовое использование

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### С порогами

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Отдельные пороги

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Другая валюта

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Пользовательский таймаут

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Актуальность данных и бюджет повторных попыток

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Котировка, содержащая временную метку поставщика, по умолчанию должна быть не старше одного часа.
Конечные точки, возвращающие только цену, остаются доступными при отсутствии флага `--max-age`.
При указании `--max-age` отсутствующие, некорректные, относящиеся к будущему или устаревшие временные метки поставщика возвращают `UNKNOWN`; плагин не подменяет время котировки поставщика локальным временем получения ответа. Временная метка, точно совпадающая с пределом возраста, считается допустимой. Временные метки в будущем отклоняются всегда.

По умолчанию допускается одна повторная попытка. Повторы выполняются только при ошибках соединения, таймаутах и ответах HTTP 408/429/500/502/503/504. Задержка перед повтором начинается с 0.5 секунды и удваивается при последующих попытках; значения `Retry-After` в секундах и даты HTTP имеют приоритет. Все попытки, чтение ответов, декодирование JSON и ожидания перед повтором расходуют общий бюджет `--timeout`. Если ожидание перед повтором не укладывается в оставшийся бюджет, плагин немедленно возвращает `UNKNOWN` и сообщает о вызвавшем его сбое, например `HTTP 429` или `ConnectionError`, а не о таймауте. Ошибки аутентификации, другие постоянные ошибки HTTP, некорректный JSON и ответы объемом более 64 КиБ декодированных данных не повторяются. Используйте `--retries 0` для отключения повторных попыток.

### Резервные источники котировок

Используйте повторяемые параметры `--fallback-url URL` с конечными точками, совместимыми с CoinGecko. Например, добавьте `--fallback-url https://quotes.example.org/simple/price`. Каждый источник получает равную долю оставшегося дедлайна запроса, включая повторные попытки. Временный сбой или задержка повтора, превышающая эту долю, приводят к переходу к следующему источнику. Ошибки проверки TLS, постоянные ошибки HTTP и некорректные котировки возвращают UNKNOWN. Размер каждого ответа с котировкой ограничен 64 КиБ декодированных данных. Если настроены резервные источники, строка статуса указывает ответивший источник как `primary`, `fallback1` и так далее, не выводя его URL.

### Изменение цены на коротком интервале

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Предоставьте пользователю мониторинга приватный каталог состояния с правом записи в локальной файловой системе Linux или macOS. Сохраняйте соседний файл `.lock` между проверками. Используйте отдельный файл состояния для каждого временного окна. История по разным валютам хранится внутри него независимо. Окно по умолчанию составляет 3600 секунд. Каждая валидная котировка должна иметь временную метку поставщика в пределах окна и ограничения возраста, которое составляет один час, если `--max-age` не задает иное. Плагин сравнивает текущую цену с самой старой предыдущей положительной ценой в этом окне и сообщает фактическое прошедшее время в секундах. Повторяющиеся временные метки не создают дополнительных замеров. Первый замер, истекшая история или поврежденный JSON начинают новый базовый отсчет; метрика окна имеет значение unknown, пока не появится сопоставимый замер. Остальные оповещения продолжают действовать. Недоступное для записи состояние, файл состояния или блокировки в виде символической ссылки, а также котировка старше самого нового записанного замера возвращают UNKNOWN. Знаковая метрика `bitcoin_move_window` использует симметричные диапазоны для предупреждений и критических порогов. Равенство пределу не вызывает оповещения.

Плагин открывает каталог состояния один раз за проверку и работает относительно него, поэтому подмена компонента пути во время проверки не может перенаправить блокировку, чтение или запись. Символические ссылки в каталожной части пути разыменовываются при старте проверки, что сохраняет работоспособность системных ссылок, таких как `/var` в macOS. Поэтому сам каталог состояния и все его родительские каталоги не должны быть доступны для записи другим пользователям. Файлы состояния и блокировки создаются с правами 0600.

### Дневное изменение в процентах

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Пороги изменения измеряют абсолютное значение знакового 24-часового процентного изменения CoinGecko в выбранной валюте. Изменение, точно равное порогу, не вызывает оповещения. Если заданы оба порога, предупредительный порог не должен превышать критический. Отсутствующие или некорректные требуемые данные об изменении возвращают `UNKNOWN`. Оповещения по цене и по изменению можно комбинировать; побеждает наивысший уровень серьезности, а при совпадении уровней приоритет имеет цена.

## Параметры командной строки

| Параметр | Описание |
|--------|-------------|
| `-w`, `--warning` | Диапазон предупредительного порога (формат: LOW:HIGH) |
| `-c`, `--critical` | Диапазон критического порога (формат: LOW:HIGH) |
| `--warning-low` | Предупредительный порог для низкой цены |
| `--warning-high` | Предупредительный порог для высокой цены |
| `--critical-low` | Критический порог для низкой цены |
| `--critical-high` | Критический порог для высокой цены |
| `--currency` | Код валюты из 2-16 букв или цифр (по умолчанию: usd) |
| `--timeout` | Общий бюджет времени на запрос API и повторные попытки в секундах, включая дробные значения (по умолчанию: 10) |
| `--retries` | Дополнительные попытки при временных сбоях, 0-5 (по умолчанию: 1) |
| `--max-age` | Максимальный возраст котировки поставщика в секундах с обязательным наличием временной метки; для котировок с меткой по умолчанию 3600 |
| `--warning-change` | Предупредительный предел для абсолютного 24-часового изменения в процентах |
| `--critical-change` | Критический предел для абсолютного 24-часового изменения в процентах |
| `--api-url` | URL основного API |
| `--fallback-url` | Дополнительная совместимая конечная точка; указывайте несколько раз в порядке приоритета |
| `--state-file` | Файл истории изменений в формате JSON |
| `--move-window` | Временное окно изменения в секундах (по умолчанию: 3600) |
| `--warning-move`, `--critical-move` | Пороги абсолютного изменения за окно в процентах |
| `-v`, `--verbose` | Включить подробный вывод |
| `-V`, `--version` | Показать версию |
| `-h`, `--help` | Показать справочное сообщение |

## Конфигурация Nagios

### Определение команды

Установите макрос ресурса Nagios `$USER1$` на каталог плагинов (нативные пакеты используют `/usr/lib/nagios/plugins`). Добавьте в конфигурацию команд Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Определение сервиса

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

### Конфигурация Icinga2

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

## Коды завершения

Некорректные аргументы, неположительные таймауты, некорректные диапазоны порогов и невалидные цены от API возвращают `UNKNOWN` (код выхода 3). Пороги должны быть конечными неотрицательными числами, где нижняя граница не превышает верхнюю. Валюта должна состоять из 2-16 букв или цифр. Некорректная конфигурация отклоняется до обращения к API. Цены должны быть конечными и неотрицательными, переданными в виде чисел JSON или обычных десятичных строк, например `"43521.5"`. Ответ без запрошенной валюты прямо указывает ее, например `Response has no EUR price`. Невалидные ответы не выводят данные производительности. Подробная диагностика выводится в stderr, чтобы stdout содержал одну строку статуса мониторинга.

| Код | Статус | Описание |
|------|--------|-------------|
| 0 | OK | Цена находится в допустимом диапазоне |
| 1 | WARNING | Цена пересекла предупредительный порог |
| 2 | CRITICAL | Цена пересекла критический порог |
| 3 | UNKNOWN | Произошла ошибка (сбой API, таймаут и т. д.) |

## Данные производительности

Плагин выводит данные производительности в стандартном формате Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Данные производительности по цене включают настроенные диапазоны warning/critical и минимум, равный нулю. Пороги выводятся в полной десятичной записи, без округления и экспоненциальной формы, чтобы крупные значения, такие как `14500000:16250000`, оставались пригодными для разбора. Время запроса включает все попытки и задержки повтора. Возраст котировки выводится только тогда, когда поставщик передает корректную временную метку; дневное изменение выводится при наличии. Диапазоны изменения симметричны относительно нуля. Некорректные или устаревшие данные приводят к статусу `UNKNOWN` без данных производительности по цене. Эти метрики можно использовать в системах построения графиков, таких как PNP4Nagios, Grafana или InfluxDB.

## API

По умолчанию плагин использует [CoinGecko API](https://www.coingecko.com/en/api), который бесплатен и не требует API-ключа. Действуют ограничения частоты запросов.

Пользовательские конечные точки должны использовать ту же структуру ответа: `bitcoin.<currency>` для цены, `bitcoin.last_updated_at` для временной метки UNIX в секундах и `bitcoin.<currency>_24h_change` для знакового дневного изменения в процентах. Если `--max-age` и пороги изменения не заданы, обязательна только цена. Присутствующая временная метка все равно проверяется: она не должна находиться в будущем или быть старше одного часа. Декодированный ответ должен помещаться в 64 КиБ.

Поддерживаемые валюты включают: usd, eur, gbp, jpy, aud, cad, chf, cny и многие другие.

## Безопасность

Ниже приведены меры, реализованные в текущем коде. Они ограничивают ущерб, который некорректно работающая конечная точка или локальный пользователь могут нанести хосту мониторинга; они не делают саму котировку заслуживающей доверия.

- Сертификаты HTTPS проверяются со стандартными настройками `requests`, и нет параметра, отключающего эту проверку. Пользовательский `--api-url`, использующий незашифрованный `http://`, такой защиты не имеет.
- DNS, установка соединения, чтение, повторные попытки и задержки перед повтором разделяют общий дедлайн `--timeout`. Медленно отправляющий данные узел не может продлить его.
- Размер каждого ответа после распаковки ограничен 64 КиБ, а тела перенаправлений отбрасываются без чтения.
- При сбоях запроса выводятся только статус HTTP или класс ошибки, поскольку пользовательский `--api-url` может содержать учетные данные.
- Команда, устанавливаемая пакетами `.deb` и `.rpm`, запускает Python в изолированном режиме. Она игнорирует `PYTHONPATH`, пользовательский каталог site-packages и модули в рабочем каталоге. Установка через `pip` использует стандартный консольный скрипт и следует настройкам окружения, в которое установлена.
- Состояние изменений читается и записывается без перехода по символическим ссылкам по имени файла состояния или блокировки относительно каталога, открытого один раз за проверку.
- Релизные артефакты помимо `SHA256SUMS` содержат подтверждения происхождения сборки; см. [Из GitHub Releases](#из-github-releases).

## Обновление с версии 1.0.0

Следующие изменения вошли в версию 2.0.0.

- Котировка с временной меткой поставщика старше одного часа возвращает `UNKNOWN`, если не задан больший `--max-age`. На конечные точки, не возвращающие временную метку, это не влияет.
- `--currency` принимает только от 2 до 16 букв или цифр.
- Числовые строки с разделителями разрядов или окружающими пробелами отклоняются.
- Если задержка повтора не укладывается в бюджет, выводится исходная ошибка вместо `API request timed out`.
- Нативные пакеты больше не учитывают `PYTHONPATH`.
- Пороги от одного миллиона и выше выводятся в данных производительности в обычной десятичной записи вместо экспоненциальной формы.

## Локализация

Справка CLI, ошибки валидации и описания статусов плагина поддерживают 45 локалей (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) с помощью встроенных каталогов, загружаемых стандартной библиотекой. Выбор локали проверяет `--lang`, затем `LC_ALL`, `LC_MESSAGES` и `LANG`, с откатом к `en`. Префиксы статусов Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) и данные производительности остаются неизменными во всех локалях.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Разработка

Установите [mise](https://mise.jdx.dev/getting-started.html), затем выполните приведенную выше настройку окружения разработки. Файл `mise.toml` фиксирует версии Python и uv. Инструменты разработки объявлены в `pyproject.toml` и зафиксированы в файле `uv.lock` в репозитории.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

После настройки установите хуки коммитов:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Используйте `mise exec -- uv add --dev <tool>` или `mise exec -- uv add <dependency>` для обновления зависимостей и добавляйте в коммит оба файла: `pyproject.toml` и `uv.lock`.

CI проверяет Python 3.12 и 3.13 на Linux, а также Python 3.13 на macOS. В каждом PR также выполняются валидация пакетов, аудит зависимостей и CodeQL, а также установка `.deb` на Ubuntu и `.rpm` на Fedora. Собранные дистрибутивы доступны как артефакт `distributions` в запусках CI.

Версия пакета и CLI берется из `check_bitcoin_price/__init__.py`. Порядок повышения версии и автоматической публикации релизных артефактов на GitHub описан в разделе [процесс выпуска релизов](../../../CONTRIBUTING.md#releases).

## Участие в разработке

См. [CONTRIBUTING.md](../../../CONTRIBUTING.md), где описаны процесс разработки и требования к подписанным коммитам (signed-off commits).

## Лицензия

Этот проект распространяется под лицензией MIT: подробности см. в файле [LICENSE](../../../LICENSE).

## Автор

Thomas Vincent

## Благодарности

- [CoinGecko](https://www.coingecko.com/) за предоставление бесплатного API криптовалют
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
