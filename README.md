Drunken Sailor
==============

A simple web application to help you navigate through your [Drunken Debuggers](https://github.com/DrunkenDebuggers/DrunkenDebuggers) mini-projects.

Use with caution, this is a highly experimental version!

INSTALL
-------

* See: http://www.djangobook.com/en/2.0/chapter12.html
* Copy and edit settings.py.example, set up your SECRET\_KEY properly!
* Create aliases for the static directories and unset their handler:

```
<Location /static>
    SetHandler None
</Location>

<Location /static/admin>
    SetHandler None
</Location>
`
```

TODO
----

* Fixtures for default user groups (Project and Label add only)
* Team support
  * Let people/teams associate with projects ("X team is working on project Y")
* Proper design
* Testing, testing, testing

