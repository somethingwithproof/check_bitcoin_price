# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · **Türkçe** · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Bitcoin fiyatını yapılandırılabilir uyarı ve kritik eşiklerle izlemek için bir Nagios/Icinga eklentisi.

## Özellikler

- Bitcoin fiyatını birden fazla para biriminde izleyin (USD, EUR, GBP vb.)
- Yapılandırılabilir uyarı ve kritik eşikler (yüksek ve düşük)
- Performans verileriyle birlikte standart Nagios eklenti çıktısı
- CoinGecko API kullanır (ücretsiz, API anahtarı gerektirmez)
- Özel API uç noktaları desteği
- Yapılandırılabilir zaman aşımı
- Sağlayıcı zaman damgalarını kullanan ve varsayılan bir saatlik sınıra sahip fiyat güncelliği kontrolleri
- Hız sınırları ve geçici API hataları için sınırlı yeniden denemeler
- Tüm denemeler için tek bir zaman sınırı ve her yanıt için 64 KiB üst sınırı
- Mutlak 24 saatlik yüzdelik değişim için isteğe bağlı uyarılar
- Performans verilerinde fiyat eşikleri, istek süresi ve fiyat yaşı

## Kurulum

<a name="from-github-releases"></a>

### GitHub Sürümlerinden

[GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases) sayfasından `.deb`, `.rpm`, `.tar.gz`, wheel ve `SHA256SUMS` dosyalarını indirin. İndirilen dosyayı `sha256sum --ignore-missing --check SHA256SUMS` ile doğrulayın. 1.0.0 sonrası sürümler ayrıca imzalı derleme kökeni taşır; bir dosyanın bu deponun sürüm iş akışından geldiğini `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price` ile doğrulayın.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Seçilen sürümden dosya adlarını kullanın. Yerel paketler `/usr/bin/check_bitcoin_price` ve `/usr/lib/nagios/plugins/check_bitcoin_price` yollarına kurulum yapar; RPM paketi ayrıca `/usr/lib64/nagios/plugins/check_bitcoin_price` yolunu sağlar. Paketlenen komut Python'ı yalıtılmış modda çalıştırır, bu nedenle `PYTHONPATH` ve çalışma dizinindeki modülleri yok sayar; sistem paket yöneticisi Python ve `requests` bağımlılıklarını çözer. Mimari bağımsız Python kodu içerirler ve Python 3.12 veya daha yeni bir sürüm sağlayan bir dağıtım gerektirirler.

### Kaynaktan Kurulum

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Geliştirme İçin

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Kullanım

### Temel Kullanım

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Eşiklerle Kullanım

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Ayrı Eşikler

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Farklı Para Birimi

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Özel Zaman Aşımı

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Güncellik ve Yeniden Deneme Bütçesi

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Sağlayıcı zaman damgası taşıyan bir fiyat varsayılan olarak en fazla bir saatlik olabilir.
`--max-age` belirtilmediğinde yalnızca fiyat döndüren uç noktalar kullanılabilir durumda kalır.
`--max-age` ile eksik, geçersiz, gelecek tarihli veya bayat sağlayıcı zaman damgaları `UNKNOWN`
döndürür; eklenti sağlayıcının fiyat zamanı yerine yerel alma zamanını koymaz. Tam olarak
yaş sınırındaki bir zaman damgası kabul edilir. Gelecek tarihli zaman damgaları her zaman reddedilir.

Varsayılan olarak bir yeniden denemeye izin verilir. Yalnızca bağlantı hataları, zaman aşımları ve HTTP
408/429/500/502/503/504 yanıtları yeniden denenir. Geri çekilme (backoff) süresi 0,5 saniyeden başlar
ve sonraki yeniden denemeler için iki katına çıkar; `Retry-After` saniye değerleri ve HTTP tarihleri
önceliklidir. Tüm denemeler, yanıt okumaları, JSON çözümleme ve yeniden deneme beklemeleri `--timeout`
bütçesini paylaşır. Bütçeye sığmayan bir yeniden deneme beklemesi hemen `UNKNOWN` döndürür ve zaman aşımı
yerine buna yol açan `HTTP 429` veya `ConnectionError` gibi hatayı bildirir. Kimlik doğrulama hataları,
diğer kalıcı HTTP hataları, geçersiz JSON ve çözümlenmiş verisi 64 KiB'den büyük yanıtlar yeniden
denenmez. Yeniden denemeleri devre dışı bırakmak için `--retries 0` kullanın.

### Yedek Fiyat Kaynakları

