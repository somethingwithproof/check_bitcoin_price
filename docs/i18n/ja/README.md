# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · **日本語** · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

設定可能な警告およびクリティカルしきい値を用いて Bitcoin 価格を監視する Nagios/Icinga プラグインです。

## 機能

- 複数通貨（USD、EUR、GBP など）での Bitcoin 価格の監視
- 設定可能な警告（warning）およびクリティカル（critical）しきい値（上限および下限）
- パフォーマンスデータ付きの標準 Nagios プラグイン出力
- CoinGecko API を使用（無料、API キー不要）
- カスタム API エンドポイントのサポート
- 設定可能なタイムアウト
- ベンダーのタイムスタンプを使用したクオートの鮮度チェック（デフォルト上限は 1 時間）
- レート制限および一時的な API 障害に対する回数制限付きリトライ
- すべての試行で共有される単一のデッドラインと、各レスポンスに対する 64 KiB の上限
- 24 時間変動率（絶対値）に基づくオプションのアラート
- 価格しきい値、リクエスト所要時間、クオート経過時間をパフォーマンスデータに出力

## インストール

### GitHub Releases から

[GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) から `.deb`、`.rpm`、`.tar.gz`、wheel、および `SHA256SUMS` ファイルをダウンロードします。`sha256sum --ignore-missing --check SHA256SUMS` でダウンロードファイルを検証してください。1.0.0 以降のリリースには署名付きのビルド来歴（build provenance）も付与されています。`gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` を実行して、アセットがこのリポジトリのリリースワークフローから生成されたことを確認できます。

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

選択したリリースのファイル名を使用してください。ネイティブパッケージは `/usr/bin/check_bitcoin_price` と `/usr/lib/nagios/plugins/check_bitcoin_price` をインストールします。RPM では `/usr/lib64/nagios/plugins/check_bitcoin_price` も提供されます。パッケージ版のコマンドは Python を分離モード（isolated mode）で実行するため、`PYTHONPATH` や作業ディレクトリ内のモジュールを無視します。Python と `requests` の依存関係はシステムのパッケージマネージャーが解決します。これらにはアーキテクチャ非依存の Python コードが含まれており、Python 3.12 以降を提供するディストリビューションが必要です。

### ソースから

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### 開発用

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## 使い方

### 基本的な使い方

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### しきい値の指定

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### 個別のしきい値

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### 通貨の変更

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### カスタムタイムアウト

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### 鮮度チェックとリトライ予算

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

ベンダーのタイムスタンプを含むクオートは、デフォルトで経過時間が 1 時間以内でなければなりません。価格のみを返すエンドポイントは、`--max-age` が指定されていない場合は引き続き利用可能です。`--max-age` を指定した場合、ベンダーのタイムスタンプが欠落している、無効である、未来の時刻である、または古い場合は `UNKNOWN` を返します。プラグインはローカルの取得時刻をベンダーのクオート時刻の代わりに使用しません。経過時間が上限とちょうど一致するタイムスタンプは許容されます。未来のタイムスタンプは常に拒否されます。

デフォルトでは 1 回のリトライが許可されています。リトライ対象は接続エラー、タイムアウト、および HTTP 408/429/500/502/503/504 レスポンスのみです。バックオフは 0.5 秒から始まり、以降のリトライごとに倍増します。`Retry-After` の秒数および HTTP 日時はこれより優先されます。すべての試行、レスポンスの読み取り、JSON デコード、およびリトライ待機は、`--timeout` の時間予算を共有します。リトライ待機時間が予算内に収まらない場合は直ちに `UNKNOWN` を返し、タイムアウトではなく、リトライのトリガーとなった障害（`HTTP 429` や `ConnectionError` など）を報告します。認証エラー、その他の恒久的な HTTP エラー、不正な JSON、およびデコード後のデータが 64 KiB を超えるレスポンスはリトライされません。リトライを無効にするには `--retries 0` を使用してください。

### フォールバッククオートソース

