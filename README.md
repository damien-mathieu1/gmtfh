# GMTFH - Give Me The F***ing Hour

A Rastafarian-themed time display utility that shows the current time in different time zones.

## Description

GMTFH (Give Me The F***ing Hour) is a simple command-line utility that displays the current time in multiple time zones with a Rastafarian twist. Perfect for when you need to know the time but want it delivered with some island vibes. Main purpose is to learn how to create deb package with a fun project.

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

## Uninstallation

```bash
sudo dpkg -r gmtfh
```

## Author

Damien Mathieu

## License

This is free software; see the source for copying conditions.
