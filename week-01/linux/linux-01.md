# Table of Contents

1.  [Software movements and philosophies](#org4ccec5c)
    1.  [Open Source Initiative](#org1b0b1dc)
    2.  [Free Software Movement](#org3896d22)
    3.  [Proprietary softwares](#orga458d48)
2.  [UNIX](#org603eae4)
    1.  [UNIX Philosophy](#orgce9d735)
3.  [Linux and/or GNU](#org7551ed2)
    1.  [GNU](#org96167eb)
    2.  [Linux](#orge8c5957)
4.  [Essential Linux](#org776f265)
    1.  [Teletypewriters](#org6927fff)
        1.  [Virtual TTY](#org06186f6)
        2.  [Pseudo-TTY (PTS)](#orgad3b1dd)
    2.  [WM&rsquo;s and DE&rsquo;s](#org366d464)
        1.  [Window Manager](#org62cdae3)
        2.  [Desktop Environment](#org86f360b)
    3.  [Distributions](#org8807cdf)
    4.  [Ubuntu](#orge3ef540)

<a id="org4ccec5c"></a>

# Software movements and philosophies

<a id="org1b0b1dc"></a>

## Open Source Initiative

![img](./images/open-source-iniative.png)

- To make software open-sourced.
- Aims to make well-working software by virtue of collaboration.
- No comments about the means to and from development.
- Restrictions on end-user can exist depsite being open sourced
- Free open source software points more to the price than freedom.

<a id="org3896d22"></a>

## Free Software Movement

![img](./images/fsf.png)

- To make software &ldquo;libre&rdquo; for everyone.
- End-user has god-level control over any such software they use.
- The four freedoms:
  1.  Use
  2.  Study
  3.  Modify
  4.  Distribute
- Monetization can exist, if it still respects these four freedoms.
  principles.

<a id="orga458d48"></a>

## Proprietary softwares

- Users have only limited control over the entire software.
- Modifications, distributions etc. can cause lawsuits.

- <del>FOSS</del> FLOSS
- The philosophy is contained in the _licence_.

<a id="org603eae4"></a>

# UNIX

- UNIX (UNICS) system, developed at Bell Labs in the mid 1960s.
- Cascade of ownership transfers results in:
  - BSD
  - Solaris
  - Xenix
  - AIX
  - Darwin, etc.
- Based on **Unix philosophy**.
- Portability due to being written almost entirely in C.
- Notable features include
  - Hierarchial file-system
  - Everything is a file
  - Plain text data
  - Piping
  - a **kernel** between hardward and processes
- Components of every `*N*X` system:
  - Kernel
  - Shell + essential commands
  - Utilities

<a id="orgce9d735"></a>

## UNIX Philosophy

- Programs should do one thing, and do it well.
- Programs should be able to be &ldquo;piped&rdquo; and work together.
- Data in communication and output should be plain text.

<a id="org7551ed2"></a>

# Linux and/or GNU

<a id="org96167eb"></a>

## GNU

![img](./images/stallman.png)

- _Richard Stallman_ started **GNU Project** in 1984.
- Ecosystem of libre softwares.
- Hurd

<a id="orge8c5957"></a>

## Linux

![img](./images/linus.jpg)

- _Linus Torvalds_ Started creating the Linux kernel in 1991.
- Based on the Unix system developed at Bell Labs.
- Linux + any software ecosystem = &ldquo;Linux&rdquo; operating system.

<a id="org776f265"></a>

# Essential Linux

<a id="org6927fff"></a>

## Teletypewriters

- Commands is the class of language `*N*X` speaks.
- Before digital era, communications were done with physical typewriters -
  with paper and ink.
- Digital interface is known as **teletypewriter** or **terminal**.
- Two kinds of teletypewriters (or **TTY**&rsquo;s):

<a id="org06186f6"></a>

### Virtual TTY

![img](./images/dec-vt100.jpg)

- Implemented by the kernel, independent of graphical environment (if any).
- These are provided by `/dev/ttyX` files.

<a id="orgad3b1dd"></a>

### Pseudo-TTY (PTS)

![img](./images/gnome-terminal.png)

- Software-emulated, provides various features - mostly graphical enhancements
- Examples include:
  - Gnome Terminal
  - Alacritty
  - Termite
  - Kitty, etc.
- Provided by `/dev/pts/X` files.

<a id="org366d464"></a>

## WM&rsquo;s and DE&rsquo;s

- GUI contained of &ldquo;windows&rdquo;
- Display server - only for viewing/handling windows, and windows only.

<a id="org62cdae3"></a>

### Window Manager

- Manages placement and appearance of windows.
- Provides options to manipulate/navigate windows.

<a id="org86f360b"></a>

### Desktop Environment

- Essentially `WM + utilities`.
- Every DE is based on some WM.
- Utilities include office suite, editors, viewers, players, games, etc.

<a id="org8807cdf"></a>

## Distributions

- Linux kernel + some utilities like:
  - Package manager
  - Installer
  - Core Utilities
  - Desktop Environment
  - Other Bloats
- Examples: Ubuntu, Fedora, Debian, Arch Linux, Gentoo Linux, OpenSUSE,
  Manjaro, Pop! OS etc.

<a id="orge3ef540"></a>

## Ubuntu

- Graphical installer - minimal configurations.
- Beginner friendly: GNOME already available (+lot of bloat)
- Lot of packages available in `apt`.
