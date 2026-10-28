# -*- coding: utf-8 -*-
"""
Cryptographie pour les débutants sur Labex.io """

""" 
Lab 1 : Installation des Outils de Cryptographie et Configuration de l'Environnement

Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: Emma SAGET
New password:
Retype new password:
passwd: password updated successfully
usermod: no changes
Installation successful!

Provisioning the new WSL instance Ubuntu
This might take a while...
Help improve Ubuntu!

Help us improve Ubuntu features and compatibility by sharing system reports with Canonical.
Reports are sent anonymously and do not contain any personal data.
For legal details, please visit: https://ubuntu.com/legal/systems-information-notice

We will save your answer to Windows and will only ask you once.

Would you like to opt-in to platform metrics collection (Y/n)? To see an example of the data collected, enter 'e'.
[Y/n/e]: n
Welcome to Ubuntu 26.04.1 LTS (GNU/Linux 6.18.40.1-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://docs.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Fri Oct  2 21:01:23 CEST 2026

  System load:  0.1                 Processes:             36
  Usage of /:   0.1% of 1006.85GB   Users logged in:       0
  Memory usage: 6%                  IPv4 address for eth0: 172.27.225.205
  Swap usage:   0%


This message is shown once a day. To disable it please create the
/home/Emma/.hushlogin file.
Emma@Bob:~$ /home/Emma/.hushlogin file.
-bash: /home/Emma/.hushlogin: No such file or directory
Emma@Bob:~$ /home/Emma/.hushlogin file.
-bash: /home/Emma/.hushlogin: Permission denied
Emma@Bob:~$ open /home/Emma/.hushlogin file.
Command 'open' not found, but can be installed with:
sudo apt install mailcap    # version 3.75ubuntu1, or
sudo apt install xdg-utils  # version 1.2.1-2ubuntu2
Emma@Bob:~$ sudo apt update
[sudo: authenticate] Password:
Get:1 http://security.ubuntu.com/ubuntu resolute-security InRelease [137 kB]
Hit:2 http://archive.ubuntu.com/ubuntu resolute InRelease
Get:3 http://archive.ubuntu.com/ubuntu resolute-updates InRelease [137 kB]
Get:4 http://security.ubuntu.com/ubuntu resolute-security/main amd64 Packages [550 kB]
Get:5 http://security.ubuntu.com/ubuntu resolute-security/main Translation-en [129 kB]
Get:6 http://security.ubuntu.com/ubuntu resolute-security/main amd64 Components [46.7 kB]
Get:7 http://security.ubuntu.com/ubuntu resolute-security/universe amd64 Packages [191 kB]
Get:8 http://security.ubuntu.com/ubuntu resolute-security/universe Translation-en [60.4 kB]
Get:9 http://security.ubuntu.com/ubuntu resolute-security/universe amd64 Components [55.6 kB]
Get:10 http://security.ubuntu.com/ubuntu resolute-security/universe amd64 c-n-f Metadata [3552 B]
Get:11 http://security.ubuntu.com/ubuntu resolute-security/restricted amd64 Packages [445 kB]
Get:12 http://security.ubuntu.com/ubuntu resolute-security/restricted Translation-en [89.7 kB]
Get:13 http://security.ubuntu.com/ubuntu resolute-security/multiverse amd64 Packages [10.8 kB]
Get:14 http://security.ubuntu.com/ubuntu resolute-security/multiverse Translation-en [2844 B]
Get:15 http://security.ubuntu.com/ubuntu resolute-security/multiverse amd64 Components [212 B]
Get:16 http://security.ubuntu.com/ubuntu resolute-security/multiverse amd64 c-n-f Metadata [120 B]
Get:17 http://archive.ubuntu.com/ubuntu resolute-backports InRelease [137 kB]
Get:18 http://archive.ubuntu.com/ubuntu resolute/universe amd64 Packages [16.0 MB]
Get:19 http://archive.ubuntu.com/ubuntu resolute/universe Translation-en [6329 kB]
Get:20 http://archive.ubuntu.com/ubuntu resolute/universe amd64 Components [4556 kB]
Get:21 http://archive.ubuntu.com/ubuntu resolute/universe amd64 c-n-f Metadata [313 kB]
Get:22 http://archive.ubuntu.com/ubuntu resolute/multiverse amd64 Packages [290 kB]
Get:23 http://archive.ubuntu.com/ubuntu resolute/multiverse Translation-en [127 kB]
Get:24 http://archive.ubuntu.com/ubuntu resolute/multiverse amd64 Components [50.0 kB]
Get:25 http://archive.ubuntu.com/ubuntu resolute/multiverse amd64 c-n-f Metadata [8276 B]
Get:26 http://archive.ubuntu.com/ubuntu resolute-updates/main amd64 Packages [717 kB]
89% [20 Components-amd64 store 0 B] [26 Packages 2657 B/717 kB 0%]          Get:27 http://archive.ubuntu.com/ubuntu resolute-updates/main Translation-en [167 kB]
Get:28 http://archive.ubuntu.com/ubuntu resolute-updates/main amd64 Components [97.7 kB]
Get:29 http://archive.ubuntu.com/ubuntu resolute-updates/universe amd64 Packages [315 kB]
Get:30 http://archive.ubuntu.com/ubuntu resolute-updates/universe Translation-en [101 kB]
Get:31 http://archive.ubuntu.com/ubuntu resolute-updates/universe amd64 Components [201 kB]
Get:32 http://archive.ubuntu.com/ubuntu resolute-updates/universe amd64 c-n-f Metadata [4704 B]
Get:33 http://archive.ubuntu.com/ubuntu resolute-updates/restricted amd64 Packages [486 kB]
Get:34 http://archive.ubuntu.com/ubuntu resolute-updates/restricted Translation-en [97.7 kB]
Get:35 http://archive.ubuntu.com/ubuntu resolute-updates/multiverse amd64 Packages [11.9 kB]
Get:36 http://archive.ubuntu.com/ubuntu resolute-updates/multiverse Translation-en [3276 B]
Get:37 http://archive.ubuntu.com/ubuntu resolute-updates/multiverse amd64 Components [216 B]
Get:38 http://archive.ubuntu.com/ubuntu resolute-updates/multiverse amd64 c-n-f Metadata [256 B]
Get:39 http://archive.ubuntu.com/ubuntu resolute-backports/main amd64 Components [212 B]
Get:40 http://archive.ubuntu.com/ubuntu resolute-backports/main amd64 c-n-f Metadata [112 B]
Get:41 http://archive.ubuntu.com/ubuntu resolute-backports/universe amd64 Packages [3132 B]
Get:42 http://archive.ubuntu.com/ubuntu resolute-backports/universe Translation-en [7988 B]
Get:43 http://archive.ubuntu.com/ubuntu resolute-backports/universe amd64 Components [1056 B]
Get:44 http://archive.ubuntu.com/ubuntu resolute-backports/universe amd64 c-n-f Metadata [116 B]
Get:45 http://archive.ubuntu.com/ubuntu resolute-backports/restricted amd64 Components [216 B]
Get:46 http://archive.ubuntu.com/ubuntu resolute-backports/restricted amd64 c-n-f Metadata [120 B]
Get:47 http://archive.ubuntu.com/ubuntu resolute-backports/multiverse amd64 Components [216 B]
Get:48 http://archive.ubuntu.com/ubuntu resolute-backports/multiverse amd64 c-n-f Metadata [120 B]
Fetched 31.8 MB in 10s (3221 kB/s)
98 packages can be upgraded. Run 'apt list --upgradable' to see them.
Emma@Bob:~$ sudo apt install -y openssl
Upgrading:
  libssl3t64  openssl  openssl-provider-legacy

Summary:
  Upgrading: 3, Installing: 0, Removing: 0, Not Upgrading: 95
  Download size: 3651 kB
  Space needed: 10.2 kB / 1024 GB available

Get:1 http://archive.ubuntu.com/ubuntu resolute-updates/main amd64 openssl-provider-legacy amd64 3.5.5-1ubuntu3.7 [39.7 kB]
Get:2 http://archive.ubuntu.com/ubuntu resolute-updates/main amd64 libssl3t64 amd64 3.5.5-1ubuntu3.7 [2368 kB]
Get:3 http://archive.ubuntu.com/ubuntu resolute-updates/main amd64 openssl amd64 3.5.5-1ubuntu3.7 [1243 kB]
Fetched 3651 kB in 2s (1651 kB/s)
(Reading database ... 35908 files and directories currently installed.)
Preparing to unpack .../openssl-provider-legacy_3.5.5-1ubuntu3.7_amd64.deb ...
Unpacking openssl-provider-legacy (3.5.5-1ubuntu3.7) over (3.5.5-1ubuntu3.4) ...
Setting up openssl-provider-legacy (3.5.5-1ubuntu3.7) ...
(Reading database ... 35908 files and directories currently installed.)
Preparing to unpack .../libssl3t64_3.5.5-1ubuntu3.7_amd64.deb ...
Unpacking libssl3t64:amd64 (3.5.5-1ubuntu3.7) over (3.5.5-1ubuntu3.4) ...
Setting up libssl3t64:amd64 (3.5.5-1ubuntu3.7) ...
(Reading database ... 35908 files and directories currently installed.)
Preparing to unpack .../openssl_3.5.5-1ubuntu3.7_amd64.deb ...
Unpacking openssl (3.5.5-1ubuntu3.7) over (3.5.5-1ubuntu3.4) ...
Setting up openssl (3.5.5-1ubuntu3.7) ...
Processing triggers for man-db (2.13.1-1build1) ...
Processing triggers for libc-bin (2.43-2ubuntu2.3) ...
Emma@Bob:~$ sudo apt install -y python3 python3-pip
python3 is already the newest version (3.14.3-0ubuntu2).
python3 set to manually installed.
Installing:
  python3-pip

Installing dependencies:
  python3-wheel

Recommended packages:
  build-essential  python3-dev

Summary:
  Upgrading: 0, Installing: 2, Removing: 0, Not Upgrading: 95
  Download size: 1444 kB
  Space needed: 10.5 MB / 1024 GB available

Get:1 http://archive.ubuntu.com/ubuntu resolute/universe amd64 python3-wheel all 0.46.3-2 [27.9 kB]
Get:2 http://archive.ubuntu.com/ubuntu resolute/universe amd64 python3-pip all 25.1.1+dfsg-1ubuntu2 [1416 kB]
Fetched 1444 kB in 1s (1697 kB/s)
Selecting previously unselected package python3-wheel.
(Reading database ... 35908 files and directories currently installed.)
Preparing to unpack .../python3-wheel_0.46.3-2_all.deb ...
Unpacking python3-wheel (0.46.3-2) ...
Selecting previously unselected package python3-pip.
Preparing to unpack .../python3-pip_25.1.1+dfsg-1ubuntu2_all.deb ...
Unpacking python3-pip (25.1.1+dfsg-1ubuntu2) ...
Setting up python3-wheel (0.46.3-2) ...
Setting up python3-pip (25.1.1+dfsg-1ubuntu2) ...
Processing triggers for man-db (2.13.1-1build1) ...
Emma@Bob:~$ pip install -U cryptography
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.14/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
Emma@Bob:~$  apt install
    python3-xyz
Error: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
Error: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
python3-xyz: command not found
Emma@Bob:~$ apt install python3-xyz
Error: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
Error: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
Emma@Bob:~$ pip install python3-xyz
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.14/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
Emma@Bob:~$ apt install python3-cryptography
Error: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
Error: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
Emma@Bob:~$ apt install phyton3 -U cryptography
Error: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)
Error: Unable to lock directory /var/lib/apt/lists/
Warning: Problem unlinking the file /var/cache/apt/pkgcache.bin - RemoveCaches (13: Permission denied)
Warning: Problem unlinking the file /var/cache/apt/srcpkgcache.bin - RemoveCaches (13: Permission denied)
Emma@Bob:~$ apt install python3 -U cryptography
Error: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)
Error: Unable to lock directory /var/lib/apt/lists/
Warning: Problem unlinking the file /var/cache/apt/pkgcache.bin - RemoveCaches (13: Permission denied)
Warning: Problem unlinking the file /var/cache/apt/srcpkgcache.bin - RemoveCaches (13: Permission denied)
Emma@Bob:~$ pip install python3-full
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.14/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
Emma@Bob:~$ apt install python3-full
Error: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
Error: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
Emma@Bob:~$ sudo apt install python3-pip
python3-pip is already the newest version (25.1.1+dfsg-1ubuntu2).
Summary:
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 95
Emma@Bob:~$ python3 -m pip install -U cryptography
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.14/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
Emma@Bob:~$ sudo python3 -m pip install -U cryptography
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.14/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
Emma@Bob:~$ sudo apt update
sudo apt install python3-cryptography
Hit:1 http://security.ubuntu.com/ubuntu resolute-security InRelease
Hit:2 http://archive.ubuntu.com/ubuntu resolute InRelease
Hit:3 http://archive.ubuntu.com/ubuntu resolute-updates InRelease
Hit:4 http://archive.ubuntu.com/ubuntu resolute-backports InRelease
95 packages can be upgraded. Run 'apt list --upgradable' to see them.
Upgrading:
  python3-cryptography

Summary:
  Upgrading: 1, Installing: 0, Removing: 0, Not Upgrading: 94
  Download size: 1160 kB
  Space needed: 24.6 kB / 1024 GB available

Get:1 http://archive.ubuntu.com/ubuntu resolute-updates/main amd64 python3-cryptography amd64 46.0.5-1ubuntu2.2 [1160 kB]
Fetched 1160 kB in 1s (920 kB/s)
(Reading database ... 36693 files and directories currently installed.)
Preparing to unpack .../python3-cryptography_46.0.5-1ubuntu2.2_amd64.deb ...
Unpacking python3-cryptography (46.0.5-1ubuntu2.2) over (46.0.5-1ubuntu2) ...
Setting up python3-cryptography (46.0.5-1ubuntu2.2) ...
Emma@Bob:~$ openssl version
OpenSSL 3.5.5 27 Jan 2026 (Library: OpenSSL 3.5.5 27 Jan 2026)
Emma@Bob:~$ python -c "import cryptography"
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
Emma@Bob:~$ python3 -c "import cryptography"
Emma@Bob:~$
"""

