# pylint: disable=C0111,R0902,R0904,R0912,R0913,R0915,E1101
# Smartsheet Python SDK.
#
# Copyright 2016 Smartsheet.com, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import absolute_import

from ..types import TypedList
from ..util import prep
from datetime import datetime
import json
import logging
import six

class CopyOrMoveRowDestination(object):

    """Smartsheet CopyOrMoveRowDestination data model."""

    def __init__(self, props=None, base_obj=None):
        """Initialize the CopyOrMoveRowDestination model."""
        self._base = None
        if base_obj is not None:
            self._base = base_obj
        self._pre_request_filter = None
        self._log = logging.getLogger(__name__)
        self._log.info('initializing CopyOrMoveRowDestination (%s)',
                          __name__)

        self._sheet_id = None

        if props:
            # account for alternate variable names from raw API response
            if 'sheetId' in props:
                self.sheet_id = props['sheetId']
            if 'sheet_id' in props:
                self.sheet_id = props['sheet_id']

    @property
    def sheet_id(self):
        return self._sheet_id

    @sheet_id.setter
    def sheet_id(self, value):
        if isinstance(value, int):
            self._sheet_id = value

    def to_dict(self, op_id=None, method=None):
        obj = {
            'sheetId': prep(self._sheet_id)}
        return obj

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)

    def __str__(self):
        return json.dumps(self.to_dict())