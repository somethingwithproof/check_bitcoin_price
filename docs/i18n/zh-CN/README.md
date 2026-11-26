# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · **简体中文** · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

一个用于监控 Bitcoin 价格的 Nagios/Icinga 插件，支持可配置的警告和严重阈值。

## 功能特性

- 支持以多种货币（USD、EUR、GBP 等）监控 Bitcoin 价格
- 支持配置警告与严重阈值（上限和下限）
- 输出包含性能数据的标准 Nagios 插件结果
- 使用 CoinGecko API（免费，无需 API 密钥）
- 支持自定义 API 端点
- 支持配置超时时间
- 使用数据源时间戳检查报价时效性，默认限制为 1 小时
- 针对速率限制和临时性 API 故障提供有界重试
- 所有重试共享同一个总截止时间，且每次响应限制在 64 KiB 以内
- 可选针对 24 小时绝对百分比涨跌幅触发告警
- 在性能数据中包含价格阈值、请求耗时和报价距今时长

## 安装

<a name="from-github-releases"></a>

### 从 GitHub Releases 安装

从 [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) 下载 `.deb`、`.rpm`、`.tar.gz`、wheel 包和 `SHA256SUMS` 文件。使用 `sha256sum --ignore-missing --check SHA256SUMS` 校验下载文件。1.0.0 之后的版本还附带已签名的构建溯源证明；可使用 `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` 验证资产是否来自本仓库的发布工作流。

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

请使用所选版本对应的文件名。原生软件包会安装 `/usr/bin/check_bitcoin_price` 和 `/usr/lib/nagios/plugins/check_bitcoin_price`；RPM 包还会额外提供 `/usr/lib64/nagios/plugins/check_bitcoin_price`。打包后的命令会以隔离模式运行 Python，因此会忽略 `PYTHONPATH` 和当前工作目录中的模块；系统包管理器会自动解析 Python 和 `requests` 依赖。这些包包含与架构无关的 Python 代码，要求系统发行版提供 Python 3.12 或更高版本。

### 从源码安装

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### 开发环境安装

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## 用法

### 基本用法

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### 指定阈值

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### 单独设置阈值

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### 指定其他货币

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### 自定义超时时间

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### 时效性检查与重试预算

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

带有数据源时间戳的报价默认距今不得超过 1 小时。如果未指定 `--max-age`，仅返回价格的端点仍然可以使用。当指定了 `--max-age` 时，缺失、无效、位于未来时间或已过期的数据源时间戳均会返回 `UNKNOWN`；插件不会用本地拉取时间替代数据源的报价时间。恰好达到时限的时间戳仍视为有效。未来的时间戳始终会被拒绝。

默认允许重试 1 次。仅针对连接错误、超时以及 HTTP 408/429/500/502/503/504 响应进行重试。退避时间从 0.5 秒开始，并在后续重试中翻倍；如果响应中包含 `Retry-After` 秒数或 HTTP 日期，则优先遵循该值。所有请求尝试、响应读取、JSON 解码和重试等待共享 `--timeout` 预算。如果剩余预算不足以容纳重试等待时间，插件会立即返回 `UNKNOWN`，并报告触发该重试的故障（例如 `HTTP 429` 或 `ConnectionError`），而不是报告超时。认证失败、其他永久性 HTTP 错误、无效 JSON 以及解码后超过 64 KiB 的响应均不会重试。使用 `--retries 0` 可禁用重试。

### 备用报价源

使用可重复的 `--fallback-url URL` 选项指定兼容 CoinGecko 格式的端点。例如，添加 `--fallback-url https://quotes.example.org/simple/price`。每个数据源会均分剩余的请求截止时间（包含其自身重试）。遇到瞬时故障或重试延迟超过该配额时，会自动切换到下一个数据源。TLS 校验失败、永久性 HTTP 错误和无效报价均会返回 UNKNOWN。每个报价响应解码后上限为 64 KiB。配置了备用源时，状态输出会将实际响应的来源标识为 `primary`、`fallback1` 等，而不会打印其 URL。

### 短时间窗口波动

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

为监控运行用户在本地 Linux 或 macOS 文件系统上分配一个私有的可写状态目录。在多次检查之间请保留同级的 `.lock` 文件。每个时间窗口应使用单独的状态文件，不同货币在文件内部各自维护独立的历史记录。默认时间窗口为 3600 秒。每个有效报价都必须包含处于该时间窗口及有效时限内的数据源时间戳（除非通过 `--max-age` 另行指定，否则默认时限为 1 小时）。插件会将当前价格与该窗口内最早的先前正数价格进行比较，并报告实际经过的秒数。重复的时间戳不会生成额外样本。首次采样、历史记录过期或 JSON 损坏时都会重新建立基线；在获得可比较的样本之前，窗口波动指标为未知状态，但其他告警规则仍正常生效。若状态文件不可写、状态文件或锁文件为符号链接，或当前报价早于已记录的最新样本，均会返回 UNKNOWN。带符号的 `bitcoin_move_window` 指标使用对称的警告和严重阈值范围。恰好等于阈值时不会触发告警。