CoinGecko 互換エンドポイントを指定する反復可能な `--fallback-url URL` オプションを使用します。たとえば、`--fallback-url https://quotes.example.org/simple/price` のように追加します。各ソースには、リトライを含めて残りのリクエスト期限が均等に割り当てられます。一時的な障害が発生した場合、またはリトライ遅延がその割り当て時間を超える場合は、次のソースへ進みます。TLS 検証エラー、恒久的な HTTP エラー、および無効なクオートは UNKNOWN を返します。各クオートレスポンスはデコード後 64 KiB に制限されます。フォールバックが設定されている場合、ステータスには URL を出力せずに、応答したソースが `primary`、`fallback1` のように識別表示されます。

### 短時間ウィンドウの価格変動

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

監視ユーザーに対して、ローカルの Linux または macOS ファイルシステム上のプライベートで書き込み可能な状態ディレクトリを割り当ててください。チェック間で同じディレクトリの `.lock` ファイルを保持し、ウィンドウごとに個別の状態ファイルを使用してください。ファイル内では通貨ごとに独立した履歴が保持されます。デフォルトのウィンドウは 3600 秒です。各有効なクオートには、そのウィンドウ内および経過時間上限（`--max-age` で別値を設定しない限り 1 時間）内のベンダータイムスタンプが必要です。プラグインは現在の価格を、そのウィンドウ内で最も古い過去の正の価格と比較し、実際の経過秒数を報告します。同じタイムスタンプが繰り返された場合は追加のサンプルは作成されません。最初のサンプル、期限切れの履歴、または破損した JSON の場合は新しいベースラインが開始され、比較可能なサンプルが得られるまでウィンドウメトリクスは unknown になります。他のアラートは引き続き適用されます。状態が書き込み不可の場合、状態ファイルまたはロックファイルがシンボリックリンクの場合、あるいは記録されている最新のサンプルより古いクオートを受け取った場合は UNKNOWN を返します。符号付きの `bitcoin_move_window` メトリクスは対称的な警告およびクリティカル範囲を使用します。上限値とちょうど等しい場合はアラートになりません。

プラグインはチェックごとに 1 回だけ状態ディレクトリを開き、そのディレクトリからの相対パスで処理を行うため、チェック中にパス要素が差し替えられてもロック、読み取り、書き込みのリダイレクトを防ぐことができます。パスのディレクトリ部分に含まれるシンボリックリンクはチェック開始時に辿られるため、macOS 上の `/var` のようなプラットフォームリンクも問題なく利用できます。したがって、状態ディレクトリとその上位ディレクトリは他のユーザーが書き込めないようにしておく必要があります。状態ファイルおよびロックファイルはモード 0600 で作成されます。

### 24時間変動率

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

変動しきい値は、選択した通貨における CoinGecko の符号付き 24 時間変動率の絶対値を測定します。変動率がしきい値とちょうど一致する場合はアラートになりません。両方のしきい値を指定する場合、警告しきい値はクリティカルしきい値以下である必要があります。必須の変動率データが欠落しているか無効な場合は `UNKNOWN` を返します。価格アラートと変動率アラートは組み合わせることができ、最も高い重大度が優先されます。重大度が同じ場合は価格が優先されます。

## コマンドラインオプション

| オプション | 説明 |
|--------|-------------|
| `-w`, `--warning` | 警告しきい値範囲（形式: LOW:HIGH） |
| `-c`, `--critical` | クリティカルしきい値範囲（形式: LOW:HIGH） |
| `--warning-low` | 下限価格の警告しきい値 |
| `--warning-high` | 上限価格の警告しきい値 |
| `--critical-low` | 下限価格のクリティカルしきい値 |
| `--critical-high` | 上限価格のクリティカルしきい値 |
| `--currency` | 2〜16 文字の英数字による通貨コード（デフォルト: usd） |
| `--timeout` | API リクエストとリトライの合計時間予算（秒単位、小数値可、デフォルト: 10） |
| `--retries` | 一時的障害に対する追加リトライ回数、0〜5（デフォルト: 1） |
| `--max-age` | ベンダーのクオート最大経過時間（秒単位）およびタイムスタンプ必須化（タイムスタンプ付きクオートのデフォルトは 3600） |
| `--warning-change` | 24 時間変動率（絶対値）の警告上限 |
| `--critical-change` | 24 時間変動率（絶対値）のクリティカル上限 |
| `--api-url` | プライマリ API URL |
| `--fallback-url` | 追加の互換エンドポイント（優先順に繰り返し指定可） |
| `--state-file` | JSON 価格変動履歴ファイル |
| `--move-window` | 変動ウィンドウ（秒単位、デフォルト: 3600） |
| `--warning-move`, `--critical-move` | ウィンドウ内の価格変動率（絶対値、パーセント）のしきい値 |
| `-v`, `--verbose` | 詳細出力を有効にする |
| `-V`, `--version` | バージョンを表示する |
| `-h`, `--help` | ヘルプメッセージを表示する |