CoinGecko uyumlu uç noktalarla tekrarlanabilir `--fallback-url URL` seçeneklerini kullanın.
Örneğin, `--fallback-url https://quotes.example.org/simple/price` ekleyin.
Her kaynak, yeniden denemeleri de dahil olmak üzere kalan istek süresinden eşit bir pay alır.
Geçici bir hata veya bu paydan daha uzun bir yeniden deneme gecikmesi bir sonraki kaynağa geçilmesine
neden olur. TLS doğrulama hataları, kalıcı HTTP hataları ve geçersiz fiyatlar `UNKNOWN` döndürür.
Her fiyat yanıtı çözümlenmiş 64 KiB veri ile sınırlıdır. Yedekler yapılandırıldığında durum bilgisi,
yanıt veren kaynağı URL'sini yazdırmadan `primary`, `fallback1` ve benzeri şekilde tanımlar.

### Kısa Zaman Aralığı Hareketi

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

İzleme kullanıcısına yerel bir Linux veya macOS dosya sisteminde özel, yazılabilir bir durum dizini
verin. Kontroller arasında kardeş `.lock` dosyasını yerinde tutun. Her zaman aralığı için ayrı bir
durum dosyası kullanın. Para birimleri bunun içinde bağımsız geçmişlere sahiptir. Varsayılan zaman
aralığı 3600 saniyedir. Geçerli her fiyatın, bu aralık ve aksi `--max-age` ile ayarlanmadıkça bir
saat olan yaş sınırı içinde bir sağlayıcı zaman damgasına sahip olması gerekir. Eklenti, mevcut
fiyatı bu aralıktaki en eski pozitif önceki fiyatla karşılaştırır ve gerçekte geçen saniye süresini
bildirir. Tekrarlanan zaman damgaları ek örnek oluşturmaz. İlk örnek, süresi dolmuş geçmiş veya
bozuk JSON yeni bir temel başlatır; karşılaştırılabilir bir örnek olana kadar zaman aralığı metriği
bilinmez olur. Diğer uyarılar yine geçerlidir. Yazılamayan durum dosyası, sembolik bağlantı olan
durum veya kilit dosyası ya da kaydedilen en yeni örnekten daha eski bir fiyat `UNKNOWN` döndürür.
İşaretli `bitcoin_move_window` metriği simetrik uyarı ve kritik aralıklar kullanır. Sınıra eşit
değerler uyarı vermez.

Eklenti her kontrolde durum dizinini bir kez açar ve ona göreli çalışır; böylece kontrol sırasında
değiştirilen bir yol bileşeni kilidi, okumayı veya yazmayı yönlendiremez. Yolun dizin kısmındaki
sembolik bağlantılar kontrol başlarken takip edilir, bu da macOS'taki `/var` gibi platform
bağlantılarının kullanılabilir kalmasını sağlar. Bu nedenle durum dizini ve üst dizinleri diğer
kullanıcılar tarafından yazılabilir olmamalıdır. Durum ve kilit dosyaları 0600 modu ile oluşturulur.

### Günlük Yüzdelik Değişim

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Değişim eşikleri, seçilen para biriminde CoinGecko'nun işaretli 24 saatlik yüzdelik değişiminin
mutlak değerini ölçer. Tam olarak eşik değerindeki bir değişim uyarı vermez. Her iki eşik de
verilirse uyarı eşiği kritik eşiği aşmamalıdır. Eksik veya geçersiz gerekli değişim verisi `UNKNOWN`
döndürür. Fiyat ve değişim uyarıları birleştirilebilir; en yüksek önem derecesi kazanır, önem
dereceleri eşit olduğunda fiyat öncelik alır.

## Komut Satırı Seçenekleri

| Seçenek | Açıklama |
|---------|----------|
| `-w`, `--warning` | Uyarı eşik aralığı (biçim: LOW:HIGH) |
| `-c`, `--critical` | Kritik eşik aralığı (biçim: LOW:HIGH) |
| `--warning-low` | Düşük fiyat için uyarı eşiği |
| `--warning-high` | Yüksek fiyat için uyarı eşiği |
| `--critical-low` | Düşük fiyat için kritik eşiği |
| `--critical-high` | Yüksek fiyat için kritik eşiği |
| `--currency` | 2-16 harf veya rakamdan oluşan para birimi kodu (varsayılan: usd) |
| `--timeout` | Kesirli değerler dahil saniye cinsinden toplam API istek/yeniden deneme bütçesi (varsayılan: 10) |
| `--retries` | Ek geçici deneme sayısı, 0-5 (varsayılan: 1) |
| `--max-age` | Saniye cinsinden maksimum sağlayıcı fiyat yaşı ve zaman damgası zorunluluğu; zaman damgalı fiyatlar varsayılan olarak 3600 |
| `--warning-change` | Mutlak 24 saatlik yüzdelik değişim için uyarı sınırı |
| `--critical-change` | Mutlak 24 saatlik yüzdelik değişim için kritik sınır |
| `--api-url` | Birincil API URL'si |
| `--fallback-url` | Ek uyumlu uç nokta; tercih sırasına göre tekrarlayın |
| `--state-file` | JSON hareket geçmişi dosyası |
| `--move-window` | Saniye cinsinden hareket zaman aralığı (varsayılan: 3600) |
| `--warning-move`, `--critical-move` | Yüzde cinsinden mutlak zaman aralığı hareket eşikleri |
| `-v`, `--verbose` | Ayrıntılı çıktıyı etkinleştir |
| `-V`, `--version` | Sürümü göster |
| `-h`, `--help` | Yardım mesajını göster |

