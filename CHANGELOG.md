# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/)

The types of changes are:

* `Added` for new features.
* `Changed` for changes in existing functionality.
* `Developer Experience` for changes in developer workflow or tooling.
* `Deprecated` for soon-to-be removed features.
* `Removed` for now removed features.
* `Fixed` for any bug fixes.
* `Security` in case of vulnerabilities.

## [Unreleased](https://github.com/ethyca/fideslang/compare/1.1.0...main)

### Fixed

* Fixed broken links in docs [#74](https://github.com/ethyca/fideslang/pull/74)

## [1.2.0](https://github.com/ethyca/fideslang/compare/1.1.0...1.2.0)

### Added

* New field `is_default` added to DataCategory, DataUse, DataSubject, and DataQualifier [#68](https://github.com/ethyca/fideslang/pull/68)
* Return invalid key values as part of the stack trace for easier debugging [#55](https://github.com/ethyca/fideslang/pull/55)

### Docs

* Updated documentation for new Data Category and Use taxonomy [#69](https://github.com/ethyca/fideslang/pull/69)

### Changed

* Docker images now use Debian `bullseye` instead of `buster`

### Fixed

* Add setuptools to dev-requirements to fix versioneer error [#72](https://github.com/ethyca/fideslang/pull/72)

## 1.1.0

### Changed

* Simplification of Data Categories and Data Uses [#62](https://github.com/ethyca/fideslang/pull/62)

## 1.0.0

### Added

* There is now a `tags` field on the `FidesModel` model [#45](https://github.com/ethyca/fideslang/pull/45)
* Add DatasetFieldBase model [#49](https://github.com/ethyca/fideslang/pull/49)

## 0.9.0

### Added

* Created the fideslang standalone python module

### Developer Experience

* Added a py.typed file
