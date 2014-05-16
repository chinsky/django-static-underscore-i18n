import io
import os
import pytest

from django.core import management
from django.template import loader, Context
from django.utils import six


@pytest.mark.usefixtures("cleandir")
def test_compile_all(settings):
    out = six.StringIO()
    management.call_command('compilejsunderscorei18n', verbosity=1, stdout=out)
    out.seek(0)
    lines = [l.strip() for l in out.readlines()]
    assert len(lines) == 2
    assert lines[0] == "processing language en"
    assert lines[1] == "processing language fr"
    assert os.path.exists(os.path.join(
        settings.STATIC_ROOT, "jsi18n", "en", "djangojs.js"))
    filename = os.path.join(
        settings.STATICI_UNDERSCORE_18N_ROOT, "jsi18n", "fr", "djangojs.js")
    assert os.path.exists(filename)
    with io.open(filename, "r", encoding="utf-8") as fp:
        content = fp.read()
        assert "django.catalog" in content
        assert '"Hello world!": "Bonjour \\u00e0 tous !"' in content


@pytest.mark.usefixtures("cleandir")
def test_compile_locale_not_exists(settings):
    out = six.StringIO()
    management.call_command('compilejsunderscorei18n', locale='ar', verbosity=1, stderr=out)
    assert out.getvalue() == ""
