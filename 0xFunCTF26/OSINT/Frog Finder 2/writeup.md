# Challenge Name: Frog Finder 2

## Description

**Category:** OSINT

> A frog has escaped from the prison cells of a cybersecurity club and is on the run. Somehow, they've gained the ability to roam the internet and gain human intellect. Their newest adventures are documented online — you need to track them down. The handle is likely along the lines of **@myst3ryfr0gg3r**.
>
> You will find the flag already in the format `0xfun{...}`.

---

## Writeup

### Step 1: Username Lookup

Use [whatsmyname.app](https://whatsmyname.app/) or similar to search for **myst3ryfr0gg3r** ([full results](Resources/myst3ryfr0gg3r.txt)). This leads to an X (Twitter) profile:

```
https://x.com/myst3ryfr0gg3r
```

### Step 2: Finding the GeoOSINT Image

Scroll through the profile. The user posts an image of a restaurant and hints at geoOSINT.

![Restaurant image from X profile](Resources/twitter-frogg.png)

### Step 3: Reverse Image Search

Save the image and run a **reverse image search**. One result points to a photo gallery (e.g. [alorenz.photography](https://www.alorenz.photography/gallery)).

![Reverse image search result](Resources/photo-site.png)

Searching further leads to a post indicating the location is **The Strand, London**, mentioning a cafe — **Costa**.

![Costa location on map](Resources/Costa%20coffee.png)

### Step 4: Locating the Restaurant

Search for "Costa" and "The Strand" on Google Maps. From the original image, the name **Eve** appears. Searching "Eve Bar, The Strand" gives the precise location — **Frog** restaurant.

![Frog restaurant location](Resources/Frog_Restaurant.png)

### Step 5: Finding the Flag

Look at **reviews** for the identified location. One review contains the flag.

---

## Resources

- **[Resources/twitter-frogg.png](Resources/twitter-frogg.png)** — Screenshot of the X profile with restaurant image.
- **[Resources/HA40_wzaYAAq00C.jpg](Resources/HA40_wzaYAAq00C.jpg)** — Original restaurant image from the profile.
- **[Resources/photo-site.png](Resources/photo-site.png)** — Reverse image search result / gallery reference.
- **[Resources/202405-Keep+Entrance+Clear-SMALLSQ-B0000759.webp](Resources/202405-Keep+Entrance+Clear-SMALLSQ-B0000759.webp)** — Gallery reference image.
- **[Resources/Costa coffee.png](Resources/Costa%20coffee.png)** — Costa / location on map.
- **[Resources/Frog_Restaurant.png](Resources/Frog_Restaurant.png)** — Frog restaurant location.
- **[Resources/myst3ryfr0gg3r.txt](Resources/myst3ryfr0gg3r.txt)** — Username lookup results across platforms.

---

## Flag

```
0xfun{n0t_gu3ssy_4t_4ll}
```
