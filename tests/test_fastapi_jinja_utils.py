import unittest
from typing import Callable
from unittest.mock import Mock

import fastapi
import jinja2
from fastapi.testclient import TestClient

from fastapi_jinja_utils import Jinja2TemplatesDependency, Renderable


class TestJinja2TemplatesDependency(unittest.TestCase):
    def test_callable(self):
        jinja = Jinja2TemplatesDependency("templates", env_globals={"APP_NAME": "My App"})
        self.assertEqual(jinja.templates.env.globals["APP_NAME"], "My App")
        request = Mock()
        self.assertIsInstance(jinja(request), Callable)

    def test_dep(self):
        app = fastapi.FastAPI()
        jinja = Jinja2TemplatesDependency("templates", env_globals={"APP_NAME": "My App"})
        @app.get("/")
        def index(render: Renderable = fastapi.Depends(jinja)):
            with self.assertRaises(jinja2.exceptions.TemplateNotFound):
                render("index.html", {})
            return {}
        client = TestClient(app)
        response = client.get("/")
