# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · **Français (Maroc)** · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Un plugin Nagios/Icinga pour surveiller le cours du Bitcoin avec des seuils d'avertissement et des seuils critiques configurables.

## Fonctionnalités

- Surveiller le cours du Bitcoin dans plusieurs devises (USD, EUR, GBP, etc.)
- Seuils d'avertissement et seuils critiques configurables (haut et bas)
- Sortie standard de plugin Nagios avec données de performance
- Utilise l'API CoinGecko (gratuite, aucune clé API requise)
- Prise en charge de points de terminaison API personnalisés
- Délai d'expiration (timeout) configurable
- Vérification de la fraîcheur des cotations à partir des horodatages du fournisseur, avec une limite d'une heure par défaut
- Tentatives bornées en cas de limitation de débit (rate limit) et de pannes temporaires de l'API
- Une échéance globale pour l'ensemble des tentatives et un plafond de 64 Kio par réponse
- Alertes optionnelles sur la variation absolue en pourcentage sur 24 heures
- Seuils de prix, durée des requêtes et âge de la cotation inclus dans les données de performance

## Installation

<a name="from-github-releases"></a>

### Depuis GitHub Releases

Téléchargez les fichiers `.deb`, `.rpm`, `.tar.gz`, wheel et `SHA256SUMS` depuis [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Vérifiez un téléchargement avec `sha256sum --ignore-missing --check SHA256SUMS`. Les versions postérieures à 1.0.0 incluent également une attestation de provenance de build signée ; confirmez qu'un fichier provient bien du workflow de publication de ce dépôt avec `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Utilisez les noms de fichiers correspondant à la version sélectionnée. Les paquets natifs installent `/usr/bin/check_bitcoin_price` et `/usr/lib/nagios/plugins/check_bitcoin_price` ; le paquet RPM fournit aussi `/usr/lib64/nagios/plugins/check_bitcoin_price`. La commande empaquetée exécute Python en mode isolé, ignorant ainsi `PYTHONPATH` et les modules présents dans le répertoire courant ; le gestionnaire de paquets du système résout les dépendances Python et `requests`. Ils contiennent du code Python indépendant de l'architecture et nécessitent une distribution fournissant Python 3.12 ou une version ultérieure.

### Depuis les sources

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Pour le développement

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## Utilisation

### Utilisation de base

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### Avec des seuils

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Seuils individuels

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Autre devise

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Délai d'expiration personnalisé

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Fraîcheur des données et budget de tentatives

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Par défaut, une cotation comportant un horodatage du fournisseur doit dater d'au maximum une heure. Les points de terminaison qui ne renvoient qu'un prix restent utilisables lorsque `--max-age` n'est pas spécifié. Avec `--max-age`, un horodatage fournisseur absent, invalide, dans le futur ou périmé renvoie `UNKNOWN` ; le plugin ne remplace pas l'horodatage de la cotation du fournisseur par l'heure locale de récupération. Un horodatage exactement égal à la limite d'âge reste acceptable. Les horodatages dans le futur sont toujours rejetés.

La configuration par défaut autorise une nouvelle tentative. Seules les erreurs de connexion, les dépassements de délai et les réponses HTTP 408/429/500/502/503/504 font l'objet d'une nouvelle tentative. Le délai d'attente (backoff) commence à 0,5 seconde et double à chaque tentative suivante ; les secondes et dates HTTP de l'en-tête `Retry-After` ont la priorité. Toutes les tentatives, lectures de réponse, décodages JSON et attentes avant nouvelle tentative partagent le budget défini par `--timeout`. Une attente qui dépasse le budget restant renvoie immédiatement `UNKNOWN` et signale l'erreur qui l'a déclenchée, telle que `HTTP 429` ou `ConnectionError`, et non un dépassement de délai. Les échecs d'authentification, les autres erreurs HTTP permanentes, le JSON invalide et les réponses dépassant 64 Kio de données décodées ne sont pas relancés. Utilisez `--retries 0` pour désactiver les nouvelles tentatives.

### Sources de cotation de secours (fallback)

Utilisez des options `--fallback-url URL` répétables avec des points de terminaison compatibles CoinGecko. Par exemple, ajoutez `--fallback-url https://quotes.example.org/simple/price`. Chaque source reçoit une part égale du délai restant de la requête, nouvelles tentatives incluses. Une défaillance transitoire ou un délai d'attente supérieur à cette part fait passer à la source suivante. Les échecs de vérification TLS, les erreurs HTTP permanentes et les cotations invalides renvoient UNKNOWN. Chaque réponse de cotation est limitée à 64 Kio de données décodées. Lorsque des sources de secours sont configurées, le statut identifie la source ayant répondu par `primary`, `fallback1`, et ainsi de suite, sans afficher son URL.

### Variation sur fenêtre courte

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Attribuez à l'utilisateur de supervision un répertoire d'état privé et accessible en écriture sur un système de fichiers local Linux ou macOS. Conservez le fichier `.lock` associé en place entre les vérifications. Utilisez un fichier d'état distinct par fenêtre. Les devises disposent d'historiques indépendants à l'intérieur de ce fichier. La fenêtre par défaut est de 3600 secondes. Chaque cotation valide doit comporter un horodatage fournisseur compris dans la fenêtre et dans la limite d'âge, fixée à une heure sauf si `--max-age` en définit une autre. Le plugin compare le cours actuel au prix positif antérieur le plus ancien dans cette fenêtre et signale le nombre réel de secondes écoulées. Les horodatages répétés ne créent pas d'échantillons supplémentaires. Un premier échantillon, un historique expiré ou un fichier JSON corrompu démarre une nouvelle référence ; la métrique de fenêtre reste inconnue jusqu'à ce qu'un échantillon comparable soit disponible. Les autres alertes continuent de s'appliquer. Un état non accessible en écriture, un fichier d'état ou de verrou qui est un lien symbolique, ou une cotation plus ancienne que l'échantillon enregistré le plus récent renvoie UNKNOWN. La métrique signée `bitcoin_move_window` utilise des plages symétriques d'avertissement et critiques. L'égalité exacte avec une limite ne déclenche pas d'alerte.

Le plugin ouvre le répertoire d'état une seule fois par vérification et travaille relativement à celui-ci, de sorte qu'un composant de chemin remplacé pendant la vérification ne puisse rediriger ni le verrou, ni la lecture, ni l'écriture. Les liens symboliques présents dans la partie répertoire du chemin sont suivis au démarrage de la vérification, ce qui permet de garder utilisables des liens système tels que `/var` sur macOS. Le répertoire d'état et ses répertoires parents ne doivent donc pas être accessibles en écriture par d'autres utilisateurs. Les fichiers d'état et de verrou sont créés avec le mode 0600.

### Variation journalière en pourcentage

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Les seuils de variation mesurent la valeur absolue de la variation signée en pourcentage sur 24 heures fournie par CoinGecko dans la devise sélectionnée. Une variation exactement égale à un seuil ne déclenche pas d'alerte. Si les deux seuils sont fournis, le seuil d'avertissement ne doit pas dépasser le seuil critique. Des données de variation requises absentes ou invalides renvoient `UNKNOWN`. Les alertes de prix et de variation peuvent être combinées ; la sévérité la plus élevée l'emporte, le prix ayant la priorité à sévérité égale.

## Options de ligne de commande

| Option | Description |
|--------|-------------|
| `-w`, `--warning` | Plage de seuils d'avertissement (format : LOW:HIGH) |
| `-c`, `--critical` | Plage de seuils critiques (format : LOW:HIGH) |
| `--warning-low` | Seuil d'avertissement pour le prix bas |
| `--warning-high` | Seuil d'avertissement pour le prix haut |
| `--critical-low` | Seuil critique pour le prix bas |
| `--critical-high` | Seuil critique pour le prix haut |
| `--currency` | Code de devise de 2 à 16 lettres ou chiffres (par défaut : usd) |
| `--timeout` | Budget total de requête/tentatives API en secondes, valeurs décimales incluses (par défaut : 10) |
| `--retries` | Tentatives supplémentaires sur erreur transitoire, de 0 à 5 (par défaut : 1) |
| `--max-age` | Âge maximal de la cotation fournisseur en secondes et exigence d'un horodatage ; par défaut 3600 pour les cotations horodatées |
| `--warning-change` | Limite d'avertissement pour la variation absolue en pourcentage sur 24 heures |
| `--critical-change` | Limite critique pour la variation absolue en pourcentage sur 24 heures |
| `--api-url` | URL principale de l'API |
| `--fallback-url` | Point de terminaison compatible supplémentaire ; à répéter par ordre de préférence |
| `--state-file` | Fichier JSON d'historique des variations |
| `--move-window` | Fenêtre de variation en secondes (par défaut : 3600) |
| `--warning-move`, `--critical-move` | Seuils absolus de variation sur la fenêtre, en pourcentage |
| `-v`, `--verbose` | Activer la sortie détaillée (verbose) |
| `-V`, `--version` | Afficher la version |
| `-h`, `--help` | Afficher le message d'aide |

## Configuration Nagios

### Définition de la commande

Définissez la macro de ressource Nagios `$USER1$` sur le répertoire des plugins (les paquets natifs utilisent `/usr/lib/nagios/plugins`). Ajoutez ceci à votre configuration de commandes Nagios :

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Définition du service

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

### Configuration Icinga2

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

## Codes de sortie

Les arguments invalides, les délais d'expiration inférieurs ou égaux à zéro, les plages de seuils invalides et les prix API mal formés renvoient `UNKNOWN` (code de sortie 3). Les seuils doivent être des nombres finis, positifs ou nuls, chaque borne inférieure ne pouvant dépasser sa borne supérieure. La devise doit comporter entre 2 et 16 lettres ou chiffres. Toute configuration invalide est rejetée avant de contacter l'API. Les prix doivent être finis et positifs ou nuls, fournis sous forme de nombres JSON ou de chaînes décimales simples comme `"43521.5"`. Une réponse ne contenant pas la devise demandée la mentionne explicitement, par exemple `Response has no EUR price`. Les réponses invalides n'émettent pas de données de performance. Les diagnostics détaillés sont écrits sur stderr afin que stdout ne contienne qu'une seule ligne d'état de supervision.

| Code | Statut | Description |
|------|--------|-------------|
| 0 | OK | Le cours se situe dans la plage acceptable |
| 1 | WARNING | Le cours a franchi le seuil d'avertissement |
| 2 | CRITICAL | Le cours a franchi le seuil critique |
| 3 | UNKNOWN | Une erreur s'est produite (panne d'API, expiration du délai, etc.) |