"""
Lab 2 : Bases du Chiffrement Symétrique en Cryptographie

Emma@Bob:~$ ls -l
total 12
drwxr-xr-x 2 Emma Emma 4096 Oct  2 21:43 Cryptographie
-rw------- 1 Emma Emma    2 Oct  2 21:53 a.save
-rw-r--r-- 1 Emma Emma    0 Oct  2 21:09 file.
-rw-r--r-- 1 Emma Emma   27 Oct  2 21:45 original.txt
Emma@Bob:~$ cat original.txt
This is a secret message.

Emma@Bob:~$ openssl rand -hex 32 > aes.key
Emma@Bob:~$ cat aes.key
7401ceade84ff52b4885a2455d941dd23c15eab6efe9b808e02a9f454f7c7613
Emma@Bob:~$ openssl enc -aes-256-cbc -pbkdf2 -salt -in original.txt -out encrypted.dat -pass file:./aes.key
"""
#Nous utiliserons le chiffrement AES-256-CBC.
#- AES-256: Fait référence à l'Advanced Encryption Standard avec une clé de 256 bits.
#- CBC: Signifie Cipher Block Chaining (Chaînage de Blocs de Chiffrement), un mode d'opération qui ajoute de l'aléatoire et garantit que des blocs de texte clair identiques ne produisent pas des blocs de texte chiffré identiques.
#Examinons les options de la commande :
#openssl enc: La commande pour les chiffrements.
#-aes-256-cbc: Spécifie l'algorithme de chiffrement à utiliser.
#-pbkdf2: Utilise une fonction de dérivation de clé basée sur un mot de passe (PBKDF2), moderne et standardisée, pour éviter les avertissements de dépréciation.
#-salt: Ajoute un sel (salt) aléatoire à la clé avant le chiffrement. C'est une pratique de sécurité cruciale qui protège contre certains types d'attaques.
#-in original.txt: Spécifie le fichier d'entrée à chiffrer.
#-out encrypted.dat: Spécifie le nom du fichier de sortie qui stockera les données chiffrées.
#-pass file:./aes.key: Indique à OpenSSL de lire le mot de passe (dans notre cas, la clé symétrique) depuis le fichier aes.key.
"""
Emma@Bob:~$ cat encrypted.dat
Salted__D5���gp֯��;fc�N�
␦Ow�ΒD��P�Emopenssl enc -d -aes-256-cbc -pbkdf2 -in encrypted.dat -out decrypted.txt -pass file:./aes.key:./aes.key
Emma@Bob:~$ openssl enc -d -aes-256-cbc -pbkdf2 -in encrypted.dat -out decrypted.txt -pass file:./aes.key:./aes.key
Can't open file ./aes.key:./aes.key
Error getting password
4027C96EB87C0000:error:80000002:system library:BIO_new_file:No such file or directory:../crypto/bio/bss_file.c:67:calling fopen(./aes.key:./aes.key, r)
4027C96EB87C0000:error:10000080:BIO routines:BIO_new_file:no such file:../crypto/bio/bss_file.c:75:
Emma@Bob:~$ openssl enc -d -aes-256-cbc -pbkdf2 -in encrypted.dat -out decrypted.txt -pass file:./aes.key
Emma@Bob:~$ cat decrypted.txt
This is a secret message.

Emma@Bob:~$ diff original.txt decrypted.txt
Emma@Bob:~$ ls -l
total 24
drwxr-xr-x 2 Emma Emma 4096 Oct  2 21:43 Cryptographie
-rw------- 1 Emma Emma    2 Oct  2 21:53 a.save
-rw-r--r-- 1 Emma Emma   65 Oct  2 21:54 aes.key
-rw-r--r-- 1 Emma Emma   27 Oct  2 22:10 decrypted.txt
-rw-r--r-- 1 Emma Emma   48 Oct  2 22:02 encrypted.dat
-rw-r--r-- 1 Emma Emma    0 Oct  2 21:09 file.
-rw-r--r-- 1 Emma Emma   27 Oct  2 21:45 original.txt
"""

"""
Lab 3 : Hachage avec SHA-256 en Cryptographie

Emma@Bob:~$ echo -n "hello" | openssl dgst -sha256
SHA2-256(stdin)= 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
Emma@Bob:~$ echo -n "hello" | openssl dgst -sha256
SHA2-256(stdin)= 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
Emma@Bob:~$ echo -n "Hello" | openssl dgst -sha256
SHA2-256(stdin)= 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
Emma@Bob:~$ cat original.txt
This is a secret message.

Emma@Bob:~$ openssl dgst -sha256 original.txt
SHA2-256(original.txt)= a90945bb523f436b9761bdcec203f09058bf2dec782afba2f433bd10889bf009
Emma@Bob:~$ echo -n "labex" | openssl dgst -sha256
SHA2-256(stdin)= 679e75b679886c5eaf8aaab88ddfc0181e6dae14cff346db8ba398bd7b2e31fe
Emma@Bob:~$ echo -n "crypto" | openssl dgst -sha256
SHA2-256(stdin)= da2f073e06f78938166f247273729dfe465bf7e46105c13ce7cc651047bf0ca4
Emma@Bob:~$ openssl dgst -sha256 original.txt
SHA2-256(original.txt)= a90945bb523f436b9761bdcec203f09058bf2dec782afba2f433bd10889bf009
Emma@Bob:~$ echo "." >> original.txt
Emma@Bob:~$ cat original.txt
This is a secret message.

.
Emma@Bob:~$ openssl dgst -sha256 original.txt
SHA2-256(original.txt)= 2cfb8dedbc9a040ba502ab45e3736475bc4ce7b7ae3dc1c89d35b2d8d6f42a7a
Emma@Bob:~$ touch hash_password.py
Emma@Bob:~$ nano hash_password.py
Emma@Bob:~$ python3 hash_password.py
The password is: mysecretpassword
The SHA-256 hash is: 94aefb8be78b2b7c344d11d1ba8a79ef087eceb19150881f69460b8772753263 
    """
""" 
Lab 4 : Chiffrement asymétrique avec RSA en Cryptographie  

Emma@Bob:~$ openssl genrsa -out private.pem 2048
Emma@Bob:~$ ls
Cryptographie  aes.key        encrypted.dat  hash_password.py  private.pem
a.save         decrypted.txt  file.          original.txt
Emma@Bob:~$ openssl rsa -in private.pem -pubout -out public.pem
writing RSA key
Emma@Bob:~$ ls
Cryptographie  aes.key        encrypted.dat  hash_password.py  private.pem
a.save         decrypted.txt  file.          original.txt      public.pem
Emma@Bob:~$ cat public.pem
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlufoyRmpXXOGChWbFkEQ
KNsLipaPp/9CFbw5auIo7TJMgUtjyRsLp5B2UP14lsUUF8lyWSwJvV3ujy4lb5hk
i8/H6sTGgTEiXKsv/iwC7V2hO74IrdBiTYC6WIDXyescHyngw4Tsva1OXPDIff4D
3UeChXNWDCSulfSShD53YBVScGUoQaZzWVTraO3oUWz3nhkErk29ziWpmoP1QiY7
2mKguwf2rUuiiFoCl9rhyTtvKGboJBNiQaJj25ul19jNqGKaZKgspB5GMTgVogv4
J2NlAZsPKw7mg6rzHIpW/cQgbfJUso6HbxuPDYiiLPYizeMa+adyEjsNB9CWpYzr
HQIDAQAB
-----END PUBLIC KEY-----
Emma@Bob:~$ echo "This is a secret message." > message.txt
Emma@Bob:~$ openssl pkeyutl -encrypt -pubin -inkey public.pem -in message.txt -out encrypted.bin
Emma@Bob:~$ cat encrypted.bin
�Nyk��S��ܸ�ba
         �8<t�6Ӿ����v`("���VH�nJK���G��P��6��[kgp��\��K�֊����B؋4 ��k��ȵ3>�!����4�ln��K��+Il�T�����X�YK��IQ$��?lK����"�t]~m��������e
               K ��ʡJ�MK�+��U�s Y\�SS��5U,��\�E␦����N���\yS� }�o�6�x��A0
"""   
# Examinons cette commande :

