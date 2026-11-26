# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · **Tiếng Việt** · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Một plugin Nagios/Icinga dùng để giám sát giá Bitcoin với các ngưỡng cảnh báo và nghiêm trọng có thể cấu hình.

## Tính năng

- Giám sát giá Bitcoin bằng nhiều loại tiền tệ (USD, EUR, GBP, v.v.)
- Ngưỡng cảnh báo và nghiêm trọng có thể cấu hình (mức cao và mức thấp)
- Đầu ra chuẩn của plugin Nagios kèm dữ liệu hiệu suất
- Sử dụng CoinGecko API (miễn phí, không cần khóa API)
- Hỗ trợ các endpoint API tùy chỉnh
- Thời gian chờ có thể cấu hình
- Kiểm tra độ mới của báo giá bằng dấu thời gian từ nhà cung cấp, với giới hạn mặc định là một giờ
- Thử lại có giới hạn đối với giới hạn tốc độ và lỗi API tạm thời
- Một thời hạn duy nhất cho tất cả các lần thử và giới hạn 64 KiB cho mỗi phản hồi
- Cảnh báo tùy chọn theo mức biến động phần trăm tuyệt đối trong 24 giờ
- Ngưỡng giá, thời lượng yêu cầu và tuổi báo giá trong dữ liệu hiệu suất

## Cài đặt

### Từ GitHub Releases

