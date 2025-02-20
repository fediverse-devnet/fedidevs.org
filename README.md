# Fedidevs.org

This is the content of [fedidevs.org](https://fedidevs.org/).

It is built with the [Hugo](https://gohugo.io/) static site generator, plus some Python scripts that generate a few of the pages.

Contributions welcome; file a pull request.

## Software requirements

Install Git and Git-LFS, and initialize it:

```shell
$ brew install git
$ brew install git-lfs
$ git lfs install
```

Install Hugo, e.g. on macOS:

```shell
$ brew install hugo
```

## To run the website locally

Get the content:

```shell
$ git clone --recurse-submodules https://github.com/fediverse-devnet/fedidevs.org.git
$ cd fedidevs.org
```

Note that the [theme](https://github.com/fediverse-devnet/fedidevs-hugo-theme.git) is a submodule, so you need to use `--recurse-submodules` to get it. If you do not, you'll likely see an error related to shortcode templates when you try to run the site. In this case, run `git submodule update --init --recursive` to synchronise the submodule content.

Run:

```shell
$ hugo server
```

Then go to `http://localhost:1313/` (actual port will be printed to the terminal).

## Making changes

If you are not familiar with Hugo, leave all files and directories alone except for what's in the `content/` directory. There, you'll find the Markup files that make up the content of the site.

By and large, there are two kinds of content files:

* Standard Markdown files, such as `content/foo/bar/baz.md`. This is a "leaf" node in the page hierarchy, i.e. it will have no child pages. The content will be at URL `http://localhost:1313/foo/bar/baz/`.

* Markdown files named with an underscore prefix `_index.md`, such as a `content/bar/foo/_index.md`. This is a "directory" node in the page hierarchy, i.e. it can have further child pages. It is a regular Markdown file whose content will be at URL `http://localhost:1313/bar/foo/`. It uses a different layout generation algorithm that automatically inserts links to its child pages.

## Intended structure of the site

This describes files below `content/`.

* Front page: Welcome, overview

* `notes/`: Notes from meetings

* `people/`: A table listing those who have chosen to be involved and identified as moving the project forward. Note that this is not an exclusive list, and we welcome contributors!

* `practices/`: A collection of practices that we consider useful. Not standards, but more tips and tricks how to best apply the standards to solve certain problems.

* `projects/`: Contains all information about Fediverse software projects, further subdivided by category.

* `projects/libraries/`: Information about Fediverse-related software libraries.

* `projects/server-apps/`: Information about Fediverse server-side applications.

* `projects/mobile-apps/`: Information about Fediverse mobile apps.

* `reference/`: Collection of reference information that is useful for development, such as an overview over how the ActivityPub actor files look for different server apps. Much content here is generated.

## Other directories

* `static/`: Static assets, such as images.

* `scripts/`: Scripts that generate content for the site.
