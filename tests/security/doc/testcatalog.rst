Test catalog
============
Test name: postgresql_ssl_client

`source <https://github.com/os-autoinst/os-autoinst-distri-opensuse/tree/master/tests/security/postgresql_ssl/postgresql_ssl_client.pm>`_

 .. warning::
    This is to test a warning text0

 Test steps:
    * install runtime dependencies (iputils)
    * determine client ip
    * install postgresql
    * restart postgres
    * setup mutex to wait for server
    * connect to postgresql server

 .. NOTE::
    This is the server-side of a multimachine test
Test name: postgresql_ssl_server

`source <https://github.com/os-autoinst/os-autoinst-distri-opensuse/tree/master/tests/security/postgresql_ssl/postgresql_ssl_server.pm>`_

 Maintainer: QE Security <none@suse.de>
 Tags: poo#110233, tc#1769967, poo#112094

 Test steps:
    * stop firewalld
    * install postgres
    * setup ssl key
    * setup password for postgres
    * setup configuration, inc. ssl certificate
    * restart postgres
    * check postgres status
    * setup mutex to wait for client
    * after test is done, stop postgres

 .. NOTE::
    This is the server-side of a multimachine test