#openssl pkeyutl: Un utilitaire pour effectuer des opérations de clé publique telles que le chiffrement et le déchiffrement.
#-encrypt: Spécifie que nous souhaitons effectuer une opération de chiffrement.
#-pubin: Indique que la clé d'entrée (-inkey) est une clé publique.
#-inkey public.pem: Spécifie la clé publique à utiliser pour le chiffrement.
#-in message.txt: Le fichier d'entrée contenant le message en clair (plaintext).
#-out encrypted.bin: Le fichier de sortie où les données chiffrées (texte chiffré ou ciphertext) seront stockées.
#Après avoir exécuté la commande, un nouveau fichier encrypted.bin sera créé. Si vous essayez de visualiser son contenu, vous verrez des données binaires illisibles, qui sont la forme chiffrée de votre message.

""" 
Emma@Bob:~$ openssl pkeyutl -decrypt -inkey private.pem -in encrypted.bin -out decrypted.txt
"""

#Passons en revue les options de la commande :
#openssl pkeyutl: Le même utilitaire qu'auparavant.
#-decrypt: Cette fois, nous spécifions l'opération de déchiffrement.
#-inkey private.pem: Spécifie la clé privée à utiliser pour le déchiffrement.
#-in encrypted.bin: Le fichier d'entrée contenant le texte chiffré (ciphertext).
#-out decrypted.txt: Le fichier de sortie où le texte brut récupéré sera sauvegardé.
#Cette commande créera un nouveau fichier nommé decrypted.txt. Pour vérifier que le déchiffrement a réussi, affichez le contenu de ce nouveau fichier.

""" 
Emma@Bob:~$ cat decrypted.txt
This is a secret message.
"""

""" 
Lab 5 : Signatures Numériques avec RSA en Cryptographie    
"""
#Concept de Signature Numérique
#Dans cette étape, nous allons commencer par comprendre le concept fondamental d'une signature numérique. Une signature numérique est créée par l'expéditeur en utilisant sa clé privée (private key). Cette clé est gardée secrète et n'est connue que de l'expéditeur. La signature peut ensuite être vérifiée par toute personne possédant la clé publique (public key) correspondante de l'expéditeur.
#Ce processus fournit deux garanties de sécurité essentielles :
#Authenticité : Puisque seul l'expéditeur possède la clé privée, une signature valide prouve que le message provient bien de lui.
#Intégrité : La signature est mathématiquement liée au contenu du message. Si le message est modifié de quelque manière que ce soit, la signature ne sera plus valide.
#Pour faciliter ce laboratoire, le processus de configuration a déjà généré une paire de clés RSA pour vous : private.pem (votre clé secrète) et public.pem (votre clé partageable). Il a également créé un fichier nommé message.txt. Listons les fichiers dans notre répertoire de projet pour les visualiser.
"""
Emma@Bob:~$ ls -l
total 44
drwxr-xr-x 2 Emma Emma 4096 Oct  2 21:43 Cryptographie
-rw------- 1 Emma Emma    2 Oct  2 21:53 a.save
-rw-r--r-- 1 Emma Emma   65 Oct  2 21:54 aes.key
-rw-r--r-- 1 Emma Emma   26 Oct  8 15:55 decrypted.txt
-rw-r--r-- 1 Emma Emma  256 Oct  8 15:50 encrypted.bin
-rw-r--r-- 1 Emma Emma   48 Oct  2 22:02 encrypted.dat
-rw-r--r-- 1 Emma Emma    0 Oct  2 21:09 file.
-rw-r--r-- 1 Emma Emma  488 Oct  6 16:17 hash_password.py
-rw-r--r-- 1 Emma Emma   26 Oct  8 15:49 message.txt
-rw-r--r-- 1 Emma Emma   29 Oct  6 16:12 original.txt
-rw------- 1 Emma Emma 1704 Oct  8 15:46 private.pem
-rw-r--r-- 1 Emma Emma  451 Oct  8 15:48 public.pem
"""
#Signer le Message avec la Clé Privée
#Dans cette étape, vous allez créer une signature numérique pour le fichier message.txt. Le processus implique deux actions principales : premièrement, la création d'un hachage cryptographique (une chaîne d'octets unique de taille fixe) du message, et deuxièmement, le chiffrement de ce hachage avec votre clé privée. Le résultat est la signature numérique.
#Nous utiliserons la commande openssl dgst pour effectuer cette opération. Exécutons la commande pour signer message.txt.
"""
Emma@Bob:~$ openssl dgst -sha256 -sign private.pem -out signature.bin message.txt
"""
#Décortiquons cette commande :
#openssl dgst: Ceci invoque la commande de résumé (digest) OpenSSL.
#-sha256: Ceci spécifie l'algorithme SHA-256 pour créer le hachage du message.
#-sign private.pem: Ceci indique à OpenSSL de signer le hachage en utilisant la clé privée spécifiée, private.pem.
#-out signature.bin: Ceci spécifie le fichier de sortie où la signature binaire résultante sera stockée.
#message.txt: Ceci est le fichier d'entrée que nous signons.
#Après avoir exécuté la commande, un nouveau fichier nommé signature.bin sera créé. Ce fichier contient la signature numérique. Vous pouvez vérifier sa création en listant à nouveau les fichiers.
"""
Emma@Bob:~$ ls -l
total 48
drwxr-xr-x 2 Emma Emma 4096 Oct  2 21:43 Cryptographie
-rw------- 1 Emma Emma    2 Oct  2 21:53 a.save
-rw-r--r-- 1 Emma Emma   65 Oct  2 21:54 aes.key
-rw-r--r-- 1 Emma Emma   26 Oct  8 15:55 decrypted.txt
-rw-r--r-- 1 Emma Emma  256 Oct  8 15:50 encrypted.bin
-rw-r--r-- 1 Emma Emma   48 Oct  2 22:02 encrypted.dat
-rw-r--r-- 1 Emma Emma    0 Oct  2 21:09 file.
-rw-r--r-- 1 Emma Emma  488 Oct  6 16:17 hash_password.py
-rw-r--r-- 1 Emma Emma   26 Oct  8 15:49 message.txt
-rw-r--r-- 1 Emma Emma   29 Oct  6 16:12 original.txt
-rw------- 1 Emma Emma 1704 Oct  8 15:46 private.pem
-rw-r--r-- 1 Emma Emma  451 Oct  8 15:48 public.pem
-rw-r--r-- 1 Emma Emma  256 Oct  8 17:56 signature.bin
"""
#Vérifier la Signature avec la Clé Publique
#Dans cette étape, nous allons jouer le rôle d'un destinataire qui souhaite vérifier la signature. Pour ce faire, le destinataire a besoin de trois éléments : le message original (message.txt), la signature numérique (signature.bin), et la clé publique de l'expéditeur (public.pem).
#Le processus de vérification inverse le processus de signature. OpenSSL utilisera la clé publique pour déchiffrer la signature, révélant ainsi le hachage original. Il calculera ensuite indépendamment un nouveau hachage du message qu'il a reçu. Si les deux hachages correspondent, la signature est valide.
#Utilisons à nouveau openssl dgst, mais cette fois avec l'option -verify.
"""
Emma@Bob:~$ openssl dgst -sha256 -verify public.pem -signature signature.bin message.txt
Verified OK
"""
#Voici la décomposition de la commande de vérification :
#-verify public.pem: Ceci indique à OpenSSL de vérifier une signature en utilisant la clé publique spécifiée, public.pem.
#-signature signature.bin: Ceci spécifie le fichier de signature à vérifier.
#message.txt: Ceci est le fichier de message original auquel la signature est censée correspondre.
#Cette confirmation signifie deux choses : le message a été signé sans aucun doute par le propriétaire de la clé private.pem, et le contenu de message.txt n'a pas été modifié depuis sa signature.

#Signer le Fichier avec la Clé Privée
#Dans cette étape, nous allons renforcer le processus de signature en l'appliquant à un fichier différent. Cela aidera à consolider votre compréhension de la manière dont un hachage signé est créé et utilisé. Nous avons un autre fichier dans notre répertoire nommé document.txt. Nous allons maintenant créer une signature numérique pour ce document.
#La procédure est identique à celle que nous avons suivie à l'Étape 2. Nous allons générer un hachage SHA-256 de document.txt et signer ensuite ce hachage avec notre clé private.pem.
#Créons la signature et sauvegardons-la dans un fichier nommé document.sig.
"""
Emma@Bob:~$ touch document.txt
Emma@Bob:~$ cat document.txt
Emma@Bob:~$ echo "This is an important document that needs to be signed."  > document.txt
Emma@Bob:~$ cat document.txt
This is an important document that needs to be signed.
"""
#Signer le Fichier avec la Clé Privée
#Dans cette étape, nous allons renforcer le processus de signature en l'appliquant à un fichier différent. Cela aidera à consolider votre compréhension de la manière dont un hachage signé est créé et utilisé. Nous avons un autre fichier dans notre répertoire nommé document.txt. Nous allons maintenant créer une signature numérique pour ce document.
#La procédure est identique à celle que nous avons suivie à l'Étape 2. Nous allons générer un hachage SHA-256 de document.txt et signer ensuite ce hachage avec notre clé private.pem.
#Créons la signature et sauvegardons-la dans un fichier nommé document.sig.
"""
Emma@Bob:~$ openssl dgst -sha256 -sign private.pem -out document.sig document.txt
"""
#Cette commande crée un nouveau fichier de signature, document.sig, qui est spécifique au contenu actuel de document.txt. Tout changement apporté au document nécessiterait la génération d'une nouvelle signature.
#Listons les fichiers pour confirmer que document.sig a été créé.
"""
Emma@Bob:~$ ls
Cryptographie  decrypted.txt  encrypted.bin  hash_password.py  private.pem
a.save         document.sig   encrypted.dat  message.txt       public.pem
aes.key        document.txt   file.          original.txt      signature.bin
"""
#Tester la Modification de Signature
#Dans cette dernière étape, nous allons démontrer la caractéristique la plus critique d'une signature numérique : la protection de l'intégrité. Nous allons intentionnellement altérer le fichier document.txt après qu'il ait été signé, puis tenter de le vérifier avec la signature originale. Cela montrera comment les signatures numériques empêchent les modifications non autorisées.
#Tout d'abord, ajoutons du texte au fichier document.txt. Cela simule un attaquant modifiant le document.
"""
Emma@Bob:~$ echo "This is an unauthorized change." >> document.txt
"""
#Le contenu de document.txt a maintenant changé. La signature originale, document.sig, a été créée sur la base du contenu précédent du fichier.
#Maintenant, essayons de vérifier le fichier document.txt modifié en utilisant la signature originale document.sig et la clé publique.
"""
Emma@Bob:~$ openssl dgst -sha256 -verify public.pem -signature document.sig document.txt
Verification failure
40772612617A0000:error:02000068:rsa routines:ossl_rsa_verify:bad signature:../crypto/rsa/rsa_sign.c:441:
40772612617A0000:error:1C880004:Provider routines:rsa_verify_directly:RSA lib:../providers/implementations/signature/rsa_sig.c:1035:
"""
#Cet échec est le résultat attendu. Il se produit parce que le hachage du document.txt modifié ne correspond plus au hachage qui a été chiffré à l'intérieur de document.sig. Cela prouve instantanément que le fichier a été falsifié depuis sa signature. Ce mécanisme est fondamental pour faire confiance aux documents et communications numériques.

