<!--
.. title: Mutual Funds Decoded - From Order to NAV
.. slug: mutual-funds-decoded-order-to-nav
.. date: 2026-10-20 12:20:55 UTC+05:30
.. tags: investing, wealth
.. category: wealth
.. link: 
.. description: 
.. type: text
-->

1. [Mutual Funds Decoded - Structure of MF](/2025/08/mutual-funds-behind-the-scenes.html)

2. [Mutual Funds Decoded - From Order to NAV](/2026/10/mutual-funds-decoded-order-to-nav.html) (you are here)

### A visit to MF office

Capital Mind Mutual Fund held [flexi cap unit holder meet](https://www.youtube.com/watch?v=L24I3z0bJI0) in the last month.
When I asked if I can visit their office and talk to the team they gladly agreed.

![mutual-funds-decoded-visit](/images/mutual-funds-decoded-visit.png)

Thanks to [Varun Mishra](https://capitalmindmf.com/team.html), Head of Operations, 
for taking time out to explain various aspects of MF process in detail.

### MF Orders

There a bunch of ways investors can buy mutual funds as shown below.

![mutual-funds-decoded-order](/images/mutual-funds-decoded-money-flow.png)

On a daily basis, Ops team will monitor all these inflows in real time, aggregate the amount and let Portfolio Manager(PM) know about the available cash.

### MF NAV

A 14 step sequence diagram showing interactions between R&D, Ops, PM, Dealers, Custodian & daily timelines on how MF orders gets converted to NAV.

![mutual-funds-decoded-money-nav](/images/mutual-funds-decoded-money-nav.png)

[Click here to see full size image](/images/mutual-funds-decoded-money-nav.png)

#### Why PM can't buy directly?

As an individual stock investor, we can buy/sell stocks directly from broker. But in case of mutual funds, the process is more complex. 

AMCs enforce a strict separation of decision making(Portfolio Management) and trade execution(Dealing Room).

- Best execution of trades: MFs deal with large volumes of trades. Dumping a single gaint market order can move the market and result in poor execution. Dealers use algorithmic strategies to break large orders into smaller ones and execute them over time to minimize market impact.
- Execution Skill: PMs value lies in company valuation, sector allocation, and risk management. They may not have the expertise to execute trades efficiently. Dealers are trained in market microstructure, order routing, and execution strategies.
- Regulatory Compliance: SEBI regulations require AMCs to have a clear separation of duties between PMs and dealers to prevent conflicts of interest and ensure fair treatment of all investors.


### Conclusion

We have seen how money flows from investors to AMCs & how it gets converted to NAV. We also learnt why PMs can't buy/sell directly and why we need dealers to execute trades.

In the next article, we will deep dive into expense ratio, how it is calculated and how it impacts investors.