## Nagios Yapılandırması

### Komut Tanımı

Nagios kaynak makrosu `$USER1$` değerini eklenti dizinine ayarlayın (yerel paketler `/usr/lib/nagios/plugins` kullanır). Nagios komutları yapılandırmanıza ekleyin:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Servis Tanımı

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

### Icinga2 Yapılandırması

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

## Çıkış Kodları

Geçersiz argümanlar, pozitif olmayan zaman aşımları, geçersiz eşik aralıkları ve hatalı biçimlendirilmiş
API fiyatları `UNKNOWN` (çıkış 3) döndürür. Eşikler sonlu, negatif olmayan sayılar olmalı ve her alt
sınır üst sınırından büyük olmamalıdır. Para birimi 2-16 harf veya rakam olmalıdır. Geçersiz
yapılandırma API ile iletişime geçmeden önce reddedilir. Fiyatlar sonlu ve negatif olmayan olmalı,
JSON sayıları veya `"43521.5"` gibi düz ondalık dizeler olarak verilmelidir. İstenen para birimini
içermeyen bir yanıt bunu belirtir, örneğin `Response has no EUR price`. Geçersiz yanıtlar performans
verisi yaymaz. Ayrıntılı tanılama bilgileri stderr'e gider, böylece stdout tek bir izleme durum
satırı içerir.

| Kod | Durum | Açıklama |
|-----|-------|----------|
| 0 | OK | Fiyat kabul edilebilir aralıkta |
| 1 | WARNING | Fiyat uyarı eşiğini aştı |
| 2 | CRITICAL | Fiyat kritik eşiği aştı |
| 3 | UNKNOWN | Hata oluştu (API hatası, zaman aşımı vb.) |

## Performans Verileri

Eklenti standart Nagios biçiminde performans verisi çıktısı üretir:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Fiyat performans verileri, yapılandırılmış uyarı/kritik aralıklarını ve minimum sıfır değerini içerir.
Eşikler asla yuvarlanmadan veya üstel biçimde değil, tam ondalık gösterimde yazdırılır; böylece
`14500000:16250000` gibi büyük değerler ayrıştırılabilir kalır. İstek süresi tüm denemeleri ve geri
çekilme sürelerini içerir. Fiyat yaşı yalnızca sağlayıcı geçerli bir zaman damgası sağladığında
yayılır; günlük değişim mevcut olduğunda yayılır. Değişim aralıkları sıfır etrafında simetriktir.
Geçersiz veya bayat veriler fiyat performans verisi olmadan `UNKNOWN` üretir. Bu metrikler PNP4Nagios,
Grafana veya InfluxDB gibi grafik araçlarıyla kullanılabilir.

## API