#Résumé
#Dans ce laboratoire, vous avez réussi à apprendre l'application pratique des signatures numériques en utilisant RSA et OpenSSL.
#Vous avez parcouru l'ensemble du processus :
#Compris les concepts fondamentaux d'authenticité et d'intégrité fournis par les signatures numériques.
#Utilisé une clé privée (private.pem) pour signer un message et créer un fichier de signature.
#Utilisé la clé publique correspondante (public.pem) pour vérifier la signature et confirmer l'authenticité du message.
#Constaté un Verification failure (échec de vérification) après avoir intentionnellement falsifié un fichier signé, démontrant ainsi comment les signatures numériques protègent l'intégrité des données.
#Cette expérience pratique fournit une base solide pour comprendre comment la confiance est établie dans le monde numérique, un concept crucial en cybersécurité et en informatique moderne.

"""
Lab 6 : Échange de Clés Basique avec Diffie-Hellman en Cryptographie

Emma@Bob:~$ openssl dhparam -out dhparam.pem 2048
"""
#Décortiquons cette commande :
#openssl dhparam: Ceci invoque l'outil de gestion des paramètres DH dans OpenSSL.
#-out dhparam.pem: Ce drapeau spécifie que la sortie doit être enregistrée dans un fichier nommé dhparam.pem.
#2048: C'est la longueur en bits souhaitée pour le module premier p.
"""
Generating DH parameters, 2048 bit long safe prime
...+........................................................................................................................................................................................................................................................................................................................................................................................+..............................................................................................................+................................+.......................................................................................................................................+...............................+..+................................+.....................................................................+...............................................................................................................................+...........................................................................................................+..............................+.................................................................................................+..........................................................................................................................................................+...................................+.................................................................................................................+...................................................................................................................................................................................+............................................................................................+...........................................................................................................................................................................+............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................+....................................+.....................................+...............................................+..............................+......................................................................................+...................................................................................................+...................................+.....................................................................................................................................................................................................+..............................+....................................+..........................................................................................................................................................................................................................................................................................................................................................................................................................................+.........++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*
Emma@Bob:~$ openssl genpkey -paramfile dhparam.pem -out a_private_key.pem
"""
#genpkey: La commande pour générer une clé privée.
#-paramfile dhparam.pem: Ceci indique à genpkey d'utiliser les paramètres de notre fichier dhparam.pem pour créer une clé DH.
#-out a_private_key.pem: Ceci enregistre la clé privée générée dans le fichier a_private_key.pem.
"""
Emma@Bob:~$ openssl pkey -in a_private_key.pem -pubout -out a_public_key.pem
"""
#pkey: Une commande pour gérer les clés publiques et privées.
#-in a_private_key.pem: Spécifie la clé privée d'entrée.
#-pubout: Ce drapeau demande à la commande de produire la partie publique de la clé.
#-out a_public_key.pem: Enregistre la clé publique résultante dans a_public_key.pem
"""
Emma@Bob:~$ openssl genpkey -paramfile dhparam.pem -out b_private_key.pem
Emma@Bob:~$ openssl pkey -in b_private_key.pem -pubout -out b_public_key.pem
Emma@Bob:~$ openssl pkeyutl -derive -inkey a_private_key.pem -peerkey b_public_key.pem -out a_shared_secret.bin
"""
#pkeyutl: Un utilitaire pour effectuer des opérations de clé publique.
#-derive: Cette action indique à l'utilitaire de dériver un secret partagé.
#-inkey a_private_key.pem: Spécifie la clé privée propre à la Partie A.
#-peerkey b_public_key.pem: Spécifie la clé publique de l'autre partie (le "pair").
#-out a_shared_secret.bin: Enregistre le secret binaire résultant dans un fichier.
"""
Emma@Bob:~$ openssl pkeyutl -derive -inkey b_private_key.pem -peerkey a_public_key.pem -out b_shared_secret.bin
Emma@Bob:~$ cmp a_shared_secret.bin b_shared_secret.bin
Emma@Bob:~$ sha256sum *.bin
9823cb9f86ea80621d5f4f3864bea08870bc5c2ef45e9298d6f2693c7405bdc9  a_shared_secret.bin
9823cb9f86ea80621d5f4f3864bea08870bc5c2ef45e9298d6f2693c7405bdc9  b_shared_secret.bin
c5d8dc2d83e68e6f9bab7f85c67146ab1851735da5ccea0884e942eb2a7b0687  encrypted.bin
bf0896911f39f81e00b851546c8bfefecb03e3dddb96c08f95eaa170f1662bc1  signature.bin
"""

"""
Lab 7 : Authentification de Message avec HMAC en Cryptographie
    """
#Introduction au HMAC
#Dans cette étape, nous allons aborder le concept fondamental du HMAC et pourquoi il est essentiel pour une communication sécurisée.
#Une fonction de hachage standard, comme SHA-256, prend un message en entrée et produit une chaîne de caractères de taille fixe, connue sous le nom de hachage ou digest. Si ne serait-ce qu'un seul bit du message est modifié, le hachage résultant sera complètement différent. C'est excellent pour vérifier l'intégrité des données. Cependant, cela n'assure pas l'authenticité. Si un attaquant intercepte et modifie un message, il peut simplement calculer un nouveau hachage pour le message falsifié et l'envoyer. Le destinataire n'aurait aucun moyen de savoir que le message a été altéré.
#Le HMAC résout ce problème en introduisant une clé symétrique secrète dans le processus de hachage. Une clé symétrique est une information secrète partagée uniquement entre l'expéditeur et le destinataire prévu.
#Le processus HMAC fonctionne approximativement comme suit :
#L'expéditeur combine la clé secrète avec le message.
#Une fonction de hachage (par exemple, SHA-256) est appliquée à cette combinaison.
#Le hachage résultant, appelé maintenant HMAC, est envoyé avec le message original.
#Lorsque le destinataire reçoit le message et le HMAC, il effectue le même calcul en utilisant sa copie de la clé secrète.
#Si le HMAC calculé correspond au HMAC reçu, le destinataire sait que le message n'a pas été altéré (intégrité) et qu'il provient de quelqu'un qui possède la clé secrète (authenticité).
#Si les HMAC ne correspondent pas, le message est considéré comme compromis et doit être rejeté.
#Cette étape est purement conceptuelle. Dans les étapes suivantes, vous mettrez cette théorie en pratique.
#Générer la Clé Secrète HMAC
#Dans cette étape, vous allez générer une clé secrète aléatoire et sécurisée qui est le fondement de la sécurité du HMAC. Une clé prévisible permettrait à un attaquant de forger des HMAC. Nous utiliserons l'outil openssl, un utilitaire polyvalent en ligne de commande pour la cryptographie.
#Nous utiliserons la commande openssl rand pour générer des données aléatoires.
#-hex: Cette option indique à openssl de produire les données aléatoires sous forme de chaîne hexadécimale.
#32: Ceci spécifie le nombre d'octets aléatoires à générer. 32 octets équivalent à 256 bits, ce qui est une longueur de clé forte et couramment utilisée, surtout lorsqu'elle est associée à l'algorithme de hachage SHA-256.
"""
Emma@Bob:~$ export HMAC_KEY=$(openssl rand -hex 32)
"""
#Cette commande exécute openssl rand -hex 32, et sa sortie (la clé hexadécimale) est capturée et assignée à la variable HMAC_KEY.
"""
Emma@Bob:~$ echo $HMAC_KEY
ea841340718972818e8ea8a4b2fae2c86805018d6567cee8f7da00d93b7b7e3a
"""
#Calculer HMAC-SHA256
#Dans cette étape, vous allez calculer un HMAC pour un message d'exemple en utilisant la clé que vous avez générée. Tout d'abord, créons un fichier contenant notre message.
#Nous utiliserons la commande echo pour créer un fichier nommé message.txt. L'option -n est importante car elle empêche echo d'ajouter un caractère de nouvelle ligne à la fin de la chaîne, ce qui modifierait le contenu et donc le HMAC final.
"""
Emma@Bob:~$ echo -n "This is a secret message." > message.txt
"""
#Maintenant, avec le message et la clé, nous pouvons calculer le HMAC. Nous utiliserons la commande openssl dgst, qui sert à calculer les digests de messages (hachages).
#-sha256: Spécifie que nous souhaitons utiliser l'algorithme de hachage SHA-256.
#-mac hmac: Spécifie que nous souhaitons calculer un Code d'Authentification de Message (Message Authentication Code, MAC) en utilisant la méthode HMAC.
#-macopt hexkey:$HMAC_KEY: Ceci fournit les options pour l'algorithme MAC. Ici, nous spécifions que notre clé est au format hexadécimal (hexkey) et nous passons la clé elle-même en utilisant la variable d'environnement $HMAC_KEY que nous avons créée précédemment.
#message.txt: Le fichier d'entrée contenant les données à authentifier.
"""
Emma@Bob:~$ openssl dgst -sha256 -mac hmac -macopt hexkey:$HMAC_KEY message.txt
HMAC-SHA2-256(message.txt)= fd7a2f302b1cc5f288c77830caaf093481c5130e83f2c307af09a8575fdf36c2
"""
#Le résultat sera le digest HMAC de votre message, calculé avec votre clé secrète. Le format de sortie affichera l'algorithme utilisé et la valeur HMAC résultante.
#Cette valeur HMAC est ce que vous enverriez avec votre message à un destinataire qui possède également la clé secrète.