插件每次检查仅打开一次状态目录并基于该目录句柄执行相对路径操作，因此在检查期间替换路径组件无法重定向锁文件、读取或写入操作。检查开始时会解析路径目录部分中的符号链接，从而保证 macOS 上的 `/var` 等平台链接正常可用。因此，状态目录及其上级目录不得对其他用户可写。状态文件和锁文件在创建时的权限模式为 0600。

### 24 小时百分比涨跌幅

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

涨跌幅阈值衡量所选货币在 CoinGecko 中带符号的 24 小时百分比变化的绝对值。涨跌幅恰好等于阈值时不会触发告警。如果同时提供了两个阈值，警告阈值不得大于严重阈值。缺失或无效的必需涨跌幅数据会返回 `UNKNOWN`。价格告警与涨跌幅告警可以组合使用；以严重级别较高者为准，级别相同时优先采用价格告警。

## 命令行选项

| 选项 | 说明 |
|------|------|
| `-w`, `--warning` | 警告阈值范围（格式：LOW:HIGH） |
| `-c`, `--critical` | 严重阈值范围（格式：LOW:HIGH） |
| `--warning-low` | 价格下限警告阈值 |
| `--warning-high` | 价格上限警告阈值 |
| `--critical-low` | 价格下限严重阈值 |
| `--critical-high` | 价格上限严重阈值 |
| `--currency` | 2 至 16 位字母或数字组成的货币代码（默认：usd） |
| `--timeout` | API 请求与重试的总时间预算（单位：秒，支持小数，默认：10） |
| `--retries` | 针对瞬时故障的额外重试次数，0 到 5 次（默认：1） |
| `--max-age` | 数据源报价的最大允许时长（单位：秒）并强制要求时间戳；含时间戳报价默认为 3600 |
| `--warning-change` | 24 小时绝对百分比涨跌幅的警告阈值 |
| `--critical-change` | 24 小时绝对百分比涨跌幅的严重阈值 |
| `--api-url` | 主 API URL |
| `--fallback-url` | 额外兼容端点；可按优先级顺序重复指定 |
| `--state-file` | JSON 波动历史状态文件 |
| `--move-window` | 波动统计窗口时长（单位：秒，默认：3600） |
| `--warning-move`, `--critical-move` | 窗口内绝对波动幅度的百分比阈值 |
| `-v`, `--verbose` | 启用详细输出 |
| `-V`, `--version` | 显示版本信息 |
| `-h`, `--help` | 显示帮助信息 |

## Nagios 配置

### 命令定义

将 Nagios 资源宏 `$USER1$` 设置为插件目录（原生软件包使用 `/usr/lib/nagios/plugins`）。在 Nagios 命令配置中添加：

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### 服务定义

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

### Icinga2 配置

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

## 退出状态码

无效参数、非正数超时时间、无效阈值范围以及格式错误的 API 价格均会返回 `UNKNOWN`（退出码 3）。阈值必须为有限的非负数，且每个下限不得大于其上限。货币代码必须为 2 至 16 位字母或数字。配置校验会在访问 API 之前执行并拒绝无效配置。价格必须为有限的非负数，以 JSON 数字或纯十进制字符串（例如 `"43521.5"`）表示。如果响应中不包含所请求的货币，错误信息会明确指出该货币，例如 `Response has no EUR price`。无效响应不会输出性能数据。详细诊断信息会输出到 stderr，以确保 stdout 仅包含单行监控状态输出。

| 状态码 | 状态 | 说明 |
|--------|------|------|
| 0 | OK | 价格处于可接受范围内 |
| 1 | WARNING | 价格越过警告阈值 |
| 2 | CRITICAL | 价格越过严重阈值 |
| 3 | UNKNOWN | 发生错误（API 故障、超时等） |

## 性能数据

插件按标准 Nagios 格式输出性能数据：

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

价格性能数据包含已配置的警告/严重阈值范围，且最小值为 0。阈值以完整的十进制表示法输出，既不四舍五入，也不采用科学计数法，从而确保 `14500000:16250000` 等大数值保持可解析。请求耗时包含所有重试尝试及退避等待时间。仅当数据源提供有效时间戳时才会输出报价距今时长；当日涨跌幅可用时才会输出该指标。涨跌幅阈值范围以 0 为中心对称。无效或过期的数据会返回 `UNKNOWN`，且不输出价格性能数据。这些指标可用于 PNP4Nagios、Grafana 或 InfluxDB 等绘图工具。

## API

