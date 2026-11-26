# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · **Português (BR)** · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Um plugin para Nagios/Icinga para monitorar o preço do Bitcoin com limites de aviso e críticos configuráveis.

## Recursos

- Monitore o preço do Bitcoin em várias moedas (USD, EUR, GBP, etc.)
- Limites de aviso e críticos configuráveis (máximo e mínimo)
- Saída padrão de plugin Nagios com dados de desempenho
- Usa a API do CoinGecko (gratuita, sem necessidade de chave de API)
- Suporte a endpoints de API personalizados
- Tempo limite (timeout) configurável
- Verificações de atualidade da cotação usando timestamps do fornecedor, com limite padrão de uma hora
- Tentativas limitadas para limites de taxa (rate limits) e falhas temporárias da API
- Um prazo único para todas as tentativas e limite de 64 KiB por resposta
- Alertas opcionais sobre variação percentual absoluta em 24 horas
- Limites de preço, duração da requisição e idade da cotação nos dados de desempenho

## Instalação

### A partir dos GitHub Releases

Baixe os arquivos `.deb`, `.rpm`, `.tar.gz`, wheel e `SHA256SUMS` em [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). Verifique o download com `sha256sum --ignore-missing --check SHA256SUMS`. Versões posteriores à 1.0.0 também trazem proveniência de build assinada; confirme que um ativo veio do fluxo de lançamento deste repositório com `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

Use os nomes de arquivo da versão selecionada. Os pacotes nativos instalam `/usr/bin/check_bitcoin_price` e `/usr/lib/nagios/plugins/check_bitcoin_price`; o RPM também fornece `/usr/lib64/nagios/plugins/check_bitcoin_price`. O comando empacotado executa o Python em modo isolado, portanto ignora `PYTHONPATH` e módulos no diretório de trabalho; o gerenciador de pacotes do sistema resolve as dependências do Python e do `requests`. Eles contêm código Python independente de arquitetura e exigem uma distribuição com Python 3.12 ou mais recente.

### A partir do código-fonte

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### Para desenvolvimento

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

### Com limites

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### Limites individuais

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### Outra moeda

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### Tempo limite personalizado

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### Atualidade e orçamento de tentativas

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

Uma cotação que contenha um timestamp do fornecedor deve ter no máximo uma hora por padrão.
Endpoints que retornam apenas um preço continuam utilizáveis quando `--max-age` está ausente.
Com `--max-age`, timestamps do fornecedor ausentes, inválidos, futuros ou desatualizados retornam
`UNKNOWN`; o plugin não substitui o horário da cotação do fornecedor pelo horário local da consulta.
Um timestamp exatamente no limite de idade continua aceitável. Timestamps
futuros são sempre rejeitados.

O padrão permite uma nova tentativa. Apenas erros de conexão, timeouts e respostas HTTP
408/429/500/502/503/504 são repetidos. O backoff começa em 0,5 segundo e
dobra nas tentativas seguintes; segundos em `Retry-After` e datas HTTP têm
precedência. Todas as tentativas, leituras de resposta, decodificação JSON e esperas de repetição compartilham
o orçamento de `--timeout`. Uma espera de repetição que não caiba no prazo retorna `UNKNOWN` imediatamente
e informa a falha que a originou, como `HTTP 429` ou `ConnectionError`,
não um timeout. Falhas de autenticação, outros erros HTTP permanentes, JSON inválido
e respostas maiores que 64 KiB de dados decodificados não são repetidos. Use
`--retries 0` para desativar novas tentativas.

### Fontes de cotação de fallback

Use opções repetíveis `--fallback-url URL` com endpoints compatíveis com CoinGecko.
Por exemplo, adicione `--fallback-url https://quotes.example.org/simple/price`.
Cada fonte recebe uma parcela igual do prazo restante da requisição, incluindo suas
novas tentativas. Uma falha transitória ou um atraso de repetição maior que essa parcela avança para
a próxima fonte. Falhas de verificação TLS, erros HTTP permanentes e cotações inválidas
retornam UNKNOWN. Cada resposta de cotação é limitada a 64 KiB de dados decodificados.
Quando fallbacks são configurados, o status identifica a fonte que respondeu como
`primary`, `fallback1` e assim por diante, sem exibir sua URL.

