# fastapi-jinja-utils


## Installation
```pip install fastapi-jinja-utils```

## Usage

```
from fastapi_jinja_utils import Jinja2TemplatesDependency

 
jinja = Jinja2TemplatesDependency("/templates")

@app.get("/")
def my_view(..., render: JinjaTemplatesDependency = Depends(jinja)):
    ...
    return render("my_template.html.jinja2", context={"name": name})
```
```