# check_bitcoin_price

[![CI](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/somethingwithproof/check_bitcoin_price/actions/workflows/ci.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=somethingwithproof_check_bitcoin_price&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=somethingwithproof_check_bitcoin_price)
[![Release](https://img.shields.io/github/v/release/somethingwithproof/check_bitcoin_price)](https://github.com/somethingwithproof/check_bitcoin_price/releases)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/somethingwithproof/check_bitcoin_price/main/pyproject.toml)](../../../pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](../../../LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/somethingwithproof/check_bitcoin_price/badge)](https://scorecard.dev/viewer/?uri=github.com/somethingwithproof/check_bitcoin_price)

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · **עברית** · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

תוסף Nagios/Icinga לניטור מחיר Bitcoin עם ספי אזהרה וקריטיות הניתנים להגדרה.

## תכונות

- ניטור מחיר Bitcoin במטבעות מרובים (USD, EUR, GBP ועוד)
- ספי אזהרה וקריטיות הניתנים להגדרה (גבוה ונמוך)
- פלט תוסף תקני של Nagios עם נתוני ביצועים
- שימוש ב-CoinGecko API (חינמי, ללא צורך במפתח API)
- תמיכה בנקודות קצה מותאמות אישית של API
- זמן קצוב (timeout) ניתן להגדרה
- בדיקות עדכניות ציטוט באמצעות חותמות זמן של הספק, עם מגבלת ברירת מחדל של שעה אחת
- ניסיונות חוזרים מוגבלים עבור הגבלות קצב וכשלי API זמניים
- מועד יעד אחד לכל הניסיונות ומגבלה של 64 KiB על כל תגובה
- התראות אופציונליות על תנועה מוחלטת באחוזים ב-24 שעות
- ספי מחיר, משך בקשה וגיל הציטוט בנתוני הביצועים

## התקנה

<a name="from-github-releases"></a>

### מתוך GitHub Releases

הורידו קבצי `.deb`, `.rpm`, `.tar.gz`, wheel ו-`SHA256SUMS` מתוך [GitHub Releases](https://github.com/somethingwithproof/check_bitcoin_price/releases). אמתו את ההורדה באמצעות `sha256sum --ignore-missing --check SHA256SUMS`. מהדורות לאחר 1.0.0 כוללות גם אישור מקור בנייה חתום; ודאו שנכס הגיע מתהליך העבודה של שחרור המהדורות במאגר זה באמצעות `gh attestation verify <file> --repo somethingwithproof/check_bitcoin_price`.

```bash
# Debian/Ubuntu with Python >=3.12 (for example Ubuntu 24.04)
sudo apt install ./check-bitcoin-price_2.0.0-1_all.deb

# Fedora or another RPM distribution with Python >=3.12
sudo dnf install ./check-bitcoin-price-2.0.0-1.noarch.rpm

# Python source archive
pip install ./check_bitcoin_price-2.0.0.tar.gz
```

השתמשו בשמות הקבצים מהמהדורה שנבחרה. חבילות מקוריות מתקינות את `/usr/bin/check_bitcoin_price` ואת `/usr/lib/nagios/plugins/check_bitcoin_price`; חבילת ה-RPM מספקת גם את `/usr/lib64/nagios/plugins/check_bitcoin_price`. הפקודה הארוזה מריצה Python במצב מבודד, ולכן היא מתעלמת מ-`PYTHONPATH` וממודולים בתיקיית העבודה; מנהל החבילות של המערכת פותר את תלויות Python ו-`requests`. הן מכילות קוד Python בלתי תלוי בארכיטקטורה ודורשות הפצה המספקת Python 3.12 ומעלה.

### מקוד מקור

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
pip install .
```

### לפיתוח

```bash
git clone https://github.com/somethingwithproof/check_bitcoin_price.git
cd check_bitcoin_price
mise trust
mise install
mise run setup
```

## שימוש

### שימוש בסיסי

```bash
# Check Bitcoin price (valid quotes return OK when no thresholds are set)
check_bitcoin_price

# Output: OK - Bitcoin price is 43521.00 USD | bitcoin_price=43521.00;;;0; request_time=0.125s;;;0;
```

### עם ספים

```bash
# Alert if price drops below 30000 or rises above 50000 (warning)
# Alert if price drops below 25000 or rises above 60000 (critical)
check_bitcoin_price -w 30000:50000 -c 25000:60000
```

### ספים בודדים

```bash
# Only alert on price drops
check_bitcoin_price --warning-low 30000 --critical-low 25000

# Only alert on price spikes
check_bitcoin_price --warning-high 50000 --critical-high 60000
```

### מטבע שונה

```bash
# Check price in EUR
check_bitcoin_price --currency eur

# Check price in GBP
check_bitcoin_price --currency gbp
```

### זמן קצוב מותאם אישית

```bash
# Set a total 30-second budget for requests and retries
check_bitcoin_price --timeout 30
```

### עדכניות ותקציב ניסיונות חוזרים

```bash
# Require a quote no older than five minutes; allow two retries within ten seconds
check_bitcoin_price --max-age 300 --timeout 10 --retries 2
```

ציטוט הנושא חותמת זמן של הספק חייב להיות בן שעה אחת לכל היותר כברירת מחדל.
נקודות קצה המחזירות מחיר בלבד נשארות שמישות כאשר `--max-age` אינו מוגדר.
עם `--max-age`, חותמות זמן של הספק שהן חסרות, לא תקינות, עתידיות או מיושנות מחזירות
`UNKNOWN`; התוסף אינו מחליף את זמן הציטוט של הספק בזמן האחזור המקומי.
חותמת זמן הנמצאת בדיוק בגבול הגיל נותרת תקינה. חותמות זמן
עתידיות נדחות תמיד.

ברירת המחדל מאפשרת ניסיון חוזר אחד. רק שגיאות חיבור, זמני קצוב ותגובות HTTP
408/429/500/502/503/504 מנוסות שוב. זמן ההמתנה (backoff) מתחיל ב-0.5 שניות ומוכפל
עבור ניסיונות חוזרים עוקבים; שניות `Retry-After` ותאריכי HTTP מקבלים
עדיפות. כל הניסיונות, קריאות התגובה, פענוח JSON והמתנות לניסיונות חוזרים חולקים
את תקציב `--timeout`. המתנה לניסיון חוזר שאינה נכנסת בתקציב מחזירה `UNKNOWN` מיד
ומדווחת על הכשל שהוביל לכך, כגון `HTTP 429` או `ConnectionError`,
ולא על זמן קצוב. כשלי אימות, שגיאות HTTP קבועות אחרות, JSON לא תקין
ותגובות הגדולות מ-64 KiB של נתונים מפוענחים אינם מנוסים שוב. השתמשו ב-`--retries 0`
כדי להשבית ניסיונות חוזרים.

### מקורות ציטוט חלופיים (Fallback)

השתמשו באפשרויות `--fallback-url URL` הניתנות לחזרה עם נקודות קצה תואמות CoinGecko.
לדוגמה, הוסיפו `--fallback-url https://quotes.example.org/simple/price`.
כל מקור מקבל חלק שווה ממועד היעד הנותר לבקשה, כולל הניסיונות החוזרים
שלו. כשל חולף או עיכוב ניסיון חוזר הארוך מאותו חלק מעבירים למקור
הבא. כשלי אימות TLS, שגיאות HTTP קבועות וציטוטים לא תקינים
מחזירים UNKNOWN. כל תגובת ציטוט מוגבלת ל-64 KiB של נתונים מפוענחים.
כאשר מוגדרים מקורות חלופיים, הסטטוס מזהה את המקור המשיב כ-`primary`,
`fallback1` וכן הלאה, מבלי להדפיס את ה-URL שלו.

### תנועה בחלון זמן קצר

```bash
check_bitcoin_price --state-file /var/lib/nagios/bitcoin-usd.json \
  --move-window 900 --warning-move 3 --critical-move 6
```

הקצו למשתמש הניטור תיקיית מצב פרטית הניתנת לכתיבה במערכת קבצים מקומית של Linux או
macOS. שמרו על קובץ ה-`.lock` הסמוך במקומו בין בדיקות. השתמשו בקובץ
מצב נפרד לכל חלון זמן. למטבעות יש היסטוריות עצמאיות בתוכו.
חלון ברירת המחדל הוא 3600 שניות. כל ציטוט תקין דורש חותמת זמן של הספק
בתוך החלון ומגבלת הגיל, שהיא שעה אחת אלא אם `--max-age` מגדיר
אחרת. התוסף משווה את המחיר הנוכחי
למחיר החיובי המוקדם ביותר באותו חלון ומדווח על
השניות שחלפו בפועל. חותמות זמן חוזרות אינן יוצרות דגימות נוספות.
דגימה ראשונה, היסטוריה שפג תוקפה או JSON פגום מתחילים קו בסיס חדש; מדד
החלון הוא unknown עד שיש דגימה בת-השוואה. התראות אחרות עדיין
חלות. מצב שאינו ניתן לכתיבה, קובץ מצב או קובץ נעילה מסוג קישור סמלי, או ציטוט הישן
מהדגימה החדשה ביותר שנרשמה מחזירים UNKNOWN. המדד החתום `bitcoin_move_window`
משתמש בטווחי אזהרה וקריטיות סימטריים. שוויון בגבול אינו מפעיל התראה.

התוסף פותח את תיקיית המצב פעם אחת בכל בדיקה ופועל באופן יחסי אליה, כך
שרכיב נתיב שמוחלף במהלך הבדיקה אינו יכול להפנות מחדש את הנעילה, הקריאה
או הכתיבה. קישורים סמליים בחלק התיקייה של הנתיב נעקבים בעת
התחלת הבדיקה, מה ששומר על קישורי פלטפורמה כגון `/var` ב-macOS כשמישים.
לפיכך, תיקיית המצב ותיקיות האב שלה אינן רשאיות להיות ניתנות לכתיבה על ידי משתמשים
אחרים. קבצי המצב והנעילה נוצרים עם הרשאות 0600.

### תנועה יומית באחוזים

```bash
# Warn on a daily move greater than 5%; critical above 10%, in either direction
check_bitcoin_price --warning-change 5 --critical-change 10 --max-age 300
```

ספי השינוי מודדים את הערך המוחלט של השינוי היומי החתום ב-24 שעות של CoinGecko
במטבע שנבחר. שינוי הנמצא בדיוק על הסף אינו
מפעיל התראה. אם מסופקים שני הספים, סף האזהרה אסור שיעלה על הסף הקריטי.
נתוני שינוי נדרשים חסרים או לא תקינים מחזירים `UNKNOWN`. ניתן לשלב התראות מחיר ושינוי;
החומרה הגבוהה ביותר קובעת, כאשר למחיר ניתנת עדיפות
במקרה של חומרות זהות.

## אפשרויות שורת הפקודה

| אפשרות | תיאור |
|--------|-------|
| `-w`, `--warning` | טווח סף אזהרה (פורמט: LOW:HIGH) |
| `-c`, `--critical` | טווח סף קריטיות (פורמט: LOW:HIGH) |
| `--warning-low` | סף אזהרה למחיר נמוך |
| `--warning-high` | סף אזהרה למחיר גבוה |
| `--critical-low` | סף קריטיות למחיר נמוך |
| `--critical-high` | סף קריטיות למחיר גבוה |
| `--currency` | קוד מטבע בן 2-16 אותיות או ספרות (ברירת מחדל: usd) |
| `--timeout` | תקציב כולל לבקשת API ולניסיונות חוזרים בשניות, כולל ערכים עשרוניים (ברירת מחדל: 10) |
| `--retries` | ניסיונות נוספים לכשלים חולפים, 0–5 (ברירת מחדל: 1) |
| `--max-age` | גיל מרבי של ציטוט הספק בשניות וחיוב חותמת זמן; ציטוטים עם חותמת זמן מוגדרים כברירת מחדל ל-3600 |
| `--warning-change` | מגבלת אזהרה לתנועה מוחלטת באחוזים ב-24 שעות |
| `--critical-change` | מגבלת קריטיות לתנועה מוחלטת באחוזים ב-24 שעות |
| `--api-url` | כתובת URL ראשית של API |
| `--fallback-url` | נקודת קצה תואמת נוספת; יש לחזור לפי סדר העדיפויות |
| `--state-file` | קובץ JSON להיסטוריית תנועה |
| `--move-window` | חלון תנועה בשניות (ברירת מחדל: 3600) |
| `--warning-move`, `--critical-move` | ספי תנועה מוחלטים בחלון באחוזים |
| `-v`, `--verbose` | הפעלת פלט מפורט |
| `-V`, `--version` | הצגת גרסה |
| `-h`, `--help` | הצגת הודעת עזרה |

## הגדרת Nagios

### הגדרת פקודה

הגדירו את מאקרו המשאב של Nagios `$USER1$` לתיקיית התוספים (החבילות המקוריות משתמשות ב-`/usr/lib/nagios/plugins`). הוסיפו להגדרות הפקודות של Nagios:

```cfg
define command {
    command_name    check_bitcoin_price
    command_line    $USER1$/check_bitcoin_price -w $ARG1$ -c $ARG2$ --currency $ARG3$
}
```

### הגדרת שירות

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

### הגדרת Icinga2

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

## קודי יציאה

ארגומנטים לא תקינים, זמני קצוב לא חיוביים, טווחי סף לא תקינים ומחירי API פגומים
מחזירים `UNKNOWN` (קוד יציאה 3). הספים חייבים להיות מספרים סופיים
ואי-שליליים, כאשר כל גבול תחתון אינו גדול מהגבול העליון שלו. המטבע חייב
להכיל 2-16 אותיות או ספרות. הגדרה לא תקינה נדחית לפני יצירת קשר עם
ה-API. המחירים חייבים להיות סופיים ואי-שליליים, וניתנים כמספרי JSON או כמחרוזות
עשרוניות פשוטות כגון `"43521.5"`. תגובה ללא המטבע המבוקש
מציינת אותו בשמו, לדוגמה `Response has no EUR price`. תגובות לא תקינות אינן מפיקות
נתוני ביצועים. אבחון מפורט נשלח אל stderr
כך ש-stdout מכיל שורת סטטוס ניטור יחידה.

| קוד | סטטוס | תיאור |
|-----|--------|-------|
| 0 | OK | המחיר נמצא בטווח התקין |
| 1 | WARNING | המחיר חצה את סף האזהרה |
| 2 | CRITICAL | המחיר חצה את הסף הקריטי |
| 3 | UNKNOWN | אירעה שגיאה (כשל API, זמן קצוב וכו') |

## נתוני ביצועים

התוסף מפיק נתוני ביצועים בפורמט התקני של Nagios:

```text
bitcoin_price=43521.00;30000:50000;25000:60000;0; request_time=0.125s;;;0; price_age=20.000s;;;0; bitcoin_change_24h=-6.00%;-5:5;-10:10;;
```

נתוני ביצועי המחיר כוללים את טווחי האזהרה/קריטיות שהוגדרו ומינימום
של אפס. הספים מודפסים בסימון עשרוני מלא, לעולם לא מעוגלים
או בצורת חזקה, כך שערכים גדולים כגון `14500000:16250000` נשארים ניתנים לפענוח. זמן הבקשה כולל את כל הניסיונות ואת זמני ההמתנה (backoff). גיל הציטוט
נפלט רק כאשר הספק מספק חותמת זמן תקינה; שינוי יומי נפלט
כאשר הוא זמין. טווחי השינוי סימטריים סביב אפס. נתונים לא תקינים או מיושנים
מפיקים `UNKNOWN` ללא נתוני ביצועי מחיר. ניתן להשתמש במדדים אלה עם
כלי גרפים כגון PNP4Nagios, Grafana או InfluxDB.

## API

תוסף זה משתמש ב-[CoinGecko API](https://www.coingecko.com/en/api) כברירת מחדל, שהוא חינמי ואינו דורש מפתח API. חלות מגבלות קצב.

נקודות קצה מותאמות אישית חייבות להשתמש באותו מבנה תגובה: `bitcoin.<currency>` עבור
מחיר, `bitcoin.last_updated_at` עבור שניות חותמת זמן של UNIX, ו-`bitcoin.<currency>_24h_change`
עבור תנועה יומית חתומה באחוזים. רק המחיר
נדרש כאשר `--max-age` וספי השינוי אינם מוגדרים. חותמת זמן
שקיימת עדיין נבדקת: אסור שהיא תהיה בעתיד או בת יותר משעה
אחת. התגובה המפוענחת חייבת להיכנס ב-64 KiB.

המטבעות הנתמכים כוללים: usd, eur, gbp, jpy, aud, cad, chf, cny ורבים נוספים.

## אבטחה

האמצעים שלהלן מיושמים בקוד הנוכחי. הם מגבילים את מה שנקודת קצה סוררת או משתמש מקומי יכולים לעשות למארח הניטור;
הם אינם הופכים את הציטוט עצמו למהימן.

- תעודות HTTPS מאומתות באמצעות ברירות המחדל של `requests`, ואף אפשרות
  אינה משביתה אימות. ל-`--api-url` מותאם אישית המשתמש ב-`http://` רגיל אין
  הגנה כזו.
- DNS, חיבור, קריאות, ניסיונות חוזרים והמתנת backoff חולקים את מועד היעד של `--timeout`.
  עמית ששולח נתונים לאט אינו יכול להאריך אותו.
- כל תגובה מוגבלת ל-64 KiB לאחר פריסה, וגופי הפניות מחדש (redirect)
  נזרקים מבלי להיקרא.
- כשלי בקשה מדפיסים רק סטטוס HTTP או מחלקת שגיאה, מכיוון ש-`--api-url` מותאם
  אישית עשוי להכיל אישורי גישה.
- הפקודה המותקנת על ידי `.deb` ו-`.rpm` מריצה Python במצב מבודד.
  היא מתעלמת מ-`PYTHONPATH`, מתיקיית ה-site של המשתמש וממודולים בתיקיית
  העבודה. התקנת `pip` משתמשת בסקריפט המסוף התקני ופועלת לפי
  הסביבה שבה היא מותקנת.
- מצב התנועה נקרא ונכתב מבלי לעקוב אחר קישור סמלי בשם קובץ
  המצב או קובץ הנעילה, באופן יחסי לתיקייה הנפתחת פעם אחת בכל בדיקה.
- נכסי המהדורה נושאים אישורי מקור בנייה בנוסף ל-`SHA256SUMS`;
  ראו [מתוך GitHub Releases](#from-github-releases).

## שדרוג מגרסה 1.0.0

שינויים אלה נכללים בגרסה 2.0.0.

- ציטוט עם חותמת זמן של הספק הישנה משעה אחת מחזיר `UNKNOWN` אלא אם
  סופק `--max-age` גדול יותר. נקודות קצה שאינן מחזירות חותמת זמן אינן מושפעות.
- `--currency` מקבלת רק 2-16 אותיות או ספרות.
- מחרוזות מספריות עם מפרידי ספרות או רווחים מסביב נדחות.
- המתנה לניסיון חוזר שאינה נכנסת בתקציב מדווחת על הכשל הבסיסי
  במקום `API request timed out`.
- החבילות המקוריות אינן מכבדות עוד את `PYTHONPATH`.
- ספים של מיליון או יותר מופיעים בנתוני הביצועים כמספרים
  עשרוניים פשוטים במקום בסימון חזקה.

## לוקליזציה

עזרת CLI, שגיאות אימות ותיאורי סטטוס של התוסף תומכים ב-45 שפות ומיקומים (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) באמצעות קטלוגים מצורפים הנטענים מהספרייה התקנית. פתרון השפה בודק את `--lang`, ולאחר מכן את `LC_ALL`, `LC_MESSAGES` ו-`LANG`, וחוזר ל-`en` כברירת מחדל. קידומות הסטטוס של Nagios (`OK`, `WARNING`, `CRITICAL`, `UNKNOWN`) ונתוני הביצועים נותרים ללא שינוי בכל השפות.

```bash
check_bitcoin_price --lang de
LANG=ja_JP.UTF-8 check_bitcoin_price --help
```

## פיתוח

התקינו את [mise](https://mise.jdx.dev/getting-started.html), ולאחר מכן הריצו את הגדרת הפיתוח שלעיל. `mise.toml` מקבע את Python ואת uv. כלי הפיתוח מוצהרים ב-`pyproject.toml` ונפתרים ב-`uv.lock` השמור במאגר.

```bash
mise run check   # lockfile, formatting, lint, and types
mise run test    # unit tests, installed CLI tests, and >=98% branch-aware coverage
mise run audit   # Bandit and locked runtime dependency audit
mise run build   # wheel, source distribution, and strict metadata validation
mise run package # also build .deb, .rpm, and SHA256SUMS
mise run format
```

התקינו את ה-commit hooks לאחר ההגדרה:

```bash
mise exec -- uv run --frozen --no-sync --no-build pre-commit install
mise exec -- uv run --frozen --no-sync --no-build pre-commit run --all-files
```

השתמשו ב-`mise exec -- uv add --dev <tool>` או ב-`mise exec -- uv add <dependency>` כדי לעדכן תלויות ובצעו commit הן ל-`pyproject.toml` והן ל-`uv.lock`.

CI בודק את Python 3.12 ו-3.13 ב-Linux ואת Python 3.13 ב-macOS. כל PR מריץ גם אימות חבילות, ביקורת תלויות ו-CodeQL, ומתקין את ה-`.deb` ב-Ubuntu ואת ה-`.rpm` ב-Fedora. תוצרי ההפצה הבנויים זמינים כנכס `distributions` בהרצות CI.

גרסת החבילה וה-CLI מגיעה מתוך `check_bitcoin_price/__init__.py`. ראו את [תהליך השחרור](../../../CONTRIBUTING.md#releases) לעדכוני גרסה ופרסום אוטומטי של נכסי מהדורות GitHub.

## תרומה לפרויקט

ראו [CONTRIBUTING.md](../../../CONTRIBUTING.md) עבור תהליך העבודה בפיתוח ודרישות signed-off commit.

## רישיון

פרויקט זה מורשה תחת רישיון MIT - ראו את הקובץ [LICENSE](../../../LICENSE) לפרטים.

## מחבר

Thomas Vincent

## תודות

- [CoinGecko](https://www.coingecko.com/) על אספקת API חינמי למטבעות קריפטוגרפיים
- [Nagios Plugins Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)
