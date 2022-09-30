<!--
.. title: Mastering DICOM - #3 Setup Modality Worklist SCP
.. slug: dicom-modality-worklist-scp
.. date: 2022-07-31 18:19:29 UTC+05:30
.. tags: dicom
.. category:
.. link:
.. description:
.. type: text
-->


### Introduction

In the earlier article, we have learnt how to setup DICOM for digging deeper into DICOM protocol. In this article, let us learn how to setup a modality worklist(WML) SCP. Modalities can send C-FIND queries to this SCP and retrieve worklist information


### Using Orthanc Worklist Plugin

Orthanc server has worklist plugin[^owp] which will serve worklist files that are stored in a particular directory. Let us download sample worklist files from Orthanc repository and keep in "WorklistDatabase" directory.

Generate default configuration by running the following command.

```
$ ./Orthanc --config=config.json
```

In the orthanc configuration file, enable worklist plugin, specify the worklist database directory so that Orthanc can locate relevant worklist files, add required modalities and restart the server.

```
  "Plugins" : [
    "libModalityWorklists.dylib"
  ],

  "Worklists" : {
    "Enable": true,
    "Database": "./WorklistsDatabase",
    "FilterIssuerAet": false,
    "LimitAnswers": 0
  },

  "DicomModalities" : {
      "PYNETDICOM" : ["PYNETDICOM", "127.0.0.1", 4243],
      "FINDSCU" : ["FINDSCU", "127.0.0.1", 4244]
  }
```

Once the plugin is enabled, we can use findscu to send C-FIND query.

```
$ findscu -W -k "ScheduledProcedureStepSequence" 127.0.0.1 4242
```

This will retrieve all worklist files from the server.


### Using wlmscpfs

`dcmtk` [^dcmtk] is a collection of utilities for DICOM standard. It has `wlmscpfs` application which implements basic Service Class Provider(SCP). We can start the service by running the following command.

```
wlmscpfs --debug --data-files-path WorklistsDatabase 4242
```

Once the service is started modalities can send C-FIND query to this service.


### Conclusion

We have seen how to setup MWL SCP using Orthanc & wmlscpfs. Now that we have PACS & WML SCP up and running, in the next article lets see how to dig deeper in to the dicom standard.


[^owp]: [https://book.orthanc-server.com/plugins/worklists-plugin.html](https://book.orthanc-server.com/plugins/worklists-plugin.html)
[^dcmtk]: [https://github.com/DCMTK/dcmtk](https://github.com/DCMTK/dcmtk)