<!--
.. title: Verifying TLS Certificate Chain With OpenSSL
.. slug: verify-tls-certificate-chain-with-openssl
.. date: 2019-11-30 10:15:14 UTC+05:30
.. tags: command-line
.. category: programming
.. link:
.. description: How to verify certificate chain with openssl on the command line in linux or mac?
.. type: text
-->

### Introduction

To communicate securely over the internet, HTTPS (HTTP over TLS) is used. A key component of HTTPS is Certificate authority (CA), which by issuing digital certificates acts as a trusted 3rd party between server(eg: google.com) and others(eg: mobiles, laptops).

In this article, we will learn how to obtain certificates from a server and manually verify them on a laptop to establish a chain of trust.


### Chain of Trust

TLS certificate chain typically consists of server certificate which is signed by intermediate certificate of CA which is inturn signed with CA root certificate.

Using OpenSSL, we can gather the server and intermediate certificates sent by a server using the following command.

```bash
$ openssl s_client -showcerts -connect avilpage.com:443

CONNECTED(00000006)
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert High Assurance EV Root CA
verify return:1
depth=1 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert SHA2 High Assurance Server CA
verify return:1
depth=0 C = US, ST = California, L = San Francisco, O = "GitHub, Inc.", CN = www.github.com
verify return:1
---
Certificate chain
 0 s:/C=US/ST=California/L=San Francisco/O=GitHub, Inc./CN=www.github.com
   i:/C=US/O=DigiCert Inc/OU=www.digicert.com/CN=DigiCert SHA2 High Assurance Server CA
-----BEGIN CERTIFICATE-----
MIIHMTCCBhmgAwIBAgIQDf56dauo4GsS0tOc8
MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlna
0wGjIChBWUMo0oHjqvbsezt3tkBigAVBRQHvF
aTrrJ67dru040my
-----END CERTIFICATE-----
 1 s:/C=US/O=DigiCert Inc/OU=www.digicert.com/CN=DigiCert SHA2 High Assurance Server CA
   i:/C=US/O=DigiCert Inc/OU=www.digicert.com/CN=DigiCert High Assurance EV Root CA
-----BEGIN CERTIFICATE-----
MIIEsTCCA5mgAwIBAgIQBOHnpNxc8vNtwCtC
MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGln
0wGjIChBWUMo0oHjqvbsezt3tkBigAVBRQHv
cPUeybQ=
-----END CERTIFICATE-----

    Verify return code: 0 (ok)
```

This command internally verfies if the certificate chain is valid. The output contains the server certificate and the intermediate certificate along with their issuer and subject. Copy both the certificates into `server.pem` and `intermediate.pem` files.

We can decode these pem files and see the information in these certificates using

```sh
$ openssl x509 -noout -text -in server.crt

Certificate:
    Data:
        Version: 3 (0x2)
    Signature Algorithm: sha256WithRSAEncryption
    ----
```

We can also get only the subject and issuer of the certificate with

```sh
$ openssl x509 -noout -subject -noout -issuer -in server.pem

subject= CN=www.github.com
issuer= CN=DigiCert SHA2 High Assurance Server CA

$ openssl x509 -noout -subject -noout -issuer -in intermediate.pem

subject= CN=DigiCert SHA2 High Assurance Server CA
issuer= CN=DigiCert High Assurance EV Root CA
```

Now that we have both server and intermediate certificates at hand, we need to look for the relevant root certificate (in this case DigiCert High Assurance EV Root CA) in our system to verify these.

If you are using a Linux machine, all the root certificate will readily available in `.pem` format in `/etc/ssl/certs` directory.

If you are using a Mac, open `Keychain Access`, search and export the relevant root certificate in `.pem` format.

<p algin="center">
<img src="/images/tls-openssl1.png" />
</p>

We have all the 3 certificates in the chain of trust and we can validate them with

```bash
$ openssl verify -verbose -CAfile root.pem -untrusted intermediate.pem server.pem
server.pem: OK
```

If there is some issue with validation OpenSSL will throw an error with relevant information.

### Conclusion

In this article, we learnt how to get certificates from the server and validate them with the root certificate using OpenSSL.