### Variação em janela curta

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

Forneça ao usuário de monitoramento um diretório de estado privado e gravável em um sistema de arquivos local Linux ou
macOS. Mantenha o arquivo irmão `.lock` no lugar entre as verificações. Use um
arquivo de estado separado por janela. As moedas têm históricos independentes dentro dele.
A janela padrão é de 3600 segundos. Cada cotação válida precisa de um timestamp do fornecedor
dentro da janela e do limite de idade, que é de uma hora, salvo se `--max-age` definir
outro. O plugin compara o preço atual
com o preço positivo anterior mais antigo nessa janela e informa os
segundos reais decorridos. Timestamps repetidos não criam amostras adicionais.
Uma primeira amostra, histórico expirado ou JSON corrompido inicia uma nova linha de base; a
métrica da janela fica desconhecida até que haja uma amostra comparável. Outros alertas ainda se
aplicam. Estado sem permissão de gravação, arquivo de estado ou de lock que seja link simbólico, ou cotação mais antiga
que a amostra mais recente registrada retorna UNKNOWN. A métrica com sinal `bitcoin_move_window`
usa faixas simétricas de aviso e críticas. Igualdade exata no limite não gera alerta.

O plugin abre o diretório de estado uma vez por verificação e opera de forma relativa a ele, de modo que
um componente de caminho substituído durante a verificação não possa redirecionar o lock, a leitura
ou a gravação. Links simbólicos na parte de diretório do caminho são seguidos quando
a verificação começa, o que mantém utilizáveis links da plataforma como `/var` no macOS. O
diretório de estado e seus ancestrais não devem, portanto, ter permissão de escrita para outros
usuários. Os arquivos de estado e de lock são criados com permissão 0600.

### Variação percentual diária

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

Os limites de variação medem o valor absoluto da variação percentual de 24 horas com sinal
do CoinGecko na moeda selecionada. Uma variação exatamente no limite não
gera alerta. Se ambos os limites forem informados, o de aviso não deve exceder o crítico.
Dados de variação obrigatórios ausentes ou inválidos retornam `UNKNOWN`. Alertas de preço e de variação
podem ser combinados; vence a maior severidade, com o preço tendo precedência
quando as severidades forem iguais.

## Opções de linha de comando

| Opção | Descrição |
|-------|-----------|
| `-w`, `--warning` | Faixa de limite de aviso (formato: LOW:HIGH) |
| `-c`, `--critical` | Faixa de limite crítico (formato: LOW:HIGH) |
| `--warning-low` | Limite de aviso para preço mínimo |
| `--warning-high` | Limite de aviso para preço máximo |
| `--critical-low` | Limite crítico para preço mínimo |
| `--critical-high` | Limite crítico para preço máximo |
| `--currency` | Código de moeda de 2 a 16 letras ou dígitos (padrão: usd) |
| `--timeout` | Orçamento total de requisição/repetição da API em segundos, incluindo valores fracionários (padrão: 10) |
| `--retries` | Tentativas transitórias adicionais, 0 a 5 (padrão: 1) |
| `--max-age` | Idade máxima da cotação do fornecedor em segundos e exige timestamp; cotações com timestamp usam 3600 por padrão |
| `--warning-change` | Limite de aviso para variação percentual absoluta em 24 horas |
| `--critical-change` | Limite crítico para variação percentual absoluta em 24 horas |
| `--api-url` | URL da API primária |
| `--fallback-url` | Endpoint compatível adicional; repita na ordem de preferência |
| `--state-file` | Arquivo JSON de histórico de variação |
| `--move-window` | Janela de variação em segundos (padrão: 3600) |
| `--warning-move`, `--critical-move` | Limites absolutos de variação na janela em porcentagem |
| `-v`, `--verbose` | Ativar saída detalhada |
| `-V`, `--version` | Exibir versão |
| `-h`, `--help` | Exibir mensagem de ajuda |