## Données de performance

Le plugin génère des données de performance au format standard Nagios :

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Les données de performance du prix incluent les plages d'avertissement/critiques configurées ainsi qu'un minimum fixé à zéro. Les seuils sont affichés en notation décimale complète, jamais arrondis ni en notation scientifique, afin que les grandes valeurs comme `14500000:16250000` restent analysables. Le temps de requête englobe toutes les tentatives et les délais d'attente (backoff). L'âge de la cotation n'est émis que lorsque le fournisseur transmet un horodatage valide ; la variation journalière est émise lorsqu'elle est disponible. Les plages de variation sont symétriques autour de zéro. Des données invalides ou périmées produisent `UNKNOWN` sans données de performance de prix. Ces métriques peuvent être exploitées avec des outils de création de graphiques comme PNP4Nagios, Grafana ou InfluxDB.

## API

Ce plugin utilise par défaut l'[API CoinGecko](https://www.coingecko.com/en/api), qui est gratuite et ne requiert pas de clé API. Des limites de débit s'appliquent.

Les points de terminaison personnalisés doivent respecter la même structure de réponse : `bitcoin.<currency>` pour le prix, `bitcoin.last_updated_at` pour l'horodatage UNIX en secondes et `bitcoin.<currency>_24h_change` pour la variation journalière signée en pourcentage. Seul le prix est obligatoire lorsque `--max-age` et les seuils de variation ne sont pas utilisés. Lorsqu'un horodatage est présent, il reste vérifié : il ne doit être ni dans le futur ni vieux de plus d'une heure. La réponse décodée doit tenir dans 64 Kio.

