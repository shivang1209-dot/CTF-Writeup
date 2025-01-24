### **Challenge Name: DF 300 - Daily Doses**

---

### **Description**

You know what I find most frustrating about digital forensic work? The attention to detail. It never fails that I look over a piece of evidence again and again and still somehow miss something. Well, this challenge is more of a test of your powers of detection than your technical acumen. Still, this is exactly the kind of thing I've missed over and over again. Most people miss the forest for the trees. Some people miss the trees for the forest.

#### **File Provided**  
- [DF300-2.pcap](Resources/DF300-2.pcap)

---

### **Approach**

#### **Step 1: Open the PCAP File**
Opened the `DF300-2.pcap` file in **Wireshark** for analysis.

#### **Step 2: Inspect GET Requests**
Scanned through the HTTP GET requests and identified a request to `travel.changsha.cn`.

Endpoints observed:  
- `/images_2014/css.css`  
- `/h/8701/20150716/2288227.html`

Attempted visiting these URLs but found no useful information. The website returned a 404 error, and **Wayback Machine** showed no relevant entries after 2017.

#### **Step 3: Extract Strings**
To dig deeper, used the `strings` command in the terminal to extract plain text from the PCAP file:

```bash
strings DF300-2.pcap > output.txt
```

#### **Step 4: Anomaly in User-Agent Header**
While inspecting `output.txt`, noticed a suspicious User-Agent string:

```
User-Agent: Mozilla/5.0 (706F6374667B757773705F315F346D5F6C3336336E647D) (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36
```

The string `706F6374667B757773705F315F346D5F6C3336336E647D` looked like hexadecimal data.

#### **Step 5: Decode Hexadecimal String**
Decoded the hexadecimal string using **CyberChef**:

Input: `706F6374667B757773705F315F346D5F6C3336336E647D`  
Recipe: "From Hex"  

Output:  
`poctf{uwsp_1_4m_l363nd}`

---

### **Flag**

`poctf{uwsp_1_4m_l363nd}`

---