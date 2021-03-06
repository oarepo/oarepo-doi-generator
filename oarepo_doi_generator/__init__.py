# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CIS theses repository is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Record serializers."""

from .ext import OARepoDOIGenerator
from .version import __version__

__all__ = ('__version__', 'OARepoDOIGenerator',)