本插件默认使用 [CoinGecko API](https://www.coingecko.com/en/api)，该 API 免费且无需 API 密钥，但受速率限制约束。

自定义端点必须使用相同的响应结构：`bitcoin.<currency>` 表示价格，`bitcoin.last_updated_at` 表示 UNIX 秒级时间戳，`bitcoin.<currency>_24h_change` 表示带符号的 24 小时百分比涨跌幅。未指定 `--max-age` 和涨跌幅阈值时，仅价格字段为必填项。若响应中包含时间戳，仍会进行校验：不得位于未来时间或距今超过 1 小时。解码后的响应大小必须在 64 KiB 以内。

支持的货币包括：usd、eur、gbp、jpy、aud、cad、chf、cny 等众多货币。

## 安全性

当前代码实现了以下安全措施。这些措施限制了异常端点或本地用户对监控主机可能造成的影响，但本身不能保证报价数据绝对可信。

- 使用 `requests` 默认配置校验证书，且没有任何选项可以禁用 HTTPS 证书校验。使用明文 `http://` 的自定义 `--api-url` 不具备此类保护。
- DNS 解析、连接、读取、重试和退避等待共享 `--timeout` 截止时间。发送数据缓慢的对端无法延长该超时限制。
- 每个响应解压缩后的大小限制为 64 KiB，重定向响应体会被直接丢弃而不读取。
- 由于自定义 `--api-url` 中可能包含凭据，请求失败时仅打印 HTTP 状态码或错误类名。
- `.deb` 和 `.rpm` 安装的命令会以隔离模式运行 Python，忽略 `PYTHONPATH`、用户 site 目录以及工作目录中的模块。通过 `pip` 安装时会使用标准控制台脚本，并遵循其所在安装环境。
- 波动状态文件的读取和写入均基于每次检查打开一次的目录句柄执行相对路径操作，不会在状态文件或锁文件名处跟随符号链接。
- 除 `SHA256SUMS` 外，发布资产还附带构建溯源证明；请参阅[从 GitHub Releases 安装](#from-github-releases)。

## 从 1.0.0 升级

以下变更包含在 2.0.0 版本中。

- 除非通过 `--max-age` 指定更大的值，否则数据源时间戳距今超过 1 小时的报价将返回 `UNKNOWN`。不返回时间戳的端点不受影响。
- `--currency` 仅接受 2 至 16 位字母或数字。
- 拒绝带有数字分隔符或前后空格的数字字符串。
- 当剩余预算不足以容纳重试等待时间时，会报告底层故障原因，而不再报告 `API request timed out`。
- 原生软件包不再遵循 `PYTHONPATH`。
- 一百万及以上的阈值在性能数据中以普通十进制数输出，不再使用指数表示法。

## 本地化

CLI 帮助信息、参数校验错误及插件状态描述通过内置的、由标准库加载的语言目录支持 45 种语言区域（`en`、`de`、`es`、`fr`、`it`、`pt-BR`、`nl`、`ru`、`uk`、`ja`、`ko`、`zh-CN`、`zh-TW`、`ar`、`hi`、`pl`、`tr`、`sv`、`vi`、`id`、`af-ZA`、`am-ET`、`ar-EG`、`ar-MA`、`fr-MA`、`fr-SN`、`ha-NG`、`ig-NG`、`mg-MG`、`rw-RW`、`so-SO`、`sw-KE`、`xh-ZA`、`yo-NG`、`zu-ZA`、`bn`、`fa`、`he`、`mr`、`ta`、`te`、`th`、`ur`、`ms`、`fil`）。语言解析顺序依次检查 `--lang`、`LC_ALL`、`LC_MESSAGES` 和 `LANG`，最终回退至 `en`。在所有语言区域中，Nagios 状态前缀（`OK`、`WARNING`、`CRITICAL`、`UNKNOWN`）以及性能数据均保持不变。

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## 开发

安装 [mise](https://mise.jdx.dev/getting-started.html)，然后运行上方的开发环境安装命令。`mise.toml` 固定了 Python 和 uv 版本。开发工具在 `pyproject.toml` 中声明，并在已提交的 `uv.lock` 中锁定解析结果。

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

完成配置后安装提交钩子：

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

使用 `mise exec -- uv add --dev <tool>` 或 `mise exec -- uv add <dependency>` 更新依赖，并同时提交 `pyproject.toml` 和 `uv.lock`。

CI 会在 Linux 上测试 Python 3.12 和 3.13，在 macOS 上测试 Python 3.13。每个 PR 还会运行软件包校验、依赖审计和 CodeQL，并在 Ubuntu 上测试安装 `.deb`、在 Fedora 上测试安装 `.rpm`。构建好的分发包可在 CI 运行的 `distributions` 产物中获取。

软件包和 CLI 的版本号来源于 `check_bitcoin_price/__init__.py`。有关版本升级和 GitHub 发布资产的自动化发布流程，请参阅[发布流程](../../../CONTRIBUTING.md#releases)。

## 贡献

有关开发工作流和提交签名（signed-off）要求，请参阅 [CONTRIBUTING.md](../../../CONTRIBUTING.md)。

## 许可证

本项目基于 MIT 许可证开源，详见 [LICENSE](../../../LICENSE) 文件。

## 作者

Thomas Vincent

## 致谢

- [CoinGecko](https://www.coingecko.com/) 提供免费的加密货币 API
- [Nagios 插件开发指南](https://nagios-plugins.org/doc/guidelines.html)
