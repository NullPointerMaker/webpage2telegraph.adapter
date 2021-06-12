#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import export_to_telegraph

export_to_telegraph.name = 'webpage2telegraph'


def clear_url(url):
    """
    This function was originally used to remove useless parameters in the link.
    But I think the original code is too rough:
    Filter all URLs by default.
    For security reasons, I will not show the source links by default.
    If we want to filter the parameters, then we need to filter for each website.
    :param url: URL
    :return: URL
    """
    return url


export_to_telegraph.clearUrl = clear_url


def get_author_field(author, noSourceLink):
    if author =='Source':
        if noSourceLink:
            return ''
        return '原文'
    return author


export_to_telegraph.getAuthorField = get_author_field


def transfer(url, throw_exception=True, source=False, simplify=False):
    return export_to_telegraph.export(url,
                                      force=True,
                                      throw_exception=throw_exception,
                                      noSourceLink=not source,
                                      toSimplified=simplify
                                      )
