# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
"""Base module for all caches."""

from __future__ import annotations

############## HACKS ################
#
## HACK
# put kwargs.next_page_token.next_page_token into self.config.next_page_token. read more in comments below/
#

from airbyte_cdk.sources.declarative.requesters.request_options.interpolated_nested_request_input_provider import InterpolatedNestedRequestInputProvider
def hacked_eval_request_inputs(self, stream_state, stream_slice, next_page_token) :
    kwargs = {
            "stream_state": stream_state,
            "stream_slice": stream_slice,
            "next_page_token": next_page_token,
        }
    ##  
    # HACK is this: put kwargs.next_page_token.next_page_token into self.config.next_page_token, so it can be referenced as config.next_page_token
    # this solves: https://github.com/airbytehq/airbyte/issues/40697 for now
    ##
    self.config['next_page_token'] = kwargs.get('next_page_token').get('next_page_token') if kwargs.get('next_page_token') else None
    return self._interpolator.eval(self.config, **kwargs)

InterpolatedNestedRequestInputProvider.eval_request_inputs = hacked_eval_request_inputs

## end of HACK

from airbyte.caches import base, bigquery, duckdb, motherduck, postgres, snowflake, databricks, util
from airbyte.caches.base import CacheBase
from airbyte.caches.bigquery import BigQueryCache
from airbyte.caches.duckdb import DuckDBCache
from airbyte.caches.motherduck import MotherDuckCache
from airbyte.caches.postgres import PostgresCache
from airbyte.caches.snowflake import SnowflakeCache
from airbyte.caches.databricks import DatabricksCache
from airbyte.caches.util import get_default_cache, new_local_cache


# We export these classes for easy access: `airbyte.caches...`
__all__ = [
    # Factories
    "get_default_cache",
    "new_local_cache",
    # Classes
    "BigQueryCache",
    "CacheBase",
    "DuckDBCache",
    "MotherDuckCache",
    "PostgresCache",
    "SnowflakeCache",
    "DatabricksCache"
    # Submodules,
    "util",
    "bigquery",
    "duckdb",
    "motherduck",
    "postgres",
    "snowflake",
    "databricks"
    "base",
]
