<!--
.. title: Switching Hosts With Bookmarklets - Web Development Tips
.. slug: environment-bookmarklet-web-development-tips
.. date: 2019-05-08 21:10:52 UTC+05:30
.. tags: javascript, browser
.. category: tech, programming
.. link:
.. description: How to change enviroments (local, dev, qa, staging, production) on browser with bookmarklets.
.. type: text
-->

When debugging an issue related to web development projects, which is inconsistent between environments (local, development, QA, staging and production), we have to frequently switch between them.

If we are debugging something on the home page, then we can just bookmark the host URLs. We can switch between them by clicking on the relevant bookmark. Some browsers provide autocompletion for bookmarks. So we can type a few characters and then select the relevant URL from suggestions.

When debugging an issue on some other page like [https://avilpage.com/validate/books/?name=darwin&year=2019](), which has URL path and query param, switching between enviroment becomes tedious. To switch to local environment, we have to manually replace the hostname with localhost.

To avoid this, we can use a bookmarklet to switch the hosts. A [bookmarklet][bookmarklet] is a bookmark which contains a JavaScript code snippet in its URL. This code snippet will be executed when the bookmarklet is clicked.

Lets create a bookmarklet to replace host in the URL with [http://localhost:8000](http://localhost:8000). Create new bookmark called `To Local` and in the URL add the following snippet.

```js
javascript:(function() { window.location.replace("http://localhost:8000" + window.location.pathname + window.location.search); }())
```

If we click on `To Local` bookmarklet, it will redirect the current active page to localhost URL.

We can create one more bookmarklet to switch to production. Create a bookmarklet called `To Production` and add the following snippet in the URL.

```js
javascript:(function() { window.location.replace("http://avilpage.com" + window.location.pathname + window.location.search); }())
```

We can create similar bookmarklets to switch to other enviroments. Now, switching between enviroments on any page is as easy as clicking a button.



[bookmarklet]: https://en.wikipedia.org/wiki/Bookmarklet
