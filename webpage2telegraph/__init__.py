#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import export_to_telegraph

export_to_telegraph.name = 'webpage2telegraph'


def clear_url(url):
    return url


export_to_telegraph.clear_url = clear_url


def transfer(url, throw_exception=False, source=False, simplify=False, force_cache=False, no_auto_convert=False):
    return export_to_telegraph.export(url,
                                      throw_exception=throw_exception,
                                      noSourceLink=not source,
                                      toSimplified=simplify,
                                      force=force_cache,
                                      noAutoConvert=no_auto_convert
                                      )
