---
marp: true
theme: default
paginate: true
style: |
  section {
    font-family: Georgia, 'Times New Roman', Times, serif;
    background-color: #fff;
    color: #333;
  }
  h1, h2, h3 {
    color: #222;
    border-bottom: 1px solid #e5e5e5;
    padding-bottom: 0.2em;
  }
  section {
    justify-content: flex-start;
  }
  section h2 {
    position: absolute;
    top: 40px;
    left: 70px;
    right: 70px;
    margin: 0;
  }
  section h2 + * {
    margin-top: 70px;
  }
  a {
    color: #007bff;
  }
  section img {
    max-height: 480px;
    max-width: 100%;
    display: block;
    margin: 0 auto;
    object-fit: contain;
  }
  .side-by-side {
    display: flex;
    gap: 1rem;
    align-items: center;
    justify-content: center;
  }
  .side-by-side img {
    max-height: 420px;
    width: 48%;
  }
  .side-by-side > div {
    width: 48%;
  }
---

# Classifying Billion base-pairs/second

Chillar Anand ([avilpage.com](https://avilpage.com))

---
## Agenda

- What is meta-genomic analysis?
- Taxanomic classification tools
- Intro to Kraken2
- Speeding up Kraken2

---
## What is Meta-Genomics?

<div class="side-by-side">
<div>

Study of all organims in a community by their DNA.
Ex: Soil sample, gut microbiome, ocean water, etc.

<br />

Can a scoop of mud give you latitude/longitude?
Can we detect an outbreak in cities of before doctors?

</div>
<img src="mg.png" />
</div>

---
## Abundance Profile & Taxonomy

<div class="side-by-side">
<img src="abundance-profile.png" />
<img src="ncbi-taxanomy.jpg" />
</div>


[//]: # (## Classification Tools)

[//]: # ()
[//]: # (![]&#40;class-tools.png&#41;)

[//]: # ()
[//]: # (---)

---
## Sub-string search

![](subs.mmd.svg)

---
## Kraken2 Index

![](k2i.mmd.svg)


---
## Faster Classification

![](k2c.png)


---
## References

- https://github.com/DerrickWood/kraken2

- https://github.com/hoytech/vmtouch

- https://avilpage.com/tags/kraken2.html

- https://pmc.ncbi.nlm.nih.gov/articles/PMC6716367/
