# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/)

The types of changes are:

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Developer Experience` for changes in developer workflow or tooling.
- `Deprecated` for soon-to-be removed features.
- `Removed` for now removed features.
- `Fixed` for any bug fixes.
- `Security` in case of vulnerabilities.

## [Unreleased](https://github.com/ethyca/fideslang/compare/2.1.0...main)

### Fixed

- Removed mistaken trailing `.` on some data category `name`s in the default taxonomy [#169](https://github.com/ethyca/fideslang/pull/169)


## [2.1.0](https://github.com/ethyca/fideslang/compare/2.0.4...2.1.0)

### Added 

- Added GVL mappings and utility functions [#167](https://github.com/ethyca/fideslang/pull/167)


## [2.0.4](https://github.com/ethyca/fideslang/compare/2.0.3...2.0.4)


### Changed

- Add Collection > Fides Meta > Skip Processing Flag to skip collections in DSR processing [#165](https://github.com/ethyca/fideslang/pull/165)


## [2.0.3](https://github.com/ethyca/fideslang/compare/2.0.2...2.0.3)

### Changed

- Relax system legal basis for transfer fields [#162](https://github.com/ethyca/fideslang/pull/162)


## [2.0.2](https://github.com/ethyca/fideslang/compare/2.0.1...2.0.2)

### Changed

- Update `system.legal_basis_for_profiling` and `system.legal_basis_for_transfers` fields [#156](https://github.com/ethyca/fideslang/pull/156)

## [2.0.1](https://github.com/ethyca/fideslang/compare/2.0.0...2.0.1)

### Changed

- Fix validation around the new FidesVersion type [#151](https://github.com/ethyca/fideslang/pull/151)

### Fixed

- Fix docs site for fideslang 2.0.0 [#154](https://github.com/ethyca/fideslang/pull/154)

## [2.0.0](https://github.com/ethyca/fideslang/compare/1.4.4...2.0.0)

### Changed

- Updated the Data Categories and Data Uses to support GVL [#144](https://github.com/ethyca/fideslang/pull/144)
- Add version metadata to the default taxonomy items [#147](https://github.com/ethyca/fideslang/pull/147)


## [1.4.6 (Hotfix)](https://github.com/ethyca/fideslang/compare/1.4.5...1.4.6)

### Changed

- Relax system legal basis for transfer fields [#162](https://github.com/ethyca/fideslang/pull/162)


## [1.4.5 (Hotfix)](https://github.com/ethyca/fideslang/compare/1.4.4...1.4.5)

### Changed

- Update `system.legal_basis_for_profiling` and `system.legal_basis_for_transfers` fields [#156](https://github.com/ethyca/fideslang/pull/156)

## [1.4.4](https://github.com/ethyca/fideslang/compare/1.4.3...1.4.4)

### Changed

- Add new fields to System and Privacy Declarations to support GVL [#146](https://github.com/ethyca/fideslang/pull/146)

### Added

- Add versioning metadata as fields on Taxonomy Data types [#147](https://github.com/ethyca/fideslang/pull/147)

### Changed

- Updated the Data Categories and Data Uses to support GVL [#144](https://github.com/ethyca/fideslang/pull/144)

### Fixed

- Don't allow duplicate entries for DatasetCollections as part of Datasets [#136](https://github.com/ethyca/fideslang/pull/136)
- Cython/PyYAML versions breaking builds [#145](https://github.com/ethyca/fideslang/pull/145)

## [1.4.3](https://github.com/ethyca/fideslang/compare/1.4.2...1.4.3)

### Changed

- Consolidate Python build tooling into `pyproject.toml` [#135](https://github.com/ethyca/fideslang/pull/135)

## [1.4.2](https://github.com/ethyca/fideslang/compare/1.4.1...1.4.2)

### Added

- Support Pydantic <1.11 [#122] (https://github.com/ethyca/fideslang/pull/122)

### Changed

- Add `Cookies` schema and similar property to `PrivacyDeclaration` [#115](https://github.com/ethyca/fideslang/pull/115)

### Fixed

- Fix Fideslang visual explorer on docs site [#123](https://github.com/ethyca/fideslang/pull/123)
- Fix Fideslang key finding function [#131](https://github.com/ethyca/fideslang/pull/131)

### Developer Experience

- Allow Docker to select plaform [#121] https://github.com/ethyca/fideslang/pull/121
- Use build time versioneer [#120] https://github.com/ethyca/fideslang/pull/120

## [1.4.1](https://github.com/ethyca/fideslang/compare/1.4.0...1.4.1)

### Changed

- Make `meta` property of `System` and `Dataset` models more permissive [#113](https://github.com/ethyca/fideslang/pull/113)

## [1.4.0](https://github.com/ethyca/fideslang/compare/1.3.4...1.4.0)

### Changed

- Updated the default data uses [#107](https://github.com/ethyca/fideslang/pull/107)

### Removed

- The `system_dependencies` field of `System` resources [#105](https://github.com/ethyca/fideslang/pull/105)

## [1.3.4](https://github.com/ethyca/fideslang/compare/1.3.3...1.3.4)

### Changed

- Make `PrivacyDeclaration` use pydantic `orm_mode` [#101](https://github.com/ethyca/fideslang/pull/101)

## [1.3.3](https://github.com/ethyca/fideslang/compare/1.3.2...1.3.3)

### Changed

- Make `PrivacyDeclation.name` optional [#97](https://github.com/ethyca/fideslang/pull/97)

## [1.3.2](https://github.com/ethyca/fideslang/compare/1.3.1...1.3.2)

### Changed

- Update css to brand colors, edit footer [#87](https://github.com/ethyca/fideslang/pull/87)
- Moved over DSR concepts into Fideslang. Expanded allowable characters for FideKey and added additional Dataset validation. [#95](https://github.com/ethyca/fideslang/pull/95)
- Docs css and link updates [#93](https://github.com/ethyca/fideslang/pull/93)

## [1.3.1](https://github.com/ethyca/fideslang/compare/1.3.0...1.3.1)

### Fixed

- `DataFlow` resource models included in `System` resource models are now exported to valid YAML [#89](https://github.com/ethyca/fideslang/pull/89)

## [1.3.0](https://github.com/ethyca/fideslang/compare/1.2.0...1.3.0)

### Added

- The `DataFlow` resource model defines a resource with which a `System` resource may communicate [#85](https://github.com/ethyca/fideslang/pull/85)
- `PrivacyDeclaration`s may define `egress` and `ingress`, to contextualize communications with other resources [#85](https://github.com/ethyca/fideslang/pull/85)

### Deprecated

- The `dataset_references` field of `PrivacyDeclaration` resources [#85](https://github.com/ethyca/fideslang/pull/85)
- The `system_dependencies` field of `System` resources [#85](https://github.com/ethyca/fideslang/pull/85)

### Developer Experience

- The `DataFlow` resource model is exposed when importing `fideslang` [#85](https://github.com/ethyca/fideslang/pull/85)

### Docs

- Updated the brand colors and footer on the docs site [#87](https://github.com/ethyca/fideslang/pull/87)

### Fixed

- Fixed broken links in docs [#74](https://github.com/ethyca/fideslang/pull/74)
- Pydantic 1.10.0 was causing issues so specified the pydantic version needs to be less than 1.10.0 [#79](https://github.com/ethyca/fideslang/pull/79)
- Resolved a circular import in `default_taxonomy.py` [#85](https://github.com/ethyca/fideslang/pull/85)

## [1.2.0](https://github.com/ethyca/fideslang/compare/1.1.0...1.2.0)

### Added

- New field `is_default` added to DataCategory, DataUse, DataSubject, and DataQualifier [#68](https://github.com/ethyca/fideslang/pull/68)
- Return invalid key values as part of the stack trace for easier debugging [#55](https://github.com/ethyca/fideslang/pull/55)

### Docs

- Updated documentation for new Data Category and Use taxonomy [#69](https://github.com/ethyca/fideslang/pull/69)

### Changed

- Docker images now use Debian `bullseye` instead of `buster`

### Fixed

- Add setuptools to dev-requirements to fix versioneer error [#72](https://github.com/ethyca/fideslang/pull/72)

## 1.1.0

### Changed

- Simplification of Data Categories and Data Uses [#62](https://github.com/ethyca/fideslang/pull/62)

## 1.0.0

### Added

- There is now a `tags` field on the `FidesModel` model [#45](https://github.com/ethyca/fideslang/pull/45)
- Add DatasetFieldBase model [#49](https://github.com/ethyca/fideslang/pull/49)

## 0.9.0

### Added

- Created the fideslang standalone python module

### Developer Experience

- Added a py.typed file
