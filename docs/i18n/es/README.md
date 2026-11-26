# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · **Español** · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Un plugin de Nagios/Icinga para monitorear el precio de Bitcoin con umbrales de advertencia y críticos configurables.

## Características

- Monitorear el precio de Bitcoin en múltiples monedas (USD, EUR, GBP, etc.)
- Umbrales de advertencia y críticos configurables (altos y bajos)
- Salida estándar de plugin de Nagios con datos de rendimiento
- Utiliza la API de CoinGecko (gratuita, no requiere clave de API)
- Soporte para endpoints de API personalizados
- Tiempo de espera configurable
- Comprobaciones de frescura de cotizaciones mediante marcas de tiempo del proveedor, con un límite predeterminado de una hora
- Reintentos acotados para límites de tasa y fallos temporales de la API
- Un único plazo límite para todos los intentos y un tope de 64 KiB por respuesta
- Alertas opcionales sobre la variación porcentual absoluta en 24 horas
- Umbrales de precio, duración de la solicitud y antigüedad de la cotización en los datos de rendimiento

## Instalación

<a name="from-github-releases"></a>

### Desde GitHub Releases

Descarga los archivos `.deb`, `.rpm`, `.tar.gz`, wheel y `SHA256SUMS` desde [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Verifica una descarga con `sha256sum --ignore-missing --check SHA256SUMS`. Las versiones posteriores a la 1.0.0 también incluyen procedencia de compilación firmada; confirma que un archivo proviene del flujo de trabajo de publicación de este repositorio con `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Usa los nombres de archivo de la versión seleccionada. Los paquetes nativos instalan `/usr/bin/check_bitcoin_price` y `/usr/lib/nagios/plugins/check_bitcoin_price`; el paquete RPM también proporciona `/usr/lib64/nagios/plugins/check_bitcoin_price`. El comando empaquetado ejecuta Python en modo aislado, por lo que ignora `PYTHONPATH` y los módulos del directorio de trabajo; el gestor de paquetes del sistema resuelve las dependencias de Python y `requests`. Contienen código Python independiente de la arquitectura y requieren una distribución que proporcione Python 3.12 o posterior.

### Desde el código fuente

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Para desarrollo

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Uso

### Uso básico

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Con umbrales

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Umbrales individuales

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Moneda diferente

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Tiempo de espera personalizado

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Frescura y presupuesto de reintentos

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Una cotización que incluya una marca de tiempo del proveedor debe tener como máximo una hora de antigüedad de forma predeterminada.
Los endpoints que devuelven solo un precio siguen siendo utilizables cuando `--max-age` está ausente.
Con `--max-age`, las marcas de tiempo del proveedor faltantes, inválidas, futuras u obsoletas devuelven `UNKNOWN`; el plugin no sustituye la hora de obtención local por la hora de cotización del proveedor. Una marca de tiempo exactamente en el límite de antigüedad sigue siendo aceptable. Las marcas de tiempo futuras siempre se rechazan.

La configuración predeterminada permite un reintento. Solo se reintentan errores de conexión, tiempos de espera agotados y respuestas HTTP 408/429/500/502/503/504. El retroceso exponencial comienza en 0.5 segundos y se duplica en los reintentos siguientes; los segundos de `Retry-After` y las fechas HTTP tienen prioridad. Todos los intentos, lecturas de respuesta, decodificación de JSON y esperas de reintento comparten el presupuesto de `--timeout`. Una espera de reintento que no quepa en el presupuesto devuelve `UNKNOWN` inmediatamente e informa el fallo que la motivó, como `HTTP 429` o `ConnectionError`, no un tiempo de espera agotado. No se reintentan fallos de autenticación, otros errores HTTP permanentes, JSON inválido ni respuestas de más de 64 KiB de datos decodificados. Usa `--retries 0` para deshabilitar los reintentos.

### Fuentes de cotización de respaldo

Usa opciones repetibles `--fallback-url URL` con endpoints compatibles con CoinGecko.
Por ejemplo, agrega `--fallback-url https://quotes.example.org/simple/price`.
Cada fuente recibe una parte equitativa del plazo restante de la solicitud, incluidos sus reintentos. Un fallo transitorio o un retraso de reintento mayor que esa parte avanza a la siguiente fuente. Los fallos de verificación TLS, los errores HTTP permanentes y las cotizaciones inválidas devuelven `UNKNOWN`. Cada respuesta de cotización está limitada a 64 KiB de datos decodificados.
Cuando se configuran respaldos, el estado identifica la fuente que responde como `primary`, `fallback1` y así sucesivamente, sin imprimir su URL.

### Variación en ventana corta

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Asigna al usuario de monitoreo un directorio de estado privado con permisos de escritura en un sistema de archivos local de Linux o macOS. Mantén el archivo hermano `.lock` en su lugar entre comprobaciones. Usa un archivo de estado separado por cada ventana. Las monedas tienen historiales independientes dentro de él.
La ventana predeterminada es de 3600 segundos. Cada cotización válida necesita una marca de tiempo del proveedor dentro de la ventana y del límite de antigüedad, que es de una hora a menos que `--max-age` establezca otro. El plugin compara el precio actual con el precio positivo anterior más antiguo en esa ventana e informa los segundos reales transcurridos. Las marcas de tiempo repetidas no crean muestras adicionales.
Una primera muestra, un historial expirado o un JSON corrupto inicia una nueva línea base; la métrica de la ventana es desconocida hasta que haya una muestra comparable. Las demás alertas siguen aplicándose. Un estado sin permisos de escritura, un archivo de estado o bloqueo que sea un enlace simbólico o una cotización más antigua que la muestra registrada más reciente devuelve `UNKNOWN`. La métrica con signo `bitcoin_move_window` utiliza rangos simétricos de advertencia y críticos. La igualdad en un límite no genera alerta.

El plugin abre el directorio de estado una vez por comprobación y trabaja de forma relativa a él, de modo que un componente de ruta reemplazado durante la comprobación no pueda redirigir el bloqueo, la lectura ni la escritura. Los enlaces simbólicos en la parte de directorio de la ruta se siguen al iniciar la comprobación, lo que mantiene utilizables enlaces de la plataforma como `/var` en macOS. Por lo tanto, el directorio de estado y sus directorios superiores no deben tener permisos de escritura para otros usuarios. Los archivos de estado y bloqueo se crean con modo 0600.

### Variación porcentual diaria

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Los umbrales de variación miden el valor absoluto de la variación porcentual diaria con signo de CoinGecko en la moneda seleccionada. Una variación exactamente en un umbral no genera alerta. Si se proporcionan ambos umbrales, el de advertencia no debe superar al crítico. Los datos de variación requeridos faltantes o inválidos devuelven `UNKNOWN`. Las alertas de precio y de variación pueden combinarse; prevalece la mayor gravedad, con prioridad del precio cuando las gravedades coinciden.

## Opciones de línea de comandos

| Opción | Descripción |
|--------|-------------|
| `-w`, `--warning` | Rango del umbral de advertencia (formato: LOW:HIGH) |
| `-c`, `--critical` | Rango del umbral crítico (formato: LOW:HIGH) |
| `--warning-low` | Umbral de advertencia para precio bajo |
| `--warning-high` | Umbral de advertencia para precio alto |
| `--critical-low` | Umbral crítico para precio bajo |
| `--critical-high` | Umbral crítico para precio alto |
| `--currency` | Código de moneda de 2 a 16 letras o dígitos (predeterminado: usd) |
| `--timeout` | Presupuesto total de solicitud/reintento de la API en segundos, incluidos valores fraccionarios (predeterminado: 10) |
| `--retries` | Intentos transitorios adicionales, 0-5 (predeterminado: 1) |
| `--max-age` | Antigüedad máxima de la cotización del proveedor en segundos y requisito de marca de tiempo; las cotizaciones con marca de tiempo usan 3600 de forma predeterminada |
| `--warning-change` | Límite de advertencia para la variación porcentual absoluta en 24 horas |
| `--critical-change` | Límite crítico para la variación porcentual absoluta en 24 horas |
| `--api-url` | URL de la API principal |
| `--fallback-url` | Endpoint compatible adicional; repetir en orden de preferencia |
| `--state-file` | Archivo JSON de historial de variaciones |
| `--move-window` | Ventana de variación en segundos (predeterminado: 3600) |
| `--warning-move`, `--critical-move` | Umbrales absolutos de variación en ventana en porcentaje |
| `-v`, `--verbose` | Habilitar salida detallada |
| `-V`, `--version` | Mostrar versión |
| `-h`, `--help` | Mostrar mensaje de ayuda |

## Configuración de Nagios

### Definición de comando

Establece la macro de recurso de Nagios `$USER1$` al directorio de plugins (los paquetes nativos usan `/usr/lib/nagios/plugins`). Agrega a tu configuración de comandos de Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Definición de servicio

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

### Configuración de Icinga2

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

## Códigos de salida

Argumentos inválidos, tiempos de espera no positivos, rangos de umbral inválidos y precios malformados de la API devuelven `UNKNOWN` (salida 3). Los umbrales deben ser números finitos y no negativos, con cada límite inferior no mayor que su límite superior. La moneda debe tener de 2 a 16 letras o dígitos. La configuración inválida se rechaza antes de contactar a la API. Los precios deben ser finitos y no negativos, proporcionados como números JSON o cadenas decimales simples como `"43521.5"`. Una respuesta sin la moneda solicitada la nombra, por ejemplo `Response has no EUR price`. Las respuestas inválidas no emiten datos de rendimiento. Los diagnósticos detallados se envían a stderr para que stdout contenga una única línea de estado de monitoreo.

| Código | Estado | Descripción |
|--------|--------|-------------|
| 0 | OK | El precio está dentro del rango aceptable |
| 1 | WARNING | El precio superó el umbral de advertencia |
| 2 | CRITICAL | El precio superó el umbral crítico |
| 3 | UNKNOWN | Ocurrió un error (fallo de API, tiempo de espera agotado, etc.) |

## Datos de rendimiento

El plugin genera datos de rendimiento en el formato estándar de Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Los datos de rendimiento de precio incluyen los rangos de advertencia y críticos configurados y un mínimo de cero. Los umbrales se imprimen en notación decimal completa, nunca redondeados ni en notación exponencial, de modo que valores grandes como `14500000:16250000` sigan siendo analizables. El tiempo de solicitud incluye todos los intentos y el retroceso. La antigüedad de la cotización se emite solo cuando el proveedor proporciona una marca de tiempo válida; la variación diaria se emite cuando está disponible. Los rangos de variación son simétricos alrededor de cero. Los datos inválidos u obsoletos producen `UNKNOWN` sin datos de rendimiento de precio. Estas métricas se pueden usar con herramientas de gráficos como PNP4Nagios, Grafana o InfluxDB.

## API

Este plugin utiliza de forma predeterminada la [API de CoinGecko](https://www.coingecko.com/en/api), que es gratuita y no requiere clave de API. Se aplican límites de tasa.

Los endpoints personalizados deben usar la misma estructura de respuesta: `bitcoin.<currency>` para el precio, `bitcoin.last_updated_at` para los segundos de marca de tiempo UNIX y `bitcoin.<currency>_24h_change` para la variación porcentual diaria con signo. Solo el precio es obligatorio cuando `--max-age` y los umbrales de variación están ausentes. Una marca de tiempo presente sigue siendo verificada: no debe estar en el futuro ni tener más de una hora de antigüedad. La respuesta decodificada debe caber en 64 KiB.

Las monedas admitidas incluyen: usd, eur, gbp, jpy, aud, cad, chf, cny y muchas más.

## Seguridad

Las medidas siguientes están implementadas en el código actual. Limitan lo que un endpoint con comportamiento erróneo o un usuario local puede hacer al host de monitoreo; no garantizan por sí mismas la fiabilidad de la cotización.

- Los certificados HTTPS se verifican con los valores predeterminados de `requests`, y ninguna opción deshabilita la verificación. Una `--api-url` personalizada que use `http://` sin cifrar no cuenta con esa protección.
- La resolución DNS, la conexión, las lecturas, los reintentos y el retroceso comparten el plazo límite de `--timeout`. Un interlocutor que envíe datos lentamente no puede extenderlo.
- Cada respuesta está limitada a 64 KiB después de la descompresión, y los cuerpos de redirección se descartan sin leerse.
- Los fallos de solicitud imprimen únicamente un estado HTTP o una clase de error, porque una `--api-url` personalizada puede contener credenciales.
- El comando instalado por `.deb` y `.rpm` ejecuta Python en modo aislado. Ignora `PYTHONPATH`, el directorio site del usuario y los módulos del directorio de trabajo. Una instalación con `pip` utiliza el script de consola estándar y sigue el entorno en el que está instalada.
- El estado de variación se lee y escribe sin seguir un enlace simbólico en el nombre del archivo de estado o de bloqueo, de forma relativa a un directorio abierto una vez por comprobación.
- Los archivos de lanzamiento incluyen atestaciones de procedencia de compilación además de `SHA256SUMS`; consulta [Desde GitHub Releases](#from-github-releases).

## Actualización desde 1.0.0

Estos cambios se incluyen en la versión 2.0.0.

- Una cotización con una marca de tiempo del proveedor de más de una hora de antigüedad devuelve `UNKNOWN` a menos que se indique un `--max-age` mayor. Los endpoints que no devuelven marca de tiempo no se ven afectados.
- `--currency` acepta solo de 2 a 16 letras o dígitos.
- Se rechazan cadenas numéricas con separadores de dígitos o espacios circundantes.
- Una espera de reintento que no cabe en el presupuesto informa el fallo subyacente en lugar de `API request timed out`.
- Los paquetes nativos ya no respetan `PYTHONPATH`.
- Los umbrales de un millón o más aparecen en los datos de rendimiento como decimales simples en lugar de notación exponencial.

## Localización

La ayuda de la línea de comandos, los errores de validación y las descripciones de estado del plugin admiten 45 configuraciones regionales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) mediante catálogos integrados cargados con la biblioteca estándar. La resolución comprueba `--lang`, luego `LC_ALL`, `LC_MESSAGES` y `LANG`, con respaldo en `en`. Los prefijos de estado de Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) y los datos de rendimiento permanecen sin cambios en todas las configuraciones regionales.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Desarrollo

Instala [mise](https://mise.jdx.dev/getting-started.html) y luego ejecuta la configuración de desarrollo anterior. `mise.toml` fija las versiones de Python y uv. Las herramientas de desarrollo están declaradas en `pyproject.toml` y resueltas en el archivo `uv.lock` confirmado en el repositorio.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Instala los hooks de commit después de la configuración:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Usa `mise exec -- uv add --dev <tool>` o `mise exec -- uv add <dependency>` para actualizar dependencias y confirma tanto `pyproject.toml` como `uv.lock`.

CI comprueba Python 3.12 y 3.13 en Linux y Python 3.13 en macOS. Cada PR también ejecuta validación de paquetes, auditoría de dependencias y CodeQL, e instala el `.deb` en Ubuntu y el `.rpm` en Fedora. Las distribuciones compiladas están disponibles como el artefacto `distributions` en las ejecuciones de CI.

La versión del paquete y de la CLI proviene de `check_bitcoin_price/__init__.py`. Consulta [el proceso de lanzamiento](../../../CONTRIBUTING.md#releases) para incrementar versiones y publicar automáticamente los archivos de lanzamiento en GitHub.

## Contribuciones

Consulta [CONTRIBUTING.md](../../../CONTRIBUTING.md) para conocer el flujo de trabajo de desarrollo y los requisitos de commits con firma DCO.

## Licencia

Este proyecto está bajo la Licencia MIT; consulta el archivo [LICENSE](../../../LICENSE) para más detalles.

## Autor

Thomas Vincent

## Agradecimientos

- [CoinGecko](https://www.coingecko.com/) por proporcionar una API gratuita de criptomonedas
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
