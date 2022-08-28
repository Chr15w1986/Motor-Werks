<h1 align=center>Testing</h1>

#
## **Validation and accessibility**

### **Lighthouse report**
<details>
  <summary>Reports</summary>
  
  All pages of the app were tested using the lighthouse function built in to the Google Chrome browser on incognito mode.
  
  <img width="400" src="static/assets/images/TESTING-images/homepageLighthouse.png"><br>
  <img width="400" src="static/assets/images/TESTING-images/loginLighthouse.png"><br>
  <img width="400" src="static/assets/images/TESTING-images/signupLighthouse.png"><br>
  <img width="400" src="static/assets/images/TESTING-images/servicespageLighthouse.png"><br>
  <img width="400" src="static/assets/images/TESTING-images/servicedetailpageLighthouse.png"><br>
  <img width="400" src="static/assets/images/TESTING-images/profilepageLighthouse.png"><br>
  <img width="400" src="static/assets/images/TESTING-images/signuplinkissueLighthouse.png"><br>
 
  
  The low best practices score on `Home` with 83, is due to the main image aspect ratio<br>
  The low best SEO score on `Signup` with 89, is due to the link text no being descriptive, but it simply says `here`
  

</details>
  
### **WAVE Webaim Accessibility testing**
<details>
  <summary>Reports</summary>

  ### **Accessibility report**
  The WAVE tool was used to test all pages on the app.<br>
  Some errors repeat over each page tested, these were due to the social links not having text as they are fontawesome links.<br>
  I also received some contrast errors on some of the pages. This is due to the green text on purple background.<br>
  I did receive an error for alt text on the main image as `'suspicious'`, <br>I changed it from 'image of an audi r8 in the dark'
  to 'Audi R8 in the dark', it liked that.<br>
  - Links to the individual results:  
    
    
  * [link to home page WAVE result](https://wave.webaim.org/report#/https://motor-werks.herokuapp.com/)  
  * [link to login page WAVE result](https://wave.webaim.org/report#/https://motor-werks.herokuapp.com/accounts/login/)  
  * [link to signup page WAVE result](https://wave.webaim.org/report#/https://motor-werks.herokuapp.com/accounts/signup/)  
  * [link to services page WAVE result](https://wave.webaim.org/report#/https://motor-werks.herokuapp.com/services/)  
  * [link to service-detail page WAVE result](https://wave.webaim.org/report#/https://motor-werks.herokuapp.com/services/services_detail/4/)

  There were 2 parts of the site that were inaccesible and due to this I was unable to check them with the tool.
  * These were:
    - Payments page, Internal server error
    - User profile page, User must be signed in, WAVE wouldn't allow me to sign in
    
</details>

  ### **CSS Validation**
  <details>
  <summary>CSS Validator results</summary>

  * Only the custom CSS file was tested (style.css)<br>
    - If I test the entire site url, all of the bootstrap styles are also tested but still pass.<br>
  <img width="600" src="static/assets/images/TESTING-images/cssvalidation.png">
  
  </details>
  
 ### **HTML Validation**  
  <details>
  <summary>HTML Validator results</summary>

  * All HTML was passed through the validator retreived from the source code within devtools on Chrome.<br>
    - Three minor warnings remain:
        - Mailchimp javascript 
        - Amazon Javascript
        - Section heading requires h2-h6 element

  * [link to w3c validator result](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmotor-werks.herokuapp.com%2F)
  
  </details>
  
 ### **Python Validation (PEP8)**
  <details>
  <summary>PEP8 Validator results</summary>

###  **Motor-werks App**

<p float="left">
        <img src="static/assets/images/TESTING-images/PEP8-images/motorwerks-asgi-pep8.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/motorwerks-settings-pep8.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/motorwerks-wsgi-pep8.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/motorwerks-views-pep8.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/motorwerks-urls-pep8.png" width="300" height="300"/>
</p>

All files for Motor-werks passed through PEP8 without errors

###  **Home App**

<p float="left">
        <img src="static/assets/images/TESTING-images/PEP8-images/home-views.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/home-urls.png" width="300" height="300"/>
</p>

All files for home app passed through PEP8 without errors

### **Payments App**

<p float="left">
        <img src="static/assets/images/TESTING-images/PEP8-images/payments-urls-pep8.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/payments-views-pep8.png" width="300" height="300"/>
</p>

All files for Payments app passed through PEP8 without errors

### **Profiles App**

<p float="left">
        <img src="static/assets/images/TESTING-images/PEP8-images/profiles-admin-pep8.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/profiles-apps-pep8.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/profiles-forms-pep8.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/profiles-models-pep8.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/profiles-urls-pep8.png" width="300" height="300"/>
        <img src="static/assets/images/TESTING-images/PEP8-images/profiles-views-pep8.png" width="300" height="300"/>
</p>

All files for Profiles app passed through PEP8 without errors



## **Manual Testing**

<!-- TO DO -->