## Configuração do Nagios

### Definição de comando

Defina a macro de recurso do Nagios `$USER1$` para o diretório do plugin (os pacotes nativos usam `/usr/lib/nagios/plugins`). Adicione à configuração de comandos do Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### Definição de serviço

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

### Configuração do Icinga2

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

## Códigos de saída

Argumentos inválidos, timeouts não positivos, faixas de limites inválidas e preços da API
malformados retornam `UNKNOWN` (saída 3). Os limites devem ser números finitos e não negativos,
com cada limite inferior menor ou igual ao respectivo limite superior. A moeda deve
ter de 2 a 16 letras ou dígitos. Configurações inválidas são rejeitadas antes de contatar
a API. Os preços devem ser finitos e não negativos, fornecidos como números JSON ou strings
decimais simples como `"43521.5"`. Uma resposta sem a moeda solicitada
indica seu nome, por exemplo `Response has no EUR price`. Respostas inválidas não emitem
dados de desempenho. Diagnósticos detalhados vão para stderr
para que stdout contenha uma única linha de status de monitoramento.

| Código | Status | Descrição |
|--------|--------|-----------|
| 0 | OK | O preço está dentro da faixa aceitável |
| 1 | WARNING | O preço ultrapassou o limite de aviso |
| 2 | CRITICAL | O preço ultrapassou o limite crítico |
| 3 | UNKNOWN | Ocorreu um erro (falha na API, timeout, etc.) |

## Dados de desempenho

O plugin gera dados de desempenho no formato padrão do Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

Os dados de desempenho de preço incluem as faixas de aviso/críticas configuradas e um
mínimo igual a zero. Os limites são impressos em notação decimal completa, nunca arredondados
nem em notação exponencial, para que valores grandes como `14500000:16250000` permaneçam analisáveis. O tempo de requisição inclui todas as tentativas e o backoff. A idade da cotação é
emitida apenas quando o fornecedor envia um timestamp válido; a variação diária é emitida
quando disponível. As faixas de variação são simétricas em torno de zero. Dados inválidos ou desatualizados
produzem `UNKNOWN` sem dados de desempenho de preço. Essas métricas podem ser usadas com
ferramentas de gráficos como PNP4Nagios, Grafana ou InfluxDB.

## API

