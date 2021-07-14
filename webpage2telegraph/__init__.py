#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

import export_to_telegraph
from export_to_telegraph import getArticle
from html_telegraph_poster.utils import DocumentPreprocessor

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
    if author == 'Source':
        if noSourceLink:
            return ''
        return '原文'
    return author


export_to_telegraph.getAuthorField = get_author_field


def get_article(url, throw_exception=False, toSimplified=False, force_cache=False, noAutoConvert=False):
    article = getArticle(url,
                         throw_exception=throw_exception,
                         toSimplified=toSimplified,
                         force_cache=force_cache,
                         noAutoConvert=noAutoConvert)
    if throw_exception and article.text and article.text.text and re.match(r'HTTP \d{3}', str(article.text.text)):
        raise IOError(str(article.text.text))
    return article


export_to_telegraph.getArticle = get_article


export_to_telegraph.TelegraphPoster.post_origin = export_to_telegraph.TelegraphPoster.post


# noinspection PyBroadException
def _post(self, title, author, text, author_url):
    try:
        dp = DocumentPreprocessor(text)
        dp.upload_all_images()
        text = dp.get_processed_html()
    except:
        pass
    return self.post_origin(title, author, text, author_url)


export_to_telegraph.TelegraphPoster.post = _post


def transfer(url, throw_exception=True, source=False, simplify=False):
    return export_to_telegraph.export(url,
                                      force=True,
                                      throw_exception=throw_exception,
                                      noSourceLink=not source,
                                      toSimplified=simplify
                                      )
