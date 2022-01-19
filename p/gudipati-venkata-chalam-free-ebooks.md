<!--
.. title: Gudipati Venkata Chalam Free Ebooks
.. slug: gudipati-venkata-chalam-free-ebooks
.. date: 2020-12-31 18:34:03 UTC+06:30
.. tags: telugu, books
.. category:
.. link:
.. description:
.. type: text
-->


{% block content %}
    <article class="listpage">
        <header>
            <h1>{{ title|e }}</h1>
        </header>
        {{ archive_nav.archive_navigation() }}
        {{ feeds_translations.translation_link() }}
        <div class="postlist">
            {% for group in posts|groupby('date.year')|reverse %}
                <h4>{{ group.grouper }}</h4>
                {% for post in group.list %}
                    <a href="{{ post.permalink() }}" class="listtitle">{{ post.title()|e }}</a>
                    <br />
                    <time class="listdate" datetime="{{ post.formatted_date('webiso') }}" title="{{ post.formatted_date(date_format)|e }}">
                        {{ post.formatted_date(date_format) }}
                    </time>
                    {{ helper.duration(post) }}
                    <br /><br />
                {% endfor %}
            {% endfor %}
        </div>
    </article>
{% endblock %}

{% block extra_head %}
    {{ feeds_translations.head() }}
{% endblock %}