Parmi les devises prises en charge figurent : usd, eur, gbp, jpy, aud, cad, chf, cny, et bien d'autres.

## Sécurité

Les mesures ci-dessous sont implémentées dans le code actuel. Elles limitent ce qu'un point de terminaison défaillant ou un utilisateur local peut faire sur l'hôte de supervision ; elles ne garantissent pas la fiabilité de la cotation elle-même.

- Les certificats HTTPS sont vérifiés selon les paramètres par défaut de `requests`, et aucune option ne permet de désactiver cette vérification. Une option `--api-url` personnalisée utilisant du simple `http://` ne bénéficie pas de cette protection.
- La résolution DNS, la connexion, les lectures, les nouvelles tentatives et le backoff partagent l'échéance définie par `--timeout`. Un pair qui transmet des données lentement ne peut pas la prolonger.
- Chaque réponse est limitée à 64 Kio après décompression, et les corps de redirection sont ignorés sans être lus.
- Les échecs de requête affichent uniquement un statut HTTP ou une classe d'erreur, car une option `--api-url` personnalisée peut contenir des identifiants.
- La commande installée par les paquets `.deb` et `.rpm` exécute Python en mode isolé. Elle ignore `PYTHONPATH`, le répertoire site utilisateur et les modules du répertoire courant. Une installation via `pip` utilise le script console standard et suit l'environnement dans lequel elle est installée.
- L'état des variations est lu et écrit sans suivre de lien symbolique au niveau du nom du fichier d'état ou de verrou, relativement à un répertoire ouvert une seule fois par vérification.
- Les fichiers de publication incluent des attestations de provenance de build en plus de `SHA256SUMS` ; voir [Depuis GitHub Releases](#from-github-releases).

## Mise à niveau depuis la version 1.0.0

Ces changements sont introduits dans la version 2.0.0.

- Une cotation dont l'horodatage fournisseur date de plus d'une heure renvoie `UNKNOWN`, sauf si une valeur `--max-age` plus élevée est indiquée. Les points de terminaison qui ne renvoient pas d'horodatage ne sont pas affectés.
- `--currency` n'accepte que 2 à 16 lettres ou chiffres.
- Les chaînes numériques contenant des séparateurs de chiffres ou des espaces autour sont rejetées.
- Une attente avant nouvelle tentative qui ne rentre pas dans le budget signale l'erreur sous-jacente au lieu de `API request timed out`.
- Les paquets natifs ne tiennent plus compte de `PYTHONPATH`.
- Les seuils d'un million ou plus apparaissent dans les données de performance en notation décimale simple plutôt qu'en notation scientifique.

## Localisation

L'aide CLI, les erreurs de validation et les descriptions d'état du plugin prennent en charge 45 locales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) à l'aide de catalogues intégrés chargés par la bibliothèque standard. La résolution vérifie `--lang`, puis `LC_ALL`, `LC_MESSAGES` et `LANG`, avec repli sur `en`. Les préfixes d'état Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) et les données de performance restent inchangés dans toutes les locales.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Développement

