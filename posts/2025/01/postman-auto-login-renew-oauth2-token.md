<!--
.. title: Postman - Auto Login & Renew OAuth2 Token
.. slug: postman-auto-login-renew-oauth2-token
.. date: 2025-01-31 22:50:17 UTC+05:30
.. tags: postman, automation
.. category: automation
.. link: 
.. description: How to automate login & renewal of JWT token in OAuth2 using Postman
.. type: text
-->

### Introduction

When using Postman to interact with APIs behind an OAuth2 authentication, we need to login and renew the token manually. This can be automated using the following steps.

- Set credentials in environment variables
- Create a pre-request script to login and renew the token
- Use the token in the request headers

### Automating Login & Renewal

```javascript
var e = pm.environment;
var isSessionExpired = true;

var loginTimestamp = e.get("loginTimestamp");
var expiresInSeconds = pm.environment.get("expiresInSeconds") || 86400;

if (loginTimestamp) {
  var loginDuration = Date.now() - loginTimestamp;
  isSessionExpired = loginDuration >= expiresInSeconds;
}

if (isSessionExpired) {
  pm.sendRequest({
    url: e.get('host') + "/auth/connect/token",
    method: 'POST',
    header: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': 'application/json'
    },
    body: {
        mode: 'urlencoded',
        urlencoded: [
          { key: "username", value: e.get('username') },
          { key: "password", value: e.get('password') },
          { key: "grant_type", value: "password" },
          { key: "client_id", value: e.get("client_id") }
        ]
    }
  }, function (err, res) {
    jsonData = res.json();
    
    e.set("access_token", jsonData.access_token);

    if(res.json().expires_in){
        expiresInSeconds = res.json().expires_in * 1000;
    }
    e.set("expiresInSeconds", expiresInSeconds);
    e.set("loginTimestamp", Date.now())
  });
}
```

We can copy this script to the pre-request script of the collection. 

![Cockpit](/images/postman-auto-login.png)


Most of the script is self-explanatory. The script checks if the session is expired and sends a request to the token endpoint to get a new token. The token is stored in environment variables and used in the request headers.


### Conclusion

This is a one time setup for Postman collection and it saves a lot of time in the long run. The script can be modified to handle different grant types and token renewal strategies.