Tải các tệp `.deb`, `.rpm`, `.tar.gz`, wheel và `SHA256SUMS` từ [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Xác minh tệp tải về bằng lệnh `sha256sum --ignore-missing --check SHA256SUMS`. Các bản phát hành sau 1.0.0 cũng đi kèm bằng chứng dựng đã ký; xác nhận tài nguyên đến từ quy trình phát hành của kho lưu trữ này bằng lệnh `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Sử dụng tên tệp từ bản phát hành đã chọn. Các gói gốc cài đặt `/usr/bin/check_bitcoin_price` và `/usr/lib/nagios/plugins/check_bitcoin_price`; gói RPM cũng cung cấp `/usr/lib64/nagios/plugins/check_bitcoin_price`. Lệnh được đóng gói chạy Python ở chế độ cô lập, nên nó bỏ qua `PYTHONPATH` và các mô-đun trong thư mục làm việc; trình quản lý gói của hệ thống sẽ giải quyết các phụ thuộc Python và `requests`. Các gói này chứa mã Python độc lập với kiến trúc và yêu cầu bản phân phối cung cấp Python 3.12 trở lên.

### Từ mã nguồn

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Dành cho phát triển

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Cách sử dụng

### Sử dụng cơ bản

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Với các ngưỡng

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Các ngưỡng riêng lẻ

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Tiền tệ khác

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Thời gian chờ tùy chỉnh

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Độ mới của dữ liệu và ngân sách thử lại

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Báo giá có dấu thời gian của nhà cung cấp mặc định chỉ được cũ tối đa một giờ.
Các endpoint chỉ trả về giá vẫn dùng được khi không có `--max-age`.
Khi dùng `--max-age`, dấu thời gian của nhà cung cấp bị thiếu, không hợp lệ, nằm trong tương lai hoặc quá cũ sẽ trả về
`UNKNOWN`; plugin không thay thế thời gian lấy dữ liệu cục bộ cho thời gian báo giá của
nhà cung cấp. Dấu thời gian đúng bằng giới hạn tuổi vẫn được chấp nhận. Dấu thời gian trong tương lai
luôn bị từ chối.

Mặc định cho phép thử lại một lần. Chỉ các lỗi kết nối, hết thời gian chờ và phản hồi HTTP
408/429/500/502/503/504 mới được thử lại. Thời gian chờ tăng dần bắt đầu từ 0,5 giây và
tăng gấp đôi cho các lần thử lại tiếp theo; giá trị giây `Retry-After` và ngày HTTP được
ưu tiên áp dụng. Tất cả các lần thử, đọc phản hồi, giải mã JSON và thời gian chờ thử lại đều dùng chung
ngân sách `--timeout`. Nếu thời gian chờ thử lại không còn đủ trong ngân sách, plugin trả về `UNKNOWN` ngay lập tức
và báo cáo lỗi đã kích hoạt việc thử lại đó, chẳng hạn như `HTTP 429` hoặc `ConnectionError`,
chứ không báo hết thời gian chờ. Lỗi xác thực, các lỗi HTTP cố định khác, JSON không hợp lệ
và phản hồi lớn hơn 64 KiB dữ liệu đã giải mã sẽ không được thử lại. Dùng
`--retries 0` để tắt tính năng thử lại.

### Nguồn báo giá dự phòng

Sử dụng các tùy chọn `--fallback-url URL` có thể lặp lại với các endpoint tương thích với CoinGecko.
Ví dụ, thêm `--fallback-url https://quotes.example.org/simple/price`.
Mỗi nguồn nhận được một phần bằng nhau của thời hạn yêu cầu còn lại, bao gồm cả các
lần thử lại của nó. Lỗi tạm thời hoặc độ trễ thử lại dài hơn phần thời gian đó sẽ chuyển sang
nguồn tiếp theo. Lỗi xác minh TLS, lỗi HTTP cố định và báo giá không hợp lệ
sẽ trả về UNKNOWN. Mỗi phản hồi báo giá bị giới hạn ở 64 KiB dữ liệu đã giải mã.
Khi các nguồn dự phòng được cấu hình, trạng thái sẽ xác định nguồn trả lời là
`primary`, `fallback1`, v.v., mà không in URL của nguồn đó.

### Biến động trong cửa sổ thời gian ngắn

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Cấp cho người dùng giám sát một thư mục trạng thái có quyền ghi riêng tư trên hệ thống tệp cục bộ của Linux hoặc
macOS. Giữ nguyên tệp `.lock` đi kèm giữa các lần kiểm tra. Sử dụng một
tệp trạng thái riêng cho mỗi cửa sổ thời gian. Các loại tiền tệ có lịch sử độc lập bên trong tệp đó.
Cửa sổ mặc định là 3600 giây. Mỗi báo giá hợp lệ cần có dấu thời gian của nhà cung cấp
nằm trong cửa sổ và trong giới hạn tuổi, mặc định là một giờ trừ khi `--max-age` đặt
giá trị khác. Plugin so sánh giá hiện tại
với giá dương cũ nhất trước đó trong cửa sổ đó và báo cáo
số giây thực tế đã trôi qua. Các dấu thời gian lặp lại không tạo thêm mẫu mới.
Mẫu đầu tiên, lịch sử đã hết hạn hoặc JSON bị hỏng sẽ bắt đầu một mốc cơ sở mới; chỉ số
cửa sổ sẽ ở trạng thái unknown cho đến khi có mẫu để so sánh. Các cảnh báo khác vẫn
được áp dụng. Trạng thái không thể ghi, tệp trạng thái hoặc tệp khóa là liên kết tượng trưng, hoặc báo giá cũ hơn
mẫu mới nhất đã ghi nhận sẽ trả về UNKNOWN. Chỉ số `bitcoin_move_window` có dấu
sử dụng các khoảng cảnh báo và nghiêm trọng đối xứng. Giá trị bằng đúng giới hạn sẽ không kích hoạt cảnh báo.

Plugin mở thư mục trạng thái một lần cho mỗi lần kiểm tra và thao tác tương đối với thư mục đó, nên
một thành phần đường dẫn bị thay thế trong quá trình kiểm tra không thể chuyển hướng việc khóa, đọc
hoặc ghi. Các liên kết tượng trưng trong phần thư mục của đường dẫn vẫn được đi theo khi
bắt đầu kiểm tra, giúp các liên kết nền tảng như `/var` trên macOS vẫn sử dụng được. Do đó,
thư mục trạng thái và các thư mục cha của nó không được phép cho người dùng
khác ghi. Các tệp trạng thái và tệp khóa được tạo với chế độ quyền 0600.

### Biến động phần trăm hằng ngày

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Các ngưỡng biến động đo giá trị tuyệt đối của mức thay đổi phần trăm có dấu trong 24 giờ của CoinGecko
theo loại tiền tệ đã chọn. Mức thay đổi đúng bằng ngưỡng sẽ
không kích hoạt cảnh báo. Nếu cung cấp cả hai ngưỡng, ngưỡng cảnh báo không được vượt quá ngưỡng nghiêm trọng.
Dữ liệu thay đổi bắt buộc bị thiếu hoặc không hợp lệ sẽ trả về `UNKNOWN`. Có thể kết hợp cảnh báo giá và
cảnh báo biến động; mức độ nghiêm trọng cao nhất sẽ được ưu tiên, và cảnh báo giá được ưu tiên hơn
khi hai mức độ bằng nhau.

## Tùy chọn dòng lệnh

| Tùy chọn | Mô tả |
|----------|-------|
| `-w`, `--warning` | Khoảng ngưỡng cảnh báo (định dạng: LOW:HIGH) |
| `-c`, `--critical` | Khoảng ngưỡng nghiêm trọng (định dạng: LOW:HIGH) |
| `--warning-low` | Ngưỡng cảnh báo cho giá thấp |
| `--warning-high` | Ngưỡng cảnh báo cho giá cao |
| `--critical-low` | Ngưỡng nghiêm trọng cho giá thấp |
| `--critical-high` | Ngưỡng nghiêm trọng cho giá cao |
| `--currency` | Mã tiền tệ gồm 2-16 chữ cái hoặc chữ số (mặc định: usd) |
| `--timeout` | Tổng ngân sách yêu cầu/thử lại API tính bằng giây, bao gồm giá trị thập phân (mặc định: 10) |
| `--retries` | Số lần thử lại bổ sung cho lỗi tạm thời, 0–5 (mặc định: 1) |
| `--max-age` | Tuổi tối đa của báo giá từ nhà cung cấp tính bằng giây và bắt buộc phải có dấu thời gian; báo giá có dấu thời gian mặc định là 3600 |
| `--warning-change` | Giới hạn cảnh báo cho biến động phần trăm tuyệt đối trong 24 giờ |
| `--critical-change` | Giới hạn nghiêm trọng cho biến động phần trăm tuyệt đối trong 24 giờ |
| `--api-url` | URL API chính |
| `--fallback-url` | Endpoint tương thích bổ sung; lặp lại theo thứ tự ưu tiên |
| `--state-file` | Tệp JSON lưu lịch sử biến động |
| `--move-window` | Cửa sổ biến động tính bằng giây (mặc định: 3600) |
| `--warning-move`, `--critical-move` | Ngưỡng biến động tuyệt đối trong cửa sổ tính theo phần trăm |
| `-v`, `--verbose` | Bật đầu ra chi tiết |
| `-V`, `--version` | Hiển thị phiên bản |
| `-h`, `--help` | Hiển thị thông báo trợ giúp |

## Cấu hình Nagios

### Định nghĩa lệnh

Đặt macro tài nguyên Nagios `$USER1$` thành thư mục plugin (các gói gốc sử dụng `/usr/lib/nagios/plugins`). Thêm vào cấu hình lệnh Nagios của bạn:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Định nghĩa dịch vụ

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

### Cấu hình Icinga2

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

## Mã thoát

Tham số không hợp lệ, thời gian chờ không dương, khoảng ngưỡng không hợp lệ và giá từ API sai định dạng
sẽ trả về `UNKNOWN` (mã thoát 3). Ngưỡng phải là số hữu hạn, không âm,
với mỗi cận dưới không lớn hơn cận trên của nó. Mã tiền tệ phải
gồm 2-16 chữ cái hoặc chữ số. Cấu hình không hợp lệ bị từ chối trước khi liên hệ
với API. Giá phải hữu hạn và không âm, được cung cấp dưới dạng số JSON hoặc chuỗi
thập phân thuần túy như `"43521.5"`. Phản hồi không có loại tiền tệ được yêu cầu
sẽ nêu rõ tên tiền tệ đó, ví dụ `Response has no EUR price`. Phản hồi không hợp lệ không xuất
dữ liệu hiệu suất. Thông tin chẩn đoán chi tiết được ghi ra stderr
để stdout chỉ chứa một dòng trạng thái giám sát duy nhất.

| Mã | Trạng thái | Mô tả |
|----|------------|-------|
| 0 | OK | Giá nằm trong phạm vi chấp nhận được |
| 1 | WARNING | Giá đã vượt ngưỡng cảnh báo |
| 2 | CRITICAL | Giá đã vượt ngưỡng nghiêm trọng |
| 3 | UNKNOWN | Đã xảy ra lỗi (lỗi API, hết thời gian chờ, v.v.) |

## Dữ liệu hiệu suất

Plugin xuất dữ liệu hiệu suất theo định dạng chuẩn của Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Dữ liệu hiệu suất giá bao gồm các khoảng cảnh báo/nghiêm trọng đã cấu hình và giá trị
tối thiểu bằng không. Các ngưỡng được in ở dạng ký pháp thập phân đầy đủ, không bao giờ làm tròn
hoặc dùng dạng số mũ, nhờ đó các giá trị lớn như `14500000:16250000` vẫn có thể phân tích được. Thời gian yêu cầu bao gồm tất cả các lần thử và thời gian backoff. Tuổi báo giá chỉ
được xuất ra khi nhà cung cấp cung cấp dấu thời gian hợp lệ; biến động hằng ngày được xuất ra
khi có sẵn. Các khoảng biến động đối xứng quanh số không. Dữ liệu không hợp lệ hoặc quá cũ
sẽ trả về `UNKNOWN` mà không có dữ liệu hiệu suất giá. Các chỉ số này có thể được sử dụng với
các công cụ vẽ đồ thị như PNP4Nagios, Grafana hoặc InfluxDB.

## API

Theo mặc định, plugin này sử dụng [CoinGecko API](https://www.coingecko.com/en/api), hoàn toàn miễn phí và không yêu cầu khóa API. Có áp dụng giới hạn tốc độ.

Các endpoint tùy chỉnh phải sử dụng cùng cấu trúc phản hồi: `bitcoin.<currency>` cho
giá, `bitcoin.last_updated_at` cho dấu thời gian UNIX tính bằng giây và
`bitcoin.<currency>_24h_change` cho biến động phần trăm hằng ngày có dấu. Chỉ cần có giá
khi `--max-age` và các ngưỡng biến động không được sử dụng. Nếu có dấu thời gian,
nó vẫn được kiểm tra: không được nằm trong tương lai hoặc cũ hơn một
giờ. Phản hồi đã giải mã phải nằm gọn trong 64 KiB.

Các loại tiền tệ được hỗ trợ bao gồm: usd, eur, gbp, jpy, aud, cad, chf, cny và nhiều loại khác.

## Bảo mật

Các biện pháp dưới đây được triển khai trong mã nguồn hiện tại. Chúng giới hạn những gì một endpoint hoạt động sai hoặc một người dùng cục bộ có thể làm đối với
máy chủ giám sát; chúng không làm cho bản thân báo giá trở nên đáng tin cậy.

- Chứng chỉ HTTPS được xác minh theo mặc định của `requests`, và không có tùy chọn nào
  tắt việc xác minh này. Một `--api-url` tùy chỉnh sử dụng `http://` thuần túy sẽ không có
  sự bảo vệ như vậy.
- DNS, kết nối, đọc dữ liệu, thử lại và backoff dùng chung thời hạn `--timeout`. Một
  máy chủ gửi dữ liệu chậm không thể kéo dài thời hạn này.
- Mỗi phản hồi bị giới hạn ở 64 KiB sau khi giải nén, và nội dung chuyển hướng
  bị loại bỏ mà không đọc.
- Lỗi yêu cầu chỉ in ra mã trạng thái HTTP hoặc lớp lỗi, vì một
  `--api-url` tùy chỉnh có thể chứa thông tin xác thực.
- Lệnh được cài đặt bởi `.deb` và `.rpm` chạy Python ở chế độ cô lập.
  Nó bỏ qua `PYTHONPATH`, thư mục site người dùng và các mô-đun trong thư mục
  làm việc. Bản cài đặt bằng `pip` sử dụng console script chuẩn và tuân theo
  môi trường mà nó được cài đặt.
- Trạng thái biến động được đọc và ghi mà không đi theo liên kết tượng trưng tại
  tên tệp trạng thái hoặc tệp khóa, tương đối với một thư mục được mở một lần cho mỗi lần kiểm tra.
- Các tài nguyên phát hành mang theo chứng thực nguồn gốc bản dựng bên cạnh
  `SHA256SUMS`; xem [Từ GitHub Releases](#from-github-releases).

## Nâng cấp từ 1.0.0

Những thay đổi này có trong phiên bản 2.0.0.

- Báo giá có dấu thời gian của nhà cung cấp cũ hơn một giờ sẽ trả về `UNKNOWN` trừ khi có
  giá trị `--max-age` lớn hơn. Các endpoint không trả về dấu thời gian không bị ảnh hưởng.
- `--currency` chỉ chấp nhận 2-16 chữ cái hoặc chữ số.
- Các chuỗi số có dấu phân tách chữ số hoặc khoảng trắng bao quanh sẽ bị từ chối.
- Thời gian chờ thử lại không vừa với ngân sách sẽ báo cáo lỗi gốc
  thay vì `API request timed out`.
- Các gói gốc không còn tuân theo `PYTHONPATH`.
- Các ngưỡng từ một triệu trở lên xuất hiện trong dữ liệu hiệu suất dưới dạng số
  thập phân thuần túy thay vì ký pháp số mũ.

## Bản địa hóa

Trợ giúp CLI, lỗi xác thực và mô tả trạng thái plugin hỗ trợ 45 ngôn ngữ địa phương (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) bằng các danh mục nạp qua thư viện chuẩn đi kèm. Thứ tự phân giải kiểm tra `--lang`, sau đó đến `LC_ALL`, `LC_MESSAGES` và `LANG`, rồi quay về `en`. Tiền tố trạng thái Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) và dữ liệu hiệu suất giữ nguyên trên tất cả các ngôn ngữ.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Phát triển

Cài đặt [mise](https://mise.jdx.dev/getting-started.html), sau đó chạy phần thiết lập phát triển ở trên. `mise.toml` ghim phiên bản Python và uv. Các công cụ phát triển được khai báo trong `pyproject.toml` và được phân giải trong tệp `uv.lock` đã commit.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Cài đặt các hook commit sau khi thiết lập:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Sử dụng `mise exec -- uv add --dev <tool>` hoặc `mise exec -- uv add <dependency>` để cập nhật phụ thuộc và commit cả `pyproject.toml` lẫn `uv.lock`.

CI kiểm tra Python 3.12 và 3.13 trên Linux và Python 3.13 trên macOS. Mọi PR cũng chạy kiểm tra hợp lệ gói, kiểm toán phụ thuộc và CodeQL, đồng thời cài đặt gói `.deb` trên Ubuntu và gói `.rpm` trên Fedora. Các bản phân phối đã dựng sẵn có sẵn dưới dạng artifact `distributions` trên các lần chạy CI.

Phiên bản gói và CLI lấy từ `check_bitcoin_price/__init__.py`. Xem [quy trình phát hành](../../../CONTRIBUTING.md#releases) để biết cách tăng phiên bản và tự động xuất bản các tài nguyên phát hành trên GitHub.

## Đóng góp

Xem [CONTRIBUTING.md](../../../CONTRIBUTING.md) để biết quy trình làm việc phát triển và các yêu cầu ký xác nhận commit.

## Giấy phép

Dự án này được cấp phép theo Giấy phép MIT - xem tệp [LICENSE](../../../LICENSE) để biết chi tiết.

## Tác giả

Thomas Vincent

## Lời cảm ơn

- [CoinGecko](https://www.coingecko.com/) đã cung cấp API tiền điện tử miễn phí
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
