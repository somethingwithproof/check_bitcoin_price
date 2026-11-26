# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · **繁體中文** · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

一款用於監控 Bitcoin 價格並支援自訂警告與嚴重閾值的 Nagios/Icinga 外掛程式。

## 功能特色

- 支援多種幣別的 Bitcoin 價格監控（USD、EUR、GBP 等）
- 可設定警告與嚴重閾值（上限與下限）
- 符合標準的 Nagios 外掛程式輸出與效能資料
- 使用 CoinGecko API（免費，無需 API 金鑰）
- 支援自訂 API 端點
- 可設定逾時時間
- 使用供應商時間戳記檢查報價即時性，預設上限為一小時
- 針對速率限制與暫時性 API 失敗提供有上限的重試機制
- 所有嘗試共用單一總期限，且每次回應上限為 64 KiB
- 可選擇針對 24 小時絕對百分比變動發出警示
- 效能資料中包含價格閾值、請求耗時與報價經過時間

## 安裝

### 從 GitHub Releases 安裝

請從 [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) 下載 `.deb`、`.rpm`、`.tar.gz`、wheel 及 `SHA256SUMS` 檔案。使用 `sha256sum --ignore-missing --check SHA256SUMS` 驗證下載檔案。1.0.0 之後的版本亦附帶經簽章的建置來源證明；可使用 `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` 確認資產來自此儲存庫的發布工作流程。

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

請使用所選版本的實際檔名。原生套件會安裝 `/usr/bin/check_bitcoin_price` 與 `/usr/lib/nagios/plugins/check_bitcoin_price`；RPM 套件另外提供 `/usr/lib64/nagios/plugins/check_bitcoin_price`。封裝後的指令會以隔離模式執行 Python，因此會忽略 `PYTHONPATH` 與工作目錄中的模組；系統套件管理員會自動處理 Python 與 `requests` 相依套件。這些套件包含與架構無關的 Python 程式碼，且需要提供 Python 3.12 或更新版本的發行版。

### 從原始碼安裝

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### 開發環境安裝

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## 使用方式

### 基本用法

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### 設定閾值

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### 個別閾值

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### 指定不同幣別

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### 自訂逾時時間

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### 報價即時性與重試預算

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

帶有供應商時間戳記的報價預設最多只能距今一小時。當未指定 `--max-age` 時，僅回傳價格的端點仍可正常使用。若指定了 `--max-age`，缺少、無效、未來時間或過期的供應商時間戳記都會回傳 `UNKNOWN`；外掛程式不會以本機擷取時間替代供應商的報價時間。剛好達到時間上限的時間戳記仍可視為有效。未來的時間戳記一律予以拒絕。

預設允許重試一次。僅針對連線錯誤、逾時以及 HTTP 408/429/500/502/503/504 回應進行重試。退避時間從 0.5 秒開始，後續每次重試加倍；若有 `Retry-After` 秒數或 HTTP 日期標頭則優先採用。所有嘗試、回應讀取、JSON 解碼與重試等待皆共用 `--timeout` 預算。若重試等待無法容納於剩餘預算內，外掛程式會立即回傳 `UNKNOWN`，並回報觸發重試的原始失敗原因（例如 `HTTP 429` 或 `ConnectionError`），而非逾時。驗證失敗、其他永久性 HTTP 錯誤、無效 JSON 以及解碼後超過 64 KiB 的回應均不會重試。使用 `--retries 0` 可停用重試。

### 備援報價來源

可重複使用 `--fallback-url URL` 選項來指定與 CoinGecko 相容的端點。例如，加入 `--fallback-url https://quotes.example.org/simple/price`。每個來源會平分剩餘的請求期限（包含其自身的重試）。若發生暫時性失敗，或重試延遲超過該來源分配到的時間份額，就會切換至下一個來源。TLS 驗證失敗、永久性 HTTP 錯誤及無效報價皆會回傳 UNKNOWN。每個報價回應的解碼資料上限為 64 KiB。設定備援來源時，狀態訊息會將實際回應的來源標示為 `primary`、`fallback1` 等，而不會印出其 URL。

### 短時間區間波動

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

請為監控使用者在本機 Linux 或 macOS 檔案系統上提供一個私有的可寫入狀態目錄。在兩次檢查之間請保留同層的 `.lock` 檔案。每個時間區間請使用獨立的狀態檔。不同幣別在該檔案中各自擁有獨立的歷史紀錄。預設時間區間為 3600 秒。每筆有效報價都必須具有落在此時間區間與有效期限內的供應商時間戳記（除非透過 `--max-age` 另行設定，否則有效期限為一小時）。外掛程式會將目前價格與該區間內最早的先前正數價格進行比較，並回報實際經過的秒數。重複的時間戳記不會建立額外樣本。第一筆樣本、過期的歷史紀錄或損毀的 JSON 會建立新的基準點；在出現可比較的樣本之前，區間指標會呈現未知狀態，但其他警示仍會照常套用。無法寫入狀態、狀態檔或鎖定檔為符號連結，或是報價時間早於最新紀錄的樣本，皆會回傳 UNKNOWN。帶正負號的 `bitcoin_move_window` 指標採用對稱的警告與嚴重範圍。剛好等於上限時不會觸發警示。