#Vérifier l'Intégrité HMAC
#Dans cette étape, vous allez observer le processus de vérification du HMAC en action. Vous verrez comment l'utilisation de la clé correcte réussit, tandis que l'utilisation d'une clé incorrecte ou d'un message modifié entraîne un échec.
#Vérification avec la Clé Correcte
#La vérification n'est pas une commande spéciale ; c'est simplement l'acte pour le destinataire de recalculer le HMAC par lui-même et de le comparer à celui qu'il a reçu. Si vous exécutez à nouveau la commande de l'étape précédente, vous obtiendrez exactement la même valeur HMAC. Cela confirme que tant que la clé et le message restent inchangés, le HMAC est cohérent.
#Observer l'Échec avec une Clé Incorrecte
#Maintenant, simulons un attaquant ou une configuration incorrecte en essayant de vérifier le message avec une clé différente.
"""
Emma@Bob:~$ export WRONG_KEY=$(openssl rand -hex 32)
"""
#Essayez maintenant de calculer le HMAC pour le message.txt original, mais en utilisant cette $WRONG_KEY :
"""
Emma@Bob:~$ openssl dgst -sha256 -mac hmac -macopt hexkey:$WRONG_KEY message.txt
HMAC-SHA2-256(message.txt)= f721513c35b2a7768b67bb59f2454c89c1b82c888523b4efd7797fa4c4c84b70
"""
#Remarquez que ce HMAC est complètement différent de celui que vous avez généré avec la $HMAC_KEY correcte. Cela démontre qu'en l'absence de la clé secrète correcte, il est impossible de produire un HMAC valide pour le message, assurant ainsi l'authenticité.

#Observer l'Échec avec un Message Modifié
#Voyons également ce qui se passe si le message lui-même est falsifié. Nous allons modifier légèrement message.txt :
"""
Emma@Bob:~$ echo -n "This is a tampered message." > message.txt
Emma@Bob:~$ openssl dgst -sha256 -mac hmac -macopt hexkey:$HMAC_KEY message.txt
HMAC-SHA2-256(message.txt)= 0ef1bbe9e322060cbc584529794dd25f562cece73cbaf511035feeae1896fd3e
""" 
#Encore une fois, vous obtiendrez une valeur HMAC complètement différente. Cela prouve que toute modification apportée au message, aussi minime soit-elle, sera détectée, assurant ainsi l'intégrité.

#Implémenter HMAC en Python
#Dans cette étape, vous apprendrez à effectuer des opérations HMAC par programmation en utilisant Python. Ceci est une exigence courante dans les applications web, les API et autres logiciels qui doivent garantir la sécurité des messages. La bibliothèque standard de Python fournit les modules hmac et hashlib à cette fin.
#Nous allons écrire un script Python simple pour calculer le HMAC-SHA256 d'un message. Tout d'abord, ouvrez le fichier hmac_example.py en utilisant l'éditeur de texte nano :
"""
Emma@Bob:~$ nano hmac_example.py
Emma@Bob:~$ python3 hmac_example.py
HMAC Digest:
214fbb56f716dfe1c2f4a60615a5b901b263fd74c9678b2aef4f01779b34dea8
""" 
#Vous avez maintenant implémenté avec succès la génération de HMAC en Python, une compétence directement applicable à la construction de logiciels sécurisés.

#Résumé
#Dans ce laboratoire, vous avez acquis une expérience pratique avec les Codes d'Authentification de Message Basés sur des Fonctions de Hachage (HMAC - Hash-based Message Authentication Codes), une pierre angulaire de la cryptographie moderne pour garantir l'intégrité et l'authenticité des données.
#Vous avez appris que :
#Le HMAC combine une fonction de hachage cryptographique avec une clé secrète pour créer un code d'authentification de message.
#Seules les parties possédant la clé secrète peuvent générer ou vérifier le HMAC, empêchant ainsi la modification non autorisée et la falsification.
#L'outil en ligne de commande openssl est un utilitaire puissant pour effectuer des opérations cryptographiques, y compris la génération de clés aléatoires (openssl rand) et le calcul des HMAC (openssl dgst).
#Tout changement apporté au message ou l'utilisation d'une clé incorrecte entraînera un HMAC complètement différent, rendant la falsification facilement détectable.
#Python fournit les bibliothèques hmac et hashlib pour intégrer facilement la fonctionnalité HMAC dans vos applications.
#En maîtrisant le HMAC, vous avez franchi une étape importante vers la construction de systèmes plus sécurisés et dignes de confiance.

"""
Lab 8 : Générer des certificats X.509"""

#Un certificat X.509 est un document numérique standardisé qui contient des informations cruciales pour établir la confiance. Ses principaux composants comprennent :
#Sujet (Subject) : L'identité du détenteur du certificat (par exemple, une personne, un nom de serveur comme www.example.com).
#Émetteur (Issuer) : L'entité qui a vérifié l'identité et signé le certificat (l'Autorité de Certification ou CA).
#Clé Publique (Public Key) : La clé publique correspondant à la clé privée du sujet.
#Période de Validité (Validity Period) : Les dates (Not Before et Not After) pendant lesquelles le certificat est valide.
#Signature : La signature numérique de l'émetteur, qui garantit l'authenticité du certificat.
#Un certificat auto-signé (self-signed certificate) est un type spécial de certificat où l'émetteur et le sujet sont identiques. Essentiellement, le certificat se signe lui-même. Bien que ces certificats ne soient pas considérés comme fiables par les navigateurs ou systèmes publics (car ils ne sont pas vérifiés par une CA connue), ils sont extrêmement utiles pour les tests internes, les environnements de développement ou les réseaux privés où vous contrôlez à la fois le client et le serveur.
#Dans cette étape, vous allez créer un certificat auto-signé. Une clé privée nommée private.pem a déjà été générée pour vous dans le répertoire ~/project afin de simplifier le processus. Vous utiliserez cette clé pour générer un certificat.
#La commande openssl req est utilisée pour créer et traiter les demandes de certificat. Décomposons les options (flags) que nous allons utiliser :
#-new: Génère une nouvelle demande de certificat.
#-x509: Produit un certificat auto-signé au lieu d'une demande de certificat.
#-key private.pem: Spécifie la clé privée à utiliser.
#-out cert.pem: Spécifie le nom du fichier de sortie pour le certificat.
#-days 365: Définit la validité du certificat à 365 jours.
#-subj "...": Fournit les informations du sujet de manière non interactive.
"""
Emma@Bob:~$ openssl req -new -x509 -key private.pem -out cert.pem -days 365 -subj "/C=US/ST=California/L=Mountain View/O=MyOrg/CN=example.com"
Emma@Bob:~$ ls
ca-key.pem  ca.pem  cert.pem  private.pem
"""
#Dans cette étape, vous allez inspecter le contenu du certificat auto-signé que vous venez de créer. Cela vous permettra de vérifier ses détails et de comprendre sa structure dans un format lisible par l'homme.
#Nous utiliserons la commande openssl x509, conçue pour visualiser et manipuler les fichiers de certificat.
#-in cert.pem: Spécifie le fichier de certificat en entrée.
#-text: Affiche tous les détails du certificat au format texte.
#-noout: Empêche la commande d'afficher la version encodée du certificat.
"""
Emma@Bob:~$ openssl x509 -in cert.pem -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            ...
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = US, ST = California, L = Mountain View, O = MyOrg, CN = example.com
        Validity
            Not Before: ...
            Not After : ...
        Subject: C = US, ST = California, L = Mountain View, O = MyOrg, CN = example.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    ...
                Exponent: 65537 (0x10001)
...
"""
#Dans cette étape, vous allez générer une Demande de Signature de Certificat (CSR - Certificate Signing Request). Une CSR est un bloc de texte encodé contenant votre clé publique et vos informations d'identité. Vous envoyez une CSR à une Autorité de Certification (CA - Certificate Authority) pour demander un certificat numérique signé.
#Nous utiliserons à nouveau la commande openssl req, mais cette fois sans l'option -x509, afin qu'elle produise une CSR au lieu d'un certificat auto-signé.
#-new: Indique une nouvelle demande.
#-key private.pem: Utilise votre clé privée existante.
#-out csr.pem: Spécifie le nom du fichier de sortie pour la CSR.
#-subj "...": Fournit les informations d'identité pour le certificat que vous demandez.

"""
Emma@Bob:~$ openssl req -new -key private.pem -out csr.pem -subj "/C=US/ST=New York/L=New York City/O=MyWebApp/CN=webapp.example.com"
Emma@Bob:~$ ls
ca-key.pem  ca.pem  cert.pem  csr.pem  private.pem
"""
#Dans cette étape finale, vous allez agir en tant qu'Autorité de Certification (CA) pour signer la CSR que vous avez créée à l'étape précédente. À cette fin, un certificat de CA simple (ca.pem) et sa clé privée correspondante (ca-key.pem) ont été pré-générés dans votre environnement.
#Nous utiliserons la commande openssl x509 -req pour traiter la CSR et émettre un nouveau certificat.
#-req: Spécifie que nous traitons une CSR.
#-in csr.pem: Le fichier CSR en entrée.
#-CA ca.pem: Le certificat de la CA utilisé pour la signature.
#-CAkey ca-key.pem: La clé privée de la CA utilisée pour la signature.
#-out signed-cert.pem: Le fichier de sortie pour le certificat nouvellement signé.
#-days 365: Définit la période de validité (365 jours).
#-CAcreateserial: Crée et gère un fichier de numéro de série (ca.srl), requis pour que les CA suivent les certificats émis.
"""
Emma@Bob:~$ openssl x509 -req -in csr.pem -CA ca.pem -CAkey ca-key.pem -out signed-cert.pem -days 365 -CAcreateserial
Certificate request self-signature ok
subject=C = US, ST = New York, L = New York City, O = MyWebApp, CN = webapp.example.com
Emma@Bob:~$ openssl x509 -req -in csr.pem -CA ca.pem -CAkey ca-key.pem -out signed-cert.pem -days 365 -CAcreateserial
Certificate request self-signature ok
subject=C = US, ST = New York, L = New York City, O = MyWebApp, CN = webapp.example.com
Emma@Bob:~$ ls
ca-key.pem  ca.pem  ca.srl  cert.pem  csr.pem  private.pem  signed-cert.pem
"""
#Vous pouvez inspecter ce nouveau certificat avec openssl x509 -in signed-cert.pem -text -noout. Vous remarquerez que l'Issuer (Émetteur) est maintenant la CA (CN=myca.com), et que le Subject (Sujet) est l'identité de votre CSR (CN=webapp.example.com).
#Résumé
#Dans ce laboratoire, vous avez acquis une expérience pratique du cycle de vie fondamental des certificats X.509 en utilisant l'outil openssl.
#Vous avez réussi à apprendre comment :
#Comprendre les composants principaux d'un certificat X.509 et le concept des certificats auto-signés (self-signed certificates).
#Créer un certificat auto-signé adapté au développement et aux tests en utilisant openssl req.
#Inspecter les détails d'un certificat pour vérifier son contenu avec openssl x509.
#Générer une Demande de Signature de Certificat (CSR) pour demander formellement un certificat à une CA.
#Agir en tant que simple Autorité de Certification pour signer une CSR et émettre un nouveau certificat valide.
#Ces compétences sont essentielles pour toute personne impliquée dans l'administration système, la sécurité des réseaux ou le développement logiciel, fournissant la base pour gérer les communications sécurisées dans une variété d'applications.