## Nagios 設定

### コマンド定義

Nagios のリソースマクロ `$USER1$` にプラグインディレクトリを設定し（ネイティブパッケージでは `/usr/lib/nagios/plugins` を使用）、Nagios のコマンド設定に以下を追加します。

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### サービス定義

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

## 終了コード

無効な引数、0 以下のタイムアウト、無効なしきい値範囲、および不正な形式の API 価格は `UNKNOWN`（終了コード 3）を返します。しきい値は有限かつ非負の数値で、各下限が上限以下でなければなりません。通貨は 2〜16 文字の英数字である必要があります。無効な設定は API に接続する前に拒否されます。価格は有限かつ非負で、JSON 数値または `"43521.5"` のような単純な 10 進数文字列として与えられる必要があります。要求した通貨が含まれないレスポンスは `Response has no EUR price` のように通貨名を示します。無効なレスポンスではパフォーマンスデータは出力されません。詳細な診断出力は stderr に送られるため、stdout には監視ステータス行のみが 1 行で出力されます。

| コード | ステータス | 説明 |
|------|--------|-------------|
| 0 | OK | 価格は許容範囲内です |
| 1 | WARNING | 価格が警告しきい値を超えました |
| 2 | CRITICAL | 価格がクリティカルしきい値を超えました |
| 3 | UNKNOWN | エラーが発生しました（API 障害、タイムアウトなど） |

## パフォーマンスデータ

このプラグインは、標準の Nagios 形式でパフォーマンスデータを出力します。

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

価格のパフォーマンスデータには、設定された警告/クリティカル範囲と最小値 0 が含まれます。しきい値は丸めや指数表記をせず完全な 10 進表記で出力されるため、`14500000:16250000` のような大きな値もそのまま解析可能です。リクエスト時間にはすべての試行とバックオフが含まれます。クオート経過時間はベンダーが有効なタイムスタンプを提供した場合にのみ出力され、日次変動率は利用可能な場合に出力されます。変動率の範囲は 0 を中心に対称です。データが無効または古い場合は、価格パフォーマンスデータなしで `UNKNOWN` を出力します。これらのメトリクスは PNP4Nagios、Grafana、InfluxDB などのグラフ作成ツールで利用できます。

## API