Installez [mise](https://mise.jdx.dev/getting-started.html), puis lancez la configuration de développement ci-dessus. `mise.toml` fige les versions de Python et de uv. Les outils de développement sont déclarés dans `pyproject.toml` et résolus dans le fichier `uv.lock` suivi par Git.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Installez les hooks de commit après la configuration :

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Utilisez `mise exec -- uv add --dev <tool>` ou `mise exec -- uv add <dependency>` pour mettre à jour les dépendances et validez (commit) à la fois `pyproject.toml` et `uv.lock`.

La CI vérifie Python 3.12 et 3.13 sur Linux ainsi que Python 3.13 sur macOS. Chaque PR exécute également la validation des paquets, l'audit des dépendances et CodeQL, et installe le `.deb` sur Ubuntu ainsi que le `.rpm` sur Fedora. Les distributions générées sont disponibles en tant qu'artefact `distributions` lors des exécutions CI.

La version du paquet et de la CLI provient de `check_bitcoin_price/__init__.py`. Consultez [le processus de publication](../../../CONTRIBUTING.md#releases) pour les incrémentations de version et la publication automatisée des fichiers de version sur GitHub.

## Contribuer

Consultez [CONTRIBUTING.md](../../../CONTRIBUTING.md) pour le workflow de développement et les exigences relatives aux commits signés (signed-off).

## Licence

Ce projet est distribué sous licence MIT - consultez le fichier [LICENSE](../../../LICENSE) pour plus de détails.

## Auteur

Thomas Vincent

## Remerciements

- [CoinGecko](https://www.coingecko.com/) pour la mise à disposition d'une API gratuite sur les cryptomonnaies
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
