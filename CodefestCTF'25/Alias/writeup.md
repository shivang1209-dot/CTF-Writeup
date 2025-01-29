# Challenge Name: Alias

## Description  
**Background Check**  
You have been asked by Sprinklr to do a background check on an intern candidate. The candidate's name is Arnav Kumar Sinha from IIT(BHU), Varanasi, India.  

**Objective**  
The candidate's known to use a certain 5-digit username on many online platforms. Find that username.  

**Flag Format**  
`CodefestCTF{username}`  

## Writeup

### Investigation Steps
1. Located candidate's LinkedIn profile:  
   `linkedin.com/in/iedfa`
2. Identified unique 5-character pattern in profile URL path

### Key Finding
Profile URL contains username: **`iedfa`**

## Flag
`CodefestCTF{iedfa}`