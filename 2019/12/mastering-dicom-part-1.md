<!--
.. title: Mastering DICOM - Part #1
.. slug: mastering-dicom-part-1
.. date: 2019-12-31 18:59:09 UTC+05:30
.. tags: python, health-care
.. category:
.. link:
.. description: How to query and retrieve DICOM files store in a remote PACS using c-find command with Python.
.. type: text
-->


### Introduction

In hospitals, [PACS][pacs] simplifies the clinical workflow by reducing physical and time barriers. A typical radiology workflow looks like this.

<p algin="center">
<img src="/images/dicom-pacs-python1.png" />
</p>

<p>Credit: <cite>Wikipedia</cite></p>

A patient as per doctor's request will visit a radiology center to undergo CT/MRI/X-RAY. Data captured from modality(medical imaging equipments like CT/MRI machine) will be sent to QA for verfication and then sent to PACS for archiving.

After this when patient visits doctor, doctor can see this study on his workstation(which has DICOM viewer) by entering patient details.

In this series of articles, we will how to achieve this seamless transfer of medical data digitally with DICOM.


### DICOM standard

DICOM modalities create files in DICOM format. This file has dicom header which contains meta data and dicom data set which has modality info(equipment information, equipment configuration etc), patient information(name, sex etc) and the image data.

Storing and retreiving DICOM files from PACS servers is generally achieved through DIMSE DICOM for desktop applications and DICOMWeb for web applications.

All the machines which transfer/receive DICOM data must follow DICOM standard. With this all the DICOM machines which are in a network can store and retrieve DICOM files from PACS.

When writing software to handle DICOM data, there are third party packages to handle most of the these things for us.

 - Python([pydicom](https://pypi.org/project/pydicom/), [pynetdicom](https://pypi.org/project/pynetdicom/))

- Ruby ([ruby-dicom](https://rubygems.org/gems/dicom/))

- R ([oro.dicom](https://CRAN.R-project.org/package=oro.dicom))

- C/C++ ([dcmtoolkit](https://dicom.offis.de/dcmtk))


### Conclusion

In this article, we have learnt the clinical radiology workflow and how DICOM standard is useful in digitally transferring data between DICOM modalities.

In the next article, we will dig into DICOM file formats and learn about the structure of DICOM data.

[pacs]: https://en.wikipedia.org/wiki/Picture_archiving_and_communication_system
