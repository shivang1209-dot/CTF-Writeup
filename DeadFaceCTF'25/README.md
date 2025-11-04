# DEADFACE CTF 2025 Writeups

Welcome to my repository for the DEADFACE CTF 2025 writeups!  
This CTF was organized by **DEADFACE**, and I participated in solving challenges across multiple categories.

## Repo Structure

This repository contains the writeups for **challenges** I attempted during the DEADFACE CTF 2025 competition. Each challenge has its own folder organized by category, and inside each folder, you will find:
- A **writeup** in markdown format explaining how the challenge was solved.
- Any relevant **images** and **resources** used during the investigation.
- **Flag(s)** found from the challenge.

## Categories

### Database (1 challenge)
- **sqLite007** - SQL injection challenge involving authentication bypass and database enumeration

### Forensics (13 challenges)

#### hostBusters (3 challenges)
- **letMeIn** - SSH access and file system enumeration
- **secretStash** - Finding hidden files on a remote system
- **etCetra** - Locating and reading scripts from Ghost Town clues

#### stolenSecrets (5 challenges)
- **theSource** - Identifying attacker IP from log files
- **callingCard** - Finding flag in HTTP request headers
- **compromised** - Identifying compromised user credentials from PCAP
- **aWildUserSuddenlyAppearered** - Finding user created for persistence
- **versions** - Identifying web server version from HTTP headers

#### trojanEchoes (5 challenges)
- **whatsThePassword** - Cracking ZIP file password
- **stringTheory** - Extracting flag from binary strings (flag 01)
- **lingeringShadows** - Finding flag in Base64-encoded strings (flag 02)
- **theCallFromBeyond** - Reassembling Base64 flag fragments (flag 03)
- **watchTheBirdies** - Decoding hex and Base64 encoded flag (flag 04)

### OSINT (5 challenges)
- **dissTrack** - Finding flag in Spotify playlist description
- **gitGood** - Locating DEADFACE member's GitHub account
- **melodyWay** - Geolocation challenge using image analysis
- **potOfGreed** - Finding coffee shop location from image
- **waffWaff** - Geolocation challenge identifying country, city, and street

### Reverse (2 challenges)
- **cerealKiller101** - Binary reverse engineering and hash cracking
- **ghostInTheShell** - C64 program analysis and interactive execution

### Steganography (4 challenges)
- **badBoy** - Extracting flag from PNG trailer data
- **doubleDecode** - Decoding Base64 and hex from PNG trailer
- **secretFrog** - Extracting and fixing corrupted GIF from PNG
- **thinkOutsideTheBox3** - Using stegsolve to reveal hidden text

### Web - hacktheNight (12 challenges)
- **theSourceOfOurTroubles** - Finding flag in HTML comments
- **accessGranted** - SQL injection authentication bypass
- **consoleChaos** - Finding flag in browser console logs
- **hiddenPaths** - Finding flag in robots.txt
- **classified** - SQL injection to extract classified research
- **notSoPublicDomain** - SQL injection to find hidden announcements
- **pestControl** - Finding flag in debug API endpoint
- **reverseCourse** - Command injection to read database backup
- **stickToTheScript** - Decoding Base64 from JavaScript comments
- **theInvisibleMan** - IDOR vulnerability exploitation
- **classified** - Additional classified research access

## Repo Structure

The structure of the repository is as follows:

```
DEADFACE CTF'25/
│
├── Database/
│   └── sqLite007/
│
├── Forensics/
│   ├── hostBusters/
│   ├── stolenSecrets/
│   └── trojanEchoes/
│
├── OSINT/
│   ├── dissTrack/
│   ├── gitGood/
│   ├── melodyWay/
│   ├── potOfGreed/
│   └── waffWaff/
│
├── Reverse/
│   ├── cerealKiller101/
│   └── ghostInTheShell/
│
├── Steganography/
│   ├── badBoy/
│   ├── doubleDecode/
│   ├── secretFrog/
│   └── thinkOutsideTheBox3/
│
├── Web/
│   └── hacktheNight/
│
└── README.md
```

---

*Happy Hacking! 🎃*

