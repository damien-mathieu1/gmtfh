# GMTFH - Give Me The F\*\*\*ing Hour

A Rastafarian-themed time display utility that shows the current time in different time zones.

## Description

GMTFH (Give Me The F\*\*\*ing Hour) is a simple command-line utility that displays the current time in multiple time zones with a Rastafarian twist. Perfect for when you need to know the time but want it delivered with some island vibes. Main purpose is to learn how to create deb package with a fun project.

## Features

- Displays current time in Paris (local time)
- Displays current time in Jamaica
- Rastafarian-themed output messages

## Installation

### From Debian Package

```bash
sudo dpkg -i gmtfh.deb
```

If you encounter dependency issues, run:

```bash
sudo apt-get install -f
```

### From Local Mirror

1. Add the local repository to your sources:

```bash
echo "deb [trusted=yes] file:///path/to/mirror ./" | sudo tee /etc/apt/sources.list.d/local-mirror.list
```

2. If using signed packages, import the GPG key:

```bash
# Export the key from the mirror maintainer
sudo cp mirror-key.gpg /etc/apt/trusted.gpg.d/
sudo chmod 644 /etc/apt/trusted.gpg.d/mirror-key.gpg
```

3. Update and install:

```bash
sudo apt update
sudo apt install gmtfh-damien-mathieu
```

### Using Signed Repositories

For better security, it's recommended to use the `signed-by` option in your sources list which explicitly specifies which key to use for verification:

```bash
# Copy the exported key to the trusted.gpg.d folder
sudo cp gmtfh-damien-mathieu.gpg /etc/apt/trusted.gpg.d/
sudo chmod 644 /etc/apt/trusted.gpg.d/gmtfh-damien-mathieu.gpg

# Add the repository with signed-by option
echo "deb [signed-by=/etc/apt/trusted.gpg.d/gmtfh-damien-mathieu.gpg] http://localhost/mirror ./" | \
  sudo tee /etc/apt/sources.list.d/gmtfh-mirror.list

# Update and install
sudo apt update
sudo apt install gmtfh-damien-mathieu
```

This approach is more secure than using the deprecated `trusted=yes` option or the global keyring, as it explicitly links the repository with its specific signing key.

### Using a Remote Test Mirror

You can also use a remote test mirror instead of a local one. Here's how to add the remote mirror at http://162.38.112.140:9000/mirror/ to your sources list with proper GPG verification:

```bash
# Download the GPG key from the remote mirror
wget http://162.38.112.140:9000/mirror/gmtfh-damien-mathieu.gpg

# Copy the key to the trusted.gpg.d folder
sudo cp gmtfh-damien-mathieu.gpg /etc/apt/trusted.gpg.d/
sudo chmod 644 /etc/apt/trusted.gpg.d/gmtfh-damien-mathieu.gpg

# Add the repository with signed-by option
echo "deb [signed-by=/etc/apt/trusted.gpg.d/gmtfh-damien-mathieu.gpg] http://162.38.112.140:9000/mirror ./" | \
  sudo tee /etc/apt/sources.list.d/gmtfh-remote-mirror.list

# Update and install
sudo apt update
sudo apt install gmtfh-damien-mathieu
```

This configures your system to verify packages from the remote mirror using the downloaded GPG key, ensuring that the packages you install are authentic and haven't been tampered with.

### Dependencies

This package depends on:

- python3
- python3-dateutil

## Usage

Simply run the command in your terminal:

```bash
gmtfh
```

## Package Structure

- `/lib/gmtfh.py` - The main Python script
- `/usr/bin/gmtfh` - Symlink to the main script (created during installation)

## Setting Up a Local Mirror

### Managing GPG Keys

Before signing packages, you need a GPG key. Here's how to manage your keys:

#### List Existing GPG Keys

```bash
# List all public keys
gpg --list-keys

# List secret keys (the ones you can sign with)
gpg --list-secret-keys --keyid-format LONG
```

The output will show your key ID (like `3AA5C34371567BD2`) which you'll use for signing.

#### Create a New GPG Key if Needed

```bash
# Generate a new GPG key
gpg --full-generate-key
```

Follow the prompts:

1. Select key type (RSA and RSA is recommended)
2. Choose key size (2048 or 4096 bits recommended)
3. Set expiration time
4. Enter your name, email and comment
5. Set a strong passphrase

After creation, list your keys again to find your new key ID.

1. Build the package:

```bash
./make_deb gmtfh-damien-mathieu
```

2. Create a mirror directory:

```bash
mkdir -p /var/www/html/mirror
cp gmtfh-damien-mathieu_1.0_all.deb /var/www/html/mirror/
```

3. Sign the package with GPG (optional):

```bash
gpg --default-key YOUR_KEY_ID --detach-sign gmtfh-damien-mathieu_1.0_all.deb
# This creates gmtfh-damien-mathieu_1.0_all.deb.sig
cp gmtfh-damien-mathieu_1.0_all.deb.sig /var/www/html/mirror/
```

4. Generate repository index:

```bash
./make_release /var/www/html/mirror YOUR_KEY_ID
```

5. Export your GPG key for users:

```bash
gpg --export YOUR_KEY_ID > gmtfh-damien-mathieu.gpg
chmod 644 gmtfh-damien-mathieu.gpg
```

## Uninstallation

```bash
sudo dpkg -r gmtfh
```

## Author

Damien Mathieu

## License

This is free software; see the source for copying conditions.
