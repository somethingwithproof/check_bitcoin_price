# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · **Bahasa Melayu** · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Pemalam Nagios/Icinga untuk memantau harga Bitcoin dengan ambang amaran dan kritikal yang boleh dikonfigurasikan.

## Ciri-ciri

- Memantau harga Bitcoin dalam pelbagai mata wang (USD, EUR, GBP, dll.)
- Ambang amaran dan kritikal yang boleh dikonfigurasikan (tinggi dan rendah)
- Output pemalam Nagios standard dengan data prestasi
- Menggunakan API CoinGecko (percuma, tiada kunci API diperlukan)
- Sokongan untuk titik akhir API tersuai
- Had masa yang boleh dikonfigurasikan
- Semakan kesegaran sebut harga menggunakan cap masa pembekal, dengan had lalai satu jam
- Cubaan semula terhad untuk had kadar dan kegagalan API sementara
- Satu tarikh akhir untuk semua cubaan dan had 64 KiB bagi setiap respons
- Makluman pilihan bagi pergerakan peratusan mutlak 24 jam
- Ambang harga, tempoh permintaan, dan usia sebut harga dalam data prestasi

## Pemasangan

### Dari Keluaran GitHub

Muat turun fail `.deb`, `.rpm`, `.tar.gz`, wheel, dan `SHA256SUMS` daripada [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Sahkan muat turun dengan `sha256sum --ignore-missing --check SHA256SUMS`. Keluaran selepas 1.0.0 juga membawa bukti binaan bertandatangan; sahkan bahawa aset berasal daripada aliran kerja keluaran repositori ini dengan `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Gunakan nama fail daripada keluaran yang dipilih. Pakej natif memasang `/usr/bin/check_bitcoin_price` dan `/usr/lib/nagios/plugins/check_bitcoin_price`; RPM juga menyediakan `/usr/lib64/nagios/plugins/check_bitcoin_price`. Perintah yang dipakejkan menjalankan Python dalam mod terasing, jadi ia mengabaikan `PYTHONPATH` dan modul dalam direktori kerja; pengurus pakej sistem menyelesaikan kebergantungan Python dan `requests`. Pakej ini mengandungi kod Python yang tidak bergantung pada seni bina dan memerlukan pengedaran yang menyediakan Python 3.12 atau lebih baharu.

### Dari Sumber

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Untuk Pembangunan

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Penggunaan

### Penggunaan Asas

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Dengan Ambang

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Ambang Individu

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Mata Wang Berbeza

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Had Masa Tersuai

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Kesegaran dan Bajet Cubaan Semula

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Sebut harga yang membawa cap masa pembekal mestilah berusia paling lama satu jam secara lalai.
Titik akhir yang hanya mengembalikan harga kekal boleh digunakan apabila `--max-age` tiada.
Dengan `--max-age`, cap masa pembekal yang hilang, tidak sah, masa hadapan, atau lapuk mengembalikan
`UNKNOWN`; pemalam tidak menggantikan masa ambilan tempatan untuk masa sebut harga
pembekal. Cap masa yang tepat pada had usia kekal boleh diterima. Cap masa hadapan
sentiasa ditolak.

Tetapan lalai membenarkan satu cubaan semula. Hanya ralat sambungan, tamat masa, dan respons HTTP
408/429/500/502/503/504 dicuba semula. Undur mula pada 0.5 saat dan
berganda untuk cubaan semula berikutnya; saat `Retry-After` dan tarikh HTTP
diutamakan. Semua cubaan, bacaan respons, penyahkodan JSON, dan tempoh tunggu cubaan semula berkongsi
bajet `--timeout`. Tempoh tunggu cubaan semula yang tidak muat mengembalikan `UNKNOWN` serta-merta
dan melaporkan kegagalan yang mencetuskannya, seperti `HTTP 429` atau `ConnectionError`,
bukannya tamat masa. Kegagalan pengesahan, ralat HTTP kekal lain, JSON tidak
sah, dan respons yang lebih besar daripada 64 KiB data ternyahkod tidak dicuba semula. Gunakan
`--retries 0` untuk melumpuhkan cubaan semula.

### Sumber sebut harga sandaran

Gunakan pilihan `--fallback-url URL` yang boleh diulang dengan titik akhir yang serasi dengan CoinGecko.
Sebagai contoh, tambah `--fallback-url https://quotes.example.org/simple/price`.
Setiap sumber mendapat bahagian yang sama daripada baki tarikh akhir permintaan, termasuk
cubaan semulanya. Kegagalan sementara atau kelewatan cubaan semula yang lebih panjang daripada bahagian tersebut beralih ke
sumber seterusnya. Kegagalan pengesahan TLS, ralat HTTP kekal dan sebut harga tidak sah
mengembalikan UNKNOWN. Setiap respons sebut harga dihadkan kepada 64 KiB data ternyahkod.
Apabila sandaran dikonfigurasikan, status mengenal pasti sumber yang menjawab sebagai
`primary`, `fallback1`, dan seterusnya, tanpa mencetak URLnya.

### Pergerakan tetingkap pendek

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Berikan pengguna pemantauan direktori keadaan boleh tulis peribadi pada sistem fail Linux atau
macOS tempatan. Kekalkan fail `.lock` bersebelahan di tempatnya di antara semakan. Gunakan
fail keadaan berasingan bagi setiap tetingkap. Mata wang mempunyai sejarah bebas di dalamnya.
Tetingkap lalai ialah 3600 saat. Setiap sebut harga yang sah memerlukan cap masa pembekal
dalam tetingkap dan had usia, iaitu satu jam melainkan `--max-age` menetapkan
nilai lain. Pemalam membandingkan harga
semasa dengan harga positif terdahulu yang paling lama dalam tetingkap tersebut dan melaporkan
saat sebenar yang telah berlalu. Cap masa berulang tidak mencipta sampel tambahan.
Sampel pertama, sejarah tamat tempoh, atau JSON rosak memulakan garis dasar baharu;
metrik tetingkap tidak diketahui sehingga terdapat sampel yang boleh dibandingkan. Makluman lain masih
terpakai. Keadaan tidak boleh tulis, fail keadaan atau fail kunci pautan simbolik, atau sebut harga lebih lama
daripada sampel terbaharu yang direkodkan mengembalikan UNKNOWN. Metrik `bitcoin_move_window` bertanda
menggunakan julat amaran dan kritikal simetri. Persamaan pada had tidak mencetuskan makluman.

Pemalam membuka direktori keadaan sekali bagi setiap semakan dan berfungsi secara relatif kepadanya, jadi
komponen laluan yang digantikan semasa semakan tidak dapat mengalihkan kunci, bacaan,
atau penulisan. Pautan simbolik dalam bahagian direktori laluan diikuti apabila
semakan bermula, yang memastikan pautan platform seperti `/var` pada macOS kekal boleh digunakan. Oleh itu,
direktori keadaan dan leluhurnya mestilah tidak boleh ditulis oleh pengguna lain.
Fail keadaan dan fail kunci dicipta dengan mod 0600.

### Pergerakan Peratusan Harian

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Ambang perubahan mengukur nilai mutlak peratusan perubahan 24 jam bertanda CoinGecko
dalam mata wang yang dipilih. Perubahan yang tepat pada ambang tidak
mencetuskan makluman. Jika kedua-dua ambang dibekalkan, amaran tidak boleh melebihi kritikal.
Data perubahan yang diperlukan yang hilang atau tidak sah mengembalikan `UNKNOWN`. Makluman harga dan perubahan
boleh digabungkan; tahap keterukan tertinggi menang, dengan harga diutamakan
apabila tahap keterukan sepadan.

## Pilihan Baris Perintah

| Pilihan | Keterangan |
|---------|------------|
| `-w`, `--warning` | Julat ambang amaran (format: LOW:HIGH) |
| `-c`, `--critical` | Julat ambang kritikal (format: LOW:HIGH) |
| `--warning-low` | Ambang amaran untuk harga rendah |
| `--warning-high` | Ambang amaran untuk harga tinggi |
| `--critical-low` | Ambang kritikal untuk harga rendah |
| `--critical-high` | Ambang kritikal untuk harga tinggi |
| `--currency` | Kod mata wang 2-16 huruf atau digit (lalai: usd) |
| `--timeout` | Jumlah bajet permintaan/cubaan semula API dalam saat, termasuk nilai pecahan (lalai: 10) |
| `--retries` | Cubaan sementara tambahan, 0-5 (lalai: 1) |
| `--max-age` | Usia sebut harga pembekal maksimum dalam saat dan memerlukan cap masa; sebut harga bercap masa berlalai kepada 3600 |
| `--warning-change` | Had amaran untuk pergerakan peratusan mutlak 24 jam |
| `--critical-change` | Had kritikal untuk pergerakan peratusan mutlak 24 jam |
| `--api-url` | URL API utama |
| `--fallback-url` | Titik akhir serasi tambahan; ulang mengikut urutan pilihan |
| `--state-file` | Fail sejarah pergerakan JSON |
| `--move-window` | Tetingkap pergerakan dalam saat (lalai: 3600) |
| `--warning-move`, `--critical-move` | Ambang pergerakan tetingkap mutlak dalam peratus |
| `-v`, `--verbose` | Dayakan output terperinci |
| `-V`, `--version` | Paparkan versi |
| `-h`, `--help` | Paparkan mesej bantuan |

## Konfigurasi Nagios

### Takrifan Perintah

Tetapkan makro sumber Nagios `$USER1$` ke direktori pemalam (pakej natif menggunakan `/usr/lib/nagios/plugins`). Tambah pada konfigurasi perintah Nagios anda:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Takrifan Perkhidmatan

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

## Kod Keluar

Argumen tidak sah, had masa bukan positif, julat ambang tidak sah, dan harga API
cacat mengembalikan `UNKNOWN` (keluar 3). Ambang mestilah nombor terhingga bukan negatif,
dengan setiap had rendah tidak lebih besar daripada had tingginya. Mata wang mestilah
2-16 huruf atau digit. Konfigurasi tidak sah ditolak sebelum menghubungi
API. Harga mestilah terhingga dan bukan negatif, diberikan sebagai nombor JSON atau rentetan
perpuluhan biasa seperti `"43521.5"`. Respons tanpa mata wang yang diminta
menamakannya, contohnya `Response has no EUR price`. Respons tidak sah tidak mengeluarkan
data prestasi. Diagnostik terperinci dihantar ke stderr
supaya stdout mengandungi satu baris status pemantauan.

| Kod | Status | Keterangan |
|-----|--------|------------|
| 0 | OK | Harga berada dalam julat yang boleh diterima |
| 1 | WARNING | Harga melepasi ambang amaran |
| 2 | CRITICAL | Harga melepasi ambang kritikal |
| 3 | UNKNOWN | Ralat berlaku (kegagalan API, tamat masa, dll.) |

## Data Prestasi

Pemalam mengeluarkan data prestasi dalam format Nagios standard:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Data prestasi harga merangkumi julat amaran/kritikal yang dikonfigurasikan dan nilai
minimum sifar. Ambang dicetak dalam tatatanda perpuluhan penuh, tidak pernah dibundarkan
atau dalam bentuk eksponen, supaya nilai besar seperti `14500000:16250000` kekal boleh dihuraikan. Masa permintaan merangkumi semua cubaan dan undur. Usia sebut harga hanya
dikeluarkan apabila pembekal membekalkan cap masa yang sah; perubahan harian dikeluarkan
apabila tersedia. Julat perubahan adalah simetri di sekitar sifar. Data tidak sah atau lapuk
menghasilkan `UNKNOWN` tanpa data prestasi harga. Metrik ini boleh digunakan dengan
alat graf seperti PNP4Nagios, Grafana, atau InfluxDB.

## API

Pemalam ini menggunakan [CoinGecko API](https://www.coingecko.com/en/api) secara lalai, yang percuma dan tidak memerlukan kunci API. Had kadar terpakai.

Titik akhir tersuai mesti menggunakan bentuk respons yang sama: `bitcoin.<currency>` untuk
harga, `bitcoin.last_updated_at` untuk saat cap masa UNIX, dan
`bitcoin.<currency>_24h_change` untuk pergerakan peratusan harian bertanda. Hanya harga
diperlukan apabila `--max-age` dan ambang perubahan tiada. Cap masa
yang hadir masih disemak: ia tidak boleh berada pada masa hadapan atau berusia lebih daripada satu
jam. Respons ternyahkod mesti muat dalam 64 KiB.

Mata wang yang disokong termasuk: usd, eur, gbp, jpy, aud, cad, chf, cny, dan banyak lagi.

## Keselamatan

Langkah-langkah di bawah dilaksanakan dalam kod semasa. Langkah ini mengehadkan perkara yang boleh dilakukan oleh titik akhir yang tidak berkelakuan baik atau pengguna tempatan terhadap
hos pemantauan; langkah ini tidak menjadikan sebut harga itu sendiri boleh dipercayai.

- Sijil HTTPS disahkan dengan tetapan lalai `requests`, dan tiada pilihan yang
  melumpuhkan pengesahan. `--api-url` tersuai yang menggunakan `http://` biasa tidak mempunyai
  perlindungan sedemikian.
- DNS, sambungan, bacaan, cubaan semula, dan undur berkongsi tarikh akhir `--timeout`. Rakan
  yang menghantar data secara perlahan tidak boleh memanjangkannya.
- Setiap respons dihadkan kepada 64 KiB selepas penyahmampatan, dan isi pengalihan
  dibuang tanpa dibaca.
- Kegagalan permintaan hanya mencetak status HTTP atau kelas ralat, kerana `--api-url`
  tersuai mungkin mengandungi kelayakan.
- Perintah yang dipasang oleh `.deb` dan `.rpm` menjalankan Python dalam mod terasing.
  Ia mengabaikan `PYTHONPATH`, direktori tapak pengguna, dan modul dalam direktori
  kerja. Pemasangan `pip` menggunakan skrip konsol standard dan mengikut
  persekitaran tempat ia dipasang.
- Keadaan pergerakan dibaca dan ditulis tanpa mengikuti pautan simbolik pada nama
  fail keadaan atau fail kunci, secara relatif kepada direktori yang dibuka sekali bagi setiap semakan.
- Aset keluaran membawa pengesahan bukti binaan sebagai tambahan kepada
  `SHA256SUMS`; lihat [Dari Keluaran GitHub](#dari-keluaran-github).

## Menaik Taraf daripada 1.0.0

Perubahan ini disertakan dalam 2.0.0.

- Sebut harga dengan cap masa pembekal yang lebih lama daripada satu jam mengembalikan `UNKNOWN` melainkan
  `--max-age` yang lebih besar diberikan. Titik akhir yang tidak mengembalikan cap masa tidak terjejas.
- `--currency` hanya menerima 2-16 huruf atau digit.
- Rentetan berangka dengan pemisah digit atau ruang di sekelilingnya ditolak.
- Tempoh tunggu cubaan semula yang tidak muat dalam bajet melaporkan kegagalan asas
  dan bukannya `API request timed out`.
- Pakej natif tidak lagi mematuhi `PYTHONPATH`.
- Ambang satu juta atau lebih muncul dalam data prestasi sebagai perpuluhan
  biasa dan bukannya tatatanda eksponen.

## Penyetempatan

Bantuan CLI, ralat pengesahan, dan keterangan status pemalam menyokong 45 lokal (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) menggunakan katalog tergabung yang dimuatkan oleh stdlib. Peleraian menyemak `--lang`, kemudian `LC_ALL`, `LC_MESSAGES`, dan `LANG`, dengan sandaran kepada `en`. Awalan status Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) dan data prestasi kekal tidak berubah merentas semua lokal.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Pembangunan

Pasang [mise](https://mise.jdx.dev/getting-started.html), kemudian jalankan persediaan pembangunan di atas. `mise.toml` menetapkan versi Python dan uv. Alat pembangunan diisytiharkan dalam `pyproject.toml` dan diselesaikan dalam `uv.lock` yang dikomitkan.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Pasang cangkuk komit selepas persediaan:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Gunakan `mise exec -- uv add --dev <tool>` atau `mise exec -- uv add <dependency>` untuk mengemas kini kebergantungan dan komit kedua-dua `pyproject.toml` dan `uv.lock`.

CI menyemak Python 3.12 dan 3.13 pada Linux serta Python 3.13 pada macOS. Setiap PR juga menjalankan pengesahan pakej, pengauditan kebergantungan, dan CodeQL, serta memasang `.deb` pada Ubuntu dan `.rpm` pada Fedora. Pengedaran terbina tersedia sebagai artifak `distributions` pada larian CI.

Versi pakej dan CLI berasal daripada `check_bitcoin_price/__init__.py`. Lihat [proses keluaran](../../../CONTRIBUTING.md#releases) untuk peningkatan versi dan penerbitan automatik aset keluaran GitHub.

## Sumbangan

Lihat [CONTRIBUTING.md](../../../CONTRIBUTING.md) untuk aliran kerja pembangunan dan keperluan komit bertandatangan.

## Lesen

Projek ini dilesenkan di bawah Lesen MIT - lihat fail [LICENSE](../../../LICENSE) untuk butiran.

## Pengarang

Thomas Vincent

## Penghargaan

- [CoinGecko](https://www.coingecko.com/) kerana menyediakan API mata wang kripto percuma
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
