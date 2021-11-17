Steps to reproduce


```python
python -m venv /tmp/venv
source /tmp/venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt


mypy --config-file=pyproject.toml . --show-traceback
```



```
mypy --config-file=pyproject.toml . --show-traceback
./stubissue/fake_issue.py:9: error: INTERNAL ERROR -- Please try using mypy master on Github:
https://mypy.readthedocs.io/en/stable/common_issues.html#using-a-development-mypy-build
Please report a bug at https://github.com/python/mypy/issues
version: 0.910
Traceback (most recent call last):
  File "mypy/checkexpr.py", line 3911, in accept
  File "mypy/nodes.py", line 1558, in accept
  File "mypy/checkexpr.py", line 271, in visit_call_expr
  File "mypy/checkexpr.py", line 353, in visit_call_expr_inner
  File "mypy/checkexpr.py", line 858, in check_call_expr_with_callee_type
  File "mypy/checkexpr.py", line 917, in check_call
  File "mypy/checkexpr.py", line 1029, in check_callable_call
  File "mypy/checkexpr.py", line 738, in apply_function_plugin
  File "/Users/sidmitra/Library/Caches/pypoetry/virtualenvs/django-stubs-annotate-issue-kUmubfCn-py3.9/lib/python3.9/site-packages/mypy_django_plugin/transformers/querysets.py", line 231, in extract_proper_type_queryset_annotate
    annotated_type = get_or_create_annotated_type(api, model_type, fields_dict=fields_dict)
  File "/Users/sidmitra/Library/Caches/pypoetry/virtualenvs/django-stubs-annotate-issue-kUmubfCn-py3.9/lib/python3.9/site-packages/mypy_django_plugin/transformers/models.py", line 447, in get_or_create_annotated_type
    model_module_file = api.modules[model_module_name]  # type: ignore
KeyError: 'django_stubs_ext'
./stubissue/fake_issue.py:9: : note: use --pdb to drop into pdb
```
