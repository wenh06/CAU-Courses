# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import re
from typing import Any, Dict

import pydata_sphinx_theme
import requests
import sphinx_book_theme
import sphinx_rtd_theme
import sphinx_theme
from docutils import nodes
from sphinx.application import Sphinx

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "CAU-MathematicalAnalysis"
copyright = "2023, WEN Hao"
author = "WEN Hao"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
    "sphinx_design",
    "nbsphinx",
    # 'sphinx.ext.autosectionlabel',
    "sphinx_multiversion",
    "sphinx_favicon",
    "sphinx_emoji_favicon",
    # "numpydoc",
    "sphinxcontrib.tikz",
    # "sphinxcontrib.pseudocode",
    # "sphinxcontrib.bibtex",
    "sphinxcontrib.proof",
    "sphinxcontrib.xlsxtable",
]

# bibtex_bibfiles = ["references.bib"]
# bibtex_bibliography_header = ".. rubric:: 参考文献"
# bibtex_footbibliography_header = bibtex_bibliography_header

# intersphinx_mapping = {
#     "python": ("https://docs.python.org/3", None),
#     "numpy": ("https://numpy.org/doc/stable/", None),
# }

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "wenh06",  # Username
    "github_repo": "CAU-Courses",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/MathematicalAnalysis/source/",  # Path in the checkout to the docs root
}

proof_theorem_types = {
    "theorem": "定理",
    "conjecture": "猜想",
    "corollary": "推论",
    "definition": "定义",
    "example": "例",
    "lemma": "引理",
    "observation": "观察",
    "proof": "证明",
    "property": "性质",
    "remark": "注记",
    "solution": "解",
}

templates_path = ["_templates"]
exclude_patterns = []

language = "zh"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

_theme_name = "sphinx_book_theme"  # "pydata_sphinx_theme", "stanford_theme", etc.

if _theme_name == "stanford_theme":
    html_theme = "stanford_theme"
    html_theme_path = [sphinx_theme.get_html_theme_path("stanford-theme")]
    html_theme_options = {
        "collapse_navigation": False,
        "display_version": True,
    }
elif _theme_name == "sphinx_rtd_theme":
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme_options = {
        "collapse_navigation": False,
        "display_version": True,
    }
elif _theme_name == "sphinx_book_theme":
    html_theme = "sphinx_book_theme"
    html_theme_path = [sphinx_book_theme.get_html_theme_path()]
    html_theme_options = {
        # "repository_url": "https://github.com/wenh06/CAU-Courses",
        # "use_repository_button": True,
        # "use_issues_button": True,
        # "use_edit_page_button": True,
        "use_download_button": True,
        "use_fullscreen_button": True,
        "path_to_docs": "MathematicalAnalysis/source",
        "repository_branch": "master",
    }
elif _theme_name == "pydata_sphinx_theme":
    html_theme = "pydata_sphinx_theme"
    html_theme_path = [pydata_sphinx_theme.get_html_theme_path()]
    html_theme_options = {
        "collapse_navigation": False,
        "display_version": True,
    }
else:  # builtin themes: alabaster, etc.
    html_theme = _theme_name

html_static_path = ["_static"]
html_title = "CAU Mathematical Analysis"

# favicons = [
#     {"href": "favicon.png"},  # => use `_static/favicon.png`
# ]
emoji_favicon = ":livres:"


_mathjax_file = "tex-chtml-full.js"


def _get_mathjax_latest_version() -> str:
    """Get the latest mathjax version.

    Returns
    -------
    str
        The latest mathjax version.

    """
    defalut_mathjax_latest_version = "3.2.2"
    url = f"https://unpkg.com/mathjax@latest/es5/{_mathjax_file}"
    try:
        r = requests.get(url, timeout=3)
        if r.status_code == 200:
            # search for the version number in r.url
            # which will be redirected to the latest version with version number
            # e.g. https://unpkg.com/mathjax@3.2.2/es5/tex-chtml-full.js
            return re.search("mathjax@([\\w\\.\\-]+)", r.url).group(1)
        else:
            return defalut_mathjax_latest_version
    except Exception:
        return defalut_mathjax_latest_version


mathjax_path = f"https://cdnjs.cloudflare.com/ajax/libs/mathjax/{_get_mathjax_latest_version()}/es5/{_mathjax_file}"
# mathjax_path = f"https://cdn.bootcdn.net/ajax/libs/mathjax/{_get_mathjax_latest_version()}/es5/{_mathjax_file}"


master_doc = "index"

numfig = False

linkcheck_ignore = [
    r"https://doi.org/*",  # 418 Client Error
]


# -------------------------------------------------
# Code from https://github.com/SuperKogito/sphinxcontrib-pdfembed/blob/master/sphinxcontrib/pdfembed.py
# -------------------------------------------------


def pdfembed_html(pdfembed_specs):
    """
    Build the iframe code for the pdf file,
    """
    html_base_code = """
                        <iframe
                                id="ID"
                                style="border:1px solid #666CCC"
                                title="PDF"
                                src="%s"
                                frameborder="1"
                                scrolling="auto"
                                height="%s"
                                width="%s"
                                align="%s">
                        </iframe>
                     """
    return html_base_code % (pdfembed_specs["src"], pdfembed_specs["height"], pdfembed_specs["width"], pdfembed_specs["align"])


def pdfembed_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Get iframe specifications and generate the associate HTML code for the pdf iframe.
    """
    # parse and init variables
    text = text.replace(" ", "")
    pdfembed_specs = {}
    # read specs
    for component in text.split(","):
        pdfembed_specs[component.split(":")[0]] = component.split(":")[1]
    # build node from pdf iframe html code
    node = nodes.raw("", pdfembed_html(pdfembed_specs), format="html")
    return [node], []


# -------------------------------------------------


def html_page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: nodes.document,
) -> None:
    """Update the html page context by adding tikzjax related parameters.

    Parameters
    ----------
    app : Sphinx
        The Sphinx application.
    pagename : str
        The name of the page.
    templatename : str
        The name of the template.
    context : Dict[str, Any]
        The context of the html page.
    doctree : nodes.document
        The document tree.

    Returns
    -------
    None
        The context is updated in-place.

    """
    if "metatags" not in context:
        context["metatags"] = ""
    context["metatags"] += """<link rel="stylesheet" type="text/css" href="https://tikzjax.com/v1/fonts.css">"""
    context["metatags"] += """<script src="https://tikzjax.com/v1/tikzjax.js"></script>"""


def setup(app):
    app.add_css_file("css/custom.css")
    app.add_css_file("css/proof.css")
    app.add_role("pdfembed", pdfembed_role)
    app.connect("html-page-context", html_page_context)
