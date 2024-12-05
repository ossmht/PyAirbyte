"""A Databricks implementation of the PyAirbyte cache.

## Usage Example

```python
from airbyte as ab
from airbyte_.caches import DatabricksCache

cache = DatabricksCache(
    access_token = ab.get_secret("databricks_access_token"),
    server_hostname = ab.get_secret("databricks_server_hostname"),
    http_path= ab.get_secret("databricks_http_path"),
    catalog = ab.get_secret("databricks_catalog"),
    schema_name = ab.get_secret("databricks_target_schema")
)
```
"""

from __future__ import annotations

from pydantic import PrivateAttr

from airbyte_._processors.sql.databricks import DatabricksConfig, DatabricksSqlProcessor
from airbyte.caches.base import CacheBase

class DatabricksCache(DatabricksConfig, CacheBase):
    _sql_processor_class = PrivateAttr(default=DatabricksSqlProcessor)
    

__all__ = [
    "DatabricksCache",
    "DatabricksConfig",
]    