外掛程式在每次檢查時只會開啟狀態目錄一次並相對於該目錄進行操作，因此在檢查期間替換路徑元件無法重新導向鎖定、讀取或寫入的目標。檢查開始時會跟隨路徑目錄部分的符號連結，以確保 macOS 上的 `/var` 等平台連結可正常運作。因此，狀態目錄及其上層目錄不得讓其他使用者擁有寫入權限。狀態檔與鎖定檔建立時的權限模式為 0600。

### 每日百分比波動

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

變動閾值會量測所選幣別中 CoinGecko 帶正負號的 24 小時百分比變動之絕對值。變動幅度剛好等於閾值時不會觸發警示。若同時提供兩個閾值，警告閾值不得大於嚴重閾值。缺少或無效的必要變動資料會回傳 `UNKNOWN`。價格警示與變動警示可以合併使用；系統會採計最高嚴重等級，若嚴重等級相同則以價格警示優先。

## 命令列選項

| 選項 | 說明 |
|------|------|
| `-w`, `--warning` | 警告閾值範圍（格式：LOW:HIGH） |
| `-c`, `--critical` | 嚴重閾值範圍（格式：LOW:HIGH） |
| `--warning-low` | 低價警告閾值 |
| `--warning-high` | 高價警告閾值 |
| `--critical-low` | 低價嚴重閾值 |
| `--critical-high` | 高價嚴重閾值 |
| `--currency` | 2-16 個字母或數字的幣別代碼（預設：usd） |
| `--timeout` | API 請求／重試的總時間預算（秒），支援小數（預設：10） |
| `--retries` | 針對暫時性錯誤的額外重試次數，0-5（預設：1） |
| `--max-age` | 供應商報價的最大有效秒數並強制要求時間戳記；含時間戳記的報價預設為 3600 |
| `--warning-change` | 24 小時絕對百分比波動的警告上限 |
| `--critical-change` | 24 小時絕對百分比波動的嚴重上限 |
| `--api-url` | 主要 API URL |
| `--fallback-url` | 額外相容端點；依偏好的順序重複指定 |
| `--state-file` | JSON 波動歷史紀錄檔案 |
| `--move-window` | 波動觀察區間，單位為秒（預設：3600） |
| `--warning-move`, `--critical-move` | 區間內絕對波動百分比閾值 |
| `-v`, `--verbose` | 啟用詳細輸出 |
| `-V`, `--version` | 顯示版本資訊 |
| `-h`, `--help` | 顯示說明訊息 |

## Nagios 設定

### 指令定義

將 Nagios 資源巨集 `$USER1$` 設為外掛程式目錄（原生套件使用 `/usr/lib/nagios/plugins`）。在您的 Nagios 指令設定檔中加入：

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### 服務定義

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

### Icinga2 設定

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

## 結束代碼

無效參數、非正數逾時、無效閾值範圍以及格式錯誤的 API 價格皆會回傳 `UNKNOWN`（結束代碼 3）。閾值必須為有限且非負的數值，且各下限不得大於其上限。幣別必須為 2-16 個字母或數字。無效的設定會在連線至 API 之前即被拒絕。價格必須為有限且非負的數值，以 JSON 數字或純十進位字串（例如 `"43521.5"`）表示。若回應缺少所請求的幣別，訊息會指明該幣別，例如 `Response has no EUR price`。無效的回應不會輸出效能資料。詳細診斷資訊會輸出至 stderr，使 stdout 僅保留單行監控狀態。

| 代碼 | 狀態 | 說明 |
|------|------|------|
| 0 | OK | 價格在可接受範圍內 |
| 1 | WARNING | 價格超出警告閾值 |
| 2 | CRITICAL | 價格超出嚴重閾值 |
| 3 | UNKNOWN | 發生錯誤（API 失敗、逾時等） |

## 效能資料

外掛程式會以標準 Nagios 格式輸出效能資料：

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

價格效能資料包含設定的警告／嚴重範圍，且最小值為零。閾值會以完整十進位記號輸出，絕不四捨五入或使用指數格式，使 `14500000:16250000` 等大數值仍可被正確剖析。請求時間包含所有嘗試與退避等待。僅在供應商提供有效時間戳記時才會輸出報價經過時間；每日變動幅度則在可用時輸出。變動範圍以零為中心對稱。無效或過期的資料會產生 `UNKNOWN`，且不包含價格效能資料。這些指標可搭配 PNP4Nagios、Grafana 或 InfluxDB 等繪圖工具使用。

## API

