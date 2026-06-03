<!--
 .. title: Mango Health - Privacy Policy
 .. slug: Mango-Health-Privacy-Policy
 .. date: 2026-06-02 11:16:41 UTC+05:30
 .. tags: 
 .. category: meta
 .. link:
 .. description: Mango Health - Privacy Policy
 .. type: text
-->


# Mango Health - Privacy Policy

**App Name:** Mango Health  
**Last Updated:** June 2, 2026  
**Developer:** AvilPage

---

## Overview

Mango Health is a personal health companion app that helps you track daily steps, earn rewards, and store medical documents securely. Your privacy is a core design principle — **all data stays on your device by default**.

---

## Data We Collect

### Health Data
- **Step count** — read from Android Health Connect or Apple HealthKit (read-only). This data is stored locally on your device.
- We do **not** write to or modify your health data.

### Medical Documents
- Photos and documents you capture or import are stored locally in an on-device SQLite database as encrypted blobs.
- We do **not** upload or share your medical documents with any third party.

### Optional Cloud Sync (PocketBase)
If you choose to configure a self-hosted PocketBase server:
- Your step data and reward points may be synced to **your own server**.
- User account credentials (email/password) are used to authenticate with **your PocketBase instance**.
- We have no access to your self-hosted server or the data on it.

---

## Data We Do NOT Collect

- We do **not** collect any personally identifiable information (PII) by default.
- We do **not** use third-party analytics, advertising SDKs, or crash reporting services.
- We do **not** sell, rent, or share your data with any third party.
- We do **not** track your location.

---

## Permissions

| Permission | Purpose |
|---|---|
| `READ_STEPS` (Health Connect) | Read your daily step count to track activity |
| `READ_EXTERNAL_STORAGE` / `MANAGE_MEDIA` | Import existing images from your gallery |

All permissions are requested at runtime and can be revoked at any time from your device settings.

---

## Data Storage & Security

- All app data is stored locally on your device using SQLite.
- No data is transmitted to external servers unless you explicitly configure optional cloud sync.
- Uninstalling the app removes all locally stored data.

---

## Children's Privacy

Mango Health is not directed at children under 13. We do not knowingly collect data from children.

---

## Changes to This Policy

We may update this policy from time to time. Continued use of the app after changes constitutes acceptance of the updated policy. The "Last Updated" date at the top reflects the most recent revision.

---

## Contact

If you have questions or concerns about this privacy policy, please contact us:

**Email:** support@avilpage.com  
**Website:** https://avilpage.com