Bu eklenti varsayılan olarak ücretsiz olan ve API anahtarı gerektirmeyen [CoinGecko API](https://www.coingecko.com/en/api) kullanır. Hız sınırları geçerlidir.

Özel uç noktalar aynı yanıt yapısını kullanmalıdır: fiyat için `bitcoin.<currency>`, UNIX zaman damgası
saniyeleri için `bitcoin.last_updated_at` ve işaretli günlük yüzdelik değişim için
`bitcoin.<currency>_24h_change`. `--max-age` ve değişim eşikleri bulunmadığında yalnızca fiyat
gereklidir. Mevcut olan bir zaman damgası yine de kontrol edilir: gelecekte veya bir saatten eski
olmamalıdır. Çözümlenmiş yanıt 64 KiB içine sığmalıdır.

Desteklenen para birimleri şunları içerir: usd, eur, gbp, jpy, aud, cad, chf, cny ve çok daha fazlası.

## Güvenlik

Aşağıdaki önlemler mevcut kodda uygulanmıştır. Hatalı davranan bir uç noktanın veya yerel bir
kullanıcının izleme sunucusuna yapabileceklerini sınırlarlar; fiyatın kendisini güvenilir kılmazlar.

- HTTPS sertifikaları `requests` varsayılanlarıyla doğrulanır ve doğrulamayı devre dışı bırakan bir
  seçenek yoktur. Düz `http://` kullanan özel bir `--api-url` böyle bir korumaya sahip değildir.
- DNS, bağlantı, okumalar, yeniden denemeler ve geri çekilme `--timeout` zaman sınırını paylaşır.
  Veriyi yavaş gönderen bir eş bunu uzatamaz.
- Her yanıt sıkıştırma açıldıktan sonra 64 KiB ile sınırlıdır ve yönlendirme gövdeleri okunmadan
  atılır.
- Özel bir `--api-url` kimlik bilgileri içerebileceğinden, istek hataları yalnızca bir HTTP durumu
  veya bir hata sınıfı yazdırır.
- `.deb` ve `.rpm` tarafından kurulan komut Python'ı yalıtılmış modda çalıştırır. `PYTHONPATH`,
  kullanıcı site dizinini ve çalışma dizinindeki modülleri yok sayar. Bir `pip` kurulumu standart
  konsol betiğini kullanır ve kurulduğu ortamı takip eder.
- Hareket durumu, her kontrolde bir kez açılan bir dizine göreli olarak, durum veya kilit dosyası
  adındaki bir sembolik bağlantı takip edilmeden okunur ve yazılır.
- Sürüm varlıkları `SHA256SUMS` dosyasına ek olarak derleme kökeni doğrulamaları (build provenance
  attestations) taşır; bkz. [GitHub Sürümlerinden](#from-github-releases).

## 1.0.0 Sürümünden Yükseltme

Bu değişiklikler 2.0.0 sürümünde sunulmuştur.

- Sağlayıcı zaman damgası bir saatten eski olan bir fiyat, daha büyük bir `--max-age` verilmedikçe
  `UNKNOWN` döndürür. Zaman damgası döndürmeyen uç noktalar etkilenmez.
- `--currency` yalnızca 2-16 harf veya rakam kabul eder.
- Basamak ayırıcıları veya çevresinde boşluklar bulunan sayısal dizeler reddedilir.
- Bütçeye sığmayan bir yeniden deneme beklemesi, `API request timed out` yerine temel hatayı bildirir.
- Yerel paketler artık `PYTHONPATH` değişkenini dikkate almaz.
- Bir milyon veya daha büyük eşikler, performans verilerinde üstel gösterim yerine düz ondalık olarak
  görünür.

## Yerelleştirme

CLI yardımı, doğrulama hataları ve eklenti durum açıklamaları, paketlenmiş stdlib yüklü kataloglar kullanarak 45 yerel ayarı (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) destekler. Çözümleme `--lang`, ardından `LC_ALL`, `LC_MESSAGES` ve `LANG` değişkenlerini kontrol eder ve `en` diline geri döner. Nagios durum önekleri (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) ve performans verileri tüm yerel ayarlarda değişmeden kalır.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Geliştirme

[mise](https://mise.jdx.dev/getting-started.html) kurun, ardından yukarıdaki geliştirme kurulumunu çalıştırın. `mise.toml` dosyası Python ve uv sürümlerini sabitler. Geliştirme araçları `pyproject.toml` dosyasında bildirilir ve repoya işlenmiş `uv.lock` dosyasında çözümlenir.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Kurulumdan sonra commit kancalarını (hooks) yükleyin:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Bağımlılıkları güncellemek için `mise exec -- uv add --dev <tool>` veya `mise exec -- uv add <dependency>` kullanın ve hem `pyproject.toml` hem de `uv.lock` dosyalarını commit edin.

CI, Linux üzerinde Python 3.12 ve 3.13'ü, macOS üzerinde Python 3.13'ü kontrol eder. Her PR ayrıca paket doğrulaması, bağımlılık denetimi ve CodeQL çalıştırır ve Ubuntu'da `.deb`, Fedora'da `.rpm` paketlerini kurar. Derlenen dağıtımlar CI çalıştırmalarında `distributions` yapıtı (artifact) olarak mevcuttur.

Paket ve CLI sürümü `check_bitcoin_price/__init__.py` dosyasından gelir. Sürüm yükseltmeleri ve GitHub sürüm varlıklarının otomatik yayınlanması için [sürüm sürecine](../../../CONTRIBUTING.md#releases) bakın.

## Katkıda Bulunma

Geliştirme iş akışı ve imzalı (signed-off) commit gereksinimleri için [CONTRIBUTING.md](../../../CONTRIBUTING.md) dosyasına bakın.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır - ayrıntılar için [LICENSE](../../../LICENSE) dosyasına bakın.

## Yazar

Thomas Vincent

## Teşekkürler

- Ücretsiz bir kripto para birimi API'si sağladığı için [CoinGecko](https://www.coingecko.com/)
- [Nagios Eklentileri Geliştirme Yönergeleri](https://nagios-plugins.org/doc/guidelines.html)