本外掛程式預設使用 [CoinGecko API](https://www.coingecko.com/en/api)，免費且無需 API 金鑰，但受速率限制規範。

自訂端點必須使用相同的回應格式：`bitcoin.<currency>` 表示價格，`bitcoin.last_updated_at` 表示 UNIX 時間戳記秒數，`bitcoin.<currency>_24h_change` 表示帶正負號的每日百分比變動。當未設定 `--max-age` 與變動閾值時，僅需提供價格即可。若回應中包含時間戳記，系統仍會進行檢查：不得為未來時間，亦不得超過一小時前。解碼後的回應必須小於 64 KiB。

支援的幣別包括：usd、eur、gbp、jpy、aud、cad、chf、cny 等多種幣別。

## 安全性

以下防護措施已實作於目前程式碼中。它們限制異常端點或本機使用者對監控主機所能造成的影響，但無法保證報價本身的真實性。

- HTTPS 憑證使用 `requests` 預設值進行驗證，且未提供停用驗證的選項。使用純文字 `http://` 的自訂 `--api-url` 則無此防護。
- DNS 解析、連線、讀取、重試與退避皆共用 `--timeout` 期限。傳送資料緩慢的對端無法延長此期限。
- 每次回應在解壓縮後上限為 64 KiB，且重新導向的回應主體會直接捨棄而不讀取。
- 由於自訂 `--api-url` 可能包含認證憑證，請求失敗時僅會印出 HTTP 狀態碼或錯誤類別名稱。
- `.deb` 與 `.rpm` 安裝的指令會以隔離模式執行 Python。它會忽略 `PYTHONPATH`、使用者 site 目錄及工作目錄中的模組。透過 `pip` 安裝則使用標準主控台腳本，並遵循所處 Python 環境的設定。
- 波動狀態檔的讀寫作業相對於每次檢查開啟一次的目錄執行，且不會跟隨狀態檔或鎖定檔名稱上的符號連結。
- 發行資產除了 `SHA256SUMS` 之外，亦附帶建置來源證明；請參閱 [From GitHub Releases](#from-github-releases)。

## 從 1.0.0 升級

以下變更於 2.0.0 版本中推出。

- 供應商時間戳記超過一小時的報價會回傳 `UNKNOWN`，除非指定較大的 `--max-age`。未回傳時間戳記的端點不受影響。
- `--currency` 僅接受 2-16 個字母或數字。
- 包含數字分隔符號或前後空白的數字字串會遭到拒絕。
- 當重試等待時間超出預算時，會回報底層失敗原因，而非 `API request timed out`。
- 原生套件不再套用 `PYTHONPATH`。
- 一百萬以上的閾值在效能資料中會以純十進位格式顯示，而非指數記號。

## 在地化

CLI 說明訊息、驗證錯誤及外掛程式狀態說明支援 45 種語系（`en`、`de`、`es`、`fr`、`it`、`pt-BR`、`nl`、`ru`、`uk`、`ja`、`ko`、`zh-CN`、`zh-TW`、`ar`、`hi`、`pl`、`tr`、`sv`、`vi`、`id`、`af-ZA`、`am-ET`、`ar-EG`、`ar-MA`、`fr-MA`、`fr-SN`、`ha-NG`、`ig-NG`、`mg-MG`、`rw-RW`、`so-SO`、`sw-KE`、`xh-ZA`、`yo-NG`、`zu-ZA`、`bn`、`fa`、`he`、`mr`、`ta`、`te`、`th`、`ur`、`ms`、`fil`），使用隨附並透過標準函式庫載入的語系目錄。語系解析依序檢查 `--lang`、`LC_ALL`、`LC_MESSAGES` 與 `LANG`，並於無符合項目時退回 `en`。Nagios 狀態前綴（`OK`、`WARNING`、`CRITICAL`、`UNKNOWN`）及效能資料在所有語系中皆保持不變。

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## 開發

請先安裝 [mise](https://mise.jdx.dev/getting-started.html)，再執行上方的開發環境設定。`mise.toml` 固定了 Python 與 uv 的版本。開發工具宣告於 `pyproject.toml`，並於已提交的 `uv.lock` 中解析鎖定。

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

設定完成後，請安裝提交掛鉤：

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

請使用 `mise exec -- uv add --dev <tool>` 或 `mise exec -- uv add <dependency>` 更新相依套件，並一併提交 `pyproject.toml` 與 `uv.lock`。

CI 會在 Linux 上測試 Python 3.12 與 3.13，並在 macOS 上測試 Python 3.13。每個 PR 亦會執行套件驗證、相依套件稽核與 CodeQL，並在 Ubuntu 上安裝 `.deb` 套件以及在 Fedora 上安裝 `.rpm` 套件。建置完成的發行套件可於 CI 執行紀錄的 `distributions` 產出物中取得。

套件與 CLI 版本號定義於 `check_bitcoin_price/__init__.py`。有關版本遞增與自動發布 GitHub 發行資產的細節，請參閱[發布流程](../../../CONTRIBUTING.md#releases)。

## 貢獻指南

有關開發工作流程與簽署提交（signed-off commit）的要求，請參閱 [CONTRIBUTING.md](../../../CONTRIBUTING.md)。

## 授權條款

本專案採用 MIT 授權條款，詳情請參閱 [LICENSE](../../../LICENSE) 檔案。

## 作者

Thomas Vincent

## 致謝

- [CoinGecko](https://www.coingecko.com/) 提供免費的加密貨幣 API
- [Nagios 外掛程式開發指南](https://nagios-plugins.org/doc/guidelines.html)
