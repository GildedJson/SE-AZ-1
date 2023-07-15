<div dir="rtl">

# آزمایش اول آز مهندسی نرم‌افزار

## سیدمحمدصادق طبائیان - 98105868

## عبدالصمد حقیری - 98105727



مراحل ساخت مخزن و اولین کامیت‌ها در شکل زیر قابل مشاهده است.

<img src="./init.JPG" width="350px">

ایجاد قانون جلوگیری از کامیت مستقیم به شاخه‌ی اصلی به شکل زیر است. (البته این قانون تا زمان ایجاد شاخه‌ها تنظیم نشد.)

<img src="./branchProtection.JPG" width="350px">


پرسش ۱: دستور git init یک مخزن (repo) جدید ایجاد می‌کند. این دستور، یک پوشه‌ی .git در مسیر فعلی ایجاد می‌کند که تمام متادیتای مورد نیاز گیت برای پروژه را در خود نگه می‌دارد. این متادیتا شامل پوشه‌هایی برای فایل‌های مرجع، قالب و آبجکت‌های گیت است. به علاوه یک فایل head که به کامیت checkout اشاره می‌کند. 

پرسش ۲: اتمیک بودن یعنی تشکیل یک جزء غیر قابل تقلیل در یک سیستم بزرگ‌تر. مثلا کامیت اتمیک یعنی انقدر کامیت را کوچک کنیم تا به کوچک‌ترین کامیت معنی‌دار برسد. نه اینکه یک کامیت بزنیم که در آن چند تغییر با هم اتفاق افتاده است. PR اتمیک هم یعنی PR ای که کوچک‌ترین و غیرقابل تقلیل‌ترین PR معنادار ممکن باشد. این کار تعداد PR ها را بیشتر می‌کند اما هر PR نشان‌دهنده‌ی یک کار مشخص و کوچک است.
اتمیک بودن باعث می‌شود برای بازبینی و پیداکردن باگ، کار راحت‌تری داشته باشیم.


پرسش ۳: زمانی که می‌خواهیم کامیت‌ها و فایل‌ها را از یک مخزن remote در مخزن محلی خودمان دانلود کنیم، از دستورهای git fetch و git pull استفاده می‌کنم.
با git fetch، محتوای remote دانلود می‌شود اما وضعیت کاری محلی آپدیت نمی‌شود. اما git pull، درواقع ترکیب دو دستور git fetch و git merge است. ابتدا یک git fetch را به شاخه محلی که head به آن اشاره می‌کند اجرا می‌کند. پس از دانلود محتوا، git merge اجرا می‌شود و یک کامیت جدید برای merge ایجاد می‌شود و head آپدیت می‌شود و به کامیت جدید اشاره می‌کند.
Git merge و git rebase هر دو برای یکپارچه‌سازی و ادغام تغییرات از یک شاخه به شاخه دیگر طراحی شده‌اند اما به روش‌های مختلفی این کار را انجام می‌دهند.
در merge، محتوای شاخه مبدا را با شاخه مقصد یکپارچه می‌کنیم. در این فرایند، فقط شاخه مقصد تغییر می‌کند و سابقه شاخه مبدا دست نخورده باقی می‌ماند.
در rebase، همه تغییرات 	شاخه مبدا را از شروع آخرین کامیت شاخه مقصد اضافه می‌کند. این روش بر خلاف merge، باعث از بین رفتن سابقه تغییرات می‌شود. زیرا کل کار را از یک شاخه به شاخه دیگر منتقل می‌کند.
پس merge، تاریخچه را حفظ می‌کند اما rebase آن را rewrite می‌کند. از طرفی از طریق rebase، می‌توان کامیت‌های نامطلوب را حذف کرد، پیام یک کامیت را ویرایش کرد و خلاصه تاریخچه کامیت را تغییر داد.

پرسش ۴: به صورت کلی git reset دستوری برای لغو تغییرات است. سه فرم اصلی فراخوانی دارد. --soft، --mixed و --hard. در اولی، فقط پوینترها آپدیت می‌شوند و مسیر جاری (working directory) و staging index دست نخورده باقی می‌مانند. یعنی فایل‌های ما و همچنین چیزهایی که add شده بودند و staged بودند تغییری نمی‌کنند. فقط پوینترهای head و شاخه (branch) جاری را به کامیت گفته شده (که در ورودی می‌آید) بازنشانی می‌کند (اگر کامیتی در ورودی نیاید، به صورت پیش‌فرض head را درنظر می‌گیرد). در دومی، علاوه‌بر اینکه پوینترها آپدیت می‌شوند، وضعیت staging index هم بازنشانی می‌شود یعنی فایل/فایل‌های مورد نظر که staged بودند، به حالت unstaged تبدیل می‌شوند. در سومی، علاوه‌بر آپدیت پوینترها و بازنشانی staging index، مسیر جاری (working directory) هم بازنشانی می‌شود و تغییراتش نسبت به کامیت منظور لغو می‌شود. (در این حالت این داده‌های از دست رفته را نمی‌توان بازگرداند)
دستور git restore می‌تواند با --staged فایل‌های add شده (staged) را به وضعیت گفته شده بازنشانی کند و با --worktree تغییرات مسیر جاری را بازنشانی کند (هردو با هم نیز می‌تواند استفاده شود). درواقع به جز آپدیت پوینترها، کارهای reset را می‌تواند انجام دهد.
دستور git revert تغییرات یک کامیت خاص را درنظر می‌گیرد، تغییرات را برمی‌گرداند (معکوس می‌کند) و یک کامیت جدید می‌سازد و پوینتر را به این کامیت می‌برد. این کار کامیتی را پاک نمی‌کند و جلوی از دست رفتن تاریخچه‌ی کامیت‌ها را می‌گیرد.
ضمنا این دستور می‌تواند یک کامیت مشخص در هرجای پروژه را مورد هدف قرار دهد درحالی که reset فقط می‌تواند به کامیت‌های قبل کامیت فعلی برگردد.

پرسش ۵: محیط stage، فایل‌های آماده برای کامیت شدن در مخزن ما هستند. با دستور git add می‌توانیم یک یا چند فایل را به محیط Stage اضافه کنیم.
دستور git stash تغییرهای کامیت نشده (هم آن‌هایی که stage شده‌اند و هم آن‌ّهایی که stage نشده‌اند) را به‌طور موقت برای استفاده‌ی بعدی ذخیره‌شان می‌کند و سپس به نسخه کاری برمان می‌گرداند.
Stash در مخزن محلی ماست و زمان push کردن به سرور منتقل نمی‌شود.
می‌توانیم با دستور git stash pop تغییرهای stash شده خود را دوباره اعمال کنیم. Pop کردن stash، تغییرها را از stash برمی‌دارد و دوباره در نسخه کاری‌مان اعمال می‌کند.

پرسش ۶: مفهوم snapshot به معنای ذخیره‌سازی وضعیت فعلی یک سیستم است. یعنی یک تصویر یا نسخه از حالت فعلی سیستم. مثلا گیت در هر کامیت، یک snapshot از فایل‌ها دارد. یا مثلا دستور git commit، یک snapshot از دایرکتوری Staging را به تاریخچه‌ی کامیت‌های مخزن اضافه می‌کند.
</div>

