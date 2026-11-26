# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · **한국어** · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

warning 및 critical 임계값을 구성하여 Bitcoin 가격을 모니터링하는 Nagios/Icinga 플러그인입니다.

## 주요 기능

- 다양한 통화(USD, EUR, GBP 등)로 Bitcoin 가격 모니터링
- warning 및 critical 임계값 구성 가능(상한 및 하한)
- 성능 데이터를 포함한 표준 Nagios 플러그인 출력
- CoinGecko API 사용(무료, API 키 불필요)
- 사용자 지정 API 엔드포인트 지원
- 타임아웃 구성 가능
- 공급자 타임스탬프를 사용한 시세 최신성 검사(기본 제한 시간 1시간)
- 요청 속도 제한 및 일시적인 API 장애에 대한 제한된 재시도
- 모든 시도에 대한 단일 마감 시간 및 각 응답당 64 KiB 크기 제한
- 24시간 절대 변동률(%)에 대한 선택적 알림
- 성능 데이터에 가격 임계값, 요청 소요 시간 및 시세 경과 시간 포함

## 설치

<a name="from-github-releases"></a>

### GitHub 릴리스에서 설치

[GitHub 릴리스](https://github.com/somethingwithproof/check_bitcoin_price/releases)에서 `.deb`, `.rpm`, `.tar.gz`, wheel 및 `SHA256SUMS` 파일을 다운로드합니다. `sha256sum --ignore-missing --check SHA256SUMS`로 다운로드를 검증합니다. 1.0.0 이후 릴리스에는 서명된 빌드 출처(provenance)도 포함되므로 `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`로 자산이 이 저장소의 릴리스 워크플로에서 생성되었는지 확인합니다.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

선택한 릴리스의 파일 이름을 사용하세요. 네이티브 패키지는 `/usr/bin/check_bitcoin_price`와 `/usr/lib/nagios/plugins/check_bitcoin_price`를 설치하며, RPM은 `/usr/lib64/nagios/plugins/check_bitcoin_price`도 제공합니다. 패키징된 명령어는 격리 모드(isolated mode)로 Python을 실행하므로 `PYTHONPATH`와 작업 디렉터리의 모듈을 무시하며, 시스템 패키지 관리자가 Python 및 `requests` 의존성을 해결합니다. 패키지에는 아키텍처에 독립적인 Python 코드가 포함되어 있으며 Python 3.12 이상을 제공하는 배포판이 필요합니다.

### 소스에서 설치

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### 개발용 설치

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## 사용법

### 기본 사용법

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### 임계값 설정

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### 개별 임계값 설정

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### 다른 통화 사용

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### 사용자 지정 타임아웃

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### 최신성 검사 및 재시도 예산

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

공급자 타임스탬프가 포함된 시세는 기본적으로 최대 1시간 이내여야 합니다.
가격만 반환하는 엔드포인트는 `--max-age`가 없을 때 계속 사용할 수 있습니다.
`--max-age`가 지정된 경우 공급자 타임스탬프가 누락되었거나, 유효하지 않거나, 미래 시점이거나, 오래되었으면
`UNKNOWN`을 반환하며, 플러그인은 공급자의 시세 시각을 로컬 조회 시각으로
대체하지 않습니다. 제한 시간과 정확히 일치하는 타임스탬프는 허용됩니다. 미래 시점의
타임스탬프는 항상 거부됩니다.

기본값은 1회 재시도를 허용합니다. 연결 오류, 타임아웃 및 HTTP
408/429/500/502/503/504 응답만 재시도합니다. 백오프(backoff)는 0.5초부터 시작하여
이후 재시도마다 2배씩 증가하며, `Retry-After` 초 단위 값과 HTTP 날짜가
우선 적용됩니다. 모든 시도, 응답 읽기, JSON 디코딩 및 재시도 대기 시간은
`--timeout` 예산을 공유합니다. 남은 예산에 맞지 않는 재시도 대기가 발생하면 즉시 `UNKNOWN`을 반환하고
타임아웃이 아니라 `HTTP 429` 또는 `ConnectionError`와 같이 재시도를 유발한 실패 원인을
보고합니다. 인증 실패, 기타 영구적인 HTTP 오류, 유효하지 않은
JSON, 그리고 디코딩된 데이터가 64 KiB를 초과하는 응답은 재시도하지 않습니다. 재시도를 비활성화하려면
`--retries 0`을 사용하세요.

### 대체 시세 소스

CoinGecko 호환 엔드포인트와 함께 반복 가능한 `--fallback-url URL` 옵션을 사용합니다.
예를 들어 `--fallback-url https://quotes.example.org/simple/price`를 추가할 수 있습니다.
각 소스는 재시도를 포함하여 남은 요청 마감 시간을 균등하게
배분받습니다. 일시적인 장애가 발생하거나 재시도 지연 시간이 배분된 시간보다 길면
다음 소스로 넘어갑니다. TLS 검증 실패, 영구적인 HTTP 오류 및 유효하지 않은
시세는 UNKNOWN을 반환합니다. 각 시세 응답은 디코딩된 데이터 기준 64 KiB로 제한됩니다.
대체 소스가 구성된 경우, 상태 출력은 URL을 표시하지 않고 응답한 소스를
`primary`, `fallback1` 등으로 식별합니다.

### 단기 구간 변동

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

모니터링 사용자에게 로컬 Linux 또는 macOS 파일시스템의 비공개 쓰기 가능 상태 디렉터리를 제공하세요.
검사 사이에도 같은 위치의 `.lock` 파일을 그대로 유지해야 합니다. 구간(window)마다
별도의 상태 파일을 사용하세요. 상태 파일 내부에서는 통화별로 독립적인 기록이 관리됩니다.
기본 구간은 3600초입니다. 유효한 각 시세에는 해당 구간과 최신성 제한(`--max-age`로 달리 설정하지 않은 경우
1시간) 이내의 공급자 타임스탬프가 필요합니다. 플러그인은 현재 가격을
해당 구간 내 가장 오래된 이전 양수 가격과 비교하고 실제 경과 초를
보고합니다. 중복된 타임스탬프는 추가 샘플을 생성하지 않습니다.
첫 번째 샘플이거나, 기록이 만료되었거나, JSON이 손상된 경우 새 기준선이 시작되며,
비교 가능한 샘플이 생길 때까지 구간 메트릭은 알 수 없음(unknown) 상태가 됩니다. 다른 알림은 계속
적용됩니다. 쓰기 불가능한 상태 파일, 심볼릭 링크인 상태 파일 또는 잠금 파일, 또는 기록된 최신 샘플보다 오래된
시세는 UNKNOWN을 반환합니다. 부호가 있는 `bitcoin_move_window` 메트릭은
대칭형 warning 및 critical 범위를 사용합니다. 제한값과 정확히 일치할 때는 알림이 발생하지 않습니다.

플러그인은 검사당 한 번 상태 디렉터리를 열고 이를 기준으로 상대 경로 작업을 수행하므로,
검사 도중 경로 구성 요소가 교체되더라도 잠금, 읽기 또는 쓰기를 다른 곳으로 리디렉션할 수
없습니다. 경로의 디렉터리 부분에 있는 심볼릭 링크는 검사가 시작될 때 따라가므로
macOS의 `/var` 같은 플랫폼 링크를 계속 사용할 수 있습니다. 따라서
상태 디렉터리와 그 상위 디렉터리는 다른 사용자가 쓸 수 없도록 설정해야 합니다.
상태 파일과 잠금 파일은 0600 권한으로 생성됩니다.

### 일일 변동률(%)

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

변동 임계값은 선택한 통화에서 CoinGecko가 제공하는 부호 있는 24시간
변동률(%)의 절댓값을 측정합니다. 변동 폭이 임계값과 정확히 일치할 때는 알림이
발생하지 않습니다. 두 임계값을 모두 지정하는 경우 warning은 critical을 초과할 수 없습니다.
필요한 변동 데이터가 누락되었거나 유효하지 않으면 `UNKNOWN`을 반환합니다. 가격 알림과 변동
알림을 함께 사용할 수 있으며, 가장 높은 심각도가 우선 적용되고 심각도가 같을 때는
가격 알림이 우선합니다.

## 명령줄 옵션

| 옵션 | 설명 |
|------|------|
| `-w`, `--warning` | Warning 임계값 범위 (형식: LOW:HIGH) |
| `-c`, `--critical` | Critical 임계값 범위 (형식: LOW:HIGH) |
| `--warning-low` | 하한 가격 Warning 임계값 |
| `--warning-high` | 상한 가격 Warning 임계값 |
| `--critical-low` | 하한 가격 Critical 임계값 |
| `--critical-high` | 상한 가격 Critical 임계값 |
| `--currency` | 2~16자의 영문자 또는 숫자로 된 통화 코드 (기본값: usd) |
| `--timeout` | 총 API 요청/재시도 예산(초, 소수점 값 포함, 기본값: 10) |
| `--retries` | 일시적 오류 시 추가 재시도 횟수, 0–5 (기본값: 1) |
| `--max-age` | 최대 공급자 시세 경과 시간(초) 및 타임스탬프 필수 지정(타임스탬프가 있는 시세의 기본값: 3600) |
| `--warning-change` | 24시간 절대 변동률(%) Warning 제한값 |
| `--critical-change` | 24시간 절대 변동률(%) Critical 제한값 |
| `--api-url` | 기본 API URL |
| `--fallback-url` | 추가 호환 엔드포인트(선호 순서대로 반복 지정) |
| `--state-file` | JSON 변동 기록 파일 |
| `--move-window` | 변동 구간(초, 기본값: 3600) |
| `--warning-move`, `--critical-move` | 절대 구간 변동 임계값(%) |
| `-v`, `--verbose` | 상세 출력 활성화 |
| `-V`, `--version` | 버전 표시 |
| `-h`, `--help` | 도움말 메시지 표시 |

## Nagios 구성

### 명령어 정의

Nagios 리소스 매크로 `$USER1$`을 플러그인 디렉터리로 설정합니다(네이티브 패키지는 `/usr/lib/nagios/plugins`를 사용). Nagios 명령어 구성에 다음을 추가합니다:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### 서비스 정의

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

### Icinga2 구성

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

## 종료 코드

잘못된 인수, 0 이하의 타임아웃, 잘못된 임계값 범위 및 잘못된 형식의
API 가격은 `UNKNOWN`(종료 코드 3)을 반환합니다. 임계값은 유한한 음이 아닌
숫자여야 하며 각 하한은 상한보다 클 수 없습니다. 통화 코드는
2~16자의 영문자 또는 숫자여야 합니다. 잘못된 구성은 API에 요청하기 전에
거부됩니다. 가격은 유한하고 음이 아니어야 하며 JSON 숫자 또는
`"43521.5"`와 같은 일반 10진수 문자열로 제공되어야 합니다. 요청한 통화가 없는 응답은
해당 통화 이름을 명시합니다(예: `Response has no EUR price`). 유효하지 않은 응답은
성능 데이터를 출력하지 않습니다. 상세 진단 메시지는 stderr로 출력되므로
stdout에는 단일 모니터링 상태 줄만 포함됩니다.

| 코드 | 상태 | 설명 |
|------|------|------|
| 0 | OK | 가격이 허용 범위 내에 있음 |
| 1 | WARNING | 가격이 warning 임계값을 초과함 |
| 2 | CRITICAL | 가격이 critical 임계값을 초과함 |
| 3 | UNKNOWN | 오류 발생 (API 실패, 타임아웃 등) |

## 성능 데이터

플러그인은 표준 Nagios 형식으로 성능 데이터를 출력합니다:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

가격 성능 데이터에는 구성된 warning/critical 범위와
최솟값 0이 포함됩니다. 임계값은 반올림되거나 지수 표기법으로 변환되지 않고 전체 10진수 표기법으로 출력되므로
`14500000:16250000`과 같은 큰 값도 파싱 가능한 상태로 유지됩니다. 요청 시간에는 모든 시도와 백오프 시간이 포함됩니다. 시세 경과 시간은
공급자가 유효한 타임스탬프를 제공한 경우에만 출력되며, 일일 변동률은 사용 가능한 경우
출력됩니다. 변동 범위는 0을 기준으로 대칭입니다. 유효하지 않거나 오래된 데이터는
가격 성능 데이터 없이 `UNKNOWN`을 생성합니다. 이러한 메트릭은
PNP4Nagios, Grafana 또는 InfluxDB와 같은 그래프 도구와 함께 사용할 수 있습니다.

## API

이 플러그인은 기본적으로 무료이며 API 키가 필요하지 않은 [CoinGecko API](https://www.coingecko.com/en/api)를 사용합니다. 요청 속도 제한이 적용됩니다.

사용자 지정 엔드포인트는 동일한 응답 형식을 사용해야 합니다. 가격은 `bitcoin.<currency>`,
UNIX 타임스탬프(초)는 `bitcoin.last_updated_at`, 부호 있는 일일 변동률(%)은
`bitcoin.<currency>_24h_change`입니다. `--max-age`와 변동 임계값이 없을 때는 가격만
필수입니다. 타임스탬프가 존재하는 경우 여전히 검사되며,
미래 시점이거나 1시간을 초과한 과거 시점이어서는 안 됩니다. 디코딩된 응답은 64 KiB 이내여야 합니다.

지원 통화에는 usd, eur, gbp, jpy, aud, cad, chf, cny 등이 포함됩니다.

## 보안

아래의 보안 조치는 현재 코드에 구현되어 있습니다. 이는 비정상적으로 동작하는 엔드포인트나 로컬 사용자가
모니터링 호스트에 미칠 수 있는 영향을 제한하지만, 시세 자체의 신뢰성을 보장하지는 않습니다.

- HTTPS 인증서는 `requests` 기본값으로 검증되며, 검증을 비활성화하는 옵션은
  없습니다. 일반 `http://`를 사용하는 사용자 지정 `--api-url`에는
  이러한 보호가 적용되지 않습니다.
- DNS, 연결, 읽기, 재시도 및 백오프는 `--timeout` 마감 시간을 공유합니다.
  데이터를 느리게 전송하는 피어가 이를 연장할 수 없습니다.
- 각 응답은 압축 해제 후 64 KiB로 제한되며 리디렉션 본문은
  읽지 않고 폐기됩니다.
- 사용자 지정 `--api-url`에 자격 증명이 포함될 수 있으므로 요청 실패 시
  HTTP 상태 코드나 오류 클래스만 출력합니다.
- `.deb` 및 `.rpm`으로 설치된 명령어는 격리 모드로 Python을 실행합니다.
  `PYTHONPATH`, 사용자 사이트 디렉터리 및 작업 디렉터리의 모듈을 무시합니다.
  `pip` 설치는 표준 콘솔 스크립트를 사용하며 설치된 환경을
  따릅니다.
- 변동 상태는 검사당 한 번 열린 디렉터리를 기준으로 상태 파일이나 잠금 파일 이름의
  심볼릭 링크를 따라가지 않고 읽고 씁니다.
- 릴리스 자산에는 `SHA256SUMS` 외에도 빌드 출처 증명이 포함됩니다.
  [GitHub 릴리스에서 설치](#from-github-releases)를 참조하세요.

## 1.0.0에서 업그레이드

다음 변경 사항은 2.0.0에 포함되어 있습니다.

- 더 큰 `--max-age`를 지정하지 않으면 공급자 타임스탬프가 1시간을 초과한 시세는 `UNKNOWN`을 반환합니다.
  타임스탬프를 반환하지 않는 엔드포인트는 영향을 받지 않습니다.
- `--currency`는 2~16자의 영문자 또는 숫자만 허용합니다.
- 자릿수 구분 기호나 앞뒤 공백이 있는 숫자 문자열은 거부됩니다.
- 예산에 맞지 않는 재시도 대기는 `API request timed out` 대신
  근본적인 실패 원인을 보고합니다.
- 네이티브 패키지는 더 이상 `PYTHONPATH`를 참조하지 않습니다.
- 100만 이상의 임계값은 성능 데이터에서 지수 표기법 대신
  일반 10진수로 표시됩니다.

## 다국어 지원

CLI 도움말, 유효성 검사 오류 및 플러그인 상태 설명은 표준 라이브러리로 로드되는 내장 카탈로그를 사용하여 45개 로캘(`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`)을 지원합니다. 로캘 결정은 `--lang`을 먼저 확인하고, 이어서 `LC_ALL`, `LC_MESSAGES`, `LANG` 순으로 확인하며, 기본값은 `en`입니다. Nagios 상태 접두사(`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`)와 성능 데이터는 모든 로캘에서 동일하게 유지됩니다.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## 개발

[mise](https://mise.jdx.dev/getting-started.html)를 설치한 후 위의 개발 환경 설정을 실행하세요. `mise.toml`은 Python 및 uv 버전을 고정합니다. 개발 도구는 `pyproject.toml`에 선언되어 있으며 커밋된 `uv.lock`에서 해결됩니다.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

설정 후 커밋 훅을 설치하세요:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

의존성을 업데이트하려면 `mise exec -- uv add --dev <tool>` 또는 `mise exec -- uv add <dependency>`를 사용하고 `pyproject.toml`과 `uv.lock`을 모두 커밋하세요.

CI는 Linux에서 Python 3.12 및 3.13을, macOS에서 Python 3.13을 검사합니다. 또한 모든 PR은 패키지 검증, 의존성 감사 및 CodeQL을 실행하며 Ubuntu에 `.deb`를, Fedora에 `.rpm`을 설치하여 테스트합니다. 빌드된 배포판은 CI 실행의 `distributions` 아티팩트로 제공됩니다.

패키지 및 CLI 버전은 `check_bitcoin_price/__init__.py`에서 가져옵니다. 버전 업데이트 및 GitHub 릴리스 자산의 자동 게시에 대해서는 [릴리스 프로세스](../../../CONTRIBUTING.md#releases)를 참조하세요.

## 기여하기

개발 워크플로 및 서명된 커밋(signed-off commit) 요구 사항은 [CONTRIBUTING.md](../../../CONTRIBUTING.md)를 참조하세요.

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 배포됩니다. 자세한 내용은 [LICENSE](../../../LICENSE) 파일을 참조하세요.

## 작성자

Thomas Vincent

## 감사의 말

- 무료 암호화폐 API를 제공하는 [CoinGecko](https://www.coingecko.com/)
- [Nagios 플러그인 개발 가이드라인](https://nagios-plugins.org/doc/guidelines.html)