"""
Lab 9 : Explorer les bases de l'infrastructure à clés publiques
"""
#Dans ce laboratoire, vous explorerez les fondamentaux de l'Infrastructure à Clé Publique (PKI - Public Key Infrastructure), le système qui soutient une grande partie de la sécurité sur Internet, y compris HTTPS. La PKI est un ensemble de rôles, de politiques, de matériel, de logiciels et de procédures nécessaires pour créer, gérer, distribuer, utiliser, stocker et révoquer des certificats numériques, ainsi que pour gérer le chiffrement à clé publique.
#Comprendre les Bases de la PKI
#Dans cette étape, nous allons aborder les concepts fondamentaux de la PKI. Aucune commande n'est à exécuter dans cette étape ; l'objectif est de construire une base théorique solide avant de commencer la pratique.
#Infrastructure à Clé Publique (PKI)
#La PKI est un cadre conçu pour améliorer la sécurité dans les communications électroniques. Elle utilise la cryptographie à clé publique pour lier les clés publiques aux identités d'utilisateurs respectives au moyen d'une Autorité de Certification (CA - Certificate Authority). Cette liaison est établie par un processus d'enregistrement et d'émission.
#Autorité de Certification (CA)
#Une Autorité de Certification est une entité de confiance qui délivre des certificats numériques. La CA agit comme une tierce partie de confiance, reconnue comme telle à la fois par le sujet (propriétaire) du certificat et par la partie qui se fie à ce certificat. Le rôle principal de la CA est de signer numériquement et de publier la clé publique liée à un utilisateur donné.
#Certificat Numérique
#Un certificat numérique est un document électronique (suivant souvent la norme X.509) qui contient :
#La clé publique du propriétaire.
#Les informations d'identification du propriétaire (comme un nom ou un nom d'hôte).
#Les informations de l'émetteur (la CA) et sa signature numérique.
#Une période de validité (date de début et de fin).
#Un numéro de série unique.
#La signature de la CA sur le certificat atteste que la clé publique contenue dans le certificat appartient à l'entité nommée dans le certificat.
#Chaîne de Confiance
#Une chaîne de confiance (ou chaîne de certificats) est une séquence de certificats, commençant par un certificat d'entité finale (par exemple, pour example.com) et se terminant par un certificat de CA Racine (Root CA).
#Certificat de CA Racine (Root CA) : Il s'agit d'un certificat auto-signé de l'autorité ultime, la CA Racine. Ces certificats sont préinstallés dans le "magasin de confiance" (trust store) de votre navigateur ou de votre système d'exploitation.
#Certificat(s) de CA Intermédiaire(s) : Les grandes CA utilisent souvent des CA intermédiaires pour délivrer des certificats aux utilisateurs finaux, protégeant ainsi la clé racine. Un certificat intermédiaire est signé par la CA Racine.
#Certificat d'Entité Finale : C'est le certificat délivré à un serveur ou un utilisateur spécifique. Il est signé par une CA intermédiaire (ou directement par la CA Racine dans des configurations plus simples).
#Lorsque votre navigateur reçoit le certificat d'un serveur, il vérifie la signature en examinant le certificat de l'émetteur. Il suit cette chaîne jusqu'à atteindre une CA Racine qui est déjà présente dans son magasin de confiance. Si la chaîne est valide et que toutes les signatures correspondent, le serveur est considéré comme digne de confiance.
#Dans cette étape, vous agirez en tant qu'Autorité de Certification (CA) et créerez ses composants fondamentaux : une clé privée et un certificat racine auto-signé. Toutes les commandes seront exécutées dans le terminal, et tous les fichiers seront créés dans votre répertoire courant, ~/project.
#Premièrement, générez la clé privée de la CA. Cette clé est le secret le plus critique de la PKI ; elle est utilisée pour signer tous les certificats émis par la CA.
"""
Emma@Bob:~$ openssl genpkey -algorithm RSA -out ca.key
..+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+......+.............+...+.....+...+.+..................+...+..+.+..............+...+.......+.....+.+..+....+........+......+.+.....+.........+.........+++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++*...+........................+.+..+....+........+...............+...+...+.+...+...
..+.......+......+..+............................+...+............+..+.+.........+.....+.+..
....+.........+..+...+......+...+.+......+.....+.........+............+.......+........+....
.....+.+.........+........+.......++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++
..........+.......+......+..+.......+.....+...+......+.+.........+.....+.+........+.......+...+........+...+.........+.+...........+...+++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++*......+..+....+......+..............+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*..+......+.+..+.+..............+..........+.................+....
+..............+...+...+..........+..+.........+...+.......+........+...+....+........+.....
.......+.........+....+......+..+.......+......+.....+....+...+..+.+...........+....+.....+.
+......+.........+......+.....+....+..............+....+...+..+...+............+...+...+.+..
.............+...+..+.+..+.+.....+......+....+..+.........+.............+..+....+.........+.
.+.+..+.+..+....+........+................+.....+......+....+.....+.......+.........+.......
.+..........+...+...+..+...+......+......+....+.....+....+..+.......+......+..+.........+...
+............+.........+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
#Ensuite, vous allez créer un certificat racine auto-signé. Un certificat racine est auto-signé car il est l'ancre ultime de confiance ; il n'y a pas d'autorité supérieure pour le signer.
#Exécutez la commande suivante pour générer le certificat. Nous utilisons l'argument -subj pour fournir les informations du sujet du certificat de manière non interactive.
"""
Emma@Bob:~$ openssl req -x509 -new -nodes -key ca.key -sha256 -days 365 -out ca.pem -subj "/C=US/ST=California/L=MountainView/O=MyLab/CN=MyLabRootCA"
"""
#Décortiquons cette commande :
#req: Utilitaire pour la Demande de Signature de Certificat (CSR - Certificate Signing Request) et la génération de certificats.
#-x509: Produit un certificat auto-signé au lieu d'une CSR.
#-new: Crée un nouveau certificat.
#-nodes: "No DES", ce qui signifie que la clé privée ne sera pas chiffrée avec une phrase de passe (passphrase). Ceci est fait pour simplifier dans notre laboratoire.
#-key ca.key: Spécifie la clé privée à utiliser pour la signature.
#-sha256: Utilise l'algorithme de hachage SHA-256 pour la signature.
#-days 365: Définit la période de validité du certificat à 365 jours.
#-out ca.pem: Spécifie le fichier de sortie pour le nouveau certificat.
#-subj "/C=.../CN=...": Fournit les détails du sujet. CN (Common Name - Nom Commun) est l'identité principale, qui, pour une CA, est son nom.
#Vous disposez maintenant d'une clé privée de CA (ca.key) et d'un certificat racine (ca.pem). Vous pouvez inspecter le contenu de votre nouveau certificat de CA :
"""
Emma@Bob:~$ openssl x509 -in ca.pem -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            ...
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = US, ST = California, L = MountainView, O = MyLab, CN = MyLabRootCA
        Validity
            Not Before: ...
            Not After : ...
        Subject: C = US, ST = California, L = MountainView, O = MyLab, CN = MyLabRootCA
        Subject Public Key Info:
            ...
"""
#Délivrer un Certificat Serveur
#Dans cette étape, vous simulerez un propriétaire de serveur demandant un certificat. Vous allez générer une clé privée et une Demande de Signature de Certificat (CSR - Certificate Signing Request) pour le serveur, puis utiliser votre CA de l'étape précédente pour signer la CSR et émettre un certificat valide.
#Premièrement, générez une clé privée pour le serveur. Cette clé doit rester secrète sur le serveur lui-même.
"""
Emma@Bob:~$ openssl genpkey -algorithm RSA -out server.key
..+...........+....+......+.....+......+.............+..+...+.........+.......+...........+...+.......+..+.......+...+...+...+...........+.+...+..+.............+.........+...+..+...+...+......+.+..+.+.....+.+.....+.+...+..+....+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*......+.....+...+.+....................+....+..+....+.....+................+........+......+.+...+........+...+.+......+...............+.....+....+.....+.+............+..+.............+.....+.+......+...............+...+......+..+...+.+...+..+...+.+...........+.+..+.+..+....+......+.....+...+.......+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*...+...+....+...+.........+.....+....+.........+..+.+..+.................
....+.........+.+....................+.+........+.+......+...+..+.+.........+...........+...
..........+..+....+...+.....+..........+...+.....+..........+...+............+........+....+
.....+.......+.....+......+.......+..+.+.........+.........+......+......+..+.+..+...+....+.
..+...............+..+......+......+.+...............+...+..+...............+.........+....+
......+......+..+.+..+...+.........+.+......+.....+.+..+.......+...........+++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++
....+..+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+.+.....+...+.......+..............+.......+..+...+.........+...+...+....+++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++*..+.......+...........+...+.+......+.....+.......+.....+...+...
.+...+......+......+...+...+...+..+....+.....+....+..............+.+......++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++
"""
#Ensuite, créez une Demande de Signature de Certificat (CSR). Une CSR est un bloc de texte encodé contenant la clé publique et d'autres informations qui seront incluses dans le certificat, telles que le nom de l'organisation et le nom de domaine. La CSR est envoyée à la CA pour signature.
"""
Emma@Bob:~$ openssl req -new -key server.key -out server.csr -subj "/C=US/ST=California/L=MountainView/O=MyWebServer/CN=example.com"
"""
#Notez que pour un certificat de serveur, le CN (Common Name - Nom Commun) doit correspondre au nom de domaine du serveur, dans ce cas, example.com.
#Maintenant, en agissant en tant que CA, vous allez signer la CSR du serveur (server.csr) avec la clé privée de votre CA (ca.key). Cette action crée le certificat serveur final (server.crt).
"""
Emma@Bob:~$ openssl x509 -req -in server.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out server.crt -days 300 -sha256
Certificate request self-signature ok
subject=C = US, ST = California, L = MountainView, O = MyWebServer, CN = example.com
"""
#Examinons les nouvelles options :
#x509 -req: Indique à OpenSSL de traiter une CSR.
#-in server.csr: Le fichier CSR d'entrée.
#-CA ca.pem: Le certificat de la CA à utiliser comme émetteur.
#-CAkey ca.key: La clé privée de la CA pour la signature.
#-CAcreateserial: Ceci crée et gère un fichier de numéro de série (ca.srl), ce qui est requis pour garantir que chaque certificat émis par la CA possède un numéro de série unique.
#-days 300: La validité pour le certificat serveur. Celle-ci devrait être plus courte que la validité du certificat de la CA.
#Enfin, inspectez le certificat serveur nouvellement créé.
"""
Emma@Bob:~$ openssl x509 -in server.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: ...
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = US, ST = California, L = MountainView, O = MyLab, CN = MyLabRootCA
        Validity
            Not Before: ...
            Not After : ...
        Subject: C = US, ST = California, L = MountainView, O = MyWebServer, CN = example.com
        ...
    Signature Algorithm: sha256WithRSAEncryption
         ...