Este plugin usa a [API do CoinGecko](https://www.coingecko.com/en/api) por padrão, que é gratuita e não exige chave de API. Limites de taxa se aplicam.

Endpoints personalizados devem usar o mesmo formato de resposta: `bitcoin.<currency>` para
preço, `bitcoin.last_updated_at` para segundos de timestamp UNIX e
`bitcoin.<currency>_24h_change` para a variação percentual diária com sinal. Apenas o preço
é obrigatório quando `--max-age` e os limites de variação estão ausentes. Um timestamp
presente ainda é verificado: ele não pode estar no futuro nem ter mais de uma
hora. A resposta decodificada deve caber em 64 KiB.

As moedas suportadas incluem: usd, eur, gbp, jpy, aud, cad, chf, cny e muitas outras.

## Segurança

As medidas abaixo estão implementadas no código atual. Elas limitam o que um endpoint malcomportado ou um usuário local pode fazer ao
host de monitoramento; elas não tornam a cotação em si confiável.

- Os certificados HTTPS são verificados com os padrões do `requests`, e nenhuma opção
  desativa a verificação. Um `--api-url` personalizado que use `http://` simples não tem
  essa proteção.
- DNS, conexão, leituras, repetições e backoff compartilham o prazo de `--timeout`. Um
  par remoto que envie dados lentamente não consegue estendê-lo.
- Cada resposta é limitada a 64 KiB após a descompressão, e corpos de redirecionamento
  são descartados sem leitura.
- Falhas de requisição exibem apenas um status HTTP ou uma classe de erro, porque um
  `--api-url` personalizado pode conter credenciais.
- O comando instalado pelo `.deb` e pelo `.rpm` executa o Python em modo isolado.
  Ele ignora `PYTHONPATH`, o diretório de pacotes do usuário e módulos no diretório de
  trabalho. Uma instalação via `pip` usa o script de console padrão e segue
  o ambiente em que está instalada.
- O estado de variação é lido e gravado sem seguir links simbólicos no nome do
  arquivo de estado ou de lock, em relação a um diretório aberto uma vez por verificação.
- Os ativos de lançamento carregam atestações de proveniência de build além de
  `SHA256SUMS`; consulte [A partir dos GitHub Releases](#from-github-releases).

## Atualizando a partir da versão 1.0.0

Estas alterações são incluídas na versão 2.0.0.

- Uma cotação com timestamp do fornecedor mais antigo que uma hora retorna `UNKNOWN`, a menos que um
  `--max-age` maior seja informado. Endpoints que não retornam timestamp não são afetados.
- `--currency` aceita apenas de 2 a 16 letras ou dígitos.
- Strings numéricas com separadores de dígitos ou espaços ao redor são rejeitadas.
- Uma espera de repetição que não caiba no orçamento informa a falha subjacente
  em vez de `API request timed out`.
- Os pacotes nativos não respeitam mais `PYTHONPATH`.
- Limites de um milhão ou mais aparecem nos dados de desempenho como decimais
  simples em vez de notação exponencial.

## Localização

A ajuda da CLI, os erros de validação e as descrições de status do plugin oferecem suporte a 45 localidades (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) usando catálogos empacotados carregados pela biblioteca padrão. A resolução verifica `--lang`, depois `LC_ALL`, `LC_MESSAGES` e `LANG`, recorrendo a `en` como fallback. Os prefixos de status do Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) e os dados de desempenho permanecem inalterados em todas as localidades.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## Desenvolvimento

Instale o [mise](https://mise.jdx.dev/getting-started.html) e execute a configuração de desenvolvimento acima. O arquivo `mise.toml` fixa as versões do Python e do uv. As ferramentas de desenvolvimento são declaradas em `pyproject.toml` e resolvidas no arquivo `uv.lock` commitado.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

Instale os hooks de commit após a configuração:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

Use `mise exec -- uv add --dev <tool>` ou `mise exec -- uv add <dependency>` para atualizar dependências e faça o commit tanto de `pyproject.toml` quanto de `uv.lock`.

A CI verifica o Python 3.12 e 3.13 no Linux e o Python 3.13 no macOS. Cada PR também executa validação de pacotes, auditoria de dependências e CodeQL, além de instalar o `.deb` no Ubuntu e o `.rpm` no Fedora. As distribuições compiladas ficam disponíveis como o artefato `distributions` nas execuções de CI.

A versão do pacote e da CLI vem de `check_bitcoin_price/__init__.py`. Consulte [o processo de lançamento](../../../CONTRIBUTING.md#releases) para incrementos de versão e publicação automatizada dos ativos de lançamento no GitHub.

## Contribuição

Consulte [CONTRIBUTING.md](../../../CONTRIBUTING.md) para o fluxo de trabalho de desenvolvimento e requisitos de commits assinados (signed-off).

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](../../../LICENSE) para obter detalhes.

## Autor

Thomas Vincent

## Agradecimentos

- [CoinGecko](https://www.coingecko.com/) por fornecer uma API gratuita de criptomoedas
- [Diretrizes de Desenvolvimento de Plugins do Nagios](https://nagios-plugins.org/doc/guidelines.html)
