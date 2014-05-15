Management commands
===================

.. highlight:: console

.. _compilejsi18n:

compilejsi18n
-------------

Collect JavaScript catalog files in a single location.

Some commonly used options are:

``-l LOCALE`` or ``--locale=LOCALE``
    The locale to process. Default is to process all.

``-p PACKAGES`` or ``-packages=PACKAGES``
    A list of packages to check for translations. Default is ``'django.conf'``.
    Use multiple times to add more.

``-o OUPUT_DIR`` or ``--output=OUTPUT_DIR``
    Output directory to store generated catalogs. Defaults to the joining path
    of :attr:`~django.conf.settings.STATICI18N_ROOT` and
    :attr:`~django.conf.settings.STATICI18N_OUTPUT_DIR`.

For a full list of options, refer to the ``compilejsi18n`` management command
help by running::

   $ python manage.py compilejsi18n --help


.. note::

    Missing directories will be created on-the-fly by the command when invoked.
