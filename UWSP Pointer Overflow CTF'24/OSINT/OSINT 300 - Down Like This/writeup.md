## **Challenge Name: OSINT 300 - Intimidation by Ecolocation**

---

### **Description**

You ever look around at the things you see every day, and think about how what is mundane for you would be novel and interesting for others? Take the following image, for example.

![OSINT300-2.jpg](Resources/OSINT300-2.jpg)

A perfectly normal street in a perfectly mundane place for many people, but when I look at it, I see all these little details that cause it to differ from my own version of mundane. The script, the bikes left unsecured near what looks to be an ATM in broad view of the sidewalk (unlike the one next to it with a privacy screen), the format of the telephone numbers, and on and on... It looks exactly like scenes I have viewed many times, and in fact it is a place much like those places I've been. But it's those subtle differences - exotic spices on a familiar food.

The really incredible thing about living in our time is that we don't have to travel to see these things. We can go to a map and drop the little dude on the blue line and take a look around at (most) places in the world. But that's not it - we can not just see a place, but we can sometimes go back in time. See it how it was years ago.

If we went to this place, for example, we might see the comings and goings of people throughout time. Let's pay a little more attention to that. At one point, there was a white van parked on the street in front of this location. The license plate is obviously blurred, but the fax number on the back is not. That is your target. The archive below contains the flag. The password for this archive is the fax number on the back of the van parked in front of this location. Do not include spaces or special characters - just the numbers and all of the numbers you see there.

---

### **Approach**

A little reverse image lookup using Google and we find the street view.

![Image1](Resources/image1.png)


Go little closer to the shop and then you can see various versions of images avaialable.

December 2016 has a Van to it's right, with the Fax Number - 042292803

![Image2](Resources/image2.png)

Unlocked the archive with the password and get the flag.

---

### **Flag**

`poctf{uwsp_7h3_4n5w3r_70_3v3ry7h1n6}`

---