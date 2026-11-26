# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · **Bahasa Indonesia**

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Plugin Nagios/Icinga untuk memantau harga Bitcoin dengan ambang batas peringatan dan kritis yang dapat dikonfigurasi.

## Fitur

- Memantau harga Bitcoin dalam berbagai mata uang (USD, EUR, GBP, dll.)
- Ambang batas peringatan dan kritis yang dapat dikonfigurasi (tinggi dan rendah)
- Output standar plugin Nagios dengan data performa
- Menggunakan CoinGecko API (gratis, tidak memerlukan kunci API)
- Dukungan untuk endpoint API kustom
- Batas waktu (timeout) yang dapat dikonfigurasi
- Pemeriksaan kesegaran kuotasi menggunakan timestamp vendor, dengan batas default satu jam
- Percobaan ulang terbatas untuk pembatasan laju (rate limit) dan kegagalan API sementara
- Satu tenggat waktu untuk semua percobaan dan batas 64 KiB untuk setiap respons
- Peringatan opsional pada pergerakan persentase absolut 24 jam
- Ambang batas harga, durasi permintaan, dan usia kuotasi dalam data performa

## Instalasi

<a name="from-github-releases"></a>

### Dari GitHub Releases

Unduh file `.deb`, `.rpm`, `.tar.gz`, wheel, dan `SHA256SUMS` dari [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Verifikasi unduhan dengan `sha256sum --ignore-missing --check SHA256SUMS`. Rilis setelah 1.0.0 juga menyertakan provenans build yang ditandatangani; pastikan aset berasal dari alur kerja rilis repositori ini dengan `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Gunakan nama file dari rilis yang dipilih. Paket native menginstal `/usr/bin/check_bitcoin_price` dan `/usr/lib/nagios/plugins/check_bitcoin_price`; paket RPM juga menyediakan `/usr/lib64/nagios/plugins/check_bitcoin_price`. Perintah dalam paket menjalankan Python dalam mode terisolasi, sehingga mengabaikan `PYTHONPATH` dan modul di direktori kerja; pengelola paket sistem menyelesaikan dependensi Python dan `requests`. Paket ini berisi kode Python yang independen terhadap arsitektur dan memerlukan distribusi yang menyediakan Python 3.12 atau lebih baru.

### Dari Kode Sumber

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Untuk Pengembangan

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Penggunaan

### Penggunaan Dasar

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Dengan Ambang Batas

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Ambang Batas Individual

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Mata Uang Berbeda

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Timeout Kustom

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Kesegaran Data dan Anggaran Percobaan Ulang

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Kuotasi yang membawa timestamp vendor harus berusia maksimal satu jam secara default.
Endpoint yang hanya mengembalikan harga tetap dapat digunakan ketika `--max-age` tidak disertakan.
Dengan `--max-age`, timestamp vendor yang hilang, tidak valid, berada di masa depan, atau kedaluwarsa akan mengembalikan
`UNKNOWN`; plugin tidak mengganti waktu kuotasi vendor dengan waktu pengambilan lokal.
Timestamp yang tepat berada pada batas usia tetap diterima. Timestamp di
masa depan selalu ditolak.

Default-nya mengizinkan satu kali percobaan ulang. Hanya kesalahan koneksi, timeout, dan respons HTTP
408/429/500/502/503/504 yang dicoba ulang. Backoff dimulai pada 0,5 detik dan
berlipat ganda untuk percobaan ulang berikutnya; detik `Retry-After` dan tanggal HTTP
diprioritaskan. Semua percobaan, pembacaan respons, pendekodean JSON, dan penantian percobaan ulang berbagi
anggaran `--timeout`. Penantian percobaan ulang yang tidak muat dalam anggaran langsung mengembalikan `UNKNOWN`
dan melaporkan kegagalan yang memicunya, seperti `HTTP 429` atau `ConnectionError`,
bukan timeout. Kegagalan autentikasi, kesalahan HTTP permanen lainnya, JSON tidak
valid, dan respons yang lebih besar dari 64 KiB data terdekode tidak dicoba ulang. Gunakan
`--retries 0` untuk menonaktifkan percobaan ulang.

### Sumber kuotasi cadangan

Gunakan opsi `--fallback-url URL` yang dapat diulang dengan endpoint yang kompatibel dengan CoinGecko.
Misalnya, tambahkan `--fallback-url https://quotes.example.org/simple/price`.
Setiap sumber mendapat porsi yang sama dari sisa tenggat waktu permintaan, termasuk percobaan ulangnya.
Kegagalan sementara atau penundaan percobaan ulang yang lebih lama dari porsi tersebut akan beralih ke
sumber berikutnya. Kegagalan verifikasi TLS, kesalahan HTTP permanen, dan kuotasi yang tidak valid
mengembalikan UNKNOWN. Setiap respons kuotasi dibatasi hingga 64 KiB data terdekode.
Ketika sumber cadangan dikonfigurasi, status mengidentifikasi sumber yang menjawab sebagai
`primary`, `fallback1`, dan seterusnya, tanpa mencetak URL-nya.

### Pergerakan jendela pendek

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Berikan pengguna pemantauan direktori status privat yang dapat ditulis pada sistem file lokal Linux atau
macOS. Pertahankan file `.lock` pendamping tetap di tempatnya di antara pemeriksaan. Gunakan
file status terpisah untuk setiap jendela. Setiap mata uang memiliki riwayat independen di dalamnya.
Jendela default adalah 3600 detik. Setiap kuotasi yang valid memerlukan timestamp vendor
di dalam jendela dan batas usia, yaitu satu jam kecuali `--max-age` menetapkan nilai
lain. Plugin membandingkan harga saat ini
dengan harga positif paling awal sebelumnya dalam jendela tersebut dan melaporkan
detik berlalu yang sebenarnya. Timestamp yang berulang tidak membuat sampel tambahan.
Sampel pertama, riwayat yang kedaluwarsa, atau JSON yang rusak memulai baseline baru;
metrik jendela bernilai unknown hingga ada sampel yang dapat dibandingkan. Peringatan lain tetap
berlaku. Status yang tidak dapat ditulis, file status atau file kunci berupa symbolic link, atau kuotasi yang lebih lama
dari sampel terbaru yang tercatat akan mengembalikan UNKNOWN. Metrik `bitcoin_move_window` bertanda
menggunakan rentang peringatan dan kritis yang simetris. Nilai yang tepat sama dengan batas tidak memicu peringatan.

Plugin membuka direktori status satu kali per pemeriksaan dan bekerja relatif terhadapnya, sehingga
komponen jalur yang diganti selama pemeriksaan tidak dapat mengalihkan kunci, pembacaan,
atau penulisan. Symbolic link pada bagian direktori dari jalur diikuti saat
pemeriksaan dimulai, sehingga link platform seperti `/var` di macOS tetap dapat digunakan. Oleh karena itu,
direktori status dan induknya tidak boleh dapat ditulis oleh pengguna lain.
File status dan file kunci dibuat dengan mode 0600.

### Pergerakan Persentase Harian

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Ambang batas perubahan mengukur nilai absolut dari perubahan persentase 24 jam bertanda milik CoinGecko
dalam mata uang yang dipilih. Perubahan yang tepat berada pada ambang batas tidak
memicu peringatan. Jika kedua ambang batas diberikan, nilai peringatan tidak boleh melebihi nilai kritis.
Data perubahan wajib yang hilang atau tidak valid mengembalikan `UNKNOWN`. Peringatan harga dan perubahan
dapat digabungkan; tingkat keparahan tertinggi yang menang, dengan harga diutamakan
ketika tingkat keparahan sama.

## Opsi Baris Perintah

| Opsi | Deskripsi |
|------|-----------|
| `-w`, `--warning` | Rentang ambang batas peringatan (format: LOW:HIGH) |
| `-c`, `--critical` | Rentang ambang batas kritis (format: LOW:HIGH) |
| `--warning-low` | Ambang batas peringatan untuk harga rendah |
| `--warning-high` | Ambang batas peringatan untuk harga tinggi |
| `--critical-low` | Ambang batas kritis untuk harga rendah |
| `--critical-high` | Ambang batas kritis untuk harga tinggi |
| `--currency` | Kode mata uang terdiri dari 2-16 huruf atau angka (default: usd) |
| `--timeout` | Total anggaran permintaan/percobaan ulang API dalam detik, termasuk nilai pecahan (default: 10) |
| `--retries` | Percobaan tambahan untuk kesalahan sementara, 0–5 (default: 1) |
| `--max-age` | Usia maksimum kuotasi vendor dalam detik dan mewajibkan timestamp; kuotasi bertimestamp memiliki default 3600 |
| `--warning-change` | Batas peringatan untuk pergerakan persentase absolut 24 jam |
| `--critical-change` | Batas kritis untuk pergerakan persentase absolut 24 jam |
| `--api-url` | URL API utama |
| `--fallback-url` | Endpoint kompatibel tambahan; ulangi sesuai urutan prioritas |
| `--state-file` | File riwayat pergerakan JSON |
| `--move-window` | Jendela pergerakan dalam detik (default: 3600) |
| `--warning-move`, `--critical-move` | Ambang batas pergerakan jendela absolut dalam persen |
| `-v`, `--verbose` | Aktifkan output verbose |
| `-V`, `--version` | Tampilkan versi |
| `-h`, `--help` | Tampilkan pesan bantuan |

## Konfigurasi Nagios

### Definisi Perintah

Atur makro sumber daya Nagios `$USER1$` ke direktori plugin (paket native menggunakan `/usr/lib/nagios/plugins`). Tambahkan ke konfigurasi perintah Nagios Anda:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Definisi Layanan

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

### Konfigurasi Icinga2

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

## Kode Keluar

Argumen yang tidak valid, timeout tidak positif, rentang ambang batas tidak valid, dan harga API
yang cacat mengembalikan `UNKNOWN` (keluar 3). Ambang batas harus berupa bilangan berhingga dan non-negatif,
dengan setiap batas bawah tidak lebih besar dari batas atasnya. Mata uang harus
berupa 2-16 huruf atau angka. Konfigurasi yang tidak valid ditolak sebelum menghubungi
API. Harga harus berhingga dan non-negatif, diberikan sebagai angka JSON atau string
desimal biasa seperti `"43521.5"`. Respons tanpa mata uang yang diminta
akan menyebutkannya, misalnya `Response has no EUR price`. Respons yang tidak valid tidak mengeluarkan
data performa. Diagnostik verbose diarahkan ke stderr
sehingga stdout hanya berisi satu baris status pemantauan.

| Kode | Status | Deskripsi |
|------|--------|-----------|
| 0 | OK | Harga berada dalam rentang yang dapat diterima |
| 1 | WARNING | Harga melewati ambang batas peringatan |
| 2 | CRITICAL | Harga melewati ambang batas kritis |
| 3 | UNKNOWN | Terjadi kesalahan (kegagalan API, timeout, dll.) |

## Data Performa

Plugin mengeluarkan data performa dalam format standar Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Data performa harga mencakup rentang peringatan/kritis yang dikonfigurasi dan
nilai minimum nol. Ambang batas dicetak dalam notasi desimal penuh, tidak pernah dibulatkan
atau dalam bentuk eksponen, sehingga nilai besar seperti `14500000:16250000` tetap dapat diurai. Waktu permintaan mencakup semua percobaan dan backoff. Usia kuotasi
dikeluarkan hanya jika vendor menyertakan timestamp yang valid; perubahan harian dikeluarkan
jika tersedia. Rentang perubahan simetris di sekitar nol. Data yang tidak valid atau kedaluwarsa
menghasilkan `UNKNOWN` tanpa data performa harga. Metrik ini dapat digunakan dengan
alat grafik seperti PNP4Nagios, Grafana, atau InfluxDB.

## API

Plugin ini menggunakan [CoinGecko API](https://www.coingecko.com/en/api) secara default, yang gratis dan tidak memerlukan kunci API. Pembatasan laju (rate limit) berlaku.

Endpoint kustom harus menggunakan bentuk respons yang sama: `bitcoin.<currency>` untuk
harga, `bitcoin.last_updated_at` untuk detik timestamp UNIX, dan
`bitcoin.<currency>_24h_change` untuk pergerakan persentase harian bertanda. Hanya harga
yang wajib ada ketika `--max-age` dan ambang batas perubahan tidak disertakan. Timestamp
yang tersedia tetap diperiksa: tidak boleh berada di masa depan atau lebih tua dari satu
jam. Respons yang didekodekan harus muat dalam 64 KiB.

Mata uang yang didukung meliputi: usd, eur, gbp, jpy, aud, cad, chf, cny, dan banyak lagi.

## Keamanan

Langkah-langkah di bawah ini diterapkan dalam kode saat ini. Langkah-langkah ini membatasi apa yang dapat dilakukan endpoint yang bermasalah atau pengguna lokal terhadap
host pemantauan; langkah-langkah ini tidak membuat kuotasi itu sendiri dapat dipercaya.

- Sertifikat HTTPS diverifikasi dengan default `requests`, dan tidak ada opsi yang
  menonaktifkan verifikasi. `--api-url` kustom yang menggunakan `http://` biasa tidak memiliki
  perlindungan tersebut.
- DNS, koneksi, pembacaan, percobaan ulang, dan backoff berbagi tenggat waktu `--timeout`. Pihak
  lawan yang mengirim data secara lambat tidak dapat memperpanjangnya.
- Setiap respons dibatasi hingga 64 KiB setelah dekompresi, dan isi pengalihan
  dibuang tanpa dibaca.
- Kegagalan permintaan hanya mencetak status HTTP atau kelas kesalahan, karena `--api-url`
  kustom dapat berisi kredensial.
- Perintah yang diinstal oleh `.deb` dan `.rpm` menjalankan Python dalam mode terisolasi.
  Perintah tersebut mengabaikan `PYTHONPATH`, direktori site pengguna, dan modul di direktori
  kerja. Instalasi `pip` menggunakan skrip konsol standar dan mengikuti
  lingkungan tempat ia diinstal.
- Status pergerakan dibaca dan ditulis tanpa mengikuti symbolic link pada nama
  file status atau file kunci, relatif terhadap direktori yang dibuka satu kali per pemeriksaan.
- Aset rilis membawa atestasi provenans build selain
  `SHA256SUMS`; lihat [Dari GitHub Releases](#from-github-releases).

## Peningkatan dari 1.0.0

Perubahan berikut hadir pada versi 2.0.0.

- Kuotasi dengan timestamp vendor yang lebih lama dari satu jam mengembalikan `UNKNOWN` kecuali
  `--max-age` yang lebih besar diberikan. Endpoint yang tidak mengembalikan timestamp tidak terpengaruh.
- `--currency` hanya menerima 2-16 huruf atau angka.
- String numerik dengan pemisah digit atau spasi di sekitarnya ditolak.
- Penantian percobaan ulang yang tidak muat dalam anggaran melaporkan kegagalan yang mendasarinya,
  bukan `API request timed out`.
- Paket native tidak lagi menghormati `PYTHONPATH`.
- Ambang batas satu juta atau lebih muncul dalam data performa sebagai desimal biasa,
  bukan notasi eksponen.

## Lokalisasi

Bantuan CLI, kesalahan validasi, dan deskripsi status plugin mendukung 45 lokal (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) menggunakan katalog bawaan yang dimuat dengan stdlib. Resolusi memeriksa `--lang`, lalu `LC_ALL`, `LC_MESSAGES`, dan `LANG`, dengan fallback ke `en`. Awalan status Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) dan data performa tetap tidak berubah di semua lokal.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Pengembangan

Instal [mise](https://mise.jdx.dev/getting-started.html), lalu jalankan penyiapan pengembangan di atas. `mise.toml` mengunci versi Python dan uv. Alat pengembangan dideklarasikan dalam `pyproject.toml` dan diselesaikan dalam `uv.lock` yang di-commit.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Instal commit hook setelah penyiapan:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Gunakan `mise exec -- uv add --dev <tool>` atau `mise exec -- uv add <dependency>` untuk memperbarui dependensi dan commit baik `pyproject.toml` maupun `uv.lock`.

CI memeriksa Python 3.12 dan 3.13 di Linux serta Python 3.13 di macOS. Setiap PR juga menjalankan validasi paket, audit dependensi, dan CodeQL, serta menginstal `.deb` di Ubuntu dan `.rpm` di Fedora. Distribusi hasil build tersedia sebagai artefak `distributions` pada eksekusi CI.

Versi paket dan CLI berasal dari `check_bitcoin_price/__init__.py`. Lihat [proses rilis](../../../CONTRIBUTING.md#releases) untuk kenaikan versi dan publikasi otomatis aset rilis GitHub.

## Berkontribusi

Lihat [CONTRIBUTING.md](../../../CONTRIBUTING.md) untuk alur kerja pengembangan dan persyaratan commit yang ditandatangani (signed-off).

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](../../../LICENSE) untuk detailnya.

## Penulis

Thomas Vincent

## Ucapan Terima Kasih

- [CoinGecko](https://www.coingecko.com/) karena telah menyediakan API mata uang kripto gratis
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