"""
#Vérifier la Chaîne de Certificats
#Dans cette étape, vous apprendrez comment vérifier une chaîne de certificats. C'est le processus qu'un client (comme un navigateur web) effectue pour déterminer si le certificat d'un serveur est digne de confiance. Le client vérifie si le certificat a été signé par une CA en laquelle il a confiance.
#Vous pouvez utiliser la commande openssl verify pour effectuer cette vérification. Vous devez indiquer à OpenSSL quelles CA vous faites confiance en fournissant le certificat racine.
#Exécutez la commande suivante pour vérifier server.crt par rapport à votre certificat racine ca.pem :
"""
Emma@Bob:~$ openssl verify -CAfile ca.pem server.crt
server.crt: OK
"""
#Ce statut OK confirme que :
#Le certificat server.crt a bien été signé par la clé privée correspondant à la clé publique dans ca.pem.
#Le certificat n'a pas expiré.
#Voyons maintenant ce qui se passe si le vérificateur n'a pas notre CA dans sa liste de CA de confiance. Vous pouvez simuler cela en exécutant la commande verify sans l'option -CAfile.
"""
labex:project/ $ openssl verify server.crt
C = US, ST = California, L = MountainView, O = MyWebServer, CN = example.com
error 20 at 0 depth lookup: unable to get local issuer certificate
error server.crt: verification failed
"""
#L'erreur "unable to get local issuer certificate" (impossible d'obtenir le certificat de l'émetteur local) signifie que le système n'a pas pu trouver le certificat de l'émetteur (MyLabRootCA) dans son magasin de confiance par défaut. Cela démontre pourquoi il est essentiel que les clients possèdent le certificat de la CA racine pour établir une chaîne de confiance.
#Simuler la Révocation de Certificat
#Dans cette étape, vous apprendrez comment révoquer un certificat. La révocation est un processus critique lorsqu'une clé privée de certificat est compromise, ou lorsque le certificat n'est plus nécessaire avant son expiration naturelle. Ceci est géré à l'aide d'une Liste de Révocation de Certificats (CRL - Certificate Revocation List).
#Une CRL est une liste signée numériquement, émise par une CA, qui contient les numéros de série de tous les certificats qu'elle a révoqués. Les clients peuvent télécharger la CRL pour vérifier si un certificat qu'ils ont reçu est toujours valide.
#Pour gérer la révocation, openssl a besoin d'un petit fichier de configuration pour savoir où trouver les fichiers de base de données de la CA (index.txt et serial). Le script de configuration pour ce laboratoire a déjà créé le répertoire nécessaire (my-ca) et les fichiers. Créez maintenant le fichier de configuration.
#Utilisez la commande cat pour créer my-ca.conf :
"""
Emma@Bob:~$ cat << EOF > my-ca.conf
[ ca ]
default_ca = CA_default

[ CA_default ]
dir = ./my-ca
database = \$dir/index.txt
serial = \$dir/serial
private_key = ca.key
certificate = ca.pem
default_md = sha256
policy = policy_anything
crl_extensions = crl_ext
default_crl_days = 30

[ policy_anything ]
countryName = optional
stateOrProvinceName = optional
localityName = optional
organizationName = optional
organizationalUnitName = optional
commonName = supplied
emailAddress = optional