このプラグインはデフォルトで [CoinGecko API](https://www.coingecko.com/en/api) を使用します。無料で利用でき、API キーは不要です（レート制限があります）。

カスタムエンドポイントは同じレスポンス形式を使用する必要があります。価格は `bitcoin.<currency>`、UNIX タイムスタンプ（秒）は `bitcoin.last_updated_at`、符号付き 24 時間変動率は `bitcoin.<currency>_24h_change` です。`--max-age` と変動率しきい値が指定されていない場合は、価格のみが必須となります。タイムスタンプが存在する場合は引き続きチェックされ、未来の時刻や 1 時間以上前であってはなりません。デコード後のレスポンスは 64 KiB 以内に収まる必要があります。

対応通貨には usd、eur、gbp、jpy、aud、cad、chf、cny ほか多数が含まれます。

## セキュリティ

現在のコードには以下の対策が実装されています。これらは不正な挙動をするエンドポイントやローカルユーザーが監視ホストに及ぼしうる影響を制限するものであり、クオート自体の信頼性を保証するものではありません。

- HTTPS 証明書は `requests` のデフォルト設定で検証され、検証を無効化するオプションはありません。平文の `http://` を使用するカスタム `--api-url` にはこの保護がありません。
- DNS、接続、読み取り、リトライ、およびバックオフは `--timeout` の期限を共有します。データ送信が低速なピアによって期限を延長させることはできません。
- 各レスポンスは展開後 64 KiB に制限され、リダイレクトのレスポンスボディは読み取らずに破棄されます。
- カスタム `--api-url` に認証情報が含まれる可能性があるため、リクエスト失敗時は HTTP ステータスまたはエラークラスのみを出力します。
- `.deb` および `.rpm` によってインストールされるコマンドは、Python を分離モード（isolated mode）で実行します。`PYTHONPATH`、ユーザー site ディレクトリ、および作業ディレクトリ内のモジュールを無視します。`pip` でインストールした場合は標準のコンソールスクリプトを使用し、インストール先の環境に従います。
- 変動状態は、チェックごとに 1 回開いたディレクトリを基準に、状態ファイル名またはロックファイル名にあるシンボリックリンクを辿らずに読み書きされます。
- リリースアセットには `SHA256SUMS` に加えてビルド来歴の証明（attestation）が付与されています。[GitHub Releases から](#github-releases-から)を参照してください。

## 1.0.0 からのアップグレード

2.0.0 では以下の変更が含まれます。

- ベンダーのタイムスタンプが 1 時間より古いクオートは、より大きな `--max-age` が指定されない限り `UNKNOWN` を返します。タイムスタンプを返さないエンドポイントは影響を受けません。
- `--currency` は 2〜16 文字の英数字のみを受け付けます。
- 桁区切り文字や前後の空白を含む数値文字列は拒否されます。
- 時間予算内に収まらないリトライ待機が発生した場合、`API request timed out` ではなく原因となった障害を報告します。
- ネイティブパッケージは `PYTHONPATH` を参照しなくなりました。
- 100 万以上のしきい値が、パフォーマンスデータ内で指数表記ではなく通常の 10 進数として出力されます。

## ローカライズ

CLI のヘルプ、バリデーションエラー、およびプラグインのステータス説明は、同梱の標準ライブラリ読み込みカタログを使用して 45 ロケール（`en`、`de`、`es`、`fr`、`it`、`pt-BR`、`nl`、`ru`、`uk`、`ja`、`ko`、`zh-CN`、`zh-TW`、`ar`、`hi`、`pl`、`tr`、`sv`、`vi`、`id`、`af-ZA`、`am-ET`、`ar-EG`、`ar-MA`、`fr-MA`、`fr-SN`、`ha-NG`、`ig-NG`、`mg-MG`、`rw-RW`、`so-SO`、`sw-KE`、`xh-ZA`、`yo-NG`、`zu-ZA`、`bn`、`fa`、`he`、`mr`、`ta`、`te`、`th`、`ur`、`ms`、`fil`）に対応しています。ロケールの解決は `--lang`、`LC_ALL`、`LC_MESSAGES`、`LANG` の順で確認し、該当がない場合は `en` にフォールバックします。Nagios のステータス接頭辞（`OK`、`WARNING`、`CRITICAL`、`UNKNOWN`）およびパフォーマンスデータはすべてのロケールで変更されません。

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## 開発

[mise](https://mise.jdx.dev/getting-started.html) をインストールしてから、上記の開発用セットアップを実行してください。`mise.toml` は Python と uv のバージョンを固定しています。開発ツールは `pyproject.toml` で宣言され、コミット済みの `uv.lock` で解決されています。

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

セットアップ後にコミットフックをインストールしてください。

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

依存関係を更新するには `mise exec -- uv add --dev <tool>` または `mise exec -- uv add <dependency>` を使用し、`pyproject.toml` と `uv.lock` の両方をコミットしてください。

CI では Linux 上の Python 3.12 および 3.13 と、macOS 上の Python 3.13 をチェックします。すべての PR でパッケージ検証、依存関係監査、CodeQL も実行され、Ubuntu 上での `.deb` インストールと Fedora 上での `.rpm` インストールが検証されます。ビルドされた配布物は CI 実行時の `distributions` アーティファクトとして利用できます。

パッケージおよび CLI のバージョンは `check_bitcoin_price/__init__.py` から取得されます。バージョンの更新や GitHub リリースアセットの自動公開については、[リリースプロセス](../../../CONTRIBUTING.md#releases)を参照してください。

## コントリビューション

開発ワークフローおよび Signed-off-by 付きコミットの要件については、[CONTRIBUTING.md](../../../CONTRIBUTING.md) を参照してください。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](../../../LICENSE) ファイルを参照してください。

## 作者

Thomas Vincent

## 謝辞

- 無料の暗号資産 API を提供している [CoinGecko](https://www.coingecko.com/)
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
