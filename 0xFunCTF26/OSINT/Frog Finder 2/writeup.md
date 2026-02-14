# Challenge Name: Frog Finder 2

## Description

A frog has escaped from the prison cells of a cybersecurity club and is on the run. Somehow, they've gained the ability to roam the internet and gain human intellect. Their newest adventures are documented online—you need to track them down. The handle is likely along the lines of **@myst3ryfr0gg3r**.

You will find the flag already in the format `0xfun{...}`.

---

## Writeup

### Step 1: Username Lookup

Use [whatsmyname.app](https://whatsmyname.app/) or similar to search for **myst3ryfr0gg3r**. This leads to an X (Twitter) profile:

```
https://x.com/myst3ryfr0gg3r
```

### Step 2: Finding the GeoOSINT Image

Scroll through the profile. The user posts an image of a restaurant and hints at geoOSINT (e.g. a filename like `@HA40_wza......jpg`).

![Restaurant image from X profile](Resources/image1.png)

### Step 3: Reverse Image Search

Save the image and run a **reverse image search**. One result points to a photo gallery (e.g. [alorenz.photography/gallery](https://www.alorenz.photography/gallery)) and an image such as `@202405-Keep.....webp`.

![Reverse image search result](Resources/image2.png)

Searching further with the same image leads to a post such as:

`https://x.com/PetrocTrelawny/status/1176972688700661762`

This indicates the location is **The Strand, London**, and mentions a café name—**Costa**.

### Step 4: Locating the Café

Search for "Costa" and "The Strand" (e.g. Google Maps) to find the exact spot.

![Costa location on map](Resources/image3.png)

Example:  
`https://www.google.com/maps/place/Costa/...`

From the original image, the name **Eve** appears. Searching "Eve Bar, The Strand" gives the precise location (e.g. coordinates, Street View). You can also find **Frog** names restaurant there.

![Eve Bar / Frog location](Resources/image4.png)

### Step 5: Finding the Flag

Look at **reviews** for the identified location (e.g. Frog or the specific venue). One review or linked page contains the flag.

Example review link: `https://maps.app.goo.gl/kyBQo11sq7K8oAzQ8`

---

## Resources

- **Resources/image1.png** — Restaurant image from the X profile.
- **Resources/image2.png** — Reverse image search result / gallery reference.
- **Resources/image3.png** — Costa / location on map.
- **Resources/image4.png** — Eve Bar / Frog restaurant location.

*(Add your own screenshots to the `Resources` folder and keep the filenames above for the links to work.)*

---

## Flag

```
0xfun{n0t_gu3ssy_4t_4ll}
```

---