[ crl_ext ]
authorityKeyIdentifier=keyid:always
EOF
"""
#Ce fichier de configuration indique à OpenSSL comment fonctionner en tant qu'Autorité de Certification. Voici ce que fait chaque section :
#default_ca = CA_default: Pointeur vers la section de configuration principale de la CA.
#dir = ./my-ca: Répertoire de travail de la CA pour les fichiers de base de données
#database = $dir/index.txt: Base de données des certificats (suit les certificats émis/révoqués)
#serial = $dir/serial: Fichier de numéro de série pour les identifiants uniques de certificat
#private_key = ca.key: Clé privée de la CA pour la signature des certificats
#certificate = ca.pem: Le certificat propre à la CA
#default_md = sha256: Algorithme de hachage pour les signatures (SHA-256)
#policy = policy_anything: Règles de validation des certificats
#crl_extensions = crl_ext: Options de formatage de la CRL
#default_crl_days = 30: Période de validité de la CRL (30 jours)
#countryName = optional: Code pays
#stateOrProvinceName = optional: État/province
#localityName = optional: Ville/localisation
#organizationName = optional: Nom de l'organisation
#organizationalUnitName = optional: Département
#commonName = supplied: Nom de domaine/serveur (requis)
#emailAddress = optional: Adresse e-mail
#authorityKeyIdentifier=keyid:always: Inclut l'identifiant de la CA dans les CRL pour la vérification
#Ce fichier de configuration est le "manuel d'exploitation" de votre CA. Il indique à OpenSSL où trouver les clés, comment stocker les certificats et quelles règles suivre pour l'émission et la révocation des certificats.
#Maintenant, révoquez le certificat serveur (server.crt). Cette commande recherchera le numéro de série du certificat et le marquera comme révoqué dans le fichier de base de données index.txt.
"""
Emma@Bob:~$ openssl ca -config my-ca.conf -revoke server.crt
Using configuration from my-ca.conf
Adding Entry with serial number 2987A9005015FFDDEDB55D9DFFB34B98F33BDF3F to DB for /C=US/ST=California/L=MountainView/O=MyWebServer/CN=example.com
Revoking Certificate 2987A9005015FFDDEDB55D9DFFB34B98F33BDF3F.
Data Base Updated
"""
#Après la révocation, vous devez générer et publier une CRL mise à jour.
"""
Emma@Bob:~$ openssl ca -config my-ca.conf -gencrl -out my-ca.crl        
Using configuration from my-ca.conf
"""
#Ceci crée le fichier my-ca.crl, qui contient la liste des certificats révoqués.
#Enfin, essayons de vérifier à nouveau le certificat serveur, mais cette fois, nous fournirons également la CRL. Un processus de vérification approprié doit vérifier la révocation.
"""
Emma@Bob:~$ openssl verify -CAfile ca.pem -CRLfile my-ca.crl -crl_check server.crt
C = US, ST = California, L = MountainView, O = MyWebServer, CN = example.com
error 23 at 0 depth lookup: certificate revoked
error server.crt: verification failed
"""
#La commande échoue maintenant avec un message clair
#L'erreur "certificate revoked" (certificat révoqué) confirme que notre processus de révocation a réussi. Le client, lors de la vérification de la CRL, a correctement identifié que le certificat pour example.com n'est plus digne de confiance.
#Résumé
#Félicitations ! Vous avez terminé avec succès ce laboratoire sur les bases de l'Infrastructure à Clé Publique (PKI). Vous avez acquis une expérience pratique des opérations fondamentales qui sécurisent les communications numériques.
#Dans ce laboratoire, vous avez appris à :
#Comprendre les concepts fondamentaux de la PKI, des Autorités de Certification (CA) et des chaînes de confiance.
#Créer votre propre CA Racine simple en générant une clé privée et un certificat auto-signé.
#Émettre un certificat serveur en signant une Demande de Signature de Certificat (CSR - Certificate Signing Request) avec la clé de votre CA.
#Vérifier la chaîne de confiance d'un certificat en utilisant la commande openssl verify.
#Révocation d'un certificat et confirmation de son statut révoqué en générant et en utilisant une Liste de Révocation de Certificats (CRL).
#Ces compétences constituent les éléments de base pour gérer des systèmes sécurisés et comprendre comment la confiance est établie sur Internet.

"""
Lab 10 : Explorer les schémas de chiffrement hybride
"""
#Introduction
#Dans le monde de la cryptographie, nous sommes souvent confrontés à un compromis entre la vitesse et la sécurité. Les algorithmes de chiffrement symétrique comme AES sont très rapides et idéaux pour chiffrer de grandes quantités de données, mais ils nécessitent une clé secrète partagée qui doit être distribuée de manière sécurisée à la fois à l'expéditeur et au destinataire. Les algorithmes de chiffrement asymétrique comme RSA sont excellents pour l'échange de clés sécurisé en utilisant une paire de clés publique/privée, mais ils sont coûteux en calcul et trop lents pour chiffrer des données en masse.
#Le chiffrement hybride résout ce problème en combinant les forces des deux méthodes. Il utilise une approche du "meilleur des deux mondes" :
#Le chiffrement asymétrique est utilisé pour chiffrer et partager de manière sécurisée une clé symétrique temporaire et unique (souvent appelée "clé de session").
#Le chiffrement symétrique est ensuite utilisé avec cette clé de session pour chiffrer rapidement et efficacement les données du message réel, plus volumineux.
#Dans ce laboratoire, vous implémenterez un schéma de chiffrement hybride complet à partir de zéro en utilisant l'outil en ligne de commande openssl. Vous générerez une paire de clés RSA, créerez une clé de session AES aléatoire, utiliserez RSA pour chiffrer la clé de session, utiliserez AES pour chiffrer un message, et enfin, inverserez le processus pour déchiffrer le message.
#Aperçu du Chiffrement Hybride
#Dans cette étape, nous allons brièvement revoir les concepts fondamentaux qui font du chiffrement hybride une technique puissante et largement utilisée. Aucune commande n'est à exécuter dans cette étape ; l'objectif est de construire une base conceptuelle solide avant de commencer le travail pratique.
#Chiffrement Symétrique (ex. AES)
#Fonctionnement : Utilise une seule clé secrète partagée pour le chiffrement et le déchiffrement.
#Force : Très rapide et efficace, ce qui le rend parfait pour chiffrer de grands fichiers ou des flux de données.
#Faiblesse : La distribution de la clé. Comment transmettre la clé secrète partagée au destinataire de manière sécurisée ? Si un attaquant intercepte la clé, il peut déchiffrer toutes les communications.
#Chiffrement Asymétrique (ex. RSA)
#Fonctionnement : Utilise une paire de clés : une clé publique pour le chiffrement et une clé privée pour le déchiffrement. La clé publique peut être partagée librement, tandis que la clé privée doit être gardée secrète par son propriétaire.
#Force : Résout le problème de la distribution des clés. N'importe qui peut utiliser votre clé publique pour vous chiffrer un message, mais seul vous pouvez le déchiffrer avec votre clé privée.
#Faiblesse : Il est mathématiquement complexe et donc beaucoup plus lent que le chiffrement symétrique. Il est peu pratique pour chiffrer de grandes quantités de données.
#La Solution Hybride
#Le chiffrement hybride combine ces deux méthodes pour obtenir la sécurité du chiffrement asymétrique et la vitesse du chiffrement symétrique. Voici le flux de travail typique :
#L'expéditeur (Alice) souhaite envoyer un message sécurisé au destinataire (Bob).
#Alice génère une nouvelle clé de session symétrique aléatoire.
#Alice chiffre son message réel en utilisant cette clé de session symétrique rapide.
#Alice obtient la clé publique de Bob. Elle l'utilise pour chiffrer uniquement la petite clé de session symétrique.
#Alice envoie à Bob à la fois le message chiffré symétriquement et la clé de session chiffrée asymétriquement.
#Bob reçoit les deux éléments. Il utilise d'abord sa clé privée pour déchiffrer la clé de session chiffrée.
#Maintenant que Bob possède la clé de session symétrique originale, il l'utilise pour déchiffrer rapidement le message réel.
#Ce processus garantit que les données en masse sont chiffrées efficacement, et que la clé utilisée pour ce chiffrement est échangée avec une sécurité maximale. Dans les étapes suivantes, nous implémenterons exactement ce flux de travail.
#Générer les Clés RSA et AES
#Dans cette étape, nous allons générer les deux ensembles de clés requis pour notre schéma de chiffrement hybride : une paire de clés RSA (publique et privée) pour la partie asymétrique, et une clé de session aléatoire pour la partie symétrique (AES). Toutes les opérations seront effectuées dans le répertoire ~/project.
#Tout d'abord, générons une clé privée RSA de 2048 bits. Cette clé doit être gardée secrète par le destinataire.
"""
Emma@Bob:~$ openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
....+..+.+..+......+.+.....+...+......+............+...+......+....+.....+.......+............+..+....+.....+.......+...+.....+....+..+....+...........+...+.+......++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++*...........+..+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*....+..........+......+.....+...+.+........+...+.........+....+.....+......+...+.+......+.........+..+............+.+.....+......+...+++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++
......+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+..++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++*...+...+....+......+...........+...+.+....
................+.......+..+.+......+.....+.........+......+.+.....+....+...+......+........
...+.+.................+.+............+..+.+.........+..+.+..............+..................
............+.+........+.......+...+..............+.+..+...+.......+.........+...+..+.......
........+....+.....+....+...+..+......+......+++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++
"""
#Vous verrez une sortie pendant la génération de la clé. Ensuite, nous devons extraire la clé publique correspondante de la clé privée que nous venons de créer. Cette clé publique peut être partagée avec toute personne souhaitant vous envoyer un message chiffré.
"""
Emma@Bob:~$ openssl rsa -pubout -in private_key.pem -out public_key.pem
writing RSA key
"""
#La commande affichera writing RSA key.
#Maintenant, créons une clé de session aléatoire de 256 bits (32 octets). Cette clé sera utilisée avec l'algorithme AES pour chiffrer nos données réelles. Nous utilisons openssl rand pour générer des données aléatoires cryptographiquement fortes et l'encodons en Base64 pour une manipulation plus facile.
"""
Emma@Bob:~$ openssl rand -base64 32 > session_key.key
"""
#Listons les fichiers dans notre répertoire pour voir les clés que nous avons créées.
"""
Emma@Bob:~$ ls -l        
total 16
-rw-rw-r-- 1 labex labex   57 Oct 29 00:03 message.txt
-rw------- 1 labex labex 1704 Oct 29 00:05 private_key.pem
-rw-rw-r-- 1 labex labex  451 Oct 29 00:07 public_key.pem
-rw-rw-r-- 1 labex labex   45 Oct 29 00:08 session_key.key
"""
#Vous devriez voir les trois fichiers de clés que vous venez de générer, ainsi que le fichier message.txt créé lors de la configuration.
#Chiffrer la Clé de Session avec RSA
#Dans cette étape, nous allons effectuer une partie critique du processus de chiffrement hybride : le chiffrement de la clé de session symétrique. Pour garantir que seule la personne destinataire prévue puisse utiliser la clé de session, nous allons la chiffrer à l'aide de sa clé publique RSA.
#Nous utiliserons la commande openssl pkeyutl, qui est un utilitaire pour les opérations de clé publique. Nous l'utiliserons pour chiffrer le fichier session_key.key avec la clé public_key.pem.
"""
Emma@Bob:~$ openssl pkeyutl -encrypt -pubin -inkey public_key.pem -in session_key.key -out encrypted_session_key.bin
"""
#Décortiquons cette commande :
#pkeyutl: L'outil d'utilité pour les clés publiques (public key utility tool).
#-encrypt: Spécifie que nous souhaitons effectuer une opération de chiffrement.
#-pubin: Indique que la clé d'entrée (-inkey) est une clé publique.
#-inkey public_key.pem: Spécifie la clé publique à utiliser pour le chiffrement.
#-in session_key.key: Le fichier d'entrée à chiffrer (notre clé de session AES).
#-out encrypted_session_key.bin: Le fichier de sortie où la clé chiffrée sera stockée.
#Cette commande crée un nouveau fichier, encrypted_session_key.bin, qui contient la clé de session sous une forme chiffrée. Ce fichier peut maintenant être transmis en toute sécurité, car seul le propriétaire de la clé privée correspondante peut le déchiffrer.
"""
Emma@Bob:~$ ls -l encrypted_session_key.bin
-rw-rw-r-- 1 labex labex 256 Oct 29 00:11 encrypted_session_key.bin
"""
#Chiffrer les Données avec AES
#Maintenant que nous avons sécurisé notre clé de session, nous pouvons utiliser la clé de session originale, non chiffrée, pour chiffrer rapidement notre fichier de données principal, message.txt. Nous utiliserons le chiffrement symétrique AES-256-CBC pour cette tâche.
#La commande openssl enc exige que la clé (key) et le Vecteur d'Initialisation (IV - Initialization Vector) soient fournis au format hexadécimal. Notre session_key.key est en Base64, nous devons donc d'abord le décoder et le convertir en hexadécimal. Nous allons également générer un IV aléatoire. Nous stockerons les deux dans des variables d'environnement pour plus de commodité.
#Premièrement, convertissez la clé de session et stockez-la dans la variable AES_KEY :
"""
Emma@Bob:~$ export AES_KEY=$(cat session_key.key | base64 -d | xxd -p -c 32)
"""
#Ensuite, générez un IV aléatoire de 128 bits (16 octets) et stockez-le dans la variable AES_IV. Un IV est utilisé pour garantir que le chiffrement du même texte clair plusieurs fois produit des textes chiffrés différents.
"""
Emma@Bob:~$ export AES_IV=$(openssl rand -hex 16)
"""
#Avec la clé et l'IV prêts, nous pouvons maintenant chiffrer message.txt en utilisant openssl enc :
"""
Emma@Bob:~$ openssl enc -aes-256-cbc -in message.txt -out encrypted_message.dat -K $AES_KEY -iv $AES_IV
"""
#Examinons les options de la commande :
#-aes-256-cbc: Spécifie le chiffrement AES-256 en mode CBC.
#-in message.txt: Le fichier de données d'entrée.
#-out encrypted_message.dat: Le fichier de sortie pour les données chiffrées.
#-K $AES_KEY: La clé de chiffrement au format hexadécimal (K majuscule).
#-iv $AES_IV: Le vecteur d'initialisation au format hexadécimal.
#À ce stade, l'expéditeur empaquèterait encrypted_message.dat, encrypted_session_key.bin, et l'IV ($AES_IV) pour les envoyer au destinataire. Pour ce laboratoire, nous avons tous les fichiers dans notre répertoire, prêts pour l'étape de déchiffrement.
#Vérifions que le fichier de données chiffré a été créé :
"""
Emma@Bob:~$ ls -l encrypted_message.dat
-rw-rw-r-- 1 labex labex 64 Oct 29 00:15 encrypted_message.dat
"""
#Déchiffrer le Message
#Dans cette étape finale, nous allons simuler les actions du destinataire. Le destinataire a reçu les données chiffrées (encrypted_message.dat), la clé de session chiffrée (encrypted_session_key.bin), et l'IV. Il utilisera sa clé privée secrète pour inverser le processus et récupérer le message original.
#Premièrement, le destinataire doit déchiffrer la clé de session en utilisant sa private_key.pem.
"""
Emma@Bob:~$ openssl pkeyutl -decrypt -inkey private_key.pem -in encrypted_session_key.bin -out decrypted_session_key.key
"""
#Cette commande utilise pkeyutl avec l'indicateur -decrypt et la clé privée pour récupérer la clé de session AES originale, en l'enregistrant dans decrypted_session_key.key.
#Nous pouvons rapidement vérifier que la clé déchiffrée est identique à l'originale que nous avons créée à l'Étape 2. La commande diff ne devrait produire aucune sortie si les fichiers sont identiques.
"""
Emma@Bob:~$ diff session_key.key decrypted_session_key.key
"""
#Maintenant que nous avons la clé de session, nous pouvons déchiffrer le message principal. Tout comme lors de l'étape de chiffrement, nous devons d'abord convertir la clé au format hexadécimal.
"""
Emma@Bob:~$ export DECRYPTED_AES_KEY=$(cat decrypted_session_key.key | base64 -d | xxd -p -c 32)
"""
#Enfin, utilisez openssl enc avec l'indicateur -d (decrypt/déchiffrer), en fournissant la même clé et le même IV qui ont été utilisés pour le chiffrement. (La variable $AES_IV est toujours définie dans notre shell depuis l'étape précédente).
"""
Emma@Bob:~$ openssl enc -d -aes-256-cbc -in encrypted_message.dat -out decrypted_message.txt -K $DECRYPTED_AES_KEY -iv $AES_IV
"""
#Le processus est terminé ! Le message original a été récupéré et sauvegardé dans decrypted_message.txt. Visualisons son contenu pour confirmer notre succès.
"""
Emma@Bob:~$ cat decrypted_message.txt
This is a secret message that needs to be sent securely.
"""
#Résumé
#Dans ce laboratoire, vous avez réussi à mettre en œuvre un flux complet de chiffrement et de déchiffrement hybride à l'aide d'OpenSSL. Vous avez acquis une expérience pratique des concepts fondamentaux qui sécurisent une grande partie de nos communications numériques.
#Vous avez appris à :
#Générer une paire de clés RSA pour le chiffrement asymétrique.
#Créer une clé de session AES aléatoire pour le chiffrement symétrique.
#Sécuriser la clé de session en utilisant la clé publique RSA.
#Chiffrer efficacement les données volumineuses en utilisant la clé de session AES.
#Inverser le processus en déchiffrant la clé de session avec la clé privée RSA, puis en déchiffrant les données.
#Cette approche qui combine le meilleur des deux mondes ("best of both worlds"), en alliant la sécurité de la cryptographie asymétrique pour l'échange de clés à la rapidité de la cryptographie symétrique pour le chiffrement des données, est une pierre angulaire des protocoles de sécurité modernes tels que TLS/SSL qui protègent vos données sur Internet tous les jours.






